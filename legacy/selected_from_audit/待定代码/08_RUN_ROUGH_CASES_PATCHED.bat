@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo Patch v17: run RMS_0p300/RMS_0p600/RMS_0p900 with current config.json
echo ============================================================
for %%C in (RMS_0p300 RMS_0p600 RMS_0p900) do (
    python "01_SCRIPTS\run_wall_case.py" "%%C"
    if errorlevel 1 goto fail_run
    python "01_SCRIPTS\extract_standard_kerogen_plate.py" "%%C"
    if errorlevel 1 goto fail_extract
)
echo ALL ROUGH CASES COMPLETED.
pause
exit /b 0
:fail_run
echo ERROR: one case stopped. Read its logs.
pause
exit /b 1
:fail_extract
echo ERROR: standard kerogen plate extraction failed.
pause
exit /b 1
