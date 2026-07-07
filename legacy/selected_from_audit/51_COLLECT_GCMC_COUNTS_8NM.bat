@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo V33 STEP 4: collect CH4 and H2O equilibrium molecule counts
echo ============================================================
python "01_SCRIPTS\collect_gcmc_counts.py" --config "8nm_pore_raspa2_config.json"
if errorlevel 1 (
  echo ERROR: result collection failed.
  pause
  exit /b 1
)
echo DONE. See RASPA2_GCMC_8NM_V33\GCMC_CH4_H2O_MOLECULE_COUNTS.csv
pause
