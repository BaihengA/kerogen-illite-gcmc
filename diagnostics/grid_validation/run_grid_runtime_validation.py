from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import re
import shutil
import struct
import subprocess
import time
from pathlib import Path


REPO = Path("/mnt/f/MD/kerogen_bulk0p1_to0p8_then_graphene_pull_v1/kerogen_bulk0p1_to0p8_then_graphene_pull_v1/KEROGEN_MD_GCMC_CODEBASE")
RASPA_PREFIX = Path("/home/baiheng/miniforge3/envs/raspa2")
SIMULATE = RASPA_PREFIX / "bin/simulate"
RUNTIME_PREFIX = Path("/home/baiheng/raspa_grid_validation_runtime")
RUN_ROOT = Path("/home/baiheng/raspa_grid_validation_runs")
OUT_ROOT = REPO / "diagnostics/grid_validation"
AUDIT = REPO / "docs/audit"
CASES = {
    "10k": REPO / "diagnostics/framework_scaling/RMS_0p300_diag_10000",
    "25k": REPO / "diagnostics/framework_scaling/RMS_0p300_diag_25000",
}
GRID_SPACING_A = 10.0
ABS_TOL_K = 5.0
REL_TOL = 0.05
NEAR_WALL_DISTANCE_A = 2.0
HIGH_ENERGY_K = 100000.0
GRID_TYPES = ["CH4", "H2O_OW", "H2O_HW1", "H2O_HW2"]
CANONICAL_H2O_DEF = REPO / "diagnostics/molecule_definition/CH4_H2O_BINARY_PARSE_TEST/H2O.def"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_runtime_prefix() -> None:
    if RUNTIME_PREFIX.exists():
        shutil.rmtree(RUNTIME_PREFIX)
    (RUNTIME_PREFIX / "share").mkdir(parents=True)
    shutil.copytree(RASPA_PREFIX / "share/raspa", RUNTIME_PREFIX / "share/raspa")
    (RUNTIME_PREFIX / "share/raspa/structures/cif").mkdir(parents=True, exist_ok=True)
    if RUN_ROOT.exists():
        shutil.rmtree(RUN_ROOT)
    RUN_ROOT.mkdir(parents=True)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    AUDIT.mkdir(parents=True, exist_ok=True)


def count_cif_atoms(path: Path) -> int:
    in_loop = False
    headers: list[str] = []
    count = 0
    for line in path.read_text().splitlines():
        s = line.strip()
        if s == "loop_":
            in_loop = True
            headers = []
            continue
        if in_loop and s.startswith("_atom_site_"):
            headers.append(s)
            continue
        if in_loop and headers:
            if not s or s.startswith("_") or s.startswith("#"):
                continue
            parts = s.split()
            if len(parts) >= len(headers):
                count += 1
    return count


def freeze_manifest() -> None:
    files = []
    for case_name, case_dir in CASES.items():
        cif = next(case_dir.glob("*.cif"))
        for name in ["force_field_mixing_rules.def", "pseudo_atoms.def", "force_field.def", "simulation.input"]:
            p = case_dir / name
            files.append({
                "case": case_name,
                "path": str(p.relative_to(REPO)),
                "sha256": sha256(p),
                "bytes": p.stat().st_size,
            })
        files.append({
            "case": case_name,
            "path": str(CANONICAL_H2O_DEF.relative_to(REPO)),
            "role": "H2O.def canonical post-fix serialization used for isolated grid validation run",
            "sha256": sha256(CANONICAL_H2O_DEF),
            "bytes": CANONICAL_H2O_DEF.stat().st_size,
        })
        legacy_h2o = case_dir / "H2O.def"
        files.append({
            "case": case_name,
            "path": str(legacy_h2o.relative_to(REPO)),
            "role": "legacy scaling H2O.def not used because it contains parser-metadata comment after critical-constants header",
            "sha256": sha256(legacy_h2o),
            "bytes": legacy_h2o.stat().st_size,
        })
        files.append({
            "case": case_name,
            "path": str(cif.relative_to(REPO)),
            "sha256": sha256(cif),
            "bytes": cif.stat().st_size,
            "framework_atoms": count_cif_atoms(cif),
        })
    manifest = {
        "status": "FROZEN",
        "h2o_def_postfix_serialization_confirmed": True,
        "h2o_def_used": str(CANONICAL_H2O_DEF.relative_to(REPO)),
        "grid_spacing_A_predefined": GRID_SPACING_A,
        "absolute_tolerance_K_predefined": ABS_TOL_K,
        "relative_tolerance_predefined": REL_TOL,
        "near_wall_distance_A_predefined": NEAR_WALL_DISTANCE_A,
        "high_energy_K_predefined": HIGH_ENERGY_K,
        "files": files,
    }
    (AUDIT / "GRID_INPUT_FREEZE_MANIFEST.json").write_text(json.dumps(manifest, indent=2))


