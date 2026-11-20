# Bash variables, environment, and PATH

**Basics · Lesson 07 · 60–90 minutes**

## Goal
Manage shell variables and exported values without exposing credentials or shadowing trusted executables.

Linux/WSL2 shell recommended. Examples are read-only or work with disposable files.

### 1. Use assignments correctly
Bash assignments have no spaces around =. Expansions should be quoted, especially in paths and messages. Variables are shell-local unless exported or passed to child commands.

```bash
course='Linux operations'
printf '%s\n' "$course"
export COURSE_LEVEL=basics
bash -c 'printf "child=%s\n" "$COURSE_LEVEL"'
```

**Check:** Why does a child normally not see an unexported local variable?

### 2. Inspect PATH
PATH is a colon-delimited directory search list for commands. An untrusted path before system directories could execute a malicious program. Use command -v and type -a to understand resolution.

```bash
printf '%s\n' "$PATH" | tr ':' '\n'
command -v bash
type -a grep
```

**Check:** When should an absolute executable path be used?

### 3. Use defaults and required fields
Parameter expansion can provide fallbacks when variables are unset/empty. A script can reject absent required values. Avoid logging complete environments; they often contain service tokens.

```bash
unset OPTIONAL || :
printf 'mode=%s\n' "\${OPTIONAL:-safe}"
required=present
printf 'required=%s\n' "\${required:?missing}"
```

**Check:** How does an empty value differ from an unset value for parameter defaults?

### 4. Set environment for one command
Assignment preceding an executable changes its environment without modifying persistent shell settings. Locale affects sort order and number formatting; deterministic scripts often set LC_ALL=C.

```bash
LC_ALL=C sort <<< $'b\na\n'
printenv HOME
if printenv COURSE_LEVEL >/dev/null; then echo 'exported'; fi
```

**Check:** Why can a test pass on one locale but fail on another?

## Independent practice
1. Write a script requiring a configuration variable.
2. Inspect a command's path and type.
3. Explain how PATH shadowing can alter behavior.

## Interview checks
- How are shell variables and environment variables related?
- Why is an environment variable not secure storage?

**Safety:** Never print passwords, access tokens or full environment dumps.

**Complete when:** You can explain input, output, exit status, and one failing case.
