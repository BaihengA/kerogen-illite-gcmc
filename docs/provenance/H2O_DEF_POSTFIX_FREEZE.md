# H2O DEF Postfix Freeze

status: PASS

- H2O.def path: `F:\MD\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\KEROGEN_MD_GCMC_CODEBASE\workflows\08_gcmc_ch4_h2o\generated\RMS_0p300\P20MPa\H2O.def`
- H2O.def sha256: `bf1a5c1964e031f84c88d9974ef09d26ba818aab4e570ab1c37151c204f06bf8`
- atom count unchanged: YES, 3
- atom order unchanged: YES, OW, HW1, HW2
- charges unchanged: YES, from `pseudo_atoms.def` OW=-0.82, HW1=0.41, HW2=0.41
- geometry unchanged: YES, OW=(0,0,0), HW1=(0,-0.784,0.554), HW2=(0,0.784,0.554) Angstrom
- LJ mapping unchanged: YES, `WATER_LJ_RESOLUTION.csv` unchanged
- f_H2O/IAPWS/fugacity mapping unchanged: YES

The only change from the failing version is removal of one extra metadata comment line so RASPA2's fixed-line parser reads NumberOfAtoms from the intended integer line.

```text
# critical constants: Temperature [T], Pressure [Pa], and Acentric factor [-]
647.096
22064000.0
0.3443
#Number Of Atoms
3
# Number of groups
1
# H2O-group
rigid
# number of atoms
3
```
