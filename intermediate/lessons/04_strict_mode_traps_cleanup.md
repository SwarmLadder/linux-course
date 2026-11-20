# Strict mode, traps, and safe temporary resources

**Intermediate · Lesson 04 · 75–110 minutes**

## Learning outcome
Treat error handling as a deliberate design choice rather than copying a magic set of Bash flags.

Practice in Bash on Linux or WSL2. Examples use disposable files, and no sudo or internet connection is required.

### 1. Understand shell safety switches
`set -euo pipefail` enables errexit, nounset and pipeline failure propagation. Errexit has exceptions in conditions and compound expressions; it is not a substitute for checking contracts.

```bash
bash -c 'set -euo pipefail; echo ready; true'
bash -c 'set -o pipefail; (false | cat >/dev/null) || echo failed'
```

**Verify:** What can fail without stopping a script even with -e?

### 2. Handle cleanup with traps
`trap ... EXIT` is useful for removing temporary files, even on many error paths. Traps do not run on SIGKILL or a system crash. Keep cleanup paths narrow and validated.

```bash
work=$(mktemp -d)
cleanup() { rm -f -- "$work/output.tmp"; }
trap cleanup EXIT
printf 'demo\n' > "$work/output.tmp"
ls -l "$work/output.tmp"
```

**Verify:** Why must cleanup code use quoted, controlled paths?

### 3. Write atomically where feasible
For single-filesystem replacement, write a complete temporary file in the target directory, validate it, then rename it. Atomic rename is not the same as crash-durable storage; fsync behavior matters for stronger guarantees.

```bash
destination="$work/report.txt"
tmp=$(mktemp "$destination.tmp.XXXXXXXX")
printf 'status=ok\n' > "$tmp"
mv -- "$tmp" "$destination"
cat "$destination"
```

**Verify:** Why should the temporary file be on the destination filesystem?

### 4. Classify failures
Expected invalid input can be a handled nonzero status; unavailable dependencies and corrupted files should not be silently ignored with `|| true`. Use explicit conditionals and error reporting.

```bash
if command -v sha256sum >/dev/null; then echo 'hash tool present'; else echo 'missing hash tool' >&2; fi
if [[ ! -f "$work/nope" ]]; then echo 'missing input detected'; fi
```

**Verify:** How would you test cleanup when a mid-operation command fails?

## Practice
1. Write a trap that cleans temporary files on failure.
2. Implement a temp-write-and-rename pattern.
3. Document three cases where errexit behaves unexpectedly.

## Interview questions
- Is set -e a complete exception-handling system?
- How does `trap EXIT` differ from guaranteed crash recovery?

**Production caution:** Never use broad rm -rf in cleanup traps.

**Pass condition:** Show a normal case, failure case and explanation of exit status and side effects.
