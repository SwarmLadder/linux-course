# Final assessment — Linux, Bash & Backend Operations

## Deliverables

1. Complete all **12 graded Bash labs** on two fixtures each.
2. Submit three projects with contracts, example runs and failure tests.
3. Explain 48 of the 60 interview questions without notes.
4. Reproduce a service incident diagnosis and an isolated backup restore.

## Rubric (100 points)

| Category | Points |
|---|---:|
| Linux fundamentals and safe commands | 20 |
| Bash input validation and correctness | 20 |
| Backend networking and processes | 15 |
| Operational recovery and reliability | 20 |
| Automated tests and edge cases | 15 |
| Explanations and documentation | 10 |

**Suggested passing threshold:** 80/100; no secrets exposed, unauthorized network activity, or destructive work on real systems.

## Validation

```bash
python tools/grade.py --verify-references
python -m unittest discover -s tests -v
```

Passing the reference tests is a course validation, not a substitute for independently completing the starter files.
