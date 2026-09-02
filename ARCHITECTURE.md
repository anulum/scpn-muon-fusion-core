<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
SCPN Muon Fusion Core — Architecture summary
-->

# Architecture summary

`SCPN-MUON-FUSION-CORE` is the device-family owner for muon-catalysed
fusion research inside the SCPN Reactor Systems Research Group. The
repository is `architecture_only`: it holds the device boundary, its
ecosystem contracts, and the validation tooling that enforces the
truthfulness of that state, and no implemented reactor capability.

The authoritative architecture record is
[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md). The ownership decision and
its consequences are fixed in
[`docs/adr/0001-repository-boundary.md`](docs/adr/0001-repository-boundary.md).

Boundary in one paragraph: this repository owns muon-catalysed plant and
experiment truth — configuration policy for cold dense hydrogen-isotope
targets in which externally supplied negative muons form muonic molecules
and catalyse fusion within the muon lifetime, run-oriented lifecycle
semantics (source conditioning, target fill, catalysis run, tritium
accounting) with tritium, cryogenic and radiation hazards, neutron- and
muon-decay-anchored diagnostic and clock declarations, actuator-response
boundaries limited to run-to-run programming, safety-envelope
declarations, and the device-owned CONTROL adapter specification. The muon
source's accelerator physics is a facility interface only; beam-defined
reaction kinematics stay with `SCPN-BEAM-TARGET-CORE`; lattice confinement
with `SCPN-LATTICE-FUSION-CORE`; fission blankets with
`SCPN-FUSION-FISSION-HYBRID-CORE`; solver mathematics in
`SCPN-FUSION-CORE`; typed semantics in `SCPN-PHASE-ORCHESTRATOR`
(review-only); admitted control actions are formed only by `SCPN-CONTROL`;
independent machine protection keeps the final veto; portfolio
presentation belongs to `SCPN-STUDIO`, towards which this project is
`not_federated`.
