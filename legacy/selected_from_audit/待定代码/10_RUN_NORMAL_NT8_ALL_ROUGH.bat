@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo Patch v17 NORMAL RUN: no-PBC-split fixed-footprint 0.300/0.600/0.900, 30ps NVT, stronger pressure imprint
echo GROMACS mdrun uses: -ntmpi 1 -ntomp 12
echo Existing 02_GRAPHENE_CASES\RMS_* will be backed up automatically.
echo ============================================================
copy /Y "config_normal_nt8.json" "config.json" >nul
python "01_SCRIPTS\build_graphene_cases.py"
if errorlevel 1 goto fail_build
python "01_SCRIPTS\generate_wall_mdps.py"
if errorlevel 1 goto fail_mdp
for %%C in (RMS_0p300 RMS_0p600 RMS_0p900) do (
    echo ------------------------------------------------------------
    echo Running %%C
    python "01_SCRIPTS\run_wall_case.py" "%%C"
    if errorlevel 1 goto fail_run
    python "01_SCRIPTS\extract_standard_kerogen_plate.py" "%%C"
    if errorlevel 1 goto fail_extract
)
echo.
echo NORMAL RUN COMPLETED.
echo Standard kerogen plates are in each case folder under 02_RUN\STANDARD_KEROGEN_PLATE
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
echo ERROR: one rough case stopped. Read its 02_RUN logs.
pause
exit /b 1
:fail_extract
echo ERROR: standard kerogen plate extraction failed.
pause
exit /b 1
