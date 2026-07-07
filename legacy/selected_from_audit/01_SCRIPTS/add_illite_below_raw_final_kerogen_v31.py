#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V31 - Add illite below the EXACT RAW final kerogen plate without changing kerogen.

Hard guarantees:
  * Kerogen input is read from an explicitly selected final KERO-only GRO.
  * No flip, no centering, no wrapping, no standardization, no rotation.
  * No kerogen atom is deleted or reordered.
  * No kerogen coordinate is changed.
  * Illite alone is replicated/rotated/translated and placed below kerogen.
  * The first N atoms in the combined GRO are the original kerogen atoms.
  * A post-write verification aborts if any kerogen coordinate changed.

Required input source:
  KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/
    RMS_xxx_kerogen_only_raw_from_final.gro

Illite structure and force-field files are discovered from 00_INPUT.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import shutil
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

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
    element: str = ""


def fail(msg: str) -> None:
    raise RuntimeError(msg)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def dump_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def guess_element(name: str) -> str:
    s = re.sub(r"[^A-Za-z]", "", name or "")
    if not s:
        return "X"
    two = s[:2].capitalize()
    if two in {"Si", "Al", "Mg", "Fe", "Ca", "Na", "Cl", "Li", "Ti", "Mn", "Zn", "Cu", "Ni", "Co", "Cr"}:
        return two
    return s[0].upper()


def gro_box_to_matrix(vals: Sequence[float]) -> np.ndarray:
    if len(vals) >= 9:
        return np.array([
            [vals[0], vals[3], vals[4]],
            [vals[5], vals[1], vals[6]],
            [vals[7], vals[8], vals[2]],
        ], dtype=float)
    if len(vals) >= 3:
        return np.diag([vals[0], vals[1], vals[2]]).astype(float)
    fail("GRO box line has fewer than 3 values")


def read_gro(path: Path) -> Tuple[str, List[Atom], np.ndarray]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(lines) < 3:
        fail(f"Invalid GRO file: {path}")
    title = lines[0].strip()
    try:
        n = int(lines[1].strip())
    except Exception as e:
        fail(f"Cannot read atom count from {path}: {e}")
    if len(lines) < n + 3:
        fail(f"Truncated GRO file: {path}")
    atoms: List[Atom] = []
    for idx, line in enumerate(lines[2:2+n], 1):
        try:
            resid = int(line[0:5])
            resname = line[5:10].strip() or "MOL"
            atomname = line[10:15].strip() or "X"
            atomnr = int(line[15:20])
            x = float(line[20:28]); y = float(line[28:36]); z = float(line[36:44])
        except Exception as e:
            fail(f"Cannot parse GRO atom line {idx} in {path}: {e}\n{line}")
        atoms.append(Atom(resid, resname, atomname, atomnr, x, y, z, guess_element(atomname)))
    vals = [float(v) for v in lines[2+n].split()]
    return title, atoms, gro_box_to_matrix(vals)


def crystallographic_vectors(a: float, b: float, c: float, alpha_deg: float, beta_deg: float, gamma_deg: float) -> np.ndarray:
    alpha = math.radians(alpha_deg); beta = math.radians(beta_deg); gamma = math.radians(gamma_deg)
    va = np.array([a, 0.0, 0.0])
    vb = np.array([b * math.cos(gamma), b * math.sin(gamma), 0.0])
    cx = c * math.cos(beta)
    sy = max(math.sin(gamma), 1e-12)
    cy = c * (math.cos(alpha) - math.cos(beta) * math.cos(gamma)) / sy
    cz2 = max(c*c - cx*cx - cy*cy, 0.0)
    vc = np.array([cx, cy, math.sqrt(cz2)])
    return np.vstack([va, vb, vc])


def read_pdb(path: Path) -> Tuple[str, List[Atom], np.ndarray]:
    atoms: List[Atom] = []
    box: Optional[np.ndarray] = None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        rec = line[:6].strip().upper()
        if rec == "CRYST1":
            try:
                a = float(line[6:15]) / 10.0; b = float(line[15:24]) / 10.0; c = float(line[24:33]) / 10.0
                alpha = float(line[33:40]); beta = float(line[40:47]); gamma = float(line[47:54])
                box = crystallographic_vectors(a, b, c, alpha, beta, gamma)
            except Exception:
                pass
        elif rec in {"ATOM", "HETATM"}:
            atomnr = int(line[6:11]) if line[6:11].strip() else len(atoms) + 1
            atomname = line[12:16].strip() or "X"
            resname = line[17:20].strip() or "MOL"
            resid = int(line[22:26]) if line[22:26].strip() else 1
            x = float(line[30:38]) / 10.0; y = float(line[38:46]) / 10.0; z = float(line[46:54]) / 10.0
            atoms.append(Atom(resid, resname[:5], atomname, atomnr, x, y, z, guess_element(atomname)))
    if not atoms:
        fail(f"No atoms in PDB: {path}")
    if box is None:
        xyz = xyz_of(atoms)
        span = xyz.max(axis=0) - xyz.min(axis=0)
        box = np.diag(np.maximum(span + 0.2, 0.2))
    return path.stem, atoms, box


