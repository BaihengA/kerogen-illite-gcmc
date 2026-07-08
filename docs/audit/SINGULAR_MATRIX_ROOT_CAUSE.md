# Singular Matrix Root Cause

status: DIAGNOSTIC_CARRIER_GATE_FAIL

## Cell Matrix Result

`docs/audit/DIAGNOSTIC_CELL_MATRIX_VALIDATION.csv` shows 10k, 25k, binary 10k carrier, and full canonical all share the same orthorhombic non-singular cell:

- a = 170.21 A
- b = 166.68 A
- c = 191.47528562 A
- alpha/beta/gamma = 90/90/90 deg
- det(H) = 5432269.27434 A^3
- inverse_status = PASS

## Variant Evidence

| variant | singular_matrix | notes |
|---|---|---|
| BINARY_NO_EWALD_LINE | True | removed ChargeMethod Ewald |
| BINARY_CHARGE_NONE | True | ChargeMethod Ewald->ChargeMethod None |
| BINARY_CREATE_ONE_EACH | True | CreateNumberOfMolecules 0->CreateNumberOfMolecules 1 |
| BINARY_NO_ROTATION | True | removed RotationProbability |
| BINARY_UNIT_FUGACITY | True | FugacityCoefficient 0.8439459552->FugacityCoefficient 1.0; FugacityCoefficient 1.1266978304747->FugacityCoefficient 1.0 |
| BINARY_WITH_IDENTITY_CHANGE | True | official mixture identity-change controls added |

## Root-Cause Classification

A. cell geometry: REJECTED
B. coordinate conversion: REJECTED_BY_CELL_VALIDATION
C. diagnostic cropping: NOT_SUPPORTED; cropping preserves the full non-singular cell and single-component tests pass
D. RASPA internal matrix setup: MOST_LIKELY
E. other: not excluded, but no evidence stronger than D

The singular matrix is triggered by binary-component setup after molecule definitions are parsed and after `Shift all potentials`. It persists when Ewald is removed, `ChargeMethod None` is used, initial molecule count is set to 1, rotation is removed, fugacity coefficients are set to 1, and official mixture identity-change controls are added. Therefore it is not fixed by diagnostic carrier cell reconstruction.

DIAGNOSTIC_CARRIER_GATE: FAIL

Because this gate failed, grid generation and energy validation were not run in this round.
