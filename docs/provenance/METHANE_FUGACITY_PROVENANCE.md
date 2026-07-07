# Methane Fugacity Provenance

- molecule definition: `/home/baiheng/miniforge3/envs/raspa2/share/raspa/molecules/ExampleDefinitions/methane.def`
- sha256: `5281d172d5c98f8f75e04976a8c13cc3ea6125c56e240ba72e06043e52b1541e`
- critical_temperature_K: `190.564`
- critical_pressure_Pa: `4599200.0`
- acentric_factor: `0.01142`

## RASPA 0-Cycle Evidence

At T=353.15 K and P=20000000.0 Pa for pure methane:

- omitted `FugacityCoefficient` -> phi_CH4 = `0.8439459552`
- partial fugacity = `16878919.10383212193847` Pa
- explicit `FugacityCoefficient 1.0` -> partial fugacity = `20000000.00000000000000` Pa

For the project water-saturated methane composition estimate:

- y_CH4 = `0.9976366459343216`
- f_CH4_Pa = y_CH4 * phi_CH4 * P = `16839028.241911303`

Status: PASS for CH4 fugacity provenance.
