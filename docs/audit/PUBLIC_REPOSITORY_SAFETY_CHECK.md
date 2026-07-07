# Public Repository Safety Check

status: PASS

target_repository: BaihengA/kerogen-illite-gcmc

## Scope

This check covers the first public commit candidate in `KEROGEN_MD_GCMC_CODEBASE`.

## Results

| item | status | evidence |
|---|---|---|
| secrets/passwords/tokens/private keys | PASS | Keyword scan for password, token, secret, credential, private key, ghp_, sk-, AKIA, api_key found no candidate secret values. |
| email exposure | PASS | No Git identity was embedded in committed source or docs by this audit step. |
| local absolute paths | PASS_WITH_PROVENANCE_NOTE | Local machine paths remain in audit/provenance/legacy evidence to preserve scientific traceability. Canonical local runtime config `config/paths.json` is ignored and replaced by `config/paths.example.json`. |
| proprietary/raw trajectory data | PASS | `*.trr`, `*.xtc`, `*.cpt`, `*.edr`, `*.tpr`, `Output/`, RASPA/GCMC output folders, caches, and `results/` are ignored. |
| large files | PASS | No commit candidate above 1 MiB after excluding ignored caches/results. Largest candidates are audit/provenance text tables. |
| GROMACS installation files | PASS | No GROMACS installation tree is committed. OPLS-AA source paths and numeric LJ values appear only in provenance reports. |
| RASPA2 installation files | PASS | No RASPA2 installation tree is committed. RASPA paths and binary hashes appear only as provenance. |
| third-party force-field files | PASS | Installed GROMACS/RASPA force-field files are not copied into the repository. |
| generated RASPA outputs | PASS | RASPA `Output/` and generated reservoir state files are ignored; the small audited `simulation.input` is retained for roundtrip evidence. |

## Notes

The repository is suitable for a public first commit as an evidence-rich code and workflow consolidation. It is not a production GCMC result release: `production_ready = NO` because the RMS_0p300 smoke test failed before RASPA execution due missing canonical Local forcefield/run assets.
