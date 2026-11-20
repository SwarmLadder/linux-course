# Project 2 — Versioned local release simulator

**Goal:** Deploy a synthetic artifact without producing partially written active files. No SSH, sudo, or production services.

## Contract

Input: source file, version name, existing root directory. Maintain `releases/VERSION/app.txt` and an active `current` symlink. Refuse duplicate versions; support switching back to any existing version.

## Deliverables

1. Validate arguments, version name, source file, writable root and existing release.
2. Copy into a temporary staging directory in the same filesystem, verify the copy, then rename into a versioned release.
3. Switch a temporary symlink to current using a rename after validation.
4. Keep old releases and implement rollback to a known version.
5. Test missing source, duplicate version, corrupted content and rollback failures.

## Try the reference

```bash
work=$(mktemp -d)
printf 'version 1\n' > "$work/app.txt"
bash projects/examples/release_simulator.sh "$work/app.txt" v1 "$work"
printf 'version 2\n' > "$work/app.txt"
bash projects/examples/release_simulator.sh "$work/app.txt" v2 "$work"
bash projects/examples/rollback_release.sh "$work" v1
cat "$work/current/app.txt"
```

**Limitations:** Local illustration only. A real deployment needs concurrency controls, readiness and smoke tests, file ownership, durable writes, permissions and rollback compatibility with migrations.

**Interview:** Explain atomic rename versus crash durability, and what happens during parallel deploys.
