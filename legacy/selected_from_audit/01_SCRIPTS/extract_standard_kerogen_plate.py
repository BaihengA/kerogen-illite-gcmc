from pathlib import Path
import argparse
import csv
import json
import math
import shutil

from common import load_config, read_gro, write_gro, fail, read_itp_atoms

ROOT = Path(__file__).resolve().parents[1]


def percentile(values, p):
    if not values:
        return 0.0
    values = sorted(values)
    idx = int(round((len(values) - 1) * p))
    return values[max(0, min(len(values) - 1, idx))]


def molecule_chunks(atoms, atoms_per_mol):
    if len(atoms) % atoms_per_mol != 0:
        fail(f"KERO atom count {len(atoms)} is not divisible by atoms_per_mol={atoms_per_mol}")
    for i in range(0, len(atoms), atoms_per_mol):
        yield atoms[i:i + atoms_per_mol]


def wrap_molecule_xy(mol, lx, ly):
    cx = sum(a["x"] for a in mol) / len(mol)
    cy = sum(a["y"] for a in mol) / len(mol)
    sx = -math.floor(cx / lx) * lx
    sy = -math.floor(cy / ly) * ly
    out = []
    for a in mol:
        b = dict(a)
        b["x"] += sx
        b["y"] += sy
        out.append(b)
    return out


def surface_grid_metrics(atoms, lx, ly, nx, ny):
    bins = [[None for _ in range(ny)] for _ in range(nx)]
    for a in atoms:
        x = a["x"] % lx
        y = a["y"] % ly
        ix = min(nx - 1, max(0, int(x / lx * nx)))
        iy = min(ny - 1, max(0, int(y / ly * ny)))
        z = a["z"]
        if bins[ix][iy] is None or z > bins[ix][iy]:
            bins[ix][iy] = z
    vals = [bins[i][j] for i in range(nx) for j in range(ny) if bins[i][j] is not None]
    coverage = len(vals) / float(nx * ny)
    if not vals:
        return {"surface_grid_coverage": 0.0}
    mean_z = sum(vals) / len(vals)
    rms = math.sqrt(sum((v - mean_z) ** 2 for v in vals) / len(vals))
    return {
        "surface_grid_coverage": coverage,
        "surface_grid_top_mean_z_nm": mean_z,
        "surface_grid_top_min_z_nm": min(vals),
        "surface_grid_top_max_z_nm": max(vals),
        "surface_grid_top_rms_nm": rms,
        "surface_grid_top_peak_to_valley_nm": max(vals) - min(vals),
        "surface_grid_bins_used": len(vals),
        "surface_grid_bins_total": nx * ny,
    }


def write_topology_for_kero_only(path: Path, original_top: Path, molecule_name: str, molecule_count: int):
    lines = []
    for line in original_top.read_text(errors="ignore").splitlines():
        if line.strip().lower().startswith("[ system"):
            break
        lines.append(line)
    lines += [
        "",
        "[ system ]",
        "standardized rough kerogen plate only",
        "",
        "[ molecules ]",
        f"{molecule_name} {molecule_count}",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="ascii")


def make_pbc_view_molecules(mols, lx, ly, box_z):
    """Return a 3x3 periodic visualization copy.

    This file is NOT for production MD. It lets the user see whether apparent
    empty zones are only caused by whole molecules crossing the xy boundary.
    """
    view = []
    for sx in (-lx, 0.0, lx):
        for sy in (-ly, 0.0, ly):
            for resname, atoms in mols:
                shifted = []
                for a in atoms:
                    b = dict(a)
                    b["x"] = a["x"] + sx + lx
                    b["y"] = a["y"] + sy + ly
                    shifted.append(b)
                view.append((resname, shifted))
    return view, [3.0 * lx, 3.0 * ly, box_z]


