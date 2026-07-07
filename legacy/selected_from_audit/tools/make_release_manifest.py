#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "RELEASE_MANIFEST_SHA256.json"
SKIP_DIRS = {
    ".git", "__pycache__", ".venv", "venv",
    "COMPOSITE_PORES_8NM_V33", "RASPA2_GCMC_8NM_V33",
    "00_INPUT", "KEROGEN_ONLY_FINALS",
    "ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE",
}
SKIP_FILES = {OUT.name}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    entries = []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        if rel.name in SKIP_FILES or any(part in SKIP_DIRS for part in rel.parts):
            continue
        entries.append({"path": rel.as_posix(), "sha256": sha256(p), "bytes": p.stat().st_size})
    OUT.write_text(json.dumps({"files": entries}, indent=2), encoding="utf-8")
    print(f"Wrote {OUT} with {len(entries)} files")


if __name__ == "__main__":
    main()
