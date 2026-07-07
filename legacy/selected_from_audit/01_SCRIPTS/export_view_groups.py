from pathlib import Path
import argparse
import json
import math
import shutil

from common import fail, load_config, read_gro

ROOT = Path(__file__).resolve().parents[1]
WALLS = {"GBOT", "GTOP", "GXMN", "GXMX", "GYMN", "GYMX"}


def write_selected_gro(path: Path, title: str, atoms: list[dict], box: list[float]) -> None:
    with path.open("w", encoding="ascii") as handle:
        handle.write(title[:120] + "\n")
        handle.write(f"{len(atoms)}\n")
        for idx, atom in enumerate(atoms, start=1):
            # Renumber atoms only for clean visualization files.  Coordinates are not changed.
            handle.write(
                f"{int(atom['resid'])%100000:5d}{atom['resname'][:5]:<5s}"
                f"{atom['atomname'][:5]:>5s}{idx%100000:5d}"
                f"{atom['x']:8.3f}{atom['y']:8.3f}{atom['z']:8.3f}\n"
            )
        handle.write("".join(f"{value:10.5f}" for value in box[:3]) + "\n")


def bbox(atoms: list[dict]) -> dict:
    if not atoms:
        return {}
    return {
        "count": len(atoms),
        "x_min_nm": min(a["x"] for a in atoms),
        "x_max_nm": max(a["x"] for a in atoms),
        "y_min_nm": min(a["y"] for a in atoms),
        "y_max_nm": max(a["y"] for a in atoms),
        "z_min_nm": min(a["z"] for a in atoms),
        "z_max_nm": max(a["z"] for a in atoms),
    }


def pick_input_gro(run_dir: Path) -> Path:
    preferred = [
        run_dir / "final_structure_pull.gro",
        run_dir / "03_pull_stage_01_900K_chunk01_100ps.gro",
        run_dir / "03_pull_stage_01_900K_100ps.gro",
        run_dir / "02_pull_ramp_02_10MPa.gro",
        run_dir / "02_pull_ramp_01_5MPa.gro",
        run_dir / "00_em.gro",
        run_dir / "system_initial.gro",
    ]
    for item in preferred:
        if item.exists():
            return item
    candidates = [p for p in run_dir.glob("*.gro") if not p.name.startswith("VIEW_")]
    if not candidates:
        fail(f"No GRO file found in {run_dir}")
    return max(candidates, key=lambda p: p.stat().st_mtime)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export clean visualization GRO files: GTOP only, walls only, kerogen only.")
    parser.add_argument("case", help="case name, e.g. RMS_0p300")
    parser.add_argument("--gro", default="", help="optional explicit GRO path")
    args = parser.parse_args()

    case = ROOT / "02_GRAPHENE_CASES" / args.case
    run_dir = case / "02_RUN"
    if args.gro:
        source = Path(args.gro)
    else:
        source = pick_input_gro(run_dir)
    if not source.exists():
        fail(f"GRO file not found: {source}")

    title, atoms, box = read_gro(source)
    groups = {
        "VIEW_GTOP_ONLY.gro": [a for a in atoms if a["resname"] == "GTOP"],
        "VIEW_ALL_WALLS_ONLY.gro": [a for a in atoms if a["resname"] in WALLS],
        "VIEW_KERO_ONLY.gro": [a for a in atoms if a["resname"].lower() == "kero"],
    }

    report = {"source_gro": str(source), "box_nm": box, "groups": {}}
    for filename, selected in groups.items():
        if not selected:
            continue
        out = run_dir / filename
        write_selected_gro(out, f"{args.case} {filename} from {source.name}", selected, box)
        report["groups"][filename] = bbox(selected)
        print("WROTE", out)

    report_path = run_dir / "VIEW_GROUPS_REPORT.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("REPORT", report_path)
    if "VIEW_GTOP_ONLY.gro" in report["groups"]:
        g = report["groups"]["VIEW_GTOP_ONLY.gro"]
        print(
            "GTOP xy rectangle bbox:",
            f"x={g['x_min_nm']:.3f}-{g['x_max_nm']:.3f} nm,",
            f"y={g['y_min_nm']:.3f}-{g['y_max_nm']:.3f} nm,",
            f"z={g['z_min_nm']:.3f}-{g['z_max_nm']:.3f} nm",
        )


if __name__ == "__main__":
    main()
