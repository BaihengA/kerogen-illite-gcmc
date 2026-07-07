#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared Windows<->WSL RASPA2 discovery helpers for V36."""
from __future__ import annotations

import os
import shlex
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


def decode_process_bytes(data: bytes | None) -> str:
    if not data:
        return ""
    if data.startswith((b"\xff\xfe", b"\xfe\xff")):
        try:
            return data.decode("utf-16")
        except UnicodeDecodeError:
            pass
    if data.startswith(b"\xef\xbb\xbf"):
        try:
            return data.decode("utf-8-sig")
        except UnicodeDecodeError:
            pass
    sample = data[: min(len(data), 512)]
    if len(sample) >= 8:
        ez = sum(1 for i in range(0, len(sample), 2) if sample[i] == 0)
        oz = sum(1 for i in range(1, len(sample), 2) if sample[i] == 0)
        en = max(1, (len(sample) + 1) // 2)
        on = max(1, len(sample) // 2)
        if oz / on > 0.25:
            try:
                return data.decode("utf-16-le")
            except UnicodeDecodeError:
                pass
        if ez / en > 0.25:
            try:
                return data.decode("utf-16-be")
            except UnicodeDecodeError:
                pass
    for enc in ("utf-8", "gb18030"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", errors="replace")


def run_raw(cmd: list[str], *, input_bytes: bytes | None = None, timeout: int = 60) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        input=input_bytes,
        capture_output=True,
        text=False,
        check=False,
        timeout=timeout,
    )


def run_wsl_script(distro: str, script: str, timeout: int = 90) -> tuple[int, str, str]:
    cp = run_raw(
        ["wsl.exe", "-d", distro, "--", "bash", "-s"],
        input_bytes=script.encode("utf-8"),
        timeout=timeout,
    )
    return cp.returncode, decode_process_bytes(cp.stdout), decode_process_bytes(cp.stderr)


def list_wsl_distros() -> list[str]:
    if os.name != "nt" or shutil.which("wsl.exe") is None:
        return []
    cp = run_raw(["wsl.exe", "-l", "-q"], timeout=20)
    text = decode_process_bytes(cp.stdout)
    return [x.strip().strip("\x00") for x in text.splitlines() if x.strip().strip("\x00")]


def sq(text: str) -> str:
    return "'" + text.replace("'", "'\\''") + "'"


@dataclass(frozen=True)
class WslRaspaInfo:
    distro: str
    root: str
    simulate: str
    base_ff: str
    methane_def: str | None
    tip5p_def: str | None
    stderr: str = ""


def _discovery_script(configured_root: str, ffname: str) -> str:
    cr = sq(configured_root)
    ff = sq(ffname)
    return f'''#!/usr/bin/env bash
set +u
CONFIGURED_ROOT={cr}
FFNAME={ff}
source ~/.bashrc >/dev/null 2>&1 || true

emit_if_valid() {{
  root="$1"
  [ -n "$root" ] || return 1
  root="$(readlink -f "$root" 2>/dev/null || printf '%s' "$root")"
  exe="$root/bin/simulate"
  mix="$root/share/raspa/forcefield/$FFNAME/force_field_mixing_rules.def"
  pseudo="$root/share/raspa/forcefield/$FFNAME/pseudo_atoms.def"
  if [ -x "$exe" ] && [ -f "$mix" ] && [ -f "$pseudo" ]; then
    printf 'ROOT=%s\n' "$root"
    printf 'SIMULATE=%s\n' "$exe"
    printf 'BASE_FF=%s\n' "$root/share/raspa/forcefield/$FFNAME"
    meth="$(find "$root/share/raspa/molecules" -type f -iname 'methane.def' -print -quit 2>/dev/null || true)"
    tip="$(find "$root/share/raspa" -type f \\( -iname 'Tip5p.def' -o -iname 'TIP5P.def' \\) -print -quit 2>/dev/null || true)"
    printf 'METHANE_DEF=%s\n' "${{meth:-NOT_FOUND}}"
    printf 'TIP5P_DEF=%s\n' "${{tip:-NOT_FOUND}}"
    printf 'STATUS=PASS\n'
    exit 0
  fi
  return 1
}}

emit_if_valid "$CONFIGURED_ROOT" || true
emit_if_valid "${{RASPA_DIR:-}}" || true
emit_if_valid "${{CONDA_PREFIX:-}}" || true

if command -v simulate >/dev/null 2>&1; then
  exe="$(readlink -f "$(command -v simulate)" 2>/dev/null || command -v simulate)"
  emit_if_valid "$(dirname "$(dirname "$exe")")" || true
fi

for root in \
  /home/*/miniforge3/envs/* \
  /home/*/mambaforge/envs/* \
  /home/*/miniconda3/envs/* \
  /home/*/anaconda3/envs/* \
  /opt/conda/envs/* \
  /opt/mambaforge/envs/* \
  /opt/raspa2 \
  /usr/local; do
  [ -d "$root" ] || continue
  emit_if_valid "$root" || true
done

while IFS= read -r exe; do
  [ -n "$exe" ] || continue
  root="$(dirname "$(dirname "$(readlink -f "$exe" 2>/dev/null || printf '%s' "$exe")")")"
  emit_if_valid "$root" || true
done < <(find /home /opt /usr/local -maxdepth 9 -type f -name simulate -perm -111 -print 2>/dev/null | head -n 100)

printf 'STATUS=FAIL\n'
'''


def _parse_kv(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            k = k.strip()
            if k and k.replace("_", "").isalnum():
                out[k] = v.strip()
    return out


def discover_wsl_raspa(cfg: dict, timeout: int = 120) -> WslRaspaInfo | None:
    if os.name != "nt" or shutil.which("wsl.exe") is None:
        return None
    configured_distro = str(cfg.get("wsl_distribution", "Ubuntu-22.04"))
    configured_root = str(cfg.get("raspa_wsl_dir", "/home/baiheng/miniforge3/envs/raspa2"))
    ffname = str(cfg.get("raspa_base_forcefield_name", "ExampleZeolitesForceField"))
    order: list[str] = []
    for d in [configured_distro, *list_wsl_distros()]:
        if d and d not in order:
            order.append(d)
    script = _discovery_script(configured_root, ffname)
    for distro in order:
        try:
            rc, stdout, stderr = run_wsl_script(distro, script, timeout=timeout)
        except Exception:
            continue
        kv = _parse_kv(stdout)
        if rc == 0 and kv.get("STATUS") == "PASS" and kv.get("ROOT") and kv.get("SIMULATE") and kv.get("BASE_FF"):
            return WslRaspaInfo(
                distro=distro,
                root=kv["ROOT"],
                simulate=kv["SIMULATE"],
                base_ff=kv["BASE_FF"],
                methane_def=None if kv.get("METHANE_DEF") in (None, "NOT_FOUND", "") else kv.get("METHANE_DEF"),
                tip5p_def=None if kv.get("TIP5P_DEF") in (None, "NOT_FOUND", "") else kv.get("TIP5P_DEF"),
                stderr=stderr,
            )
    return None


def wsl_cat(distro: str, linux_path: str, timeout: int = 30) -> bytes | None:
    try:
        cp = run_raw(["wsl.exe", "-d", distro, "--", "cat", linux_path], timeout=timeout)
    except Exception:
        return None
    if cp.returncode != 0:
        return None
    return bytes(cp.stdout or b"")


def cache_wsl_raspa_assets(cfg: dict, project_root: Path) -> tuple[Path, Path | None, WslRaspaInfo] | None:
    """Cache minimal RASPA files from WSL into the Windows project.

    Returns (base_forcefield_dir, local_tip5p_def_or_none, discovery_info).
    This avoids relying on \\wsl$ / \\wsl.localhost UNC access.
    """
    info = discover_wsl_raspa(cfg)
    if info is None:
        return None
    cache_rel = str(cfg.get("raspa_asset_cache_dir", "00_INPUT/RASPA2_AUTO_CACHE_V36"))
    cache = Path(cache_rel)
    if not cache.is_absolute():
        cache = project_root / cache
    ffname = str(cfg.get("raspa_base_forcefield_name", "ExampleZeolitesForceField"))
    base = cache / "forcefield" / ffname
    base.mkdir(parents=True, exist_ok=True)

    required = ["force_field_mixing_rules.def", "pseudo_atoms.def"]
    optional = ["force_field.def"]
    for name in [*required, *optional]:
        data = wsl_cat(info.distro, f"{info.base_ff}/{name}")
        if data is not None:
            (base / name).write_bytes(data)
    if any(not (base / x).exists() for x in required):
        return None

    tip_local: Path | None = None
    if info.tip5p_def:
        data = wsl_cat(info.distro, info.tip5p_def)
        if data is not None:
            tip_local = cache / "molecules" / "Tip5p.def"
            tip_local.parent.mkdir(parents=True, exist_ok=True)
            tip_local.write_bytes(data)

        # When water definition has sibling local FF files, cache them too.
        parent = info.tip5p_def.rsplit("/", 1)[0]
        for name in ("force_field_mixing_rules.def", "pseudo_atoms.def"):
            data = wsl_cat(info.distro, f"{parent}/{name}")
            if data is not None:
                (tip_local.parent / name).write_bytes(data)  # type: ignore[union-attr]

    meta = cache / "WSL_RASPA_DISCOVERY.txt"
    meta.write_text(
        "\n".join([
            f"distro={info.distro}",
            f"root={info.root}",
            f"simulate={info.simulate}",
            f"base_ff={info.base_ff}",
            f"methane_def={info.methane_def or 'NOT_FOUND'}",
            f"tip5p_def={info.tip5p_def or 'NOT_FOUND'}",
        ]) + "\n",
        encoding="utf-8",
    )
    return base, tip_local, info
