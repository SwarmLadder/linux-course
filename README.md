# Linux, Bash & Backend Operations

Practical Linux training for backend developers, SRE beginners, and technical interviews.

| Material | Total |
|---|---:|
| Detailed guided lessons | **36** |
| Independently graded Bash labs | **12** |
| Additional independent practice questions | **75** |
| Portfolio projects | **3** |
| Interview questions with concise answers | **60** |

## Learning paths

- [Basics](basics/README.md) — shell, filesystem, streams, permissions, process fundamentals.
- [Intermediate](intermediate/README.md) — reliable Bash, awk/find, monitoring, SSH, scheduling, networking, releases.
- [Advanced](advanced/README.md) — systemd, Linux security, containers, filesystems, observability, diagnosis and recovery.

## Start locally

**Requirements:** Linux or WSL2; Bash, GNU core utilities, Python 3.10+ for grading. No server, Docker, credentials or sudo needed for graded labs.

```bash
git clone https://github.com/SwarmLadder/linux-course.git
cd linux-course
python tools/grade.py --list
python tools/grade.py B01
```

Implement `labs/starter/b01_count_errors.sh` and rerun. The starter fails until completed. After attempting a lab, compare [reference implementations](labs/reference/).

```bash
python tools/grade.py --verify-references
python -m unittest discover -s tests -v
```

## Further learning

- [Three portfolio projects](projects/README.md)
- [75 additional exercises](exercises/README.md)
- [Interview preparation and 3 mock rounds](interview/README.md)
- [Four-week curriculum](CURRICULUM.md)
- [Command cheat sheet](CHEATSHEET.md) and [glossary](GLOSSARY.md)
- [Course safety rules](SAFETY.md)

**Safety:** System-level production commands are illustrative, not automatically run. Only local trusted Bash scripts are executed by the practice grader. The grader uses disposable files but is **not a security sandbox**.

[MIT License](LICENSE).
