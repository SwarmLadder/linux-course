# Permissions, ownership, and umask

**Basics · Lesson 06 · 60–90 minutes**

## Goal
Read permission bits, create private files and distinguish script executability from sudo privileges.

Linux/WSL2 shell recommended. Examples are read-only or work with disposable files.

### 1. Read owner and mode
Linux discretionary permissions distinguish owner, group and others. Read, write and execute have different meanings on files and directories. Directory execute permission controls traversal, not running code.

```bash
id
ls -ld /tmp "$HOME"
stat -c '%A %a %U:%G %n' "$HOME"
```

**Check:** Why can an inaccessible parent block access to an otherwise readable file?

### 2. Choose least privilege
chmod controls mode bits on owned files. A private config might need 600 and a private directory 700. Do not use chmod 777 as a substitute for understanding owner/group and service accounts.

```bash
work=$(mktemp -d)
printf 'demo\n' > "$work/config.txt"
chmod 600 "$work/config.txt"
stat -c '%a %n' "$work/config.txt"
```

**Check:** The example contains synthetic data, not credentials.

### 3. Understand umask
umask removes bits from the default creation mode. It does not simply specify final mode. Effective file and directory defaults differ because new regular files normally do not start executable.

```bash
umask
(umask 077; work=$(mktemp -d); touch "$work/private.txt"; stat -c '%a %n' "$work/private.txt")
```

**Check:** Why should a private deployment script establish a restrictive umask?

### 4. Run scripts with a shebang
A script's shebang chooses an interpreter for direct execution; Bash can run the same file explicitly without its executable bit. Keep permission changes scoped to practice files.

```bash
work=$(mktemp -d)
printf '#!/usr/bin/env bash\nprintf "ready\\n"\n' > "$work/hello.sh"
chmod 700 "$work/hello.sh"
bash "$work/hello.sh"
```

**Check:** What changes between `bash script.sh` and `./script.sh`?

## Independent practice
1. Predict chmod 640 and directory 750.
2. Create a private practice file and verify its mode.
3. Explain difference between sudo and changing permissions.

## Interview checks
- What does the execute bit mean on a directory?
- Why is chmod 777 risky?

**Safety:** Do not alter system-wide permissions for an educational task.

**Complete when:** You can explain input, output, exit status, and one failing case.
