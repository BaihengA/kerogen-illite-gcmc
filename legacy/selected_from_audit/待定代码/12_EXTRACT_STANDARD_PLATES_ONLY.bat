@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo Patch v13: extract standardized kerogen-only plates from existing final_structure_pull.gro
echo ============================================================
for %%C in (RMS_0p300 RMS_0p600 RMS_0p900) do (
    if exist "02_GRAPHENE_CASES\%%C\02_RUN\final_structure_pull.gro" (
        python "01_SCRIPTS\extract_standard_kerogen_plate.py" "%%C"
    ) else (
        echo SKIP %%C: final_structure_pull.gro not found
    )
)
pause
