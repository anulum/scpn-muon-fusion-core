<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
SCPN Muon Fusion Core — ROADMAP
-->

# Roadmap

Planned work and implemented capability are kept strictly separate. Anything
listed under "Planned" carries no implementation, no code, and no claim in
this repository until it appears in the capability inventory with evidence.

## Implemented (repository infrastructure, not reactor capability)

- Domain manifest (`reactor-domain.json`) with validator, pinning the
  prepared registry release `1.1.0` and validating it against the family
  map's pending block.
- Derived Studio portfolio descriptor (`not_federated`) with drift check.
- Generated capability inventory (truthfully empty) with drift check.
- CONTROL adapter specification (contract only, no implementation).
- Local and workflow gate definitions (lint, typing, tests, coverage,
  REUSE, typographical check, commit-trailer guard, workflow modularity
  guard, security audit, SBOM, documentation checks).

## Planned (no implementation exists; ordering is not a commitment)

1. **Device configuration model** — typed configuration policy for the
   family (target isotope fractions, density relative to liquid hydrogen
   density, temperature and phase, containment class; muon-source rate,
   momentum and geometry; cycle parameters with their published ranges)
   with the closed-form cycles-per-muon estimate of the kinetic model as
   the documented consistency instrument, targeting
   `computational_prototype`.
2. **Diagnostic and clock semantics** — declared source, target-state,
   muon-arrival, neutron and muon-decay channels with arrival-anchored
   clock identities, aligned with the SCPN Phase Orchestrator
   observability catalogue.
3. **Level-0 device physics** — closed forms of the published kinetic
   model of the catalytic cycle (cycles per muon from the cycling rate,
   the lifetime and the sticking probability; fusion energy per muon
   against the declared muon production cost) evaluated on the validated
   configuration and anchored to the sources' printed numbers, with native
   parity; planned before code in the group's family plan.
4. **Safety-envelope declaration** — machine-readable operational envelope
   (tritium inventory, target pressure and temperature, source bounds,
   radiation) consumed by the CONTROL adapter contract.
5. **CONTROL adapter implementation** — device-owned adapter against the
   published specification, with replay fixtures and HIL evidence,
   targeting `control_research_ready` only after replay and HIL
   acceptance.
6. **Facility-data correlation** — preregistered acceptance contracts
   against identified published experimental data, targeting
   `experiment_correlated` per capability.

## Not planned in this repository

Muon-source accelerator physics, beam-defined reaction kinematics,
lattice confinement, fission blankets and hybrid plants, thermal plasma
confinement of every kind, generic controller mathematics,
machine-protection logic, any direct actuation path, and any energy-gain
statement.
