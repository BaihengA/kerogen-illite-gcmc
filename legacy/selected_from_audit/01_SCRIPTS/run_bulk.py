
from pathlib import Path
import csv
import json
import math
import shutil

from common import (
    copy_local_itps,
    density_g_cm3,
    fail,
    load_config,
    read_gro,
    run_command,
)

ROOT = Path(__file__).resolve().parents[1]


def em_mdp() -> str:
    return """integrator = steep
emtol = 1000
emstep = 0.001
nsteps = 100000
cutoff-scheme = Verlet
nstlist = 20
rlist = 1.2
coulombtype = PME
rcoulomb = 1.2
vdwtype = Cut-off
rvdw = 1.2
DispCorr = EnerPres
pbc = xyz
"""


def md_base(
    temperature: float,
    time_ps: float,
    dt_ps: float,
    continuation: bool,
    gen_vel: bool,
) -> str:
    nsteps = round(time_ps / dt_ps)
    return f"""integrator = md
dt = {dt_ps:.6f}
nsteps = {nsteps}
continuation = {'yes' if continuation else 'no'}
gen-vel = {'yes' if gen_vel else 'no'}
gen-temp = {temperature:.3f}
gen-seed = -1

constraints = h-bonds
constraint-algorithm = lincs
lincs-order = 4
lincs-iter = 2

cutoff-scheme = Verlet
nstlist = 20
rlist = 1.2
coulombtype = PME
rcoulomb = 1.2
vdwtype = Cut-off
rvdw = 1.2
DispCorr = EnerPres

tcoupl = V-rescale
tc-grps = KERO
tau-t = 1.0
ref-t = {temperature:.3f}

pbc = xyz
comm-mode = Linear
nstcomm = 100

nstlog = 500
nstenergy = 500
nstxout-compressed = 1000
compressed-x-precision = 1000
"""


def nvt_mdp(
    temperature: float,
    time_ps: float,
    dt_ps: float,
    continuation: bool,
    gen_vel: bool,
) -> str:
    return (
        md_base(temperature, time_ps, dt_ps, continuation, gen_vel)
        + "\npcoupl = no\n"
    )


def npt_mdp(
    temperature: float,
    time_ps: float,
    dt_ps: float,
    pressure_mpa: float,
    tau_p: float,
    compressibility: float,
) -> str:
    pressure_bar = pressure_mpa * 10.0
    return (
        md_base(temperature, time_ps, dt_ps, True, False)
        + f"""
pcoupl = Berendsen
pcoupltype = isotropic
tau-p = {tau_p:.3f}
ref-p = {pressure_bar:.6f}
compressibility = {compressibility:.8g}
refcoord-scaling = com
"""
    )


def pressure_for_density(rho: float) -> float:
    if rho < 0.20:
        return 100.0
    if rho < 0.35:
        return 60.0
    if rho < 0.50:
        return 40.0
    if rho < 0.62:
        return 25.0
    if rho < 0.70:
        return 15.0
    if rho < 0.75:
        return 10.0
    if rho < 0.78:
        return 5.0
    return 2.0


def execute(
    cfg: dict,
    work: Path,
    mdp: Path,
    input_gro: Path,
    name: str,
    checkpoint: Path | None,
) -> tuple[Path, Path | None]:
    gmx = cfg["gromacs_exe"]
    output_gro = work / f"{name}.gro"
    output_cpt = work / f"{name}.cpt"
    output_tpr = work / f"{name}.tpr"

    if output_gro.exists():
        print("SKIP COMPLETED:", output_gro.name)
        return output_gro, output_cpt if output_cpt.exists() else None

    if output_cpt.exists() and output_tpr.exists():
        run_command(
            [
                gmx,
                "mdrun",
                "-deffnm",
                name,
                "-cpi",
                output_cpt.name,
                "-append",
                "-cpt",
                "5",
                "-ntmpi",
                "1",
                "-ntomp",
                str(cfg["omp_threads"]),
                "-pin",
                str(cfg["pinning"]),
            ],
            work,
            work / f"{name}_resume.log",
        )
        if not output_gro.exists():
            fail(f"Resume did not create {output_gro}")
        return output_gro, output_cpt

    command = [
        gmx,
        "grompp",
        "-f",
        str(mdp),
        "-c",
        str(input_gro),
        "-r",
        str(input_gro),
        "-p",
        "topol.top",
        "-n",
        "index.ndx",
        "-o",
        output_tpr.name,
        "-maxwarn",
        str(cfg["maxwarn"]),
    ]
    if checkpoint is not None and checkpoint.exists():
        command += ["-t", str(checkpoint)]

    run_command(command, work, work / f"{name}_grompp.log")
    run_command(
        [
            gmx,
            "mdrun",
            "-deffnm",
            name,
            "-cpt",
            "5",
            "-ntmpi",
            "1",
            "-ntomp",
            str(cfg["omp_threads"]),
            "-pin",
            str(cfg["pinning"]),
        ],
        work,
        work / f"{name}_mdrun.log",
    )

    if not output_gro.exists():
        fail(f"Expected output not generated: {output_gro}")
    return output_gro, output_cpt if output_cpt.exists() else None


