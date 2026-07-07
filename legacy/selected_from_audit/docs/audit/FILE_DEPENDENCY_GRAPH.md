# File Dependency Graph

## `00_CHECK_ENVIRONMENT.bat`
- status: UNKNOWN
- inputs: 00_INPUT\kero.itp; 00_INPUT\kero.pdb; 00_INPUT\kero.top; 00_INPUT\kero_ATP.itp; kero.itp; kero.pdb; kero.top; kero_ATP.itp
- outputs: 00_INPUT\kero.itp; 00_INPUT\kero.pdb; 00_INPUT\kero.top; 00_INPUT\kero_ATP.itp; kero.itp; kero.pdb; kero.top; kero_ATP.itp
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `00_INPUT/H2O.itp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: BLOCKERS.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `00_INPUT/PUT_kero_ATP.itp_HERE.txt`
- status: DUPLICATE
- inputs: kero.top; kero_ATP.itp
- outputs: kero.top; kero_ATP.itp
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `00_INPUT/illite.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_illite_under_kerogen.py; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p300/RMS_0p300_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p600/RMS_0p600_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p900/RMS_0p900_build_report.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `00_INPUT/illite.top`
- status: DUPLICATE
- inputs: illi.itp; illi_ATP.itp
- outputs: illi.itp; illi_ATP.itp
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `00_INPUT/illite_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: BLOCKERS.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `00_INPUT/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `00_INPUT/kero.top`
- status: DUPLICATE
- inputs: kero.itp; kero_ATP.itp
- outputs: kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `00_INPUT/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `01_BUILD_BULK_0P1.bat`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/01_INITIAL/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/01_INITIAL/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `01_BULK/01_INITIAL/topol.top`
- status: DUPLICATE
- inputs: kero.itp; kero_ATP.itp
- outputs: kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/00_em.mdp`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/generate_wall_mdps.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/01_nvt_01_300K.mdp`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/01_nvt_02_600K.mdp`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/01_nvt_03_900K.mdp`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_001_100MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_002_100MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_003_100MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_004_100MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_005_100MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_006_100MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_007_100MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_008_60MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_009_60MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_010_60MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_011_60MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_012_60MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_013_60MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_014_60MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_015_40MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_016_40MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_017_40MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_018_40MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_019_40MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_020_40MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_021_40MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_022_40MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_023_25MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_024_25MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_025_25MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_026_25MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_027_25MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_028_25MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_029_15MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_030_15MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_031_15MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_032_15MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_033_15MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_034_10MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_035_10MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_036_10MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/02_npt_compress_037_10MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/02_MDP/03_nvt_lock_900K.mdp`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/run_bulk.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `01_BULK/03_RUN/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/03_RUN/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `01_BULK/03_RUN/mdout.mdp`
- status: UNKNOWN
- inputs: mdout.mdp
- outputs: not explicit
- calls/imports: grompp
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `01_BULK/03_RUN/topol.top`
- status: DUPLICATE
- inputs: kero.itp; kero_ATP.itp
- outputs: kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_BULK/BULK_BUILD_REPORT.json`
- status: UNKNOWN
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\01_INITIAL\\bulk_initial_0p1.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\01_INITIAL\\bulk_initial_0p1.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `01_BULK/BULK_DENSIFICATION_REPORT.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\BULK_DENSITY_SUMMARY.csv; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\BULK_DENSITY_SUMMARY.csv; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/run_bulk.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `01_SCRIPTS/add_illite_below_raw_final_kerogen_v30.py`
- status: SUPERSEDED
- inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro; RMS_xxx_kerogen_only_raw_from_final.gro; V30_BUILD_REPORT_ALL.csv; _EXACT_KEROGEN_INPUT_COPY.gro; _EXACT_kerogen_plus_illite.gro; _build_report.csv; _build_report.json; _illite_only.gro; _index.ndx; illite_below_raw_final_kerogen_v30_config.json
- outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro; RMS_xxx_kerogen_only_raw_from_final.gro; V30_BUILD_REPORT_ALL.csv; _EXACT_KEROGEN_INPUT_COPY.gro; _EXACT_kerogen_plus_illite.gro; _build_report.csv; _build_report.json; _illite_only.gro; illite_below_raw_final_kerogen_v30_config.json
- calls/imports: Dict, List, Optional, Sequence, Tuple; Path; __future__; annotations; argparse; csv; dataclass, replace; dataclasses; hashlib; json; math; numpy as np; pathlib; re; shutil; typing
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/add_illite_below_raw_final_kerogen_v31.py`
- status: ACTIVE
- inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro; RMS_xxx_kerogen_only_raw_from_final.gro; V31_BUILD_REPORT_ALL.csv; _EXACT_KEROGEN_INPUT_COPY.gro; _EXACT_kerogen_plus_illite.gro; _build_report.csv; _build_report.json; _illite_only.gro; _index.ndx; illite_below_raw_final_kerogen_v31_config.json
- outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro; RMS_xxx_kerogen_only_raw_from_final.gro; V31_BUILD_REPORT_ALL.csv; _EXACT_KEROGEN_INPUT_COPY.gro; _EXACT_kerogen_plus_illite.gro; _build_report.csv; _build_report.json; _illite_only.gro; illite_below_raw_final_kerogen_v31_config.json
- calls/imports: Dict, List, Optional, Sequence, Tuple; Path; __future__; annotations; argparse; csv; dataclass, replace; dataclasses; hashlib; json; math; numpy as np; pathlib; re; shutil; typing
- referenced by: 41_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ALL_V31.bat; 42_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ONE_V31.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/analyze_rough_surface.py`
- status: ACTIVE
- inputs: ROUGHNESS_METRICS_ALL.csv; _roughness_metrics.csv; _roughness_metrics.json; _standard_kerogen_plate.gro; _top_surface_grid.csv; args.inp
- outputs: ROUGHNESS_METRICS_ALL.csv; _roughness_metrics.csv; _roughness_metrics.json; _standard_kerogen_plate.gro; _top_surface_grid.csv
- calls/imports: Axes3D; List, Dict, Tuple; Path; __future__; annotations; argparse; csv; gro_tools; json; math; matplotlib; matplotlib.pyplot as plt; mpl_toolkits.mplot3d; numpy as np; pathlib; read_gro, select_kerogen_atoms, atoms_to_xyz; typing
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/apply_graphene_patch_settings.py`
- status: UNKNOWN
- inputs: config.json
- outputs: config.json
- calls/imports: Path; __future__; annotations; datetime; json, shutil; pathlib
- referenced by: FILE_INVENTORY_SHA256.txt; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `01_SCRIPTS/build_4nm_mirrored_pore.py`
- status: ACTIVE
- inputs: 4nm_pore_raspa2_config.json; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; PORE_4NM_BUILD_REPORT_ALL.csv; _COMPOSITE_PORE_4nm.gro; _EXACT_kerogen_plus_illite.gro; _LOWER_WALL.gro; _UPPER_WALL_MIRRORED.gro; _pore_build_report.csv; _pore_build_report.json; _wall_atom_mapping.csv
- outputs: 4nm_pore_raspa2_config.json; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; PORE_4NM_BUILD_REPORT_ALL.csv; _COMPOSITE_PORE_4nm.gro; _EXACT_kerogen_plus_illite.gro; _LOWER_WALL.gro; _UPPER_WALL_MIRRORED.gro; _pore_build_report.csv; _pore_build_report.json; _wall_atom_mapping.csv
- calls/imports: List, Sequence, Tuple; Path; __future__; annotations; argparse; csv; dataclass, replace; dataclasses; json; math; numpy as np; pathlib; typing
- referenced by: 43_BUILD_4NM_COMPOSITE_PORES.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/build_8nm_mirrored_pore.py`
- status: ACTIVE
- inputs: 8nm_pore_raspa2_config.json; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; PORE_8NM_BUILD_REPORT_ALL.csv; _COMPOSITE_PORE_8nm.gro; _EXACT_kerogen_plus_illite.gro; _LOWER_WALL.gro; _UPPER_WALL_MIRRORED.gro; _pore_build_report.csv; _pore_build_report.json; _wall_atom_mapping.csv
- outputs: 8nm_pore_raspa2_config.json; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; PORE_8NM_BUILD_REPORT_ALL.csv; _COMPOSITE_PORE_8nm.gro; _EXACT_kerogen_plus_illite.gro; _LOWER_WALL.gro; _UPPER_WALL_MIRRORED.gro; _pore_build_report.csv; _pore_build_report.json; _wall_atom_mapping.csv
- calls/imports: List, Sequence, Tuple; Path; __future__; annotations; argparse; csv; dataclass, replace; dataclasses; json; math; numpy as np; pathlib; typing
- referenced by: 48_BUILD_8NM_COMPOSITE_PORES.bat; RELEASE_MANIFEST_SHA256.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/build_graphene_cases.py`
- status: ACTIVE
- inputs: CASE_METADATA.json; GRAPHENE_BUILD_REPORT.json; GTOP_posre_full.itp; GTOP_posre_pull.itp; _posre_fixed.itp; bulk_density_0p8_final.gro; index.ndx; kero.itp; kero.top; kero_ATP.itp; system_initial.gro; topol.top
- outputs: CASE_METADATA.json; GRAPHENE_BUILD_REPORT.json; GTOP_posre_full.itp; GTOP_posre_pull.itp; _posre_fixed.itp; bulk_density_0p8_final.gro; kero.itp; kero.top; kero_ATP.itp; system_initial.gro; topol.top
- calls/imports: Path; argparse; common; datetime; json; math; pathlib; shutil
- referenced by: 03_BUILD_GRAPHENE_CASES.bat; 27_BUILD_RUN_RMS0_ONLY_NT8.bat; 28_RUN_ALL_RMS0_0300_0600_0900_FROM_SCRATCH_NT8.bat; FILE_INVENTORY_SHA256.txt; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; 待定代码/07_REBUILD_GRAPHENE_CASES_PATCHED.bat; 待定代码/09_QUICK_TEST_RMS_0p300_NT14.bat; 待定代码/10_RUN_NORMAL_NT8_ALL_ROUGH.bat

