# Namespaces, cgroups, and container isolation

**Advanced · Lesson 04 · 90–120 minutes**

## Outcome
Understand what containers isolate and why container boundaries are not automatically security boundaries.

These are safe inspection commands and configuration illustrations. No root privileges or network access is required to work through the concepts.

### 1. Inspect namespaces
A namespace changes what a process sees for resources such as PIDs, mounts and networking. Containers often combine namespaces with cgroup limits and filesystem layering.

```bash
ls -l /proc/self/ns | head -n 12
ps -p 1 -o pid,comm
```

**Check:** Why can PID 1 inside a container differ from the host's PID 1?

### 2. Read cgroup limits
Cgroups account for and constrain CPU, memory, I/O and tasks. The layout differs between cgroups v1 and v2. A host can have ample memory while a container reaches its own limit.

```bash
stat -fc %T /sys/fs/cgroup 2>/dev/null || :
cat /proc/self/cgroup | head -n 6
if [[ -f /sys/fs/cgroup/memory.max ]]; then cat /sys/fs/cgroup/memory.max; fi
```

**Check:** Why can a container OOM even when the host reports free RAM?

### 3. Understand image and runtime roles
Container images package filesystem content and metadata; a runtime starts a process under configured namespaces, mounts and restrictions. An image is not equivalent to a virtual machine kernel.

```bash
command -v docker || echo 'Docker not installed'
command -v podman || echo 'Podman not installed'
uname -r
```

**Check:** Why do containers typically share the host kernel?

### 4. Reduce runtime privileges
Rootless execution, dropped capabilities, read-only filesystems and explicit mounts can reduce attack surface. Do not mount the host's Docker socket into an untrusted app; it often grants control of host containers.

```bash
# Security review checklist:
# runAsNonRoot; drop unnecessary Linux capabilities
# read-only root filesystem where feasible
# restrict network and mount access
# avoid privileged mode and host socket mounts
```

**Check:** What happens when a service needs writable cache/state paths?

## Applied exercises
1. Explain namespace versus cgroup role.
2. Describe how to debug an OOM-killed container.
3. Review a Docker run policy for excessive privileges.

## Interview review
- Are containers VMs?
- Does read-only root filesystem make a container fully secure?

**Caution:** Commands inspect local capabilities; no container setup is required.

**Pass:** Explain the subsystem, how to inspect failure, and one risk of the naive fix.
