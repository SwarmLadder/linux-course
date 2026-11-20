# Basics — 25 exercises

Practice independently after the corresponding [lesson track](../basics/README.md). Document commands, outputs, failures and assumptions. Do not perform privileged or destructive work against real systems.

1. Print shell name, Bash version, kernel version, and current user without dumping the environment.
2. Explain the difference among terminal emulator, shell, external program, and kernel with concrete examples.
3. Create a disposable directory with nested logs/, data/, cache/ and list all directories.
4. Write a text file with three newline-terminated records using printf; report bytes and lines.
5. Navigate from a nested directory back to the workspace root using a relative path.
6. Find two files by their names without parsing ls output.
7. Copy a file to a new name and compare inode numbers.
8. Create a symbolic link and read its target; break it intentionally and explain the result.
9. Create a hard link and explain reference counts after deleting one filename.
10. Filter only ERROR-level lines from a whitespace log; ignore 'error' in message text.
11. Count lines matching a literal period using grep -F, not regex syntax.
12. List first and last five lines of a 30-line synthetic log.
13. Use awk to count levels INFO, WARN and ERROR and sort output deterministically.
14. Demonstrate how word splitting changes arguments for a value containing spaces.
15. Write a single-quoted and double-quoted example that expands a variable differently.
16. Enumerate filenames containing spaces through find -print0 and read -d.
17. Redirect stdout to one file and stderr to another, recording the process status.
18. Build a pipeline that fails upstream; compare status with and without pipefail.
19. Create a 600-mode private file and explain its effective permissions.
20. Compare permissions of a file and directory created under umask 077.
21. Export a variable into one child Bash process; show an unexported variable is absent.
22. Inspect PATH and explain how Bash selects among duplicate command names.
23. Start a background sleep, capture its PID, and collect its exit code using wait.
24. Create a tar.gz from a temporary directory, restore into a second location, and compare bytes.
25. Complete labs B01–B04 and document the failure cases for each.

**Completion:** At least 20/25 solutions reproducible in a fresh disposable environment; no secrets, system changes or unverified destructive steps.
