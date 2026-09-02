<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
SCPN Muon Fusion Core — ADR 0001
-->

# ADR 0001 — Repository boundary and ownership

**Status:** accepted (2026-09-02)

**Deciders:** project owner (direct instruction of 2026-09-02); SCPN Reactor
Systems Research Group standard, section "Reserved extension projects"

## Context

The SCPN reactor portfolio assigns every built-in configuration of the SCPN
Phase Orchestrator reactor registry (release `1.0.0`, 32 configurations) to
exactly one device-family repository. Muon-catalysed fusion has no built-in
configuration: the family standard reserved the name
`SCPN-MUON-FUSION-CORE` and set three conditions for creating it — a
namespaced registry extension accepted by the orchestrator, a producer and
evidence class defined by the research group, and an owner-approved
boundary. On 2026-09-02 the owner directed the creation of the repository;
the group prepared registry release `1.1.0` with the namespaced extension
`scpn.reactor_systems:muon_catalysed_fusion` (family `extension`,
built-ins untouched), recorded it as pending in the family map, and
defined the producer and evidence class in its bootstrap plan.

## Decision

1. `SCPN-MUON-FUSION-CORE` owns exactly one registry configuration, the
   namespaced extension `scpn.reactor_systems:muon_catalysed_fusion`, and
   pins the prepared release `1.1.0` and its digest; the validator
   cross-checks the pin against the family map's pending block until the
   orchestrator lands the release.
2. The repository owns device-level truth only: target configuration
   policy (isotope fractions, density relative to liquid hydrogen density,
   temperature, phase, containment), muon-source declarations as a
   catalyst supply (rate, momentum, beam geometry), cycle-parameter
   declarations as inputs with their published ranges (cycling rate,
   sticking probability, muon lifetime), run lifecycle semantics with
   tritium, cryogenic and radiation hazard records, neutron- and
   muon-decay-anchored diagnostic and clock declarations,
   actuator-response model boundaries, the safety-envelope declaration,
   and the device-owned CONTROL adapter specification.
3. The muon source's accelerator physics is a facility interface, declared
   as a driver class only. Accelerator beam-on-target reaction kinematics
   stay with `SCPN-BEAM-TARGET-CORE` (the muon beam catalyses, it does not
   set the fusion kinematics); lattice confinement with
   `SCPN-LATTICE-FUSION-CORE`; fission blankets and the hybrid concepts of
   the muon literature with `SCPN-FUSION-FISSION-HYBRID-CORE`; thermal
   confinement of every kind with the magnetic, inertial and
   magneto-inertial families.
4. The family makes no energy-gain statement. With the published sticking
   probability (about 0.45 %) and cycle count (about 150 per muon) the
   catalysed yield per muon is below the muon's production cost (of order
   GeV), and the repository carries no path around that fact; every model
   landing carries that statement as a non-claim. Sources on file:
   the 2026 review of the catalytic cycle (arXiv 2605.26432), the
   sticking analysis (arXiv physics/0605206) and the D–T target delivery
   design (arXiv 2606.19304); the paywalled classics (Jackson 1957,
   Breunlich et al. 1989) are cited, not copied.
5. Solver mathematics remains in `SCPN-FUSION-CORE` until an exact surface
   passes the family migration gate. No solver code is copied here.
6. Typed semantics remain in `SCPN-PHASE-ORCHESTRATOR` (review-only).
   Admission and `ControlAction` formation remain exclusively in
   `SCPN-CONTROL`. Machine protection remains independent with the final
   veto. Presentation remains in `SCPN-STUDIO`; this project is
   `not_federated`.
7. The repository starts, and remains until evidenced otherwise, at
   `architecture_only` with empty capability and claim inventories.

## Alternatives considered

- **Folding the family into `SCPN-BEAM-TARGET-CORE`** (a beam meets a
  target): rejected — the muon beam sets no reaction kinematics; the
  defining quantities are the catalytic-cycle kinetics and the sticking
  loss, absent from the beam-target boundary.
- **A built-in registry configuration** instead of a namespaced
  extension: rejected — the standard's route for reserved projects is the
  namespaced extension, which leaves the 32 built-ins and every existing
  pin untouched.
- **Waiting for the orchestrator to land the release first**: rejected by
  the owner's instruction; the prepared release is pinned exactly and the
  family map carries it as pending, so the eventual landing is a re-pin
  only if the digest differs.

## Consequences

The family map gains one planned repository and one namespaced
assignment; the orchestrator receives a prepared patch and lands the
release under its own gates; until then this repository validates against
the pending block. Every later capability is a separately evidenced
landing under this boundary; the non-claim of item 4 is permanent.
