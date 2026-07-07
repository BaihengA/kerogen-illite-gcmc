from __future__ import annotations

import csv
import json
import shlex
import shutil
import subprocess
from pathlib import Path

from asset_resolver import (
    AtomType,
    element_from_name,
    load_water_lj,
    mixing_line,
    parse_atomtypes,
    parse_cif_types,
    parse_pdb_atoms,
    parse_top_atoms,
    pseudo_line,
    read_base_ch4_entries,
    sha256_file,
)
from workflow_common import CODEBASE, PATHS, PROJECT_ROOT

RUN_DIR = CODEBASE / "workflows" / "08_gcmc_ch4_h2o" / "generated" / "RMS_0p300" / "P20MPa"
CONFIG = PROJECT_ROOT / "8nm_pore_raspa2_config.json"
SOURCE_CIF = PROJECT_ROOT / "COMPOSITE_PORES_8NM_V33" / "RMS_0p300" / "RMS_0p300_COMPOSITE_PORE_8nm_GEOMETRY_ONLY.cif"
SOURCE_BUILD_REPORT = PROJECT_ROOT / "COMPOSITE_PORES_8NM_V33" / "RMS_0p300" / "RMS_0p300_pore_build_report.json"
SOURCE_GRO = PROJECT_ROOT / "COMPOSITE_PORES_8NM_V33" / "RMS_0p300" / "RMS_0p300_COMPOSITE_PORE_8nm.gro"
STAGED_CIF = RUN_DIR / "RMS_0p300_Pore8nm.cif"
WATER_PDB = PROJECT_ROOT / "00_INPUT" / "H2O.pdb"
WATER_ITP = PROJECT_ROOT / "00_INPUT" / "H2O.itp"
KERO_ITP = PROJECT_ROOT / "00_INPUT" / "kero.itp"
ILLITE_ITP = PROJECT_ROOT / "00_INPUT" / "illite.itp"
KERO_ATP = PROJECT_ROOT / "00_INPUT" / "kero_ATP.itp"
ILLITE_ATP = PROJECT_ROOT / "00_INPUT" / "illite_ATP.itp"
WATER_LJ = CODEBASE / "docs" / "provenance" / "WATER_LJ_RESOLUTION.csv"


def win_to_wsl(path: Path) -> str:
    resolved = path.resolve()
    drive = resolved.drive.rstrip(":").lower()
    rest = str(resolved)[3:].replace("\\", "/")
    return f"/mnt/{drive}/{rest}"


def wsl_to_unc(path: str) -> Path:
    rel = path.strip("/").replace("/", "\\")
    return Path(rf"\\wsl.localhost\{PATHS['wsl_distro']}\{rel}")


def write_force_field_def(path: Path) -> None:
    path.write_text("# generated local override file: no explicit force-field override rules\n0\n0\n0\n", encoding="utf-8")


