# Project 1 — Log analytics CLI

**Goal:** Analyze structured synthetic backend logs from the terminal and return reproducible counts.

## Contract

Input: one UTF-8 log path. Rows contain a timestamp-like field, a level, and optional user=NAME field. Output should include records, errors (level exactly ERROR), and distinct nonempty user names.

## Deliverables

1. Implement a Bash CLI that validates one file argument and reports errors to stderr.
2. Count only rows with second field exactly ERROR; avoid counting messages that merely mention ERROR.
3. Count distinct user=NAME values without including empty names.
4. Handle an empty file and paths containing spaces.
5. Add tests for malformed rows and predictable sorting.

## Try the reference

```bash
printf '2026 INFO user=ana\n2026 ERROR user=bob\n' > /tmp/course-sample.log
bash projects/examples/log_summary.sh /tmp/course-sample.log
```

**Expected:** records=2, errors=1, unique_users=2.

**Extensions:** emit JSON safely using a real JSON encoder; support date filtering; compare a streaming approach with loading all lines.

**Interview:** Explain why awk is appropriate for a fixed whitespace schema but not a general JSON/CSV parser.
