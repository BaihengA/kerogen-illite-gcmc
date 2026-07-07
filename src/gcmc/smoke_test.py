from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

from run_materializer import RUN_DIR, materialize, stage_framework_into_raspa, win_to_wsl
from workflow_common import CODEBASE, PROJECT_ROOT, require_ready_for_smoke

REPORT = CODEBASE / "docs" / "audit" / "RMS_0P300_SMOKE_TEST_REPORT.md"
LEGACY_REPORT = CODEBASE / "docs" / "audit" / "RMS_0p300_SMOKE_TEST.md"
PREFLIGHT = RUN_DIR / "SMOKE_PREFLIGHT_REPORT.json"
DEFAULT_TIMEOUT_SECONDS = 300


def sha256_file(path: Path) -> str:
    import hashlib
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def check_roundtrip() -> bool:
    report = CODEBASE / "docs" / "audit" / "FUGACITY_ROUNDTRIP_VALIDATION.md"
    return report.exists() and "fugacity_mapping_status: PASS" in report.read_text(encoding="utf-8", errors="replace")


def check_wsl(paths: dict) -> dict:
    proc = subprocess.run(["wsl", "-d", paths["wsl_distro"], "--", "bash", "-lc", f"test -x '{paths['raspa2_simulate']}' && echo OK"], capture_output=True, timeout=30)
    stdout = proc.stdout.decode("utf-8", errors="replace")
    stderr = proc.stderr.decode("utf-8", errors="replace")
    return {"status": "PASS" if proc.returncode == 0 and "OK" in stdout else "FAIL", "stdout": stdout.strip(), "stderr": stderr.strip(), "exit_code": proc.returncode}


