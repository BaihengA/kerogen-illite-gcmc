@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo Patch v25: build and run RMS_0p000 baseline only, SAFE 3ps NVT, preserving existing RMS_0p300/0p600/0p900
echo GROMACS mdrun uses: -ntmpi 1 -ntomp 8
echo Flow: EM ^> 900K 3ps NVT ^> 20/40/60MPa pressure imprint ^> 700K/500K anneal ^> kerogen-only extraction
echo ============================================================
copy /Y "config_rms0_nt8.json" "config.json" >nul
python "01_SCRIPTS\build_graphene_cases.py" --rms-list 0.0 --preserve-existing
if errorlevel 1 goto fail_build
python "01_SCRIPTS\generate_wall_mdps.py"
if errorlevel 1 goto fail_mdp
python "01_SCRIPTS\run_wall_case.py" "RMS_0p000"
if errorlevel 1 goto fail_run
python "01_SCRIPTS\extract_standard_kerogen_plate.py" "RMS_0p000"
if errorlevel 1 goto fail_extract
python "01_SCRIPTS\extract_kerogen_only_from_final.py" --cases "RMS_0p000" --raw --standard
if errorlevel 1 goto fail_extract
echo.
echo RMS_0p000 COMPLETED.
echo Standard plate: 02_GRAPHENE_CASES\RMS_0p000\02_RUN\STANDARD_KEROGEN_PLATE\RMS_0p000_standard_kerogen_plate.gro
echo Kerogen-only outputs: KEROGEN_ONLY_FINALS
pause
exit /b 0
:fail_build
echo ERROR: RMS_0p000 case construction failed.
pause
exit /b 1
:fail_mdp
echo ERROR: MDP generation failed.
pause
exit /b 1
:fail_run
echo ERROR: RMS_0p000 run stopped. Read 02_GRAPHENE_CASES\RMS_0p000\02_RUN logs.
pause
exit /b 1
:fail_extract
echo ERROR: kerogen-only extraction failed.
pause
exit /b 1
