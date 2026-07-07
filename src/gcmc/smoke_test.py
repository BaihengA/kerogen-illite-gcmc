from __future__ import annotations

import json
import subprocess
from pathlib import Path

from workflow_common import CODEBASE, PROJECT_ROOT, require_ready_for_smoke

REPORT = CODEBASE / "docs" / "audit" / "RMS_0p300_SMOKE_TEST.md"
GENERATED = CODEBASE / "workflows" / "08_gcmc_ch4_h2o" / "generated" / "RMS_0p300" / "P20MPa"


def main() -> int:
    gate = require_ready_for_smoke()
    if gate:
        REPORT.write_text("# RMS_0p300 Smoke Test\n\nstatus: BLOCKED\n\nReadiness gates did not permit smoke execution.\n", encoding="utf-8")
        return gate
    sim = GENERATED / "simulation.input"
    required = [
        sim,
        GENERATED / "force_field_mixing_rules.def",
        GENERATED / "pseudo_atoms.def",
        GENERATED / "force_field.def",
        GENERATED / "H2O.def",
        GENERATED / "RMS_0p300_Pore8nm.cif",
    ]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        REPORT.write_text(
            "# RMS_0p300 Smoke Test\n\n"
            "status: FAIL\n\n"
            "RASPA execution was not started because the canonical run directory is incomplete.\n\n"
            "Missing files:\n" + "\n".join(f"- {x}" for x in missing) + "\n\n"
            "This is a smoke-test failure, not a production result.\n",
            encoding="utf-8",
        )
        return 3
    paths = json.loads((CODEBASE / "config" / "paths.json").read_text(encoding="utf-8"))
    cmd = [
        "wsl", "-d", paths["wsl_distro"], "--", "bash", "-lc",
        f"cd '{GENERATED.as_posix()}' && RASPA_DIR='{paths['raspa2_root']}' '{paths['raspa2_simulate']}'",
    ]
    proc = subprocess.run(cmd, cwd=str(PROJECT_ROOT), text=True, capture_output=True, timeout=120)
    fatal = "fatal" in (proc.stdout + proc.stderr).lower()
    status = "PASS" if proc.returncode == 0 and not fatal else "FAIL"
    REPORT.write_text(
        "# RMS_0p300 Smoke Test\n\n"
        f"status: {status}\n\n"
        f"exit_code: {proc.returncode}\n\n"
        f"fatal_detected: {fatal}\n\n"
        "This short smoke test is not a production GCMC result.\n",
        encoding="utf-8",
    )
    return 0 if status == "PASS" else 4


raise SystemExit(main())
