# Durability, backups, restore tests, and rollback

**Advanced · Lesson 08 · 90–120 minutes**

## Learning goal
Design a recovery plan around actual failure modes, integrity checks, retention and operational constraints.

Use Linux/WSL2 for inspection and disposable local fixtures for writing. Production configuration is conceptual unless you own a safe test environment.

### 1. Define recovery objectives
RPO measures acceptable data loss in time; RTO measures the target time to restore service. Backups are incomplete unless you test restoration and evaluate application consistency.

```bash
# Recovery plan example:
# RPO: 15 minutes of data maximum
# RTO: service restored in 1 hour
# Test scope: restore database + configuration + secrets references
```

**Check:** What must be true about replication/backup cadence to meet a stated RPO?

### 2. Archive deterministic test data
Use isolated directories and tar to make a small backup, then record a checksum. A checksum verifies bytes against the expected digest but does not authenticate untrusted provenance.

```bash
work=$(mktemp -d)
mkdir -p "$work/source" "$work/restored"
printf 'data\n' > "$work/source/item.txt"
tar -czf "$work/archive.tar.gz" -C "$work" source
sha256sum "$work/archive.tar.gz"
```

**Check:** How would you verify checksum authenticity in production?

### 3. Restore, compare, and validate
Extract a trusted archive into a new location; confirm files, permissions and application-level correctness. Restoring a database backup requires checking transaction consistency and migrations, not only file existence.

```bash
tar -xzf "$work/archive.tar.gz" -C "$work/restored"
cmp "$work/source/item.txt" "$work/restored/source/item.txt"
stat -c '%s bytes' "$work/restored/source/item.txt"
```

**Check:** What business invariant should be checked after database restoration?

### 4. Prepare rollback before rollout
Keep versioned artifacts and a documented switch-back route. Data schema changes may make code rollback unsafe; plan expand/backfill/contract before deleting old fields.

```bash
# Release verification:
# artifact digest checked
# migrations backward compatible
# readiness/health checks pass
# previous release available
# restore test recently successful
```

**Check:** Why can reverting application code fail to reverse a destructive schema migration?

## Applied work
1. Implement checksum verification lab A01.
2. Write an RPO/RTO-driven backup test plan.
3. Define failure drills for corruption and unavailable storage.

## Interview review
- What does a backup guarantee?
- How does code rollback differ from data rollback?

**Safety:** Practice only with synthetic data and trusted archives.

**Complete when:** You can justify the diagnostic evidence, operational risk and recovery choice.
