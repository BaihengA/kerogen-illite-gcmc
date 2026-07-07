@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo V33 STEP 2: prepare RASPA2 CH4-H2O GCMC cases for 8 nm pores
echo Reservoir state is read from 8nm_pore_raspa2_config.json.
echo ============================================================
python "01_SCRIPTS\prepare_raspa2_gcmc.py" --config "8nm_pore_raspa2_config.json"
if errorlevel 1 (
  echo ERROR: RASPA2 preparation failed.
  echo Check 00_INPUT force-field files, RASPA_DIR, molecule definitions, and topology mapping.
  pause
  exit /b 1
)
echo DONE. See RASPA2_GCMC_8NM_V33
pause
