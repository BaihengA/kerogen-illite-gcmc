# RASPA Grid Runtime Report

Scope: DIAGNOSTIC_ONLY 10k/25k grid runtime validation; no production GCMC was run.

- 10k MakeGrid: PASS, exit_code=0, grid_dimensions=17x17x19, grid_file_size=1037448
- 25k MakeGrid: PASS, exit_code=0, grid_dimensions=17x17x19, grid_file_size=1037448

- grid_runtime_PASS: True
- CH4_energy_PASS: False
- H2O_VDW_PASS: False
- H2O_Coulomb_PASS: True
- H2O_orientation_PASS: False
- GRID_GATE: FAIL

Notes:
- `UseTabularGrid yes` is included in grid-using Monte Carlo inputs. RASPA source ignores it during `SimulationType MakeGrid`, which is expected.
- Energy comparison uses frozen diagnostic inputs, RASPA-generated grid files, and a predefined coarse 10.0 A spacing; near-wall/high-energy points are retained and classified separately.
- No full 276864-atom grid and no production GCMC were run.
