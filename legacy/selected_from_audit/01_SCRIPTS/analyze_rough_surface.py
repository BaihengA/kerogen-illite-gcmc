# -*- coding: utf-8 -*-
"""
Analyze and plot rough kerogen surfaces from GRO files.
Outputs:
  - 3D top surface plot similar in spirit to rough-wall figures in MD papers
  - contour map
  - surface grid CSV
  - metrics CSV/JSON
  - optional batch processing for RMS_0p300/0p600/0p900 standard plates
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path
from typing import List, Dict, Tuple
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

from gro_tools import read_gro, select_kerogen_atoms, atoms_to_xyz


def robust_plane_detrend(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> Tuple[np.ndarray, Tuple[float, float, float]]:
    valid = np.isfinite(z)
    if valid.sum() < 6:
        return z * np.nan, (0.0, 0.0, float(np.nanmean(z)))
    A = np.column_stack([x[valid], y[valid], np.ones(valid.sum())])
    coeff, *_ = np.linalg.lstsq(A, z[valid], rcond=None)
    plane = coeff[0] * x + coeff[1] * y + coeff[2]
    return z - plane, (float(coeff[0]), float(coeff[1]), float(coeff[2]))


def make_surface_grid(xyz: np.ndarray, x_range: Tuple[float, float], y_range: Tuple[float, float], grid_nm: float,
                      mode: str = 'top') -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    x0, x1 = x_range
    y0, y1 = y_range
    nx = max(2, int(math.ceil((x1 - x0) / grid_nm)))
    ny = max(2, int(math.ceil((y1 - y0) / grid_nm)))
    xs = x0 + (np.arange(nx) + 0.5) * (x1 - x0) / nx
    ys = y0 + (np.arange(ny) + 0.5) * (y1 - y0) / ny
    X, Y = np.meshgrid(xs, ys, indexing='xy')
    Z = np.full((ny, nx), np.nan, dtype=float)
    counts = np.zeros((ny, nx), dtype=int)

    ix = np.floor((xyz[:, 0] - x0) / (x1 - x0) * nx).astype(int)
    iy = np.floor((xyz[:, 1] - y0) / (y1 - y0) * ny).astype(int)
    mask = (ix >= 0) & (ix < nx) & (iy >= 0) & (iy < ny)
    for i, j, z in zip(ix[mask], iy[mask], xyz[:, 2][mask]):
        if counts[j, i] == 0:
            Z[j, i] = z
        else:
            if mode == 'top':
                if z > Z[j, i]:
                    Z[j, i] = z
            else:
                if z < Z[j, i]:
                    Z[j, i] = z
        counts[j, i] += 1
    return X, Y, Z, counts


def fill_nan_by_neighbors(Z: np.ndarray, max_iter: int = 80) -> np.ndarray:
    Zf = Z.copy()
    if np.isfinite(Zf).all():
        return Zf
    global_mean = np.nanmean(Zf)
    if not np.isfinite(global_mean):
        return np.zeros_like(Zf)
    for _ in range(max_iter):
        nan_mask = ~np.isfinite(Zf)
        if not nan_mask.any():
            break
        new = Zf.copy()
        changed = 0
        for j, i in zip(*np.where(nan_mask)):
            vals = []
            for dj in (-1, 0, 1):
                for di in (-1, 0, 1):
                    if dj == 0 and di == 0:
                        continue
                    jj, ii = j + dj, i + di
                    if 0 <= jj < Zf.shape[0] and 0 <= ii < Zf.shape[1] and np.isfinite(Zf[jj, ii]):
                        vals.append(Zf[jj, ii])
            if vals:
                new[j, i] = float(np.mean(vals))
                changed += 1
        Zf = new
        if changed == 0:
            break
    Zf[~np.isfinite(Zf)] = global_mean
    return Zf


def surface_metrics(label: str, xyz: np.ndarray, X: np.ndarray, Y: np.ndarray, Z: np.ndarray, counts: np.ndarray,
                    bottom_Z: np.ndarray | None = None) -> Dict[str, float | str]:
    valid = np.isfinite(Z)
    coverage = float(valid.mean())
    z_valid = Z[valid]
    Zfill = fill_nan_by_neighbors(Z)
    residual, plane = robust_plane_detrend(X, Y, Zfill)
    res_valid = residual[np.isfinite(residual)]
    m: Dict[str, float | str] = {
        'label': label,
        'atom_count': int(xyz.shape[0]),
        'atom_x_min_nm': float(np.min(xyz[:, 0])),
        'atom_x_max_nm': float(np.max(xyz[:, 0])),
        'atom_y_min_nm': float(np.min(xyz[:, 1])),
        'atom_y_max_nm': float(np.max(xyz[:, 1])),
        'atom_z_min_nm': float(np.min(xyz[:, 2])),
        'atom_z_max_nm': float(np.max(xyz[:, 2])),
        'plate_length_x_nm': float(np.max(xyz[:, 0]) - np.min(xyz[:, 0])),
        'plate_width_y_nm': float(np.max(xyz[:, 1]) - np.min(xyz[:, 1])),
        'thickness_minmax_nm': float(np.max(xyz[:, 2]) - np.min(xyz[:, 2])),
        'thickness_p95_p05_nm': float(np.percentile(xyz[:, 2], 95) - np.percentile(xyz[:, 2], 5)),
        'surface_grid_coverage': coverage,
        'surface_grid_top_mean_nm': float(np.nanmean(z_valid)),
        'surface_grid_top_rms_raw_nm': float(np.sqrt(np.nanmean((z_valid - np.nanmean(z_valid)) ** 2))),
        'surface_grid_top_peak_to_valley_raw_nm': float(np.nanmax(z_valid) - np.nanmin(z_valid)),
        'surface_grid_top_rms_detrended_nm': float(np.sqrt(np.nanmean(res_valid ** 2))),
        'surface_grid_top_peak_to_valley_detrended_nm': float(np.nanmax(res_valid) - np.nanmin(res_valid)),
        'top_plane_a': plane[0],
        'top_plane_b': plane[1],
        'top_plane_c': plane[2],
    }
    if bottom_Z is not None:
        vb = np.isfinite(bottom_Z)
        if vb.any():
            bot = bottom_Z[vb]
            m['surface_grid_bottom_mean_nm'] = float(np.nanmean(bot))
            m['surface_grid_bottom_rms_raw_nm'] = float(np.sqrt(np.nanmean((bot - np.nanmean(bot)) ** 2)))
            m['surface_grid_bottom_peak_to_valley_raw_nm'] = float(np.nanmax(bot) - np.nanmin(bot))
            # Local thickness where both top and bottom are present.
            both = np.isfinite(Z) & np.isfinite(bottom_Z)
            if both.any():
                t = Z[both] - bottom_Z[both]
                m['surface_grid_local_thickness_mean_nm'] = float(np.mean(t))
                m['surface_grid_local_thickness_rms_nm'] = float(np.sqrt(np.mean((t - np.mean(t)) ** 2)))
    return m


def plot_surface(label: str, X: np.ndarray, Y: np.ndarray, Z: np.ndarray, out_prefix: Path, title_extra: str = '') -> None:
    Zfill = fill_nan_by_neighbors(Z)
    residual, _ = robust_plane_detrend(X, Y, Zfill)

    fig = plt.figure(figsize=(7.5, 5.8), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Zfill, cmap='viridis', linewidth=0, antialiased=True, alpha=0.96)
    ax.set_xlabel('x / nm')
    ax.set_ylabel('y / nm')
    ax.set_zlabel('z / nm')
    ax.set_title(f'{label} top surface {title_extra}'.strip())
    ax.view_init(elev=28, azim=-55)
    fig.colorbar(surf, ax=ax, shrink=0.62, pad=0.08, label='z / nm')
    fig.tight_layout()
    fig.savefig(out_prefix.with_name(out_prefix.name + '_top_surface_3D.png'))
    plt.close(fig)

    fig = plt.figure(figsize=(7.2, 5.8), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, residual, cmap='coolwarm', linewidth=0, antialiased=True, alpha=0.96)
    ax.set_xlabel('x / nm')
    ax.set_ylabel('y / nm')
    ax.set_zlabel('detrended height / nm')
    ax.set_title(f'{label} detrended rough surface')
    ax.view_init(elev=30, azim=-55)
    fig.colorbar(surf, ax=ax, shrink=0.62, pad=0.08, label='height residual / nm')
    fig.tight_layout()
    fig.savefig(out_prefix.with_name(out_prefix.name + '_top_surface_3D_detrended.png'))
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.8, 5.6), dpi=300)
    im = ax.contourf(X, Y, Zfill, levels=40, cmap='viridis')
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('x / nm')
    ax.set_ylabel('y / nm')
    ax.set_title(f'{label} top surface contour')
    fig.colorbar(im, ax=ax, label='z / nm')
    fig.tight_layout()
    fig.savefig(out_prefix.with_name(out_prefix.name + '_top_surface_contour.png'))
    plt.close(fig)


def save_grid_csv(path: Path, X: np.ndarray, Y: np.ndarray, Z: np.ndarray, counts: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['x_nm', 'y_nm', 'top_z_nm', 'atom_count_in_cell'])
        for j in range(Z.shape[0]):
            for i in range(Z.shape[1]):
                w.writerow([f'{X[j, i]:.6f}', f'{Y[j, i]:.6f}', '' if not np.isfinite(Z[j, i]) else f'{Z[j, i]:.6f}', int(counts[j, i])])


def infer_label(path: Path) -> str:
    s = path.as_posix()
    for key in ['RMS_0p300', 'RMS_0p600', 'RMS_0p900', 'RMS_0p000']:
        if key in s:
            return key
    return path.stem.replace('_standard_kerogen_plate', '')


def find_default_inputs(root: Path) -> List[Path]:
    return sorted(root.glob('02_GRAPHENE_CASES/RMS_*/02_RUN/STANDARD_KEROGEN_PLATE/*_standard_kerogen_plate.gro'))


def analyze_one(path: Path, outdir: Path, grid_nm: float, plate_length_nm: float | None, plate_width_nm: float | None,
                x0: float | None = None, y0: float | None = None) -> Dict[str, float | str]:
    _, atoms, box = read_gro(path)
    k_atoms = select_kerogen_atoms(atoms)
    if not k_atoms:
        k_atoms = atoms
    xyz = atoms_to_xyz(k_atoms)
    label = infer_label(path)

    if x0 is None:
        x0 = float(np.percentile(xyz[:, 0], 0.2))
    if y0 is None:
        y0 = float(np.percentile(xyz[:, 1], 0.2))
    if plate_length_nm is None:
        x1 = float(np.percentile(xyz[:, 0], 99.8))
    else:
        x1 = x0 + plate_length_nm
    if plate_width_nm is None:
        y1 = float(np.percentile(xyz[:, 1], 99.8))
    else:
        y1 = y0 + plate_width_nm

    X, Y, Ztop, counts = make_surface_grid(xyz, (x0, x1), (y0, y1), grid_nm, mode='top')
    _, _, Zbot, _ = make_surface_grid(xyz, (x0, x1), (y0, y1), grid_nm, mode='bottom')
    metrics = surface_metrics(label, xyz, X, Y, Ztop, counts, Zbot)
    metrics['input_gro'] = str(path)
    metrics['analysis_x0_nm'] = float(x0)
    metrics['analysis_x1_nm'] = float(x1)
    metrics['analysis_y0_nm'] = float(y0)
    metrics['analysis_y1_nm'] = float(y1)
    metrics['grid_nm'] = float(grid_nm)

    case_out = outdir / label
    case_out.mkdir(parents=True, exist_ok=True)
    prefix = case_out / label
    save_grid_csv(prefix.with_name(prefix.name + '_top_surface_grid.csv'), X, Y, Ztop, counts)
    plot_surface(label, X, Y, Ztop, prefix)
    (case_out / f'{label}_roughness_metrics.json').write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding='utf-8')
    with (case_out / f'{label}_roughness_metrics.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(list(metrics.keys()))
        w.writerow([metrics[k] for k in metrics.keys()])
    return metrics


def main():
    p = argparse.ArgumentParser(description='Analyze kerogen plate roughness and make 3D/contour figures.')
    p.add_argument('--root', default='.', help='Project root. Default: current directory.')
    p.add_argument('--input', action='append', help='Input GRO file. Can be repeated. If omitted, auto-detect standard kerogen plates.')
    p.add_argument('--outdir', default='ROUGHNESS_FIGURES', help='Output directory.')
    p.add_argument('--grid', type=float, default=0.20, help='Surface grid size in nm. Default 0.20 nm.')
    p.add_argument('--plate-length', type=float, default=12.0, help='Analysis x length in nm. Use <=0 for atom percentile extent.')
    p.add_argument('--plate-width', type=float, default=12.0, help='Analysis y width in nm. Use <=0 for atom percentile extent.')
    p.add_argument('--x0', type=float, default=None, help='Optional x origin for analysis window.')
    p.add_argument('--y0', type=float, default=None, help='Optional y origin for analysis window.')
    args = p.parse_args()

    root = Path(args.root).resolve()
    if args.input:
        inputs = [Path(v).resolve() for v in args.input]
    else:
        inputs = find_default_inputs(root)
    if not inputs:
        raise SystemExit('No input GRO found. Provide --input or run after STANDARD_KEROGEN_PLATE files are generated.')
    outdir = (root / args.outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    plate_length = None if args.plate_length <= 0 else args.plate_length
    plate_width = None if args.plate_width <= 0 else args.plate_width

    all_metrics = []
    for path in inputs:
        print(f'ANALYZE: {path}')
        all_metrics.append(analyze_one(path, outdir, args.grid, plate_length, plate_width, args.x0, args.y0))

    # Summary CSV
    keys = []
    for m in all_metrics:
        for k in m.keys():
            if k not in keys:
                keys.append(k)
    with (outdir / 'ROUGHNESS_METRICS_ALL.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(keys)
        for m in all_metrics:
            w.writerow([m.get(k, '') for k in keys])
    print(f'DONE: {outdir / "ROUGHNESS_METRICS_ALL.csv"}')

if __name__ == '__main__':
    main()