## `01_SCRIPTS/build_illite_under_kerogen.py`
- status: ACTIVE
- inputs: 02_GRAPHENE_CASES/RMS_xxx/02_RUN/STANDARD_KEROGEN_PLATE/RMS_xxx_standard_kerogen_plate.gro; ILLITE_BUILD_REPORT_ALL.csv; ILLITE_BUILD_REPORT_ALL.json; ILLITE_UNDER_KEROGEN/RMS_xxx/RMS_xxx_ILLITE_SUPERCELL.itp; ILLITE_UNDER_KEROGEN/RMS_xxx/RMS_xxx_illite_under_kerogen.gro; _ILLITE_SUPERCELL.itp; _build_report.csv; _build_report.json; _composite_topol_template.top; _illite_only.gro; _illite_under_kerogen.gro; _illite_under_kerogen_PBC_VIEW_3x3.gro; _kerogen_oriented_rough_top.gro; _posre_illite.itp; forcefield.itp; illite_under_kerogen_config.json; kerogen.itp; m.gro
- outputs: 02_GRAPHENE_CASES/RMS_xxx/02_RUN/STANDARD_KEROGEN_PLATE/RMS_xxx_standard_kerogen_plate.gro; ILLITE_BUILD_REPORT_ALL.csv; ILLITE_BUILD_REPORT_ALL.json; ILLITE_UNDER_KEROGEN/RMS_xxx/RMS_xxx_ILLITE_SUPERCELL.itp; ILLITE_UNDER_KEROGEN/RMS_xxx/RMS_xxx_illite_under_kerogen.gro; _ILLITE_SUPERCELL.itp; _build_report.csv; _build_report.json; _composite_topol_template.top; _illite_only.gro; _illite_under_kerogen.gro; _illite_under_kerogen_PBC_VIEW_3x3.gro; _kerogen_oriented_rough_top.gro; _posre_illite.itp; forcefield.itp; illite_under_kerogen_config.json; kerogen.itp; m.gro
- calls/imports: Dict, Iterable, List, Optional, Tuple; Path; __future__; annotations; argparse; csv; dataclass, replace; dataclasses; json; math; numpy as np; os; pathlib; re; shutil; typing
- referenced by: 24_BUILD_ILLITE_UNDER_KEROGEN_ALL.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/build_quartz_under_kerogen.py`
- status: ACTIVE
- inputs: QUARTZ_BUILD_REPORT_ALL.csv; _kerogen_oriented_rough_top.gro; _quartz_build_report.csv; _quartz_build_report.json; _quartz_nonbonded_snippet.itp; _quartz_under_kerogen_rough_top.gro; _quartz_wall.itp; _quartz_wall_only.gro; _standard_kerogen_plate.gro; _topol_include_snippet.txt; args.inp
- outputs: QUARTZ_BUILD_REPORT_ALL.csv; _kerogen_oriented_rough_top.gro; _quartz_build_report.csv; _quartz_build_report.json; _quartz_nonbonded_snippet.itp; _quartz_under_kerogen_rough_top.gro; _quartz_wall.itp; _quartz_wall_only.gro; _standard_kerogen_plate.gro
- calls/imports: GroAtom, read_gro, write_gro, select_kerogen_atoms, atoms_to_xyz, copy_atoms, shift_atoms; List, Tuple, Dict; Path; __future__; analyze_rough_surface; annotations; argparse; csv; gro_tools; json; make_surface_grid, surface_metrics; math; numpy as np; pathlib; typing
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/collect_gcmc_counts.py`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json; GCMC_CH4_H2O_MOLECULE_COUNTS.csv; RESERVOIR_STATE.json; m.gro
- outputs: 8nm_pore_raspa2_config.json; GCMC_CH4_H2O_MOLECULE_COUNTS.csv; RESERVOIR_STATE.json; m.gro; raspa_console.log
- calls/imports: Optional, Tuple; Path; __future__; annotations; argparse, csv, json, re; pathlib; typing
- referenced by: 46_COLLECT_GCMC_COUNTS.bat; 51_COLLECT_GCMC_COUNTS_8NM.bat; 59_COLLECT_GCMC_COUNTS_8NM_V35.bat; 63_COLLECT_GCMC_COUNTS_8NM_V36.bat; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/collect_standard_plate_metrics.py`
- status: UNKNOWN
- inputs: STANDARD_PLATE_METRICS_ALL.csv; _standard_kerogen_plate_metrics.json
- outputs: STANDARD_PLATE_METRICS_ALL.csv; _standard_kerogen_plate_metrics.json
- calls/imports: Path; csv; json; pathlib
- referenced by: 13_COLLECT_STANDARD_PLATE_METRICS.bat; 19_CONTINUE_RMS300_AFTER60_THEN_RUN600_900.bat; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `01_SCRIPTS/common.py`
- status: UNKNOWN
- inputs: config.json; match.gro
- outputs: config.json; match.gro
- calls/imports: Dict, Iterable, List, Optional, Sequence, Tuple; Path; __future__; annotations; collections; csv; defaultdict, deque; json; math; pathlib; random; re; shutil; subprocess; typing
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/continue_case_after_stage.py`
- status: ACTIVE
- inputs: PULL_RUN_SUMMARY.csv; final_structure_pull.gro; system_initial.gro
- outputs: PULL_RUN_SUMMARY.csv; final_structure_pull.gro; system_initial.gro
- calls/imports: Path; argparse; common; csv; fail, load_config; pathlib; run_wall_case; shutil
- referenced by: 19_CONTINUE_RMS300_AFTER60_THEN_RUN600_900.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/diagnose_raspa2_wsl_v34.py`
- status: SUPERSEDED
- inputs: 8nm_pore_raspa2_config.json; FF/force_field_mixing_rules.def; FF/pseudo_atoms.def; RASPA2_WSL_DIAGNOSTIC_V34.txt; TIP5P.def; Tip5p.def; methane.def
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: Path; __future__; annotations; argparse; json; os; pathlib; shutil; simulate; subprocess
- referenced by: 53_DIAGNOSE_RASPA2_WSL_V34.bat; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/diagnose_raspa2_wsl_v35.py`
- status: SUPERSEDED
- inputs: 8nm_pore_raspa2_config.json; FF/force_field_mixing_rules.def; FF/pseudo_atoms.def; RASPA2_WSL_DIAGNOSTIC_V35.txt; TIP5P.def; Tip5p.def; methane.def
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: Path; __future__; annotations; argparse; json; os; pathlib; shutil; simulate; subprocess
- referenced by: 56_DIAGNOSE_RASPA2_WSL_V35_ENCODING_SAFE.bat; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/diagnose_raspa2_wsl_v36.py`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json; FFNAME/force_field_mixing_rules.def; FFNAME/pseudo_atoms.def; RASPA2_WSL_DIAGNOSTIC_V36.txt; TIP5P.def; Tip5p.def; methane.def
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: Iterable; Path; __future__; annotations; argparse; json; os; pathlib; shutil; simulate; subprocess; typing
- referenced by: 60_DIAGNOSE_RASPA2_WSL_V36_AUTODISCOVER.bat; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/export_view_groups.py`
- status: ACTIVE
- inputs: 00_em.gro; 02_pull_ramp_01_5MPa.gro; 02_pull_ramp_02_10MPa.gro; 03_pull_stage_01_900K_100ps.gro; 03_pull_stage_01_900K_chunk01_100ps.gro; VIEW_ALL_WALLS_ONLY.gro; VIEW_GROUPS_REPORT.json; VIEW_GTOP_ONLY.gro; VIEW_KERO_ONLY.gro; args.gro; final_structure_pull.gro; system_initial.gro
- outputs: 00_em.gro; 02_pull_ramp_01_5MPa.gro; 02_pull_ramp_02_10MPa.gro; 03_pull_stage_01_900K_100ps.gro; 03_pull_stage_01_900K_chunk01_100ps.gro; VIEW_ALL_WALLS_ONLY.gro; VIEW_GROUPS_REPORT.json; VIEW_GTOP_ONLY.gro; VIEW_KERO_ONLY.gro; args.gro; final_structure_pull.gro; system_initial.gro
- calls/imports: Path; argparse; common; fail, load_config, read_gro; json; math; pathlib; shutil
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; 待定代码/11_EXPORT_RMS_0p300_VIEW_FILES.bat

