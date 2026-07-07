# RASPA Hotspot Report

status: SYMBOL_HOTSPOTS_UNAVAILABLE

perf_status: PERF_NOT_AVAILABLE
fallback_used: strace -c, thread CPU sampling, /proc/PID/task/*/stack attempt

## Top CPU Hotspots

Symbol-level top CPU hotspots are not available because `perf` is not installed and `gdb` is not installed. `/proc/PID/task/*/stack` was denied by kernel permissions.

| rank | symbol | shared_object | percent_cpu | probable_stage | confidence | notes |
|---:|---|---|---:|---|---|---|
| 1 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 2 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 3 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 4 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 5 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 6 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 7 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 8 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 9 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 10 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 11 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 12 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 13 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 14 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 15 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 16 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 17 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 18 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 19 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 20 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 21 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 22 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 23 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 24 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 25 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 26 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 27 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 28 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 29 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |
| 30 | UNAVAILABLE | UNAVAILABLE |  | UNKNOWN | high | perf/gdb unavailable; no symbol sample collected |

## Fallback Evidence

```text
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ------------------
 99.52   10.870096      339690        32        31 futex
  0.17    0.018094           3      4696           read
  0.10    0.011130         337        33           set_robust_list
  0.08    0.009008           1      6033           mremap
  0.06    0.006279         202        31           clone3
  0.01    0.001517          16        94           rt_sigprocmask
  0.01    0.001435          29        48           mprotect
  0.01    0.001264          14        86        55 openat
  0.01    0.001164           8       133           mmap
  0.00    0.000537           7        70        36 newfstatat
  0.00    0.000441          13        33           rseq
  0.00    0.000334          10        32           mbind
  0.00    0.000268           8        31           close
  0.00    0.000159          19         8           write
  0.00    0.000048          16         3           fstat
  0.00    0.000033           4         8           pread64
  0.00    0.000031           7         4           munmap
  0.00    0.000030          15         2           set_tid_address
  0.00    0.000029          29         1           readlink
  0.00    0.000025          12         2           getdents64
  0.00    0.000023           2        10           brk
  0.00    0.000012          12         1           sched_getaffinity
  0.00    0.000011           5         2         2 access
  0.00    0.000009           4         2           getrandom
  0.00    0.000008           8         1           rt_sigaction
  0.00    0.000008           2         4         2 arch_prctl
  0.00    0.000008           4         2           prlimit64
  0.00    0.000000           0         2           lseek
  0.00    0.000000           0         2           execve
------ ----------- ----------- --------- --------- ------------------
100.00   10.922001         957     11406       126 total
```

## Stage Classification

- framework read: observed
- after framework read: observed for full framework as active compute/timeout
- forcefield/potential shift: observed only in 10k/25k diagnostic subsets
- component initialization: reached in 10k/25k diagnostic subsets, then failed with `Number of atoms per molecule (0)`
- canonical full 276864: no component/cycle output within 900 s

probable_cpu_stage: POST_FRAMEWORK_READ_SETUP
probable_cpu_stage_confidence: medium
system_call_block: NO_STRONG_EVIDENCE

This report does not infer non-observed symbols or functions.
