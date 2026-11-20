# Writing and evaluating systemd service units

**Advanced · Lesson 01 · 90–120 minutes**

## Outcome
Read service unit files and choose lifecycle limits, user context, and observable failure behavior.

These are safe inspection commands and configuration illustrations. No root privileges or network access is required to work through the concepts.

### 1. Service unit structure
A typical unit has Unit, Service and Install sections. `ExecStart` is not a shell script unless explicitly run through a shell. Choose absolute paths and a dedicated service account rather than assuming an interactive environment.

```bash
# Illustrative /etc/systemd/system/demo.service:
# [Unit]
# Description=Demo API
# [Service]
# User=demoapp
# WorkingDirectory=/opt/demoapp
# ExecStart=/opt/demoapp/venv/bin/python -m server
# Restart=on-failure
```

**Check:** How would a relative path differ under systemd?

### 2. Bound resource usage
systemd can apply memory, CPU and task limits through cgroups. Limits help isolate workloads but can make startup, thread creation or peak requests fail when undersized.

```bash
# Illustrative unit fields:
# MemoryMax=512M
# TasksMax=128
# TimeoutStopSec=20s
# RestartSec=2s
if command -v systemctl >/dev/null; then systemctl --version | head -n 1; fi
```

**Check:** How would you confirm the process exits gracefully when stopped?

### 3. Apply useful sandboxing
Options such as NoNewPrivileges, ProtectSystem, PrivateTmp and RestrictAddressFamilies can narrow service privileges. These settings require testing against actual read/write and network requirements; they are not universal copy-paste defaults.

```bash
# Example hardening (not deployed):
# NoNewPrivileges=yes
# ProtectSystem=strict
# PrivateTmp=yes
# ReadWritePaths=/var/lib/demoapp
```

**Check:** Which writable locations must a stateful service retain?

### 4. Validate before deployment
`systemd-analyze security` (where available) reports unit exposure, but a score cannot guarantee application safety. CI should test unit syntax and production should test behavior and rollback.

```bash
command -v systemd-analyze || :
if command -v systemctl >/dev/null; then systemctl list-unit-files --type=service --no-pager 2>/dev/null | head -n 7; fi
```

**Check:** How can a unit be active but not ready for requests?

## Applied exercises
1. Design a read-only service account and filesystem policy.
2. Write a systemd unit for a Python API with restart and stop timeout.
3. Explain how to verify a change without breaking production.

## Interview review
- What is the purpose of WorkingDirectory?
- What does ProtectSystem=strict change?

**Caution:** Unit examples are for review only, not automatic installation.

**Pass:** Explain the subsystem, how to inspect failure, and one risk of the naive fix.
