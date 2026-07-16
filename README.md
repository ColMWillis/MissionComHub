# Mission Communications Hub Mk I

**Branding:** Mission Communications Hub / Mk I / GAWG CAP

MissionComHub is an open hardware project to develop a portable, serviceable communications and power-distribution appliance for Civil Air Patrol aircraft, ground vehicles, and mission-base use.

## Milestone 1 status

This repository baseline defines the mechanical requirements for the Mk I enclosure. CAD geometry is intentionally not marked production-ready until the exact panel components are selected and measured.

## Initial capability

- USB-C Power Delivery input from an Anker SOLIX C200 DC or equivalent source
- Regulated 12 VDC internal bus
- Four individually fused Anderson Powerpole outputs
- Master power control and voltage indication
- Removable internal electronics sled
- AMPS-compatible mounting provisions
- Expansion volume for networking and embedded-computing modules

## Repository layout

- `CAD/` — native CAD, STEP, STL, 3MF, and drawings
- `Electronics/` — schematics, harness drawings, and electrical data
- `Firmware/` — reserved for future monitoring and control software
- `docs/` — requirements, design specification, BOM, assembly, and test plans
- `images/` — renders, photographs, and diagrams
- `.github/` — issue and pull-request templates

## Project phase

Current phase: **Milestone 1 — Mechanical definition and prototype enclosure**.

See [`docs/design-spec.md`](docs/design-spec.md) and [`docs/requirements.md`](docs/requirements.md).

## Safety and approval

This is experimental, portable mission-support equipment. It is not certified avionics and must not be connected to aircraft electrical systems or installed in a manner that interferes with aircraft controls, emergency egress, weight and balance, antenna systems, or required equipment without appropriate CAP and aircraft-owner approval.

## License

Documentation and mechanical designs are released under CERN-OHL-P-2.0 unless a file states otherwise. Software, when added, should use the MIT License.
