# Intermediate — 20 interview questions

Explain each answer using a command, log line, configuration example, or failure scenario from the course.

1. **How do you preserve all Bash positional arguments?** Use quoted `"$@"`; it retains each supplied argument as a distinct shell word.

2. **What is the purpose of a shebang?** It identifies the interpreter used when a script is executed directly.

3. **How do Bash functions return text?** Usually by printing to stdout or assigning via a variable; `return` is for numeric exit status.

4. **When should a script use stderr?** For diagnostics and errors; keep stdout stable for data consumers.

5. **Why does `[[ ]]` differ from `[ ]`?** `[[ ]]` is Bash syntax with different expansion and pattern behavior; `[ ]` is test command syntax with POSIX variants.

6. **Why test numeric input before arithmetic?** To reject invalid strings and avoid unexpected shell arithmetic evaluation or numeric ambiguity.

7. **What is the problem with `for f in $(find ...)`?** Command substitution and word splitting destroy filename boundaries; use NUL-delimited find/read or xargs.

8. **When does `set -e` not exit?** In several tested conditional contexts, negations and compound constructs; do not treat it as complete error handling.

9. **Why use a trap EXIT?** To run cleanup on normal and many error exits; it is not guaranteed after SIGKILL or power failure.

10. **How do you publish a file atomically?** Write a complete temporary file in the same destination filesystem, validate it, then rename to final path.

11. **Does atomic rename guarantee crash durability?** No. Stronger persistence may require flushing file and directory metadata.

12. **What is the difference between memory free and available?** Available estimates memory usable without heavy swapping, including reclaimable caches.

13. **Why can a filesystem report ENOSPC with free disk blocks?** Inodes, quotas, or other filesystem constraints can be exhausted.

14. **What does load average count on Linux?** Roughly runnable tasks plus certain uninterruptible-waiting tasks over windows; not simply CPU percent.

15. **What is the purpose of rsync --dry-run?** Show proposed transfers/changes without applying them, allowing destination and delete-policy review.

16. **Why verify SSH host keys?** To detect impersonation and help prevent man-in-the-middle attacks.

17. **Why do cron jobs need explicit paths?** Scheduler environments and working directories differ from interactive shells.

18. **How does systemd differ from nohup?** systemd supervises lifecycle, dependencies, restart, logging and resource policy; nohup mainly changes hangup signal behavior.

19. **What does ss -ltn show?** Listening TCP sockets, not proof that an external client can connect successfully.

20. **DNS works but curl times out: next checks?** Verify resolved addresses, route, firewall/security rules, listener bind and TCP connectivity before blaming HTTP.

**Review standard:** Explain a practical example and one unsafe shortcut for at least 16/20 questions.
