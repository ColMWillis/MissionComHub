# Mk I R0.10 USB-PD Carrier Test Plan

## Automated release validation

| Test ID | Method | Pass criterion | R0.10 |
|---|---|---|---|
| T-A-001 | Inspect every STL and 3MF mesh | Watertight, consistent winding, positive volume | Pass |
| T-A-002 | Compare matching STL and 3MF extents | Agreement within 0.02 mm | Pass |
| T-A-003 | Inspect 3MF package | Valid structure; millimeter units | Pass |
| T-A-004 | Re-import each STEP | At least one valid positive-volume solid | Pass |
| T-A-005 | Measure body mesh | 146 × 96 × 52 mm within 0.02 mm | Pass |
| T-A-006 | Intersect assembled body and lid STEP solids | No interference above 0.05 mm³ | Pass: 0 mm³ |
| T-A-007 | Read dimensions manifest | Voltmeter opening equals 45.17 × 26.39 mm | Pass |
| T-A-008 | Read dimensions manifest | Peplink exit equals 4.10 × 2.40 mm | Pass |
| T-A-009 | Read dimensions manifest | Strain-relief channel equals 4.55 × 2.70 mm | Pass |
| T-A-010 | Inspect block coupon exports | Both coupons are watertight and have matching STL/3MF extents | Pass |
| T-A-011 | Intersect conservative component envelopes | Fused block, unfused busbar, and body have zero intersection above risers | Pass |
| T-A-012 | Assemble carrier STEP below lid | Carrier has zero intersection with body and both power blocks | Pass |
| T-A-013 | Intersect two conservative 8 mm-deep card envelopes | Cards have zero intersection with body and both power blocks | Pass |
| T-A-014 | Measure vertical card-to-busbar clearance | Greater than 4.0 mm | Pass: 4.84 mm |

Detailed values are in `CAD/Releases/R0.10/VALIDATION.md` and `validation_report.json`.

## Physical fit tests

| Test ID | Method | Pass criterion |
|---|---|---|
| T-F-001 | Fit switch in control coupon | Fully retained; no coupon distortion |
| T-F-002 | Fit voltmeter in R0.6 control coupon | Seats without rattle or excessive insertion force |
| T-F-003 | Fit received USB-C connector | Confirm the final 18.55 mm interface seats without force or movement |
| T-F-004 | Fit Peplink cable in the 4.10 × 2.40 mm opening | Passes without insulation damage |
| T-F-005 | Tighten cable clamp | Cable resists a gentle pull without visible crushing |
| T-F-006 | Fit Blue Sea 5045 | Both mounting points align at 65.1 mm centers |
| T-F-007 | Fit unfused busbar on final coupon | Base rests flat; both confirmed 120.65 mm mounting points align; supplied screws clear the 5.5 mm holes |
| T-F-008 | Inspect outside labels | BATTERY, STARLINK, PEPLINK, VOLTAGE, and POWER are readable from outside |
| T-F-009 | Fit both USB-PD cards in carrier | Cards seat between guides without force; solder extensions remain clear |
| T-F-010 | Secure each PD card with two zip ties | No card movement and no board/component crushing |

## Mechanical prototype tests

| Test ID | Method | Pass criterion |
|---|---|---|
| T-M-001 | Measure printed body | Within printer-calibrated tolerance of 146 × 96 × 52 mm |
| T-M-002 | Cycle lid screws 20 times | No stripped insert, crack, or loss of retention |
| T-M-003 | Open and close lid 20 times | Lip remains self-aligning without binding |
| T-M-004 | Shake non-energized assembled enclosure by hand | No loose hardware or component movement |
| T-M-005 | Inspect cable routes with lid installed | No wire contacts screw tips or sharp edges |
| T-M-006 | Remove and reinstall populated carrier 10 times | No insert movement, cracking, or loss of card retention |
| T-M-007 | Seat lid over populated carrier and power blocks | No compressed card, solder joint, component, or wire |
| T-B-001 | Inspect lid | All three branding lines are legible and centered |

## Electrical and thermal tests

These require a completed documented harness and are not satisfied by CAD validation.

| Test ID | Method | Pass criterion |
|---|---|---|
| T-E-001 | Continuity and polarity inspection before power | No short; every output polarity correct |
| T-E-002 | Peplink-only test | Stable boot and operation; no abnormal heat |
| T-E-003 | Starlink-only test | Stable boot and operation; no abnormal heat |
| T-E-004 | Combined maximum intended load for 30 minutes | No reset, odor, discoloration, hot cable, or unsafe temperature |
| T-E-005 | Verify fuse behavior using a safe test method | Correct branch interruption without harness damage |

## Deferred operational screening

- hot-soak dimensional stability
- vibration and connector-retention screening
- padded-transport drop screening
- sunlight and cockpit-temperature exposure
- restraint evaluation in each proposed aircraft or vehicle
- CAP and aircraft-owner operational approval
