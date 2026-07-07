@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo Patch v24: remove graphene from existing roughness final structures only
echo Cases: RMS_0p300 RMS_0p600 RMS_0p900
echo ============================================================
python "01_SCRIPTS\extract_kerogen_only_from_final.py" --cases "RMS_0p300,RMS_0p600,RMS_0p900" --raw --standard
if errorlevel 1 goto fail
echo.
echo DONE. See KEROGEN_ONLY_FINALS.
pause
exit /b 0
:fail
echo ERROR: kerogen-only extraction failed.
pause
exit /b 1
