# Active Pipelines

This file records the currently inferred formal pipelines. Items marked UNKNOWN require human confirmation before deletion or archival.

## bulk density

- `01_BULK/BULK_DENSIFICATION_REPORT.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\BULK_DENSITY_SUMMARY.csv; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\BULK_DENSITY_SUMMARY.csv; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- `01_SCRIPTS/run_bulk.py`; inputs: 00_em.mdp; 03_nvt_lock_900K.mdp; BULK_BUILD_REPORT.json; BULK_DENSIFICATION_REPORT.json; BULK_DENSITY_SUMMARY.csv; K.mdp; MPa.mdp; bulk_density_0p8_final.gro; bulk_initial_0p1.gro; index.ndx; topol.top; outputs: BULK_BUILD_REPORT.json; BULK_DENSIFICATION_REPORT.json; BULK_DENSITY_SUMMARY.csv; _grompp.log; _mdrun.log; _resume.log; bulk_density_0p8_final.gro; bulk_initial_0p1.gro; topol.top
- `02_GRAPHENE_CASES/GRAPHENE_BUILD_REPORT.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- `02_GRAPHENE_CASES/RMS_0p000/CASE_METADATA.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- `02_GRAPHENE_CASES/RMS_0p300/CASE_METADATA.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- `02_GRAPHENE_CASES/RMS_0p600/CASE_METADATA.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro
- `02_GRAPHENE_CASES/RMS_0p900/CASE_METADATA.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\01_BULK\\03_RUN\\bulk_density_0p8_final.gro

## graphene pressing

- No active script/config confidently identified by static audit.

## rough surface

