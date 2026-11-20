# Linux & Backend Operations glossary

| Term | Meaning |
|---|---|
| Shell | Program interpreting commands and scripts |
| Kernel | Operating-system core coordinating processes and resources |
| Process | Running program with PID and execution state |
| PID 1 | First process in a PID namespace; init or container entrypoint |
| inode | Filesystem metadata object referenced by directory entries |
| Hard link | Additional filename for the same inode |
| Symlink | File referring to another path |
| Mount | Attachment of a filesystem to a directory path |
| PATH | Executable lookup search directories |
| umask | Mask removing default permission bits on new objects |
| stdin/stdout/stderr | Standard input, output, and error streams |
| Exit code | Numeric success/failure status of a process |
| pipefail | Bash option propagating pipeline stage failures |
| trap | Bash handler for selected signals or shell EXIT |
| systemd unit | Configuration describing managed system resources |
| cgroup | Kernel grouping/accounting and resource-limit mechanism |
| Namespace | Kernel isolation of resources visible to a process |
| DNS | System resolving domain names to addresses |
| TLS | Authenticated encryption protocol for network connections |
| ACL | Access control list extending basic permission bits |
| SLI | Measured service reliability indicator |
| SLO | Service reliability target within a stated window |
| RPO | Maximum tolerable data-loss interval |
| RTO | Recovery time objective |
| Atomic rename | Single-filesystem path switch with atomic visibility |
| journald | Logging daemon typically used by systemd |
| SSH | Secure Shell for authenticated encrypted remote access |
| idempotency | Repeated logical operation does not multiply intended effects |
| readiness | Whether a service can handle intended work |
| liveness | Whether a process should be considered alive by a supervisor |
