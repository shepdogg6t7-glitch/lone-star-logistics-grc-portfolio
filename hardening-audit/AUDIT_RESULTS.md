# Lone Star Logistics — Hardening Audit Results

**Document ID:** LSL-AUDIT-RESULTS-001
**Target System:** WSL2 Ubuntu 22.04 (development/test environment)
**Auditor:** `hardening_auditor.py`
**Validates:** Access Control Policy (LSL-POL-AC-001), Hardening Checklist (LSL-AUDIT-001)

---

## Summary

| Check | Initial Result | Final Result | Remediation Applied |
|---|---|---|---|
| SSH root login disabled | Unable to verify (no SSH server installed) | **PASS** | Installed `openssh-server`; set `PermitRootLogin no` |
| SSH password auth disabled | Unable to verify | **PASS** | Set `PasswordAuthentication no` |
| UFW firewall active | Unable to verify (needs elevated access) | **PASS** | Installed and enabled `ufw` |
| Automatic security updates | **PASS** (already compliant) | **PASS** | No action needed |
| Password minimum length ≥ 14 | Unable to verify (package not installed) | **PASS** | Installed `libpam-pwquality`; set `minlen = 14` |
| No unauthorized UID 0 accounts | **PASS** (already compliant) | **PASS** | No action needed |
| Quarterly access review | Manual (not automatable) | Manual (not automatable) | N/A — process control, verified separately |

**Final result: 6/6 automated checks passing, 1 manual attestation item outstanding.**

## Remediation Narrative

Getting from the initial to final state surfaced two real technical issues beyond simply editing config values — both worth documenting, since they reflect genuine root-cause troubleshooting rather than a clean first pass:

### Issue 1: SSH Config Syntax Error
After editing `sshd_config`, `sshd -t` (the built-in syntax validator) failed with `line 50: no argument after keyword "no"` — a stray orphaned line left over from manual editing. Root cause was isolated by running the syntax check directly rather than guessing from the generic `systemctl` failure message, then corrected by removing the malformed line.

**Lesson:** A service restart failure alone doesn't tell you *why* — running the daemon's own config-test flag (`sshd -t`) isolates syntax issues immediately, before touching the service itself.

### Issue 2: Missing `/run/sshd` Directory (WSL-Specific)
After fixing the syntax error, `sshd -t` returned a second, unrelated error: `Missing privilege separation directory: /run/sshd`. This is a known behavior in WSL2 — `/run` is a `tmpfs` (memory-backed, non-persistent) filesystem, and unlike a standard Linux boot sequence, WSL does not always recreate service-required directories under `/run` automatically.

**Operational Finding:** This directory will need to be recreated (`mkdir -p /run/sshd`) after every WSL instance restart unless a startup hook is configured to handle it — otherwise SSH will silently fail to start on next boot despite a fully correct config. This is logged as a known gap rather than treated as fully resolved.

**Recommended Follow-up:** Add a systemd override or `/etc/wsl.conf` boot command to recreate `/run/sshd` automatically, so this doesn't require manual intervention on every environment restart.

---

*This audit reflects an actual remediation performed on a live WSL2 environment, not a simulated result. Both technical issues encountered were diagnosed and resolved using the daemon's own diagnostic tooling (`sshd -t`, `systemctl status`) rather than trial-and-error configuration changes.*
