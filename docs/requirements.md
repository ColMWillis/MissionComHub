# Mk I R0.8 Requirements

Requirement identifiers remain stable. Retired conceptual requirements are preserved and not reassigned.

## Mechanical

- MCH-M-001: The R0.8 body shall measure 146 × 96 × 52 mm.
- MCH-M-002: The enclosure shall use a separate body and removable locating-lip lid.
- MCH-M-003: Lid service points shall use M3 machine-screw positions suitable for inserts.
- MCH-M-004: **Retired** — removable electronics sled.
- MCH-M-005: **Retired** — replaceable front and rear panels.
- MCH-M-006: **Deferred** — AMPS mounting pattern.
- MCH-M-007: **Deferred** — integrated 25 mm strap paths.
- MCH-M-008: The enclosure shall have rounded external corners and no sharp cable-contact edges.
- MCH-M-009: Normal lid and strain-relief service shall not require destructive removal of printed parts.
- MCH-M-010: Blue Sea 5045 bosses shall use 65.1 mm mounting centers.
- MCH-M-011: The Peplink body exit shall use the physically verified 4.10 × 2.40 mm opening.
- MCH-M-012: Internal routing features shall retain wiring away from fuse terminals and lid screws.
- MCH-M-013: The strain-relief cable channel shall measure 4.55 × 2.70 mm while preserving the R0.5 clamp footprint and screw spacing.
- MCH-M-014: The Blue Sea 5045 and unfused busbar shall each have a printable mounting-fit coupon.
- MCH-M-015: The unfused busbar shall mount at the physically measured 114.30 mm centers.
- MCH-M-016: The covered unfused busbar and Blue Sea 5045 envelopes shall not intersect the body or each other above their mounting risers.

## Printing and release

- MCH-P-001: Every primary printed part shall fit the Prusa CORE One build volume.
- MCH-P-002: Primary parts shall be printable in PETG-CF with a hardened 0.4 mm nozzle.
- MCH-P-003: No inaccessible support material shall be required.
- MCH-P-004: Each release shall include STEP, STL, and 3MF files generated from one parametric source.
- MCH-P-005: Every 3MF shall declare millimeter units and match its corresponding STL dimensions.
- MCH-P-006: Control, USB-C, wire-exit, fused-block, and unfused-block fit coupons shall be supplied.

## Interfaces

- MCH-I-001: **Retired** — four Anderson Powerpole output positions.
- MCH-I-002: **Retired** — PEPLINK/STARLINK/AUX 1/AUX 2 Powerpole labels.
- MCH-I-003: The enclosure shall provide one received-style USB-C panel position labeled `BATTERY`.
- MCH-I-004: The enclosure shall provide one master-switch opening.
- MCH-I-005: The enclosure shall provide one fit-tested voltage-display opening.
- MCH-I-006: **Retired** — expansion blanking plates.
- MCH-I-007: The enclosure shall provide one received-style USB-C panel position labeled `STARLINK`.
- MCH-I-008: The enclosure shall provide one bonded-cable exit labeled `PEPLINK`.
- MCH-I-009: The I/O labels shall read correctly when viewed from outside the enclosure.
- MCH-I-010: The control face shall be labeled `VOLTAGE` and `POWER`.
- MCH-I-011: Each USB-C interface shall provide a 13.20 × 6.85 mm rounded pass-through and a 25.80 × 8.02 mm rounded flange recess.

## Branding

- MCH-B-001: The lid shall display `Mission Communications Hub`.
- MCH-B-002: The lid shall display `Mk I`.
- MCH-B-003: The lid shall display `GAWG CAP`.
- MCH-B-004: Branding shall remain legible in a single-color print.

## Safety and serviceability

- MCH-S-001: No energized conductor shall be finger-accessible with the lid installed.
- MCH-S-002: External cable loads shall be transferred to panel hardware or strain relief rather than solder joints.
- MCH-S-003: The Peplink bonded cable shall use the printed two-screw strain-relief clamp.
- MCH-S-004: Circuit protection, wire sizing, and component ratings shall be verified before energized operation.
- MCH-S-005: Internal wiring shall be retained away from lid fasteners and fuse terminals.
- MCH-S-006: This prototype shall not be represented as certified avionics.

## Documentation

- MCH-D-001: Each release shall include a BOM.
- MCH-D-002: Each release shall include assembly guidance.
- MCH-D-003: Each release shall include a dimensions manifest.
- MCH-D-004: Each release shall include automated validation results and checksums.
- MCH-D-005: Physical coupon-fit feedback shall be recorded in the changelog.
