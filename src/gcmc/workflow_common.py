from __future__ import annotations
import json
import sys
from pathlib import Path

CODEBASE = Path(__file__).resolve().parents[2]
def load_paths() -> dict:
    for name in ("paths.local.json", "paths.json", "paths.example.json"):
        path = CODEBASE / "config" / name
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    return {}

PATHS = load_paths()
PROJECT_ROOT = Path(PATHS.get("project_root", CODEBASE.parent)).resolve()
READINESS = PROJECT_ROOT / "docs" / "audit" / "GCMC_READINESS_REPORT.md"

def readiness_text() -> str:
    return READINESS.read_text(encoding="utf-8", errors="replace") if READINESS.exists() else ""

def require_ready_for_smoke() -> int:
    text = readiness_text()
    if "water_lj_status: PASS" not in text or "thermodynamic_boundary_status: PASS" not in text:
        print("GCMC readiness blockers remain; smoke/production is not allowed.")
        print(f"See: {READINESS}")
        return 2
    return 0

def require_production_ready() -> int:
    text = readiness_text()
    if "production_ready: YES" not in text:
        print("production_ready is not YES; production GCMC is not allowed.")
        print(f"See: {READINESS}")
        return 2
    return 0
