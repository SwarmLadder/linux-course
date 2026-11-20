# Bash scripts, arguments, and execution

**Intermediate · Lesson 00 · 75–110 minutes**

## Learning outcome
Turn terminal snippets into repeatable programs with clear command-line contracts.

Practice in Bash on Linux or WSL2. Examples use disposable files, and no sudo or internet connection is required.

### 1. Choose interpreter and file format
A Bash script begins with a shebang when executed directly. `bash script.sh` selects Bash explicitly; `./script.sh` requires executable permission and a valid interpreter path. Do not assume a .sh extension guarantees Bash syntax.

```bash
work=$(mktemp -d)
printf '#!/usr/bin/env bash\nprintf "hello\\n"\n' > "$work/run.sh"
bash "$work/run.sh"
chmod u+x "$work/run.sh"
"$work/run.sh"
```

**Verify:** Why might `/bin/sh script.sh` behave differently?

### 2. Access positional arguments
`$0` names invocation, `$1` the first argument, and `$#` the number of arguments. Always validate counts before using values. Use `"$@"` to preserve separate arguments, including spaces.

```bash
printf '#!/usr/bin/env bash\nprintf "count=%%s\\n" "$#"\nprintf "arg=%%s\\n" "$@"\n' > "$work/args.sh"
bash "$work/args.sh" one 'two words'
```

**Verify:** Why is `"$*"` not interchangeable with `"$@"`?

### 3. Return useful exit codes
A CLI should return 0 on success and nonzero for invalid input or unavailable resources. Errors belong on stderr; use `printf ... >&2`. Document usage and avoid generating success output before validation.

```bash
printf '#!/usr/bin/env bash\n[[ $# -eq 1 ]] || { echo "usage: script FILE" >&2; exit 2; }\n' > "$work/one.sh"
bash "$work/one.sh" || echo 'bad arguments'
```

**Verify:** Explain how callers can distinguish failure from empty successful output.

### 4. Choose executable location
A script may run from any working directory. Use absolute or explicitly resolved paths for resources; avoid assuming the current directory equals the script directory.

```bash
cd /tmp
bash "$work/args.sh" example
pwd
```

**Verify:** How can scheduled execution change the working directory?

## Practice
1. Write a script that requires exactly two arguments.
2. Preserve a filename with spaces passed as one argument.
3. Test both valid and invalid invocation statuses.

## Interview questions
- What does `$@` preserve?
- Why is a shebang still useful if scripts can run with bash?

**Production caution:** A shell script's user input must not be inserted into eval.

**Pass condition:** Show a normal case, failure case and explanation of exit status and side effects.
