# TCP, DNS, TLS, and firewalls for backend systems

**Advanced · Lesson 03 · 90–120 minutes**

## Outcome
Locate network failures by layer and distinguish service binding, routing, name resolution and encrypted HTTP.

These are safe inspection commands and configuration illustrations. No root privileges or network access is required to work through the concepts.

### 1. Inspect interfaces and routes
Interface addresses and routes determine where packets can travel. A service bound to loopback is not remotely reachable even if the process is healthy. Namespaces can present different routing tables.

```bash
if command -v ip >/dev/null; then ip -br addr; ip route; fi
getent hosts localhost
```

**Check:** Why can a service in a container be unreachable despite binding port 8080?

### 2. Inspect listeners and states
ss shows socket state; -ltn lists listening TCP sockets. Connection success requires listener, route and policy to allow traffic. A TCP handshake does not verify application readiness.

```bash
if command -v ss >/dev/null; then ss -ltn | head -n 12; fi
cat /proc/net/tcp | head -n 3
```

**Check:** What distinction exists between CONNECTION_REFUSED and TIMEOUT?

### 3. Understand DNS and TLS
DNS maps names to addresses; TLS provides authenticated encryption using certificates and trust anchors. Disabling certificate checks to make a request pass hides an important safety failure.

```bash
getent ahosts localhost | head -n 4
command -v openssl || :
# Only against an authorized server:
# openssl s_client -connect service.example.test:443 -servername service.example.test
```

**Check:** What is the role of SNI when multiple services share an IP?

### 4. Diagnose HTTP responses
Curl distinguishes DNS/TCP/TLS errors from HTTP errors through stderr and exit codes when configured. Structured access logs and request IDs help correlate server responses.

```bash
# On a local service you control:
# curl --fail-with-body --silent --show-error http://127.0.0.1:8080/health
# curl --connect-timeout 2 --max-time 5 -v http://127.0.0.1:8080/
```

**Check:** Why can HTTP 503 indicate an upstream dependency rather than a network outage?

## Applied exercises
1. Create a diagnostic flow from DNS to HTTP response.
2. Explain difference between an open TCP port and a healthy API.
3. Describe how to debug a TLS trust error without disabling checks.

## Interview review
- What does ss -ltn show?
- Why is listening on 0.0.0.0 different from 127.0.0.1?

**Caution:** Only test endpoints you own or are authorized to inspect.

**Pass:** Explain the subsystem, how to inspect failure, and one risk of the naive fix.
