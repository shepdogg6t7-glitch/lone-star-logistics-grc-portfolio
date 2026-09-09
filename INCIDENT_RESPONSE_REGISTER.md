# Lone Star Logistics — Incident & Risk Register Entry

**Incident ID:** INC-001 — Inter-Spoke Cross-Site Connectivity Failure
**Status:** Resolved / Post-Mortem Complete
**Framework Mapping:** NIST CSF v2.0 — RS.MA-01 (Incident Response Executed), DE.AE-02 (Anomalies Analyzed)

---

## 1. Detection & Impact

**Symptoms:** Personnel at **Spoke Site 1 (Sales)** were unable to reach systems at **Spoke Site 2 (Warehouse)**, despite both spokes having a working path to HQ.

**Business Impact (simulated):** If unresolved in a production environment, this class of fault would block Sales from pulling real-time inventory data from the Warehouse, stalling dispatch and freight scheduling decisions.

## 2. Diagnostic Process & Root Cause

Diagnosed using a standard tiered troubleshooting model:

```
[Spoke 1 Host] --(ping: success)--> [Spoke 1 Gateway] --(traceroute: drops)--> [HQ Hub / opposing spoke]
```

1. **Local gateway check** — `ping` from Spoke 1 clients to their default gateway succeeded, ruling out local Layer 1/2 or DHCP issues.
2. **Path trace** — `traceroute` to a Spoke 2 host reached the HQ Hub successfully, then dropped.
3. **Routing table inspection** — `show ip route` on each spoke router showed a route *to* HQ, but no return route *to the opposing spoke's* WAN transit subnet.
4. **Root cause** — Missing static routes on the spoke routers for the opposing spoke's transit subnet, producing asymmetric routing: traffic could reach HQ but had no defined path onward to the other spoke.

## 3. Remediation & Verification

- Added the missing static routes on both spoke routers, explicitly defining the path to the opposing spoke's LAN via the HQ Hub's inward-facing WAN interfaces.
- Verified with `show ip route` (routes present and correct) and a follow-up `traceroute` confirming a clean two-hop path in both directions.

## 4. Preventative Recommendation

To reduce recurrence risk of this class of fault:

- **Configuration baselines:** Maintain a documented "known-good" static route table for each site as part of change-control sign-off, so route changes are reviewed rather than made ad hoc.
- **Post-change verification step:** Require a `traceroute` between all site pairs (not just to HQ) as part of any routing change checklist — this incident specifically slipped through because HQ connectivity was verified but inter-spoke connectivity wasn't.

---
*This entry documents an actual troubleshooting exercise from a Packet Tracer lab, reframed in a corporate incident-register format for portfolio purposes. Diagnostic steps and root cause reflect the real lab session; business-impact framing is illustrative.*
