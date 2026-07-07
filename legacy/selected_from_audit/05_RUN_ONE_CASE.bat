@echo off
setlocal
cd /d "%~dp0"
echo Available cases:
for /d %%D in ("02_GRAPHENE_CASES\RMS_*") do echo   %%~nxD
echo.
set "CASE="
set /p "CASE=Enter case folder name [RMS_0p000]: "
if not defined CASE set "CASE=RMS_0p000"
python "01_SCRIPTS\run_wall_case.py" "%CASE%"
if errorlevel 1 (
  echo ERROR: Case stopped.
  echo Read logs in 02_GRAPHENE_CASES\%CASE%\02_RUN
  pause
  exit /b 1
)
echo CASE COMPLETED.
pause
