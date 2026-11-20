# Basics project: log inspection and reporting

**Basics · Lesson 11 · 60–90 minutes**

## Goal
Combine text filtering, counting, sorting and file handling into a verifiable service-log report.

Linux/WSL2 shell recommended. Examples are read-only or work with disposable files.

### 1. Define a log contract
A predictable log format makes simple shell processing possible. A structured field named ERROR is different from a message that merely includes the word error.

```bash
work=$(mktemp -d)
printf '2026 INFO user=ana\n2026 ERROR user=bob\n2026 ERROR user=ana\n' > "$work/app.log"
awk '$2=="ERROR"{n++}END{print n+0}' "$work/app.log"
```

**Check:** State which field stores log level before writing a query.

### 2. Extract and deduplicate users
Keep parsing assumptions explicit; whitespace-based awk fails if values contain spaces or escaping. Production JSON logs should be parsed with a JSON-aware tool.

```bash
awk '{for(i=1;i<=NF;i++)if($i~/^user=/){split($i,p,"=");print p[2]}}' "$work/app.log" | LC_ALL=C sort -u
wc -l < "$work/app.log"
```

**Check:** Sort order must be explicit for stable test output.

### 3. Write a machine-readable report
Generate metric=value output without destroying the source. Redirect stdout into a new report file; leave errors on stderr for callers to detect.

```bash
{ printf 'records='; wc -l < "$work/app.log";
  printf 'errors='; awk '$2=="ERROR"{n++}END{print n+0}' "$work/app.log";
} > "$work/report.txt"
cat "$work/report.txt"
```

**Check:** Which commands need failure handling before reporting success?

### 4. Verify with two test fixtures
A single sample is not proof of correctness. The course grader checks your starter solution against two datasets, including changed counts and distinct users.

```bash
python tools/grade.py --list
python tools/grade.py B01
python tools/grade.py B02
```

**Check:** The starter files fail until you implement them. Compare the reference only after attempting.

## Independent practice
1. Complete graded B01 and B02 using Bash.
2. Handle an empty log and unexpected fields.
3. Write a README explaining input/output, status codes and limitations.

## Interview checks
- Why avoid using grep -c error blindly?
- How would you test a log reporting script?

**Safety:** The project uses synthetic logs; never publish personal production logs.

**Complete when:** You can explain input, output, exit status, and one failing case.
