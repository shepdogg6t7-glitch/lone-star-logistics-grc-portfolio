# Lone Star Logistics — Corporate Network Architecture Report

**Document ID:** LSL-ARCH-NET-001 — Distributed Hub-and-Spoke Infrastructure
**Classification:** Internal Technical Documentation
**Framework Mapping:** NIST CSF v2.0 — PR.IR-01 (Networks/Environments Protected), PR.IR-02 (Architecture Resilience)

---

## 1. Executive Summary & Topology Design

Lone Star Logistics operates a hub-and-spoke network topology supporting continuous supply chain coordination across three sites:

- **Central HQ Hub** — corporate operations, centralized DHCP, core directory services
- **Spoke Site 1 (Sales Office)** — client onboarding, billing pipelines, dispatch routing
- **Spoke Site 2 (Warehouse/Distribution)** — real-time inventory, cargo loading, fleet coordination

```
                [ HQ Hub ]  (Central Services / DHCP)
                    ▲   ▲
     Dedicated WAN  │   │  Dedicated WAN
     Transit Subnet │   │  Transit Subnet
                    ▼   ▼
        [ Spoke 1: Sales ]   [ Spoke 2: Warehouse ]
```

## 2. IP Addressing & Network Services

### 2.1 IPv4 Subnetting Strategy

| Segment | Subnet | Purpose |
|---|---|---|
| HQ Core LAN | `10.100.0.0/24` | Central DHCP, IAM services |
| Spoke 1 (Sales) LAN | `10.101.0.0/24` | Sales office endpoints |
| Spoke 2 (Warehouse) LAN | `10.102.0.0/24` | Warehouse endpoints |
| WAN Transit Links | `/30` point-to-point | HQ ↔ each spoke |

### 2.2 Centralized DHCP (Relay)

- Centralized DHCP server at HQ Hub (`10.100.0.10`)
- Spoke gateway routers configured with `ip helper-address 10.100.0.10` on their local inbound interfaces
- **Verified via Simulation-mode PDU capture:** local Layer 2 DHCP Discover broadcasts from client PCs are intercepted by the spoke gateway, converted to Layer 3 unicast, and routed across the WAN transit link to HQ

## 3. Routing Architecture

### 3.1 Static Routing

Static routes provisioned on all three routers, including explicit return routes so inter-spoke traffic (Spoke 1 LAN ↔ Spoke 2 LAN) transits through the HQ Hub.

### 3.2 OSPF (Dynamic Backup)

OSPF Process ID 1, Area 0, deployed alongside static routing to provide automated failover. Neighbor adjacencies and LSDB state verified via `show ip ospf neighbor`.

## 4. Packet-Level Behavior Analysis

Captured via Packet Tracer Simulation mode:

- **MAC rewriting per hop:** ICMP echo traffic from Spoke 1 to Spoke 2 shows Layer 3 source/destination IPs remaining unchanged end-to-end, while Layer 2 source/destination MAC addresses are rewritten at every router hop to match the outbound interface and next-hop hardware address.
- **TTL decrement:** TTL field decreases by exactly `1` at each hop, consistent with standard loop-prevention behavior.
- **OSPF multicast:** OSPF Hello packets use the reserved multicast address `224.0.0.5` rather than a broadcast, limiting adjacency traffic to OSPF-speaking routers only.

---
*This document maps a hands-on Packet Tracer lab to a fictitious organization (Lone Star Logistics) for portfolio purposes. Technical configuration and behavior described reflect the actual lab build.*
