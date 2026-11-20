# Contributing

Keep lessons technically substantial, direct and runnable with standard Linux tools.

- Teach the concept, demonstrate four examples, then give independent exercises and interview checks.
- Do not recommend sudo, world-writable permissions, unverified curl-to-shell, or destructive commands without context and safeguards.
- Use disposable local fixtures and clear error handling in scripts.
- Include normal and edge cases, avoiding live network dependencies.
- Check `bash -n`, `python tools/grade.py --verify-references`, and `python -m unittest discover -s tests -v` before opening a PR.
