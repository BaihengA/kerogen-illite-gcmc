# RASPA Grid Capability Report

status: SUPPORTED_BUT_FULL_8NM_NOT_FEASIBLE_AS_DIRECT_ROUTE

## Evidence

- current source supports `SimulationType MakeGrid`: examples/Auxiliary/6_MakingGrids/simulation.input
- current source supports `UseTabularGrid yes`: examples/Auxiliary/7_UsingGrids/simulation.input and src/input.c
- docs describe `UseTabularGrid`, `SpacingVDWGrid`, `SpacingCoulombGrid`, `GridTypes`
- no active keywords named `MakingGrids` or `UsingGrids` were found; the actual interface is `SimulationType MakeGrid` and `UseTabularGrid yes`

## Required Questions

1. current version supports grid: YES
2. LJ grid supported: YES, via VDW grid / GridTypes
3. electrostatic grid supported: YES, via Coulomb grid spacing options
4. multiple adsorbate types supported: YES in principle through `NumberOfGrids`/`GridTypes`
5. CH4 usable: LIKELY, atom type `CH4` is a single-site grid candidate
6. H2O usable: LIKELY_AFTER_H2O_DEF_FIX, grid types would need water interaction sites such as `H2O_OW/H2O_HW1/H2O_HW2`
7. many framework atom types usable: INPUT_READ_SUPPORTED, but setup/generation cost is the blocker
8. rough non-crystalline CIF usable: CIF read is supported and observed; grid physical validation remains required
9. grid generation cost: HIGH for full 8 nm explicit framework
10. grid memory cost: HIGH to PROHIBITIVE for fine spacing and multiple adsorbate site grids

## Full Cell Grid Size Estimate

| spacing_A | nx | ny | nz | points_per_grid | double_grid_GB |
|---:|---:|---:|---:|---:|---:|
| 0.1 | 1703 | 1667 | 1915 | 5436495415 | 40.505 |
| 0.15 | 1135 | 1112 | 1277 | 1611727240 | 12.008 |
| 0.25 | 681 | 667 | 766 | 347937882 | 2.592 |
| 0.5 | 341 | 334 | 383 | 43621402 | 0.325 |
| 1.0 | 171 | 167 | 192 | 5482944 | 0.041 |

GRID_ROUTE: NOT_READY_FOR_FULL_PRODUCTION

A diagnostic 10k/25k grid feasibility test may be considered after defining acceptable spacing and energy-validation tolerances. Full 276864-atom grid generation should not be attempted as production without memory planning.
