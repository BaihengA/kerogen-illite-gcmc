from pathlib import Path
import argparse
import csv
import json
import math
import shutil

from common import load_config, read_gro, write_gro, read_itp_atoms, fail

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ["RMS_0p000", "RMS_0p300", "RMS_0p600", "RMS_0p900"]
GRAPHENE_RESNAMES = {"GBOT", "GTOP", "GXMN", "GXMX", "GYMN", "GYMX"}


def percentile(values, p):
    if not values:
        return 0.0
    values = sorted(values)
    idx = int(round((len(values) - 1) * p))
    return values[max(0, min(len(values) - 1, idx))]


def molecule_chunks(atoms, atoms_per_mol):
    if atoms_per_mol <= 0:
        yield atoms
        return
    if len(atoms) % atoms_per_mol != 0:
        print(f"WARNING: KERO atom count {len(atoms)} is not divisible by atoms_per_mol={atoms_per_mol}; writing as one block.")
        yield atoms
        return
    for i in range(0, len(atoms), atoms_per_mol):
        yield atoms[i:i + atoms_per_mol]


def find_latest_source(run_dir: Path) -> Path | None:
    priority_names = [
        "final_structure_pull.gro",
        "03_pull_stage_02_500K_chunk01_50ps.gro",
        "03_pull_stage_01_700K_chunk01_50ps.gro",
        "02_pull_ramp_04_80MPa.gro",
        "02_pull_ramp_03_60MPa.gro",
        "02_pull_ramp_02_40MPa.gro",
        "02_pull_ramp_01_20MPa.gro",
    ]
    for name in priority_names:
        p = run_dir / name
        if p.exists():
            return p
    candidates = sorted(run_dir.glob("*.gro"), key=lambda x: x.stat().st_mtime)
    if not candidates:
        return None
    # Prefer later pull/anneal files, otherwise latest gro.
    scored = []
    for p in candidates:
        name = p.name
        score = 0
        if name.startswith("03_pull_stage_"):
            score = 300
        elif name.startswith("02_pull_ramp_"):
            score = 200
        elif name.startswith("01_wall_nvt"):
            score = 100
        elif name.startswith("00_em"):
            score = 50
        scored.append((score, p.stat().st_mtime, p))
    return sorted(scored)[-1][2]


def read_target_footprint(case_dir: Path, atoms):
    meta_path = case_dir / "CASE_METADATA.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        geom = meta.get("wall_geometry_nm", {})
        if geom:
            x0 = float(geom.get("target_x0", geom.get("x0", 0.0)))
            x1 = float(geom.get("target_x1", geom.get("x1", 0.0)))
            y0 = float(geom.get("target_y0", geom.get("y0", 0.0)))
            y1 = float(geom.get("target_y1", geom.get("y1", 0.0)))
            if x1 > x0 and y1 > y0:
                return x0, x1, y0, y1, "CASE_METADATA target footprint"
    xs = [a["x"] for a in atoms]
    ys = [a["y"] for a in atoms]
    return min(xs), max(xs), min(ys), max(ys), "KERO atom extent fallback"


def wrap_molecule_xy(mol, lx, ly):
    cx = sum(a["x"] for a in mol) / len(mol)
    cy = sum(a["y"] for a in mol) / len(mol)
    sx = -math.floor(cx / lx) * lx if lx > 0 else 0.0
    sy = -math.floor(cy / ly) * ly if ly > 0 else 0.0
    out = []
    for a in mol:
        b = dict(a)
        b["x"] += sx
        b["y"] += sy
        out.append(b)
    return out


def make_metrics(case, source, output, kero, box, mode, footprint_note=""):
    xs, ys, zs = [a["x"] for a in kero], [a["y"] for a in kero], [a["z"] for a in kero]
    return {
        "case": case,
        "mode": mode,
        "source_gro": str(source),
        "output_gro": str(output),
        "atom_count": len(kero),
        "box_x_nm": box[0] if box else 0.0,
        "box_y_nm": box[1] if box else 0.0,
        "box_z_nm": box[2] if box else 0.0,
        "kero_min_x_nm": min(xs),
        "kero_max_x_nm": max(xs),
        "kero_length_x_nm": max(xs) - min(xs),
        "kero_min_y_nm": min(ys),
        "kero_max_y_nm": max(ys),
        "kero_width_y_nm": max(ys) - min(ys),
        "kero_min_z_nm": min(zs),
        "kero_max_z_nm": max(zs),
        "kero_total_thickness_nm": max(zs) - min(zs),
        "kero_p05_z_nm": percentile(zs, 0.05),
        "kero_p50_z_nm": percentile(zs, 0.50),
        "kero_p95_z_nm": percentile(zs, 0.95),
        "kero_90pct_thickness_nm": percentile(zs, 0.95) - percentile(zs, 0.05),
        "footprint_note": footprint_note,
    }


