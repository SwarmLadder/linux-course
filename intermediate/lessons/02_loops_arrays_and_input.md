# Loops, arrays, and reading input safely

**Intermediate · Lesson 02 · 75–110 minutes**

## Learning outcome
Iterate over files and records without losing whitespace or spawning too many processes.

Practice in Bash on Linux or WSL2. Examples use disposable files, and no sudo or internet connection is required.

### 1. For loops over defined values
Use for when the input is a known list. Quote arrays as `"${array[@]}"` to preserve item boundaries. Unquoted iteration can turn one filename into multiple arguments.

```bash
names=('Ana' 'Bob Smith' 'Cleo')
for name in "\${names[@]}"; do printf '<%s>\n' "$name"; done
```

**Verify:** How many arguments are in the names array?

### 2. Read lines without mangling
`IFS= read -r` prevents leading/trailing whitespace trimming and backslash interpretation. Handle a final line with no newline when necessary; ordinary while read loops otherwise may skip it.

```bash
work=$(mktemp -d)
printf 'first\nsecond line\n' > "$work/data.txt"
while IFS= read -r line; do printf 'line=<%s>\n' "$line"; done < "$work/data.txt"
```

**Verify:** What does `read -r` protect?

### 3. Process arbitrary filenames
Newlines are legal in Linux filenames. For file inventory, use `find -print0` paired with `read -d ''`. Avoid `for path in $(find ...)` and parsing output from ls.

```bash
touch "$work/name with spaces.txt"
while IFS= read -r -d '' file; do
  printf 'path=%q\n' "$file"
done < <(find "$work" -type f -print0)
```

**Verify:** Why is NUL a safe filename delimiter?

### 4. Control while-loop termination
A loop must have an explicit exit condition. In Bash, arithmetic commands return status 1 when the result is zero; this can surprise scripts using set -e.

```bash
count=0
while (( count < 3 )); do
 printf 'iteration=%d\n' "$count"
 count=$((count+1))
done
```

**Verify:** Why is `((count++))` dangerous under `set -e` when count starts at zero?

## Practice
1. Find and print file names containing spaces.
2. Parse lines with leading spaces and backslashes.
3. Create an array-driven command dispatcher.

## Interview questions
- When should you choose an array instead of a string?
- Why is `read -r` recommended?

**Production caution:** Use bounded loops when processing untrusted input.

**Pass condition:** Show a normal case, failure case and explanation of exit status and side effects.