- `01_SCRIPTS/analyze_rough_surface.py`; inputs: ROUGHNESS_METRICS_ALL.csv; _roughness_metrics.csv; _roughness_metrics.json; _standard_kerogen_plate.gro; _top_surface_grid.csv; args.inp; outputs: ROUGHNESS_METRICS_ALL.csv; _roughness_metrics.csv; _roughness_metrics.json; _standard_kerogen_plate.gro; _top_surface_grid.csv
- `01_SCRIPTS/build_graphene_cases.py`; inputs: CASE_METADATA.json; GRAPHENE_BUILD_REPORT.json; GTOP_posre_full.itp; GTOP_posre_pull.itp; _posre_fixed.itp; bulk_density_0p8_final.gro; index.ndx; kero.itp; kero.top; kero_ATP.itp; system_initial.gro; topol.top; outputs: CASE_METADATA.json; GRAPHENE_BUILD_REPORT.json; GTOP_posre_full.itp; GTOP_posre_pull.itp; _posre_fixed.itp; bulk_density_0p8_final.gro; kero.itp; kero.top; kero_ATP.itp; system_initial.gro; topol.top
- `01_SCRIPTS/build_quartz_under_kerogen.py`; inputs: QUARTZ_BUILD_REPORT_ALL.csv; _kerogen_oriented_rough_top.gro; _quartz_build_report.csv; _quartz_build_report.json; _quartz_nonbonded_snippet.itp; _quartz_under_kerogen_rough_top.gro; _quartz_wall.itp; _quartz_wall_only.gro; _standard_kerogen_plate.gro; _topol_include_snippet.txt; args.inp; outputs: QUARTZ_BUILD_REPORT_ALL.csv; _kerogen_oriented_rough_top.gro; _quartz_build_report.csv; _quartz_build_report.json; _quartz_nonbonded_snippet.itp; _quartz_under_kerogen_rough_top.gro; _quartz_wall.itp; _quartz_wall_only.gro; _standard_kerogen_plate.gro
- `01_SCRIPTS/continue_case_after_stage.py`; inputs: PULL_RUN_SUMMARY.csv; final_structure_pull.gro; system_initial.gro; outputs: PULL_RUN_SUMMARY.csv; final_structure_pull.gro; system_initial.gro
- `01_SCRIPTS/export_view_groups.py`; inputs: 00_em.gro; 02_pull_ramp_01_5MPa.gro; 02_pull_ramp_02_10MPa.gro; 03_pull_stage_01_900K_100ps.gro; 03_pull_stage_01_900K_chunk01_100ps.gro; VIEW_ALL_WALLS_ONLY.gro; VIEW_GROUPS_REPORT.json; VIEW_GTOP_ONLY.gro; VIEW_KERO_ONLY.gro; args.gro; final_structure_pull.gro; system_initial.gro; outputs: 00_em.gro; 02_pull_ramp_01_5MPa.gro; 02_pull_ramp_02_10MPa.gro; 03_pull_stage_01_900K_100ps.gro; 03_pull_stage_01_900K_chunk01_100ps.gro; VIEW_ALL_WALLS_ONLY.gro; VIEW_GROUPS_REPORT.json; VIEW_GTOP_ONLY.gro; VIEW_KERO_ONLY.gro; args.gro; final_structure_pull.gro; system_initial.gro
- `01_SCRIPTS/extract_standard_kerogen_plate.py`; inputs: CASE_METADATA.json; _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro; _standard_kerogen_plate_metrics.csv; _standard_kerogen_plate_metrics.json; args.inp; final_structure_pull.gro; kero.itp; kero.top; kero_ATP.itp; topol.top; outputs: CASE_METADATA.json; _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro; _standard_kerogen_plate_metrics.csv; _standard_kerogen_plate_metrics.json; final_structure_pull.gro; kero.itp; kero.top; kero_ATP.itp; topol.top
- `02_GRAPHENE_CASES/RMS_0p000/01_MDP/02_pull_ramp_01_20MPa.mdp`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p000/01_MDP/02_pull_ramp_02_40MPa.mdp`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p000/01_MDP/02_pull_ramp_03_60MPa.mdp`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p000/01_MDP/03_pull_stage_01_700K_chunk01_50ps.mdp`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p000/01_MDP/03_pull_stage_02_500K_chunk01_50ps.mdp`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p000/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p000_standard_kerogen_plate_metrics.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p000_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p000_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\final_structure_pull.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p000_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p000_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p000\\02_RUN\\final_structure_pull.gro
- `02_GRAPHENE_CASES/RMS_0p000/02_RUN/mdout.mdp`; inputs: mdout.mdp; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p000/PULL_FORCE_REPORT.json`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p300/01_MDP/02_pull_ramp_01_20MPa.mdp`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p300/01_MDP/02_pull_ramp_02_40MPa.mdp`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p300/01_MDP/02_pull_ramp_03_60MPa.mdp`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p300/01_MDP/03_pull_stage_01_700K_chunk01_50ps.mdp`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p300/01_MDP/03_pull_stage_02_500K_chunk01_50ps.mdp`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p300/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p300_standard_kerogen_plate_metrics.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p300_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p300_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\final_structure_pull.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p300_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p300_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p300\\02_RUN\\final_structure_pull.gro
- `02_GRAPHENE_CASES/RMS_0p300/02_RUN/mdout.mdp`; inputs: mdout.mdp; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p300/PULL_FORCE_REPORT.json`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p600/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p600_standard_kerogen_plate_metrics.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p600_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p600_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\final_structure_pull.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p600_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p600_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p600\\02_RUN\\final_structure_pull.gro
- `02_GRAPHENE_CASES/RMS_0p600/02_RUN/mdout.mdp`; inputs: mdout.mdp; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p600/PULL_FORCE_REPORT.json`; inputs: not explicit; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p900/02_RUN/STANDARD_KEROGEN_PLATE/RMS_0p900_standard_kerogen_plate_metrics.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p900_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p900_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\final_structure_pull.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p900_standard_kerogen_plate.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\STANDARD_KEROGEN_PLATE\\RMS_0p900_standard_kerogen_plate_PBC_VIEW_3x3.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\02_GRAPHENE_CASES\\RMS_0p900\\02_RUN\\final_structure_pull.gro
- `02_GRAPHENE_CASES/RMS_0p900/02_RUN/mdout.mdp`; inputs: mdout.mdp; outputs: not explicit
- `02_GRAPHENE_CASES/RMS_0p900/PULL_FORCE_REPORT.json`; inputs: not explicit; outputs: not explicit
- `05_RUN_ONE_CASE.bat`; inputs: not explicit; outputs: not explicit
- `19_CONTINUE_RMS300_AFTER60_THEN_RUN600_900.bat`; inputs: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\02_pull_ramp_03_60MPa.gro; 02_GRAPHENE_CASES\RMS_0p600\00_INITIAL\system_initial.gro; 02_GRAPHENE_CASES\RMS_0p900\00_INITIAL\system_initial.gro; 02_GRAPHENE_CASES\STANDARD_PLATE_METRICS_ALL.csv; config.json; config_resume_after60_nt8.json; outputs: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\02_pull_ramp_03_60MPa.gro; 02_GRAPHENE_CASES\RMS_0p600\00_INITIAL\system_initial.gro; 02_GRAPHENE_CASES\RMS_0p900\00_INITIAL\system_initial.gro; 02_GRAPHENE_CASES\STANDARD_PLATE_METRICS_ALL.csv; config.json; config_resume_after60_nt8.json
- `config_resume_after60_nt8.json`; inputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro; outputs: _standard_kerogen_plate.gro; _standard_kerogen_plate_PBC_VIEW_3x3.gro
- `待定代码/08_RUN_ROUGH_CASES_PATCHED.bat`; inputs: RMS_0p300/RMS_0p600/RMS_0p900 with current config.json; outputs: RMS_0p300/RMS_0p600/RMS_0p900 with current config.json
- `待定代码/09_QUICK_TEST_RMS_0p300_NT14.bat`; inputs: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\PULL_RUN_SUMMARY.csv; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate_metrics.csv; STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro; config.json; config_quick_test_nt14.json; outputs: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\PULL_RUN_SUMMARY.csv; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro; 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate_metrics.csv; STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro; config.json; config_quick_test_nt14.json
- `待定代码/10_RUN_NORMAL_NT8_ALL_ROUGH.bat`; inputs: config.json; config_normal_nt8.json; outputs: config.json; config_normal_nt8.json
- `待定代码/11_EXPORT_RMS_0p300_VIEW_FILES.bat`; inputs: VIEW_ALL_WALLS_ONLY.gro; VIEW_GTOP_ONLY.gro; VIEW_KERO_ONLY.gro; outputs: VIEW_ALL_WALLS_ONLY.gro; VIEW_GTOP_ONLY.gro; VIEW_KERO_ONLY.gro
- `待定代码/12_EXTRACT_STANDARD_PLATES_ONLY.bat`; inputs: C\02_RUN\final_structure_pull.gro; final_structure_pull.gro; outputs: C\02_RUN\final_structure_pull.gro; final_structure_pull.gro

