#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V33 - Build an 8 nm mirrored slit pore from the exact kerogen+illite composite wall.

Default source wall:
  ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/
  {case}_EXACT_kerogen_plus_illite.gro

Exact kerogen source used only to identify the kerogen atom block and surface:
  KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro

Geometry rule:
  * lower wall internal geometry is unchanged;
  * upper wall is an exact z-mirror of the whole lower composite wall;
  * lower inner surface is kerogen rough face;
  * upper inner surface is the mirrored kerogen rough face;
  * default nominal pore width is 8.0 nm between mean rough-surface planes.

The script writes a GRO pore model, component mapping CSV, report JSON/CSV,
and a geometry-only CIF. The CIF is NOT yet force-field-ready; the RASPA
preparation script later writes a typed/charged CIF after topology mapping.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass, replace
from pathlib import Path
from typing import List, Sequence, Tuple

import numpy as np


@dataclass
class Atom:
    resid: int
    resname: str
    atomname: str
    atomnr: int
    x: float
    y: float
    z: float


def fail(msg: str) -> None:
    raise RuntimeError(msg)


def read_gro(path: Path) -> Tuple[str, List[Atom], np.ndarray]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(lines) < 3:
        fail(f"Invalid GRO: {path}")
    n = int(lines[1].strip())
    if len(lines) < n + 3:
        fail(f"Truncated GRO: {path}")
    atoms: List[Atom] = []
    for i, line in enumerate(lines[2:2+n], 1):
        try:
            atoms.append(Atom(
                int(line[0:5]),
                line[5:10].strip() or "MOL",
                line[10:15].strip() or "X",
                int(line[15:20]),
                float(line[20:28]),
                float(line[28:36]),
                float(line[36:44]),
            ))
        except Exception as e:
            fail(f"Cannot parse {path} atom line {i}: {e}\n{line}")
    vals = [float(v) for v in lines[2+n].split()]
    if len(vals) < 3:
        fail(f"Invalid box line in {path}")
    return lines[0].strip(), atoms, np.array(vals[:3], dtype=float)


