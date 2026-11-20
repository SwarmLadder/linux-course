# Least privilege, capabilities, ACLs and sudo

**Advanced · Lesson 02 · 90–120 minutes**

## Outcome
Protect backend services through correct user boundaries, filesystem access and limited elevated operations.

These are safe inspection commands and configuration illustrations. No root privileges or network access is required to work through the concepts.

### 1. Inspect identities and groups
Every process has real/effective user and group IDs. Ownership, mode bits and ACLs influence filesystem access. A backend process should not run as root unless a narrow, justified capability is truly needed.

```bash
id
id -Gn
stat -c '%a %U:%G %n' "$HOME"
ps -o uid,gid,comm -p "$$"
```

**Check:** What happens if a service writes data owned by root and then runs unprivileged?

### 2. Understand ACLs and umask
Mode bits are only one layer; ACLs may grant additional rights and umask affects new objects. Review actual effective permissions before recommending chmod 777.

```bash
umask
command -v getfacl || echo 'getfacl not installed'
ls -ld /tmp "$HOME"
```

**Check:** Why can group ownership be preferable to world-write permissions?

### 3. Use capabilities sparingly
Linux capabilities split some traditional root privileges. Services may need network bind capabilities for privileged ports, but granting broad capabilities increases impact. Container capability configuration is a security decision.

```bash
if command -v capsh >/dev/null; then capsh --print | head -n 6; fi
cat /proc/self/status | grep '^Cap' || :
```

**Check:** How do capabilities differ from being the root user?

### 4. Review sudo safely
Sudoers policy can authorize specific commands but must avoid unsafe wildcard and shell escapes. `sudo -l` shows allowed commands when configured; do not run sudo commands for this course.

```bash
command -v sudo || :
# Read-only check if authorized:
# sudo -l
# Never store sudo passwords in scripts.
```

**Check:** Why can sudo access to an editor or shell effectively grant broad privileges?

## Applied exercises
1. Design a least-privilege account for a web application.
2. Explain when ACLs are more appropriate than changing group mode bits.
3. Threat-model a script that runs as root and reads user-controlled files.

## Interview review
- What are Linux capabilities?
- Why is sudo a policy boundary, not a debugging trick?

**Caution:** No root privileges required in local labs.

**Pass:** Explain the subsystem, how to inspect failure, and one risk of the naive fix.
