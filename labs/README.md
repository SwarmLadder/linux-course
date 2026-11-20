# 12 Graded Bash Labs

Use Python 3.10+, Bash, and Linux/GNU utilities. Each task has a starter and a reference implementation.

```bash
python tools/grade.py --list
python tools/grade.py B01
python tools/grade.py --verify-references
```

The checker runs your trusted local starter Bash file against **two different fixtures**, comparing stdout, exit codes and file side effects where relevant.

| Level | Labs |
|---|---|
| Basics | B01 error counts · B02 unique users · B03 bytes in directory · B04 find text paths |
| Intermediate | I01 port validation · I02 requests by IP · I03 mean latency · I04 atomic copy |
| Advanced | A01 SHA256 manifest · A02 p90 latency · A03 failed units · A04 log rotation |

Start in [starter/](starter/), compare with [reference/](reference/) only after trying, and inspect task descriptions in [tasks.json](tasks.json).

**Warning:** This tool executes student-authored local Bash code. It is for your own trusted scripts, not a sandbox for unknown code from the internet. No root/network access is required by the reference tasks.
