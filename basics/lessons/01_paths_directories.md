# Filesystem layout and safe navigation

**Basics · Lesson 01 · 60–90 minutes**

## Goal
Navigate absolute and relative paths, resolve links, and keep experiments inside disposable directories.

Use a Linux shell or WSL2. These examples inspect the system or write inside disposable temporary paths.

### 1. Understand Linux paths
Absolute paths begin at /; relative paths begin in the current working directory. /etc usually contains system configuration, /var changing data, and /home user directories. Production services may have different working directories.

```bash
pwd
ls -ld / /etc /var "$HOME"
readlink -f .
```

**Verify:** Why does a relative path fail when a scheduler starts a script elsewhere?

### 2. Work in isolation
mktemp -d creates a new private temporary directory. Quote its path: filenames and directories can contain spaces. Keep track of the path rather than assuming /tmp contents are yours.

```bash
work=$(mktemp -d)
mkdir -p -- "$work/app/logs"
printf '%s\n' "$work"
find "$work" -maxdepth 2 -type d
```

**Verify:** Explain why mkdir -p is useful when creating nested paths.

### 3. Move through paths
cd changes the active directory in the current shell. Dot means current directory, two dots mean parent directory. `pwd -P` resolves physical path components rather than relying only on logical symlinked paths.

```bash
cd -- "$work/app"
pwd
cd logs
pwd -P
cd ..
```

**Verify:** Predict the directory before each pwd call.

### 4. Test path types
Before reading or writing, test a path's expected type. `-d`, `-f`, and `-L` test directory, regular file, and symlink. A successful existence test alone cannot prevent concurrent path replacement.

```bash
[[ -d "$work/app" ]] && echo 'directory'
[[ ! -f "$work/missing" ]] && echo 'missing file'
ls -ld -- "$work/app"
```

**Verify:** Why might symlinks require special care in privileged scripts?

## Independent practice
1. Build a nested tree in a temporary directory.
2. Explain relative vs absolute path resolution.
3. Check for a missing input file before reading it.

## Interview checks
- What does `..` mean at filesystem root?
- How does a symlink change path interpretation?

**Safety:** Do not run deletion commands on guessed paths.

**Ready when:** You can explain each command's input, output, exit status, and a failure case.