## RAW kerogen extraction

- `01_SCRIPTS/extract_kerogen_only_from_final.py`; inputs: 02_pull_ramp_01_20MPa.gro; 02_pull_ramp_02_40MPa.gro; 02_pull_ramp_03_60MPa.gro; 02_pull_ramp_04_80MPa.gro; 03_pull_stage_01_700K_chunk01_50ps.gro; 03_pull_stage_02_500K_chunk01_50ps.gro; CASE_METADATA.json; KEROGEN_ONLY_FINALS_METRICS.csv; _kerogen_only_raw_from_final.gro; _kerogen_only_standard_plate.gro; final_structure_pull.gro; kero.itp; kero.top; kero_ATP.itp; outputs: 02_pull_ramp_01_20MPa.gro; 02_pull_ramp_02_40MPa.gro; 02_pull_ramp_03_60MPa.gro; 02_pull_ramp_04_80MPa.gro; 03_pull_stage_01_700K_chunk01_50ps.gro; 03_pull_stage_02_500K_chunk01_50ps.gro; CASE_METADATA.json; KEROGEN_ONLY_FINALS_METRICS.csv; _kerogen_only_raw_from_final.gro; _kerogen_only_standard_plate.gro; final_structure_pull.gro; kero.itp; kero.top; kero_ATP.itp
- `27_BUILD_RUN_RMS0_ONLY_NT8.bat`; inputs: 02_GRAPHENE_CASES\RMS_0p000\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p000_standard_kerogen_plate.gro; config.json; config_rms0_nt8.json; outputs: 02_GRAPHENE_CASES\RMS_0p000\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p000_standard_kerogen_plate.gro; config.json; config_rms0_nt8.json
- `28_RUN_ALL_RMS0_0300_0600_0900_FROM_SCRATCH_NT8.bat`; inputs: config.json; config_normal_nt8_with_rms0.json; outputs: config.json; config_normal_nt8_with_rms0.json
- `30_EXTRACT_KEROGEN_ONLY_FROM_ALL_FINALS.bat`; inputs: not explicit; outputs: not explicit
- `31_EXTRACT_KEROGEN_ONLY_EXISTING_0300_0600_0900.bat`; inputs: not explicit; outputs: not explicit

