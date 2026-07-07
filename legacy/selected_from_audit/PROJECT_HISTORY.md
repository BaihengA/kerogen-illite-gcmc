# Project history snapshot

This repository starts from a longer local development chain. The current reproducible baseline is:

```text
final RAW kerogen-only plates
  -> V31 thicker illite below exact RAW kerogen
  -> V33 mirrored 8 nm composite pore
  -> RASPA2 CH4/H2O GCMC
  -> equilibrium molecule-count collection
```

Current exact RAW kerogen inputs:

```text
KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/
RMS_0p000_kerogen_only_raw_from_final.gro
RMS_0p300_kerogen_only_raw_from_final.gro
RMS_0p600_kerogen_only_raw_from_final.gro
RMS_0p900_kerogen_only_raw_from_final.gro
```

Current composite-wall inputs:

```text
ILLITE_BELOW_RAW_FINAL_KEROGEN_V31_THICKER_SAFE/{case}/
{case}_EXACT_kerogen_plus_illite.gro
```
