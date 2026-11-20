# Intermediate — 25 exercises

Practice independently after the corresponding [lesson track](../intermediate/README.md). Document commands, outputs, failures and assumptions. Do not perform privileged or destructive work against real systems.

1. Implement a Bash CLI requiring exactly one path and a clear usage error.
2. Pass three arguments including one with spaces; demonstrate correct quoted $@ iteration.
3. Validate a port is a decimal integer in range 1..65535, rejecting 0 and 65536.
4. Build a case dispatch for start/stop/status with a nonzero unknown-command exit.
5. Read a file line by line, preserving leading spaces, backslashes and an empty line.
6. Use a Bash array of paths to copy several explicitly selected files.
7. Write a function with a local variable that does not change a global variable.
8. Return different status codes for missing file and malformed file.
9. Implement an EXIT trap cleaning one narrowly scoped temporary output file.
10. Use a temporary file and same-filesystem rename to publish a complete report.
11. Demonstrate when set -e does not terminate execution in an if or && conditional.
12. Count access log requests per IP using awk and deterministic sorting.
13. Compute mean latency with one decimal and handle the empty-input case.
14. Use sed to transform a simple key=value stream without editing its source.
15. Find *.txt recursively with spaces preserved using find -print0.
16. Compare xargs -n 1 versus batched execution with deterministic output.
17. Write a process report capturing PID, elapsed seconds, CPU and memory estimates.
18. Explain high load with low CPU using I/O waits or blocked tasks.
19. Measure both disk blocks and inode capacity and describe differences.
20. Write a safe SSH runbook that verifies host identity and never exposes private keys.
21. Perform a local rsync --dry-run between disposable directories, if rsync is installed.
22. Design an hourly cron job with explicit working directory and PATH.
23. Contrast systemd timers with cron for retries, logs and dependencies.
24. Diagnose a fictional HTTP outage: DNS succeeds but TCP connect times out.
25. Complete labs I01–I04 and the local release simulator project, including rollback.

**Completion:** At least 20/25 solutions reproducible in a fresh disposable environment; no secrets, system changes or unverified destructive steps.
