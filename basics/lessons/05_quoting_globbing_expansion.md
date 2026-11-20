# Quoting, word splitting, and safe filename loops

**Basics · Lesson 05 · 60–90 minutes**

## Goal
Prevent shell expansion bugs caused by spaces, wildcard characters, and unexpected input.

Use a Linux shell or WSL2. These examples inspect the system or write inside disposable temporary paths.

### 1. Quote variables
A quoted expansion usually becomes one argument; an unquoted expansion can be split and filename-expanded. Shell code must handle arbitrary user filenames rather than assuming no spaces.

```bash
value='two words'
printf '<%s>\n' "$value"
printf '<%s>\n' $value
```

**Verify:** Compare printed arguments and count them.

### 2. Single vs double quotes
Single quotes suppress parameter expansion. Double quotes allow expansions while preserving words. Command substitution strips trailing newline characters, which can be important for binary data.

```bash
name='Ada'
printf '%s\n' '$name' "$name"
answer=$(printf 'hello\n')
printf '<%s>\n' "$answer"
```

**Verify:** Why does the literal string $name survive inside single quotes?

### 3. Globs and missing matches
A glob is expanded by the shell in matching contexts, but it is not recursive by default. Bash may leave unmatched globs as literal text; don't assume a pattern always finds files.

```bash
work=$(mktemp -d)
touch "$work/a.log" "$work/b.txt"
find "$work" -maxdepth 1 -type f -name '*.log' -printf '%f\n'
```

**Verify:** Explain the difference between the quoted find pattern and shell-expanded *.log.

### 4. Use NUL delimiters for files
Unix filenames may contain spaces, tabs, and newlines; they cannot contain NUL. For comprehensive file traversal, pair find -print0 with `read -r -d ''` or xargs -0.

```bash
touch "$work/name with spaces.txt"
while IFS= read -r -d '' item; do
 printf 'found=%s\n' "$item"
done < <(find "$work" -type f -print0)
```

**Verify:** Why does `for f in $(find ...)` lose filename boundaries?

## Independent practice
1. Create and handle a path containing spaces.
2. Demonstrate the difference between single and double quotes.
3. Use find -print0 to enumerate files safely.

## Interview checks
- What is word splitting?
- Why do unmatched glob patterns need consideration?

**Safety:** Never parse ls output for scripting.

**Ready when:** You can explain each command's input, output, exit status, and a failure case.
