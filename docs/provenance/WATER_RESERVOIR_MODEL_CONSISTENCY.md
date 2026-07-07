# Water Reservoir Model Consistency

status: PASS

reservoir_reference: real water thermodynamics via IAPWS-95 external_real_water_reference

pore_molecular_representation: OPLS 3-site water from `00_INPUT/H2O.pdb` and `00_INPUT/H2O.itp`

The reservoir reference and pore molecular model are intentionally not claimed to be the same model. The external water reservoir supplies the H2O chemical-potential boundary; inserted pore water remains the audited OPLS 3-site molecular representation.

Resolved pore-water LJ evidence remains:

| atom | atom_type | sigma_nm | epsilon_kJ_mol |
|---|---|---:|---:|
| OW | opls_116 | 3.16557e-01 | 6.50194e-01 |
| HW | opls_117 | 0 | 0 |

same_model_water_reference: NOT_IMPLEMENTED. It would require a separate calibrated OPLS 3-site bulk/reference chemical potential.
