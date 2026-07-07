from pathlib import Path
import argparse
import csv
import shutil

from common import fail, load_config
from run_wall_case import (
    execute,
    append_summary,
    repair_wall_shape,
    safety,
    stats,
)

ROOT = Path(__file__).resolve().parents[1]


def find_reference_top(summary: Path, start_stage: str, start_gro: Path) -> float:
    """Recover the displacement reference used by PULL_RUN_SUMMARY.csv.

    Prefer the row of the requested start stage.  If the summary is unavailable,
    use the current GTOP mean as reference so that appended rows remain valid
    but displacement will be relative to the resume point.
    """
    if not summary.exists():
        values = stats(start_gro)
        print("WARNING: PULL_RUN_SUMMARY.csv not found; displacement will be relative to resume stage.")
        return float(values["top_mean_z_nm"])

    rows = list(csv.DictReader(summary.open("r", encoding="utf-8")))
    if not rows:
        values = stats(start_gro)
        print("WARNING: PULL_RUN_SUMMARY.csv is empty; displacement will be relative to resume stage.")
        return float(values["top_mean_z_nm"])

    # First try exact stage row, then any row containing the stage name, then latest row.
    chosen = None
    for row in rows:
        label = row.get("label", "")
        if label == start_stage or label == start_stage + "_no_coordinate_repair":
            chosen = row
    if chosen is None:
        for row in rows:
            if start_stage in row.get("label", ""):
                chosen = row
    if chosen is None:
        chosen = rows[-1]
        print("WARNING: start stage row not found in summary; using last summary row to recover reference.")

    try:
        return float(chosen["top_mean_z_nm"]) - float(chosen.get("top_displacement_nm", 0.0))
    except Exception:
        values = stats(start_gro)
        print("WARNING: could not recover reference from summary; displacement will be relative to resume stage.")
        return float(values["top_mean_z_nm"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Continue one existing wall case from a completed pressure stage and run only the remaining annealing/NVT stages.")
    parser.add_argument("case", help="Case name, e.g. RMS_0p300")
    parser.add_argument("--from-stage", default="02_pull_ramp_03_60MPa", help="Completed stage basename without .gro")
    parser.add_argument("--run-annealing", action="store_true", default=True, help="Run 03_pull_stage_*.mdp after the completed stage")
    parser.add_argument("--no-annealing", dest="run_annealing", action="store_false")
    args = parser.parse_args()

    cfg = load_config(ROOT)
    case = ROOT / "02_GRAPHENE_CASES" / args.case
    if not case.exists():
        fail(f"Case not found: {case}")
    mdp_dir = case / "01_MDP"
    work = case / "02_RUN"
    template_gro = work / "system_initial.gro"
    if not template_gro.exists():
        fail(f"Missing {template_gro}. Do not rebuild; copy initial files or rerun case construction first.")

    start_gro = work / f"{args.from_stage}.gro"
    start_cpt = work / f"{args.from_stage}.cpt"
    if not start_gro.exists():
        fail(f"Resume point missing: {start_gro}. Confirm RMS_0p300 finished {args.from_stage}.")

    summary = work / "PULL_RUN_SUMMARY.csv"
    reference_top = find_reference_top(summary, args.from_stage, start_gro)
    current = start_gro
    checkpoint = start_cpt if start_cpt.exists() else None
    current_values = append_summary(summary, f"resume_from_{args.from_stage}", current, reference_top)

    mdps = sorted(mdp_dir.glob("03_pull_stage_*.mdp")) if args.run_annealing else []
    if not mdps:
        print("No 03_pull_stage_*.mdp files to run; final structure will be copied from resume point.")
    for mdp in mdps:
        previous = current_values
        name = mdp.stem
        print("CONTINUE STAGE:", args.case, name)
        current, checkpoint = execute(
            cfg,
            work,
            mdp,
            current,
            name,
            checkpoint,
            pulling=True,
        )
        repair_wall_shape(current, template_gro, cfg, name, allow_top_translation=True)
        checkpoint = None
        current_values = append_summary(summary, name + "_resume_no_coordinate_repair", current, reference_top)
        safety(cfg, previous, current_values, pulling=True)

    final = work / "final_structure_pull.gro"
    shutil.copy2(current, final)
    print("RESUME COMPLETED:", args.case)
    print("FINAL:", final)
    print("SUMMARY:", summary)


if __name__ == "__main__":
    main()
