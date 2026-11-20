# Processes, background jobs, and signals

**Basics · Lesson 08 · 60–90 minutes**

## Goal
Track child processes, wait for results and understand why long-running servers need supervision.

Linux/WSL2 shell recommended. Examples are read-only or work with disposable files.

### 1. Read process metadata
Processes have process IDs, parent IDs and states. ps and pgrep are useful for inspection. PIDs can be reused, so do not blindly signal an old PID read from a file.

```bash
printf 'shell=%s\n' "$$"
ps -o pid,ppid,stat,comm -p "$$"
ps -ef | head -n 4
```

**Check:** Which process launched your current shell?

### 2. Launch and wait
Ampersand starts a command asynchronously from the interactive shell; $! records the newest background PID. `wait` obtains its result and collects child exit state.

```bash
sleep 0.1 &
child=$!
printf 'child pid=%s\n' "$child"
wait "$child"
printf 'exit=%s\n' "$?"
```

**Check:** Why should scripts wait for spawned work before reporting success?

### 3. Understand signals
SIGTERM requests termination, allowing cleanup if implemented; SIGKILL cannot be caught. Graceful shutdown is especially important when writing persistent files or processing messages.

```bash
kill -l TERM
kill -l INT
kill -l KILL
trap 'echo termination-requested' TERM
```

**Check:** Do not experiment by killing system or unrelated user processes.

### 4. Foreground jobs versus services
A background process is not a service manager. systemd (when present) handles lifecycle, restarts, dependencies and logs. `nohup` alone does not implement observability or reliable deployment.

```bash
jobs -l
command -v systemctl || echo 'systemd tool unavailable'
ps -o stat,comm -p "$$"
```

**Check:** What happens if a backend process crashes during the night?

## Independent practice
1. Start two background sleeps, then wait for both.
2. Describe a graceful shutdown handler.
3. Compare a background job with a supervised service.

## Interview checks
- Why is SIGKILL a last resort?
- What is the purpose of wait?

**Safety:** Don't signal unknown PIDs.

**Complete when:** You can explain input, output, exit status, and one failing case.
