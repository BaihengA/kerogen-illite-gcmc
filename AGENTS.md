# AGENTS.md

1. Never modify original coordinates in `RAW_KEEP_COORDINATES`.
2. Never overwrite final `GRO`/`PDB` files.
3. Every new workflow must record inputs and outputs.
4. Every parameter change must enter `CHANGELOG.md`.
5. GCMC must not infer binary mixture chemical potentials from T/P alone.
6. Water models must prefer user-provided `00_INPUT` PDB/ITP files.
7. Never fabricate simulation results.
8. Production simulation requires preflight.
9. Preserve complete logs on failure.
10. No silent fallback to other models.
11. Do not automatically delete `legacy`.
12. Every coordinate transform must generate a validation report.