def write_gro(path: Path, title: str, atoms: List[Atom], box: Sequence[float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(title[:200] + "\n")
        f.write(f"{len(atoms):5d}\n")
        for i, a in enumerate(atoms, 1):
            resid = int(a.resid) % 100000
            atomnr = i % 100000 or 99999
            f.write(
                f"{resid:5d}{a.resname[:5]:<5}{a.atomname[:5]:>5}{atomnr:5d}"
                f"{a.x:8.3f}{a.y:8.3f}{a.z:8.3f}\n"
            )
        f.write(f"{float(box[0]):10.5f}{float(box[1]):10.5f}{float(box[2]):10.5f}\n")


def xyz(atoms: List[Atom]) -> np.ndarray:
    return np.array([[a.x, a.y, a.z] for a in atoms], dtype=float)


def shift_atoms(atoms: List[Atom], s: Sequence[float]) -> List[Atom]:
    sx, sy, sz = map(float, s)
    return [replace(a, x=a.x+sx, y=a.y+sy, z=a.z+sz) for a in atoms]


def mirror_atoms_z(atoms: List[Atom], plane_z: float, resid_offset: int) -> List[Atom]:
    out: List[Atom] = []
    for a in atoms:
        out.append(replace(a, resid=a.resid + resid_offset, z=2.0*plane_z - a.z))
    return out


def max_abs_coord_diff(a: List[Atom], b: List[Atom]) -> float:
    if len(a) != len(b):
        return float("inf")
    return float(np.max(np.abs(xyz(a) - xyz(b)))) if a else 0.0


def surface_grid_top(atoms: List[Atom], spacing: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    p = xyz(atoms)
    xmin, ymin = p[:,0].min(), p[:,1].min()
    xmax, ymax = p[:,0].max(), p[:,1].max()
    nx = max(1, int(math.ceil((xmax-xmin)/spacing)))
    ny = max(1, int(math.ceil((ymax-ymin)/spacing)))
    grid = np.full((nx, ny), np.nan)
    ix = np.minimum(((p[:,0]-xmin)/spacing).astype(int), nx-1)
    iy = np.minimum(((p[:,1]-ymin)/spacing).astype(int), ny-1)
    for k in range(len(p)):
        i, j = int(ix[k]), int(iy[k])
        z = p[k,2]
        if np.isnan(grid[i,j]) or z > grid[i,j]:
            grid[i,j] = z
    vals = grid[np.isfinite(grid)]
    if vals.size == 0:
        fail("Could not extract kerogen top surface grid")
    return grid, vals, np.array([xmin, xmax, ymin, ymax], dtype=float)


def paired_gap_stats(lower_surface_grid: np.ndarray, mirror_plane: float) -> dict:
    vals = lower_surface_grid[np.isfinite(lower_surface_grid)]
    # Mirrored upper surface at same x/y: z_upper = 2*plane - z_lower
    gaps = 2.0*mirror_plane - 2.0*vals
    return {
        "grid_gap_min_nm": float(np.min(gaps)),
        "grid_gap_p05_nm": float(np.percentile(gaps, 5)),
        "grid_gap_mean_nm": float(np.mean(gaps)),
        "grid_gap_p95_nm": float(np.percentile(gaps, 95)),
        "grid_gap_max_nm": float(np.max(gaps)),
    }


def write_geometry_cif(path: Path, name: str, atoms: List[Atom], box_nm: Sequence[float]) -> None:
    # Geometry-only CIF: type labels are resname+atomname and charges are zero.
    # prepare_raspa2_gcmc.py later writes a force-field-ready typed/charged CIF.
    L = np.array(box_nm, dtype=float) * 10.0
    p = xyz(atoms) * 10.0
    frac = p / L.reshape(1,3)
    with path.open("w", encoding="utf-8") as f:
        f.write(f"data_{name}\n")
        f.write(f"_cell_length_a {L[0]:.8f}\n_cell_length_b {L[1]:.8f}\n_cell_length_c {L[2]:.8f}\n")
        f.write("_cell_angle_alpha 90\n_cell_angle_beta 90\n_cell_angle_gamma 90\n")
        f.write("_symmetry_space_group_name_H-M 'P 1'\n_symmetry_Int_Tables_number 1\n")
        f.write("loop_\n")
        f.write("_atom_site_label\n_atom_site_type_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_charge\n")
        for i, (a, q) in enumerate(zip(atoms, frac), 1):
            typ = ''.join(ch for ch in (a.resname + '_' + a.atomname) if ch.isalnum() or ch == '_')[:28] or 'X'
            f.write(f"{typ}{i} {typ} {q[0]:.10f} {q[1]:.10f} {q[2]:.10f} 0.0\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="8nm_pore_raspa2_config.json")
    ap.add_argument("--case", action="append", dest="cases")
    args = ap.parse_args()

    root = Path.cwd()
    cfg = json.loads((root / args.config).read_text(encoding="utf-8"))
    cases = args.cases or cfg["cases"]
    out_root = root / cfg["pore_output_dir"]
    out_root.mkdir(parents=True, exist_ok=True)

    all_reports = []
    for case in cases:
        wall_path = root / cfg["source_wall_pattern"].format(case=case)
        kero_path = root / cfg["exact_kerogen_pattern"].format(case=case)
        if not wall_path.exists() or not kero_path.exists():
            msg = f"{case}: missing wall or kerogen input: {wall_path} / {kero_path}"
            if cfg.get("skip_missing_cases", True):
                print("WARNING:", msg)
                continue
            fail(msg)

        _, lower_original, source_box = read_gro(wall_path)
        _, exact_kero, _ = read_gro(kero_path)
        nk = len(exact_kero)
        if len(lower_original) < nk:
            fail(f"{case}: composite wall has fewer atoms than exact kerogen")
        diff = max_abs_coord_diff(lower_original[:nk], exact_kero)
        tol = float(cfg.get("exact_kerogen_verify_tolerance_nm", 0.0011))
        if diff > tol:
            fail(f"{case}: first {nk} composite atoms do not match RAW exact kerogen; max diff={diff:.6g} nm")

        # Optional rigid translation of the WHOLE lower wall. Internal geometry remains exact.
        lower = lower_original
        rigid_shift = np.zeros(3)
        if cfg.get("tight_xy_box", True):
            p0 = xyz(lower)
            margin = float(cfg.get("xy_edge_margin_nm", 0.05))
            rigid_shift[0] = margin - float(p0[:,0].min())
            rigid_shift[1] = margin - float(p0[:,1].min())
            # Keep z absolute unless a negative coordinate exists.
            minz = float(p0[:,2].min())
            if minz < float(cfg.get("bottom_margin_nm", 0.02)):
                rigid_shift[2] = float(cfg.get("bottom_margin_nm", 0.02)) - minz
            lower = shift_atoms(lower, rigid_shift)
        lower_kero = lower[:nk]

        spacing = float(cfg.get("surface_grid_spacing_nm", 0.30))
        surf_grid, surf_vals, _ = surface_grid_top(lower_kero, spacing)
        surface_mean = float(np.mean(surf_vals))
        surface_max = float(np.max(surf_vals))
        pore_nm = float(cfg.get("pore_width_nm", 8.0))
        definition = cfg.get("pore_width_definition", "mean_surface_plane")
        if definition == "mean_surface_plane":
            mirror_plane = surface_mean + pore_nm/2.0
        elif definition == "peak_to_peak":
            mirror_plane = surface_max + pore_nm/2.0
        else:
            fail(f"Unknown pore_width_definition: {definition}")

        upper = mirror_atoms_z(lower, mirror_plane, int(cfg.get("upper_resid_offset", 50000)))
        combined = lower + upper

        p = xyz(combined)
        xy_margin = float(cfg.get("xy_edge_margin_nm", 0.05))
        top_margin = float(cfg.get("top_margin_nm", 0.20))
        if cfg.get("tight_xy_box", True):
            Lx = float(p[:,0].max() + xy_margin)
            Ly = float(p[:,1].max() + xy_margin)
        else:
            Lx, Ly = float(source_box[0]), float(source_box[1])
        Lz = float(p[:,2].max() + top_margin)
        box = np.array([Lx, Ly, Lz], dtype=float)

        # Verify lower wall internal geometry after optional rigid translation.
        delta_lower_internal = xyz(lower) - xyz(lower_original)
        # all atoms should share same rigid shift vector
        nonrigid = float(np.max(np.abs(delta_lower_internal - rigid_shift.reshape(1,3)))) if lower else 0.0
        if nonrigid > 1e-9:
            fail(f"{case}: lower wall was deformed unexpectedly")

        gap = paired_gap_stats(surf_grid, mirror_plane)
        report = {
            "case": case,
            "source_wall": str(wall_path),
            "exact_kerogen": str(kero_path),
            "source_wall_atoms": len(lower_original),
            "exact_kerogen_atoms": nk,
            "lower_exact_kerogen_max_diff_before_rigid_shift_nm": diff,
            "lower_wall_rigid_shift_nm": rigid_shift.tolist(),
            "lower_wall_nonrigid_change_nm": nonrigid,
            "pore_width_target_nm": pore_nm,
            "pore_width_definition": definition,
            "lower_rough_surface_mean_z_nm": surface_mean,
            "lower_rough_surface_min_z_nm": float(np.min(surf_vals)),
            "lower_rough_surface_max_z_nm": surface_max,
            "mirror_plane_z_nm": mirror_plane,
            "box_nm": box.tolist(),
            **gap,
        }
        all_reports.append(report)

        od = out_root / case
        od.mkdir(parents=True, exist_ok=True)
        write_gro(od / f"{case}_LOWER_WALL.gro", f"{case} exact lower composite wall", lower, box)
        write_gro(od / f"{case}_UPPER_WALL_MIRRORED.gro", f"{case} mirrored upper composite wall", upper, box)
        pore_gro = od / f"{case}_COMPOSITE_PORE_8nm.gro"
        write_gro(pore_gro, f"{case} mirrored composite slit pore nominal {pore_nm:.3f} nm", combined, box)
        write_geometry_cif(od / f"{case}_COMPOSITE_PORE_8nm_GEOMETRY_ONLY.cif", f"{case}_COMPOSITE_PORE_8nm", combined, box)

        with (od / f"{case}_wall_atom_mapping.csv").open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow(["output_atom_index", "wall", "source_lower_atom_index", "component", "resname", "atomname"])
            for i, a in enumerate(combined, 1):
                src = (i-1) % len(lower) + 1
                wall = "LOWER" if i <= len(lower) else "UPPER_MIRRORED"
                component = "KEROGEN" if src <= nk else "ILLITE"
                w.writerow([i, wall, src, component, a.resname, a.atomname])

        (od / f"{case}_pore_build_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        with (od / f"{case}_pore_build_report.csv").open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f); w.writerow(["metric", "value"])
            for k, v in report.items():
                w.writerow([k, json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v])
        print(f"DONE {case}: {pore_gro} | mean grid gap={gap['grid_gap_mean_nm']:.4f} nm")

    if all_reports:
        keys = sorted({k for r in all_reports for k in r.keys()})
        with (out_root / "PORE_8NM_BUILD_REPORT_ALL.csv").open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(all_reports)


if __name__ == "__main__":
    main()
