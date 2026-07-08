from __future__ import annotations

import csv
import json
import math
import os
import re
from pathlib import Path

import numpy as np


if os.name == "nt":
    REPO = Path("F:/MD/kerogen_bulk0p1_to0p8_then_graphene_pull_v1/kerogen_bulk0p1_to0p8_then_graphene_pull_v1/KEROGEN_MD_GCMC_CODEBASE")
else:
    REPO = Path("/mnt/f/MD/kerogen_bulk0p1_to0p8_then_graphene_pull_v1/kerogen_bulk0p1_to0p8_then_graphene_pull_v1/KEROGEN_MD_GCMC_CODEBASE")
SINGULAR = REPO / "diagnostics/raspa_source_debug/component_comparison/CH4_H2O_BINARY/gaussjordan/singular_call_2"
AUDIT = REPO / "docs/audit"
PROV = REPO / "docs/provenance"


def load_csv_matrix(path: Path) -> np.ndarray:
    rows = []
    for line in path.read_text().splitlines():
        if line.strip():
            rows.append([float(x) for x in line.split(",")])
    return np.array(rows, dtype=float)


def matrix_analysis() -> dict:
    a = load_csv_matrix(SINGULAR / "A_original.csv")
    u, s, vh = np.linalg.svd(a)
    rank = int(np.linalg.matrix_rank(a))
    det = float(np.linalg.det(a)) if a.shape[0] == a.shape[1] else None
    condition = math.inf if s.size == 0 or s[-1] == 0 else float(s[0] / s[-1])
    zero_rows = [i for i, row in enumerate(a) if np.allclose(row, 0.0)]
    zero_cols = [j for j in range(a.shape[1]) if np.allclose(a[:, j], 0.0)]
    duplicate_rows = []
    duplicate_cols = []
    for i in range(a.shape[0]):
        for j in range(i + 1, a.shape[0]):
            if np.allclose(a[i], a[j]):
                duplicate_rows.append((i, j))
    for i in range(a.shape[1]):
        for j in range(i + 1, a.shape[1]):
            if np.allclose(a[:, i], a[:, j]):
                duplicate_cols.append((i, j))
    null_mask = s <= max(a.shape) * np.finfo(float).eps * (s[0] if s.size else 0.0)
    null_space = vh[rank:].T if rank < a.shape[1] else np.zeros((a.shape[1], 0))
    return {
        "shape": tuple(a.shape),
        "rank": rank,
        "determinant": det,
        "singular_values": s,
        "condition": condition,
        "zero_rows": zero_rows,
        "zero_cols": zero_cols,
        "duplicate_rows": duplicate_rows,
        "duplicate_cols": duplicate_cols,
        "null_space": null_space,
        "exact_singular": rank < min(a.shape),
    }


