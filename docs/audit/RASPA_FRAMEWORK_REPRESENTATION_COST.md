# RASPA Framework Representation Cost

status: ANALYSIS_ONLY

The current 19 MB CIF writes the full explicit framework into RASPA as fixed framework atoms.

- N_framework_atoms: 276864
- unique framework atom types: 521
- charged framework entries parsed from CIF: 276864
- rough pair-interaction type/atom scale indicator: 144246144
- electrostatic/Ewald charge bookkeeping scale indicator: 276864

The 300 s profile shows sustained CPU use while the latest printed RASPA line remains `End reading cif-file`. This suggests startup work after CIF parsing is computationally active for the large explicit framework. This document is an analysis report only; no atoms were deleted, no cutoff was changed, and electrostatics were not disabled.
