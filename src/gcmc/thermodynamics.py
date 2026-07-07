from __future__ import annotations

import json
import math
import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class ThermodynamicState:
    temperature_K: float
    pressure_MPa: float
    mixture_mode: str
    reservoir_reference: str
    pore_water_model: str
    y_CH4: float | None
    y_H2O: float | None
    phi_CH4: float | None
    phi_H2O: float | None
    f_CH4_Pa: float | None
    f_H2O_Pa: float | None
    CH4_method: str
    H2O_method: str
    reference_state: str
    pressure_correction: str
    water_activity: float | None
    iapws: dict[str, Any] | None
    assumptions: list[str]
    sources: list[str]
    status: str


def water_psat_pa_antoine_1_100C(temperature_K: float) -> float:
    temperature_C = temperature_K - 273.15
    if not (1.0 <= temperature_C <= 100.0):
        raise ValueError("Antoine water correlation is only configured for 1-100 C")
    A, B, C = 8.07131, 1730.63, 233.426
    return (10.0 ** (A - B / (C + temperature_C))) * 133.32236842105263


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_iapws95_water_reference(temperature_K: float, pressure_MPa: float, water_activity: float) -> dict[str, Any]:
    try:
        import iapws
        from iapws import IAPWS95
        import iapws.iapws95 as iapws95_module
    except Exception as exc:
        return {
            "status": "BLOCKED",
            "error": f"IAPWS95 import failed: {exc}",
        }

    sat_liq = IAPWS95(T=temperature_K, x=0)
    comp_liq = IAPWS95(T=temperature_K, P=pressure_MPa)
    module_path = Path(iapws95_module.__file__).resolve()
    f_reference_pa = float(comp_liq.f) * 1.0e6
    return {
        "status": "PASS",
        "package_name": "iapws",
        "package_version": getattr(iapws, "__version__", "unknown"),
        "module_path": str(module_path),
        "module_sha256": _sha256(module_path),
        "calculation_path": "iapws.IAPWS95(T=temperature_K, x=0) for saturation cross-check; iapws.IAPWS95(T=temperature_K, P=pressure_MPa) for compressed-liquid external water reference fugacity",
        "saturation_pressure_MPa": float(sat_liq.P),
        "saturation_liquid_fugacity_MPa": float(sat_liq.f),
        "compressed_liquid_pressure_MPa": float(comp_liq.P),
        "compressed_liquid_density_kg_m3": float(comp_liq.rho),
        "compressed_liquid_fugacity_MPa": float(comp_liq.f),
        "water_activity": water_activity,
        "f_H2O_reference_Pa": f_reference_pa,
        "f_H2O_Pa": water_activity * f_reference_pa,
    }


def resolve_state(config: dict, methane_phi: float | None = None) -> ThermodynamicState:
    T = float(config["temperature_K"])
    P_MPa = float(config["pressure_MPa"][0])
    P_Pa = P_MPa * 1e6
    mode = config.get("mixture_mode")
    if mode != "water_saturated_methane":
        raise ValueError(f"Unsupported canonical mode: {mode}")

    water_activity = float(config.get("water_activity", 1.0))
    reservoir_reference = str(config.get("water_reservoir_reference", "external_real_water_reference"))
    if reservoir_reference == "same_model_water_reference":
        assumptions = [
            "same_model_water_reference requires an independently calibrated OPLS 3-site bulk-water chemical potential.",
            "No calibrated same-model water reference is present in this audited codebase.",
        ]
        return ThermodynamicState(T, P_MPa, mode, reservoir_reference, "OPLS 3-site water from 00_INPUT/H2O.pdb and 00_INPUT/H2O.itp",
                                  None, None, methane_phi, None, None, None, "unresolved", "NOT_IMPLEMENTED",
                                  "same_model_water_reference", "none", water_activity, None, assumptions, [], "BLOCKED")
    if reservoir_reference != "external_real_water_reference":
        raise ValueError(f"Unsupported water_reservoir_reference: {reservoir_reference}")

    ant_psat = water_activity * water_psat_pa_antoine_1_100C(T)
    y_H2O = min(float(config.get("max_water_mole_fraction", 0.2)), ant_psat / P_Pa)
    y_CH4 = 1.0 - y_H2O
    iapws = resolve_iapws95_water_reference(T, P_MPa, water_activity)

    assumptions = [
        "CH4 phi may be taken from RASPA EOS only when proven by RASPA output for this T/P/composition class.",
        "water_saturated_methane means a water-saturated methane gas reservoir boundary in equilibrium with an external water reservoir.",
        "The external water reservoir uses real-water thermodynamics; the pore molecule remains the user's OPLS 3-site water model.",
        "Antoine Psat/P is retained only as a gas-composition/debug estimate and is not the production water fugacity source.",
        "No silent fallback to phi=1 is allowed for production.",
    ]
    sources = ["8nm_pore_raspa2_config.json", "docs/provenance/RASPA_FUGACITY_BEHAVIOR.md", "docs/provenance/IAPWS_WATER_REFERENCE_VALIDATION.md"]
    if methane_phi is None or iapws.get("status") != "PASS":
        return ThermodynamicState(T, P_MPa, mode, reservoir_reference, "OPLS 3-site water from 00_INPUT/H2O.pdb and 00_INPUT/H2O.itp",
                                  y_CH4, y_H2O, methane_phi, None, None, iapws.get("f_H2O_Pa"),
                                  "unresolved", "IAPWS-95 external compressed-liquid water fugacity" if iapws.get("status") == "PASS" else "unresolved",
                                  "compressed liquid water at T and P_total", "IAPWS compressed-liquid fugacity relative to saturation reference", water_activity, iapws,
                                  assumptions, sources, "BLOCKED")

    f_CH4 = y_CH4 * methane_phi * P_Pa
    f_H2O = float(iapws["f_H2O_Pa"])
    phi_H2O = f_H2O / (y_H2O * P_Pa)
    return ThermodynamicState(
        T, P_MPa, mode, reservoir_reference, "OPLS 3-site water from 00_INPUT/H2O.pdb and 00_INPUT/H2O.itp",
        y_CH4, y_H2O, methane_phi, phi_H2O, f_CH4, f_H2O,
        "RASPA internal EOS methane fugacity coefficient proven by 0-cycle probe",
        "IAPWS-95 external compressed-liquid water fugacity, scaled by water_activity",
        "compressed liquid water at T and P_total",
        "IAPWS compressed-liquid fugacity includes pressure correction from saturation to P_total",
        water_activity, iapws, assumptions, sources, "PASS"
    )


def write_state(path: Path, state: ThermodynamicState) -> None:
    path.write_text(json.dumps(state.__dict__, indent=2), encoding="utf-8")