## `01_SCRIPTS/extract_kerogen_only_from_final.py`
- status: ACTIVE
- inputs: 02_pull_ramp_01_20MPa.gro; 02_pull_ramp_02_40MPa.gro; 02_pull_ramp_03_60MPa.gro; 02_pull_ramp_04_80MPa.gro; 03_pull_stage_01_700K_chunk01_50ps.gro; 03_pull_stage_02_500K_chunk01_50ps.gro; CASE_METADATA.json; KEROGEN_ONLY_FINALS_METRICS.csv; _kerogen_only_raw_from_final.gro; _kerogen_only_standard_plate.gro; final_structure_pull.gro; kero.itp; kero.top; kero_ATP.itp
- outputs: 02_pull_ramp_01_20MPa.gro; 02_pull_ramp_02_40MPa.gro; 02_pull_ramp_03_60MPa.gro; 02_pull_ramp_04_80MPa.gro; 03_pull_stage_01_700K_chunk01_50ps.gro; 03_pull_stage_02_500K_chunk01_50ps.gro; CASE_METADATA.json; KEROGEN_ONLY_FINALS_METRICS.csv; _kerogen_only_raw_from_final.gro; _kerogen_only_standard_plate.gro; final_structure_pull.gro; kero.itp; kero.top; kero_ATP.itp
- calls/imports: Path; argparse; common; csv; json; load_config, read_gro, write_gro, read_itp_atoms, fail; math; pathlib; shutil
- referenced by: 27_BUILD_RUN_RMS0_ONLY_NT8.bat; 28_RUN_ALL_RMS0_0300_0600_0900_FROM_SCRATCH_NT8.bat; 30_EXTRACT_KEROGEN_ONLY_FROM_ALL_FINALS.bat; 31_EXTRACT_KEROGEN_ONLY_EXISTING_0300_0600_0900.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/extract_standard_kerogen_plate.py`
- status: ACTIVE
- inputs: CASE_METADATA.json; _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro; _standard_kerogen_plate_metrics.csv; _standard_kerogen_plate_metrics.json; args.inp; final_structure_pull.gro; kero.itp; kero.top; kero_ATP.itp; topol.top
- outputs: CASE_METADATA.json; _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro; _standard_kerogen_plate_metrics.csv; _standard_kerogen_plate_metrics.json; final_structure_pull.gro; kero.itp; kero.top; kero_ATP.itp; topol.top
- calls/imports: Path; argparse; common; csv; json; load_config, read_gro, write_gro, fail, read_itp_atoms; math; pathlib; shutil
- referenced by: 19_CONTINUE_RMS300_AFTER60_THEN_RUN600_900.bat; 27_BUILD_RUN_RMS0_ONLY_NT8.bat; 28_RUN_ALL_RMS0_0300_0600_0900_FROM_SCRATCH_NT8.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; 待定代码/08_RUN_ROUGH_CASES_PATCHED.bat; 待定代码/09_QUICK_TEST_RMS_0p300_NT14.bat; 待定代码/10_RUN_NORMAL_NT8_ALL_ROUGH.bat; 待定代码/12_EXTRACT_STANDARD_PLATES_ONLY.bat

## `01_SCRIPTS/generate_wall_mdps.py`
- status: UNKNOWN
- inputs: 00_em.mdp; CASE_METADATA.json; MPa.mdp; PULL_FORCE_REPORT.json; _em.mdp; ps.mdp
- outputs: CASE_METADATA.json; PULL_FORCE_REPORT.json
- calls/imports: Path; common; json; pathlib
- referenced by: 04_GENERATE_GRAPHENE_MDP.bat; 19_CONTINUE_RMS300_AFTER60_THEN_RUN600_900.bat; 27_BUILD_RUN_RMS0_ONLY_NT8.bat; 28_RUN_ALL_RMS0_0300_0600_0900_FROM_SCRATCH_NT8.bat; FILE_INVENTORY_SHA256.txt; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; 待定代码/07_REBUILD_GRAPHENE_CASES_PATCHED.bat; 待定代码/09_QUICK_TEST_RMS_0p300_NT14.bat; 待定代码/10_RUN_NORMAL_NT8_ALL_ROUGH.bat

## `01_SCRIPTS/gro_tools.py`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: List, Optional, Tuple; Path; __future__; annotations; dataclass; dataclasses; math; numpy as np; pathlib; typing
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/prepare_bulk.py`
- status: UNKNOWN
- inputs: BULK_BUILD_REPORT.json; bulk_initial_0p1.gro; index.ndx; kero.itp; kero.pdb; kero.top; kero_ATP.itp; kero_centered.pdb; packed_48_kero.pdb; packmol.inp; topol.top
- outputs: BULK_BUILD_REPORT.json; bulk_initial_0p1.gro; kero.itp; kero.pdb; kero.top; kero_ATP.itp; kero_centered.pdb; packed_48_kero.pdb; packmol_bulk.log; topol.top
- calls/imports: Path; argparse; common; json; math; pathlib; shutil
- referenced by: 01_BUILD_BULK_0P1.bat; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/prepare_raspa2_gcmc.py`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json; ATOMNAME_MAPPING_WARNINGS.csv; FRAMEWORK_INSTALL_NOTE.txt; MISSING_GROMACS_ATOMTYPES.txt; MISSING_WATER_DEFINITION.txt; RASPA2_WSL_DIAGNOSTIC_V36.txt; RESERVOIR_STATE.csv; RESERVOIR_STATE.json; RESERVOIR_STATE_ALL.csv; TIP5P.def; Tip5p.def; WALL_FORCEFIELD_TYPE_MAP.csv; _COMPOSITE_PORE_8nm.gro; _wall_atom_mapping.csv; force_field.def; force_field_mixing_rules.def; kero.itp; m.gro; pseudo_atoms.def; simulation.inp
- outputs: 8nm_pore_raspa2_config.json; ATOMNAME_MAPPING_WARNINGS.csv; RESERVOIR_STATE.csv; RESERVOIR_STATE.json; RESERVOIR_STATE_ALL.csv; WALL_FORCEFIELD_TYPE_MAP.csv; _COMPOSITE_PORE_8nm.gro; _wall_atom_mapping.csv; kero.itp; m.gro
- calls/imports: Dict, Iterable, List, Optional, Sequence, Tuple; Path; __future__; annotations; argparse; cache_wsl_raspa_assets; csv; dataclass; dataclasses; json; math; numpy as np; os; pathlib; re; shutil; simulate; subprocess; typing; wsl_raspa_utils_v36
- referenced by: 01_SCRIPTS/build_4nm_mirrored_pore.py; 01_SCRIPTS/build_8nm_mirrored_pore.py; 44_PREPARE_RASPA2_GCMC.bat; 49_PREPARE_RASPA2_GCMC_8NM.bat; 54_PREPARE_RASPA2_GCMC_8NM_V34.bat; 57_PREPARE_RASPA2_GCMC_8NM_V35_ENCODING_SAFE.bat; 61_PREPARE_RASPA2_GCMC_8NM_V36_AUTODISCOVER.bat; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/run_bulk.py`
- status: ACTIVE
- inputs: 00_em.mdp; 03_nvt_lock_900K.mdp; BULK_BUILD_REPORT.json; BULK_DENSIFICATION_REPORT.json; BULK_DENSITY_SUMMARY.csv; K.mdp; MPa.mdp; bulk_density_0p8_final.gro; bulk_initial_0p1.gro; index.ndx; topol.top
- outputs: BULK_BUILD_REPORT.json; BULK_DENSIFICATION_REPORT.json; BULK_DENSITY_SUMMARY.csv; _grompp.log; _mdrun.log; _resume.log; bulk_density_0p8_final.gro; bulk_initial_0p1.gro; topol.top
- calls/imports: Path; common; csv; json; math; pathlib; shutil
- referenced by: 02_RUN_BULK_TO_0P8.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `01_SCRIPTS/run_raspa2_cases.py`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json; MISSING_WATER_DEFINITION.txt; Tip5p.def; simulation.inp
- outputs: 8nm_pore_raspa2_config.json; raspa_console.log
- calls/imports: Optional; Path; __future__; annotations; argparse; discover_wsl_raspa as discover_wsl_raspa_v36, run_wsl_script; json; os; pathlib; shlex; shutil; simulate; subprocess; typing; wsl_raspa_utils_v36
- referenced by: 01_SCRIPTS/prepare_raspa2_gcmc.py; 45_RUN_RASPA2_GCMC.bat; 50_RUN_RASPA2_GCMC_8NM.bat; 55_RUN_RASPA2_GCMC_8NM_V34_WSL.bat; 58_RUN_RASPA2_GCMC_8NM_V35_WSL_ENCODING_SAFE.bat; 62_RUN_RASPA2_GCMC_8NM_V36_WSL.bat; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/run_wall_case.py`
- status: UNKNOWN
- inputs: 00_em.mdp; PULL_FORCE_REPORT.json; PULL_RUN_SUMMARY.csv; _before_shape_repair.gro; _shape_repair.json; _translated_input.gro; final_structure_pull.gro; index.ndx; system_initial.gro; topol.top
- outputs: PULL_FORCE_REPORT.json; PULL_RUN_SUMMARY.csv; _before_shape_repair.gro; _grompp.log; _mdrun.log; _pullf.xvg; _pullx.xvg; _resume.log; _shape_repair.json; _translated_input.gro; final_structure_pull.gro; system_initial.gro; topol.top
- calls/imports: Path; argparse; common; csv; json; math; pathlib; shutil
- referenced by: 01_SCRIPTS/generate_wall_mdps.py; 05_RUN_ONE_CASE.bat; 19_CONTINUE_RMS300_AFTER60_THEN_RUN600_900.bat; 27_BUILD_RUN_RMS0_ONLY_NT8.bat; 28_RUN_ALL_RMS0_0300_0600_0900_FROM_SCRATCH_NT8.bat; FILE_INVENTORY_SHA256.txt; docs/audit/FILE_DEPENDENCY_GRAPH.md; 待定代码/06_RUN_ALL_CASES.bat; 待定代码/08_RUN_ROUGH_CASES_PATCHED.bat; 待定代码/09_QUICK_TEST_RMS_0p300_NT14.bat; 待定代码/10_RUN_NORMAL_NT8_ALL_ROUGH.bat

## `01_SCRIPTS/set_config_value.py`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: Path; __future__; annotations; argparse, json; pathlib
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `01_SCRIPTS/wsl_raspa_utils_v36.py`
- status: UNKNOWN
- inputs: FFNAME/force_field_mixing_rules.def; FFNAME/pseudo_atoms.def; TIP5P.def; Tip5p.def; WSL_RASPA_DISCOVERY.txt; force_field.def; force_field_mixing_rules.def; methane.def; pseudo_atoms.def
- outputs: not explicit
- calls/imports: Path; SIMULATE; __future__; annotations; dataclass; dataclasses; os; pathlib; shlex; shutil; simulate; subprocess
- referenced by: RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/GRAPHENE_BUILD_REPORT.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp`
- status: DUPLICATE
- inputs: GBOT_posre_fixed.itp
- outputs: GBOT_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GBOT.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp`
- status: DUPLICATE
- inputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- outputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP_posre_full.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP_posre_pull.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp`
- status: DUPLICATE
- inputs: GXMN_posre_fixed.itp
- outputs: GXMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp`
- status: DUPLICATE
- inputs: GXMX_posre_fixed.itp
- outputs: GXMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN.itp`
- status: DUPLICATE
- inputs: GYMN_posre_fixed.itp
- outputs: GYMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX.itp`
- status: DUPLICATE
- inputs: GYMX_posre_fixed.itp
- outputs: GYMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top`
- status: DUPLICATE
- inputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- outputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/01_MDP/00_em.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/generate_wall_mdps.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/01_MDP/01_wall_nvt_900K_3ps.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/01_MDP/02_pull_ramp_01_20MPa.mdp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/01_MDP/02_pull_ramp_02_40MPa.mdp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/01_MDP/02_pull_ramp_03_60MPa.mdp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/01_MDP/03_pull_stage_01_700K_chunk01_50ps.mdp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/01_MDP/03_pull_stage_02_500K_chunk01_50ps.mdp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GBOT.itp`
- status: DUPLICATE
- inputs: GBOT_posre_fixed.itp
- outputs: GBOT_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GBOT_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GBOT.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp`
- status: DUPLICATE
- inputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- outputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP_posre_full.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP_posre_pull.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMN.itp`
- status: DUPLICATE
- inputs: GXMN_posre_fixed.itp
- outputs: GXMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMX.itp`
- status: DUPLICATE
- inputs: GXMX_posre_fixed.itp
- outputs: GXMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMN.itp`
- status: DUPLICATE
- inputs: GYMN_posre_fixed.itp
- outputs: GYMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMX.itp`
- status: DUPLICATE
- inputs: GYMX_posre_fixed.itp
- outputs: GYMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p000_standard_kerogen_plate_metrics.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p000_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p000_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\final_structure_pull.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p000_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p000_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\final_structure_pull.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top`
- status: DUPLICATE
- inputs: kero.itp; kero_ATP.itp
- outputs: kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp`
- status: ACTIVE
- inputs: mdout.mdp
- outputs: not explicit
- calls/imports: grompp
- referenced by: 01_BULK/03_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top`
- status: DUPLICATE
- inputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- outputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/CASE_METADATA.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/generate_wall_mdps.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p000/PULL_FORCE_REPORT.json`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/generate_wall_mdps.py; 01_SCRIPTS/run_wall_case.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GBOT.itp`
- status: DUPLICATE
- inputs: GBOT_posre_fixed.itp
- outputs: GBOT_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GBOT_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GBOT.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp`
- status: DUPLICATE
- inputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- outputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP_posre_full.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP_posre_pull.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMN.itp`
- status: DUPLICATE
- inputs: GXMN_posre_fixed.itp
- outputs: GXMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMX.itp`
- status: DUPLICATE
- inputs: GXMX_posre_fixed.itp
- outputs: GXMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMN.itp`
- status: DUPLICATE
- inputs: GYMN_posre_fixed.itp
- outputs: GYMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMX.itp`
- status: DUPLICATE
- inputs: GYMX_posre_fixed.itp
- outputs: GYMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top`
- status: DUPLICATE
- inputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- outputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/01_MDP/00_em.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/generate_wall_mdps.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/01_MDP/01_wall_nvt_900K_3ps.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/01_MDP/02_pull_ramp_01_20MPa.mdp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/01_MDP/02_pull_ramp_02_40MPa.mdp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/01_MDP/02_pull_ramp_03_60MPa.mdp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/01_MDP/03_pull_stage_01_700K_chunk01_50ps.mdp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/01_MDP/03_pull_stage_02_500K_chunk01_50ps.mdp`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GBOT.itp`
- status: DUPLICATE
- inputs: GBOT_posre_fixed.itp
- outputs: GBOT_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GBOT_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GBOT.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp`
- status: DUPLICATE
- inputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- outputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP_posre_full.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP_posre_pull.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMN.itp`
- status: DUPLICATE
- inputs: GXMN_posre_fixed.itp
- outputs: GXMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMX.itp`
- status: DUPLICATE
- inputs: GXMX_posre_fixed.itp
- outputs: GXMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMN.itp`
- status: DUPLICATE
- inputs: GYMN_posre_fixed.itp
- outputs: GYMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMX.itp`
- status: DUPLICATE
- inputs: GYMX_posre_fixed.itp
- outputs: GYMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p300_standard_kerogen_plate_metrics.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p300_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p300_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\final_structure_pull.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p300_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p300_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\final_structure_pull.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top`
- status: DUPLICATE
- inputs: kero.itp; kero_ATP.itp
- outputs: kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp`
- status: ACTIVE
- inputs: mdout.mdp
- outputs: not explicit
- calls/imports: grompp
- referenced by: 01_BULK/03_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top`
- status: DUPLICATE
- inputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- outputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/CASE_METADATA.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/generate_wall_mdps.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p300/PULL_FORCE_REPORT.json`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/generate_wall_mdps.py; 01_SCRIPTS/run_wall_case.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GBOT.itp`
- status: DUPLICATE
- inputs: GBOT_posre_fixed.itp
- outputs: GBOT_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GBOT_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GBOT.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp`
- status: DUPLICATE
- inputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- outputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP_posre_full.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP_posre_pull.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMN.itp`
- status: DUPLICATE
- inputs: GXMN_posre_fixed.itp
- outputs: GXMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMX.itp`
- status: DUPLICATE
- inputs: GXMX_posre_fixed.itp
- outputs: GXMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMN.itp`
- status: DUPLICATE
- inputs: GYMN_posre_fixed.itp
- outputs: GYMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMX.itp`
- status: DUPLICATE
- inputs: GYMX_posre_fixed.itp
- outputs: GYMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top`
- status: DUPLICATE
- inputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- outputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/01_MDP/00_em.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/generate_wall_mdps.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/01_MDP/01_wall_nvt_900K_3ps.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/01_MDP/02_pull_ramp_01_20MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/01_MDP/02_pull_ramp_02_40MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/01_MDP/02_pull_ramp_03_60MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/01_MDP/03_pull_stage_01_700K_chunk01_50ps.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/01_MDP/03_pull_stage_02_500K_chunk01_50ps.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GBOT.itp`
- status: DUPLICATE
- inputs: GBOT_posre_fixed.itp
- outputs: GBOT_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GBOT_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GBOT.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp`
- status: DUPLICATE
- inputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- outputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP_posre_full.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP_posre_pull.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMN.itp`
- status: DUPLICATE
- inputs: GXMN_posre_fixed.itp
- outputs: GXMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMX.itp`
- status: DUPLICATE
- inputs: GXMX_posre_fixed.itp
- outputs: GXMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMN.itp`
- status: DUPLICATE
- inputs: GYMN_posre_fixed.itp
- outputs: GYMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMX.itp`
- status: DUPLICATE
- inputs: GYMX_posre_fixed.itp
- outputs: GYMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p600_standard_kerogen_plate_metrics.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p600_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p600_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\final_structure_pull.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p600_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p600_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\final_structure_pull.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top`
- status: DUPLICATE
- inputs: kero.itp; kero_ATP.itp
- outputs: kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp`
- status: ACTIVE
- inputs: mdout.mdp
- outputs: not explicit
- calls/imports: grompp
- referenced by: 01_BULK/03_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top`
- status: DUPLICATE
- inputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- outputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/CASE_METADATA.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/generate_wall_mdps.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p600/PULL_FORCE_REPORT.json`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/generate_wall_mdps.py; 01_SCRIPTS/run_wall_case.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GBOT.itp`
- status: DUPLICATE
- inputs: GBOT_posre_fixed.itp
- outputs: GBOT_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GBOT_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GBOT.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp`
- status: DUPLICATE
- inputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- outputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP_posre_full.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP_posre_pull.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMN.itp`
- status: DUPLICATE
- inputs: GXMN_posre_fixed.itp
- outputs: GXMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMX.itp`
- status: DUPLICATE
- inputs: GXMX_posre_fixed.itp
- outputs: GXMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMN.itp`
- status: DUPLICATE
- inputs: GYMN_posre_fixed.itp
- outputs: GYMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMX.itp`
- status: DUPLICATE
- inputs: GYMX_posre_fixed.itp
- outputs: GYMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top`
- status: DUPLICATE
- inputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- outputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/01_MDP/00_em.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/generate_wall_mdps.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/01_MDP/01_wall_nvt_900K_3ps.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/01_MDP/02_pull_ramp_01_20MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/01_MDP/02_pull_ramp_02_40MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/01_MDP/02_pull_ramp_03_60MPa.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/01_MDP/03_pull_stage_01_700K_chunk01_50ps.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/01_MDP/03_pull_stage_02_500K_chunk01_50ps.mdp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GBOT.itp`
- status: DUPLICATE
- inputs: GBOT_posre_fixed.itp
- outputs: GBOT_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GBOT_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GBOT.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp`
- status: DUPLICATE
- inputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- outputs: GTOP_posre_full.itp; GTOP_posre_pull.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP_posre_full.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP_posre_pull.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GTOP.itp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMN.itp`
- status: DUPLICATE
- inputs: GXMN_posre_fixed.itp
- outputs: GXMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMX.itp`
- status: DUPLICATE
- inputs: GXMX_posre_fixed.itp
- outputs: GXMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GXMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMN.itp`
- status: DUPLICATE
- inputs: GYMN_posre_fixed.itp
- outputs: GYMN_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMN_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMN.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMX.itp`
- status: DUPLICATE
- inputs: GYMX_posre_fixed.itp
- outputs: GYMX_posre_fixed.itp
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMX_posre_fixed.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/GYMX.itp; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p900_standard_kerogen_plate_metrics.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p900_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p900_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\final_structure_pull.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p900_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p900_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\final_structure_pull.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top`
- status: DUPLICATE
- inputs: kero.itp; kero_ATP.itp
- outputs: kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp`
- status: ACTIVE
- inputs: mdout.mdp
- outputs: not explicit
- calls/imports: grompp
- referenced by: 01_BULK/03_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top`
- status: DUPLICATE
- inputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- outputs: GBOT.itp; GTOP.itp; GXMN.itp; GXMX.itp; GYMN.itp; GYMX.itp; kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 01_BULK/03_RUN/mdout.mdp; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/run_bulk.py; 01_SCRIPTS/run_wall_case.py; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/CASE_METADATA.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/generate_wall_mdps.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_GRAPHENE_CASES/RMS_0p900/PULL_FORCE_REPORT.json`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/generate_wall_mdps.py; 01_SCRIPTS/run_wall_case.py; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `02_RUN_BULK_TO_0P8.bat`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `03_BUILD_GRAPHENE_CASES.bat`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md

