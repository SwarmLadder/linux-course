# stdin, stdout, stderr, and pipelines

**Basics · Lesson 04 · 60–90 minutes**

## Goal
Compose Unix tools while checking which stage failed and where error messages go.

Use a Linux shell or WSL2. These examples inspect the system or write inside disposable temporary paths.

### 1. Three standard streams
stdin=0, stdout=1, stderr=2. Redirecting one stream does not redirect the others. Keep error output visible while generating reports.

```bash
work=$(mktemp -d)
printf 'one\ntwo\n' > "$work/lines.txt"
wc -l < "$work/lines.txt"
ls /path-that-is-not-present 2> "$work/errors.txt" || :
cat "$work/errors.txt"
```

**Verify:** Why should operational errors not be mixed into parseable stdout?

### 2. Build pipelines
A pipe sends the previous command's stdout to the next command's stdin. Pipes avoid unnecessary temporary files, but each stage can fail independently.

```bash
printf 'B\na\nB\n' | sort | uniq -c
printf '1\n2\n3\n' | awk '{s+=$1} END{print s}'
```

**Verify:** Why does uniq require adjacent equal rows?

### 3. Preserve failure status
By default a pipeline often reports only the last command status. Bash's pipefail reports an upstream failure. Use it where later stages must not conceal missing input or failed producers.

```bash
set -o pipefail
if (false | cat >/dev/null); then echo ok; else echo failed; fi
set +o pipefail
if (false | cat >/dev/null); then echo ok; else echo failed; fi
```

**Verify:** Compare outputs of both conditionals.

### 4. Choose append or replace
`>` replaces target contents while `>>` appends. Always check destination paths. Write logs without secrets and include stable fields if automation will consume them.

```bash
printf 'event=start\n' > "$work/events.log"
printf 'event=stop\n' >> "$work/events.log"
cat "$work/events.log"
```

**Verify:** What happens if a crash occurs halfway through a report write?

## Independent practice
1. Capture stdout and stderr separately.
2. Count unique values using a pipeline.
3. Show a failing upstream process hidden without pipefail.

## Interview checks
- What does `2>&1` mean?
- What exit status does a pipeline return with pipefail?

**Safety:** Avoid piping untrusted network scripts directly into Bash.

**Ready when:** You can explain each command's input, output, exit status, and a failure case.
