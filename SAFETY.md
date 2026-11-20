# Safe Linux course rules

1. **No sudo required.** Use Linux, WSL2 or a disposable VM; system administration examples that could change services are documented, not executed.
2. **Use disposable paths.** Test file operations in a directory returned by mktemp -d. Inspect every path before deletion or overwrite.
3. **Protect credentials.** Never put passwords, SSH private keys, access tokens or private logs into Git or shared terminal output.
4. **Treat network access as permissioned.** Diagnose only servers you own or are authorized to test. Keep TLS verification enabled.
5. **No untrusted shell scripts.** The grader executes local student code and is not an isolation sandbox.
6. **Do not hide failures.** Verify stdout, stderr, exit code, data integrity and cleanup. Avoid broad
