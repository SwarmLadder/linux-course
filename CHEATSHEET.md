# Linux command cheat sheet

| Task | Command | Watch out for |
|---|---|---|
| Locate yourself | `pwd`, `id`, `whoami` | Different users/working directories |
| Inspect files | `ls -l`, `stat`, `file` | Symlinks and ownership |
| Search text | `grep -nF PATTERN file` | Literal versus regular expression |
| Extract fields | `awk '{print $1}' file` | Whitespace is not quoted CSV |
| Discover files | `find DIR -type f -print0` | Path delimiters and symlinks |
| Copy safely | `cp -- SRC DEST` | Existing destination overwrite |
| Inspect permissions | `stat -c '%a %U:%G' file` | ACLs can alter effective access |
| Check processes | `ps -eo pid,ppid,stat,comm` | PIDs can be reused |
| CPU/load | `uptime`, `top` | Load is not CPU percentage |
| Memory | `free -h` | Available differs from free |
| Disk | `df -h`, `df -i`, `du -sh` | Full inodes can block writes |
| Sockets | `ss -ltn` | Local bind != remote reachability |
| DNS | `getent hosts NAME` | DNS success != TCP success |
| Logs | `journalctl -u UNIT` | Systemd availability/permissions |
| Archive | `tar -czf archive.tar.gz -C DIR NAME` | Untrusted extraction paths |
| Integrity | `sha256sum -c manifest` | Trust the expected digest |
| Bash syntax | `bash -n script.sh` | Not a runtime test |
| Strict pipeline | `set -o pipefail` | Understand conditional exceptions |
| Safe cleanup | `trap cleanup EXIT` | Not guaranteed after SIGKILL |

For operational incidents, **inspect before modifying**. Never use broad permission or deletion commands to guess at a fix.
