# Lone Star Logistics — System Hardening Audit Checklist

**Document ID:** LSL-AUDIT-001
**Classification:** Internal — Technical Validation
**Framework Mapping:** NIST CSF v2.0 — PR.PS (Platform Security), DE.CM (Continuous Monitoring)
**Baseline Reference:** CIS Ubuntu Linux Benchmark (subset)
**Validates:** Access Control Policy (LSL-POL-AC-001)

---

This checklist verifies that a server matches the baseline required by the Access Control Policy. Each check maps to a specific CIS Benchmark recommendation and a specific policy requirement — this is what closes the loop between governance and technical reality.

| # | Check | CIS Benchmark Ref | Policy Requirement | Automated? |
|---|---|---|---|---|
| 1 | SSH root login is disabled | 5.2.10 | AC-001 §3.1 — no shared/generic accounts | Yes |
| 2 | SSH password authentication is disabled (key-based only) | 5.2.11 | AC-001 §3.1 — authentication strength | Yes |
| 3 | Uncomplicated Firewall (UFW) is active | 3.5.1 | Implied infrastructure protection baseline | Yes |
| 4 | Automatic security updates are enabled | 1.1.1 | Implied patch management baseline | Yes |
| 5 | Password minimum length policy is enforced (≥14 chars) | 5.4.1 | AC-001 §3.1 — password complexity | Yes |
| 6 | No unauthorized UID 0 (root-equivalent) accounts exist | 6.2.9 | AC-001 §3.2 — least privilege | Yes |
| 7 | Quarterly access review has been performed and documented | N/A | AC-001 §3.4 — periodic access review | No — manual/process check |

**Note on Check 7:** Not every control is technically automatable. Access reviews are a *process* control, not a system state — the auditor script flags this as a manual attestation item rather than fabricating a false "pass."

---

## Running the Audit

```bash
python3 hardening_auditor.py
```

Requires `sudo` for some checks (SSH config, UFW status). The script will prompt if elevated permissions are needed for a specific check and skip that check (marking it "Unable to verify") rather than failing silently if permission is denied.