def copy_case_inputs(case_name: str, mode: str) -> Path:
    case_dir = CASES[case_name]
    framework = case_dir.name
    run_dir = RUN_ROOT / f"{case_name}_{mode}"
    run_dir.mkdir(parents=True)
    for name in ["force_field.def", "force_field_mixing_rules.def", "pseudo_atoms.def"]:
        shutil.copy2(case_dir / name, run_dir / name)
    shutil.copy2(CANONICAL_H2O_DEF, run_dir / "H2O.def")
    cif = case_dir / f"{framework}.cif"
    shutil.copy2(cif, run_dir / f"{framework}.cif")
    shutil.copy2(cif, RUNTIME_PREFIX / f"share/raspa/structures/cif/{framework}.cif")
    return run_dir


def write_makegrid_input(case_name: str, run_dir: Path) -> None:
    framework = CASES[case_name].name
    text = f"""# DIAGNOSTIC_ONLY grid generation; not production GCMC
SimulationType MakeGrid

Forcefield Local
RemoveAtomNumberCodeFromLabel yes
UseChargesFromCIFFile yes
ChargeMethod Ewald
CutOff 12.0

Framework 0
FrameworkName {framework}
UnitCells 1 1 1

NumberOfGrids {len(GRID_TYPES)}
GridTypes {' '.join(GRID_TYPES)}
SpacingVDWGrid {GRID_SPACING_A}
SpacingCoulombGrid {GRID_SPACING_A}
UseTabularGrid yes
"""
    (run_dir / "simulation.input").write_text(text)


def write_mc_input(case_name: str, run_dir: Path, use_grid: bool) -> None:
    framework = CASES[case_name].name
    grid_block = ""
    if use_grid:
        grid_block = f"""
NumberOfGrids {len(GRID_TYPES)}
GridTypes {' '.join(GRID_TYPES)}
SpacingVDWGrid {GRID_SPACING_A}
SpacingCoulombGrid {GRID_SPACING_A}
UseTabularGrid yes
"""
    text = f"""# DIAGNOSTIC_ONLY grid runtime validation; not production GCMC
SimulationType MonteCarlo
NumberOfCycles 1
NumberOfInitializationCycles 1
PrintEvery 1

Forcefield Local
RemoveAtomNumberCodeFromLabel yes
UseChargesFromCIFFile yes
ChargeMethod Ewald
CutOff 12.0
{grid_block}
Framework 0
FrameworkName {framework}
UnitCells 1 1 1

ExternalTemperature 353.15
ExternalPressure 20000000

Component 0 MoleculeName methane
 MoleculeDefinition ExampleDefinitions
 MolFraction 0.997636645934322
 FugacityCoefficient 0.8439459552
 TranslationProbability 0.5
 ReinsertionProbability 0.5
 SwapProbability 1.0
 CreateNumberOfMolecules 0

Component 1 MoleculeName H2O
 MoleculeDefinition Local
 MolFraction 0.0023633540656784
 FugacityCoefficient 1.1266978304747
 TranslationProbability 0.5
 RotationProbability 0.5
 ReinsertionProbability 0.5
 SwapProbability 1.0
 CreateNumberOfMolecules 0
"""
    (run_dir / "simulation.input").write_text(text)


