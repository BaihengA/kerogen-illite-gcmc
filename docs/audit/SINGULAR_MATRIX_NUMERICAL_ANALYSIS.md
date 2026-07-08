# Singular Matrix Numerical Analysis

Scope: DIAGNOSTIC_ONLY RASPA2 source-level localization for the first zero pivot captured from `GaussJordan`.

Evidence source:
- `diagnostics/raspa_source_debug/component_comparison/CH4_H2O_BINARY/gaussjordan/singular_call_2/A_original.csv`
- `diagnostics/raspa_source_debug/component_comparison/CH4_H2O_BINARY/gaussjordan/singular_call_2/metadata.json`

Result:
- Shape: 2 x 2
- Rank: 0
- Determinant: 0
- Singular values: 0, 0
- Minimum singular value: 0
- Condition number: infinity
- Classification: exact singular

Linear dependency evidence:
- Zero rows: [0, 1]
- Zero columns: [0, 1]
- Duplicate rows: [(0, 1)]
- Duplicate columns: [(0, 1)]
- Null vector 0: 1, 0
- Null vector 1: 0, 1

Interpretation:
- `A_original` is the 2 x 2 all-zero component-count fluctuation/covariance matrix built in `PrintAverageTotalSystemEnergiesMC` before per-component heat-of-adsorption reporting.
- The first pivot search finds `big = 0`, `irow = 1`, `icol = 1`, and `pivot_value = 0` at `iteration_i = 0`.
- This is not a numerically near-singular matrix; it is exactly singular because all rows and all columns are zero.
