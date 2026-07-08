# RASPA Grid Runtime Capability

status: CAPABILITY_PRESENT_BUT_GRID_GATE_BLOCKED

Evidence from current RASPA2 source/install:

- `examples/Auxiliary/6_MakingGrids/simulation.input` uses `SimulationType MakeGrid`.
- `examples/Auxiliary/7_UsingGrids/simulation.input` uses `UseTabularGrid yes`.
- `src/input.c` parses `UseTabularGrid`, `SpacingVDWGrid`, `SpacingCoulombGrid`, `NumberOfGrids`, and `GridTypes`.
- `Docs/InputFiles/input_files.tex` documents energy/force grid options.

Runtime capability summary:

- SimulationType MakeGrid: YES
- UseTabularGrid yes: YES
- LJ/VDW grid: YES in principle
- Coulomb grid: YES in principle
- multiple adsorbate site types: YES in principle via `NumberOfGrids` and `GridTypes`
- CH4: likely compatible as one grid type
- H2O: only diagnostic after H2O.def fix; multi-site and Coulomb consistency still not validated
- full rough non-crystalline 276864-atom CIF: CIF read works, but startup/grid memory cost remains high

Grid runtime was not executed for 10k/25k in this round because `DIAGNOSTIC_CARRIER_GATE=FAIL` due to the binary-component singular matrix.
