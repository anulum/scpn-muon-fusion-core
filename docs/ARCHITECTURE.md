<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
SCPN Muon Fusion Core — Architecture
-->

# Architecture

## Purpose and evidence state

`SCPN-MUON-FUSION-CORE` is the device-family owner for muon-catalysed
fusion research in the SCPN Reactor Systems Research Group portfolio. The
repository is `architecture_only`: every section below describes
boundaries and contracts; no implemented reactor capability exists, and
the capability and claim inventories are generated, empty, and
drift-checked.

## The five-surface boundary

1. **Governing physics** — catalysis of hydrogen-isotope fusion by
   negative muons: a muon stopped in a cold dense D/T (or D/D) target
   forms a muonic atom, then a muonic molecule whose nuclei are bound
   about two hundred times closer than in an ordinary molecule and fuse;
   the muon is released and repeats the cycle until it decays (lifetime
   2.197 µs) or sticks to the alpha particle (published sticking
   probability about 0.45 %), giving about 150 catalysis cycles per muon
   in the experimental record. The defining physics is the kinetics of
   that cycle against the muon lifetime and the sticking loss, not a
   thermal plasma and not a beam-defined kinematics. The published energy
   cost of a muon (of order GeV) exceeds the catalysed yield; no gain is
   declared.
2. **Primary driver and energy delivery** — an external muon source
   (proton driver, pion production and decay channel, muon transport) is
   a facility interface declared by rate, momentum and beam geometry; the
   target's cryogenic containment and density control are the device's
   own systems.
3. **Plant and shot lifecycle** — run-oriented lifecycle: source
   conditioning, target fill and density setting, catalysis run with
   neutron counting, tritium-inventory accounting and run end. Device-level
   hazard semantics cover tritium inventory and release, cryogenic
   containment, and the radiation field of the source and the fusion
   neutrons.
4. **Diagnostic, reference-frame, and clock model** — target-cell and
   beamline coordinate conventions, muon-arrival timing, fusion-neutron
   counting with declared efficiency and background definitions,
   muon-decay electron detection, and clock identities anchored to the
   muon-arrival event with declared resolution.
5. **Solver, evidence, and control-contract boundary** — versioned seams
   towards `SCPN-FUSION-CORE`, review-only semantics towards
   `SCPN-PHASE-ORCHESTRATOR`, and the device-owned CONTROL adapter
   specification towards `SCPN-CONTROL`.

## Position in the SCPN ecosystem

```
SCPN-FUSION-CORE ──(versioned seams, none active)──► SCPN-MUON-FUSION-CORE
                                                            │
                          reactor registry 1.1.0 ◄──── manifest pin
                                                            │
SCPN-PHASE-ORCHESTRATOR ◄──(review-only semantics)──────────┤
                                                            │
SCPN-CONTROL ◄──(adapter specification, no actuation)───────┤
                                                            │
SCPN-STUDIO ◄──(derived descriptor, not_federated)──────────┘

SCPN-CONTROL ──admitted ControlAction──► independent machine protection ──► plant
```

The reactor registry configuration this repository owns is a namespaced
extension (`scpn.reactor_systems:muon_catalysed_fusion`, family
`extension`) prepared by the research group for registry release `1.1.0`
under the family standard's route for reserved projects; the family map
carries that release as pending until the orchestrator lands and
acknowledges it, and this manifest pins the prepared release and digest.

## Repository layout

| Path | Role |
|---|---|
| `reactor-domain.json` | portable source of project identity and contracts |
| `studio/portfolio-descriptor.json` | derived Studio descriptor, `not_federated` |
| `capability-inventory.json` | generated, truthfully empty inventory |
| `docs/CONTROL_ADAPTER_SPECIFICATION.md` | device-owned adapter contract |
| `docs/THREAT_MODEL.md` | assets, trust boundaries, misuse paths |
| `docs/adr/0001-repository-boundary.md` | boundary decision record |
| `papers/` | authoritative manuscript collection (empty until a manuscript exists) |
| `tools/` | validators, derivation tools, workflow guard, preflight orchestrator |
| `tests/` | statement- and branch-complete tests for `tools/` |
| `.github/workflows/` | read-only CI definitions (no publication) |

## Contract surfaces and versioning

- `reactor-domain.json` follows schema `scpn.reactor-domain.v1`; unknown
  schemas are rejected by consumers.
- The Studio descriptor is derived deterministically and embeds the
  manifest's SHA-256; manual edits are detected as drift.
- The CONTROL adapter contract is specification-only at `0.1.0-spec`.
- SPO binding is fixed to reactor registry `1.1.0`, digest
  `6741f25892d81b24aa621ee4f56b5e785e8323eca6ccf9d9009ce2c8e53f4912`
  (the prepared group extension release); the validator cross-checks it
  against the family map's pending block until the release lands, and
  against the map's source registry afterwards.

## What would change this architecture

Landing of registry `1.1.0` by the orchestrator (a re-pin only if its
digest differs from the prepared one), acceptance of a FUSION solver seam
through the family migration gate, ratification of an SPO
`ControlIntent`-class contract, or Studio federation after a real
capability passes producer and consumer gates — each recorded as a
versioned contract change in a new ADR.
