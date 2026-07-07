# Water LJ Final Resolution

Generated: 2026-07-07T12:17:20

## Decision

water_lj_status = PASS

The project-local `00_INPUT/H2O.itp` does not contain `[ atomtypes ]`, but the atom types it uses are standard OPLS-AA water atom types. They close through the configured and installed GROMACS 2018.8 OPLS-AA force field:

- force field root: `F:\gromacs some software\gmx2018.8\share\gromacs\top\oplsaa.ff`
- LJ source: `F:\gromacs some software\gmx2018.8\share\gromacs\top\oplsaa.ff\ffnonbonded.itp`
- mass source: `F:\gromacs some software\gmx2018.8\share\gromacs\top\oplsaa.ff\atomtypes.atp`
- defaults source: `F:\gromacs some software\gmx2018.8\share\gromacs\top\oplsaa.ff\forcefield.itp`
- combination rule: `3`
- selected preprocessor branch: non-`HEAVY_H`

`HEAVY_H` is not defined in `00_INPUT/H2O.itp` or the audited water workflow, so the non-heavy-hydrogen branch is the selected version. The heavy-H branch has the same sigma/epsilon for `opls_116` and `opls_117` but different masses, so the normal branch must be recorded explicitly.

## SHA256

- H2O.pdb: `e68ba32e1274535c7c986ae7933d72ed3369078846693c08499dbf6bcd090a48`
- H2O.itp: `061971ee8931da54351645a39a65de0381a0fa894d153fc4d3261ad81ae11ce1`
- ffnonbonded.itp: `fdf072dac9900c039b58e21323ce621b2112dc86c46a4b5e49e1398ae5d3b9f0`
- atomtypes.atp: `eca003e6de6ae4450d17bcd53173d79d9858713e41a1a7cfea65344c269d8638`
- forcefield.itp: `3280ec76bf783082ad1920d076d9001cf8939c7a62a74d7b7f287b1512786aa9`

## Resolution Priority Chain

1. User project water molecule file: `00_INPUT/H2O.itp` for atom names, charges, topology, SETTLES geometry.
2. Project-local `[ atomtypes ]` definitions: searched, none found for `opls_116` / `opls_117`.
3. Configured GROMACS OPLS-AA force field: selected because the water atom types are OPLS-AA names and GROMACS path is part of the audited environment.
4. Generated or historical `Tip5p.def`: rejected; not used.
5. Built-in TIP3P/TIP4P/TIP5P defaults: rejected; not used.

## Final Parameters

| water atom | atom type | charge | mass | sigma_nm | epsilon_kJ_mol | source |
| --- | --- | --- | --- | --- | --- | --- |
| OW | opls_116 | -0.82 | 15.99940 | 3.16557e-01 | 6.50194e-01 | `F:\gromacs some software\gmx2018.8\share\gromacs\top\oplsaa.ff\ffnonbonded.itp` |
| HW1 | opls_117 | 0.41 | 1.00800 | 0.00000e+00 | 0.00000e+00 | `F:\gromacs some software\gmx2018.8\share\gromacs\top\oplsaa.ff\ffnonbonded.itp` |
| HW2 | opls_117 | 0.41 | 1.00800 | 0.00000e+00 | 0.00000e+00 | `F:\gromacs some software\gmx2018.8\share\gromacs\top\oplsaa.ff\ffnonbonded.itp` |

## Conversion Rule For RASPA2 Local Parameters

- Use `sigma_nm` from GROMACS directly in nm.
- Convert sigma to Angstrom only if writing a RASPA molecule or pseudo-atom file that explicitly requires Angstrom: `sigma_A = sigma_nm * 10`.
- Keep epsilon in kJ/mol unless the target RASPA field explicitly requires Kelvin; do not silently convert.
- Keep charges from `00_INPUT/H2O.itp`.
- Do not use generated `Tip5p.def` or TIP defaults.

## Remaining Non-LJ Blockers

This file resolves the water LJ blocker only. Production readiness also depends on thermodynamic boundary and current runtime environment checks.