def load_structure(path: Path) -> Tuple[str, List[Atom], np.ndarray]:
    if path.suffix.lower() == ".gro":
        return read_gro(path)
    if path.suffix.lower() == ".pdb":
        return read_pdb(path)
    fail(f"Unsupported structure: {path}")


def write_gro(path: Path, title: str, atoms: List[Atom], box_xyz: Sequence[float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    bx, by, bz = [float(v) for v in box_xyz[:3]]
    with path.open("w", encoding="utf-8") as f:
        f.write(title[:200] + "\n")
        f.write(f"{len(atoms):5d}\n")
        for i, a in enumerate(atoms, 1):
            resid = int(a.resid) % 100000
            atomnr = i % 100000 or 99999
            f.write(f"{resid:5d}{(a.resname or 'MOL')[:5]:<5}{(a.atomname or 'X')[:5]:>5}{atomnr:5d}{a.x:8.3f}{a.y:8.3f}{a.z:8.3f}\n")
        f.write(f"{bx:10.5f}{by:10.5f}{bz:10.5f}\n")


def xyz_of(atoms: List[Atom]) -> np.ndarray:
    return np.array([[a.x, a.y, a.z] for a in atoms], dtype=float)


def shift_atoms(atoms: List[Atom], shift: Sequence[float]) -> List[Atom]:
    sx, sy, sz = map(float, shift)
    return [replace(a, x=a.x+sx, y=a.y+sy, z=a.z+sz) for a in atoms]


def rotate_xy_90(atoms: List[Atom], lattice: np.ndarray) -> Tuple[List[Atom], np.ndarray]:
    out = [replace(a, x=-a.y, y=a.x) for a in atoms]
    R = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    return out, lattice @ R.T


def discover_illite(input_dir: Path, explicit: str) -> Path:
    if explicit and explicit.lower() != "auto":
        p = Path(explicit)
        p = p if p.is_absolute() else input_dir / p
        if not p.exists():
            fail(f"Configured illite structure not found: {p}")
        return p
    for pat in ["*illite*.gro", "*Illite*.gro", "*ILLITE*.gro", "*illite*.pdb", "*Illite*.pdb", "*ILLITE*.pdb"]:
        hits = sorted(input_dir.glob(pat))
        if hits:
            return hits[0]
    fail(f"No *Illite*.gro/.pdb found in {input_dir}")


def discover_itp(input_dir: Path, explicit: str) -> Optional[Path]:
    if explicit and explicit.lower() != "auto":
        p = Path(explicit)
        p = p if p.is_absolute() else input_dir / p
        return p if p.exists() else None
    for pat in ["*illite*.itp", "*Illite*.itp", "*ILLITE*.itp"]:
        hits = [p for p in sorted(input_dir.glob(pat)) if not p.name.lower().startswith("posre")]
        if hits:
            return hits[0]
    return None


def resolve_exact_kerogen(root: Path, case: str, cfg: dict) -> Path:
    mode = str(cfg.get("kerogen_source_mode", "raw_exact")).lower()
    if mode == "standard_exact":
        pat = str(cfg.get("standard_exact_pattern", "KEROGEN_ONLY_FINALS/STANDARD_PLATES/{case}_kerogen_only_standard_plate.gro"))
    elif mode == "raw_exact":
        pat = str(cfg.get("raw_exact_pattern", "KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro"))
    else:
        fail("kerogen_source_mode must be raw_exact or standard_exact")
    p = root / pat.format(case=case)
    if not p.exists():
        fail(
            f"Exact kerogen input missing for {case}: {p}\n"
            "V31 deliberately does NOT fall back to any other kerogen file. "
            "This prevents silently using the wrong plate."
        )
    return p


def lattice_span(base_span: np.ndarray, lattice: np.ndarray, nx: int, ny: int, nz: int) -> np.ndarray:
    trans = []
    for ix in (0, nx-1):
        for iy in (0, ny-1):
            for iz in (0, nz-1):
                trans.append(ix*lattice[0] + iy*lattice[1] + iz*lattice[2])
    t = np.array(trans)
    return base_span + (t.max(axis=0) - t.min(axis=0))


def choose_xy_repeats(
    atoms: List[Atom], lattice: np.ndarray, target_x: float, target_y: float,
    max_n: int, fit_mode: str, overshoot_tol: float
) -> Tuple[int, int, np.ndarray, dict]:
    base_span = xyz_of(atoms).max(axis=0) - xyz_of(atoms).min(axis=0)
    candidates = []
    for nx in range(1, max_n+1):
        for ny in range(1, max_n+1):
            span = lattice_span(base_span, lattice, nx, ny, 1)
            sx, sy = float(span[0]), float(span[1])
            dx, dy = sx-target_x, sy-target_y
            if fit_mode == "inside":
                valid = sx <= target_x + overshoot_tol and sy <= target_y + overshoot_tol
                # maximize coverage first, then minimize absolute mismatch
                score = (0 if valid else 1, -(min(sx,target_x)*min(sy,target_y)), abs(dx)+abs(dy), nx*ny)
            elif fit_mode == "cover":
                valid = sx + 1e-9 >= target_x and sy + 1e-9 >= target_y
                score = (0 if valid else 1, max(dx,0)+max(dy,0), abs(dx)+abs(dy), nx*ny)
            else:  # nearest
                valid = True
                score = (abs(dx)+abs(dy), max(dx,0)+max(dy,0), nx*ny)
            candidates.append((score, nx, ny, span, valid))
    candidates.sort(key=lambda x: x[0])
    if not candidates:
        fail("No illite repeat candidates")
    _, nx, ny, span, valid = candidates[0]
    return nx, ny, span, {"fit_valid": bool(valid), "fit_mode": fit_mode}


def choose_compact_orientation(
    base_atoms: List[Atom], lattice: np.ndarray, target_x: float, target_y: float,
    max_n: int, fit_mode: str, overshoot_tol: float, allow_90: bool
):
    orientations = [(0, base_atoms, lattice)]
    if allow_90:
        a90, l90 = rotate_xy_90(base_atoms, lattice)
        orientations.append((90, a90, l90))
    best = None
    for angle, atoms, lat in orientations:
        nx, ny, span, meta = choose_xy_repeats(atoms, lat, target_x, target_y, max_n, fit_mode, overshoot_tol)
        sx, sy = float(span[0]), float(span[1])
        # prefer not wider than kerogen, then minimum mismatch
        over = max(0.0, sx-target_x) + max(0.0, sy-target_y)
        under = max(0.0, target_x-sx) + max(0.0, target_y-sy)
        score = (0 if meta["fit_valid"] else 1, over, under, abs(sx-target_x)+abs(sy-target_y), nx*ny)
        rec = (score, angle, atoms, lat, nx, ny, span, meta)
        if best is None or score < best[0]:
            best = rec
    if best is None:
        fail("Could not choose illite orientation")
    return best[1:]


def replicate_full_cells(template: List[Atom], lattice: np.ndarray, nx: int, ny: int, nz: int) -> Tuple[List[Atom], int]:
    xyz = xyz_of(template)
    base = shift_atoms(template, -xyz.min(axis=0))
    max_resid = max((a.resid for a in base), default=1)
    out: List[Atom] = []
    copy_id = 0
    for ix in range(nx):
        for iy in range(ny):
            for iz in range(nz):
                t = ix*lattice[0] + iy*lattice[1] + iz*lattice[2]
                roff = copy_id * max_resid
                for a in base:
                    out.append(replace(a, resid=a.resid+roff, x=a.x+t[0], y=a.y+t[1], z=a.z+t[2]))
                copy_id += 1
    return out, copy_id


def parse_itp_summary(path: Optional[Path]) -> dict:
    out = {"itp_found": bool(path), "moleculetype": "UNKNOWN", "itp_atom_count": None}
    if path is None or not path.exists():
        return out
    section = ""; mol = None; count = 0
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.split(";",1)[0].strip()
        if not line:
            continue
        if line.startswith("[") and "]" in line:
            section = line.strip("[] ").lower(); continue
        if section == "moleculetype" and mol is None:
            mol = line.split()[0]
        elif section == "atoms":
            p = line.split()
            if p and p[0].isdigit():
                count += 1
    out["moleculetype"] = mol or "UNKNOWN"
    out["itp_atom_count"] = count
    return out


def write_index(path: Path, nkero: int, nill: int) -> None:
    def emit(f, name: str, vals: List[int]):
        f.write(f"[ {name} ]\n")
        for i in range(0, len(vals), 15):
            f.write(" ".join(map(str, vals[i:i+15])) + "\n")
    with path.open("w", encoding="utf-8") as f:
        emit(f, "KERO_EXACT", list(range(1, nkero+1)))
        emit(f, "ILLITE", list(range(nkero+1, nkero+nill+1)))
        emit(f, "SOLID_ALL", list(range(1, nkero+nill+1)))


def verify_exact_kerogen(input_atoms: List[Atom], combined_path: Path) -> dict:
    _, combined, _ = read_gro(combined_path)
    if len(combined) < len(input_atoms):
        fail("Combined GRO has fewer atoms than input kerogen")
    first = combined[:len(input_atoms)]
    a = xyz_of(input_atoms); b = xyz_of(first)
    maxdiff = float(np.max(np.abs(a-b))) if len(a) else 0.0
    same_names = all(x.resname == y.resname and x.atomname == y.atomname for x,y in zip(input_atoms, first))
    if maxdiff > 1e-9 or not same_names:
        fail(
            f"KEROGEN IMMUTABILITY CHECK FAILED: max coordinate difference={maxdiff:.12g} nm, "
            f"same_names={same_names}. Output was not accepted."
        )
    return {"kerogen_max_abs_coordinate_change_nm": maxdiff, "kerogen_atom_names_preserved": same_names}


def copy_forcefield_tree(input_dir: Path, out_root: Path) -> None:
    dst = out_root / "00_INPUT_FORCEFIELD_COPY"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(input_dir, dst)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="illite_below_raw_final_kerogen_v31_config.json")
    ap.add_argument("--case", default="")
    args = ap.parse_args()

    root = Path.cwd()
    cfg = load_json(root / args.config)
    cases = [args.case] if args.case else list(cfg.get("cases", []))
    if not cases:
        fail("No cases configured")

    input_dir = root / str(cfg.get("input_dir", "00_INPUT"))
    if not input_dir.exists():
        fail(f"Missing {input_dir}")
    illite_structure = discover_illite(input_dir, str(cfg.get("illite_structure_file", "auto")))
    illite_itp = discover_itp(input_dir, str(cfg.get("illite_itp_file", "auto")))
    _, ill_template, lattice = load_structure(illite_structure)
    if abs(np.linalg.det(lattice)) < 1e-10:
        fail("Illite lattice is singular; provide GRO box vectors or PDB CRYST1")
    itp = parse_itp_summary(illite_itp)

    out_root = root / str(cfg.get("output_dir", "ILLITE_BELOW_RAW_FINAL_KEROGEN_V31"))
    out_root.mkdir(parents=True, exist_ok=True)
    copy_forcefield_tree(input_dir, out_root)

    reports = []
    for case in cases:
        try:
            kpath = resolve_exact_kerogen(root, case, cfg)
        except RuntimeError as e:
            if bool(cfg.get("skip_missing_cases", True)):
                print(f"WARNING: {e}")
                continue
            raise

        ktitle, kerogen, kbox_mat = read_gro(kpath)
        if not kerogen:
            fail(f"No atoms in exact kerogen file: {kpath}")
        kxyz = xyz_of(kerogen)
        xmin,xmax = float(kxyz[:,0].min()), float(kxyz[:,0].max())
        ymin,ymax = float(kxyz[:,1].min()), float(kxyz[:,1].max())
        zmin,zmax = float(kxyz[:,2].min()), float(kxyz[:,2].max())
        kspanx,kspany,kspanz = xmax-xmin, ymax-ymin, zmax-zmin
        kcx,kcy = 0.5*(xmin+xmax), 0.5*(ymin+ymax)

        margin = float(cfg.get("illite_xy_margin_each_side_nm", 0.0))
        target_x = kspanx + 2*margin
        target_y = kspany + 2*margin
        fit_mode = str(cfg.get("illite_xy_fit_mode", "inside")).lower()
        overshoot_tol = float(cfg.get("illite_max_overshoot_each_axis_nm", 0.15))
        angle, itempl, ilat, nx, ny, span, fitmeta = choose_compact_orientation(
            ill_template, lattice, target_x, target_y,
            int(cfg.get("max_repeat_per_axis", 80)), fit_mode, overshoot_tol,
            bool(cfg.get("auto_try_90deg_xy", True))
        )
        nz = int(cfg.get("illite_repeat_z", 1))
        if nz < 1:
            fail("illite_repeat_z must be >= 1")
        illite, copies = replicate_full_cells(itempl, ilat, nx, ny, nz)
        ixyz = xyz_of(illite)

        # ONLY illite is moved. Kerogen remains untouched.
        icx = 0.5*(float(ixyz[:,0].min()) + float(ixyz[:,0].max()))
        icy = 0.5*(float(ixyz[:,1].min()) + float(ixyz[:,1].max()))
        illite = shift_atoms(illite, [kcx-icx, kcy-icy, 0.0])
        ixyz = xyz_of(illite)

        gap = float(cfg.get("gap_illite_top_to_kerogen_bottom_nm", 0.30))
        ill_top_now = float(ixyz[:,2].max())
        target_ill_top = zmin - gap
        illite = shift_atoms(illite, [0.0, 0.0, target_ill_top - ill_top_now])
        ixyz = xyz_of(illite)

        # Keep kerogen coordinates EXACT. A small positive lower clearance is enough;
        # do not reject a valid model merely because the illite bottom is below 0.10 nm.
        strict_positive = bool(cfg.get("strict_keep_kerogen_coordinates", True))
        bottom_pad = float(cfg.get("minimum_box_bottom_clearance_nm", 0.02))
        ill_bottom = float(ixyz[:,2].min())
        if ill_bottom < bottom_pad:
            # Optional no-shift rescue: reduce only the interface gap, moving ILLITE upward.
            # Kerogen is still untouched. This is allowed only down to min_gap.
            min_gap = float(cfg.get("minimum_allowed_interface_gap_nm", 0.20))
            current_gap = gap
            need_up = bottom_pad - ill_bottom
            rescued_gap = current_gap - need_up
            if bool(cfg.get("auto_reduce_gap_to_fit_without_moving_kerogen", True)) and rescued_gap >= min_gap:
                illite = shift_atoms(illite, [0.0, 0.0, need_up])
                ixyz = xyz_of(illite)
                gap = rescued_gap
                ill_bottom = float(ixyz[:,2].min())
                print(
                    f"V31 GAP RESCUE {case}: kerogen unchanged; interface gap "
                    f"{current_gap:.3f} -> {gap:.3f} nm, illite bottom -> {ill_bottom:.3f} nm"
                )
            else:
                msg = (
                    f"{case}: exact kerogen zmin={zmin:.3f} nm leaves insufficient room below for "
                    f"2-layer illite at requested gap={current_gap:.3f} nm "
                    f"(illite bottom={ill_bottom:.3f} nm; required >= {bottom_pad:.3f} nm)."
                )
                if strict_positive:
                    fail(msg + " Kerogen will NOT be shifted. Lower minimum_box_bottom_clearance_nm, reduce gap, or reduce illite_repeat_z.")
                else:
                    fail(msg + " V31 intentionally does not auto-shift kerogen.")

        # Keep original kerogen residue/atom order. Renumber only illite residues to avoid clashes.
        max_kres = max((a.resid for a in kerogen), default=1)
        illite = [replace(a, resid=a.resid+max_kres+100) for a in illite]
        combined = list(kerogen) + illite

        # Box may be enlarged, but kerogen coordinates are unchanged.
        original_box = np.diag(kbox_mat) if np.allclose(kbox_mat, np.diag(np.diag(kbox_mat))) else np.array([
            np.linalg.norm(kbox_mat[0]), np.linalg.norm(kbox_mat[1]), np.linalg.norm(kbox_mat[2])
        ])
        allxyz = xyz_of(combined)
        pad_xy = float(cfg.get("box_xy_extra_nm", 0.20))
        pad_top = float(cfg.get("box_top_extra_nm", 1.00))
        bx = max(float(original_box[0]), float(allxyz[:,0].max()) + pad_xy)
        by = max(float(original_box[1]), float(allxyz[:,1].max()) + pad_xy)
        bz = max(float(original_box[2]), float(allxyz[:,2].max()) + pad_top)
        box = [bx, by, bz]

        od = out_root / case
        od.mkdir(parents=True, exist_ok=True)
        exact_copy = od / f"{case}_EXACT_KEROGEN_INPUT_COPY.gro"
        shutil.copy2(kpath, exact_copy)
        ill_out = od / f"{case}_illite_only.gro"
        comb_out = od / f"{case}_EXACT_kerogen_plus_illite.gro"
        write_gro(ill_out, f"{case} illite under exact final kerogen", illite, box)
        write_gro(comb_out, f"{case} EXACT final kerogen unchanged + illite below", combined, box)
        write_index(od / f"{case}_index.ndx", len(kerogen), len(illite))
        if illite_itp:
            shutil.copy2(illite_itp, od / illite_itp.name)

        verify = verify_exact_kerogen(kerogen, comb_out)
        iz = xyz_of(illite)
        actual_gap = float(kxyz[:,2].min() - iz[:,2].max())
        report = {
            "case": case,
            "kerogen_source_mode": cfg.get("kerogen_source_mode", "raw_exact"),
            "kerogen_exact_input": str(kpath.relative_to(root)),
            "kerogen_input_sha256": sha256_file(kpath),
            "kerogen_title": ktitle,
            "kerogen_atoms": len(kerogen),
            "kerogen_xmin_nm": xmin,
            "kerogen_xmax_nm": xmax,
            "kerogen_ymin_nm": ymin,
            "kerogen_ymax_nm": ymax,
            "kerogen_zmin_nm": zmin,
            "kerogen_zmax_nm": zmax,
            "kerogen_length_x_nm": kspanx,
            "kerogen_width_y_nm": kspany,
            "kerogen_thickness_z_nm": kspanz,
            **verify,
            "illite_structure": str(illite_structure.relative_to(root)),
            "illite_itp": str(illite_itp.relative_to(root)) if illite_itp else "NOT_FOUND",
            "illite_xy_fit_mode": fit_mode,
            "illite_xy_orientation_deg": angle,
            "illite_repeat_nx": nx,
            "illite_repeat_ny": ny,
            "illite_repeat_nz": nz,
            "illite_complete_cell_copies": copies,
            "illite_atoms": len(illite),
            "illite_actual_x_nm": float(iz[:,0].max()-iz[:,0].min()),
            "illite_actual_y_nm": float(iz[:,1].max()-iz[:,1].min()),
            "illite_actual_z_nm": float(iz[:,2].max()-iz[:,2].min()),
            "illite_minus_kerogen_x_nm": float((iz[:,0].max()-iz[:,0].min())-kspanx),
            "illite_minus_kerogen_y_nm": float((iz[:,1].max()-iz[:,1].min())-kspany),
            "actual_gap_illite_top_to_kerogen_minz_nm": actual_gap,
            "combined_atoms": len(combined),
            "output_combined_gro": str(comb_out.relative_to(root)),
            "output_exact_kerogen_copy": str(exact_copy.relative_to(root)),
            "box_x_nm": bx,
            "box_y_nm": by,
            "box_z_nm": bz,
            "illite_itp_moleculetype": itp.get("moleculetype"),
            "illite_itp_atom_count": itp.get("itp_atom_count"),
            "illite_template_atom_count": len(ill_template),
            "illite_topology_replication_safe": bool(illite_itp and itp.get("itp_atom_count") == len(ill_template)),
        }
        reports.append(report)
        dump_json(od / f"{case}_build_report.json", report)
        with (od / f"{case}_build_report.csv").open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=list(report.keys())); w.writeheader(); w.writerow(report)

        print("="*72)
        print(f"DONE {case}")
        print(f"EXACT KEROGEN USED: {kpath}")
        print(f"KEROGEN COORDINATE CHANGE: {verify['kerogen_max_abs_coordinate_change_nm']:.6f} nm")
        print(f"KEROGEN SIZE: {kspanx:.3f} x {kspany:.3f} x {kspanz:.3f} nm")
        print(f"ILLITE SIZE: {report['illite_actual_x_nm']:.3f} x {report['illite_actual_y_nm']:.3f} x {report['illite_actual_z_nm']:.3f} nm")
        print(f"ILLITE REPEATS: {nx} x {ny} x {nz}, XY angle={angle} deg")
        print(f"OUTPUT: {comb_out}")

    if reports:
        summary = out_root / "V31_BUILD_REPORT_ALL.csv"
        with summary.open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=list(reports[0].keys())); w.writeheader(); w.writerows(reports)
        print("SUMMARY:", summary)
    else:
        fail("No cases were built")


if __name__ == "__main__":
    main()
