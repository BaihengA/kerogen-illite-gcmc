from __future__ import annotations

import csv
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

R_KJ_MOL_K = 0.00831446261815324


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def strip_comment(line: str) -> str:
    return line.split(";", 1)[0].strip()


def iter_sections(path: Path):
    section = None
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = strip_comment(raw)
        if not line:
            continue
        match = re.match(r"^\[\s*([^\]]+)\s*\]$", line)
        if match:
            section = match.group(1).strip().lower()
            continue
        yield section, line


@dataclass(frozen=True)
class TopAtom:
    index: int
    atomtype: str
    atomname: str
    charge: float
    mass: float


@dataclass(frozen=True)
class AtomType:
    mass: float
    sigma_nm: float
    epsilon_kj_mol: float
    source_file: str


@dataclass(frozen=True)
class PdbAtom:
    atomname: str
    x_A: float
    y_A: float
    z_A: float


def parse_top_atoms(path: Path) -> dict[str, TopAtom]:
    atoms: dict[str, TopAtom] = {}
    for section, line in iter_sections(path):
        if section != "atoms":
            continue
        tok = line.split()
        if len(tok) < 7:
            continue
        mass = float(tok[7]) if len(tok) >= 8 else 0.0
        atom = TopAtom(int(tok[0]), tok[1], tok[4], float(tok[6]), mass)
        atoms[atom.atomname] = atom
    return atoms


def parse_atomtypes(paths: Iterable[Path]) -> dict[str, AtomType]:
    out: dict[str, AtomType] = {}
    for path in paths:
        for section, line in iter_sections(path):
            if section != "atomtypes":
                continue
            tok = line.split()
            if len(tok) < 6:
                continue
            try:
                out[tok[0]] = AtomType(float(tok[1]), float(tok[-2]), float(tok[-1]), str(path))
            except ValueError:
                continue
    return out


def parse_pdb_atoms(path: Path) -> list[PdbAtom]:
    atoms: list[PdbAtom] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if raw[:6].strip().upper() not in {"ATOM", "HETATM"}:
            continue
        atoms.append(PdbAtom(raw[12:16].strip(), float(raw[30:38]), float(raw[38:46]), float(raw[46:54])))
    return atoms


def parse_cif_types(path: Path) -> set[str]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    out: set[str] = set()
    in_loop = False
    headers: list[str] = []
    type_idx = None
    for raw in lines:
        line = raw.strip()
        if line == "loop_":
            in_loop = True
            headers = []
            type_idx = None
            continue
        if in_loop and line.startswith("_atom_site_"):
            headers.append(line)
            if line == "_atom_site_type_symbol":
                type_idx = len(headers) - 1
            continue
        if in_loop and headers and line and not line.startswith("_"):
            if type_idx is None:
                continue
            tok = line.split()
            if len(tok) > type_idx:
                out.add(tok[type_idx])
    return out


def element_from_name(name: str) -> str:
    raw = name.split("_", 1)[-1]
    letters = re.sub(r"[^A-Za-z]", "", raw)
    if not letters:
        return "X"
    if len(letters) >= 2 and letters[:2].lower() in {"si", "al"}:
        return letters[:2].title()
    return letters[0].upper()


def mixing_line(raspa_type: str, sigma_nm: float, epsilon_kj_mol: float) -> str:
    epsilon_K = epsilon_kj_mol / R_KJ_MOL_K
    sigma_A = sigma_nm * 10.0
    if sigma_A == 0.0 and epsilon_K == 0.0:
        return f"{raspa_type} none"
    return f"{raspa_type} lennard-jones {epsilon_K:.12g} {sigma_A:.12g}"


def pseudo_line(raspa_type: str, element: str, mass: float, charge: float) -> str:
    return f"{raspa_type} yes {element} {element} 0 {mass:.8g} {charge:.12g} 0.0 1.0 1.0 0 0 relative 0"


def read_base_ch4_entries(raspa_root: str) -> tuple[str, str, dict]:
    base = Path(raspa_root)
    mix = base / "share" / "raspa" / "forcefield" / "ExampleZeolitesForceField" / "force_field_mixing_rules.def"
    pseudo = base / "share" / "raspa" / "forcefield" / "ExampleZeolitesForceField" / "pseudo_atoms.def"
    mix_line = ""
    for line in mix.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.split()[:1] == ["CH4"]:
            mix_line = line.strip()
            break
    pseudo_line_value = ""
    for line in pseudo.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.split()[:1] == ["CH4"]:
            pseudo_line_value = line.strip()
            break
    if not mix_line or not pseudo_line_value:
        raise RuntimeError("Could not resolve CH4 base forcefield entries from RASPA ExampleZeolitesForceField")
    source = {"mixing_rules": str(mix), "mixing_rules_sha256": sha256_file(mix), "pseudo_atoms": str(pseudo), "pseudo_atoms_sha256": sha256_file(pseudo)}
    return mix_line, pseudo_line_value, source


def load_water_lj(path: Path) -> dict[str, AtomType]:
    out: dict[str, AtomType] = {}
    with path.open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            out[row["gromacs_atom_type"]] = AtomType(
                float(row["mass"]),
                float(row["sigma_nm"]),
                float(row["epsilon_kJ_mol"]),
                row["lj_source_file"],
            )
    return out