## `04_GENERATE_GRAPHENE_MDP.bat`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/run_wall_case.py; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `05_RUN_ONE_CASE.bat`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `13_COLLECT_STANDARD_PLATE_METRICS.bat`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `19_CONTINUE_RMS300_AFTER60_THEN_RUN600_900.bat`
- status: ACTIVE
- inputs: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\02_pull_ramp_03_60MPa.gro; 02_GRAPHENE_CASES\RMS_0p600\00_INITIAL\system_initial.gro; 02_GRAPHENE_CASES\RMS_0p900\00_INITIAL\system_initial.gro; 02_GRAPHENE_CASES\STANDARD_PLATE_METRICS_ALL.csv; config.json; config_resume_after60_nt8.json
- outputs: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\02_pull_ramp_03_60MPa.gro; 02_GRAPHENE_CASES\RMS_0p600\00_INITIAL\system_initial.gro; 02_GRAPHENE_CASES\RMS_0p900\00_INITIAL\system_initial.gro; 02_GRAPHENE_CASES\STANDARD_PLATE_METRICS_ALL.csv; config.json; config_resume_after60_nt8.json
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `24_BUILD_ILLITE_UNDER_KEROGEN_ALL.bat`
- status: UNKNOWN
- inputs: ILLITE_UNDER_KEROGEN\ILLITE_BUILD_REPORT_ALL.csv; illite_under_kerogen_config.json
- outputs: ILLITE_UNDER_KEROGEN\ILLITE_BUILD_REPORT_ALL.csv; illite_under_kerogen_config.json
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `27_BUILD_RUN_RMS0_ONLY_NT8.bat`
- status: ACTIVE
- inputs: 02_GRAPHENE_CASES\RMS_0p000\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p000_standard_kerogen_plate.gro; config.json; config_rms0_nt8.json
- outputs: 02_GRAPHENE_CASES\RMS_0p000\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p000_standard_kerogen_plate.gro; config.json; config_rms0_nt8.json
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `28_RUN_ALL_RMS0_0300_0600_0900_FROM_SCRATCH_NT8.bat`
- status: ACTIVE
- inputs: config.json; config_normal_nt8_with_rms0.json
- outputs: config.json; config_normal_nt8_with_rms0.json
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `30_EXTRACT_KEROGEN_ONLY_FROM_ALL_FINALS.bat`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `31_EXTRACT_KEROGEN_ONLY_EXISTING_0300_0600_0900.bat`
- status: ACTIVE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `41_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ALL_V31.bat`
- status: ACTIVE
- inputs: KEROGEN_ONLY_FINALS\RAW_KEEP_COORDINATES\RMS_xxx_kerogen_only_raw_from_final.gro; illite_below_raw_final_kerogen_v31_config.json
- outputs: KEROGEN_ONLY_FINALS\RAW_KEEP_COORDINATES\RMS_xxx_kerogen_only_raw_from_final.gro; illite_below_raw_final_kerogen_v31_config.json
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `42_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ONE_V31.bat`
- status: ACTIVE
- inputs: illite_below_raw_final_kerogen_v31_config.json
- outputs: illite_below_raw_final_kerogen_v31_config.json
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `43_BUILD_4NM_COMPOSITE_PORES.bat`
- status: UNKNOWN
- inputs: 4nm_pore_raspa2_config.json
- outputs: 4nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: 47_ALL_BUILD_PREP_RUN_COLLECT.bat; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `44_PREPARE_RASPA2_GCMC.bat`
- status: UNKNOWN
- inputs: 4nm_pore_raspa2_config.json; Tip5p.def
- outputs: 4nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: 47_ALL_BUILD_PREP_RUN_COLLECT.bat; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `45_RUN_RASPA2_GCMC.bat`
- status: UNKNOWN
- inputs: 4nm_pore_raspa2_config.json
- outputs: 4nm_pore_raspa2_config.json
- calls/imports: simulate
- referenced by: 01_SCRIPTS/prepare_raspa2_gcmc.py; 47_ALL_BUILD_PREP_RUN_COLLECT.bat; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `46_COLLECT_GCMC_COUNTS.bat`
- status: UNKNOWN
- inputs: 4nm_pore_raspa2_config.json; RASPA2_GCMC_4NM_V32\GCMC_CH4_H2O_MOLECULE_COUNTS.csv
- outputs: 4nm_pore_raspa2_config.json; RASPA2_GCMC_4NM_V32\GCMC_CH4_H2O_MOLECULE_COUNTS.csv
- calls/imports: not explicit
- referenced by: 47_ALL_BUILD_PREP_RUN_COLLECT.bat; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `47_ALL_BUILD_PREP_RUN_COLLECT.bat`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `48_BUILD_8NM_COMPOSITE_PORES.bat`
- status: ACTIVE
- inputs: 8nm_pore_raspa2_config.json
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: 52_ALL_8NM_BUILD_PREP_RUN_COLLECT.bat; README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `49_PREPARE_RASPA2_GCMC_8NM.bat`
- status: ACTIVE
- inputs: 8nm_pore_raspa2_config.json
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: 52_ALL_8NM_BUILD_PREP_RUN_COLLECT.bat; README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `4nm_pore_raspa2_config.json`
- status: ACTIVE
- inputs: 00_INPUT/kero.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro
- outputs: 00_INPUT/kero.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_4nm_mirrored_pore.py; 43_BUILD_4NM_COMPOSITE_PORES.bat; 44_PREPARE_RASPA2_GCMC.bat; 45_RUN_RASPA2_GCMC.bat; 46_COLLECT_GCMC_COUNTS.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `50_RUN_RASPA2_GCMC_8NM.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: simulate
- referenced by: 52_ALL_8NM_BUILD_PREP_RUN_COLLECT.bat; README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `51_COLLECT_GCMC_COUNTS_8NM.bat`
- status: ACTIVE
- inputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V33\GCMC_CH4_H2O_MOLECULE_COUNTS.csv
- outputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V33\GCMC_CH4_H2O_MOLECULE_COUNTS.csv
- calls/imports: not explicit
- referenced by: 52_ALL_8NM_BUILD_PREP_RUN_COLLECT.bat; README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `52_ALL_8NM_BUILD_PREP_RUN_COLLECT.bat`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `53_DIAGNOSE_RASPA2_WSL_V34.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json; RASPA2_WSL_DIAGNOSTIC_V34.txt
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: 54_PREPARE_RASPA2_GCMC_8NM_V34.bat; CHANGELOG.md; README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `54_PREPARE_RASPA2_GCMC_8NM_V34.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `55_RUN_RASPA2_GCMC_8NM_V34_WSL.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `56_DIAGNOSE_RASPA2_WSL_V35_ENCODING_SAFE.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json; RASPA2_WSL_DIAGNOSTIC_V35.txt
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: 57_PREPARE_RASPA2_GCMC_8NM_V35_ENCODING_SAFE.bat; README_V35_ENCODING_FIX.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `57_PREPARE_RASPA2_GCMC_8NM_V35_ENCODING_SAFE.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: README_V35_ENCODING_FIX.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `58_RUN_RASPA2_GCMC_8NM_V35_WSL_ENCODING_SAFE.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: README_V35_ENCODING_FIX.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `59_COLLECT_GCMC_COUNTS_8NM_V35.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V35\GCMC_CH4_H2O_MOLECULE_COUNTS.csv
- outputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V35\GCMC_CH4_H2O_MOLECULE_COUNTS.csv
- calls/imports: not explicit
- referenced by: README_V35_ENCODING_FIX.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `60_DIAGNOSE_RASPA2_WSL_V36_AUTODISCOVER.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json; RASPA2_WSL_DIAGNOSTIC_V36.txt
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/prepare_raspa2_gcmc.py; 01_SCRIPTS/run_raspa2_cases.py; 61_PREPARE_RASPA2_GCMC_8NM_V36_AUTODISCOVER.bat; 64_ALL_8NM_GCMC_V36.bat; README_V36_WSL_AUTODISCOVERY.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `61_PREPARE_RASPA2_GCMC_8NM_V36_AUTODISCOVER.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: 64_ALL_8NM_GCMC_V36.bat; README_V36_WSL_AUTODISCOVERY.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `62_RUN_RASPA2_GCMC_8NM_V36_WSL.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: 64_ALL_8NM_GCMC_V36.bat; README_V36_WSL_AUTODISCOVERY.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `63_COLLECT_GCMC_COUNTS_8NM_V36.bat`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V36\GCMC_CH4_H2O_MOLECULE_COUNTS.csv
- outputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V36\GCMC_CH4_H2O_MOLECULE_COUNTS.csv
- calls/imports: not explicit
- referenced by: 64_ALL_8NM_GCMC_V36.bat; README_V36_WSL_AUTODISCOVERY.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `64_ALL_8NM_GCMC_V36.bat`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `8nm_pore_raspa2_config.json`
- status: ACTIVE
- inputs: 00_INPUT/kero.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro
- outputs: 00_INPUT/kero.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro
- calls/imports: simulate
- referenced by: 01_SCRIPTS/build_8nm_mirrored_pore.py; 01_SCRIPTS/collect_gcmc_counts.py; 01_SCRIPTS/diagnose_raspa2_wsl_v34.py; 01_SCRIPTS/diagnose_raspa2_wsl_v35.py; 01_SCRIPTS/diagnose_raspa2_wsl_v36.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 01_SCRIPTS/run_raspa2_cases.py; 48_BUILD_8NM_COMPOSITE_PORES.bat; 49_PREPARE_RASPA2_GCMC_8NM.bat; 50_RUN_RASPA2_GCMC_8NM.bat; 51_COLLECT_GCMC_COUNTS_8NM.bat; 53_DIAGNOSE_RASPA2_WSL_V34.bat; 54_PREPARE_RASPA2_GCMC_8NM_V34.bat; 55_RUN_RASPA2_GCMC_8NM_V34_WSL.bat; 56_DIAGNOSE_RASPA2_WSL_V35_ENCODING_SAFE.bat; 57_PREPARE_RASPA2_GCMC_8NM_V35_ENCODING_SAFE.bat; 58_RUN_RASPA2_GCMC_8NM_V35_WSL_ENCODING_SAFE.bat; 59_COLLECT_GCMC_COUNTS_8NM_V35.bat; 60_DIAGNOSE_RASPA2_WSL_V36_AUTODISCOVER.bat; 61_PREPARE_RASPA2_GCMC_8NM_V36_AUTODISCOVER.bat; 62_RUN_RASPA2_GCMC_8NM_V36_WSL.bat; 63_COLLECT_GCMC_COUNTS_8NM_V36.bat; README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `BLOCKERS.md`
- status: UNKNOWN
- inputs: 00_INPUT/H2O.itp; 00_INPUT/H2O.pdb; 00_INPUT/SiO2_quartz.pdb; 00_INPUT/illite.itp; 00_INPUT/illite.pdb; 00_INPUT/illite_ATP.itp; 00_INPUT/kero.itp; 00_INPUT/kero.pdb; 00_INPUT/kero_ATP.itp
- outputs: 00_INPUT/H2O.itp; 00_INPUT/H2O.pdb; 00_INPUT/SiO2_quartz.pdb; 00_INPUT/illite.itp; 00_INPUT/illite.pdb; 00_INPUT/illite_ATP.itp; 00_INPUT/kero.itp; 00_INPUT/kero.pdb; 00_INPUT/kero_ATP.itp
- calls/imports: not explicit
- referenced by: not found

## `CHANGELOG.md`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: simulate
- referenced by: GITHUB_WORKFLOW.md; README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `COMPOSITE_PORES_4NM_V32/RMS_0p000/RMS_0p000_pore_build_report.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p000_kerogen_only_raw_from_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p000_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `COMPOSITE_PORES_4NM_V32/RMS_0p300/RMS_0p300_pore_build_report.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p300_kerogen_only_raw_from_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p300_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `COMPOSITE_PORES_4NM_V32/RMS_0p600/RMS_0p600_pore_build_report.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p600_kerogen_only_raw_from_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p600_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `COMPOSITE_PORES_4NM_V32/RMS_0p900/RMS_0p900_pore_build_report.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p900_kerogen_only_raw_from_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p900_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `COMPOSITE_PORES_8NM_V33/RMS_0p000/RMS_0p000_pore_build_report.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p000_kerogen_only_raw_from_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p000_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `COMPOSITE_PORES_8NM_V33/RMS_0p300/RMS_0p300_pore_build_report.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p300_kerogen_only_raw_from_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p300_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `COMPOSITE_PORES_8NM_V33/RMS_0p600/RMS_0p600_pore_build_report.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p600_kerogen_only_raw_from_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p600_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `COMPOSITE_PORES_8NM_V33/RMS_0p900/RMS_0p900_pore_build_report.json`
- status: ACTIVE
- inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p900_kerogen_only_raw_from_final.gro
- outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p900_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `FILE_INVENTORY_SHA256.txt`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: 66aced91fd372ddd965b7dc312427ea7164e8b0da55b9d494a994292184cee90       11376  01_SCRIPTS/run_wall_case.py; cc780b19d4cd2e33681b8a475ea98db5c920a1fcf3836f3ed2cd1c132ed4558f       16748  01_SCRIPTS/build_graphene_cases.py
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md

