# Molecule Definition Parse Error

status: RESOLVED

## Root Cause

RASPA2 source /home/baiheng/RASPA2_source/src/molecule.c lines 1388-1413 reads fixed line order: skip one line, then Tc, Pc, omega, skip one line, then NumberOfAtoms. The pre-fix H2O.def had two comment lines before Tc, shifting NumberOfAtoms to the acentric-factor line.

## Failing Component

- failing component before fix: H2O
- failing definition file before fix: canonical `H2O.def`
- failing line number in H2O.def: line 2 extra parser metadata comment
- parser expectation: exactly one skipped header line followed by Tc, Pc, omega, one skipped label line, then integer NumberOfAtoms
- actual pre-fix content: two skipped/comment lines before Tc; parser read `0.3443` as integer NumberOfAtoms, producing 0
- CH4 status: PASS

## Parser Tests After Fix

| case | parse_status | exit_code | last line | first failure evidence |
|---|---|---:|---|---|
| CH4_ONLY_PARSE_TEST | PASS | 0 | `Shift all potentials` | `` |
| H2O_ONLY_PARSE_TEST | PASS | 0 | `Shift all potentials` | `` |
| CH4_H2O_BINARY_PARSE_TEST | PASS_DEFINITION_PARSE_WITH_DOWNSTREAM_DIAGNOSTIC_MATRIX_WARNING | 0 | `Matrix Inversion, Gauss-Jordan: Singular Matrix` | `` |

Binary test note: `Matrix Inversion, Gauss-Jordan: Singular Matrix` appears after molecule definitions are read in the diagnostic 10k framework carrier. It is not the previous molecule-definition parse error and is not a production result.

MOLECULE_DEFINITION_GATE: PASS
