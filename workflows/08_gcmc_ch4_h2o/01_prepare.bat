@echo off
setlocal
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%..\..\"
python "src\gcmc\prepare.py"
if errorlevel 1 exit /b %errorlevel%
endlocal
