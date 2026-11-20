# grep, sed, awk, and structured text processing

**Intermediate · Lesson 05 · 75–110 minutes**

## Learning outcome
Choose a tool appropriate for the data format; process large logs in a streaming manner.

Practice in Bash on Linux or WSL2. Examples use disposable files, and no sudo or internet connection is required.

### 1. Use grep precisely
grep -F matches a literal sequence and grep -E supports patterns. Use -q for existence without output, -n for line numbers, and -- to stop option parsing when patterns begin with -.

```bash
work=$(mktemp -d)
printf 'INFO ready\nERROR timeout\nINFO done\n' > "$work/app.log"
grep -nF ERROR "$work/app.log"
grep -E '^(INFO|ERROR)' "$work/app.log"
```

**Verify:** Why might a broad regex match unrelated messages?

### 2. Transform with sed
sed applies line-oriented substitutions and selections. Escape regex metacharacters correctly; never assume `sed -i` is identically portable across GNU/BSD systems.

```bash
printf 'host=dev\nhost=prod\n' | sed 's/^host=/node=/'
sed -n '2p' "$work/app.log"
```

**Verify:** What input validation is needed when replacement text comes from a user?

### 3. Aggregate with awk
awk can filter rows and maintain counters in one pass. The script must define field separators; splitting on whitespace does not correctly parse quoted CSV.

```bash
awk '$1=="ERROR"{n++} END{print n+0}' "$work/app.log"
awk '{c[$1]++} END{for(k in c)print k,c[k]}' "$work/app.log" | sort
```

**Verify:** Can a simple awk script handle JSON nesting safely?

### 4. Combine with predictable sorting
Sort order depends on locale. When output forms part of an API or test assertion, set LC_ALL=C and add deterministic tie-break rules.

```bash
printf 'b\na\nb\n' | LC_ALL=C sort | uniq -c
printf 'z\nA\na\n' | LC_ALL=C sort
```

**Verify:** Why can production sorting differ across machines?

## Practice
1. Count error rows for a fixed log schema.
2. Calculate request counts by IP from access logs.
3. Explain why CSV with quoted fields needs a real parser.

## Interview questions
- When does grep return exit status 1?
- Why is combining sort and uniq common?

**Production caution:** Related labs: I02 and I03.

**Pass condition:** Show a normal case, failure case and explanation of exit status and side effects.
