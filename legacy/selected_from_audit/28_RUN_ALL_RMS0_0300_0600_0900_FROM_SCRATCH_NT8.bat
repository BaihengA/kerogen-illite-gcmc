@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo Patch v24: FULL RERUN from scratch with RMS_0p000/0p300/0p600/0p900
echo WARNING: Existing 02_GRAPHENE_CASES\RMS_* will be backed up automatically.
echo GROMACS mdrun uses: -ntmpi 1 -ntomp 8
echo ============================================================
copy /Y "config_normal_nt8_with_rms0.json" "config.json" >nul
python "01_SCRIPTS\build_graphene_cases.py"
if errorlevel 1 goto fail_build
python "01_SCRIPTS\generate_wall_mdps.py"
if errorlevel 1 goto fail_mdp
for %%C in (RMS_0p000 RMS_0p300 RMS_0p600 RMS_0p900) do (
    echo ------------------------------------------------------------
    echo Running %%C
    python "01_SCRIPTS\run_wall_case.py" "%%C"
    if errorlevel 1 goto fail_run
    python "01_SCRIPTS\extract_standard_kerogen_plate.py" "%%C"
    if errorlevel 1 goto fail_extract
)
python "01_SCRIPTS\extract_kerogen_only_from_final.py" --cases "RMS_0p000,RMS_0p300,RMS_0p600,RMS_0p900" --raw --standard
if errorlevel 1 goto fail_extract
echo.
echo FULL RERUN COMPLETED.
pause
exit /b 0
:fail_build
echo ERROR: case construction failed.
pause
exit /b 1
:fail_mdp
echo ERROR: MDP generation failed.
pause
exit /b 1
:fail_run
echo ERROR: one case stopped. Read its 02_RUN logs.
pause
exit /b 1
:fail_extract
echo ERROR: extraction failed.
pause
exit /b 1