def append_summary(
    path: Path,
    label: str,
    gro: Path,
    total_mass_amu: float,
    pressure_mpa: float | None,
) -> float:
    _, _, box = read_gro(gro)
    density = density_g_cm3(total_mass_amu, box)
    exists = path.exists()
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if not exists:
            writer.writerow(
                [
                    "label",
                    "density_g_cm3",
                    "box_x_nm",
                    "box_y_nm",
                    "box_z_nm",
                    "pressure_target_MPa",
                ]
            )
        writer.writerow(
            [
                label,
                density,
                box[0],
                box[1],
                box[2],
                "" if pressure_mpa is None else pressure_mpa,
            ]
        )
    return density


def main() -> None:
    cfg = load_config(ROOT)
    bulk_dir = ROOT / "01_BULK"
    initial = bulk_dir / "01_INITIAL"
    mdp_dir = bulk_dir / "02_MDP"
    work = bulk_dir / "03_RUN"
    mdp_dir.mkdir(parents=True, exist_ok=True)
    work.mkdir(parents=True, exist_ok=True)

    for file in initial.iterdir():
        if file.is_file():
            shutil.copy2(file, work / file.name)

    build_report = json.loads(
        (bulk_dir / "BULK_BUILD_REPORT.json").read_text(encoding="utf-8")
    )
    total_mass_amu = float(build_report["total_mass_amu"])

    current = work / "bulk_initial_0p1.gro"
    checkpoint = None
    summary = work / "BULK_DENSITY_SUMMARY.csv"

    (mdp_dir / "00_em.mdp").write_text(em_mdp(), encoding="ascii")
    current, checkpoint = execute(
        cfg, work, mdp_dir / "00_em.mdp", current, "00_em", checkpoint
    )
    append_summary(summary, "em", current, total_mass_amu, None)

    for index, stage in enumerate(cfg["bulk_nvt_schedule"], start=1):
        mdp = mdp_dir / (
            f"01_nvt_{index:02d}_{int(stage['temperature_K'])}K.mdp"
        )
        mdp.write_text(
            nvt_mdp(
                float(stage["temperature_K"]),
                float(stage["time_ps"]),
                float(stage["dt_ps"]),
                continuation=index > 1,
                gen_vel=index == 1,
            ),
            encoding="ascii",
        )
        current, checkpoint = execute(
            cfg,
            work,
            mdp,
            current,
            f"01_nvt_{index:02d}_{int(stage['temperature_K'])}K",
            checkpoint,
        )
        append_summary(
            summary,
            f"nvt_{int(stage['temperature_K'])}K",
            current,
            total_mass_amu,
            None,
        )

    target_stop = float(cfg["target_density_stop_g_cm3"])
    max_density = float(cfg["maximum_density_g_cm3"])
    max_chunks = int(cfg["bulk_compression_max_chunks"])
    previous_density = append_summary(
        summary,
        "compression_start",
        current,
        total_mass_amu,
        None,
    )
    stalled_count = 0

    for chunk in range(1, max_chunks + 1):
        if previous_density >= target_stop:
            break

        pressure = pressure_for_density(previous_density)
        if stalled_count >= 2:
            pressure = min(200.0, pressure * 1.5)

        mdp = mdp_dir / f"02_npt_compress_{chunk:03d}_{pressure:g}MPa.mdp"
        mdp.write_text(
            npt_mdp(
                float(cfg["bulk_compression_temperature_K"]),
                float(cfg["bulk_compression_chunk_ps"]),
                float(cfg["bulk_compression_dt_ps"]),
                pressure,
                float(cfg["bulk_compression_tau_p_ps"]),
                float(cfg["bulk_compressibility_bar_inv"]),
            ),
            encoding="ascii",
        )

        current, checkpoint = execute(
            cfg,
            work,
            mdp,
            current,
            f"02_npt_compress_{chunk:03d}_{pressure:g}MPa",
            checkpoint,
        )
        new_density = append_summary(
            summary,
            f"npt_{chunk:03d}",
            current,
            total_mass_amu,
            pressure,
        )

        _, _, box = read_gro(current)
        if min(box[:3]) < float(cfg["safety"]["minimum_box_length_nm"]):
            fail(f"Safety stop: box became too small: {box[:3]}")
        if new_density > max_density:
            fail(
                f"Safety stop: density overshot to {new_density:.4f} g/cm3."
            )

        if new_density - previous_density < 0.003:
            stalled_count += 1
        else:
            stalled_count = 0
        previous_density = new_density

    if previous_density < target_stop:
        fail(
            f"Target density was not reached after {max_chunks} chunks. "
            f"Current density: {previous_density:.4f} g/cm3"
        )

    lock_mdp = mdp_dir / "03_nvt_lock_900K.mdp"
    lock_mdp.write_text(
        nvt_mdp(
            float(cfg["bulk_compression_temperature_K"]),
            float(cfg["bulk_final_lock_nvt_ps"]),
            0.001,
            continuation=True,
            gen_vel=False,
        ),
        encoding="ascii",
    )
    current, checkpoint = execute(
        cfg,
        work,
        lock_mdp,
        current,
        "03_nvt_lock_900K",
        checkpoint,
    )
    final_density = append_summary(
        summary,
        "bulk_final",
        current,
        total_mass_amu,
        None,
    )

    final = work / "bulk_density_0p8_final.gro"
    shutil.copy2(current, final)

    report = {
        "final_gro": str(final),
        "final_density_g_cm3": final_density,
        "target_density_g_cm3": cfg["target_bulk_density_g_cm3"],
        "compression_chunks_completed": chunk,
        "summary_csv": str(summary),
    }
    (bulk_dir / "BULK_DENSIFICATION_REPORT.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print("BULK DENSIFICATION COMPLETED.")


if __name__ == "__main__":
    main()
