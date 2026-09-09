# Lone Star Logistics — Access Control Policy

**Document ID:** LSL-POL-AC-001
**Classification:** Internal — Governance
**Framework Mapping:** NIST CSF v2.0 — PR.AA (Identity Management, Authentication, and Access Control)
**Owner:** IT Security / IAM Team
**Review Cycle:** Annual, or upon material system change

---

## 1. Purpose

This policy establishes the requirements for granting, reviewing, and revoking access to Lone Star Logistics systems, ensuring that only authorized individuals can access company resources at the level required for their role.

## 2. Scope

Applies to all employees, contractors, and third parties with access to:

- **Corporate Network & IAM** (Active Directory / identity provider)
- **Logistics Core Platform (LCP)** — fleet tracking, scheduling, inventory
- **Client Booking Portal** — public-facing client-facing application

## 3. Policy Statements

### 3.1 Identity & Authentication (PR.AA-01, PR.AA-03)
- All user accounts must be uniquely attributable to a single individual — no shared or generic accounts.
- Multi-factor authentication (MFA) is required for all administrative accounts and all remote access to the Corporate Network.
- Passwords must meet a minimum complexity standard and be rotated upon any suspected compromise.

### 3.2 Least Privilege & Role-Based Access (PR.AA-05)
- Access to LCP and the Client Booking Portal is granted based on documented job function, not by default or convenience.
- Warehouse managers and dispatchers receive access scoped to their regional hub only, unless a documented business need requires broader access.
- Administrative privileges on any system require a documented business justification and manager approval.

### 3.3 Access Provisioning & De-provisioning (PR.AA-01)
- New account requests require manager approval and are provisioned by IT within 2 business days.
- Access must be revoked within 24 hours of an employee's termination or role change that no longer requires it.

### 3.4 Periodic Access Review (PR.AA-05)
- Access rights for all systems in scope are reviewed quarterly by system owners to identify and remove unnecessary or stale permissions.

### 3.5 Remote & Third-Party Access (PR.AA-03)
- Remote dispatcher access to the Corporate Network requires MFA and is logged for audit purposes.
- Third-party vendor access (if granted) must be time-limited and reviewed under the Vendor Risk Management Policy.

## 4. Roles & Responsibilities

| Role | Responsibility |
|---|---|
| IT Security / IAM Team | Maintains access control systems, performs quarterly reviews |
| People Managers | Approve/deny access requests for direct reports |
| System Owners (LCP, Portal) | Validate that access assignments match documented business need |

## 5. Enforcement

Violations of this policy may result in access suspension pending investigation and, depending on severity, disciplinary action up to termination.

## 6. Related Documents

- Incident Response Plan (LSL-POL-IR-001)
- Vendor Risk Management Policy (LSL-POL-VRM-001)
- Enterprise Risk Register (tracks gaps against this policy)
