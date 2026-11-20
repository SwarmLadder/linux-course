# Journald, logs, metrics, and observability

**Advanced · Lesson 06 · 90–120 minutes**

## Learning goal
Collect evidence to answer what failed, when, and for whom without disclosing secrets or confusing logs with service-level metrics.

Use Linux/WSL2 for inspection and disposable local fixtures for writing. Production configuration is conceptual unless you own a safe test environment.

### 1. Read relevant journal entries
journald records messages from supervised services on systemd systems. Unit, boot and time filters keep investigation focused. Access may be restricted and a minimal container might not run journald.

```bash
if command -v journalctl >/dev/null; then journalctl -b -n 8 --no-pager 2>/dev/null || :; fi
ps -p 1 -o comm=
```

**Check:** Why should you filter by unit and time before exporting logs?

### 2. Design log fields
Useful logs include UTC timestamp, event name, request/correlation ID, level and safe outcome. Avoid passwords, tokens and raw personal payloads. Machine-readable records support deterministic parsing and aggregation.

```bash
printf 'time=2026-11-20T12:00:00Z level=INFO event=start request_id=req-1\n'
printf 'time=2026-11-20T12:00:01Z level=ERROR event=timeout request_id=req-1\n'
```

**Check:** How would the request ID connect multiple service components?

### 3. Differentiate counters and durations
An error counter measures counts, while latency samples measure elapsed time. An average hides tail behavior, so p95/p99 may be more useful when sample size permits. Define measurement windows.

```bash
printf '10\n20\n30\n50\n100\n' | sort -n | awk '{v[++n]=$1} END{print "p90-nearest-rank:",v[int((9*n+9)/10)]}'
printf '200\n500\n200\n' | sort | uniq -c
```

**Check:** Why is the highest response time not an adequate overall service metric?

### 4. Define SLI and SLO
An SLI observes behavior, such as successful requests divided by total requests over a fixed window. An SLO is a target; an error budget is allowed unreliability. Alerts should detect actionable sustained problems.

```bash
awk 'BEGIN{success=995; total=1000; printf "availability=%.2f%%\n",100*success/total}'
# Example SLO: 99.5% success during a rolling 30-day window
```

**Check:** Why must the observation window be stated when comparing SLOs?

## Applied work
1. Write an incident timeline using event IDs and timestamps.
2. Compute mean and p90 latency from a small file.
3. Explain which error-rate changes deserve an alert.

## Interview review
- How do logs, metrics, and traces differ?
- What is an error budget?

**Safety:** Avoid claiming a universal p90/p99 from tiny samples.

**Complete when:** You can justify the diagnostic evidence, operational risk and recovery choice.
