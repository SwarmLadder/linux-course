# Linux & Bash Portfolio Projects

Three offline projects designed for backend engineering and operations interviews.

| Project | Skills | Starter/reference |
|---|---|---|
| [01 — Log analytics CLI](01_log_analytics.md) | Parsing, validation, reliable output, error cases | [Example](examples/log_summary.sh) |
| [02 — Local release simulator](02_release_simulator.md) | Staging, atomic switch, checksums, rollback | [Deploy](examples/release_simulator.sh) / [Rollback](examples/rollback_release.sh) |
| [03 — Incident operations report](03_incident_operations.md) | Latency, failed service detection, incident response | [Example](examples/operations_report.sh) |

Each project requires a README with contract, example run, tests, limitations, and one operational failure scenario. Examples run without root or network access.

```bash
python -m unittest discover -s tests -v
```

Reference examples are intentionally small. Students should add tests and handle the extension requirements before claiming portfolio readiness.
