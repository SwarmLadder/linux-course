# Performance investigation: CPU, memory, I/O, and sockets

**Advanced · Lesson 07 · 90–120 minutes**

## Learning goal
Build a hypothesis-driven diagnostic workflow rather than killing busy processes or adding resources blindly.

Use Linux/WSL2 for inspection and disposable local fixtures for writing. Production configuration is conceptual unless you own a safe test environment.

### 1. Start with baselines
Capture load, resource availability and request symptoms at the same moment. CPU percentage alone does not distinguish application bottlenecks, I/O waits and lock contention.

```bash
uptime
free -h
df -h .
ps -eo pid,stat,%cpu,%mem,comm --sort=-%cpu | head -n 10
```

**Check:** What evidence supports a CPU saturation hypothesis versus an I/O wait hypothesis?

### 2. Observe I/O and file descriptors
Open files, inode use and filesystem latency affect backends. Where available, iostat or pidstat provide deeper evidence; these tools may need additional packages.

```bash
df -i .
ulimit -n
ls /proc/self/fd | wc -l
command -v iostat || :
```

**Check:** How could a leaked file descriptor present as intermittent request failures?

### 3. Interpret scheduling and cgroup limits
A container may hit CPU or memory quotas even while the host has spare resources. Investigate throttling, OOM events and per-container limits before increasing instance size.

```bash
cat /proc/self/cgroup | head -n 5
if [[ -f /sys/fs/cgroup/cpu.stat ]]; then cat /sys/fs/cgroup/cpu.stat | head -n 5; fi
if [[ -f /sys/fs/cgroup/memory.events ]]; then cat /sys/fs/cgroup/memory.events; fi
```

**Check:** Why can throttling look like unpredictable latency spikes?

### 4. Measure before optimizing
Record workload shape, baseline latency, error rates, system metrics and change impact. Avoid overclaiming benchmark results from a tiny or unrepresentative sample.

```bash
python3 - <<'PY'
import time
start=time.perf_counter()
sum(range(100000))
print('elapsed_s',round(time.perf_counter()-start,6))
PY
```

**Check:** Why should profiling match production workload characteristics?

## Applied work
1. Write a one-page performance incident hypothesis and evidence table.
2. Distinguish memory pressure and CPU saturation.
3. Compare pre/post measurements for one change.

## Interview review
- What is CPU throttling?
- How do I/O wait and CPU utilization differ?

**Safety:** Don't run destructive load tests on shared infrastructure.

**Complete when:** You can justify the diagnostic evidence, operational risk and recovery choice.
