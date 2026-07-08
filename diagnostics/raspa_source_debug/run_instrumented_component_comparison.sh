#!/usr/bin/env bash
set -euo pipefail

REPO=/mnt/f/MD/kerogen_bulk0p1_to0p8_then_graphene_pull_v1/kerogen_bulk0p1_to0p8_then_graphene_pull_v1/KEROGEN_MD_GCMC_CODEBASE
SRC="${REPO}/diagnostics/molecule_definition/CH4_H2O_BINARY_PARSE_TEST"
INST=/home/baiheng/raspa_debug_instrumented_install
RUN_ROOT=/home/baiheng/raspa_debug_runs/instrumented_component_comparison
OUT_ROOT="${REPO}/diagnostics/raspa_source_debug/component_comparison"
FRAMEWORK=CH4_H2O_BINARY_PARSE_TEST_framework

rm -rf "${RUN_ROOT}" "${OUT_ROOT}"
mkdir -p "${RUN_ROOT}" "${OUT_ROOT}" "${INST}/share/raspa/structures/cif"
cp "${SRC}/${FRAMEWORK}.cif" "${INST}/share/raspa/structures/cif/"

write_common_files() {
  local run_dir=$1
  mkdir -p "${run_dir}"
  cp "${SRC}/force_field.def" \
     "${SRC}/force_field_mixing_rules.def" \
     "${SRC}/pseudo_atoms.def" \
     "${SRC}/H2O.def" \
     "${SRC}/${FRAMEWORK}.cif" \
     "${run_dir}/"
}

write_header() {
  local input=$1
  cat > "${input}" <<EOF_INPUT
# DIAGNOSTIC_ONLY source-level GaussJordan localization; not adsorption
SimulationType MonteCarlo
NumberOfCycles 1
NumberOfInitializationCycles 1
PrintEvery 1

Forcefield Local
RemoveAtomNumberCodeFromLabel yes
UseChargesFromCIFFile yes
ChargeMethod Ewald
CutOff 12.0

Framework 0
FrameworkName ${FRAMEWORK}
UnitCells 1 1 1

ExternalTemperature 353.15
ExternalPressure 20000000

EOF_INPUT
}

append_ch4() {
  local input=$1
  local index=$2
  local mol_fraction=$3
  cat >> "${input}" <<EOF_INPUT
Component ${index} MoleculeName methane
 MoleculeDefinition ExampleDefinitions
 MolFraction ${mol_fraction}
 FugacityCoefficient 0.8439459552
 TranslationProbability 0.5
 ReinsertionProbability 0.5
 SwapProbability 1.0
 CreateNumberOfMolecules 0

EOF_INPUT
}

append_h2o() {
  local input=$1
  local index=$2
  local mol_fraction=$3
  cat >> "${input}" <<EOF_INPUT
Component ${index} MoleculeName H2O
 MoleculeDefinition Local
 MolFraction ${mol_fraction}
 FugacityCoefficient 1.1266978304747
 TranslationProbability 0.5
 RotationProbability 0.5
 ReinsertionProbability 0.5
 SwapProbability 1.0
 CreateNumberOfMolecules 0

EOF_INPUT
}

run_case() {
  local case_name=$1
  local run_dir="${RUN_ROOT}/${case_name}"
  local out_dir="${OUT_ROOT}/${case_name}"
  write_common_files "${run_dir}"
  mkdir -p "${out_dir}/gaussjordan"
  write_header "${run_dir}/simulation.input"
  if [[ "${case_name}" == "CH4_ONLY" ]]; then
    append_ch4 "${run_dir}/simulation.input" 0 1.0
  elif [[ "${case_name}" == "H2O_ONLY" ]]; then
    append_h2o "${run_dir}/simulation.input" 0 1.0
  else
    append_ch4 "${run_dir}/simulation.input" 0 0.997636645934322
    append_h2o "${run_dir}/simulation.input" 1 0.0023633540656784
  fi

  cd "${run_dir}"
  set +e
  RASPA_GJ_DEBUG_DIR="${out_dir}/gaussjordan" RASPA_DIR="${INST}" "${INST}/bin/simulate" > "${out_dir}/stdout.txt" 2> "${out_dir}/stderr.txt"
  status=$?
  set -e
  printf 'exit_status=%s\n' "${status}" > "${out_dir}/status.txt"
}

run_case CH4_ONLY
run_case H2O_ONLY
run_case CH4_H2O_BINARY

for case_name in CH4_ONLY H2O_ONLY CH4_H2O_BINARY; do
  echo "== ${case_name} =="
  cat "${OUT_ROOT}/${case_name}/status.txt"
  find "${OUT_ROOT}/${case_name}/gaussjordan" -maxdepth 2 -type f | sort
  tail -5 "${OUT_ROOT}/${case_name}/stderr.txt" || true
done
