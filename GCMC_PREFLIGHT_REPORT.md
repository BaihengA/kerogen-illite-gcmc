# GCMC_PREFLIGHT_REPORT

Generated: 2026-07-06T15:11:12

Overall status: FAIL

| check | status | evidence |
| --- | --- | --- |
| framework CIF check | PASS | Using audited COMPOSITE_PORES_8NM_V33 pore build reports; no CIF generation started. |
| atom type coverage | FAIL | H2O ITP [ atoms ] entries do not include masses.; H2O ITP does not contain [ atomtypes ]; sigma and epsilon for opls_116/opls_117 are unresolved from user-provided water files.; Audit WATER_MODEL_REPORT marks H2O LJ_in_local_atomtypes=False. |
| pseudo atom coverage | FAIL | H2O pseudo atom definition cannot be validated without resolved sigma/epsilon and RASPA local molecule definition from 00_INPUT. |
| mixing rules coverage | FAIL | methane_fugacity_coefficient is null; fugacity assumption is unresolved.; water_fugacity_coefficient is null; fugacity assumption is unresolved.; H2O ITP [ atoms ] entries do not include masses.; H2O ITP does not contain [ atomtypes ]; sigma and epsilon for opls_116/opls_117 are unresolved from user-provided water files.; Audit WATER_MODEL_REPORT marks H2O LJ_in_local_atomtypes=False. |
| charge coverage | PASS | H2O net charge=0.0. |
| CH4 molecule definition | PASS | /home/baiheng/miniforge3/envs/raspa2/share/raspa/molecules/ExampleDefinitions/methane.def; sha256=5281d172d5c98f8f75e04976a8c13cc3ea6125c56e240ba72e06043e52b1541e |
| H2O molecule definition | FAIL | Selected 00_INPUT/H2O.pdb + 00_INPUT/H2O.itp; blocked until LJ/mass parameters are explicit. |
| box length | PASS | All four 8 nm pore reports have mean gap 8.0 nm by mean_surface_plane. |
| cutoff | PASS | cutoff_A=12.0 |
| periodic boundary | FAIL | No parsed simulation.input available in audited codebase results; cannot validate PBC before prepare. |
| overlap check | FAIL | Smoke/prepare not allowed before water model and thermodynamics pass. |
| WSL RASPA2 executable | PASS | /home/baiheng/miniforge3/envs/raspa2/bin/simulate; exit=0 |
| simulation.input parse | FAIL | Not generated in this run because preflight blockers stop before prepare. |
| output write permission | PASS | Created F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\KEROGEN_MD_GCMC_CODEBASE\results |