## `GITHUB_WORKFLOW.md`
- status: UNKNOWN
- inputs: PORE_8NM_BUILD_REPORT_ALL.csv
- outputs: PORE_8NM_BUILD_REPORT_ALL.csv
- calls/imports: not explicit
- referenced by: README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt`
- status: DUPLICATE
- inputs: kero.top; kero_ATP.itp
- outputs: kero.top; kero_ATP.itp
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/illite.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_illite_under_kerogen.py; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p300/RMS_0p300_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p600/RMS_0p600_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p900/RMS_0p900_build_report.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/illite.top`
- status: DUPLICATE
- inputs: illi.itp; illi_ATP.itp
- outputs: illi.itp; illi_ATP.itp
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/illite_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: BLOCKERS.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top`
- status: DUPLICATE
- inputs: kero.itp; kero_ATP.itp
- outputs: kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_build_report.json`
- status: ACTIVE
- inputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p000_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- outputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p000_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/illite.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_illite_under_kerogen.py; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p300/RMS_0p300_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p600/RMS_0p600_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p900/RMS_0p900_build_report.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p300/RMS_0p300_build_report.json`
- status: ACTIVE
- inputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p300_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- outputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p300_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p300/illite.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_illite_under_kerogen.py; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p300/RMS_0p300_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p600/RMS_0p600_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p900/RMS_0p900_build_report.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p600/RMS_0p600_build_report.json`
- status: ACTIVE
- inputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p600_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- outputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p600_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p600/illite.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_illite_under_kerogen.py; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p300/RMS_0p300_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p600/RMS_0p600_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p900/RMS_0p900_build_report.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p900/RMS_0p900_build_report.json`
- status: ACTIVE
- inputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p900_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- outputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p900_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p900/illite.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_illite_under_kerogen.py; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p300/RMS_0p300_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p600/RMS_0p600_build_report.json; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p900/RMS_0p900_build_report.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `KEROGEN_ONLY_FINALS/kero.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; 4nm_pore_raspa2_config.json; 8nm_pore_raspa2_config.json; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `KEROGEN_ONLY_FINALS/kero.top`
- status: DUPLICATE
- inputs: kero.itp; kero_ATP.itp
- outputs: kero.itp; kero_ATP.itp
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `KEROGEN_ONLY_FINALS/kero_ATP.itp`
- status: DUPLICATE
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 00_CHECK_ENVIRONMENT.bat; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/kero.top; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/topol.top; 01_SCRIPTS/build_graphene_cases.py; 01_SCRIPTS/extract_kerogen_only_from_final.py; 01_SCRIPTS/extract_standard_kerogen_plate.py; 01_SCRIPTS/prepare_bulk.py; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p300/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p600/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/topol.top; 02_GRAPHENE_CASES/RMS_0p900/00_INITIAL/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/topol.top; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/topol.top; BLOCKERS.md; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/PUT_kero_ATP.itp_HERE.txt; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/00_INPUT_FORCEFIELD_COPY/kero.top; KEROGEN_ONLY_FINALS/kero.top; README_V32_4NM_PORE_RASPA2_GCMC.md; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md; docs/provenance/WATER_MODEL_REPORT.md

