# Singular Matrix Root Cause

status: SOURCE_LEVEL_LOCALIZED

## Final Classification

Root-cause classification: F. OTHER_PROVEN

The first captured singular matrix is not a cell-geometry inverse, not H2O molecule geometry, not identity-change setup, not a molecule-definition parser failure, and not binary component initialization. It is a post-simulation reporting matrix generated only for multi-component systems.

## Source-Level Evidence

- Unmodified diagnostic build reproduced `Matrix Inversion, Gauss-Jordan: Singular Matrix`.
- Instrumented diagnostic build captured first singular call at `GaussJordan` call_id `2`.
- Matrix dimensions: `n = 2`, `m = 2`.
- `A_original`:

```text
0,0
0,0
```

- Rank: `0`.
- Minimum singular value: `0`.
- First pivot: `iteration_i = 0`, `irow = 1`, `icol = 1`, `pivot_value = 0`.
- Backtrace: `PrintAverageTotalSystemEnergiesMC -> InverseRealMatrix -> GaussJordan`.
- Source line context: `statistics.c` builds a `NumberOfComponents x NumberOfComponents` component-number fluctuation/covariance matrix and calls `InverseRealMatrix(matrix)` for per-component heat-of-adsorption reporting.
- Unmodified diagnostic run exit status: `0`.
- Instrumented diagnostic run exit status: `77`, by design, because the patch aborts at the first zero pivot.

## Component Comparison

See `docs/audit/GAUSSJORDAN_COMPONENT_COMPARISON.csv`.

- CH4_ONLY: PASS_NO_SINGULAR
- H2O_ONLY: PASS_NO_SINGULAR
- CH4_H2O_BINARY: FAIL_SINGULAR

## Rejected Causes

- Cell matrix singularity: rejected by cell determinant/inverse validation.
- H2O geometry degeneracy: rejected by `docs/audit/H2O_GEOMETRY_MATRIX_VALIDATION.md`.
- Identity-change matrix: rejected because the failing backtrace does not enter identity-change setup.
- Component definition parser: rejected because CH4/H2O molecule definitions parse and single-component carriers pass.
- Binary component initialization: rejected because the unmodified binary diagnostic carrier proceeds through initialization and exits `0`; the singular matrix is reached from `PrintPostSimulationStatus`.

## Gate Status

- BINARY_COMPONENT_INIT_GATE: PASS
- REPORTING_MATRIX_GATE: FAIL
- GRID_GATE: NOT_RUN_THIS_ROUND
- production_ready: NO
- production GCMC run: NO
