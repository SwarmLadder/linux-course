# find, xargs, and safe file batching

**Intermediate · Lesson 06 · 75–110 minutes**

## Learning outcome
Process large file collections without relying on whitespace splitting or unbounded command arguments.

Linux/WSL2 recommended. Host-modifying and remote commands are illustrative only; local examples use disposable paths.

### 1. Filter using find
find walks a directory tree and filters by type, name, size, or modification time. Use explicit roots and consider symlink behavior. Start with print-only inspection before performing any operation that modifies files.

```bash
work=$(mktemp -d)
mkdir -p "$work/nested"
touch "$work/a.txt" "$work/nested/b.txt" "$work/c.log"
find "$work" -type f -name '*.txt' -print
```

**Check:** Why might a glob from the shell fail to search nested directories?

### 2. Use NUL boundaries
File names can include spaces and newlines. `find -print0 | xargs -0` preserves boundaries; `-r` avoids running the command with no matches on GNU xargs.

```bash
find "$work" -type f -print0 | xargs -0 -r wc -c
find "$work" -type f -name '*.txt' -printf '%P\n' | sort
```

**Check:** Which use of print with newline is display-only rather than a safe machine format?

### 3. Batch operations carefully
xargs groups arguments and can spawn many processes. `-n` limits arguments per command, while `-P` permits concurrency. Concurrency can overwhelm disks or violate ordering assumptions.

```bash
find "$work" -type f -print0 | xargs -0 -n 1 -r basename --
find "$work" -type f -print0 | xargs -0 -n 2 -r stat -c '%s %n' --
```

**Check:** What must be true before adding `xargs -P 8`?

### 4. Prevent unsafe deletion
`find ... -delete` and `xargs rm` can remove large amounts of data. First confirm exact matches, expected directory roots, and symlink policy in a disposable directory. For a learning exercise, report candidate files rather than deleting them.

```bash
find "$work" -maxdepth 2 -type f -printf '%p\n'
find "$work" -type f -name '*.log' -print
```

**Check:** Why is previewing selection not enough when a directory can change concurrently?

## Practice
1. Enumerate text files preserving spaces.
2. Compare xargs -n and batching for 100 files.
3. Explain concurrency hazards with xargs -P.

## Interview questions
- How does -print0 avoid path parsing bugs?
- What is the risk of find -delete?

**Caution:** For modifications, keep the root fixed and test on disposable files.

**Ready when:** You can diagnose expected and failure behavior and explain the safest production alternative.