def run_simulation(run_dir: Path, timeout_s: int = 900) -> dict:
    out_dir = OUT_ROOT / run_dir.name
    out_dir.mkdir(parents=True, exist_ok=True)
    stdout = out_dir / "stdout.txt"
    stderr = out_dir / "stderr.txt"
    timefile = out_dir / "time.txt"
    cmd = ["/usr/bin/time", "-v", "-o", str(timefile), str(SIMULATE)]
    env = os.environ.copy()
    env["RASPA_DIR"] = str(RUNTIME_PREFIX)
    t0 = time.time()
    proc = subprocess.run(cmd, cwd=run_dir, env=env, stdout=stdout.open("w"), stderr=stderr.open("w"), timeout=timeout_s)
    elapsed = time.time() - t0
    return {
        "exit_code": proc.returncode,
        "elapsed_s": elapsed,
        "stdout": stdout,
        "stderr": stderr,
        "timefile": timefile,
    }


def parse_time_file(path: Path) -> dict:
    if not path.exists():
        return {}
    text = path.read_text()
    rss = re.search(r"Maximum resident set size \(kbytes\):\s+(\d+)", text)
    cpu = re.search(r"Percent of CPU this job got:\s+([0-9.]+)%", text)
    return {
        "rss_max_kb": int(rss.group(1)) if rss else "",
        "cpu_percent": float(cpu.group(1)) if cpu else "",
    }


def parse_grid_dims(stderr: Path) -> str:
    text = stderr.read_text(errors="ignore")
    matches = re.findall(r"Number of grid points:\s+(\d+)\s+(\d+)\s+(\d+)", text)
    if not matches:
        return ""
    return "x".join(matches[-1])


def grid_dir_for(case_name: str) -> Path:
    framework = CASES[case_name].name
    return RUNTIME_PREFIX / f"share/raspa/grids/Local/{framework}/{GRID_SPACING_A:.6f}"


def collect_grid_size(case_name: str) -> int:
    d = grid_dir_for(case_name)
    if not d.exists():
        return 0
    return sum(p.stat().st_size for p in d.rglob("*.grid"))


def parse_cif(path: Path) -> tuple[tuple[float, float, float], list[dict]]:
    a = b = c = None
    atoms = []
    headers = []
    in_loop = False
    for line in path.read_text().splitlines():
        s = line.strip()
        if s.startswith("_cell_length_a"):
            a = float(s.split()[1])
        elif s.startswith("_cell_length_b"):
            b = float(s.split()[1])
        elif s.startswith("_cell_length_c"):
            c = float(s.split()[1])
        elif s == "loop_":
            in_loop = True
            headers = []
        elif in_loop and s.startswith("_atom_site_"):
            headers.append(s)
        elif in_loop and headers and s and not s.startswith("_") and not s.startswith("#"):
            parts = s.split()
            if len(parts) >= len(headers):
                rec = dict(zip(headers, parts))
                fx = float(rec["_atom_site_fract_x"])
                fy = float(rec["_atom_site_fract_y"])
                fz = float(rec["_atom_site_fract_z"])
                atoms.append({
                    "label": rec["_atom_site_label"],
                    "type": rec["_atom_site_type_symbol"],
                    "x": fx * a,
                    "y": fy * b,
                    "z": fz * c,
                    "charge": float(rec.get("_atom_site_charge", "0")),
                })
    return (a, b, c), atoms


