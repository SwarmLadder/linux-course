# Conditionals, tests, and case patterns

**Intermediate · Lesson 01 · 75–110 minutes**

## Learning outcome
Build reliable branching logic without confusing strings, numbers, or filesystem tests.

Practice in Bash on Linux or WSL2. Examples use disposable files, and no sudo or internet connection is required.

### 1. Use safe test syntax
`[[ ... ]]` is a Bash keyword and avoids some unquoted-expansion surprises. `-f`, `-d`, and `-L` test file kinds; `-e` tests existence. Check required inputs before opening them.

```bash
work=$(mktemp -d)
printf 'value\n' > "$work/data.txt"
if [[ -f "$work/data.txt" ]]; then echo 'regular file'; fi
if [[ ! -e "$work/missing" ]]; then echo 'missing'; fi
```

**Verify:** What could change between testing and opening a path?

### 2. Compare strings and numbers
`==` compares strings in `[[ ]]`, while `-eq`, `-lt`, and arithmetic contexts compare integers. Use validated numeric input before arithmetic; empty or non-numeric strings can behave unexpectedly.

```bash
value=15
if [[ "$value" =~ ^[0-9]+$ ]] && (( value > 10 )); then echo 'large'; fi
[[ a == a ]] && echo 'same text'
```

**Verify:** What input checks are needed for user-provided port numbers?

### 3. Use case for dispatch
`case` matches shell patterns and is effective for a finite set of commands or states. Include a default branch that returns a clear error for unsupported options.

```bash
action=start
case "$action" in
 start) echo 'start requested' ;;
 stop) echo 'stop requested' ;;
 *) echo 'invalid action' >&2; exit 2 ;;
esac
```

**Verify:** Why is an explicit default preferable to silently ignoring a typo?

### 4. Compose logic with exit codes
`&&` and `||` execute commands conditionally. They are not substitutes for structured error handling in complex scripts; an error can be masked accidentally if chained carelessly.

```bash
if grep -qF 'ERROR' "$work/data.txt"; then
 echo 'error present'
else
 echo 'no error matches'
fi
```

**Verify:** Differentiate a no-match result from an unreadable file.

## Practice
1. Build a port validator with boundary cases.
2. Write a case-based CLI accepting start/stop/status.
3. Test file and symlink behavior.

## Interview questions
- When should numeric comparisons use arithmetic syntax?
- How does a shell condition obtain truth?

**Production caution:** Inspect suspicious paths before using shell condition results for privileged operations.

**Pass condition:** Show a normal case, failure case and explanation of exit status and side effects.
