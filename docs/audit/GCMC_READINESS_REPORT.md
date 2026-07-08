# GCMC Readiness Report

Current audited status after RASPA2 first-singular-matrix source-level localization:

- geometry_status: PASS
- raspa2_status: PASS for parser and diagnostic executable availability
- methane_status: PASS
- water_status: PASS
- binary molecule-definition parse: PASS
- BINARY_COMPONENT_INIT_GATE: PASS
- singular_matrix_status: POST_SIMULATION_REPORTING_ARTIFACT_IN_ZERO_FLUCTUATION_DIAGNOSTIC
- grid_runtime_status: PASS for 10k and 25k MakeGrid
- CH4_grid_energy_status: FAIL at predefined 10.0 A diagnostic spacing
- H2O_VDW_grid_energy_status: FAIL at predefined 10.0 A diagnostic spacing
- H2O_Coulomb_grid_energy_status: PASS
- H2O_orientation_grid_status: FAIL at predefined 10.0 A diagnostic spacing
- GRID_GATE: FAIL
- production_ready: NO
- production GCMC run: NO

Root-cause classification:
- F. OTHER_PROVEN

Evidence:
- Unmodified debug build reproduced `Matrix Inversion, Gauss-Jordan: Singular Matrix`.
- The unmodified debug run exited with status `0`; the instrumented run exited with status `77` only because the diagnostic patch intentionally aborts at first zero pivot.
- Instrumented `GaussJordan` captured first singular call as `call_id = 2`, `n = 2`, `m = 2`.
- Backtrace: `PrintAverageTotalSystemEnergiesMC -> InverseRealMatrix -> GaussJordan`.
- `A_original` is a 2 x 2 all-zero per-component number-fluctuation covariance matrix in post-simulation per-component heat-of-adsorption reporting.
- CH4-only and H2O-only one-component diagnostic carriers do not trigger the singular matrix; the CH4-H2O binary diagnostic carrier does.
- H2O geometry and inertia tensor are not degenerate.
- 10k and 25k `SimulationType MakeGrid` runs completed with exit code `0`.
- Grid-using MC inputs with `UseTabularGrid yes` opened CH4, H2O_OW, H2O_HW1, H2O_HW2, and Ewald grid files.
- Explicit-vs-grid energy checks failed for CH4, H2O VDW, and H2O orientation at the predefined coarse 10.0 A grid spacing; near-wall/high-energy points were retained and classified separately.

Production decision:
- Binary component initialization is no longer classified as the blocker. Grid runtime exists, but GRID_GATE is FAIL because energy/orientation consistency did not pass. Production readiness remains NO.
