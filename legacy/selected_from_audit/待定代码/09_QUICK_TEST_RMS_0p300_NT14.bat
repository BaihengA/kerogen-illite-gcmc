@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo Patch v17 QUICK TEST: pull-COM-safe guarded mold, 3ps NVT, stronger pressure imprint
echo GROMACS mdrun uses: -ntmpi 1 -ntomp 14
echo Output after run: STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro
echo Existing 02_GRAPHENE_CASES\RMS_* will be backed up automatically.
echo ============================================================
copy /Y "config_quick_test_nt14.json" "config.json" >nul
python "01_SCRIPTS\build_graphene_cases.py"
if errorlevel 1 goto fail_build
python "01_SCRIPTS\generate_wall_mdps.py"
if errorlevel 1 goto fail_mdp
python "01_SCRIPTS\run_wall_case.py" "RMS_0p300"
if errorlevel 1 goto fail_run
python "01_SCRIPTS\extract_standard_kerogen_plate.py" "RMS_0p300"
if errorlevel 1 goto fail_extract
echo.
echo QUICK TEST COMPLETED.
echo Check: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\PULL_RUN_SUMMARY.csv
echo Check: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate.gro
echo Check: 02_GRAPHENE_CASES\RMS_0p300\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p300_standard_kerogen_plate_metrics.csv
pause
exit /b 0
:fail_build
echo ERROR: fixed-footprint graphene case construction failed.
pause
exit /b 1
:fail_mdp
echo ERROR: MDP generation failed.
pause
exit /b 1
:fail_run
echo ERROR: RMS_0p300 quick test stopped. Read logs in 02_GRAPHENE_CASES\RMS_0p300\02_RUN
pause
exit /b 1
:fail_extract
echo ERROR: standard kerogen plate extraction failed.
pause
exit /b 1
