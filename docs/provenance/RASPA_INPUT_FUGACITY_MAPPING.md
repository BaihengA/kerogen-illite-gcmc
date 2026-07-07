# RASPA Input Fugacity Mapping

status: PASS

simulation_input: F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\KEROGEN_MD_GCMC_CODEBASE\workflows\08_gcmc_ch4_h2o\generated\RMS_0p300\P20MPa\simulation.input

Mapping rule: `f_i = phi_i * y_i * P_total`

`MolFraction` is the RASPA gas-reservoir composition/mapping fraction. It is not the H2O fugacity. H2O fugacity is supplied by the IAPWS-95 external-water reference and represented in RASPA by the calculated effective `FugacityCoefficient`.

| component | target_fugacity_Pa | MolFraction | FugacityCoefficient | effective_fugacity_Pa |
|---|---:|---:|---:|---:|
| CH4 | 16839028.2419113 | 0.997636645934322 | 0.8439459552 | 16839028.2419113 |
| H2O | 53255.717968868 | 0.0023633540656784 | 1.1266978304747 | 53255.7179688683 |
