# Canonical CH4-H2O GCMC Workflow

This is the only formal entrypoint for the audited 8 nm CH4-H2O GCMC workflow.
It intentionally avoids historical version labels and numeric BAT names.

Order:

1. `00_preflight.bat`
2. `01_prepare.bat`
3. `02_smoke_test.bat`
4. `03_run_production.bat`
5. `04_collect.bat`

Rules:

- No silent fallback.
- Historical V33/V36/V38 scripts are provenance sources, not direct formal entrypoints.
- Smoke and production are blocked unless `docs/audit/GCMC_READINESS_REPORT.md` shows required PASS states.
- Current readiness report: `F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\docs\audit\GCMC_READINESS_REPORT.md`
