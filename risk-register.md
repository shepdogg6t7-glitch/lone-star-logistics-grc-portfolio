# Lone Star Logistics — Enterprise Risk Register

**Document ID:** LSL-RISK-001
**Classification:** Internal — Governance
**Framework Mapping:** NIST CSF v2.0 (ID.RA, GV.RM) with control mapping to CIS Controls v8 and NIST SP 800-53
**Owner:** IT Security / Risk Committee
**Review Cycle:** Quarterly, or upon new incident/policy change

---

## Scoring Methodology

**Likelihood** and **Impact** are each scored 1 (Low) – 5 (Very High). **Priority** = Likelihood × Impact:

| Score Range | Priority |
|---|---|
| 1–6 | Low |
| 7–14 | Medium |
| 15–20 | High |
| 21–25 | Critical |

---

## Risk Entries

### RISK-001: Ransomware Locking the Logistics Core Platform (LCP)

| Field | Value |
|---|---|
| **Description** | A ransomware attack encrypts or locks LCP, halting fleet tracking, scheduling, and dispatch across all sites. |
| **Likelihood** | 3 (Moderate — logistics/3PL is a common ransomware target sector) |
| **Impact** | 5 (Very High — full operational halt) |
| **Priority** | 15 — **High** |
| **NIST CSF Mapping** | PR.DS (Data Security), RC.RP (Recovery Planning) |
| **Control Mapping** | CIS Control 11 (Data Recovery), NIST SP 800-53 CP-9 (System Backup) |
| **Source** | Not yet covered by an existing policy — **gap** |
| **Recommended Mitigation** | Establish immutable, tested backups for LCP; formalize a recovery-time objective in a future Business Continuity Policy. |
| **Status** | Open |

### RISK-002: Unauthorized Access to the Client Booking Portal

| Field | Value |
|---|---|
| **Description** | An attacker gains unauthorized access to the Client Booking Portal, exposing client billing and shipment data. |
| **Likelihood** | 3 (Moderate — public-facing app is a larger attack surface) |
| **Impact** | 4 (High — client data exposure, reputational and contractual impact) |
| **Priority** | 12 — **Medium** |
| **NIST CSF Mapping** | PR.AA (Access Control) |
| **Control Mapping** | CIS Control 6 (Access Control Management), NIST SP 800-53 IA-2 (Identification and Authentication) |
| **Source** | Access Control Policy (LSL-POL-AC-001) §3.1 — requires MFA for admin/remote access, but **the Client Booking Portal does not currently enforce it** |
| **Recommended Mitigation** | Extend MFA requirement to all Client Booking Portal administrative and customer accounts handling payment data; validate via Project 3 hardening audit. |
| **Status** | Open — policy exists, enforcement gap identified |

### RISK-003: Unassessed Third-Party Vendor Risk

| Field | Value |
|---|---|
| **Description** | Lone Star Logistics currently has no process to tier or assess vendor security posture before granting system access, meaning any vendor (including LCP's cloud host) could introduce unassessed risk. |
| **Likelihood** | 4 (High — no control currently exists to prevent this) |
| **Impact** | 4 (High — a compromised critical vendor could affect LCP or client data directly) |
| **Priority** | 16 — **High** |
| **NIST CSF Mapping** | GV.SC (Cybersecurity Supply Chain Risk Management) |
| **Control Mapping** | CIS Control 15 (Service Provider Management), NIST SP 800-53 SR-2 (Supply Chain Risk Management Plan) |
| **Source** | Vendor Risk Management Policy (LSL-POL-VRM-001) — policy defines the tiering process, but **no vendor has been tiered or assessed under it yet** |
| **Recommended Mitigation** | Conduct an initial tiering pass on all existing vendors within 90 days, prioritizing Tier 1 candidates (LCP cloud host, payment processor). |
| **Status** | Open — highest priority due to zero current coverage |

### RISK-004: Inter-Spoke Routing Misconfiguration Recurrence

| Field | Value |
|---|---|
| **Description** | A routing configuration drift previously caused a full connectivity failure between the Sales and Warehouse spokes (see INC-001), and no configuration baseline currently exists to prevent recurrence. |
| **Likelihood** | 2 (Low — was a one-time human/process error, but no control yet prevents repeat) |
| **Impact** | 3 (Moderate — caused real operational disruption when it occurred) |
| **Priority** | 6 — **Low** |
| **NIST CSF Mapping** | PR.IR (Technology Infrastructure Resilience), DE.CM (Continuous Monitoring) |
| **Control Mapping** | CIS Control 4 (Secure Configuration Management), NIST SP 800-53 CM-2 (Baseline Configuration) |
| **Source** | INC-001 post-mortem (Incident Response Plan, LSL-POL-IR-001) — preventative recommendation not yet implemented |
| **Recommended Mitigation** | Adopt the documented "known-good" static route baseline and require inter-site `traceroute` verification as part of any routing change checklist. |
| **Status** | Open — mitigation identified, not yet implemented |

---

## Summary Priority View

| Risk ID | Title | Priority |
|---|---|---|
| RISK-003 | Unassessed Third-Party Vendor Risk | High (16) |
| RISK-001 | Ransomware Locking LCP | High (15) |
| RISK-002 | Unauthorized Access to Client Booking Portal | Medium (12) |
| RISK-004 | Inter-Spoke Routing Misconfiguration Recurrence | Low (6) |

---

*Each entry ties directly back to a gap identified in Project 1's policies or the real INC-001 incident — no hypothetical risks were invented without a documented source.*
