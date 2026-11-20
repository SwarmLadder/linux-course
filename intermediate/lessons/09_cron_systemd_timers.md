# Scheduling, cron, and systemd timers

**Intermediate · Lesson 09 · 75–110 minutes**

## Learning outcome
Schedule repeatable jobs with explicit environments and failure visibility, and know when a service supervisor is more appropriate.

Linux/WSL2 recommended. Host-modifying and remote commands are illustrative only; local examples use disposable paths.

### 1. Understand cron context
Cron launches jobs with a limited environment and often a different working directory. Set PATH, use absolute paths and log errors. Avoid overlapping executions when a job may take longer than its interval.

```bash
# Example crontab line (do not install):
# 15 * * * * /usr/local/bin/report.sh >>/var/log/report.log 2>&1
crontab -l 2>/dev/null || :
```

**Check:** What can go wrong if the job depends on your interactive PATH?

### 2. Inspect timers without changing system state
Where systemd runs, list active timers and inspect existing unit properties. In containers or WSL, systemd may not be PID 1; command availability does not guarantee service management is active.

```bash
command -v systemctl || :
if command -v systemctl >/dev/null; then systemctl list-timers --all --no-pager 2>/dev/null | head -n 10; fi
ps -p 1 -o comm=
```

**Check:** Why might systemctl fail inside a container?

### 3. Sketch a safe oneshot service
A oneshot unit runs a command to completion, while a timer determines scheduling. Use a dedicated low-privilege user, explicit working directory and failure reporting; examples are configuration, not commands to install.

```bash
# report.service example:
# [Service]
# Type=oneshot
# User=reporter
# WorkingDirectory=/opt/report
# ExecStart=/opt/report/bin/run.sh
```

**Check:** Why shouldn't a scheduled maintenance job default to root?

### 4. Handle retries and overlap
Timers and cron don't automatically solve application idempotency, locking or data durability. Design reentrancy, bounds, and explicit outcomes. A lock file alone can have stale-lock and race problems.

```bash
# Runbook questions:
# - Is duplicate execution safe?
# - What happens when a job runs longer than its interval?
# - How is failure alerted?
# - How do we test a missed schedule?
```

**Check:** How do service managers and application-level retries complement each other?

## Practice
1. Write a safe hourly cron schedule for a synthetic script.
2. Explain differences between systemd timer and cron.
3. Design safeguards for overlapping jobs.

## Interview questions
- Why should cron commands use absolute paths?
- How would you find a failing scheduled job's output?

**Caution:** Do not install real timers or crontabs as part of course validation.

**Ready when:** You can diagnose expected and failure behavior and explain the safest production alternative.
