from __future__ import annotations

import json
from pathlib import Path

from thermodynamics import resolve_state, write_state
from run_materializer import materialize
from workflow_common import CODEBASE, PROJECT_ROOT

CONFIG = PROJECT_ROOT / "8nm_pore_raspa2_config.json"
STATE_PATH = CODEBASE / "docs" / "provenance" / "THERMODYNAMIC_STATE.json"
GENERATED = CODEBASE / "workflows" / "08_gcmc_ch4_h2o" / "generated" / "RMS_0p300" / "P20MPa"


def simulation_input(state) -> str:
    pressure_pa = float(state.pressure_MPa) * 1.0e6
    return "\n".join([
        "SimulationType MonteCarlo",
        "NumberOfCycles 1",
        "NumberOfInitializationCycles 1",
        "PrintEvery 1",
        "",
        "Forcefield Local",
        "RemoveAtomNumberCodeFromLabel yes",
        "UseChargesFromCIFFile yes",
        "ChargeMethod Ewald",
        "CutOff 12.0",
        "",
        "Framework 0",
        "FrameworkName RMS_0p300_Pore8nm",
        "UnitCells 1 1 1",
        "",
        f"ExternalTemperature {state.temperature_K:.12g}",
        f"ExternalPressure {pressure_pa:.12g}",
        "",
        "Component 0 MoleculeName methane",
        " MoleculeDefinition ExampleDefinitions",
        f" MolFraction {state.y_CH4:.15g}",
        f" FugacityCoefficient {state.phi_CH4:.15g}",
        " TranslationProbability 0.5",
        " ReinsertionProbability 0.5",
        " SwapProbability 1.0",
        " CreateNumberOfMolecules 0",
        "",
        "Component 1 MoleculeName H2O",
        " MoleculeDefinition Local",
        f" MolFraction {state.y_H2O:.15g}",
        f" FugacityCoefficient {state.phi_H2O:.15g}",
        " TranslationProbability 0.5",
        " RotationProbability 0.5",
        " ReinsertionProbability 0.5",
        " SwapProbability 1.0",
        " CreateNumberOfMolecules 0",
        "",
    ])


def main() -> int:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    state = resolve_state(cfg, methane_phi=0.8439459552)
    if state.status != "PASS":
        print("Thermodynamic state remains blocked; simulation.input was not generated.")
        write_state(STATE_PATH, state)
        return 2
    GENERATED.mkdir(parents=True, exist_ok=True)
    write_state(STATE_PATH, state)
    (GENERATED / "simulation.input").write_text(simulation_input(state), encoding="utf-8")
    (GENERATED / "RESERVOIR_STATE.json").write_text(json.dumps(state.__dict__, indent=2), encoding="utf-8")
    manifest = materialize(run_type="smoke")
    if manifest["status"] != "PASS":
        print("Run asset materialization failed; see RUN_ASSET_MANIFEST.json")
        return 3
    print(f"Generated audited simulation.input: {GENERATED / 'simulation.input'}")
    return 0


raise SystemExit(main())
