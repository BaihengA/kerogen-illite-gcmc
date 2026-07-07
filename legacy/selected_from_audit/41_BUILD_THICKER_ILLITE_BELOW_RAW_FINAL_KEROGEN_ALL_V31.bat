@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo V31 THICKER: add illite below EXACT RAW final kerogen plates
echo INPUT fixed to:
echo KEROGEN_ONLY_FINALS\RAW_KEEP_COORDINATES\RMS_xxx_kerogen_only_raw_from_final.gro
echo Kerogen coordinates will NOT be changed.
echo ============================================================
python "01_SCRIPTS\add_illite_below_raw_final_kerogen_v31.py" --config "illite_below_raw_final_kerogen_v31_config.json"
if errorlevel 1 (
  echo ERROR: V31 thicker-illite build failed.
  pause
  exit /b 1
)
echo DONE.
pause
