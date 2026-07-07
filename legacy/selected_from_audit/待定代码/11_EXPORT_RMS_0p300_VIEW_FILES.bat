@echo off
setlocal
cd /d "%~dp0"

echo ============================================================
echo Export view-only GRO files for RMS_0p300
echo This does NOT run MD. It only writes:
echo   VIEW_GTOP_ONLY.gro       (top rough graphene piston only)
echo   VIEW_ALL_WALLS_ONLY.gro  (six graphene walls only)
echo   VIEW_KERO_ONLY.gro       (kerogen only)
echo ============================================================

python "01_SCRIPTS\export_view_groups.py" "RMS_0p300"
if errorlevel 1 (
  echo ERROR: view export failed.
  pause
  exit /b 1
)

echo DONE. Open 02_GRAPHENE_CASES\RMS_0p300\02_RUN\VIEW_GTOP_ONLY.gro to check the rectangular top piston.
pause
