# RASPA Failure Evolution

status: PASS

| stage | input SHA | exit code | timeout | last stdout line | status |
|---|---:|---:|---:|---|---|
| pre-Framework-0 historical smoke | previous input, before current freeze | 139 | NO | not retained in current canonical stdout | historical FAIL_SEGFAULT |
| current 300 s canonical smoke | 05e218c06a535573ecaf0fbe5c14b1a5c2e2d62a0c7ce81d78bf9384b067b484 | None | 300 s | `End reading cif-file` | FAIL_TIMEOUT, ACTIVE_COMPUTE |
| current 900 s EXTENDED_SMOKE_ONLY | 05e218c06a535573ecaf0fbe5c14b1a5c2e2d62a0c7ce81d78bf9384b067b484 | None | 900 s | `End reading cif-file` | FAIL_TIMEOUT |

The historical exit 139 is not mixed with the current result. With the current `Framework 0` input and frozen assets, the observed failure mode is timeout, not a reproduced segfault.
