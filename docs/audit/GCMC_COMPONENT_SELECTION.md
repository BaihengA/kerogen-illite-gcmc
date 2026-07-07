# GCMC Component Selection

production_ready: NO
thermodynamic_boundary_status: BLOCKED

## geometry

- selected_file: `KEROGEN_MD_GCMC_CODEBASE/src/gcmc/preflight.py + source provenance 01_SCRIPTS/build_8nm_mirrored_pore.py`
- selected_reason: All four COMPOSITE_PORES_8NM_V33 reports show mean gap 8.0 nm using mean_surface_plane and complete mirrored composite walls.
- runtime_evidence: COMPOSITE_PORES_8NM_V33/*/*_pore_build_report.json
- rejected_alternatives: 4 nm V32 reports; V33 numeric BAT entrypoint as primary API.
- known_limitations: Geometry provenance remains in original reports; canonical entrypoint is now versionless.

## environment discovery

- selected_file: `KEROGEN_MD_GCMC_CODEBASE/src/gcmc/raspa_discovery.py`
- selected_reason: Copied from validated V36 autodiscovery utility; formal workflow no longer calls historical v36 path directly.
- runtime_evidence: RASPA2_WSL_DIAGNOSTIC_V36.txt STATUS=PASS
- rejected_alternatives: V33 failed base forcefield discovery; V34 quoting/encoding issues; V35 empty RASPA_ROOT.
- known_limitations: raspa2_status=PASS; V36 logic is required provenance but historical file is not a formal entrypoint.

## water model

- selected_file: `00_INPUT/H2O.pdb + 00_INPUT/H2O.itp via canonical water resolver`
- selected_reason: User-provided PDB/ITP only; no generated Tip5p.def fallback.
- runtime_evidence: docs/provenance/WATER_MODEL_RESOLVED.md; docs/provenance/WATER_LJ_RESOLUTION.csv
- rejected_alternatives: 00_INPUT/Tip5p.def and RASPA2_LOCAL/Tip5p.def if present; generated local water definitions.
- known_limitations: water_lj_status=BLOCKED; production blocked until LJ/mass/combination rule close.

## prepare

- selected_file: `KEROGEN_MD_GCMC_CODEBASE/workflows/08_gcmc_ch4_h2o/01_prepare.bat`
- selected_reason: Versionless canonical wrapper; refuses to run while readiness blockers remain.
- runtime_evidence: docs/audit/GCMC_READINESS_REPORT.md
- rejected_alternatives: 49_PREPARE_RASPA2_GCMC_8NM.bat, V34/V35/V36 numeric BAT wrappers as formal APIs.
- known_limitations: Must generate simulation.input, local force field, and provenance only after water/thermo PASS.

## run

- selected_file: `KEROGEN_MD_GCMC_CODEBASE/workflows/08_gcmc_ch4_h2o/03_run_production.bat`
- selected_reason: Versionless canonical wrapper; requires production_ready=YES.
- runtime_evidence: docs/audit/GCMC_READINESS_REPORT.md
- rejected_alternatives: 50_RUN_RASPA2_GCMC_8NM.bat and V34/V35/V36 numeric BAT wrappers as formal APIs.
- known_limitations: No case may be silently skipped or reported successful after failure.

## collect

- selected_file: `KEROGEN_MD_GCMC_CODEBASE/workflows/08_gcmc_ch4_h2o/04_collect.bat`
- selected_reason: Versionless collector API; may only summarize real RASPA output.
- runtime_evidence: results/GCMC_CH4_H2O_COUNTS.csv records FAILED_PREFLIGHT_NOT_RUN from previous blocked run.
- rejected_alternatives: 51_COLLECT_GCMC_COUNTS_8NM.bat and V35/V36 numeric collectors as formal APIs.
- known_limitations: Must distinguish smoke from production and never coerce failed cases to zero.
