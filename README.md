<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
SCPN Muon Fusion Core — README
-->

# SCPN Muon Fusion Core

Governed device-family repository for muon-catalysed fusion research
within the SCPN Reactor Systems Research Group. This repository is the
designated owner of device-level truth for the namespaced extension
configuration `scpn.reactor_systems:muon_catalysed_fusion` of the SCPN
Phase Orchestrator reactor registry (release `1.1.0`, prepared by the
group as a namespaced extension of the 32 built-in configurations and
carried in the family map as a pending release until the orchestrator
lands it).

**Evidence maturity: `architecture_only`.** No reactor capability is
implemented: the repository holds the device boundary, its ecosystem
contracts, the device-owned CONTROL adapter specification and the
validation tooling that enforces the truthfulness of that state. The
capability and claim inventories are empty and verified by the domain
validator.

## Scope

This repository owns, for the muon-catalysed device family:

- the device boundary: plant and experiment truth, run lifecycle, and
  configuration policy for systems in which negative muons supplied by an
  external source form muonic molecules in a cold, dense hydrogen-isotope
  target and catalyse fusion in a cycle bounded by the muon lifetime
  (2.197 µs), the cycling rate and the alpha-sticking probability (about
  0.45 % and about 150 cycles per muon in the published experimental
  record);
- target and cycle semantics as device truth: isotope fractions, density
  relative to liquid hydrogen density, temperature, phase and containment;
  muon-source declarations (rate, momentum, beam geometry) as a catalyst
  supply, never as a reaction driver of declared kinematics; cycle
  parameters (cycling rate, sticking probability, lifetime) as inputs with
  their published ranges, never as claims;
- diagnostic semantics, reference frames, and clock identity declarations
  (fusion-neutron counting, muon-decay electron detection, muon-arrival
  timing, tritium-inventory accounting);
- actuator-response model boundaries and the declared safety envelope
  (tritium inventory, cryogenics, radiation);
- the device-owned CONTROL adapter specification;
- the binding to the SCPN Phase Orchestrator reactor registry (release
  `1.1.0`, digest
  `6741f25892d81b24aa621ee4f56b5e785e8323eca6ccf9d9009ce2c8e53f4912`);
- the machine-readable domain manifest `reactor-domain.json` and the derived
  Studio portfolio descriptor (integration state `not_federated`).

## Explicit exclusions

- **Muon-source accelerator physics** (proton driver, pion production and
  decay channel, muon transport): a facility interface, declared as a
  driver class only; its physics is not owned here.
- **Accelerator beam-on-target reaction kinematics**:
  `SCPN-BEAM-TARGET-CORE`. The muon beam catalyses; it does not set the
  fusion kinematics.
- **Lattice-confinement fusion**: `SCPN-LATTICE-FUSION-CORE`.
- **Fission blankets and hybrid plant systems**:
  `SCPN-FUSION-FISSION-HYBRID-CORE` (the hybrid concepts discussed in the
  muon literature are out of this boundary).
- **Thermal plasma confinement of every kind**: the magnetic, inertial and
  magneto-inertial device families of the group.
- **Solver mathematics and validation evidence**: `SCPN-FUSION-CORE` until
  an exact surface passes the reactor family migration gate; no solver code
  exists in, or was copied into, this repository.
- **Typed signal semantics and comparability**: `SCPN-PHASE-ORCHESTRATOR`
  (review-only output; never actuation).
- **Control admission and action formation**: `SCPN-CONTROL` is the sole
  software authority that forms an admitted `ControlAction`.
- **Machine protection**: independent systems retain the final veto.
- **Portfolio presentation, identity, entitlement, and execution gating**:
  `SCPN-STUDIO`.

## Non-claims

This repository is not machine-ready, not safety-certified, and not
reactor-ready. It contains no implemented solver, no controller, no
benchmark result, no experimental correlation, no dataset, and no
deployable artefact, and no parameter describes or validates any real
apparatus. No energy-gain statement is made or implied: with the
published sticking probability and cycle count the catalysed yield per
muon is below the muon's production cost, and the repository carries no
path around that fact; every future model repeats it. Target-mixture,
density and source choices are configuration facets, not separate claims.
No capability has reached any evidence-maturity state.

## Architecture

The five-surface boundary and the position of this repository in the SCPN
ecosystem are defined in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and
fixed by
[`docs/adr/0001-repository-boundary.md`](docs/adr/0001-repository-boundary.md).
The threat model is in [`docs/THREAT_MODEL.md`](docs/THREAT_MODEL.md); the
CONTROL adapter contract is in
[`docs/CONTROL_ADAPTER_SPECIFICATION.md`](docs/CONTROL_ADAPTER_SPECIFICATION.md).

## Validation

Every gate currently active in this repository is listed in
[`VALIDATION.md`](VALIDATION.md). The local sequence is:

```bash
make lint        # ruff check + ruff format --check
make typecheck   # mypy --strict tools tests
make test        # pytest with 100 % statement and branch coverage on tools/
make validate    # domain manifest, descriptor, and inventory checks
make preflight   # the full fail-closed gate sequence
```

## Security

See [`SECURITY.md`](SECURITY.md) for the supported states and the private
reporting route (protoscience@anulum.li).

## Licensing

AGPL-3.0-or-later for the public repository, with a commercial licence
available (see [`NOTICE.md`](NOTICE.md)). Licence texts are under
[`LICENSES/`](LICENSES/); machine-readable licensing metadata follows
REUSE 3.x (`REUSE.toml`).

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). No release,
version, or DOI exists yet; cite the repository state you inspected.