def preflight(paths: dict) -> dict:
    manifest = materialize(run_type="smoke")
    checks = []
    def add(name: str, ok: bool, detail: dict | None = None):
        checks.append({"name": name, "status": "PASS" if ok else "FAIL", "detail": detail or {}})

    manifest_path = RUN_DIR / "RUN_ASSET_MANIFEST.json"
    add("RUN_ASSET_MANIFEST", manifest.get("status") == "PASS" and manifest_path.exists(), {"path": str(manifest_path)})
    required = [
        ("simulation.input", RUN_DIR / "simulation.input", manifest["simulation_input"]["sha256"]),
        ("framework CIF", RUN_DIR / "RMS_0p300_Pore8nm.cif", manifest["framework"]["sha256"]),
        ("force_field_mixing_rules.def", RUN_DIR / "force_field_mixing_rules.def", manifest["local_forcefield"]["force_field_mixing_rules"]["sha256"]),
        ("pseudo_atoms.def", RUN_DIR / "pseudo_atoms.def", manifest["local_forcefield"]["pseudo_atoms"]["sha256"]),
        ("force_field.def", RUN_DIR / "force_field.def", manifest["local_forcefield"]["force_field"]["sha256"]),
        ("H2O.def", RUN_DIR / "H2O.def", manifest["water_definition"]["sha256"]),
    ]
    for label, path, expected in required:
        ok = path.exists() and sha256_file(path) == expected
        add(label, ok, {"path": str(path), "expected_sha256": expected, "actual_sha256": sha256_file(path) if path.exists() else None})
    add("methane.def resolvable", bool(manifest["methane_definition"].get("sha256")), manifest["methane_definition"])
    add("thermodynamic state PASS", (CODEBASE / "docs" / "provenance" / "THERMODYNAMIC_STATE.json").exists() and json.loads((CODEBASE / "docs" / "provenance" / "THERMODYNAMIC_STATE.json").read_text(encoding="utf-8")).get("status") == "PASS")
    add("fugacity roundtrip PASS", check_roundtrip())
    coverage = CODEBASE / "docs" / "audit" / "LOCAL_FORCEFIELD_COVERAGE.csv"
    add("all atom types covered", coverage.exists() and "FAIL" not in coverage.read_text(encoding="utf-8", errors="replace"), {"path": str(coverage)})
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    probe = RUN_DIR / ".write_probe"
    try:
        probe.write_text("ok", encoding="utf-8")
        probe.unlink()
        writable = True
    except OSError:
        writable = False
    add("run directory writable", writable, {"path": str(RUN_DIR)})
    wsl = check_wsl(paths)
    add("WSL and simulate executable", wsl["status"] == "PASS", wsl)
    framework_resolution = stage_framework_into_raspa(manifest)
    add("RASPA framework staged", framework_resolution["status"] == "PASS", framework_resolution)
    launch_allowed = all(c["status"] == "PASS" for c in checks)
    report = {"case": "RMS_0p300", "run_directory": str(RUN_DIR), "launch_allowed": "YES" if launch_allowed else "NO", "checks": checks}
    PREFLIGHT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main() -> int:
    gate = require_ready_for_smoke()
    if gate:
        REPORT.write_text("# RMS_0p300 Smoke Test\n\nstatus: BLOCKED\n\nReadiness gates did not permit smoke execution.\n", encoding="utf-8")
        return gate
    paths = json.loads((CODEBASE / "config" / "paths.json").read_text(encoding="utf-8"))
    pre = preflight(paths)
    if pre["launch_allowed"] != "YES":
        REPORT.write_text(
            "# RMS_0p300 Smoke Test\n\nstatus: FAIL\n\nsimulate_started: NO\n\n"
            f"preflight_report: {PREFLIGHT}\n\nThis is a smoke-test failure, not a production result.\n",
            encoding="utf-8",
        )
        LEGACY_REPORT.write_text(REPORT.read_text(encoding="utf-8"), encoding="utf-8")
        return 3
    run_wsl = win_to_wsl(RUN_DIR)
    cmd = [
        "wsl", "-d", paths["wsl_distro"], "--", "bash", "-lc",
        f"cd '{run_wsl}' && RASPA_DIR='{paths['raspa2_root']}' '{paths['raspa2_simulate']}'",
    ]
    timeout_seconds = int(os.environ.get("RASPA_SMOKE_TIMEOUT_SECONDS", DEFAULT_TIMEOUT_SECONDS))
    try:
        proc = subprocess.run(cmd, cwd=str(PROJECT_ROOT), capture_output=True, timeout=timeout_seconds)
        returncode = proc.returncode
        timed_out = False
        raw_stdout = proc.stdout
        raw_stderr = proc.stderr
    except subprocess.TimeoutExpired as exc:
        returncode = None
        timed_out = True
        raw_stdout = exc.stdout or b""
        raw_stderr = exc.stderr or b""
    stdout = raw_stdout.decode("utf-8", errors="replace")
    stderr = raw_stderr.decode("utf-8", errors="replace")
    (RUN_DIR / "stdout.txt").write_text(stdout, encoding="utf-8", errors="replace")
    (RUN_DIR / "stderr.txt").write_text(stderr, encoding="utf-8", errors="replace")
    fatal = "fatal" in (stdout + stderr).lower()
    output_exists = (RUN_DIR / "Output").exists()
    saw_ch4 = "Component 0" in stdout + stderr or "methane" in (stdout + stderr).lower()
    saw_h2o = "Component 1" in stdout + stderr or "h2o" in (stdout + stderr).lower()
    if timed_out:
        status = "FAIL_TIMEOUT"
    elif returncode == 139:
        status = "FAIL_SEGFAULT"
    elif "oom" in (stdout + stderr).lower() or "killed process" in (stdout + stderr).lower():
        status = "FAIL_OOM"
    elif returncode != 0:
        status = "FAIL_INPUT"
    else:
        status = "PASS" if not fatal and output_exists and saw_ch4 and saw_h2o else "FAIL_INCOMPLETE"
    REPORT.write_text(
        "# RMS_0p300 Smoke Test\n\n"
        f"status: {status}\n\n"
        "simulate_started: YES\n\n"
        f"exit_code: {returncode}\n\n"
        f"timed_out: {timed_out}\n\n"
        f"timeout_seconds: {timeout_seconds}\n\n"
        f"fatal_detected: {fatal}\n\n"
        f"output_exists: {output_exists}\n\n"
        f"ch4_component_detected: {saw_ch4}\n\n"
        f"h2o_component_detected: {saw_h2o}\n\n"
        f"stdout: {RUN_DIR / 'stdout.txt'}\n\n"
        f"stderr: {RUN_DIR / 'stderr.txt'}\n\n"
        "This short smoke test is not a production GCMC result.\n",
        encoding="utf-8",
    )
    LEGACY_REPORT.write_text(REPORT.read_text(encoding="utf-8"), encoding="utf-8")
    return 0 if status == "PASS" else 4


raise SystemExit(main())
