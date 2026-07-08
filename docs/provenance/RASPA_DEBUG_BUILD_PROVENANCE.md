# RASPA Debug Build Provenance

Installed RASPA2 binary:
- Path: `/home/baiheng/miniforge3/envs/raspa2/bin/simulate`
- SHA256: `b875b3eee608d5bef456655e13b5b8afa67cbde3370287a717c7117ab23e70a8`
- `simulate --version`: unsupported / no version output

Closest available source tree:
- Path: `/home/baiheng/RASPA2_source`
- Remote: `https://github.com/iRASPA/RASPA2.git`
- Revision: `6498ab1eec9c8e0f063dcd0d71dd7add372c529b`
- Describe: `v2.0.50`
- Recent commits: `6498ab1 Modified polarization`; `ce3ddac Polarization improvements`; `6e90ad9 bugfix weight pressure cfcmc`

Toolchain:
- GCC/G++: `gcc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0`
- GNU Make: `4.3`
- CMake: `3.22.1`
- Autoreconf: `2.71`

Unmodified diagnostic build:
- Source copy: `/home/baiheng/raspa_debug_unmodified_src`
- Install prefix: `/home/baiheng/raspa_debug_unmodified_install`
- Configure flags: `CFLAGS=-O0 -g`, `CXXFLAGS=-O0 -g`, `LDFLAGS=-rdynamic`
- Binary SHA256: `3806cafc0c8b1724bd91c93aafec08cb1a08492f827b26760aaf386bae80542e`
- Result: unmodified binary reproduced `Matrix Inversion, Gauss-Jordan: Singular Matrix`
- Reproduction evidence: `diagnostics/raspa_source_debug/unmodified/`

Instrumented diagnostic build:
- Source copy: `/home/baiheng/raspa_debug_instrumented_src`
- Install prefix: `/home/baiheng/raspa_debug_instrumented_install`
- Source patch: `diagnostics/raspa_source_debug/gaussjordan_debug.patch`
- Configure flags: `CFLAGS=-O0 -g`, `CXXFLAGS=-O0 -g`, `LDFLAGS=-rdynamic`
- Binary SHA256: `e03dd7d2edf93aabba2d95b2b8601c58c19297a9ccd38d3eb6b84f1b332c45dc`

Safety:
- The installed production executable was not overwritten.
- No production GCMC was run.
- All runs in this report are DIAGNOSTIC_ONLY one-cycle source-localization carriers.
