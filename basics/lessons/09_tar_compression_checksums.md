# Archives, compression, and checksums

**Basics · Lesson 09 · 60–90 minutes**

## Goal
Build and verify portable archives and understand backup validation, retention and restore risks.

Linux/WSL2 shell recommended. Examples are read-only or work with disposable files.

### 1. Archive files
tar packages multiple paths while gzip compresses a stream. A .tar.gz is not simply a zip file. The command uses -C so archived paths are relative to the chosen source directory.

```bash
work=$(mktemp -d)
mkdir -p "$work/source"
printf 'hello\n' > "$work/source/readme.txt"
tar -czf "$work/archive.tar.gz" -C "$work" source
tar -tzf "$work/archive.tar.gz"
```

**Check:** Always inspect untrusted archive members before extraction.

### 2. Check data integrity
sha256sum produces an integrity digest. A digest is meaningful when the expected digest is trusted; two attacker-modified files and checksums do not establish authenticity.

```bash
(cd "$work" && sha256sum archive.tar.gz > manifest.sha256)
(cd "$work" && sha256sum -c manifest.sha256)
wc -c "$work/archive.tar.gz"
```

**Check:** Why does a checksum not prove who created an artifact?

### 3. Restore and compare
A backup is useful only if restoration succeeds. Extract trusted archives into a new directory and verify contents. Malicious archive paths and symlinks can escape unsafe extraction tooling.

```bash
mkdir -p "$work/restore"
tar -xzf "$work/archive.tar.gz" -C "$work/restore"
cat "$work/restore/source/readme.txt"
```

**Check:** Never extract unknown archives into production directories as root.

### 4. Inspect disk and capacity
df reports filesystem availability; du measures path usage. A reliable backup plan additionally defines storage access, encryption, off-host copies, retention and regularly tested restoration.

```bash
du -sh "$work/source" "$work/archive.tar.gz"
df -h "$work"
stat -c '%s bytes' "$work/archive.tar.gz"
```

**Check:** Why is a backup on the same failing disk insufficient?

## Independent practice
1. Create, verify, and restore a sample tar.gz.
2. Change a file and show checksum verification failing.
3. Describe restore testing and retention.

## Interview checks
- How do gzip and tar differ?
- Why should backups be tested by restoring?

**Safety:** Use synthetic archive files; no privileged filesystem access is needed.

**Complete when:** You can explain input, output, exit status, and one failing case.
