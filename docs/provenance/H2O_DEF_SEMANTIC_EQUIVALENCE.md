# H2O DEF Semantic Equivalence

status: PASS

The fix removes one extra parser-metadata comment line from `H2O.def` so RASPA2's fixed-line parser reads the intended fields. No physical water parameter was changed.

- fixed H2O.def sha256: `bf1a5c1964e031f84c88d9974ef09d26ba818aab4e570ab1c37151c204f06bf8`
- atom count unchanged: YES (3)
- atom order unchanged: YES (OW, HW1, HW2)
- charges unchanged: YES; stored in pseudo_atoms.def as OW=-0.82, HW1=0.41, HW2=0.41
- geometry unchanged: YES; coordinates remain OW=(0,0,0), HW1=(0,-0.784,0.554), HW2=(0,0.784,0.554) Angstrom
- LJ mapping unchanged: YES; WATER_LJ_RESOLUTION.csv unchanged
- reservoir fugacity/f_H2O unchanged: YES

## Fixed Header

```text
# critical constants: Temperature [T], Pressure [Pa], and Acentric factor [-]
647.096
22064000.0
0.3443
#Number Of Atoms
3
# Number of groups
1
```
