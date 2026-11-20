# Advanced capstone: operate a fictional backend service

**Advanced · Lesson 11 · 90–120 minutes**

## Learning goal
Combine Linux inspection, shell scripting, monitoring, deployment, backup integrity, and incident decisions into one portfolio exercise.

Use Linux/WSL2 for inspection and disposable local fixtures for writing. Production configuration is conceptual unless you own a safe test environment.

### 1. Define the service contract
Assume a Python HTTP API and worker consuming messages. Define process ownership, service unit, health/readiness endpoints, log fields, deployment directories and recovery requirements before writing scripts.

```bash
# Design deliverables:
# service user and writable directories
# service + timer unit files
# health/readiness checks
# log events and error metrics
# RPO/RTO requirements
```

**Check:** Why can't successful process startup prove the service is ready?

### 2. Use controlled artifacts
A release must be identifiable by version, checksum and source commit. Stage it in a new directory, test configuration, then switch traffic only when ready. Prefer atomic visibility over partial file writes.

```bash
work=$(mktemp -d)
mkdir -p "$work/releases/v1"
printf 'service v1\n' > "$work/releases/v1/app.txt"
sha256sum "$work/releases/v1/app.txt"
ln -s "$work/releases/v1" "$work/current"
readlink "$work/current"
```

**Check:** How would another worker be protected from concurrent release changes?

### 3. Report operational metrics
Use synthetic logs to measure error counts and latency. Keep stdout data stable and stderr diagnostic; logs should not contain secrets. Demonstrate failure cases rather than only successful output.

```bash
python tools/grade.py --list
python tools/grade.py A02
python tools/grade.py A03
# Implement starter scripts before expecting these checks to pass.
```

**Check:** What do p90 latency and failed service counts tell you together?

### 4. Demonstrate recovery
Validate a backup, describe a controlled rollback, and write an incident report showing detection, mitigation and verification. Portfolio reviewers need repeatable evidence, not a claim that deployment is production-ready.

```bash
python tools/grade.py A01
python tools/grade.py A04
python tools/grade.py --verify-references
```

**Check:** Why is an isolated restore drill essential before production release?

## Applied work
1. Complete A01–A04 with passing normal/edge fixtures.
2. Create a systemd unit review, release runbook, and backup restore plan.
3. Write an incident report for high latency plus failing workers.

## Interview review
- How would you deploy without downtime?
- Which controls prevent an unsafe rollback?

**Safety:** All runnable examples are offline and operate only on synthetic files.

**Complete when:** You can justify the diagnostic evidence, operational risk and recovery choice.
