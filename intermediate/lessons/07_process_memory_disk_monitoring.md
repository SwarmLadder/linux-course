# CPU, memory, disk, and process inspection

**Intermediate · Lesson 07 · 75–110 minutes**

## Learning outcome
Collect the minimum evidence needed to diagnose a slow or unhealthy backend service.

Linux/WSL2 recommended. Host-modifying and remote commands are illustrative only; local examples use disposable paths.

### 1. Distinguish load and CPU
uptime shows load average, which includes runnable and some blocked tasks on Linux. `ps` shows CPU and memory estimates; a high load is not identical to high CPU usage.

```bash
uptime
ps -eo pid,ppid,stat,%cpu,%mem,comm --sort=-%cpu | head -n 8
nproc
```

**Check:** Why can a system have high load and low CPU utilization?

### 2. Inspect memory pressure
free displays memory totals and available memory, which differs from simply subtracting free from total. Linux uses page cache; low free memory alone is not proof of memory exhaustion.

```bash
free -h
cat /proc/meminfo | head -n 8
ps -eo pid,rss,comm --sort=-rss | head -n 8
```

**Check:** What evidence would show an out-of-memory kill?

### 3. Check storage and inodes
df reports filesystem capacity, while df -i tracks inode usage. A system can fail to create files when free blocks remain but inodes are exhausted. du helps find path-level consumers.

```bash
df -h .
df -i .
du -sh -- "$HOME" 2>/dev/null || :
```

**Check:** Why is a full root filesystem more than an application storage problem?

### 4. Use targeted process metrics
Inspect an identified process rather than sending signals blindly. Where available, /proc provides file descriptors, status, and limits. cgroup limits may make container behavior differ from the host.

```bash
ps -o pid,ppid,stat,etimes,comm -p "$$"
cat /proc/self/limits | head -n 10
ls /proc/self/fd | head -n 10
```

**Check:** How might an open-file-descriptor leak affect a web server?

## Practice
1. Write a brief CPU/memory/disk incident report.
2. Explain free vs available memory.
3. Identify which process metrics would validate a suspected leak.

## Interview questions
- What does Linux load average measure?
- Why can inode exhaustion break services?

**Caution:** Observe first; don't kill a process before identifying ownership.

**Ready when:** You can diagnose expected and failure behavior and explain the safest production alternative.
