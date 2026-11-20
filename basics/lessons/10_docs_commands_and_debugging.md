# Manual pages, command inspection, and troubleshooting

**Basics · Lesson 10 · 60–90 minutes**

## Goal
Find authoritative local help and troubleshoot the environment before using risky changes.

Linux/WSL2 shell recommended. Examples are read-only or work with disposable files.

### 1. Read help for the right command
`--help` is common for external programs, `help` documents Bash builtins, and `man` provides manuals where installed. Exact flags differ by distribution and tool versions.

```bash
help test | head -n 15
bash --version | head -n 1
command -v man || echo 'man unavailable'
```

**Check:** How would you find Bash-specific behavior of test or printf?

### 2. Locate the executable
type -a and command -v show command resolution. A familiar name might resolve to a function, alias or different version. Check version details during incident triage.

```bash
type -a awk
command -v sed
readlink -f "$(command -v bash)"
```

**Check:** Why should an incident report record the exact program version?

### 3. Inspect package ownership
Debian and RPM distributions use different package tools. Read-only checks help identify installed components, but this lesson does not modify system packages.

```bash
if command -v dpkg-query >/dev/null; then dpkg-query -S "$(command -v bash)" || :; fi
if command -v rpm >/dev/null; then rpm -qf "$(command -v bash)" || :; fi
```

**Check:** What might be different on an Alpine-based container?

### 4. Build a minimal reproduction
Inspect input shape, exit code, locale and file permissions before changing global settings. A useful bug report includes exact steps, observed output, and expected behavior, without leaked secrets.

```bash
printf 'PATH=%s\n' "$PATH"
locale | head -n 6
id
command -v grep
```

**Check:** Why is a concise reproducible example better than guessing a permission fix?

## Independent practice
1. Find help for find -print0 and read -d.
2. Document steps to reproduce a failing command.
3. Compare commands on Ubuntu and Alpine.

## Interview checks
- When should you use `help` rather than `man`?
- Why avoid piping arbitrary installers into Bash?

**Safety:** No package installation or root privileges required.

**Complete when:** You can explain input, output, exit status, and one failing case.
