# RASPA Grid Runtime Capability

status: RUNTIME_PRESENT_BUT_GRID_GATE_FAILS_ENERGY_CONSISTENCY

Evidence from current RASPA2 source/install:

- `SimulationType MakeGrid` is supported and was executed on the 10k and 25k diagnostic frameworks.
- `UseTabularGrid yes` is supported and was executed in grid-using Monte Carlo diagnostic runs.
- RASPA opened VDW grid files for `CH4`, `H2O_OW`, `H2O_HW1`, and `H2O_HW2`.
- RASPA opened the Ewald electrostatic grid file for both 10k and 25k cases.
- The recurring `Matrix Inversion, Gauss-Jordan: Singular Matrix` message appears after grid reading and is the already-localized post-simulation zero-fluctuation reporting artifact, not a grid runtime blocker.

Runtime result:

- 10k MakeGrid: PASS
- 25k MakeGrid: PASS
- 10k grid-using MC startup: PASS, grid files opened
- 25k grid-using MC startup: PASS, grid files opened

Gate result:

- CH4 explicit-vs-grid energy: FAIL at predefined 10.0 A diagnostic spacing
- H2O VDW explicit-vs-grid energy: FAIL at predefined 10.0 A diagnostic spacing
- H2O Coulomb explicit-vs-grid energy: PASS
- H2O orientation validation: FAIL at predefined 10.0 A diagnostic spacing
- GRID_GATE: FAIL

No full 276864-atom grid and no production GCMC were run.