## illite wall

- `01_SCRIPTS/add_illite_below_raw_final_kerogen_v31.py`; inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro; RMS_xxx_kerogen_only_raw_from_final.gro; V31_BUILD_REPORT_ALL.csv; _EXACT_KEROGEN_INPUT_COPY.gro; _EXACT_kerogen_plus_illite.gro; _build_report.csv; _build_report.json; _illite_only.gro; _index.ndx; illite_below_raw_final_kerogen_v31_config.json; outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro; RMS_xxx_kerogen_only_raw_from_final.gro; V31_BUILD_REPORT_ALL.csv; _EXACT_KEROGEN_INPUT_COPY.gro; _EXACT_kerogen_plus_illite.gro; _build_report.csv; _build_report.json; _illite_only.gro; illite_below_raw_final_kerogen_v31_config.json
- `01_SCRIPTS/build_illite_under_kerogen.py`; inputs: 02_GRAPHENE_CASES/RMS_xxx/02_RUN/STANDARD_KEROGEN_PLATE/RMS_xxx_standard_kerogen_plate.gro; ILLITE_BUILD_REPORT_ALL.csv; ILLITE_BUILD_REPORT_ALL.json; ILLITE_UNDER_KEROGEN/RMS_xxx/RMS_xxx_ILLITE_SUPERCELL.itp; ILLITE_UNDER_KEROGEN/RMS_xxx/RMS_xxx_illite_under_kerogen.gro; _ILLITE_SUPERCELL.itp; _build_report.csv; _build_report.json; _composite_topol_template.top; _illite_only.gro; _illite_under_kerogen.gro; _illite_under_kerogen_PBC_VIEW_3x3.gro; _kerogen_oriented_rough_top.gro; _posre_illite.itp; forcefield.itp; illite_under_kerogen_config.json; kerogen.itp; m.gro; outputs: 02_GRAPHENE_CASES/RMS_xxx/02_RUN/STANDARD_KEROGEN_PLATE/RMS_xxx_standard_kerogen_plate.gro; ILLITE_BUILD_REPORT_ALL.csv; ILLITE_BUILD_REPORT_ALL.json; ILLITE_UNDER_KEROGEN/RMS_xxx/RMS_xxx_ILLITE_SUPERCELL.itp; ILLITE_UNDER_KEROGEN/RMS_xxx/RMS_xxx_illite_under_kerogen.gro; _ILLITE_SUPERCELL.itp; _build_report.csv; _build_report.json; _composite_topol_template.top; _illite_only.gro; _illite_under_kerogen.gro; _illite_under_kerogen_PBC_VIEW_3x3.gro; _kerogen_oriented_rough_top.gro; _posre_illite.itp; forcefield.itp; illite_under_kerogen_config.json; kerogen.itp; m.gro
- `41_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ALL_V31.bat`; inputs: KEROGEN_ONLY_FINALS\RAW_KEEP_COORDINATES\RMS_xxx_kerogen_only_raw_from_final.gro; illite_below_raw_final_kerogen_v31_config.json; outputs: KEROGEN_ONLY_FINALS\RAW_KEEP_COORDINATES\RMS_xxx_kerogen_only_raw_from_final.gro; illite_below_raw_final_kerogen_v31_config.json
- `42_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ONE_V31.bat`; inputs: illite_below_raw_final_kerogen_v31_config.json; outputs: illite_below_raw_final_kerogen_v31_config.json
- `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_build_report.json`; inputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p000_kerogen_only_raw_from_final.gro; final_structure_pull.gro; outputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p000_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p300/RMS_0p300_build_report.json`; inputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p300_kerogen_only_raw_from_final.gro; final_structure_pull.gro; outputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p300_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p600/RMS_0p600_build_report.json`; inputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p600_kerogen_only_raw_from_final.gro; final_structure_pull.gro; outputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p600_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p900/RMS_0p900_build_report.json`; inputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p900_kerogen_only_raw_from_final.gro; final_structure_pull.gro; outputs: 00_INPUT\\illite.gro; 00_INPUT\\illite.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_KEROGEN_INPUT_COPY.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p900_kerogen_only_raw_from_final.gro; final_structure_pull.gro
- `README_V30_THICKER_ILLITE.md`; inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro; outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro
- `README_V31_THICKER_ILLITE_SAFE.md`; inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro; outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro
- `illite_below_exact_final_kerogen_v28_config.json`; inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro; outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro
- `illite_below_raw_final_kerogen_v31_config.json`; inputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro; outputs: KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro
- `illite_under_kerogen_config.json`; inputs: 02_GRAPHENE_CASES/{case}/02_RUN/STANDARD_KEROGEN_PLATE/{case}_standard_kerogen_plate.gro; outputs: 02_GRAPHENE_CASES/{case}/02_RUN/STANDARD_KEROGEN_PLATE/{case}_standard_kerogen_plate.gro

## 8nm mirrored pore

- `01_SCRIPTS/build_8nm_mirrored_pore.py`; inputs: 8nm_pore_raspa2_config.json; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; PORE_8NM_BUILD_REPORT_ALL.csv; _COMPOSITE_PORE_8nm.gro; _EXACT_kerogen_plus_illite.gro; _LOWER_WALL.gro; _UPPER_WALL_MIRRORED.gro; _pore_build_report.csv; _pore_build_report.json; _wall_atom_mapping.csv; outputs: 8nm_pore_raspa2_config.json; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; PORE_8NM_BUILD_REPORT_ALL.csv; _COMPOSITE_PORE_8nm.gro; _EXACT_kerogen_plus_illite.gro; _LOWER_WALL.gro; _UPPER_WALL_MIRRORED.gro; _pore_build_report.csv; _pore_build_report.json; _wall_atom_mapping.csv
- `48_BUILD_8NM_COMPOSITE_PORES.bat`; inputs: 8nm_pore_raspa2_config.json; outputs: 8nm_pore_raspa2_config.json
- `49_PREPARE_RASPA2_GCMC_8NM.bat`; inputs: 8nm_pore_raspa2_config.json; outputs: 8nm_pore_raspa2_config.json
- `4nm_pore_raspa2_config.json`; inputs: 00_INPUT/kero.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; outputs: 00_INPUT/kero.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro
- `51_COLLECT_GCMC_COUNTS_8NM.bat`; inputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V33\GCMC_CH4_H2O_MOLECULE_COUNTS.csv; outputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V33\GCMC_CH4_H2O_MOLECULE_COUNTS.csv
- `8nm_pore_raspa2_config.json`; inputs: 00_INPUT/kero.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; outputs: 00_INPUT/kero.itp; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro
- `COMPOSITE_PORES_8NM_V33/RMS_0p000/RMS_0p000_pore_build_report.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p000_kerogen_only_raw_from_final.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p000\\RMS_0p000_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p000_kerogen_only_raw_from_final.gro
- `COMPOSITE_PORES_8NM_V33/RMS_0p300/RMS_0p300_pore_build_report.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p300_kerogen_only_raw_from_final.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p300\\RMS_0p300_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p300_kerogen_only_raw_from_final.gro
- `COMPOSITE_PORES_8NM_V33/RMS_0p600/RMS_0p600_pore_build_report.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p600_kerogen_only_raw_from_final.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p600\\RMS_0p600_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p600_kerogen_only_raw_from_final.gro
- `COMPOSITE_PORES_8NM_V33/RMS_0p900/RMS_0p900_pore_build_report.json`; inputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p900_kerogen_only_raw_from_final.gro; outputs: F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE\\RMS_0p900\\RMS_0p900_EXACT_kerogen_plus_illite.gro; F:\\MD\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\kerogen_bulk0p1_to0p8_then_graphene_pull_v1\\KEROGEN_ONLY_FINALS\\RAW_KEEP_COORDINATES\\RMS_0p900_kerogen_only_raw_from_final.gro
- `PROJECT_HISTORY.md`; inputs: RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro; _EXACT_kerogen_plus_illite.gro; outputs: RMS_0p000_kerogen_only_raw_from_final.gro; RMS_0p300_kerogen_only_raw_from_final.gro; RMS_0p600_kerogen_only_raw_from_final.gro; RMS_0p900_kerogen_only_raw_from_final.gro; _EXACT_kerogen_plus_illite.gro
- `README.md`; inputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V33/GCMC_CH4_H2O_MOLECULE_COUNTS.csv; _EXACT_kerogen_plus_illite.gro; _kerogen_only_raw_from_final.gro; outputs: 8nm_pore_raspa2_config.json; RASPA2_GCMC_8NM_V33/GCMC_CH4_H2O_MOLECULE_COUNTS.csv; _EXACT_kerogen_plus_illite.gro; _kerogen_only_raw_from_final.gro
- `README_V32_4NM_PORE_RASPA2_GCMC.md`; inputs: 00_INPUT/RASPA2_LOCAL/Tip5p.def; 00_INPUT/Tip5p.def; 00_INPUT/kero.itp; COMPOSITE_PORES_4NM_V32/{case}/{case}_COMPOSITE_PORE_4nm.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_EXACT_kerogen_plus_illite.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/RMS_0p000_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RASPA2_GCMC_4NM_V32/GCMC_CH4_H2O_MOLECULE_COUNTS.csv; Tip5p.def; _pore_build_report.csv; kero_ATP.itp; outputs: 00_INPUT/kero.itp; COMPOSITE_PORES_4NM_V32/{case}/{case}_COMPOSITE_PORE_4nm.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_EXACT_kerogen_plus_illite.gro; ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/RMS_0p000_kerogen_only_raw_from_final.gro; KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro; RASPA2_GCMC_4NM_V32/GCMC_CH4_H2O_MOLECULE_COUNTS.csv; _pore_build_report.csv; kero_ATP.itp
- `tools/make_release_manifest.py`; inputs: RELEASE_MANIFEST_SHA256.json; outputs: RELEASE_MANIFEST_SHA256.json

## RASPA2 GCMC

- No active script/config confidently identified by static audit.

## water model

- `00_INPUT/H2O.itp`; inputs: not explicit; outputs: not explicit

## diagnostics/reporting

- No active script/config confidently identified by static audit.

## unclassified

- No active script/config confidently identified by static audit.
## Corrected Formal GCMC Pipeline

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
## Corrected Formal GCMC Pipeline

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

