# SSH, remote commands, and rsync

**Intermediate · Lesson 08 · 75–110 minutes**

## Learning outcome
Understand authenticated remote access and safe file synchronization without requiring a real remote server for practice.

Linux/WSL2 recommended. Host-modifying and remote commands are illustrative only; local examples use disposable paths.

### 1. Inspect SSH trust boundaries
SSH encrypts connections and authenticates the server using host keys. Client private keys must never enter Git; host verification should not be disabled to make a demo work.

```bash
ssh -V
ls -ld "$HOME/.ssh" 2>/dev/null || :
command -v ssh-keygen || :
```

**Check:** Why does accepting any host key enable man-in-the-middle attacks?

### 2. Understand remote command quoting
Commands sent over SSH are interpreted by a remote shell. Quoting can be parsed both locally and remotely; avoid building command strings from untrusted input.

```bash
# Illustrative only; requires a server you administer:
# ssh user@example.test -- 'uname -a'
# ssh -o BatchMode=yes user@example.test -- 'id'
```

**Check:** How can command injection occur when interpolating a user name into a remote command?

### 3. Choose scp versus rsync
scp transfers files; rsync can synchronize differences and preserve selected metadata. `rsync --dry-run` shows intended actions; deletion flags are particularly risky on incorrect destinations.

```bash
work=$(mktemp -d)
mkdir -p "$work/source" "$work/dest"
printf 'test\n' > "$work/source/a.txt"
if command -v rsync >/dev/null; then rsync -av --dry-run "$work/source/" "$work/dest/"; fi
```

**Check:** What changes when the source ends with / in rsync?

### 4. Design remote deployment safety
Use narrowly scoped keys, restricted accounts, known hosts, checked artifacts, versioned releases, and rollback. Uploading files is not enough to ensure a healthy backend deployment.

```bash
# Planning checklist:
# 1) Verify host identity and artifact checksum
# 2) Upload to a versioned release directory
# 3) Test readiness before switching traffic
# 4) Keep a documented rollback target
```

**Check:** Why should deployment be repeatable and idempotent?

## Practice
1. Describe the SSH key trust model.
2. Build a local rsync dry-run and explain output.
3. Draft a remote deployment plan with rollback.

## Interview questions
- Why is StrictHostKeyChecking=no dangerous?
- Does rsync -a verify application correctness?

**Caution:** No network access or credentials required for this lesson.

**Ready when:** You can diagnose expected and failure behavior and explain the safest production alternative.