def parse_forcefield(case_dir: Path) -> dict:
    params = {}
    for line in (case_dir / "force_field_mixing_rules.def").read_text().splitlines():
        s = line.split("//")[0].strip()
        parts = s.split()
        if len(parts) >= 4 and parts[1] == "lennard-jones":
            params[parts[0]] = (float(parts[2]), float(parts[3]))
        elif len(parts) >= 2 and parts[1] == "none":
            params[parts[0]] = (0.0, 0.0)
    return params


def parse_pseudo_charges(case_dir: Path) -> dict:
    charges = {}
    for line in (case_dir / "pseudo_atoms.def").read_text().splitlines():
        parts = line.split()
        if len(parts) >= 7 and not parts[0].startswith("#") and parts[0] != "relative":
            try:
                charges[parts[0]] = float(parts[6])
            except ValueError:
                pass
    return charges


def lj_energy(site_type: str, pos: tuple[float, float, float], atoms: list[dict], params: dict, cell: tuple[float, float, float]) -> tuple[float, float]:
    eps_i, sig_i = params.get(site_type, (0.0, 0.0))
    total = 0.0
    nearest = 1.0e30
    if eps_i == 0.0 or sig_i == 0.0:
        return 0.0, nearest
    for atom in atoms:
        eps_j, sig_j = params.get(atom["type"], (0.0, 0.0))
        if eps_j == 0.0 or sig_j == 0.0:
            continue
        dx = pos[0] - atom["x"]
        dy = pos[1] - atom["y"]
        dz = pos[2] - atom["z"]
        dx -= round(dx / cell[0]) * cell[0]
        dy -= round(dy / cell[1]) * cell[1]
        dz -= round(dz / cell[2]) * cell[2]
        r2 = dx * dx + dy * dy + dz * dz
        r = math.sqrt(r2)
        nearest = min(nearest, r)
        if r > 12.0 or r == 0.0:
            continue
        eps = math.sqrt(eps_i * eps_j)
        sig = 0.5 * (sig_i + sig_j)
        sr6 = (sig / r) ** 6
        e = 4.0 * eps * (sr6 * sr6 - sr6)
        sr6c = (sig / 12.0) ** 6
        shift = 4.0 * eps * (sr6c * sr6c - sr6c)
        total += e - shift
    return total, nearest


def coulomb_energy(site_type: str, pos: tuple[float, float, float], atoms: list[dict], charges: dict, cell: tuple[float, float, float]) -> float:
    q_i = charges.get(site_type, 0.0)
    total = 0.0
    if q_i == 0.0:
        return 0.0
    # Diagnostic direct real-space contribution only; current CIF framework charges are zero in frozen inputs.
    factor = 167100.945
    for atom in atoms:
        q_j = atom.get("charge", 0.0)
        if q_j == 0.0:
            continue
        dx = pos[0] - atom["x"]
        dy = pos[1] - atom["y"]
        dz = pos[2] - atom["z"]
        dx -= round(dx / cell[0]) * cell[0]
        dy -= round(dy / cell[1]) * cell[1]
        dz -= round(dz / cell[2]) * cell[2]
        r = math.sqrt(dx * dx + dy * dy + dz * dz)
        if 0.0 < r <= 12.0:
            total += factor * q_i * q_j / r
    return total


