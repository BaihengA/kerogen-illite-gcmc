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
smoke_test_status: FAIL
production_ready: NO

## Thermodynamic State

- f_CH4_Pa: 16839028.2419113
- f_H2O_Pa: 53255.717968868
- water_activity: 1.0
- reservoir_reference: external_real_water_reference
- pore_water_model: OPLS 3-site water from 00_INPUT/H2O.pdb and 00_INPUT/H2O.itp

Production remains blocked because the RMS_0p300 smoke test did not reach RASPA execution: the canonical run directory lacks complete Local forcefield assets, H2O.def, and the RMS_0p300 framework CIF copy.
