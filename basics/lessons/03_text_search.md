# Read, filter, and summarize text

**Basics · Lesson 03 · 60–90 minutes**

## Goal
Use head, tail, grep, awk, and wc on predictable log formats without hiding malformed records.

Use a Linux shell or WSL2. These examples inspect the system or write inside disposable temporary paths.

### 1. Preview before processing
Use head/tail to see representative records and wc to count lines. For live logs, tail -f stays attached until interrupted; do not use it when a bounded snapshot is needed.

```bash
work=$(mktemp -d)
printf 'INFO start\nERROR timeout\nINFO retry\n' > "$work/app.log"
head -n 2 "$work/app.log"
tail -n 1 "$work/app.log"
wc -l "$work/app.log"
```

**Verify:** A line count depends on line terminators.

### 2. Literal versus regex grep
grep -F searches literally; grep -E uses extended regex. Anchoring can prevent unrelated text from matching. Exit status 1 means no matches, not necessarily a command error.

```bash
grep -nF 'ERROR' "$work/app.log"
grep -En '^(INFO|ERROR)' "$work/app.log"
grep -qF 'FATAL' "$work/app.log" || echo 'no fatal records'
```

**Verify:** When is regex unnecessarily risky?

### 3. Extract structured fields
awk is useful for whitespace-delimited fields and numeric aggregation. It does not correctly parse general CSV containing quoted commas. Define the log contract before indexing columns.

```bash
awk '$1=="ERROR"{print $2}' "$work/app.log"
awk '{count[$1]++} END{for(k in count)print k,count[k]}' "$work/app.log" | sort
```

**Verify:** What happens if the log format changes columns?

### 4. Inspect underlying bytes
Text may contain CRLF, UTF-8 multibyte characters, or binary bytes. Use file and od to inspect ambiguous inputs before transforming huge files with shell filters.

```bash
file "$work/app.log"
od -An -t x1 -N 20 "$work/app.log"
LC_ALL=C wc -c < "$work/app.log"
```

**Verify:** Why are bytes and characters different measures?

## Independent practice
1. Count records with the exact level ERROR.
2. Extract unique values and explain sort -u.
3. Handle a zero-match search without treating it as a crash.

## Interview checks
- How does grep -F differ from grep -E?
- Why is awk not a full CSV parser?

**Safety:** Related graded labs: B01 and B02.

**Ready when:** You can explain each command's input, output, exit status, and a failure case.