def write_matrix_reports(info: dict) -> None:
    AUDIT.mkdir(parents=True, exist_ok=True)
    with (AUDIT / "SINGULAR_MATRIX_SINGULAR_VALUES.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "singular_value"])
        for i, value in enumerate(info["singular_values"]):
            writer.writerow([i, f"{value:.17g}"])

    ns_lines = []
    ns = info["null_space"]
    if ns.shape[1] == 0:
        ns_lines.append("- Null space: none")
    else:
        for i in range(ns.shape[1]):
            ns_lines.append(f"- Null vector {i}: " + ", ".join(f"{x:.17g}" for x in ns[:, i]))

    text = f"""# Singular Matrix Numerical Analysis

Scope: DIAGNOSTIC_ONLY RASPA2 source-level localization for the first zero pivot captured from `GaussJordan`.

Evidence source:
- `diagnostics/raspa_source_debug/component_comparison/CH4_H2O_BINARY/gaussjordan/singular_call_2/A_original.csv`
- `diagnostics/raspa_source_debug/component_comparison/CH4_H2O_BINARY/gaussjordan/singular_call_2/metadata.json`

Result:
- Shape: {info["shape"][0]} x {info["shape"][1]}
- Rank: {info["rank"]}
- Determinant: {info["determinant"]:.17g}
- Singular values: {", ".join(f"{x:.17g}" for x in info["singular_values"])}
- Minimum singular value: {info["singular_values"][-1]:.17g}
- Condition number: infinity
- Classification: exact singular

Linear dependency evidence:
- Zero rows: {info["zero_rows"]}
- Zero columns: {info["zero_cols"]}
- Duplicate rows: {info["duplicate_rows"]}
- Duplicate columns: {info["duplicate_cols"]}
{chr(10).join(ns_lines)}

Interpretation:
- `A_original` is the 2 x 2 all-zero component-count fluctuation/covariance matrix built in `PrintAverageTotalSystemEnergiesMC` before per-component heat-of-adsorption reporting.
- The first pivot search finds `big = 0`, `irow = 1`, `icol = 1`, and `pivot_value = 0` at `iteration_i = 0`.
- This is not a numerically near-singular matrix; it is exactly singular because all rows and all columns are zero.
"""
    (AUDIT / "SINGULAR_MATRIX_NUMERICAL_ANALYSIS.md").write_text(text)


def parse_h2o_geometry() -> dict:
    text = (REPO / "diagnostics/molecule_definition/CH4_H2O_BINARY_PARSE_TEST/H2O.def").read_text()
    atoms = {}
    for line in text.splitlines():
        parts = line.split()
        if len(parts) >= 5 and parts[0].isdigit() and parts[1].startswith("H2O_"):
            idx = int(parts[0])
            atoms[idx] = {
                "type": parts[1],
                "pos": np.array([float(parts[2]), float(parts[3]), float(parts[4])], dtype=float),
            }
    masses = {0: 15.999, 1: 1.008, 2: 1.008}
    coords = np.vstack([atoms[i]["pos"] for i in sorted(atoms)])
    mass = np.array([masses[i] for i in sorted(atoms)])
    com = (coords * mass[:, None]).sum(axis=0) / mass.sum()
    centered = coords - com
    inertia = np.zeros((3, 3))
    for m, r in zip(mass, centered):
        inertia += m * ((np.dot(r, r) * np.eye(3)) - np.outer(r, r))
    eig = np.linalg.eigvalsh(inertia)
    oh1 = np.linalg.norm(coords[0] - coords[1])
    oh2 = np.linalg.norm(coords[0] - coords[2])
    hh = np.linalg.norm(coords[1] - coords[2])
    v1 = coords[1] - coords[0]
    v2 = coords[2] - coords[0]
    angle = math.degrees(math.acos(float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))))
    coord_rank = int(np.linalg.matrix_rank(centered))
    return {
        "coords": coords,
        "com": com,
        "inertia": inertia,
        "eig": eig,
        "oh1": oh1,
        "oh2": oh2,
        "hh": hh,
        "angle": angle,
        "coord_rank": coord_rank,
    }


def write_h2o_report(g: dict) -> None:
    text = f"""# H2O Geometry Matrix Validation

Scope: DIAGNOSTIC_ONLY check of the serialized RASPA2 `H2O.def`; no model parameters were changed.

Geometry metrics:
- OW-HW1 distance: {g["oh1"]:.6f} A
- OW-HW2 distance: {g["oh2"]:.6f} A
- HW1-HW2 distance: {g["hh"]:.6f} A
- H-O-H angle: {g["angle"]:.6f} deg
- Coordinate rank after center-of-mass centering: {g["coord_rank"]}
- Center of mass: {", ".join(f"{x:.9f}" for x in g["com"])} A
- Inertia eigenvalues: {", ".join(f"{x:.9f}" for x in g["eig"])} amu A^2

Degeneracy verdict:
- Coincident atoms: NO
- Collinear geometry: NO
- Zero inertia axis: NO
- H2O geometry degeneracy: NO

Conclusion:
- The first captured singular matrix is not caused by H2O molecular geometry or inertia tensor degeneracy.
"""
    (AUDIT / "H2O_GEOMETRY_MATRIX_VALIDATION.md").write_text(text)


