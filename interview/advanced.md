# Advanced — 20 interview questions

Explain each answer using a command, log line, configuration example, or failure scenario from the course.

1. **What is PID 1 responsible for in Linux containers?** It has special signal/reaping responsibilities within its PID namespace; some containers need an init helper.

2. **What is the difference between systemd After and Requires?** After orders unit activation; Requires expresses a stronger dependency. Neither alone proves application readiness.

3. **Why run backend services with dedicated users?** Limits damage and controls access to files, networks and privileged operations.

4. **What are Linux capabilities?** Kernel privilege units that can grant subsets of traditional root authority, subject to policy and namespace behavior.

5. **What do namespaces isolate?** Process-visible resources such as PID, mount and network views; they do not guarantee complete security alone.

6. **What do cgroups regulate?** Resource accounting and limits including CPU, memory and process tasks.

7. **Why can a container OOM with free host RAM?** It can exceed its cgroup memory limit independent of host availability.

8. **Why is listening on 127.0.0.1 different from 0.0.0.0?** Loopback only accepts local-bound connections, whereas 0.0.0.0 binds available IPv4 interfaces subject to firewall/routes.

9. **How is HTTP 503 different from a TCP timeout?** 503 is an HTTP response from a reachable server/proxy; TCP timeout usually indicates the connection could not complete.

10. **Why should TLS certificate verification remain enabled?** It authenticates the intended endpoint, protecting against impersonation and man-in-the-middle risks.

11. **What is journald useful for?** Querying collected service logs with unit, boot, timestamp and priority filters on systems using it.

12. **What are SLIs and SLOs?** An SLI is an observed service metric; an SLO is the target for that metric over a defined period.

13. **Why is p95 latency not the average?** p95 describes a tail threshold for observed latencies; an average can hide a small share of very slow requests.

14. **What is RPO?** Maximum tolerable window of data loss; it influences backup and replication cadence.

15. **What is RTO?** Target elapsed time to restore service after an incident.

16. **How can a backup be validated?** Restore it to an isolated environment and check application/data invariants, not just the presence of an archive.

17. **How can inode exhaustion affect a service?** New files cannot be created even if free bytes remain; check df -i as well as df -h.

18. **What should an incident timeline include?** Time-stamped observed facts, impact, interventions, results and unresolved hypotheses, without exposing credentials.

19. **Why is CI on pull requests a security boundary?** Untrusted contributor code can run in jobs; avoid exposing deployment tokens or privileged workflows.

20. **How should a production rollback be prepared?** Keep tested release artifacts, compatibility with schema changes, documented switches, readiness checks and responsible owners.

**Review standard:** Explain a practical example and one unsafe shortcut for at least 16/20 questions.
