# Lone Star Logistics — GRC Portfolio Case Study

A governance, risk, and compliance portfolio built around a fictitious mid-sized logistics company, mapped end-to-end to the NIST Cybersecurity Framework (CSF) v2.0.

## About This Project

This repository simulates a full GRC program lifecycle for **Lone Star Logistics**, a fictitious 3PL/freight logistics company (~450 employees, 1 HQ + 3 regional distribution hubs). Rather than treating policy, risk, and technical validation as separate exercises, this portfolio demonstrates a closed loop between them:

1. **Policy establishes the standard.**
2. **Risk analysis identifies where reality falls short of that standard.**
3. **Technical auditing and incident response verify and enforce it.**

The underlying network architecture referenced throughout (`NETWORK_ARCHITECTURE.md`) is based on a real Cisco Packet Tracer lab build — the routing, DHCP relay behavior, and the diagnosed connectivity incident are genuine, not hypothetical.

## Repository Structure

| File | Contents |
|---|---|
| `NETWORK_ARCHITECTURE.md` | Technical network topology, IP addressing, routing design (NIST CSF PR.IR) |
| `INCIDENT_RESPONSE_REGISTER.md` | Real troubleshooting incident, documented in formal GRC incident-register format (NIST CSF RS/DE) |
| `policies/` | Access Control, Incident Response, and Vendor Risk Management policies (NIST CSF PR/GV) |
| `risk-register.md` | Structured risk matrix — likelihood, impact, priority, control mapping (NIST CSF ID/GV) |
| `hardening-audit/` | CIS Benchmark–based audit checklist and validation script (NIST CSF PR/DE) |

## Framework Mapping

All deliverables reference **NIST CSF v2.0** core functions (Govern, Identify, Protect, Detect, Respond, Recover), with explicit subcategory citations in each document.

## About Me

I'm building toward a career in GRC and cybersecurity, with a focus on bridging policy with technical reality — this portfolio reflects that approach. I'm drawn to the field because compliance frameworks like NIST CSF only matter if they're actually enforced and verified on the ground, which is why every deliverable here pairs a policy or risk document with a technical artifact that proves or tests it. I built the underlying network in Cisco Packet Tracer, then diagnosed and resolved a real inter-site routing failure within it — and worked backward from that incident to show how it would be handled in a formal GRC context.

**Contact:** [LinkedIn](https://www.linkedin.com/in/kelvin-shepherd-423a7a15/) · [KelvinShepherd@gmail.com](mailto:KelvinShepherd@gmail.com) 


