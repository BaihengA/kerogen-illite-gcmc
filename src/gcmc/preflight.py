from __future__ import annotations
from pathlib import Path
from workflow_common import CODEBASE, PROJECT_ROOT

print("Canonical GCMC preflight is evidence-driven.")
print(f"Project root: {PROJECT_ROOT}")
print(f"Readiness report: {PROJECT_ROOT / 'docs' / 'audit' / 'GCMC_READINESS_REPORT.md'}")
raise SystemExit(0)
