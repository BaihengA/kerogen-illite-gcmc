@echo off
setlocal
cd /d "%~dp0"
if "%~1"=="" (
  echo Usage: %~nx0 RMS_0p300
  pause
  exit /b 1
)
echo ============================================================
echo V31 THICKER ONE CASE: %~1
echo Uses RAW_KEEP_COORDINATES exact final kerogen only.
echo ============================================================
python "01_SCRIPTS\add_illite_below_raw_final_kerogen_v31.py" --config "illite_below_raw_final_kerogen_v31_config.json" --case "%~1"
if errorlevel 1 (
  echo ERROR: V31 thicker-illite one-case build failed.
  pause
  exit /b 1
)
echo DONE.
pause
