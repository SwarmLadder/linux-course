# Basics — 20 interview questions

Explain each answer using a command, log line, configuration example, or failure scenario from the course.

1. **What is the difference between a terminal, shell and kernel?** A terminal provides an interface, a shell parses/executes commands, and the kernel manages system resources through system calls.

2. **What does exit status 0 mean?** By convention the command succeeded. Nonzero signals failure or a status meaningful to the program; always check its documented contract.

3. **What are stdin, stdout and stderr?** File descriptors 0, 1 and 2: input, normal output and diagnostics. Redirection can control them independently.

4. **How do absolute and relative paths differ?** Absolute begins at filesystem root /; relative is resolved against the current working directory.

5. **What does the execute permission on a directory allow?** Traversal of directory components; listing also generally needs read permission.

6. **What is an inode?** Filesystem object containing metadata and pointers for data. Directory entries map names to inode identities.

7. **Hard link versus symlink?** Hard links share an inode; symlinks refer to a path. Hard links normally cannot span filesystems.

8. **Why quote variables in Bash?** Quoted expansions preserve argument boundaries and avoid unwanted word splitting and pathname expansion.

9. **What is a pipeline?** One command's stdout feeds another's stdin. Pipeline status behavior depends on pipefail.

10. **Why use `set -o pipefail`?** So failure of an upstream pipeline stage is not masked by success from the last command.

11. **What does `grep -F` do?** Matches a fixed literal string, unlike regex patterns that interpret special characters.

12. **What does `awk` do well?** Line/field filtering and simple aggregation for well-defined text formats; not general parsing of quoted CSV or JSON.

13. **Why use find -print0?** NUL separates arbitrary Unix filenames safely, including those containing spaces or newlines.

14. **How do you find executable resolution?** Use `type -a` and `command -v`; inspect PATH and possible aliases/functions.

15. **How do `>` and `>>` differ?** `>` replaces/truncates target output; `>>` appends to it.

16. **What does a process PID identify?** A currently allocated process identifier; PIDs may be reused after processes exit.

17. **What does wait do?** Collects background child completion and its exit status, helping prevent orphaned lifecycle handling.

18. **What is umask?** A mask that removes permission bits from default creation modes of new files/directories.

19. **What is the difference between tar and gzip?** tar archives multiple files; gzip compresses a stream, often a tar archive.

20. **Is a checksum proof of authenticity?** No. It verifies integrity relative to a trusted expected digest; an attacker can replace both file and digest.

**Review standard:** Explain a practical example and one unsafe shortcut for at least 16/20 questions.
