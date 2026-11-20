# Backend operations incident response and hardening

**Advanced · Lesson 10 · 90–120 minutes**

## Learning goal
Respond to real failures with evidence, containment, communication, and reversible mitigation while preserving sensitive data.

Use Linux/WSL2 for inspection and disposable local fixtures for writing. Production configuration is conceptual unless you own a safe test environment.

### 1. Establish scope and severity
Start with impact: affected users, endpoints, error rate, data integrity and duration. Capture current evidence before restarting everything; the first symptom may not be the primary cause.

```bash
date -u +'%Y-%m-%dT%H:%M:%SZ'
uptime
free -h
df -h .
```

**Check:** What data would show the incident is worsening or stabilizing?

### 2. Build a timeline
Correlate deploy changes, error logs, request IDs and monitoring. Use UTC timestamps and separate observed facts from hypotheses. Avoid copying tokens or personal data into public incident notes.

```bash
# Template:
# 12:00 UTC: deploy v2 started
# 12:03 UTC: 5xx rate rose
# 12:05 UTC: database pool saturated
# 12:08 UTC: rollback initiated
```

**Check:** Why does a timeline need both the intervention and resulting metric?

### 3. Contain before deep optimization
When credentials are leaked, revoke and rotate them. When service state is corrupted, stop destructive writes before experimenting. Choose bounded reversible mitigations and document authorization.

```bash
# Incident decision tree:
# secrets exposed? revoke/rotate first
# writes corrupting data? contain write path
# resource pressure? restrict intake safely
# suspected attack? follow security escalation policy
```

**Check:** Why can aggressive troubleshooting cause additional data loss?

### 4. Close with tests and prevention
Write a concise post-incident review: impact, timeline, cause, contributing factors, recovery, follow-up owners and deadlines. Blame-free does not mean responsibility-free; use concrete controls.

```bash
# Review checklist:
# customer impact and recovery times
# factual timeline
# contributing design gaps
# tested mitigations and owners
# follow-up verification
```

**Check:** How do you know a preventive action actually worked?

## Applied work
1. Investigate a fictional disk-full API incident.
2. Design a credential leak response without publishing secret values.
3. Write a post-incident review with measurable follow-ups.

## Interview review
- What are first steps in an incident?
- When should you avoid restarting an unhealthy service?

**Safety:** Never run a security/incident simulation against systems without authorization.

**Complete when:** You can justify the diagnostic evidence, operational risk and recovery choice.