## `PROJECT_HISTORY.md`
- status: ACTIVE
- inputs: RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro; _EXACT_kerogen_plus_illite.gro
- outputs: RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro; _EXACT_kerogen_plus_illite.gro
- calls/imports: not explicit
- referenced by: RELEASE_MANIFEST_SHA256.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `RASPA2_WSL_DIAGNOSTIC_V35.txt`
- status: SUPERSEDED
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/diagnose_raspa2_wsl_v35.py; 56_DIAGNOSE_RASPA2_WSL_V35_ENCODING_SAFE.bat; README_V35_ENCODING_FIX.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `RASPA2_WSL_DIAGNOSTIC_V36.txt`
- status: UNKNOWN
- inputs: /home/baiheng/miniforge3/envs/raspa2/share/raspa/molecules/ExampleDefinitions/methane.def
- outputs: not explicit
- calls/imports: simulate
- referenced by: 01_SCRIPTS/diagnose_raspa2_wsl_v36.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 60_DIAGNOSE_RASPA2_WSL_V36_AUTODISCOVER.bat; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `README.md`
- status: ACTIVE
- inputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V33/GCMC_CH4_H2O_MOLECULE_COUNTS.csv; _EXACT_kerogen_plus_illite.gro; _kerogen_only_raw_from_final.gro
- outputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V33/GCMC_CH4_H2O_MOLECULE_COUNTS.csv; _EXACT_kerogen_plus_illite.gro; _kerogen_only_raw_from_final.gro
- calls/imports: simulate
- referenced by: RELEASE_MANIFEST_SHA256.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `README_V30_THICKER_ILLITE.md`
- status: ACTIVE
- inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro
- outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `README_V31_THICKER_ILLITE_SAFE.md`
- status: ACTIVE
- inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro
- outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `README_V32_4NM_PORE_RASPA2_GCMC.md`
- status: ACTIVE
- inputs: 00_INPUT/RASPA2_LOCAL/Tip5p.def; 00_INPUT/Tip5p.def; 00_INPUT/kero.itp; COMPOSITE_PORES_4NM_V32/{case}/{case}_COMPOSITE_PORE_4nm.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_EXACT_kerogen_plus_illite.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/RMS_0p000_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RASPA2_GCMC_4NM_V32/GCMC_CH4_H2O_MOLECULE_COUNTS.csv; Tip5p.def; _pore_build_report.csv; kero_ATP.itp
- outputs: 00_INPUT/kero.itp; COMPOSITE_PORES_4NM_V32/{case}/{case}_COMPOSITE_PORE_4nm.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_EXACT_kerogen_plus_illite.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/RMS_0p000_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RASPA2_GCMC_4NM_V32/GCMC_CH4_H2O_MOLECULE_COUNTS.csv; _pore_build_report.csv; kero_ATP.itp
- calls/imports: simulate
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `README_V35_ENCODING_FIX.md`
- status: UNKNOWN
- inputs: RASPA2_WSL_DIAGNOSTIC_V35.txt
- outputs: not explicit
- calls/imports: not explicit
- referenced by: RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md

## `README_V36_WSL_AUTODISCOVERY.md`
- status: UNKNOWN
- inputs: force_field_mixing_rules.def; pseudo_atoms.def
- outputs: not explicit
- calls/imports: simulate
- referenced by: RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md

