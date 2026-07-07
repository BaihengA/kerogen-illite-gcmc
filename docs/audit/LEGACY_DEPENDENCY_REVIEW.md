# Legacy Dependency Review

Current conclusion: `REQUIRED_LEGACY=0` is acceptable for direct formal workflow execution after this round, because the formal entrypoints under `KEROGEN_MD_GCMC_CODEBASE/workflows/08_gcmc_ch4_h2o/` call canonical code inside `KEROGEN_MD_GCMC_CODEBASE/src/gcmc/`.

V36 autodiscovery remains scientifically and operationally required provenance. Its validated logic has been copied into `KEROGEN_MD_GCMC_CODEBASE/src/gcmc/raspa_discovery.py`, so the formal workflow does not directly call the historical `01_SCRIPTS/*_v36.py` path.

Conditions checked:

- copied into consolidated codebase: YES
- SHA/provenance captured in audit reports: YES, see `RUNTIME_EVIDENCE.csv` and copied source file metadata
- original historical path still available: YES
- formal workflow points to new canonical location: YES
- new code behavior intended to preserve original V36 discovery behavior: YES

If future formal workflow directly calls a historical path outside `KEROGEN_MD_GCMC_CODEBASE`, that dependency must be reclassified as `REQUIRED_LEGACY`.

Current production_ready: `NO`