def build_h2o_def(path: Path) -> dict:
    top = list(parse_top_atoms(WATER_ITP).values())
    pdb = parse_pdb_atoms(WATER_PDB)
    if len(top) != len(pdb):
        raise RuntimeError(f"H2O atom count mismatch: PDB={len(pdb)} ITP={len(top)}")
    origin = pdb[0]
    lines = [
        "# critical constants: Temperature [T], Pressure [Pa], and Acentric factor [-]",
        "647.096",
        "22064000.0",
        "0.3443",
        "#Number Of Atoms",
        str(len(top)),
        "# Number of groups",
        "1",
        "# H2O-group",
        "rigid",
        "# number of atoms",
        str(len(top)),
        "# atomic positions",
    ]
    for i, (pdb_atom, top_atom) in enumerate(zip(pdb, top)):
        if pdb_atom.atomname != top_atom.atomname:
            raise RuntimeError(f"H2O atom order mismatch at index {i}: PDB={pdb_atom.atomname} ITP={top_atom.atomname}")
        raspa_type = f"H2O_{top_atom.atomname}"
        lines.append(f"{i} {raspa_type} {pdb_atom.x_A-origin.x_A:.12g} {pdb_atom.y_A-origin.y_A:.12g} {pdb_atom.z_A-origin.z_A:.12g}")
    lines += [
        "# Chiral centers Bond  BondDipoles Bend  UrayBradley InvBend  Torsion Imp. Torsion Bond/Bond Stretch/Bend Bend/Bend Stretch/Torsion Bend/Torsion IntraVDW IntraCoulomb",
        "               0    2            0    0            0       0        0            0         0            0         0               0            0        0            0",
        "# Bond stretch: atom n1-n2, type, parameters",
        "0 1 RIGID_BOND",
        "0 2 RIGID_BOND",
        "# Number of config moves",
        "0",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return {
        "source_pdb": str(WATER_PDB),
        "source_itp": str(WATER_ITP),
        "source_pdb_sha256": sha256_file(WATER_PDB),
        "source_itp_sha256": sha256_file(WATER_ITP),
        "staged_path": str(path),
        "sha256": sha256_file(path),
        "atom_count": len(top),
        "atom_order": [a.atomname for a in top],
    }


def framework_entries() -> tuple[list[str], list[str], list[dict]]:
    cif_types = parse_cif_types(SOURCE_CIF)
    kero_atoms = parse_top_atoms(KERO_ITP)
    illite_atoms = parse_top_atoms(ILLITE_ITP)
    atomtypes = parse_atomtypes([KERO_ATP, ILLITE_ATP])
    mix_lines: list[str] = []
    pseudo_lines: list[str] = []
    rows: list[dict] = []
    for raspa_type in sorted(cif_types):
        if raspa_type.startswith("kero_"):
            origin = "kerogen"
            atomname = raspa_type.removeprefix("kero_")
            top_atom = kero_atoms.get(atomname)
        elif raspa_type.startswith("illi_"):
            origin = "illite"
            atomname = raspa_type.removeprefix("illi_")
            top_atom = illite_atoms.get(atomname)
        else:
            top_atom = None
            origin = "unknown"
            atomname = raspa_type
        if top_atom is None or top_atom.atomtype not in atomtypes:
            rows.append({"atom_type": raspa_type, "origin": origin, "pseudo_atom_status": "FAIL", "mixing_rule_status": "FAIL", "sigma": "", "epsilon": "", "source_file": "", "status": "FAIL"})
            continue
        at = atomtypes[top_atom.atomtype]
        mix_lines.append(mixing_line(raspa_type, at.sigma_nm, at.epsilon_kj_mol))
        pseudo_lines.append(pseudo_line(raspa_type, element_from_name(atomname), top_atom.mass or at.mass, 0.0))
        rows.append({
            "atom_type": raspa_type,
            "origin": origin,
            "pseudo_atom_status": "PASS",
            "mixing_rule_status": "PASS",
            "sigma": f"{at.sigma_nm:.12g}",
            "epsilon": f"{at.epsilon_kj_mol:.12g}",
            "source_file": at.source_file,
            "status": "PASS",
        })
    return mix_lines, pseudo_lines, rows


def water_entries() -> tuple[list[str], list[str], list[dict]]:
    top = list(parse_top_atoms(WATER_ITP).values())
    atomtypes = load_water_lj(WATER_LJ)
    mix_lines: list[str] = []
    pseudo_lines: list[str] = []
    rows: list[dict] = []
    for top_atom in top:
        at = atomtypes[top_atom.atomtype]
        raspa_type = f"H2O_{top_atom.atomname}"
        mix_lines.append(mixing_line(raspa_type, at.sigma_nm, at.epsilon_kj_mol))
        pseudo_lines.append(pseudo_line(raspa_type, element_from_name(top_atom.atomname), top_atom.mass or at.mass, top_atom.charge))
        rows.append({"atom_type": raspa_type, "origin": "water", "pseudo_atom_status": "PASS", "mixing_rule_status": "PASS", "sigma": f"{at.sigma_nm:.12g}", "epsilon": f"{at.epsilon_kj_mol:.12g}", "source_file": at.source_file, "status": "PASS"})
    return mix_lines, pseudo_lines, rows


def write_forcefield(mix_lines: list[str], pseudo_lines: list[str]) -> None:
    (RUN_DIR / "force_field_mixing_rules.def").write_text(
        "# general rule for shifted vs truncated\nshifted\n# general rule tailcorrections\nno\n# number of defined interactions\n"
        + str(len(mix_lines))
        + "\n"
        + "\n".join(mix_lines)
        + "\n# general mixing rule for Lennard-Jones\nLorentz-Berthelot\n",
        encoding="utf-8",
    )
    (RUN_DIR / "pseudo_atoms.def").write_text(
        "# number of pseudo atoms\n"
        + str(len(pseudo_lines))
        + "\n# type print as chem oxidation mass charge polarization B-factor radii connectivity anisotropic anisotropic-type tinker-type\n"
        + "\n".join(pseudo_lines)
        + "\n",
        encoding="utf-8",
    )
    write_force_field_def(RUN_DIR / "force_field.def")


def write_coverage(rows: list[dict]) -> str:
    out = CODEBASE / "docs" / "audit" / "LOCAL_FORCEFIELD_COVERAGE.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = ["atom_type", "origin", "pseudo_atom_status", "mixing_rule_status", "sigma", "epsilon", "source_file", "status"]
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    mirror = PROJECT_ROOT / "docs" / "audit" / "LOCAL_FORCEFIELD_COVERAGE.csv"
    mirror.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out, mirror)
    return "PASS" if all(r["status"] == "PASS" for r in rows) else "FAIL"


