# Files, inodes, links, and metadata

**Basics · Lesson 02 · 60–90 minutes**

## Goal
Create, copy, and inspect files; understand inode identity and why a link is not a backup.

Use a Linux shell or WSL2. These examples inspect the system or write inside disposable temporary paths.

### 1. Create predictable content
printf writes exact bytes without implementation-specific echo escape behavior. stat reports size, inode number and mode. File names do not guarantee file content type.

```bash
work=$(mktemp -d)
printf 'alpha\nbeta\n' > "$work/note.txt"
stat -c 'inode=%i size=%s mode=%a' "$work/note.txt"
file "$work/note.txt"
```

**Verify:** Compare file size with the number of displayed characters.

### 2. Copy and rename
cp normally creates a new inode; mv within one filesystem usually renames a directory entry. Across filesystems, a move may require a copy followed by deletion. Inspect destinations before overwriting.

```bash
cp -- "$work/note.txt" "$work/copy.txt"
mv -- "$work/copy.txt" "$work/new.txt"
ls -li -- "$work"
```

**Verify:** Why is a rename usually cheaper than a full copy on one filesystem?

### 3. Link semantics
A symbolic link stores a reference to a path. A hard link is another name for the same inode on that filesystem. Deleting one hard-link name does not remove the data while another link exists.

```bash
ln -s -- "$work/note.txt" "$work/symbolic.txt"
ln -- "$work/note.txt" "$work/hard.txt"
ls -li -- "$work"
readlink -- "$work/symbolic.txt"
```

**Verify:** Which file names share inode numbers?

### 4. Delete deliberately
rm unlinks named paths; it is not a versioning tool. Check paths and contents before deletion; avoid wildcard or recursive removal when you haven't inspected matches.

```bash
ls -la -- "$work"
rm -- "$work/new.txt"
find "$work" -maxdepth 1 -type f -printf '%f\n'
```

**Verify:** The example removes only a disposable file.

## Independent practice
1. Compare cp versus hard-link inode numbers.
2. Delete the original symlink target and inspect links in a disposable directory.
3. Copy a filename containing spaces without splitting its path.

## Interview checks
- Why are hard links restricted across filesystems?
- Why doesn't deleting a file imply secure data destruction?

**Safety:** Never test recursive deletion on production directories.

**Ready when:** You can explain each command's input, output, exit status, and a failure case.
