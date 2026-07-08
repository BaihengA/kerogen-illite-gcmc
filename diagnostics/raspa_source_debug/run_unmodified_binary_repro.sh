#!/usr/bin/env bash
set -euo pipefail

REPO=/mnt/f/MD/kerogen_bulk0p1_to0p8_then_graphene_pull_v1/kerogen_bulk0p1_to0p8_then_graphene_pull_v1/KEROGEN_MD_GCMC_CODEBASE
SRC="${REPO}/diagnostics/molecule_definition/CH4_H2O_BINARY_PARSE_TEST"
RUN=/home/baiheng/raspa_debug_runs/unmodified/CH4_H2O_BINARY
INST=/home/baiheng/raspa_debug_unmodified_install
OUT="${REPO}/diagnostics/raspa_source_debug/unmodified"

rm -rf /home/baiheng/raspa_debug_runs/unmodified
mkdir -p "${RUN}" "${INST}/share/raspa/structures/cif" "${OUT}"

cp "${SRC}/simulation.input" \
   "${SRC}/force_field.def" \
   "${SRC}/force_field_mixing_rules.def" \
   "${SRC}/pseudo_atoms.def" \
   "${SRC}/H2O.def" \
   "${RUN}/"
cp "${SRC}/CH4_H2O_BINARY_PARSE_TEST_framework.cif" "${RUN}/"
cp "${SRC}/CH4_H2O_BINARY_PARSE_TEST_framework.cif" "${INST}/share/raspa/structures/cif/"

cd "${RUN}"
set +e
RASPA_DIR="${INST}" "${INST}/bin/simulate" > "${OUT}/stdout.txt" 2> "${OUT}/stderr.txt"
status=$?
set -e

printf 'exit_status=%s\n' "${status}" > "${OUT}/status.txt"
printf 'stderr_tail:\n'
tail -40 "${OUT}/stderr.txt" || true
printf '\nstdout_tail:\n'
tail -40 "${OUT}/stdout.txt" || true