def stage_framework() -> dict:
    shutil.copy2(SOURCE_CIF, STAGED_CIF)
    return {
        "source_gro": str(SOURCE_GRO),
        "source_build_report": str(SOURCE_BUILD_REPORT),
        "source": str(SOURCE_CIF),
        "staged_path": str(STAGED_CIF),
        "sha256": sha256_file(STAGED_CIF),
        "source_sha256": sha256_file(SOURCE_CIF),
        "status": "PASS" if sha256_file(STAGED_CIF) == sha256_file(SOURCE_CIF) else "FAIL",
    }


def materialize(run_type: str = "smoke") -> dict:
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    framework = stage_framework()
    fw_mix, fw_pseudo, fw_rows = framework_entries()
    water_mix, water_pseudo, water_rows = water_entries()
    ch4_mix, ch4_pseudo, ch4_source = read_base_ch4_entries(str(wsl_to_unc(PATHS["raspa2_root"])))
    mix_lines = [ch4_mix] + fw_mix + water_mix
    pseudo_lines = [ch4_pseudo] + fw_pseudo + water_pseudo
    write_forcefield(mix_lines, pseudo_lines)
    water_def = build_h2o_def(RUN_DIR / "H2O.def")
    forcefield_status = write_coverage([{"atom_type": "CH4", "origin": "methane ExampleDefinitions", "pseudo_atom_status": "PASS", "mixing_rule_status": "PASS", "sigma": "3.72", "epsilon": "158.5 K", "source_file": json.dumps(ch4_source), "status": "PASS"}] + fw_rows + water_rows)
    methane_def_wsl = f"{PATHS['raspa2_root']}/share/raspa/molecules/ExampleDefinitions/methane.def"
    methane_def_unc = wsl_to_unc(methane_def_wsl)
    manifest = {
        "case": "RMS_0p300",
        "run_type": run_type,
        "simulation_input": {"path": str(RUN_DIR / "simulation.input"), "sha256": sha256_file(RUN_DIR / "simulation.input")},
        "framework": framework,
        "local_forcefield": {
            "force_field_mixing_rules": {"source": "generated from RASPA CH4 base entry + project GROMACS atomtypes + water LJ", "staged_path": str(RUN_DIR / "force_field_mixing_rules.def"), "sha256": sha256_file(RUN_DIR / "force_field_mixing_rules.def")},
            "pseudo_atoms": {"source": "generated from RASPA CH4 base entry + project topology atom names/masses + water charges", "staged_path": str(RUN_DIR / "pseudo_atoms.def"), "sha256": sha256_file(RUN_DIR / "pseudo_atoms.def")},
            "force_field": {"source": "generated empty local override", "staged_path": str(RUN_DIR / "force_field.def"), "sha256": sha256_file(RUN_DIR / "force_field.def")},
        },
        "water_definition": water_def,
        "methane_definition": {"mode": "ExampleDefinitions", "resolved_path": methane_def_wsl, "sha256": sha256_file(methane_def_unc)},
        "wsl_run_directory": win_to_wsl(RUN_DIR),
        "status": "PASS" if framework["status"] == "PASS" and forcefield_status == "PASS" else "FAIL",
    }
    (RUN_DIR / "RUN_ASSET_MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def stage_framework_into_raspa(manifest: dict) -> dict:
    target = f"{PATHS['raspa2_root']}/share/raspa/structures/cif/RMS_0p300_Pore8nm.cif"
    source = manifest["framework"]["staged_path"]
    source_wsl = win_to_wsl(Path(source))
    expected = manifest["framework"]["sha256"]
    q_target = shlex.quote(target)
    q_source = shlex.quote(source_wsl)
    script = (
        f"set -e; "
        f"mkdir -p $(dirname {q_target}); "
        f"cp -f {q_source} {q_target}; "
        f"sha256sum {q_target} | cut -d ' ' -f 1"
    )
    proc = subprocess.run(["wsl", "-d", PATHS["wsl_distro"], "--", "bash", "-lc", script], capture_output=True, timeout=120)
    stdout = proc.stdout.decode("utf-8", errors="replace")
    stderr = proc.stderr.decode("utf-8", errors="replace")
    ok = proc.returncode == 0 and expected in stdout
    return {"resolved_path": target, "expected_sha256": expected, "stdout": stdout.strip(), "stderr": stderr.strip(), "exit_code": proc.returncode, "status": "PASS" if ok else "FAIL"}


if __name__ == "__main__":
    print(json.dumps(materialize(), indent=2))