def read_moleculetype(path: Path) -> str:
    section = None
    for line in path.read_text(errors="ignore").splitlines():
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            section = stripped.strip("[] ").lower()
            continue
        if section == "moleculetype" and stripped and not stripped.startswith(";"):
            return stripped.split()[0]
    fail(f"Cannot read moleculetype from {path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("case", nargs="?", default="RMS_0p300")
    parser.add_argument("--input", default="final_structure_pull.gro")
    args = parser.parse_args()

    cfg = load_config(ROOT)
    case = ROOT / "02_GRAPHENE_CASES" / args.case
    run = case / "02_RUN"
    meta_path = case / "CASE_METADATA.json"
    if not meta_path.exists():
        fail(f"Missing CASE_METADATA.json for {args.case}")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    input_gro = run / args.input
    if not input_gro.exists():
        # Fall back to the last gro generated if final_structure_pull is absent.
        candidates = sorted(run.glob("*.gro"), key=lambda p: p.stat().st_mtime)
        if not candidates:
            fail(f"No GRO file found in {run}")
        input_gro = candidates[-1]

    title, atoms, _box = read_gro(input_gro)
    kero = [a for a in atoms if a["resname"].lower() == "kero"]
    if not kero:
        fail(f"No KERO atoms found in {input_gro}")

    itp_atoms = read_itp_atoms(ROOT / "00_INPUT" / "kero.itp")
    atoms_per_mol = len(itp_atoms)
    molecule_name = read_moleculetype(ROOT / "00_INPUT" / "kero.itp")

    geom = meta["wall_geometry_nm"]
    # Patch v15: extract the fixed final plate footprint, not the larger guarded mold.
    x0 = float(geom.get("target_x0", geom["x0"]))
    y0 = float(geom.get("target_y0", geom["y0"]))
    x1 = float(geom.get("target_x1", geom["x1"]))
    y1 = float(geom.get("target_y1", geom["y1"]))
    lx, ly = x1 - x0, y1 - y0
    sp = cfg.get("standard_kerogen_plate", {})
    bottom_pad = float(sp.get("output_bottom_padding_nm", 1.5))
    top_pad = float(sp.get("output_top_padding_nm", 3.0))
    fixed_box_z = sp.get("output_box_z_nm", None)

    # Translate fixed mold origin to (0,0). Keep molecule integrity and wrap by COM in xy.
    shifted = []
    for a in kero:
        b = dict(a)
        b["x"] -= x0
        b["y"] -= y0
        shifted.append(b)

    wrapped = []
    for mol in molecule_chunks(shifted, atoms_per_mol):
        wrapped.extend(wrap_molecule_xy(mol, lx, ly))

    z_values = [a["z"] for a in wrapped]
    z_min = min(z_values)
    z_max = max(z_values)
    for a in wrapped:
        a["z"] = a["z"] - z_min + bottom_pad
    new_z_values = [a["z"] for a in wrapped]
    thickness = max(new_z_values) - min(new_z_values)
    if fixed_box_z is None:
        box_z = bottom_pad + thickness + top_pad
    else:
        box_z = float(fixed_box_z)
        if box_z < bottom_pad + thickness + 0.5:
            print(f"WARNING: output_box_z_nm={box_z:.3f} is too small for plate thickness {thickness:.3f}; increasing automatically.")
            box_z = bottom_pad + thickness + top_pad

    # Re-number and normalize atom fields for write_gro.
    mols = []
    for mol in molecule_chunks(wrapped, atoms_per_mol):
        outmol = []
        for a in mol:
            outmol.append({"name": a["atomname"], "x": a["x"], "y": a["y"], "z": a["z"]})
        mols.append(("kero", outmol))

    output_dir = run / "STANDARD_KEROGEN_PLATE"
    output_dir.mkdir(exist_ok=True)
    output_gro = output_dir / f"{args.case}_standard_kerogen_plate.gro"
    write_gro(output_gro, f"{args.case} standardized fixed-footprint rough kerogen plate from {input_gro.name}", mols, [lx, ly, box_z])

    pbc_view_gro = ""
    if bool(sp.get("output_periodic_view_3x3", True)):
        view_mols, view_box = make_pbc_view_molecules(mols, lx, ly, box_z)
        pbc_view_path = output_dir / f"{args.case}_standard_kerogen_plate_PBC_VIEW_3x3.gro"
        write_gro(pbc_view_path, f"{args.case} 3x3 PBC visualization only; do not use for production MD", view_mols, view_box)
        pbc_view_gro = str(pbc_view_path)

    shutil.copy2(ROOT / "00_INPUT" / "kero.itp", output_dir / "kero.itp")
    if (ROOT / "00_INPUT" / "kero_ATP.itp").exists():
        shutil.copy2(ROOT / "00_INPUT" / "kero_ATP.itp", output_dir / "kero_ATP.itp")
    write_topology_for_kero_only(output_dir / "topol.top", ROOT / "00_INPUT" / "kero.top", molecule_name, len(mols))

    p05 = percentile(new_z_values, 0.05)
    p50 = percentile(new_z_values, 0.50)
    p95 = percentile(new_z_values, 0.95)
    grid = surface_grid_metrics(wrapped, lx, ly, int(sp.get("surface_grid_nx", 40)), int(sp.get("surface_grid_ny", 40)))
    metrics = {
        "case": args.case,
        "source_gro": str(input_gro),
        "output_gro": str(output_gro),
        "pbc_view_3x3_gro": pbc_view_gro,
        "plate_length_x_nm": lx,
        "plate_width_y_nm": ly,
        "output_box_z_nm": box_z,
        "kerogen_molecule_count": len(mols),
        "kerogen_atom_count": len(wrapped),
        "kerogen_min_z_nm": min(new_z_values),
        "kerogen_max_z_nm": max(new_z_values),
        "kerogen_total_thickness_nm": thickness,
        "kerogen_p05_z_nm": p05,
        "kerogen_p50_z_nm": p50,
        "kerogen_p95_z_nm": p95,
        "kerogen_90pct_thickness_nm": p95 - p05,
        **grid,
    }
    metrics_json = output_dir / f"{args.case}_standard_kerogen_plate_metrics.json"
    metrics_json.write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")

    csv_path = output_dir / f"{args.case}_standard_kerogen_plate_metrics.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(metrics.keys())
        writer.writerow(metrics.values())

    print(json.dumps(metrics, ensure_ascii=False, indent=2))
    print("STANDARD KEROGEN PLATE WRITTEN:", output_gro)


if __name__ == "__main__":
    main()