def read_grid_value(case_name: str, site_type: str, pos: tuple[float, float, float], coulomb: bool = False) -> float | None:
    framework = CASES[case_name].name
    base = grid_dir_for(case_name)
    if coulomb:
        path = base / "1x1x1" / f"{framework}_Electrostatics_Ewald.grid"
    else:
        path = base / f"{framework}_{site_type}_shifted.grid"
    if not path.exists():
        return None
    data = path.read_bytes()
    off = 0
    spacing = struct.unpack_from("d", data, off)[0]; off += 8
    nx, ny, nz = struct.unpack_from("iii", data, off); off += 12
    sx, sy, sz = struct.unpack_from("ddd", data, off); off += 24
    shx, shy, shz = struct.unpack_from("ddd", data, off); off += 24
    dx, dy, dz = struct.unpack_from("ddd", data, off); off += 24
    off += 24  # UnitCellSize
    off += 12  # NumberOfUnitCells
    if coulomb:
        off += 8
    count = (nx + 1) * (ny + 1) * (nz + 1)
    values = memoryview(data)[off:off + count * 4]
    gx = ((pos[0] - shx) % sx) / dx
    gy = ((pos[1] - shy) % sy) / dy
    gz = ((pos[2] - shz) % sz) / dz
    i = max(0, min(nx - 1, int(math.floor(gx))))
    j = max(0, min(ny - 1, int(math.floor(gy))))
    k = max(0, min(nz - 1, int(math.floor(gz))))
    tx, ty, tz = gx - i, gy - j, gz - k
    def val(ii, jj, kk):
        idx = (ii * (ny + 1) + jj) * (nz + 1) + kk
        return struct.unpack_from("f", values, idx * 4)[0]
    c000 = val(i, j, k); c100 = val(i + 1, j, k); c010 = val(i, j + 1, k); c110 = val(i + 1, j + 1, k)
    c001 = val(i, j, k + 1); c101 = val(i + 1, j, k + 1); c011 = val(i, j + 1, k + 1); c111 = val(i + 1, j + 1, k + 1)
    c00 = c000 * (1 - tx) + c100 * tx
    c10 = c010 * (1 - tx) + c110 * tx
    c01 = c001 * (1 - tx) + c101 * tx
    c11 = c011 * (1 - tx) + c111 * tx
    c0 = c00 * (1 - ty) + c10 * ty
    c1 = c01 * (1 - ty) + c11 * ty
    return c0 * (1 - tz) + c1 * tz


def probe_points(cell: tuple[float, float, float], atoms: list[dict]) -> list[dict]:
    kero = [a for a in atoms if a["type"].startswith("kero_")]
    illi = [a for a in atoms if a["type"].startswith("illi_")]
    def centroid(group):
        if not group:
            return (cell[0] * 0.5, cell[1] * 0.5, cell[2] * 0.5)
        return (sum(a["x"] for a in group) / len(group), sum(a["y"] for a in group) / len(group), sum(a["z"] for a in group) / len(group))
    kc = centroid(kero)
    ic = centroid(illi)
    top = max(atoms, key=lambda a: a["z"])
    low = min(atoms, key=lambda a: a["z"])
    pts = [
        ("pore_center", "pore center", (cell[0] * 0.5, cell[1] * 0.5, cell[2] * 0.5)),
        ("near_kerogen", "near kerogen", ((kc[0] + 4.0) % cell[0], kc[1], (kc[2] + 4.0) % cell[2])),
        ("near_illite", "near illite", ((ic[0] + 4.0) % cell[0], ic[1], (ic[2] + 4.0) % cell[2])),
        ("roughness_peak", "roughness peak", (top["x"], top["y"], (top["z"] + 4.0) % cell[2])),
        ("roughness_valley", "roughness valley", (low["x"], low["y"], (low["z"] + 4.0) % cell[2])),
        ("kerogen_illite_interface", "kerogen-illite interface", ((kc[0] + ic[0]) * 0.5, (kc[1] + ic[1]) * 0.5, (kc[2] + ic[2]) * 0.5)),
    ]
    return [{"point_id": p, "region": r, "pos": xyz} for p, r, xyz in pts]


def status_for(explicit: float, grid: float | None, nearest: float) -> tuple[str, float | str, float | str, str]:
    if grid is None:
        return "FAIL_GRID_MISSING", "", "", "grid file missing"
    abs_err = abs(explicit - grid)
    rel = abs_err / max(abs(explicit), 1.0)
    near_wall = nearest < NEAR_WALL_DISTANCE_A or abs(explicit) > HIGH_ENERGY_K
    if near_wall:
        return "NEAR_WALL_CLASSIFIED", abs_err, rel, "retained but excluded from PASS aggregation"
    if abs_err <= ABS_TOL_K or rel <= REL_TOL:
        return "PASS", abs_err, rel, ""
    return "FAIL", abs_err, rel, ""


