# Canonical GCMC Call Graph

status: PASS

The canonical CH4-H2O GCMC entrypoints are under `KEROGEN_MD_GCMC_CODEBASE/workflows/08_gcmc_ch4_h2o/` and use the audited Python modules under `src/gcmc/`. Historical vXX scripts are not formal entrypoints.

## Materialization Path

1. `src/gcmc/prepare.py`
2. `resolve_state(...)` from `src/gcmc/thermo_state.py`
3. `simulation.input` written to `F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\KEROGEN_MD_GCMC_CODEBASE\workflows\08_gcmc_ch4_h2o\generated\RMS_0p300\P20MPa\simulation.input`
4. `materialize(run_type="smoke")` from `src/gcmc/run_materializer.py`
5. `RUN_ASSET_MANIFEST.json` written to `F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\KEROGEN_MD_GCMC_CODEBASE\workflows\08_gcmc_ch4_h2o\generated\RMS_0p300\P20MPa\RUN_ASSET_MANIFEST.json`

## Smoke Path

1. `src/gcmc/smoke_test.py`
2. readiness gates from `src/gcmc/workflow_common.py`
3. preflight from `src/gcmc/smoke_test.py`
4. framework staging into `F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\KEROGEN_MD_GCMC_CODEBASE\workflows\08_gcmc_ch4_h2o\generated\RMS_0p300\P20MPa\RMS_0p300_Pore8nm.cif` and RASPA CIF directory
5. RASPA executable: `/home/baiheng/miniforge3/envs/raspa2/bin/simulate`
6. 1+1 cycle canonical smoke input: `F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\KEROGEN_MD_GCMC_CODEBASE\workflows\08_gcmc_ch4_h2o\generated\RMS_0p300\P20MPa\simulation.input`

## Current Evidence

- RUN_ASSET_MANIFEST status: PASS
- SMOKE_PREFLIGHT launch_allowed: YES
- latest smoke status: FAIL_TIMEOUT
- production GCMC executed: NO