## `RELEASE_MANIFEST_SHA256.json`
- status: UNKNOWN
- inputs: 8nm_pore_raspa2_config.json; requirements.txt
- outputs: 8nm_pore_raspa2_config.json
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; tools/make_release_manifest.py

## `config.json`
- status: DUPLICATE
- inputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- outputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/add_illite_below_raw_final_kerogen_v30.py; 01_SCRIPTS/add_illite_below_raw_final_kerogen_v31.py; 01_SCRIPTS/apply_graphene_patch_settings.py; 01_SCRIPTS/build_4nm_mirrored_pore.py; 01_SCRIPTS/build_8nm_mirrored_pore.py; 01_SCRIPTS/build_illite_under_kerogen.py; 01_SCRIPTS/collect_gcmc_counts.py; 01_SCRIPTS/common.py; 01_SCRIPTS/diagnose_raspa2_wsl_v34.py; 01_SCRIPTS/diagnose_raspa2_wsl_v35.py; 01_SCRIPTS/diagnose_raspa2_wsl_v36.py; 01_SCRIPTS/prepare_raspa2_gcmc.py; 01_SCRIPTS/run_raspa2_cases.py; 19_CONTINUE_RMS300_AFTER60_THEN_RUN600_900.bat; 24_BUILD_ILLITE_UNDER_KEROGEN_ALL.bat; 27_BUILD_RUN_RMS0_ONLY_NT8.bat; 28_RUN_ALL_RMS0_0300_0600_0900_FROM_SCRATCH_NT8.bat; 41_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ALL_V31.bat; 42_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ONE_V31.bat; 43_BUILD_4NM_COMPOSITE_PORES.bat; 44_PREPARE_RASPA2_GCMC.bat; 45_RUN_RASPA2_GCMC.bat; 46_COLLECT_GCMC_COUNTS.bat; 48_BUILD_8NM_COMPOSITE_PORES.bat; 49_PREPARE_RASPA2_GCMC_8NM.bat; 50_RUN_RASPA2_GCMC_8NM.bat; 51_COLLECT_GCMC_COUNTS_8NM.bat; 53_DIAGNOSE_RASPA2_WSL_V34.bat; 54_PREPARE_RASPA2_GCMC_8NM_V34.bat; 55_RUN_RASPA2_GCMC_8NM_V34_WSL.bat

## `config_normal_nt8.json`
- status: DUPLICATE
- inputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- outputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; 待定代码/07_REBUILD_GRAPHENE_CASES_PATCHED.bat; 待定代码/10_RUN_NORMAL_NT8_ALL_ROUGH.bat

## `config_normal_nt8_with_rms0.json`
- status: DUPLICATE
- inputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- outputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- calls/imports: not explicit
- referenced by: 28_RUN_ALL_RMS0_0300_0600_0900_FROM_SCRATCH_NT8.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `config_quick_test_nt14.json`
- status: DUPLICATE
- inputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- outputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; 待定代码/09_QUICK_TEST_RMS_0p300_NT14.bat

## `config_quick_test_nt14_with_rms0.json`
- status: DUPLICATE
- inputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- outputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md

## `config_resume_after60_nt8.json`
- status: ACTIVE
- inputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- outputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- calls/imports: not explicit
- referenced by: 19_CONTINUE_RMS300_AFTER60_THEN_RUN600_900.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `config_rms0_nt8.json`
- status: DUPLICATE
- inputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- outputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- calls/imports: not explicit
- referenced by: 27_BUILD_RUN_RMS0_ONLY_NT8.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `docs/audit/ACTIVE_PIPELINES.md`
- status: ACTIVE
- inputs: 00_INPUT/H2O.itp; 00_INPUT/RASPA2_LOCAL/Tip5p.def; 00_INPUT/Tip5p.def; 00_INPUT/kero.itp; 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; 00_em.gro; 00_em.mdp; 01_BULK/BULK_DENSIFICATION_REPORT.json; 02_GRAPHENE_CASES/GRAPHENE_BUILD_REPORT.json; 02_GRAPHENE_CASES/RMS_0p000/01_MDP/02_pull_ramp_01_20MPa.mdp; 02_GRAPHENE_CASES/RMS_0p000/01_MDP/02_pull_ramp_02_40MPa.mdp; 02_GRAPHENE_CASES/RMS_0p000/01_MDP/02_pull_ramp_03_60MPa.mdp; 02_GRAPHENE_CASES/RMS_0p000/01_MDP/03_pull_stage_01_700K_chunk01_50ps.mdp; 02_GRAPHENE_CASES/RMS_0p000/01_MDP/03_pull_stage_02_500K_chunk01_50ps.mdp; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p000_standard_kerogen_plate_metrics.json; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p000/CASE_METADATA.json; 02_GRAPHENE_CASES/RMS_0p000/PULL_FORCE_REPORT.json; 02_GRAPHENE_CASES/RMS_0p300/01_MDP/02_pull_ramp_01_20MPa.mdp; 02_GRAPHENE_CASES/RMS_0p300/01_MDP/02_pull_ramp_02_40MPa.mdp; 02_GRAPHENE_CASES/RMS_0p300/01_MDP/02_pull_ramp_03_60MPa.mdp; 02_GRAPHENE_CASES/RMS_0p300/01_MDP/03_pull_stage_01_700K_chunk01_50ps.mdp; 02_GRAPHENE_CASES/RMS_0p300/01_MDP/03_pull_stage_02_500K_chunk01_50ps.mdp; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p300_standard_kerogen_plate_metrics.json; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp; 02_GRAPHENE_CASES/RMS_0p300/CASE_METADATA.json; 02_GRAPHENE_CASES/RMS_0p300/PULL_FORCE_REPORT.json; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p600_standard_kerogen_plate_metrics.json; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp
- outputs: 00_INPUT/H2O.itp; 00_INPUT/kero.itp; 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; 00_em.gro; 01_BULK/BULK_DENSIFICATION_REPORT.json; 02_GRAPHENE_CASES/GRAPHENE_BUILD_REPORT.json; 02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p000_standard_kerogen_plate_metrics.json; 02_GRAPHENE_CASES/RMS_0p000/CASE_METADATA.json; 02_GRAPHENE_CASES/RMS_0p000/PULL_FORCE_REPORT.json; 02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p300_standard_kerogen_plate_metrics.json; 02_GRAPHENE_CASES/RMS_0p300/CASE_METADATA.json; 02_GRAPHENE_CASES/RMS_0p300/PULL_FORCE_REPORT.json; 02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p600_standard_kerogen_plate_metrics.json; 02_GRAPHENE_CASES/RMS_0p600/CASE_METADATA.json; 02_GRAPHENE_CASES/RMS_0p600/PULL_FORCE_REPORT.json; 02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p900_standard_kerogen_plate_metrics.json; 02_GRAPHENE_CASES/RMS_0p900/CASE_METADATA.json; 02_GRAPHENE_CASES/RMS_0p900/PULL_FORCE_REPORT.json; 02_GRAPHENE_CASES/RMS_xxx/02_RUN/STANDARD_KEROGEN_PLATE/RMS_xxx_standard_kerogen_plate.gro; 02_GRAPHENE_CASES/{case}/02_RUN/STANDARD_KEROGEN_PLATE/{case}_standard_kerogen_plate.gro; 02_GRAPHENE_CASES\RMS_0p000\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p000_standard_kerogen_plate.gro; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\02_pull_ramp_03_60MPa.gro; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\PULL_RUN_SUMMARY.csv; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate_metrics.csv; 02_GRAPHENE_CASES\RMS_0p600\00_INITIAL\system_initial.gro; 02_GRAPHENE_CASES\RMS_0p900\00_INITIAL\system_initial.gro; 02_GRAPHENE_CASES\STANDARD_PLATE_METRICS_ALL.csv; 02_pull_ramp_01_20MPa.gro
- calls/imports: not explicit
- referenced by: not found

## `docs/audit/FILE_DEPENDENCY_GRAPH.md`
- status: ACTIVE
- inputs: /home/baiheng/miniforge3/envs/raspa2/share/raspa/molecules/ExampleDefinitions/methane.def; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/RASPA2_LOCAL/Tip5p.def; 00_INPUT/Tip5p.def; 00_INPUT/illite.itp; 00_INPUT/illite.top; 00_INPUT/kero.itp; 00_INPUT/kero.top; 00_INPUT/kero_ATP.itp; 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; 00_INPUT\kero.itp; 00_INPUT\kero.pdb; 00_INPUT\kero.top; 00_INPUT\kero_ATP.itp; 00_em.gro; 00_em.mdp; 01_BULK/01_INITIAL/kero.itp; 01_BULK/01_INITIAL/kero_ATP.itp; 01_BULK/01_INITIAL/topol.top; 01_BULK/02_MDP/00_em.mdp; 01_BULK/02_MDP/03_nvt_lock_900K.mdp; 01_BULK/03_RUN/kero.itp; 01_BULK/03_RUN/kero_ATP.itp; 01_BULK/03_RUN/mdout.mdp; 01_BULK/03_RUN/topol.top; 01_BULK/BULK_BUILD_REPORT.json; 01_BULK/BULK_DENSIFICATION_REPORT.json; 02_GRAPHENE_CASES/GRAPHENE_BUILD_REPORT.json; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp
- outputs: 00_INPUT/illite.itp; 00_INPUT/illite.top; 00_INPUT/kero.itp; 00_INPUT/kero.top; 00_INPUT/kero_ATP.itp; 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; 00_INPUT\kero.itp; 00_INPUT\kero.pdb; 00_INPUT\kero.top; 00_INPUT\kero_ATP.itp; 00_em.gro; 01_BULK/01_INITIAL/kero.itp; 01_BULK/01_INITIAL/kero_ATP.itp; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/kero.itp; 01_BULK/03_RUN/kero_ATP.itp; 01_BULK/03_RUN/topol.top; 01_BULK/BULK_BUILD_REPORT.json; 01_BULK/BULK_DENSIFICATION_REPORT.json; 02_GRAPHENE_CASES/GRAPHENE_BUILD_REPORT.json; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT_posre_fixed.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP_posre_full.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP_posre_pull.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN_posre_fixed.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX_posre_fixed.itp
- calls/imports: SIMULATE; simulate
- referenced by: not found

