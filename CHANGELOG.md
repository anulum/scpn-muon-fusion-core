<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
SCPN Muon Fusion Core — CHANGELOG
-->

# Changelog

## [Unreleased]

### Changed

- Install every CI dependency from hash-locked requirement sets with
  `--require-hashes`: the development toolchain, the audit and inventory
  tools. `make lock` regenerates the sets. Toolchain, action and interpreter
  pins move to their newest releases.

### Added

- Repository established as the architecture-only Tier-0 device-family
  repository for muon-catalysed fusion research (ADR 0001): the domain
  manifest pinning the prepared reactor registry release `1.1.0` with the
  namespaced extension configuration
  `scpn.reactor_systems:muon_catalysed_fusion`, a validator that admits
  namespaced identifiers and cross-checks a pending registry release
  against the family map, the derived Studio descriptor
  (`not_federated`), the generated empty capability inventory, the
  CONTROL adapter specification (`0.1.0-spec`, no implementation), the
  threat model, the uniform gate and workflow surfaces of the research
  group, and the manuscript collection skeleton. No reactor capability,
  claim, benchmark, dataset or deployable artefact exists, and no
  energy-gain statement is made.
