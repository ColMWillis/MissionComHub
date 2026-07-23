# Changelog

## [Unreleased]

- Confirmed the unfused-busbar fit at 120.65 mm (4.75 inch) mounting centers.
- Added a single-position R0.8C USB-C coupon at 18.55 mm after 18.60 mm remained just outside tolerance.
- The R0.8 body remains unchanged until the 18.55 mm USB fit is confirmed; the next body revision will incorporate both final values.

## [R0.8] — 2026-07-22

### Changed

- Refactored both USB-C openings around the received 12.70 × 6.35 mm pass-through body and 25.40 × 7.62 mm rounded flange.
- Enlarged the enclosure from 140 × 90 × 52 mm to 146 × 96 × 52 mm so the covered unfused busbar and Blue Sea 5045 can mount side-by-side.
- Replaced provisional unfused-busbar slots with fixed mounting holes at the physically measured 114.30 mm centers.
- Relocated the lid posts and internal tie-downs to clear both power-block envelopes.
- Removed obsolete PCB-backed USB shelves; the received interfaces are cable-backed fittings.

### Added

- Three-position USB-C fit coupon using 18.80, 19.05, and 19.30 mm screw-center variants.
- Automated conservative-envelope clearance checks for both power blocks and the enclosure.

## [R0.7] — 2026-07-22

### Changed

- Corrected the outside-reading orientation of the `BATTERY`, `STARLINK`, and `PEPLINK` body labels.
- Added `VOLTAGE` and `POWER` labels to the outside control face.
- Preserved the verified control openings, 4.10 × 2.40 mm Peplink exit, and 4.55 × 2.70 mm strain-relief channel.

### Added

- Blue Sea 5045 fused-block riser coupon using the documented 65.1 mm mounting centers.
- Provisional full-envelope coupon for the supplied 137.16 × 38.10 × 22.86 mm unfused busbar.

### Hold point

- The unfused busbar cover is 3.16 mm longer than the enclosure's 134 mm internal length. Its body mounting remains deferred until the physical component and final orientation are verified.

## [R0.6] — 2026-07-22

### Changed

- Preserved the physically verified R0.5 switch and voltmeter openings.
- Selected the smallest successful Peplink wire-coupon opening: 4.10 × 2.40 mm.
- Enlarged the strain-relief cable channel by 0.50 mm overall in width and height, to 4.55 × 2.70 mm.
- Preserved the 18 × 10 mm clamp footprint and screw spacing.

## [R0.5] — 2026-07-22

### Changed

- Widened the R0.4 voltmeter opening by 1.00 mm overall, adding 0.50 mm on the left and right.
- Retained the verified 26.39 mm voltmeter-opening height.
- Final voltmeter cutout: 45.17 × 26.39 mm.

### Added

- Synchronized STEP, STL, and 3MF files.
- Parametric CadQuery generator.
- Fit coupons, dimensions manifest, validation report, checksums, preview, and complete ZIP release.

## [R0.4] — 2026-07-22

- Reduced the R0.3 voltmeter opening by 2.00 mm in width and height after the first physical coupon rattled.
- Voltmeter cutout was 44.17 × 26.39 mm.

## [R0.3] — 2026-07-21

- Replaced generic USB-C openings with AAOTOKK panel-mount geometry.
- Added Blue Sea 5045 mounting bosses and reserved footprint.
- Added cable-routing rails and tie-down tabs.
- Resized the Peplink exit and clamp for the measured 3.81 × 2.03 mm bonded 20 AWG cable.
- Added `BATTERY`, `STARLINK`, and `PEPLINK` labels.
- Corrected inherited lid-lip interference and preserved the removable branded lid.
- Generated and cross-validated STEP, STL, and 3MF exports.

## [Milestone 1 baseline]

- Established the initial repository, conceptual requirements, documentation, and contribution workflow.