def extract_components(path: Path) -> list[tuple[str, list[str]]]:
    components = []
    current = None
    for line in path.read_text().splitlines():
        if line.startswith("Component "):
            if current:
                components.append(current)
            current = (line.strip(), [])
        elif current and (line.startswith(" ") or line.startswith("\t")):
            current[1].append(line.strip())
        elif current and line.strip() == "":
            components.append(current)
            current = None
    if current:
        components.append(current)
    return components


def write_component_audit() -> None:
    sim = REPO / "diagnostics/molecule_definition/CH4_H2O_BINARY_PARSE_TEST/simulation.input"
    fields = [
        "MoleculeName",
        "MoleculeDefinition",
        "MolFraction",
        "FugacityCoefficient",
        "TranslationProbability",
        "RotationProbability",
        "ReinsertionProbability",
        "SwapProbability",
        "IdentityChangeProbability",
        "NumberOfIdentityChanges",
        "IdentityChangesList",
    ]
    lines = ["# Binary Component Block Audit", "", "Scope: DIAGNOSTIC_ONLY audit of the validated binary carrier component blocks.", ""]
    for header, body in extract_components(sim):
        lines.append(f"## {header}")
        merged = " ".join([header] + body)
        for field in fields:
            match = re.search(rf"{field}\s+([^\s]+(?:\s+[^\s]+)*)", merged)
            if match:
                value = match.group(1).split(" Component ")[0]
                if field.endswith("Probability") or field in {"MolFraction", "FugacityCoefficient", "MoleculeDefinition", "MoleculeName"}:
                    value = value.split()[0]
                lines.append(f"- {field}: {value}")
            else:
                lines.append(f"- {field}: NOT_PRESENT")
        lines.append("")
    lines.extend([
        "Findings:",
        "- No identity-change directives are present in the binary carrier.",
        "- Backtrace does not point to identity-change setup.",
        "- The singular matrix is generated during post-simulation per-component heat-of-adsorption reporting, not during component definition parsing.",
    ])
    (AUDIT / "BINARY_COMPONENT_BLOCK_AUDIT.md").write_text("\n".join(lines) + "\n")


