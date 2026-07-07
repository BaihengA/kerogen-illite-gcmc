# GCMC Readiness Report

geometry_status: PASS
raspa2_status: PASS
methane_status: PASS
water_model_status: PASS
water_lj_status: PASS
atomtype_coverage: PASS
mixing_rule_status: PASS
CH4_reservoir_boundary_status: PASS
H2O_reservoir_boundary_status: PASS
thermodynamic_boundary_status: PASS
fugacity_mapping_status: PASS
run_asset_manifest_status: PASS
local_forcefield_coverage_status: PASS
h2o_def_status: PASS
framework_cif_status: PASS
cif_staging_status: PASS
smoke_preflight_status: PASS
startup_behavior: ACTIVE_COMPUTE
smoke_test_status: FAIL_TIMEOUT
hotspot_profile_status: SYMBOL_HOTSPOTS_UNAVAILABLE
framework_scaling_status: INSUFFICIENT_DATA_FOR_COMPLEXITY_FIT
production_feasibility: NOT_FEASIBLE_AS_IS
production_ready: NO

## Thermodynamic State

- f_CH4_Pa: 16839028.2419113
- f_H2O_Pa: 53255.717968868
- water_activity: 1.0
- reservoir_reference: external_real_water_reference
- H2O RASPA effective mapping coefficient: 1.1266978304747
- pore_water_model: OPLS 3-site water from 00_INPUT/H2O.pdb and 00_INPUT/H2O.itp

## Current Blocker

Canonical run assets and smoke preflight now pass. RASPA2 `simulate` starts and reads the RMS_0p300 framework CIF, but the canonical CH4-H2O 1+1 smoke does not complete within the 900 s `EXTENDED_SMOKE_ONLY` probe. The precise current failure class is `FAIL_TIMEOUT`, not missing assets, not reproduced exit 139, and not production output.

Production remains blocked because only a completed canonical CH4-H2O smoke may set `production_ready: YES`.