## `docs/audit/VERSION_LINEAGE.md`
- status: UNKNOWN
- inputs: RASPA2_WSL_DIAGNOSTIC_V35.txt; RASPA2_WSL_DIAGNOSTIC_V36.txt; RASPA2_WSL_DIAGNOSTIC_v36.txt; illite_below_exact_final_kerogen_v28_config.json; illite_below_raw_final_kerogen_v29_config.json; illite_below_raw_final_kerogen_v30_config.json; illite_below_raw_final_kerogen_v31_config.json
- outputs: illite_below_exact_final_kerogen_v28_config.json; illite_below_raw_final_kerogen_v29_config.json; illite_below_raw_final_kerogen_v30_config.json; illite_below_raw_final_kerogen_v31_config.json
- calls/imports: not explicit
- referenced by: not found

## `docs/audit/WORKFLOW_GRAPH.md`
- status: ACTIVE
- inputs: 00_INPUT/H2O.itp; 00_INPUT/PUT_kero_ATP.itp_HERE.txt; 00_INPUT/illite.itp; 00_INPUT/illite.top; 00_INPUT/illite_ATP.itp; 00_INPUT/kero.itp; 00_INPUT/kero.top; 00_INPUT/kero_ATP.itp; 01_BULK/01_INITIAL/kero.itp; 01_BULK/01_INITIAL/kero_ATP.itp; 01_BULK/01_INITIAL/topol.top; 01_BULK/02_MDP/00_em.mdp; 01_BULK/02_MDP/01_nvt_01_300K.mdp; 01_BULK/02_MDP/01_nvt_02_600K.mdp; 01_BULK/02_MDP/01_nvt_03_900K.mdp; 01_BULK/02_MDP/02_npt_compress_001_100MPa.mdp; 01_BULK/02_MDP/02_npt_compress_002_100MPa.mdp; 01_BULK/02_MDP/02_npt_compress_003_100MPa.mdp; 01_BULK/02_MDP/02_npt_compress_004_100MPa.mdp; 01_BULK/02_MDP/02_npt_compress_005_100MPa.mdp; 01_BULK/02_MDP/02_npt_compress_006_100MPa.mdp; 01_BULK/02_MDP/02_npt_compress_007_100MPa.mdp; 01_BULK/02_MDP/02_npt_compress_008_60MPa.mdp; 01_BULK/02_MDP/02_npt_compress_009_60MPa.mdp; 01_BULK/02_MDP/02_npt_compress_010_60MPa.mdp; 01_BULK/02_MDP/02_npt_compress_011_60MPa.mdp; 01_BULK/02_MDP/02_npt_compress_012_60MPa.mdp; 01_BULK/02_MDP/02_npt_compress_013_60MPa.mdp; 01_BULK/02_MDP/02_npt_compress_014_60MPa.mdp; 01_BULK/02_MDP/02_npt_compress_015_40MPa.mdp
- outputs: 00_INPUT/H2O.itp; 00_INPUT/illite.itp; 00_INPUT/illite.top; 00_INPUT/illite_ATP.itp; 00_INPUT/kero.itp; 00_INPUT/kero.top; 00_INPUT/kero_ATP.itp; 01_BULK/01_INITIAL/kero.itp; 01_BULK/01_INITIAL/kero_ATP.itp; 01_BULK/01_INITIAL/topol.top; 01_BULK/03_RUN/kero.itp; 01_BULK/03_RUN/kero_ATP.itp; 01_BULK/03_RUN/topol.top; 02_GRAPHENE_CASES/GRAPHENE_BUILD_REPORT.json; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GBOT_posre_fixed.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP_posre_full.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GTOP_posre_pull.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMN_posre_fixed.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GXMX_posre_fixed.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMN_posre_fixed.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/GYMX_posre_fixed.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/kero.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/kero_ATP.itp; 02_GRAPHENE_CASES/RMS_0p000/00_INITIAL/topol.top
- calls/imports: not explicit
- referenced by: not found

## `docs/provenance/WATER_MODEL_REPORT.md`
- status: UNKNOWN
- inputs: 00_INPUT/H2O.itp; 00_INPUT/H2O.pdb; 00_INPUT/SiO2_quartz.pdb; 00_INPUT/illite.itp; 00_INPUT/illite.pdb; 00_INPUT/illite_ATP.itp; 00_INPUT/kero.itp; 00_INPUT/kero.pdb; 00_INPUT/kero_ATP.itp; Tip5p.def
- outputs: 00_INPUT/H2O.itp; 00_INPUT/H2O.pdb; 00_INPUT/SiO2_quartz.pdb; 00_INPUT/illite.itp; 00_INPUT/illite.pdb; 00_INPUT/illite_ATP.itp; 00_INPUT/kero.itp; 00_INPUT/kero.pdb; 00_INPUT/kero_ATP.itp
- calls/imports: not explicit
- referenced by: not found

## `illite_below_exact_final_kerogen_v28_config.json`
- status: ACTIVE
- inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro
- outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `illite_below_raw_final_kerogen_v29_config.json`
- status: SUPERSEDED
- inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro
- outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `illite_below_raw_final_kerogen_v30_config.json`
- status: SUPERSEDED
- inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro
- outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/add_illite_below_raw_final_kerogen_v30.py; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `illite_below_raw_final_kerogen_v31_config.json`
- status: ACTIVE
- inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro
- outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/add_illite_below_raw_final_kerogen_v31.py; 41_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ALL_V31.bat; 42_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ONE_V31.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/VERSION_LINEAGE.md; docs/audit/WORKFLOW_GRAPH.md

## `illite_under_kerogen_config.json`
- status: ACTIVE
- inputs: 02_GRAPHENE_CASES/{case}/02_RUN/STANDARD_KEROGEN_PLATE/{case}_standard_kerogen_plate.gro
- outputs: 02_GRAPHENE_CASES/{case}/02_RUN/STANDARD_KEROGEN_PLATE/{case}_standard_kerogen_plate.gro
- calls/imports: not explicit
- referenced by: 01_SCRIPTS/build_illite_under_kerogen.py; 24_BUILD_ILLITE_UNDER_KEROGEN_ALL.bat; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `postprocess_config.json`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md

## `requirements.txt`
- status: UNKNOWN
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: RELEASE_MANIFEST_SHA256.json; docs/audit/FILE_DEPENDENCY_GRAPH.md; docs/audit/WORKFLOW_GRAPH.md

## `tools/make_release_manifest.py`
- status: ACTIVE
- inputs: RELEASE_MANIFEST_SHA256.json
- outputs: RELEASE_MANIFEST_SHA256.json
- calls/imports: Path; __future__; annotations; hashlib; json; pathlib
- referenced by: README.md; RELEASE_MANIFEST_SHA256.json; docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `待定代码/06_RUN_ALL_CASES.bat`
- status: EXPERIMENTAL
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md

## `待定代码/07_REBUILD_GRAPHENE_CASES_PATCHED.bat`
- status: EXPERIMENTAL
- inputs: config.json; config_normal_nt8.json
- outputs: config.json; config_normal_nt8.json
- calls/imports: not explicit
- referenced by: docs/audit/FILE_DEPENDENCY_GRAPH.md

## `待定代码/08_RUN_ROUGH_CASES_PATCHED.bat`
- status: ACTIVE
- inputs: RMS_0p300/RMS_0p600/RMS_0p900 with current config.json
- outputs: RMS_0p300/RMS_0p600/RMS_0p900 with current config.json
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `待定代码/09_QUICK_TEST_RMS_0p300_NT14.bat`
- status: ACTIVE
- inputs: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\PULL_RUN_SUMMARY.csv; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate_metrics.csv; STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro; config.json; config_quick_test_nt14.json
- outputs: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\PULL_RUN_SUMMARY.csv; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate_metrics.csv; STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro; config.json; config_quick_test_nt14.json
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `待定代码/10_RUN_NORMAL_NT8_ALL_ROUGH.bat`
- status: ACTIVE
- inputs: config.json; config_normal_nt8.json
- outputs: config.json; config_normal_nt8.json
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `待定代码/11_EXPORT_RMS_0p300_VIEW_FILES.bat`
- status: ACTIVE
- inputs: VIEW_ALL_WALLS_ONLY.gro; VIEW_GTOP_ONLY.gro; VIEW_KERO_ONLY.gro
- outputs: VIEW_ALL_WALLS_ONLY.gro; VIEW_GTOP_ONLY.gro; VIEW_KERO_ONLY.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `待定代码/12_EXTRACT_STANDARD_PLATES_ONLY.bat`
- status: ACTIVE
- inputs: C\02_RUN\final_structure_pull.gro; final_structure_pull.gro
- outputs: C\02_RUN\final_structure_pull.gro; final_structure_pull.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md

## `待定代码/config_normal_nt8.json`
- status: EXPERIMENTAL
- inputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- outputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; 待定代码/07_REBUILD_GRAPHENE_CASES_PATCHED.bat; 待定代码/10_RUN_NORMAL_NT8_ALL_ROUGH.bat

## `待定代码/config_quick_test_nt14.json`
- status: EXPERIMENTAL
- inputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- outputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- calls/imports: not explicit
- referenced by: docs/audit/ACTIVE_PIPELINES.md; docs/audit/FILE_DEPENDENCY_GRAPH.md; 待定代码/09_QUICK_TEST_RMS_0p300_NT14.bat

## `待定代码/新建 文本文档.txt`
- status: EXPERIMENTAL
- inputs: not explicit
- outputs: not explicit
- calls/imports: not explicit
- referenced by: docs/audit/WORKFLOW_GRAPH.md