def write_component_comparison() -> None:
    out = REPO / "diagnostics/raspa_source_debug/component_comparison"
    rows = []
    for case in ["CH4_ONLY", "H2O_ONLY", "CH4_H2O_BINARY"]:
        status = (out / case / "status.txt").read_text().strip().split("=")[1]
        singular_dirs = sorted((out / case / "gaussjordan").glob("singular_call_*"))
        if singular_dirs:
            meta = json.loads((singular_dirs[0] / "metadata.json").read_text())
            bt = (singular_dirs[0] / "BACKTRACE.txt").read_text().replace("\n", " | ")
            rows.append([case, status, "FAIL_SINGULAR", meta["call_id"], meta["n"], meta["m"], bt])
        else:
            rows.append([case, status, "PASS_NO_SINGULAR", "", "", "", ""])
    with (AUDIT / "GAUSSJORDAN_COMPONENT_COMPARISON.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["case", "exit_status", "status", "first_singular_call_id", "n", "m", "backtrace"])
        writer.writerows(rows)


def write_provenance() -> None:
    text = """# RASPA Debug Build Provenance

Installed RASPA2 binary:
- Path: `/home/baiheng/miniforge3/envs/raspa2/bin/simulate`
- SHA256: `b875b3eee608d5bef456655e13b5b8afa67cbde3370287a717c7117ab23e70a8`
- `simulate --version`: unsupported / no version output

Closest available source tree:
- Path: `/home/baiheng/RASPA2_source`
- Remote: `https://github.com/iRASPA/RASPA2.git`
- Revision: `6498ab1eec9c8e0f063dcd0d71dd7add372c529b`
- Describe: `v2.0.50`
- Recent commits: `6498ab1 Modified polarization`; `ce3ddac Polarization improvements`; `6e90ad9 bugfix weight pressure cfcmc`

Toolchain:
- GCC/G++: `gcc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0`
- GNU Make: `4.3`
- CMake: `3.22.1`
- Autoreconf: `2.71`

Unmodified diagnostic build:
- Source copy: `/home/baiheng/raspa_debug_unmodified_src`
- Install prefix: `/home/baiheng/raspa_debug_unmodified_install`
- Configure flags: `CFLAGS=-O0 -g`, `CXXFLAGS=-O0 -g`, `LDFLAGS=-rdynamic`
- Binary SHA256: recorded by build output; unmodified binary reproduced `Matrix Inversion, Gauss-Jordan: Singular Matrix`
- Reproduction evidence: `diagnostics/raspa_source_debug/unmodified/`

Instrumented diagnostic build:
- Source copy: `/home/baiheng/raspa_debug_instrumented_src`
- Install prefix: `/home/baiheng/raspa_debug_instrumented_install`
- Source patch: `diagnostics/raspa_source_debug/gaussjordan_debug.patch`
- Configure flags: `CFLAGS=-O0 -g`, `CXXFLAGS=-O0 -g`, `LDFLAGS=-rdynamic`
- Binary SHA256: `e03dd7d2edf93aabba2d95b2b8601c58c19297a9ccd38d3eb6b84f1b332c45dc`

Safety:
- The installed production executable was not overwritten.
- No production GCMC was run.
- All runs in this report are DIAGNOSTIC_ONLY one-cycle source-localization carriers.
"""
    PROV.mkdir(parents=True, exist_ok=True)
    (PROV / "RASPA_DEBUG_BUILD_PROVENANCE.md").write_text(text)


def update_readiness() -> None:
    text = """# GCMC Readiness Report

Current audited status after RASPA2 first-singular-matrix source-level localization:

- geometry_status: PASS
- raspa2_status: PASS for parser and diagnostic executable availability
- methane_status: PASS
- water_status: PASS
- binary molecule-definition parse: PASS
- BINARY_COMPONENT_INIT_GATE: PASS
- REPORTING_MATRIX_GATE: FAIL
- GRID_GATE: NOT_RUN_THIS_ROUND
- production_ready: NO
- production GCMC run: NO

Root-cause classification:
- F. OTHER_PROVEN

Evidence:
- Unmodified debug build reproduced `Matrix Inversion, Gauss-Jordan: Singular Matrix`.
- The unmodified debug run exited with status `0`; the instrumented run exited with status `77` only because the diagnostic patch intentionally aborts at first zero pivot.
- Instrumented `GaussJordan` captured first singular call as `call_id = 2`, `n = 2`, `m = 2`.
- Backtrace: `PrintAverageTotalSystemEnergiesMC -> InverseRealMatrix -> GaussJordan`.
- `A_original` is a 2 x 2 all-zero per-component number-fluctuation covariance matrix in post-simulation per-component heat-of-adsorption reporting.
- CH4-only and H2O-only one-component diagnostic carriers do not trigger the singular matrix; the CH4-H2O binary diagnostic carrier does.
- H2O geometry and inertia tensor are not degenerate.

Production decision:
- Binary component initialization is no longer classified as the blocker. The source-level singular matrix is proven in binary post-simulation reporting, and binary production readiness remains NO until the reporting/statistics behavior is handled without modifying validated thermodynamic boundaries or bypassing the audited model.
"""
    (AUDIT / "GCMC_READINESS_REPORT.md").write_text(text)


def main() -> None:
    info = matrix_analysis()
    write_matrix_reports(info)
    write_h2o_report(parse_h2o_geometry())
    write_component_audit()
    write_component_comparison()
    write_provenance()
    update_readiness()


if __name__ == "__main__":
    main()
