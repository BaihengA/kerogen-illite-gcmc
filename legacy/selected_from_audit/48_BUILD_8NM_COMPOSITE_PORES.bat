@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo V33 STEP 1: build 8 nm mirrored kerogen+illite composite pores
echo Lower wall is the V31 composite wall; upper wall is exact z-mirror.
echo Nominal pore width: 8.0 nm between mean rough-surface planes.
echo ============================================================
python "01_SCRIPTS\build_8nm_mirrored_pore.py" --config "8nm_pore_raspa2_config.json"
if errorlevel 1 (
  echo ERROR: 8 nm pore construction failed.
  pause
  exit /b 1
)
echo DONE. See COMPOSITE_PORES_8NM_V33
pause
