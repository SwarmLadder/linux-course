# Advanced — 25 exercises

Practice independently after the corresponding [lesson track](../advanced/README.md). Document commands, outputs, failures and assumptions. Do not perform privileged or destructive work against real systems.

1. Draw the host boot path from firmware/bootloader to kernel and init service manager.
2. Explain what systemd After=, Wants= and Requires= do with a unit dependency example.
3. Write a reviewed (not installed) systemd service with User, WorkingDirectory and ExecStart.
4. Propose resource, restart and stop-time limits for a backend API.
5. Describe how NoNewPrivileges and a read-only filesystem narrow a service's attack surface.
6. Inspect effective user/group and explain an ACL versus simple chmod permissions.
7. Explain what a Linux capability grants and why broad root privileges are unnecessary.
8. Diagnose a service bound to 127.0.0.1 that cannot be reached remotely.
9. Distinguish DNS failure, TCP timeout, TLS error and HTTP 500 from evidence.
10. Describe a container's PID/network namespaces and cgroup limits.
11. Explain why a container may run out of memory while the host has free RAM.
12. Compare hard links, symbolic links and bind mounts and their isolation effects.
13. Investigate 'no space left on device' with both df -h and df -i.
14. Explain atomic rename versus persistence after sudden power loss.
15. Write a structured diagnostic event with UTC timestamp and correlation ID, without secrets.
16. Define a success-rate SLI, 99.5% SLO and error-budget window for a fictional API.
17. Compute nearest-rank p90 on a list of ten integer latencies and verify the result.
18. Compare CPU pressure, filesystem I/O bottleneck and socket exhaustion symptoms.
19. Write an RPO/RTO plan and demonstrate restoring a trusted test archive.
20. Describe an expand/backfill/contract migration that permits code rollback.
21. Lint a Bash file using bash -n, then discuss what it cannot verify.
22. Design secure PR CI that runs no deployment secrets for untrusted code.
23. Write an incident timeline for a disk-full service and list evidence before restart.
24. Explain a credential leak response including revoke, rotate, scope assessment and prevention.
25. Complete labs A01–A04 and the operations incident project with edge-case tests.

**Completion:** At least 20/25 solutions reproducible in a fresh disposable environment; no secrets, system changes or unverified destructive steps.
