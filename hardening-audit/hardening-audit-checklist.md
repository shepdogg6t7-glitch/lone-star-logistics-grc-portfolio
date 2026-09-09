# Lone Star Logistics - Ubuntu Hardening Audit Checklist

**Document ID:** LSL-AUD-001  
**Classification:** Internal - Audit Working Paper  
**Target:** Ubuntu server hosting the Client Booking Portal  
**Framework:** NIST CSF v2.0  
**Related risks:** RSK-002, RSK-005, RSK-006  
**Audit frequency:** Monthly automated scan; quarterly evidence review; after material configuration change

---

## 1. Audit Objective

Verify that the production Ubuntu host supporting the Client Booking Portal meets the technical expectations established by the Access Control Policy, Incident Response Plan, and Enterprise Risk Register. The audit is read-only: it collects configuration evidence and does not modify the host.

## 2. Evidence Collection

Record the following before or during each audit:

- Hostname, environment, owner, and audit date
- Ubuntu release and kernel version
- Script version and command-line options used
- Reviewer and approval ticket or change reference
- Complete script output, including skipped checks and errors
- Remediation ticket for every failed check

Do not include passwords, private keys, session tokens, or full sensitive log contents in the evidence package.

## 3. Control Checklist

| ID | Check | Expected condition | Evidence | NIST CSF v2.0 | Result |
|---|---|---|---|---|---|
| AC-01 | Supported operating system | Ubuntu release is supported by the organization's patch policy. | `/etc/os-release`, support review | PR.PS-01 | Not run |
| AC-02 | Security updates | Package metadata is current and no known security updates are pending. | `apt` security update summary | PR.PS-01 | Not run |
| AC-03 | SSH root access | `PermitRootLogin` is `no` or an approved equivalent is enforced. | Effective SSH configuration | PR.AA-05 | Not run |
| AC-04 | SSH password authentication | Password-based SSH authentication is disabled unless a documented exception exists. | Effective SSH configuration | PR.AA-03 | Not run |
| AC-05 | SSH protocol and service exposure | SSH uses the approved port and is limited to approved network paths. | Listening sockets and firewall rules | PR.PS-04 | Not run |
| AC-06 | Host firewall | UFW or an approved host firewall is active with only required inbound services allowed. | Firewall status and rules | PR.PS-04 | Not run |
| AC-07 | Exposed services | Listening TCP services are limited to the approved portal and administration ports. | `ss -ltn` output | PR.PS-04 | Not run |
| AC-08 | Privileged account review | Only approved administrative users have sudo or equivalent privilege. | `sudo` group and local account review | PR.AA-05 | Manual |
| AC-09 | Password aging | Local accounts follow approved maximum password age and inactive-account settings. | `chage` output for reviewed accounts | PR.AA-03 | Manual |
| AC-10 | Sensitive file permissions | `/etc/passwd`, `/etc/group`, and `/etc/shadow` have expected ownership and permissions. | `stat` output | PR.PS-01 | Not run |
| AC-11 | Audit logging | Audit or security logs are enabled, retained, and forwarded according to the logging standard. | `systemctl`, `journalctl`, or SIEM evidence | DE.CM-01 | Manual |
| AC-12 | Time synchronization | A supported time synchronization service is active. | `timedatectl` output | DE.CM-01 | Manual |
| AC-13 | Malware and integrity monitoring | Approved endpoint or file-integrity monitoring is installed and reporting. | Agent status or console evidence | DE.CM-09 | Manual |
| AC-14 | Backup and recovery | Portal backups exist, are protected from host compromise, and have a recent restore test. | Backup job and restore-test evidence | RC.RP-01 | Manual |
| AC-15 | Change and exception management | Failed checks have remediation tickets or approved, time-bound exceptions. | Ticket or exception record | GV.RM-03 | Manual |

## 4. Execution Procedure

1. Confirm authorization and maintenance-window requirements before connecting to production.
2. Copy `hardening_auditor.py` to the host through the approved administration channel.
3. Run the script as an approved administrator so it can inspect firewall, SSH, package, and permission settings.
4. Capture the command, timestamp, host identity, script output, and exit code.
5. Investigate every `FAIL` result and distinguish a true control failure from an approved exception.
6. Create remediation tickets with an owner and target date; escalate High or Critical risk according to the Enterprise Risk Register.
7. Re-run the audit after remediation and attach the passing output to the ticket.
8. Have the system owner review and sign off the evidence package.

Example command:

```bash
sudo python3 hardening_auditor.py --allowed-ports 22,80,443
```

For a portal that uses a different administration port, specify the approved port explicitly and retain the change record with the evidence.

## 5. Pass Criteria

- All automated checks pass, or each failure has an approved, current exception.
- No unapproved administrative or database service is internet-exposed.
- No sensitive file has weaker permissions than the expected baseline.
- Evidence is attributable to the target host and audit window.
- Remediation is verified by a subsequent scan or documented manual test.

## 6. Reporting

The auditor reports findings using this format:

| Field | Required content |
|---|---|
| Finding ID | Stable identifier, such as `AC-07` |
| Condition | What the host currently shows |
| Expected state | Policy or baseline requirement |
| Risk | Business and technical consequence |
| Owner | Responsible team or system owner |
| Due date | Target remediation date |
| Exception | Approver, rationale, and expiration if applicable |
| Verification | Evidence from the follow-up test |

## 7. Related Documents

- Access Control Policy (LSL-POL-AC-001)
- Incident Response Plan (LSL-POL-IR-001)
- Enterprise Risk Register (LSL-RSK-001)
- Vendor Risk Management Policy (LSL-POL-VRM-001)
