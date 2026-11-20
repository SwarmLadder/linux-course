# Intermediate project: safe backend deployment checklist

**Intermediate · Lesson 11 · 75–110 minutes**

## Learning outcome
Build a local release script workflow that validates artifacts, updates a versioned directory and supports rollback.

Linux/WSL2 recommended. Host-modifying and remote commands are illustrative only; local examples use disposable paths.

### 1. Define release inputs
A deployment needs the artifact path, version, target directory and expected checksum. Validate each before touching the current release. Don't trust filenames or a checksum supplied by the same untrusted source.

```bash
work=$(mktemp -d)
mkdir -p "$work/releases" "$work/build"
printf 'app version 1\n' > "$work/build/app.txt"
sha256sum "$work/build/app.txt"
```

**Check:** Describe how the expected digest would be verified in real CI.

### 2. Stage instead of overwriting
Keep deployments in versioned directories. Copy artifacts to a staging directory and verify content before any service switch. In production also protect against concurrent deploys.

```bash
mkdir -p "$work/releases/v1"
cp -- "$work/build/app.txt" "$work/releases/v1/app.txt"
cmp -- "$work/build/app.txt" "$work/releases/v1/app.txt"
ls -l "$work/releases/v1"
```

**Check:** What could go wrong if two deploy jobs update the same release?

### 3. Switch via a controlled link
A symlink can point to the selected version; a better production pattern creates a temporary link and atomically renames it over the current link. Here we only demonstrate a single target switch.

```bash
ln -s "$work/releases/v1" "$work/current"
readlink -- "$work/current"
cat "$work/current/app.txt"
```

**Check:** When would a symlink switch not be enough for zero downtime?

### 4. Plan rollback and verification
Deployment is not successful until readiness and a smoke test pass. Keep prior releases, verify logs and latency after switch, and define a rollback trigger and owner.

```bash
printf 'release=v1\nstatus=ok\n' > "$work/release-report.txt"
cat "$work/release-report.txt"
python tools/grade.py I04
```

**Check:** The grade command checks your atomic-copy starter and fails until implemented.

## Practice
1. Implement the atomic-copy lab I04.
2. Write a release script with validation before switch.
3. Add tests for missing artifacts, existing versions and rollback.

## Interview questions
- Why use versioned releases?
- Which readiness signal should block a deployment?

**Caution:** Do not run this project as an unattended production deployment.

**Ready when:** You can diagnose expected and failure behavior and explain the safest production alternative.
