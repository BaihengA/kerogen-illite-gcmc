# -*- coding: utf-8 -*-
"""
Build a quartz slab under a rough kerogen plate.

Purpose:
  - keep kerogen rough surface upward;
  - place a flat quartz wall under the lower/flat side of kerogen;
  - make quartz x/y footprint match the kerogen plate footprint;
  - output quartz-only GRO, oriented kerogen GRO, combined GRO, and a GROMACS ITP.

The quartz geometry is alpha-quartz-like crystalline SiO2 generated from unit-cell
fractional coordinates and cropped to a rectangular slab. It is intended as a
fixed/mineral support wall; force-field parameters must be checked against your
main force field before production MD.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path
from typing import List, Tuple, Dict
import numpy as np

from gro_tools import GroAtom, read_gro, write_gro, select_kerogen_atoms, atoms_to_xyz, copy_atoms, shift_atoms
from analyze_rough_surface import make_surface_grid, surface_metrics

# Alpha-quartz approximate parameters, nm.
A_Q = 0.4913
C_Q = 0.5405
U_SI = 0.4697
X_O = 0.4133
Y_O = 0.2672
Z_O = 0.1188


def frac_mod(v):
    return v - math.floor(v)


def alpha_quartz_fractional_atoms() -> List[Tuple[str, Tuple[float, float, float]]]:
    # Space group P3121-like minimal fractional positions; 3 Si + 6 O.
    si = [
        (U_SI, 0.0, 0.0),
        (0.0, U_SI, 2.0 / 3.0),
        (-U_SI, -U_SI, 1.0 / 3.0),
    ]
    x, y, z = X_O, Y_O, Z_O
    oxy = [
        (x, y, z),
        (-y, x - y, z + 2.0 / 3.0),
        (-x + y, -x, z + 1.0 / 3.0),
        (-x, -y, -z),
        (y, -x + y, -z + 1.0 / 3.0),
        (x - y, x, -z + 2.0 / 3.0),
    ]
    atoms = []
    for f in si:
        atoms.append(('SI', tuple(frac_mod(v) for v in f)))
    for f in oxy:
        atoms.append(('OQ', tuple(frac_mod(v) for v in f)))
    return atoms


def frac_to_cart(frac: Tuple[float, float, float], origin=(0.0, 0.0, 0.0)) -> np.ndarray:
    f1, f2, f3 = frac
    a1 = np.array([A_Q, 0.0, 0.0])
    a2 = np.array([-0.5 * A_Q, math.sqrt(3.0) * 0.5 * A_Q, 0.0])
    a3 = np.array([0.0, 0.0, C_Q])
    return np.asarray(origin) + f1 * a1 + f2 * a2 + f3 * a3


def generate_quartz_slab(x0: float, x1: float, y0: float, y1: float, z0: float, z1: float,
                         padding_nm: float = 0.8, neutralize: bool = True,
                         q_si_base: float = 2.10) -> Tuple[List[GroAtom], Dict[str, float]]:
    """Generate a cropped rectangular alpha-quartz-like slab."""
    frac_atoms = alpha_quartz_fractional_atoms()
    # Generate sufficiently large triclinic supercell then crop to rectangular ranges.
    nx = int(math.ceil((x1 - x0 + 2 * padding_nm) / A_Q)) + 8
    ny = int(math.ceil((y1 - y0 + 2 * padding_nm) / (math.sqrt(3) * 0.5 * A_Q))) + 8
    nz = int(math.ceil((z1 - z0 + 2 * padding_nm) / C_Q)) + 4
    origin = np.array([x0 - padding_nm + 2.0 * A_Q, y0 - padding_nm, z0 - padding_nm])
    atoms: List[GroAtom] = []
    resid = 1
    atomnr = 1
    for i in range(-2, nx):
        for j in range(-2, ny):
            for k in range(-1, nz):
                cell_shift = i * np.array([A_Q, 0.0, 0.0]) + j * np.array([-0.5 * A_Q, math.sqrt(3) * 0.5 * A_Q, 0.0]) + k * np.array([0.0, 0.0, C_Q])
                for name, frac in frac_atoms:
                    pos = frac_to_cart(frac, origin=origin + cell_shift)
                    if x0 <= pos[0] <= x1 and y0 <= pos[1] <= y1 and z0 <= pos[2] <= z1:
                        atoms.append(GroAtom(resid=resid, resname='QTZ', atomname=name, atomnr=atomnr,
                                             x=float(pos[0]), y=float(pos[1]), z=float(pos[2])))
                        atomnr += 1
                resid += 1
    n_si = sum(1 for a in atoms if a.atomname.upper().startswith('SI'))
    n_o = len(atoms) - n_si
    if n_si == 0 or n_o == 0:
        raise RuntimeError('Generated quartz slab has no Si or no O atoms. Check slab dimensions.')
    q_si = q_si_base
    q_o = -q_si * n_si / n_o if neutralize else -1.05
    report = {
        'quartz_atom_count': len(atoms),
        'quartz_Si_count': n_si,
        'quartz_O_count': n_o,
        'quartz_x_min_nm': min(a.x for a in atoms),
        'quartz_x_max_nm': max(a.x for a in atoms),
        'quartz_y_min_nm': min(a.y for a in atoms),
        'quartz_y_max_nm': max(a.y for a in atoms),
        'quartz_z_min_nm': min(a.z for a in atoms),
        'quartz_z_max_nm': max(a.z for a in atoms),
        'quartz_q_Si': q_si,
        'quartz_q_O': q_o,
        'quartz_total_charge': q_si * n_si + q_o * n_o,
    }
    return atoms, report


def compute_top_bottom_rms(xyz: np.ndarray, grid_nm: float = 0.25) -> Tuple[float, float]:
    x0, x1 = float(np.percentile(xyz[:, 0], 0.5)), float(np.percentile(xyz[:, 0], 99.5))
    y0, y1 = float(np.percentile(xyz[:, 1], 0.5)), float(np.percentile(xyz[:, 1], 99.5))
    X, Y, Ztop, counts = make_surface_grid(xyz, (x0, x1), (y0, y1), grid_nm, 'top')
    _, _, Zbot, _ = make_surface_grid(xyz, (x0, x1), (y0, y1), grid_nm, 'bottom')
    mt = surface_metrics('tmp', xyz, X, Y, Ztop, counts)
    mb = surface_metrics('tmp', xyz, X, Y, Zbot, counts)
    return float(mt['surface_grid_top_rms_detrended_nm']), float(mb['surface_grid_top_rms_detrended_nm'])


def orient_kerogen_rough_top(atoms: List[GroAtom], auto_orient: bool, force_flip: bool = False) -> Tuple[List[GroAtom], Dict[str, float | bool]]:
    atoms = copy_atoms(atoms)
    xyz = atoms_to_xyz(atoms)
    top_rms, bottom_rms = compute_top_bottom_rms(xyz)
    do_flip = force_flip or (auto_orient and bottom_rms > top_rms * 1.15)
    if do_flip:
        zmin, zmax = float(np.min(xyz[:, 2])), float(np.max(xyz[:, 2]))
        for a in atoms:
            a.z = zmin + zmax - a.z
    xyz2 = atoms_to_xyz(atoms)
    top2, bottom2 = compute_top_bottom_rms(xyz2)
    return atoms, {
        'auto_orient': bool(auto_orient),
        'force_flip': bool(force_flip),
        'flipped_z': bool(do_flip),
        'top_rms_before_nm': top_rms,
        'bottom_rms_before_nm': bottom_rms,
        'top_rms_after_nm': top2,
        'bottom_rms_after_nm': bottom2,
    }


def write_quartz_itp(path: Path, quartz_atoms: List[GroAtom], report: Dict[str, float], posres_k: float = 5000000.0) -> None:
    q_si = report['quartz_q_Si']
    q_o = report['quartz_q_O']
    with path.open('w', encoding='utf-8') as f:
        f.write('; Quartz slab generated by build_quartz_under_kerogen.py\n')
        f.write('; IMPORTANT: Check atom types and charges against your force field before production MD.\n\n')
        f.write('[ moleculetype ]\n')
        f.write('; name  nrexcl\nQTZ     1\n\n')
        f.write('[ atoms ]\n')
        f.write('; nr  type  resnr  residue  atom  cgnr  charge  mass\n')
        for i, a in enumerate(quartz_atoms, start=1):
            if a.atomname.upper().startswith('SI'):
                typ, q, mass = 'QSi', q_si, 28.0855
            else:
                typ, q, mass = 'QO', q_o, 15.9994
            f.write(f'{i:6d} {typ:<6s} {1:6d} QTZ {a.atomname:<6s} {i:6d} {q:12.6f} {mass:10.4f}\n')
        f.write('\n#ifdef POSRES_QUARTZ\n')
        f.write('[ position_restraints ]\n')
        f.write('; atom  type      fx          fy          fz\n')
        for i in range(1, len(quartz_atoms) + 1):
            f.write(f'{i:6d}     1  {posres_k:10.1f} {posres_k:10.1f} {posres_k:10.1f}\n')
        f.write('#endif\n')


def write_nonbonded_snippet(path: Path) -> None:
    with path.open('w', encoding='utf-8') as f:
        f.write('; Optional quartz atom type snippet. Insert into your force-field nonbonded section only if these atom types do not exist.\n')
        f.write('; Format is GROMACS OPLS/CHARMM-like: name bond_type atomic_number mass charge ptype sigma epsilon\n')
        f.write('[ atomtypes ]\n')
        f.write('; name  bond_type  atomic_number  mass      charge  ptype  sigma(nm)  epsilon(kJ/mol)\n')
        f.write('QSi     QSi        14             28.0855   0.000   A      0.3000     0.0000\n')
        f.write('QO      QO         8              15.9994   0.000   A      0.3166     0.6500\n')


def find_default_inputs(root: Path) -> List[Path]:
    return sorted(root.glob('02_GRAPHENE_CASES/RMS_*/02_RUN/STANDARD_KEROGEN_PLATE/*_standard_kerogen_plate.gro'))


def infer_label(path: Path) -> str:
    s = path.as_posix()
    for key in ['RMS_0p300', 'RMS_0p600', 'RMS_0p900', 'RMS_0p000']:
        if key in s:
            return key
    return path.stem.replace('_standard_kerogen_plate', '')


def build_one(input_gro: Path, out_root: Path, plate_length: float, plate_width: float,
              quartz_thickness: float | None, gap: float, auto_orient: bool, force_flip: bool,
              x0_arg: float | None, y0_arg: float | None, bottom_percentile: float,
              vacuum_above: float, neutralize: bool) -> Dict[str, float | str | bool]:
    title, atoms, box = read_gro(input_gro)
    k_atoms = select_kerogen_atoms(atoms)
    if not k_atoms:
        k_atoms = atoms
    k_atoms, orient_report = orient_kerogen_rough_top(k_atoms, auto_orient=auto_orient, force_flip=force_flip)
    xyz = atoms_to_xyz(k_atoms)
    label = infer_label(input_gro)
    x0 = float(np.percentile(xyz[:, 0], 0.2)) if x0_arg is None else x0_arg
    y0 = float(np.percentile(xyz[:, 1], 0.2)) if y0_arg is None else y0_arg
    x1 = x0 + plate_length
    y1 = y0 + plate_width
    # Keep only atoms in the fixed x/y footprint for final combined model.
    kept = []
    for a in k_atoms:
        if x0 <= a.x <= x1 and y0 <= a.y <= y1:
            kept.append(a)
    if not kept:
        raise RuntimeError('No kerogen atoms retained in requested x/y footprint.')
    k_atoms = kept
    xyz = atoms_to_xyz(k_atoms)
    bottom_ref = float(np.percentile(xyz[:, 2], bottom_percentile))
    top_ref = float(np.percentile(xyz[:, 2], 99.5))
    kerogen_thickness = float(np.percentile(xyz[:, 2], 95) - np.percentile(xyz[:, 2], 5))
    if quartz_thickness is None or quartz_thickness <= 0:
        quartz_thickness = kerogen_thickness
    qz_top = bottom_ref - gap
    qz_bottom = qz_top - quartz_thickness
    quartz_atoms, quartz_report = generate_quartz_slab(x0, x1, y0, y1, qz_bottom, qz_top, neutralize=neutralize)
    # Renumber residues/atoms for clean output.
    for i, a in enumerate(k_atoms, start=1):
        a.resid = min(a.resid, 99999)
        a.atomnr = i
    for i, a in enumerate(quartz_atoms, start=1):
        a.resid = 1
        a.atomnr = i
    # Combined box.
    zmin = min(min(a.z for a in quartz_atoms), min(a.z for a in k_atoms))
    zmax = max(max(a.z for a in quartz_atoms), max(a.z for a in k_atoms))
    margin = 0.8
    # Shift all atoms so minimum coordinates are positive but preserve x/y footprint origin relationship.
    shift_x = margin - min(x0, min(a.x for a in quartz_atoms), min(a.x for a in k_atoms))
    shift_y = margin - min(y0, min(a.y for a in quartz_atoms), min(a.y for a in k_atoms))
    shift_z = margin - zmin
    shift_atoms(k_atoms, shift_x, shift_y, shift_z)
    shift_atoms(quartz_atoms, shift_x, shift_y, shift_z)
    box_vec = np.array([plate_length + 2 * margin, plate_width + 2 * margin, (zmax - zmin) + vacuum_above + 2 * margin], dtype=float)

    outdir = out_root / label
    outdir.mkdir(parents=True, exist_ok=True)
    kerogen_out = outdir / f'{label}_kerogen_oriented_rough_top.gro'
    quartz_out = outdir / f'{label}_quartz_wall_only.gro'
    combined_out = outdir / f'{label}_quartz_under_kerogen_rough_top.gro'
    write_gro(kerogen_out, f'{label} kerogen rough-top oriented, quartz builder', k_atoms, box_vec)
    write_gro(quartz_out, f'{label} quartz wall only, under kerogen', quartz_atoms, box_vec)
    write_gro(combined_out, f'{label} quartz under kerogen; rough kerogen surface upward', quartz_atoms + k_atoms, box_vec)
    write_quartz_itp(outdir / f'{label}_quartz_wall.itp', quartz_atoms, quartz_report)
    write_nonbonded_snippet(outdir / f'{label}_quartz_nonbonded_snippet.itp')
    (outdir / f'{label}_topol_include_snippet.txt').write_text(
        '#include "{0}_quartz_nonbonded_snippet.itp"\n#include "{0}_quartz_wall.itp"\n\n[ molecules ]\n; add this line with your kerogen molecule counts unchanged:\nQTZ    1\n'.format(label),
        encoding='utf-8'
    )
    report = {
        'label': label,
        'input_gro': str(input_gro),
        'combined_gro': str(combined_out),
        'quartz_only_gro': str(quartz_out),
        'kerogen_oriented_gro': str(kerogen_out),
        'plate_length_x_nm': plate_length,
        'plate_width_y_nm': plate_width,
        'gap_between_quartz_top_and_kerogen_bottom_ref_nm': gap,
        'bottom_percentile_used': bottom_percentile,
        'kerogen_atom_count_retained': len(k_atoms),
        'kerogen_thickness_p95_p05_nm': kerogen_thickness,
        'quartz_thickness_nm': quartz_thickness,
        'quartz_top_z_before_shift_nm': qz_top,
        'quartz_bottom_z_before_shift_nm': qz_bottom,
        'box_x_nm': float(box_vec[0]),
        'box_y_nm': float(box_vec[1]),
        'box_z_nm': float(box_vec[2]),
        **orient_report,
        **quartz_report,
    }
    (outdir / f'{label}_quartz_build_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    with (outdir / f'{label}_quartz_build_report.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(list(report.keys()))
        w.writerow([report[k] for k in report.keys()])
    return report


def main():
    p = argparse.ArgumentParser(description='Build quartz wall under a rough-top kerogen plate.')
    p.add_argument('--root', default='.', help='Project root. Default current directory.')
    p.add_argument('--input', action='append', help='Input standard kerogen plate GRO. Can repeat. If omitted, auto-detect.')
    p.add_argument('--outdir', default='QUARTZ_UNDER_KEROGEN', help='Output directory.')
    p.add_argument('--plate-length', type=float, default=12.0, help='Quartz/kerogen target x length in nm.')
    p.add_argument('--plate-width', type=float, default=12.0, help='Quartz/kerogen target y width in nm.')
    p.add_argument('--quartz-thickness', type=float, default=-1.0, help='Quartz thickness in nm. <=0 means use kerogen p95-p05 thickness.')
    p.add_argument('--gap', type=float, default=0.25, help='Gap between quartz top and kerogen lower reference surface in nm.')
    p.add_argument('--bottom-percentile', type=float, default=2.0, help='Kerogen lower surface percentile used for quartz placement.')
    p.add_argument('--x0', type=float, default=None, help='Optional x origin of 12 nm target footprint.')
    p.add_argument('--y0', type=float, default=None, help='Optional y origin of 12 nm target footprint.')
    p.add_argument('--vacuum-above', type=float, default=4.0, help='Extra z space above rough kerogen top in nm.')
    p.add_argument('--no-auto-orient', action='store_true', help='Disable automatic z flip to keep rougher side upward.')
    p.add_argument('--force-flip-z', action='store_true', help='Force flip z orientation.')
    p.add_argument('--no-neutralize-quartz', action='store_true', help='Do not adjust quartz O charge to neutralize cropped slab.')
    args = p.parse_args()

    root = Path(args.root).resolve()
    inputs = [Path(v).resolve() for v in args.input] if args.input else find_default_inputs(root)
    if not inputs:
        raise SystemExit('No standard kerogen plate GRO found. Provide --input or run after plate extraction.')
    out_root = (root / args.outdir).resolve()
    out_root.mkdir(parents=True, exist_ok=True)
    reports = []
    for inp in inputs:
        print(f'BUILD QUARTZ UNDER: {inp}')
        rep = build_one(
            input_gro=inp,
            out_root=out_root,
            plate_length=args.plate_length,
            plate_width=args.plate_width,
            quartz_thickness=None if args.quartz_thickness <= 0 else args.quartz_thickness,
            gap=args.gap,
            auto_orient=not args.no_auto_orient,
            force_flip=args.force_flip_z,
            x0_arg=args.x0,
            y0_arg=args.y0,
            bottom_percentile=args.bottom_percentile,
            vacuum_above=args.vacuum_above,
            neutralize=not args.no_neutralize_quartz,
        )
        reports.append(rep)
    keys = []
    for r in reports:
        for k in r.keys():
            if k not in keys:
                keys.append(k)
    with (out_root / 'QUARTZ_BUILD_REPORT_ALL.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(keys)
        for r in reports:
            w.writerow([r.get(k, '') for k in keys])
    print(f'DONE: {out_root / "QUARTZ_BUILD_REPORT_ALL.csv"}')

if __name__ == '__main__':
    main()
