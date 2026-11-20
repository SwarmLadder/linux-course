# Bash functions, local variables, and error propagation

**Intermediate · Lesson 03 · 75–110 minutes**

## Learning outcome
Build reusable functions with explicit inputs, outputs, return codes and small side effects.

Practice in Bash on Linux or WSL2. Examples use disposable files, and no sudo or internet connection is required.

### 1. Define narrow functions
A Bash function can return a status code, but not an arbitrary string through `return`; text output is normally sent through stdout or captured by command substitution. Limit one function to one responsibility.

```bash
greet() { local person=$1; printf 'hello %s\n' "$person"; }
greet 'Ada Lovelace'
```

**Verify:** Why is printing a result different from returning a status?

### 2. Avoid global variable collisions
Without `local`, shell function assignments may alter global variables unexpectedly. Local variables reduce hidden state and make tests independent.

```bash
name=outer
update() { local name=inner; printf 'inside=%s\n' "$name"; }
update
printf 'outside=%s\n' "$name"
```

**Verify:** How does this compare with a Python function's local scope?

### 3. Handle invalid input
Check argument count and shape before writing files or invoking network commands. Return a nonzero status and send diagnostics to stderr so callers can programmatically detect failure.

```bash
require_file() { [[ $# -eq 1 && -f $1 ]] || { echo 'file required' >&2; return 2; }; }
work=$(mktemp -d)
if require_file "$work/missing"; then echo ok; else echo 'input rejected'; fi
```

**Verify:** Why is a clear exit code part of a function contract?

### 4. Compose and test functions
Separate parsing, validation, calculation and output. Test both successful and unsuccessful calls. Avoid functions that silently change current directories or global shell options.

```bash
is_positive() { [[ $1 =~ ^[0-9]+$ ]] && (( 10#$1 > 0 )); }
if is_positive 20; then echo yes; fi
if ! is_positive 0; then echo 'zero rejected'; fi
```

**Verify:** Bash arithmetic requires validated values to avoid injection-like evaluation problems.

## Practice
1. Write a function counting matching records in a file.
2. Return a distinct error code for missing input.
3. Test local variable isolation.

## Interview questions
- How does `return 3` differ from printing 3?
- When should a Bash function write to stderr?

**Production caution:** Avoid eval and executing arbitrary user-provided strings.

**Pass condition:** Show a normal case, failure case and explanation of exit status and side effects.
