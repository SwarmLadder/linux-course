# Testing and reviewing Bash for production use

**Advanced · Lesson 09 · 90–120 minutes**

## Learning goal
Bring Bash scripts under CI with syntax checks, fixtures, linting, and explicit cross-platform boundaries.

Use Linux/WSL2 for inspection and disposable local fixtures for writing. Production configuration is conceptual unless you own a safe test environment.

### 1. Check syntax cheaply
`bash -n` validates syntax without executing the script. It cannot detect all runtime bugs, unsafe paths or missing dependencies, so pair it with tests on controlled inputs.

```bash
find labs/reference -name '*.sh' -print0 | xargs -0 -n1 bash -n
bash --version | head -n 1
```

**Check:** What runtime defects can a syntax check not catch?

### 2. Use shellcheck and shfmt where available
ShellCheck detects many quoting and control-flow pitfalls; shfmt normalizes style. Neither is installed by default everywhere. Include version pinning and review their output in CI.

```bash
command -v shellcheck || echo 'ShellCheck optional'
command -v shfmt || echo 'shfmt optional'
# If installed: shellcheck labs/reference/*.sh
```

**Check:** Why should a linter warning sometimes be explained rather than blindly suppressed?

### 3. Use deterministic fixtures
A good Bash test supplies fixed input files, verifies stdout/stderr/exit status and checks side effects. Run local scripts inside isolated temp directories; don't execute unknown remote shell scripts in CI.

```bash
python tools/grade.py --list
python tools/grade.py --verify-references
python -m unittest discover -s tests -v
```

**Check:** How do you test error paths without taking down a real service?

### 4. Constrain privileges and dependencies
CI should use least-privilege tokens, no deployment credentials in untrusted PR jobs, and no sudo unless explicitly justified. Pin dependencies and keep scripts resilient to missing optional commands.

```bash
# CI checklist:
# Bash syntax, unit cases and edge fixtures
# no network or root in test jobs
# no tokens printed in logs
# no destructive cleanup outside temporary paths
```

**Check:** Why is executing a pull request's shell code with deployment secrets unsafe?

## Applied work
1. Complete one graded lab and add an extra failing fixture.
2. Review a Bash script for unsafe word splitting.
3. Design CI for a script with optional systemd access.

## Interview review
- What does bash -n validate?
- Why should scripts be tested in temporary directories?

**Safety:** Auto-graded labs intentionally execute local scripts; they are not a security sandbox.

**Complete when:** You can justify the diagnostic evidence, operational risk and recovery choice.
