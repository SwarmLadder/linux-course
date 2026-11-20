# Filesystem internals, inodes, mounts, and storage health

**Advanced · Lesson 05 · 90–120 minutes**

## Outcome
Understand path resolution, inode usage and durability limitations of storage operations.

These are safe inspection commands and configuration illustrations. No root privileges or network access is required to work through the concepts.

### 1. Distinguish names from inodes
Directories map names to inode identifiers, and inodes hold metadata/pointers to data. Hard links share inodes; symbolic links store a path. Filesystem boundaries influence linking and renaming.

```bash
work=$(mktemp -d)
printf 'abc\n' > "$work/a.txt"
ln "$work/a.txt" "$work/b.txt"
stat -c '%i %h %n' "$work"/*.txt
```

**Check:** Why can a file exist after deleting one name?

### 2. Understand mounts
Mount points attach filesystems into one directory tree. Bind mounts expose another path; mount namespaces can make the same process path resolve differently in containers.

```bash
findmnt -T . 2>/dev/null || :
df -h .
mount | head -n 5
```

**Check:** How does a mount point change assumptions about atomic rename?

### 3. Check inodes and blocks
Free disk bytes are only one constraint: inode exhaustion and file descriptor limits also stop applications. Look at `df -i`, `ulimit` and process open files during failures.

```bash
df -i .
ulimit -n
ls /proc/self/fd | wc -l
```

**Check:** How might an API fail with 'too many open files' despite free disk space?

### 4. Crash consistency matters
Renaming a complete temp file usually gives atomic visibility on one filesystem, but durability after a power failure may require syncing file data and directory metadata. Databases and safe write libraries manage stronger guarantees.

```bash
work=$(mktemp -d)
printf 'complete\n' > "$work/new.tmp"
mv -- "$work/new.tmp" "$work/live.txt"
cat "$work/live.txt"
```

**Check:** Why doesn't atomic visibility guarantee disk persistence?

## Applied exercises
1. Investigate an inode-full scenario.
2. Explain hard links, symlinks and mounts in a container.
3. Design an atomic update policy for a configuration file.

## Interview review
- Why can disk space be available while writes fail?
- What happens if a rename crosses filesystem boundaries?

**Caution:** Do not modify mounted devices or production storage during practice.

**Pass:** Explain the subsystem, how to inspect failure, and one risk of the naive fix.
