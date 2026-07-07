# H2O RASPA Definition Provenance

status: PASS

`H2O.def` was generated from the user project water files, not from a default TIP3P/TIP5P substitution.

- source PDB: `F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\00_INPUT\H2O.pdb`
- source PDB sha256: `e68ba32e1274535c7c986ae7933d72ed3369078846693c08499dbf6bcd090a48`
- source ITP: `F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\00_INPUT\H2O.itp`
- source ITP sha256: `061971ee8931da54351645a39a65de0381a0fa894d153fc4d3261ad81ae11ce1`
- generated H2O.def: `F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\KEROGEN_MD_GCMC_CODEBASE\workflows\08_gcmc_ch4_h2o\generated\RMS_0p300\P20MPa\H2O.def`
- generated H2O.def sha256: `675ed1556f815fea75dd25fdda8d33f8a2be873abbc6ca70d2a81f5dda4accbd`
- atom count: 3
- atom order: OW, HW1, HW2

Water LJ closure remains the previously audited OPLS resolution in `WATER_LJ_FINAL_RESOLUTION.md` and `WATER_LJ_RESOLUTION.csv`.

The RASPA file contains parser metadata critical constants. Reservoir water fugacity is still controlled by the audited external real-water reference and explicit RASPA `FugacityCoefficient`; the H2O coefficient is an effective mapping coefficient, not a real CH4-H2O gas EOS phi.
