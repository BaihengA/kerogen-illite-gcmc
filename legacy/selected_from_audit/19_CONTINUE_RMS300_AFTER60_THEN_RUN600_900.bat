@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo Patch v19 ONE-TIME RESUME
echo 1) Do NOT rebuild cases; keep current RMS_0p300 results.
echo 2) Continue RMS_0p300 from 02_pull_ramp_03_60MPa to 03 NVT/annealing stages.
echo 3) Then run RMS_0p600 and RMS_0p900 full workflow with the same 20/40/60 MPa + NVT schedule.
echo GROMACS mdrun uses: -ntmpi 1 -ntomp 8
echo ============================================================

if not exist "02_GRAPHENE_CASES\RMS_0p300\02_RUN\02_pull_ramp_03_60MPa.gro" goto missing300
if not exist "02_GRAPHENE_CASES\RMS_0p600\00_INITIAL\system_initial.gro" goto missing600
if not exist "02_GRAPHENE_CASES\RMS_0p900\00_INITIAL\system_initial.gro" goto missing900

copy /Y "config_resume_after60_nt8.json" "config.json" >nul
if errorlevel 1 goto fail_config

echo.
echo [1/5] Regenerating MDP files only. This does NOT rebuild or backup existing cases.
python "01_SCRIPTS\generate_wall_mdps.py"
if errorlevel 1 goto fail_mdp

echo.
echo [2/5] Continue RMS_0p300 after 02_pull_ramp_03_60MPa, run only 03_pull_stage NVT/annealing.
python "01_SCRIPTS\continue_case_after_stage.py" "RMS_0p300" --from-stage "02_pull_ramp_03_60MPa" --run-annealing
if errorlevel 1 goto fail_resume300
python "01_SCRIPTS\extract_standard_kerogen_plate.py" "RMS_0p300"
if errorlevel 1 goto fail_extract300

echo.
echo [3/5] Run RMS_0p600 full workflow, no rebuild.
python "01_SCRIPTS\run_wall_case.py" "RMS_0p600"
if errorlevel 1 goto fail_run600
python "01_SCRIPTS\extract_standard_kerogen_plate.py" "RMS_0p600"
if errorlevel 1 goto fail_extract600

echo.
echo [4/5] Run RMS_0p900 full workflow, no rebuild.
python "01_SCRIPTS\run_wall_case.py" "RMS_0p900"
if errorlevel 1 goto fail_run900
python "01_SCRIPTS\extract_standard_kerogen_plate.py" "RMS_0p900"
if errorlevel 1 goto fail_extract900

echo.
echo [5/5] Collect standard plate metrics.
python "01_SCRIPTS\collect_standard_plate_metrics.py"
if errorlevel 1 goto fail_collect

echo.
echo PATCH V19 RESUME + RMS_0p600/RMS_0p900 COMPLETED.
echo Check: 02_GRAPHENE_CASES\STANDARD_PLATE_METRICS_ALL.csv
pause
exit /b 0

:missing300
echo ERROR: Missing 02_GRAPHENE_CASES\RMS_0p300\02_RUN\02_pull_ramp_03_60MPa.gro
echo Finish or locate the existing RMS_0p300 60MPa output first. This script will not rebuild RMS_0p300.
pause
exit /b 1
:missing600
echo ERROR: Missing RMS_0p600 initial case. Do not use this resume script until RMS_0p600 case exists.
echo If you need to build cases, back up your current RMS_0p300 folder first.
pause
exit /b 1
:missing900
echo ERROR: Missing RMS_0p900 initial case. Do not use this resume script until RMS_0p900 case exists.
echo If you need to build cases, back up your current RMS_0p300 folder first.
pause
exit /b 1
:fail_config
echo ERROR: Could not copy config_resume_after60_nt8.json to config.json.
pause
exit /b 1
:fail_mdp
echo ERROR: MDP generation failed. Existing GRO results were not deleted.
pause
exit /b 1
:fail_resume300
echo ERROR: RMS_0p300 resume from 60MPa failed. Read RMS_0p300\02_RUN logs.
pause
exit /b 1
:fail_extract300
echo ERROR: RMS_0p300 standard plate extraction failed.
pause
exit /b 1
:fail_run600
echo ERROR: RMS_0p600 run failed. Read RMS_0p600\02_RUN logs.
pause
exit /b 1
:fail_extract600
echo ERROR: RMS_0p600 standard plate extraction failed.
pause
exit /b 1
:fail_run900
echo ERROR: RMS_0p900 run failed. Read RMS_0p900\02_RUN logs.
pause
exit /b 1
:fail_extract900
echo ERROR: RMS_0p900 standard plate extraction failed.
pause
exit /b 1
:fail_collect
echo ERROR: metrics collection failed.
pause
exit /b 1