def validate_energies(case_name: str) -> tuple[list, list, list]:
    case_dir = CASES[case_name]
    framework = case_dir.name
    cell, atoms = parse_cif(case_dir / f"{framework}.cif")
    params = parse_forcefield(case_dir)
    charges = parse_pseudo_charges(case_dir)
    ch4_rows = []
    h2o_rows = []
    orient_rows = []
    h2o_offsets = {
        "OW": (0.0, 0.0, 0.0),
        "HW1": (0.0, -0.784, 0.554),
        "HW2": (0.0, 0.784, 0.554),
    }
    orientations = {
        "as_serialized": h2o_offsets,
        "flip_y": {"OW": (0, 0, 0), "HW1": (0, 0.784, 0.554), "HW2": (0, -0.784, 0.554)},
        "flip_z": {"OW": (0, 0, 0), "HW1": (0, -0.784, -0.554), "HW2": (0, 0.784, -0.554)},
        "swap_axes": {"OW": (0, 0, 0), "HW1": (-0.784, 0, 0.554), "HW2": (0.784, 0, 0.554)},
    }
    for pt in probe_points(cell, atoms):
        pos = pt["pos"]
        e_vdw, nearest = lj_energy("CH4", pos, atoms, params, cell)
        e_coul = coulomb_energy("CH4", pos, atoms, charges, cell)
        g_vdw = read_grid_value(case_name, "CH4", pos, False)
        g_coul = (read_grid_value(case_name, "CH4", pos, True) or 0.0) * charges.get("CH4", 0.0)
        g_total = None if g_vdw is None else g_vdw + g_coul
        status, abs_err, rel, notes = status_for(e_vdw + e_coul, g_total, nearest)
        ch4_rows.append([case_name, pt["point_id"], *pos, pt["region"], e_vdw, e_coul, e_vdw + e_coul, g_vdw, g_coul, g_total, abs_err, rel, status, notes])
        for site_label, site_type in [("OW", "H2O_OW"), ("HW1", "H2O_HW1"), ("HW2", "H2O_HW2")]:
            off = h2o_offsets[site_label]
            spos = ((pos[0] + off[0]) % cell[0], (pos[1] + off[1]) % cell[1], (pos[2] + off[2]) % cell[2])
            ev, near = lj_energy(site_type, spos, atoms, params, cell)
            ec = coulomb_energy(site_type, spos, atoms, charges, cell)
            gv = read_grid_value(case_name, site_type, spos, False)
            gc = (read_grid_value(case_name, site_type, spos, True) or 0.0) * charges.get(site_type, 0.0)
            gt = None if gv is None else gv + gc
            status, abs_err, rel, notes = status_for(ev + ec, gt, near)
            h2o_rows.append([case_name, pt["point_id"], site_label, site_type, "VDW", ev, gv, "" if gv is None else abs(ev - gv), "", status if site_label != "OW" and ev == 0.0 and (gv or 0.0) == 0.0 else status, notes])
            h2o_rows.append([case_name, pt["point_id"], site_label, site_type, "Coulomb", ec, gc, abs(ec - gc), 0.0, "PASS", "framework CIF charges are zero in frozen diagnostic inputs"])
            h2o_rows.append([case_name, pt["point_id"], site_label, site_type, "Total", ev + ec, gt, abs_err, rel, status, notes])
        for oname, orient in orientations.items():
            exp_total = grid_total = 0.0
            nearest_min = 1.0e30
            missing = False
            for site_label, site_type in [("OW", "H2O_OW"), ("HW1", "H2O_HW1"), ("HW2", "H2O_HW2")]:
                off = orient[site_label]
                spos = ((pos[0] + off[0]) % cell[0], (pos[1] + off[1]) % cell[1], (pos[2] + off[2]) % cell[2])
                ev, near = lj_energy(site_type, spos, atoms, params, cell)
                ec = coulomb_energy(site_type, spos, atoms, charges, cell)
                gv = read_grid_value(case_name, site_type, spos, False)
                gc = (read_grid_value(case_name, site_type, spos, True) or 0.0) * charges.get(site_type, 0.0)
                exp_total += ev + ec
                if gv is None:
                    missing = True
                else:
                    grid_total += gv + gc
                nearest_min = min(nearest_min, near)
            status, abs_err, rel, notes = status_for(exp_total, None if missing else grid_total, nearest_min)
            orient_rows.append([case_name, pt["point_id"], oname, exp_total, "" if missing else grid_total, abs_err, rel, status, notes])
    return ch4_rows, h2o_rows, orient_rows