def write_raw(case_name, source, title, atoms, box, out_root):
    kero = [a for a in atoms if a["resname"].lower() == "kero"]
    if not kero:
        fail(f"No KERO atoms found in {source}")
    mols = [("kero", [{"name": a["atomname"], "x": a["x"], "y": a["y"], "z": a["z"]} for a in kero])]
    out_root.mkdir(parents=True, exist_ok=True)
    out = out_root / f"{case_name}_kerogen_only_raw_from_final.gro"
    write_gro(out, f"{case_name} KERO only; graphene removed from {source.name}", mols, box)
    return out, make_metrics(case_name, source, out, kero, box, "raw_keep_coordinates")


def write_standard(case_name, case_dir, source, atoms, cfg, out_root):
    kero = [a for a in atoms if a["resname"].lower() == "kero"]
    if not kero:
        fail(f"No KERO atoms found in {source}")
    x0, x1, y0, y1, note = read_target_footprint(case_dir, kero)
    lx, ly = x1 - x0, y1 - y0
    if lx <= 0 or ly <= 0:
        fail(f"Bad target footprint for {case_name}: x0={x0}, x1={x1}, y0={y0}, y1={y1}")
    itp_atoms = read_itp_atoms(ROOT / "00_INPUT" / "kero.itp")
    atoms_per_mol = len(itp_atoms)
    shifted = []
    for a in kero:
        b = dict(a)
        b["x"] -= x0
        b["y"] -= y0
        shifted.append(b)
    wrapped = []
    for mol in molecule_chunks(shifted, atoms_per_mol):
        wrapped.extend(wrap_molecule_xy(mol, lx, ly))
    zs = [a["z"] for a in wrapped]
    bottom_pad = float(cfg.get("kerogen_only_output", {}).get("bottom_padding_nm", 1.5))
    top_pad = float(cfg.get("kerogen_only_output", {}).get("top_padding_nm", 3.0))
    zmin = min(zs)
    for a in wrapped:
        a["z"] = a["z"] - zmin + bottom_pad
    new_zs = [a["z"] for a in wrapped]
    box_z = max(new_zs) + top_pad
    mols = []
    for mol in molecule_chunks(wrapped, atoms_per_mol):
        mols.append(("kero", [{"name": a["atomname"], "x": a["x"], "y": a["y"], "z": a["z"]} for a in mol]))
    out_root.mkdir(parents=True, exist_ok=True)
    out = out_root / f"{case_name}_kerogen_only_standard_plate.gro"
    write_gro(out, f"{case_name} standardized KERO-only plate; graphene removed from {source.name}", mols, [lx, ly, box_z])
    return out, make_metrics(case_name, source, out, wrapped, [lx, ly, box_z], "standardized_fixed_footprint", note)


def copy_forcefield_files(out_root: Path):
    for name in ["kero.itp", "kero_ATP.itp", "kero.top"]:
        src = ROOT / "00_INPUT" / name
        if src.exists():
            shutil.copy2(src, out_root / name)


def main():
    parser = argparse.ArgumentParser(description="Remove all graphene walls and output KERO-only final plates.")
    parser.add_argument("--cases", default=",".join(DEFAULT_CASES), help="Comma-separated cases, e.g. RMS_0p000,RMS_0p300")
    parser.add_argument("--source", default="auto", help="Source gro name inside 02_RUN, or auto")
    parser.add_argument("--raw", action="store_true", help="Write raw KERO-only coordinates in the original simulation box.")
    parser.add_argument("--standard", action="store_true", help="Write standardized KERO-only plate using CASE_METADATA target footprint.")
    args = parser.parse_args()
    cfg = load_config(ROOT)
    if not args.raw and not args.standard:
        args.raw = True
        args.standard = True
    cases = [c.strip() for c in args.cases.replace(';', ',').split(',') if c.strip()]
    out_root = ROOT / "KEROGEN_ONLY_FINALS"
    raw_root = out_root / "RAW_KEEP_COORDINATES"
    std_root = out_root / "STANDARD_PLATES"
    all_metrics = []
    for case_name in cases:
        case_dir = ROOT / "02_GRAPHENE_CASES" / case_name
        run_dir = case_dir / "02_RUN"
        if not run_dir.exists():
            print(f"SKIP {case_name}: missing {run_dir}")
            continue
        source = run_dir / args.source if args.source != "auto" else find_latest_source(run_dir)
        if source is None or not source.exists():
            print(f"SKIP {case_name}: no source gro found in {run_dir}")
            continue
        title, atoms, box = read_gro(source)
        print(f"{case_name}: removing graphene from {source.name}")
        if args.raw:
            out, m = write_raw(case_name, source, title, atoms, box, raw_root)
            all_metrics.append(m)
        if args.standard:
            out, m = write_standard(case_name, case_dir, source, atoms, cfg, std_root)
            all_metrics.append(m)
        copy_forcefield_files(out_root)
    if all_metrics:
        keys = sorted({k for m in all_metrics for k in m.keys()})
        csv_path = out_root / "KEROGEN_ONLY_FINALS_METRICS.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for m in all_metrics:
                writer.writerow(m)
        print("METRICS:", csv_path)
    print("KEROGEN-ONLY EXTRACTION COMPLETED:", out_root)


if __name__ == "__main__":
    main()
