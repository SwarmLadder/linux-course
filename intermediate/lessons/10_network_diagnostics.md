# DNS, TCP, HTTP, and port diagnostics

**Intermediate · Lesson 10 · 75–110 minutes**

## Learning outcome
Diagnose a backend connectivity problem layer by layer without confusing DNS, TLS, TCP and HTTP status.

Linux/WSL2 recommended. Host-modifying and remote commands are illustrative only; local examples use disposable paths.

### 1. Identify interfaces and addresses
IP addresses belong to interfaces and routes decide how packets travel. `ip addr` and `ip route` are preferred on many Linux systems; container networks may expose only a namespace view.

```bash
if command -v ip >/dev/null; then ip -br addr; ip route; fi
hostname
```

**Check:** What changes between a host network namespace and a container's?

### 2. Inspect listening sockets
`ss -ltn` lists listening TCP sockets; -p may require permissions to show owning processes. A process listening on 127.0.0.1 may not accept external connections.

```bash
if command -v ss >/dev/null; then ss -ltn | head -n 12; fi
cat /etc/resolv.conf | head -n 8
```

**Check:** Why doesn't a locally open port guarantee remote reachability?

### 3. Understand DNS resolution
DNS resolves names, but failure can originate from caches, resolvers or search domains. Use getent hosts for OS-level resolution and dig when installed; these may require network.

```bash
getent hosts localhost
command -v dig || echo 'dig not installed'
getent ahosts localhost | head -n 4
```

**Check:** How does DNS resolution differ from proving a TCP connection succeeds?

### 4. Separate HTTP and TLS failures
curl can show HTTP status and timing when a service is reachable, while TLS errors occur before an HTTP response. Avoid `-k` when investigating trust failures. These commands are examples, not mandatory network tests.

```bash
# Against a service you control:
# curl --fail-with-body --silent --show-error https://service.example.test/health
# curl -I --connect-timeout 3 https://service.example.test/
```

**Check:** Why is HTTP 500 evidence different from a DNS lookup failure?

## Practice
1. Create a troubleshooting decision tree from DNS to HTTP.
2. Identify local-only vs public bind addresses.
3. Explain which logs/metrics to collect for timeout errors.

## Interview questions
- What does `ss -ltn` show?
- Why should TLS certificate verification remain enabled?

**Caution:** Only probe services that you own or are authorized to test.

**Ready when:** You can diagnose expected and failure behavior and explain the safest production alternative.
