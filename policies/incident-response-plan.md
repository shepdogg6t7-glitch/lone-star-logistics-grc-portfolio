# Lone Star Logistics — Incident Response Plan

**Document ID:** LSL-POL-IR-001
**Classification:** Internal — Governance
**Framework Mapping:** NIST CSF v2.0 — RS (Respond), DE.AE (Anomalies and Events)
**Owner:** IT Security Team
**Review Cycle:** Annual, or after any Severity 1/2 incident

---

## 1. Purpose

Defines how Lone Star Logistics detects, classifies, responds to, and recovers from security incidents affecting the Corporate Network, Logistics Core Platform (LCP), or Client Booking Portal.

## 2. Scope

Covers all confirmed or suspected incidents involving unauthorized access, service disruption, data exposure, or malicious activity affecting in-scope systems.

## 3. Incident Severity Classification (DE.AE-02)

| Severity | Definition | Example |
|---|---|---|
| **Sev 1 — Critical** | Full service outage or confirmed data breach affecting customers | LCP unavailable, halting freight dispatch |
| **Sev 2 — High** | Partial service disruption or high-risk exposure, contained | Inter-site connectivity failure blocking inventory sync |
| **Sev 3 — Moderate** | Limited/localized issue, no immediate business impact | Isolated account lockout, single failed login pattern |
| **Sev 4 — Low** | Informational anomaly, no action required beyond logging | Routine failed login within normal thresholds |

## 4. Incident Response Phases (RS.MA)

1. **Detection & Reporting** — Any employee or automated alert identifying a suspected incident reports it immediately to IT Security.
2. **Triage & Classification** — IT Security assigns a severity level within 30 minutes of report (Sev 1/2) or by end of business day (Sev 3/4).
3. **Containment** — Isolate affected systems or accounts to prevent further impact (e.g., disable compromised credentials, isolate affected network segment).
4. **Root Cause Diagnosis** — Systematic diagnosis (e.g., log review, routing table inspection, traffic tracing) to identify the underlying cause — not just the symptom.
5. **Remediation** — Apply the fix (e.g., patch, configuration correction, access revocation) and verify the fix resolves the issue without introducing new risk.
6. **Recovery & Verification** — Confirm affected systems are fully restored and functioning as expected (e.g., end-to-end connectivity test, functional test of affected service).
7. **Post-Incident Review** — For Sev 1/2 incidents, document a post-mortem within 5 business days covering root cause, remediation, and preventative controls. Logged in the Incident & Risk Register.

## 5. Roles & Responsibilities

| Role | Responsibility |
|---|---|
| IT Security Team | Leads triage, containment, and remediation |
| System Owners | Support root cause diagnosis and validate recovery |
| Management | Notified for all Sev 1/2 incidents; approves external communication if required |

## 6. Preventative Controls Feedback Loop

Every post-incident review must identify at least one preventative control (e.g., a configuration baseline, a monitoring rule, a process change) and log it against the relevant policy gap in the Enterprise Risk Register.

## 7. Related Documents

- Access Control Policy (LSL-POL-AC-001)
- Enterprise Risk Register
- Incident & Risk Register (individual incident write-ups)
