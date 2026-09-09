# Lone Star Logistics — Vendor Risk Management Policy

**Document ID:** LSL-POL-VRM-001
**Classification:** Internal — Governance
**Framework Mapping:** NIST CSF v2.0 — GV.SC (Cybersecurity Supply Chain Risk Management)
**Owner:** Procurement / IT Security (joint ownership)
**Review Cycle:** Annual, or upon onboarding any new critical vendor

---

## 1. Purpose

Establishes requirements for assessing and managing cybersecurity risk introduced by third-party vendors and service providers with access to Lone Star Logistics systems or data.

## 2. Scope

Applies to any third party that:

- Has network or system access to the Corporate Network, LCP, or Client Booking Portal, **or**
- Processes, stores, or transmits Lone Star Logistics or client data (e.g., billing processors, cloud hosting providers)

## 3. Policy Statements

### 3.1 Vendor Risk Tiering (GV.SC-04)
Vendors are classified into tiers based on data/system access:

| Tier | Definition | Example |
|---|---|---|
| Tier 1 — Critical | Direct system access or processes sensitive/client data | LCP cloud hosting provider, payment processor |
| Tier 2 — Moderate | Limited access, no sensitive data | Office equipment vendor with network-connected devices |
| Tier 3 — Low | No system access or data handling | Office supplies, non-connected services |

### 3.2 Pre-Onboarding Due Diligence (GV.SC-06)
- Tier 1 vendors must provide evidence of a security program (e.g., SOC 2 report, security questionnaire response) before contract signature.
- Tier 2 vendors complete a lightweight security questionnaire.
- Tier 3 vendors are exempt from security due diligence but remain subject to standard procurement review.

### 3.3 Contractual Requirements (GV.SC-05)
- Contracts with Tier 1 vendors must include: breach notification timelines, data handling/retention terms, and right-to-audit clauses.
- Access granted to any vendor must follow the Access Control Policy (least privilege, time-limited, logged).

### 3.4 Ongoing Monitoring (GV.SC-07)
- Tier 1 vendor security posture is reviewed annually or upon renewal.
- Any vendor-reported security incident affecting Lone Star Logistics data or systems is logged and triaged under the Incident Response Plan.

### 3.5 Offboarding
- Vendor system access is revoked within 24 hours of contract termination, consistent with the Access Control Policy.

## 4. Roles & Responsibilities

| Role | Responsibility |
|---|---|
| Procurement | Initiates vendor tiering and due diligence at contract intake |
| IT Security | Reviews Tier 1 vendor security evidence, monitors ongoing posture |
| System Owners | Approve and periodically review vendor system access |

## 5. Related Documents

- Access Control Policy (LSL-POL-AC-001)
- Incident Response Plan (LSL-POL-IR-001)
- Enterprise Risk Register
