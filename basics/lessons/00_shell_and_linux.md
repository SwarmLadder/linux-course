# Shell, terminal, and Linux processes

**Basics · Lesson 00 · 60–90 minutes**

## Goal
Explain what executes a command and how to identify the current environment.

Use a Linux shell or WSL2. These examples inspect the system or write inside disposable temporary paths.

### 1. Understand execution layers
A terminal is the interface; Bash parses your command line; programs request kernel services for files, networking, and processes. Shell builtins and external executables differ because builtins run in the current shell.

```bash
uname -srm
bash --version | head -n 1
type cd
type ls
```

**Verify:** Why can `cd` change the parent shell directory while an external child cannot?

### 2. Inspect current identity
Commands act with the privileges of the current user and groups. Inspect identity before touching files. The root user is not required anywhere in the local labs; sudo is not a general error-recovery method.

```bash
id
whoami
pwd
printf 'HOME=%s\n' "$HOME"
```

**Verify:** Identify a user ID, groups and current directory.

### 3. Find commands safely
Bash looks up external executables using PATH. Check command type and location rather than assuming a name resolves to a trusted program. Aliases and functions can override expected behavior.

```bash
type -a printf
type -a grep
command -v awk
printf '%s\n' "$PATH" | tr ':' '\n'
```

**Verify:** What risks arise if an attacker-controlled directory appears first on PATH?

### 4. Observe exit status
Most Unix commands return status zero for success and nonzero for failure. stdout and stderr are separate from this status. Scripts should test the exit code when correctness depends on a command succeeding.

```bash
true; printf 'true=%s\n' "$?"
false; printf 'false=%s\n' "$?"
if command -v python3 >/dev/null; then echo 'Python found'; fi
```

**Verify:** Distinguish silent success from silent failure.

## Independent practice
1. Explain kernel vs shell vs terminal.
2. Write a read-only environment report.
3. Demonstrate a failed command handled by an if condition.

## Interview checks
- What is the process exit status used for?
- Why should developers verify PATH?

**Safety:** Use Linux or WSL2; GNU command options may differ on macOS.

**Ready when:** You can explain each command's input, output, exit status, and a failure case.
