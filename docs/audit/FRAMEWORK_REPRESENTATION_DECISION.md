# Framework Representation Decision

status: PRELIMINARY_DECISION

## Options

| route | physics_preservation | roughness_preservation | chemical_composition_preservation | electrostatics_preservation | GCMC_compatibility | startup_cost | runtime_cost | memory_cost | reproducibility | decision |
|---|---|---|---|---|---|---|---|---|---|---|
| FULL_EXPLICIT | highest | highest | highest | highest | currently starts but 900 s smoke timeout | prohibitive | unknown/high | moderate | high | NOT_FEASIBLE_AS_IS |
| GRID_ACCELERATED | potentially high after validation | high if generated from full CIF | high if all types included | possible but must validate Coulomb grid | supported by current RASPA2 in principle | high generation cost | lower after grid | potentially prohibitive at fine spacing | high if grid files/versioned | PROMISING_DIAGNOSTIC_ROUTE_NOT_PRODUCTION_READY |
| REPRESENTATIVE_PATCH | approximate | unknown until PSD/correlation validation | must be validated | approximate | likely compatible | lower | lower | lower | medium | NOT_READY_NO_PATCH_SELECTED |

## Recommendation

Do not continue by merely increasing timeout. The immediate fixed blocker was H2O.def serialization, now resolved. For representation, prefer a diagnostic GRID_ACCELERATED feasibility path first, because it preserves the full framework better than arbitrary patch selection. Representative patches require full surface statistics, correlation length, PSD, and a uniform rule across RMS_0p000/RMS_0p300/RMS_0p600/RMS_0p900 before they can be considered.

production_ready: NO
production_gcmc_run: NO
