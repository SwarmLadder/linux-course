# Boot, kernel, init, and service lifecycle

**Advanced · Lesson 00 · 90–120 minutes**

## Outcome
Trace a Linux service from machine boot through process creation and know which layer to inspect when startup fails.

These are safe inspection commands and configuration illustrations. No root privileges or network access is required to work through the concepts.

### 1. Understand the boot chain
Firmware loads a bootloader or boot components, which load the kernel and initial filesystem. The init system then supervises user-space units. Containers often run a different PID 1 and do not follow full host boot semantics.

```bash
uname -r
ps -p 1 -o pid,comm,args
cat /proc/cmdline
```

**Check:** Why is a process inside a container not necessarily managed by host systemd?

### 2. Inspect unit state
systemd units define services, sockets, timers, mounts and dependencies. `systemctl status` and `systemctl show` can inspect units where systemd runs; avoid changing a real unit merely for a lesson.

```bash
if command -v systemctl >/dev/null; then systemctl list-units --type=service --no-pager 2>/dev/null | head -n 12; fi
ps -eo pid,ppid,comm | head -n 8
```

**Check:** Distinguish enabled, active and healthy.

### 3. Know dependencies and ordering
After= expresses ordering, not an automatic requirement; Requires= and Wants= express dependency relationships. Misunderstanding them can allow a service to start before the network or storage is ready.

```bash
# Example unit fields (documentation, not a command):
# [Unit]
# After=network-online.target
# Wants=network-online.target
# [Service]
# ExecStart=/opt/app/bin/server
```

**Check:** What if the service needs a database that is unavailable after startup?

### 4. Observe failures and restart policy
Restart=on-failure can recover a crashing process but not a service stuck while still running. Bound restart loops with start limits and make readiness checks meaningful.

```bash
if command -v journalctl >/dev/null; then journalctl -b -n 5 --no-pager 2>/dev/null || :; fi
ps -p 1 -o stat,comm
```

**Check:** Why is a restart policy not a substitute for fixing a crash?

## Applied exercises
1. Draw the kernel-to-service startup chain.
2. Explain an active service returning HTTP 500.
3. Compare dependencies, order, and readiness in a unit file.

## Interview review
- What does systemd manage?
- What is special about PID 1?

**Caution:** Commands only inspect the host; never edit init configuration for practice.

**Pass:** Explain the subsystem, how to inspect failure, and one risk of the naive fix.