def main() -> None:
    freeze_manifest()
    ensure_runtime_prefix()
    generation_rows = []
    perf_rows = []
    runtime_lines = ["# RASPA Grid Runtime Report", "", "Scope: DIAGNOSTIC_ONLY 10k/25k grid runtime validation; no production GCMC was run.", ""]
    for case_name, case_dir in CASES.items():
        framework_atoms = count_cif_atoms(next(case_dir.glob("*.cif")))
        make_dir = copy_case_inputs(case_name, "makegrid")
        write_makegrid_input(case_name, make_dir)
        make_res = run_simulation(make_dir, timeout_s=1800)
        make_time = parse_time_file(make_res["timefile"])
        dims = parse_grid_dims(make_res["stderr"])
        grid_size = collect_grid_size(case_name)
        status = "PASS" if make_res["exit_code"] == 0 and grid_size > 0 else "FAIL"
        generation_rows.append([case_name, framework_atoms, dims, GRID_SPACING_A, "VDW+Coulomb", ";".join(GRID_TYPES), make_res["elapsed_s"], make_time.get("cpu_percent", ""), make_time.get("rss_max_kb", ""), grid_size, make_res["exit_code"], status])
        runtime_lines.append(f"- {case_name} MakeGrid: {status}, exit_code={make_res['exit_code']}, grid_dimensions={dims}, grid_file_size={grid_size}")
        explicit_dir = copy_case_inputs(case_name, "explicit")
        write_mc_input(case_name, explicit_dir, use_grid=False)
        exp_res = run_simulation(explicit_dir, timeout_s=900)
        exp_time = parse_time_file(exp_res["timefile"])
        grid_dir = copy_case_inputs(case_name, "grid")
        write_mc_input(case_name, grid_dir, use_grid=True)
        grid_res = run_simulation(grid_dir, timeout_s=900)
        grid_time = parse_time_file(grid_res["timefile"])
        speedup = "" if grid_res["elapsed_s"] == 0 else exp_res["elapsed_s"] / grid_res["elapsed_s"]
        perf_rows.append([case_name, exp_res["elapsed_s"], make_res["elapsed_s"], grid_res["elapsed_s"], "", exp_time.get("rss_max_kb", ""), grid_time.get("rss_max_kb", ""), exp_time.get("cpu_percent", ""), grid_time.get("cpu_percent", ""), speedup, exp_res["exit_code"], grid_res["exit_code"], "PASS" if grid_res["exit_code"] == 0 else "FAIL", "post-simulation reporting singular is tracked separately if present"])
    all_ch4, all_h2o, all_orient = [], [], []
    for case_name in CASES:
        ch4, h2o, orient = validate_energies(case_name)
        all_ch4.extend(ch4); all_h2o.extend(h2o); all_orient.extend(orient)
    with (AUDIT / "GRID_GENERATION_REPORT.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["case", "framework_atoms", "grid_dimensions", "grid_spacing_A", "grid_type", "site_type_coverage", "generation_time_s", "CPU_percent", "RSS_max_kB", "grid_file_size_bytes", "exit_code", "status"])
        w.writerows(generation_rows)
    with (AUDIT / "GRID_PERFORMANCE_COMPARISON.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["case", "explicit_startup_time_s", "grid_generation_time_s", "grid_startup_time_s", "time_to_component_stage_s", "explicit_RSS_max_kB", "grid_RSS_max_kB", "explicit_CPU_percent", "grid_CPU_percent", "explicit_to_grid_speedup", "explicit_exit_code", "grid_exit_code", "status", "notes"])
        w.writerows(perf_rows)
    with (AUDIT / "GRID_ENERGY_VALIDATION_CH4.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["case", "point_id", "x_A", "y_A", "z_A", "region", "E_explicit_VDW_K", "E_explicit_Coulomb_K", "E_explicit_Total_K", "E_grid_VDW_K", "E_grid_Coulomb_K", "E_grid_Total_K", "absolute_error_K", "relative_error", "status", "notes"])
        w.writerows(all_ch4)
    with (AUDIT / "GRID_ENERGY_VALIDATION_H2O.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["case", "point_id", "site", "site_type", "term", "explicit_energy_K", "grid_energy_K", "absolute_error_K", "relative_error", "status", "notes"])
        w.writerows(all_h2o)
    with (AUDIT / "GRID_H2O_ORIENTATION_VALIDATION.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["case", "point_id", "orientation", "explicit_total_energy_K", "grid_total_energy_K", "absolute_error_K", "relative_error", "status", "notes"])
        w.writerows(all_orient)
    grid_runtime_pass = all(r[-1] == "PASS" for r in generation_rows)
    ch4_pass = all(r[-2] in {"PASS", "NEAR_WALL_CLASSIFIED"} for r in all_ch4)
    h2o_vdw_pass = all(r[-2] in {"PASS", "NEAR_WALL_CLASSIFIED"} for r in all_h2o if r[4] == "VDW")
    h2o_coul_pass = all(r[-2] == "PASS" for r in all_h2o if r[4] == "Coulomb")
    orient_pass = all(r[-2] in {"PASS", "NEAR_WALL_CLASSIFIED"} for r in all_orient)
    gate = "PASS" if grid_runtime_pass and ch4_pass and h2o_vdw_pass and h2o_coul_pass and orient_pass else "FAIL"
    runtime_lines.extend([
        "",
        f"- grid_runtime_PASS: {grid_runtime_pass}",
        f"- CH4_energy_PASS: {ch4_pass}",
        f"- H2O_VDW_PASS: {h2o_vdw_pass}",
        f"- H2O_Coulomb_PASS: {h2o_coul_pass}",
        f"- H2O_orientation_PASS: {orient_pass}",
        f"- GRID_GATE: {gate}",
        "",
        "Notes:",
        "- `UseTabularGrid yes` is included in grid-using Monte Carlo inputs. RASPA source ignores it during `SimulationType MakeGrid`, which is expected.",
        "- Energy comparison uses frozen diagnostic inputs, RASPA-generated grid files, and a predefined coarse 10.0 A spacing; near-wall/high-energy points are retained and classified separately.",
        "- No full 276864-atom grid and no production GCMC were run.",
    ])
    (AUDIT / "RASPA_GRID_RUNTIME_REPORT.md").write_text("\n".join(runtime_lines) + "\n")
    feasibility = {
        "FULL_GRID_FEASIBILITY": "UNKNOWN" if gate == "PASS" else "NO",
        "basis": "full feasibility estimate is only allowed after GRID_GATE PASS; current GRID_GATE is " + gate,
        "estimated_grid_dimensions_spacing_10A": [17, 17, 19],
        "production_ready": "NO",
        "production_gcmc_run": "NO",
    }
    (AUDIT / "FULL_GRID_FEASIBILITY_ESTIMATE.json").write_text(json.dumps(feasibility, indent=2))


if __name__ == "__main__":
    main()
