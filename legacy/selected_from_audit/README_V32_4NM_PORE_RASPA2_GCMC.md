# V32 — 4 nm mirrored composite pore + RASPA2 CH4/H2O GCMC

## What this package does

1. Reads the **exact final kerogen+illite wall** built previously by V31:

   `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/{case}_EXACT_kerogen_plus_illite.gro`

2. Verifies that the first kerogen atom block matches the exact RAW final kerogen:

   `KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro`

3. Keeps the lower composite wall internal geometry unchanged. The whole lower wall may receive one rigid translation only when `tight_xy_box=true`; no deformation, rotation, wrapping, clipping, or re-equilibration is performed.

4. Creates the upper wall by exact z-mirroring of the complete lower composite wall. Therefore the upper wall has illite outside and rough kerogen facing downward.

5. Builds a nominal **4.0 nm slit pore**. Default definition:

   `pore_width_definition = mean_surface_plane`

   The 4 nm distance is between mean rough-surface planes obtained from a 2D grid of kerogen top-surface maxima. The report also gives minimum, P05, mean, P95, and maximum local gaps.

6. Converts the 4 nm pore to a RASPA-ready CIF after mapping wall atoms to GROMACS topology atom types, charges, sigma, and epsilon.

7. Prepares binary CH4/H2O GCMC and collects equilibrium molecule counts.

---

## Important thermodynamic point

Temperature and total pressure alone do **not** uniquely define a binary CH4/H2O reservoir. A composition or component fugacity is also needed.

Default V32 assumption:

- Temperature: `353.15 K`
- Total pressure: `20 MPa`
- Mixture mode: `water_saturated_methane`
- Water activity: `1.0`

The script estimates water vapor saturation pressure with an Antoine relation in its valid 1–100 °C interval, then sets:

`y_H2O = p_sat(T) / P_total`

`y_CH4 = 1 - y_H2O`

This is a **water-saturated gas-reservoir assumption**, not a universal shale-reservoir composition. Edit the JSON if your experimental reservoir pressure, water activity, or gas composition is known.

To use a fixed water fraction:

```json
"mixture_mode": "fixed_water_mole_fraction",
"fixed_water_mole_fraction": 0.01
```

---

## Required files

### Existing composite wall

For each case, V31 output is expected:

- `ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/RMS_0p000/RMS_0p000_EXACT_kerogen_plus_illite.gro`
- `.../RMS_0p300/...`
- `.../RMS_0p600/...`
- `.../RMS_0p900/...`

### Exact RAW final kerogen

- `KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/RMS_0p000_kerogen_only_raw_from_final.gro`
- same for 0p300/0p600/0p900

### GROMACS force field

At minimum:

- `00_INPUT/kero.itp`
- kerogen atom-type parameters such as `kero_ATP.itp`
- an illite `.itp` containing `[ atoms ]`
- illite atom-type parameters containing `[ atomtypes ]`

The preparation script **stops** if sigma/epsilon cannot be found. It does not invent wall parameters.

### RASPA2

Set either:

- environment variable `RASPA_DIR`
- config `raspa_dir`

The script needs a base RASPA forcefield folder containing methane parameters. Default name:

`ExampleZeolitesForceField`

For water, the script searches for `Tip5p.def` in:

- `00_INPUT/Tip5p.def`
- `00_INPUT/RASPA2_LOCAL/Tip5p.def`
- the configured RASPA2 tree

If it cannot find `Tip5p.def`, the water/binary run is not launched.

---

## Run order

### Step 1 — Build 4 nm pores

`43_BUILD_4NM_COMPOSITE_PORES.bat`

Outputs:

`COMPOSITE_PORES_4NM_V32/{case}/{case}_COMPOSITE_PORE_4nm.gro`

Check:

`{case}_pore_build_report.csv`

Key metrics:

- `pore_width_target_nm`
- `grid_gap_min_nm`
- `grid_gap_mean_nm`
- `grid_gap_max_nm`
- `lower_wall_nonrigid_change_nm` — must be 0

### Step 2 — Prepare RASPA2 GCMC

`44_PREPARE_RASPA2_GCMC.bat`

Outputs:

`RASPA2_GCMC_4NM_V32/{case}/T..._P.../simulation.input`

and local force-field files.

The typed CIF contains per-atom charges from the GROMACS topology and LJ types mapped from `[ atomtypes ]`.

### Step 3 — Run RASPA2

`45_RUN_RASPA2_GCMC.bat`

The runner installs each custom CIF into:

`$RASPA_DIR/share/raspa/structures/cif`

then runs `simulate` in each case directory.

### Step 4 — Collect molecule counts

`46_COLLECT_GCMC_COUNTS.bat`

Final table:

`RASPA2_GCMC_4NM_V32/GCMC_CH4_H2O_MOLECULE_COUNTS.csv`

Columns include:

- `CH4_mean_molecules`
- `H2O_mean_molecules`
- `temperature_K`
- `total_pressure_MPa`
- `methane_mole_fraction`
- `water_mole_fraction`

---

## Pressure scan

Change:

```json
"pressure_MPa": [10.0, 20.0, 30.0]
```

The code creates one independent GCMC case per pressure.

---

## Quick screening before production

For a short test, temporarily change:

```json
"number_of_initialization_cycles": 5000,
"number_of_cycles": 10000
```

For final data, restore longer production values and check convergence of loading versus cycle block.

---

## Scientific caution

The geometry builder is deterministic, but GCMC molecule counts depend strongly on:

- kerogen and illite LJ/charge parameters;
- CH4 and H2O molecular models;
- binary reservoir composition/fugacity;
- 4 nm pore-width definition for rough surfaces;
- Monte Carlo convergence.

Do not interpret a number as final until the force-field mapping report is complete and the loading time series is converged.
