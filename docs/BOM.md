# Bill of Materials — Mk I R0.8 Prototype

This BOM records the components around which the R0.8 mechanical geometry was designed. Electrical ratings and final wiring remain subject to verification.

## Printed parts

| Ref | Qty | Part | Release file |
|---|---:|---|---|
| ENC-001 | 1 | Main body | `MCH-MkI_body_R0.8` |
| ENC-002 | 1 | Branded locating-lip lid | `MCH-MkI_lid_R0.8` |
| ENC-003 | 1 | Peplink cable clamp | `MCH-MkI_peplink_strain_relief_R0.8` |
| TST-001 | 1 | Control fit coupon | `MCH-MkI_control_fit_coupon_R0.8` |
| TST-002 | 1 | Three-position USB-C fit coupon | `MCH-MkI_USB-C_panel_fit_coupon_R0.8` |
| TST-003 | 1 | Wire-exit fit coupon | `MCH-MkI_wire_exit_fit_coupon_R0.8` |
| TST-004 | 1 | Blue Sea 5045 fused-block riser coupon | `MCH-MkI_BlueSea5045_fused_block_riser_coupon_R0.8` |
| TST-005 | 1 | Unfused-busbar riser coupon | `MCH-MkI_unfused_busbar_riser_coupon_R0.8` |

Recommended enclosure material is PETG-CF printed on a Prusa CORE One with a hardened nozzle.

## Installed and interfacing hardware

| Ref | Qty | Item | Geometry/status |
|---|---:|---|---|
| CON-001 | 2 | Received USB-C cable-backed panel fitting | 12.70 × 6.35 mm pass-through; 25.40 × 7.62 mm rounded flange; screw-center coupon verification required |
| SW-001 | 1 | Master power switch | 38.55 × 20.77 mm cutout |
| DSP-001 | 1 | DC voltmeter | R0.5 fit-tested 45.17 × 26.39 mm cutout |
| FUS-001 | 1 | Blue Sea Systems 5045 compact four-circuit fuse block | 92.5 × 43.8 mm reserved; 65.1 mm boss centers |
| BUS-001 | 1 | Received unfused 12-position busbar | 137.16 × 38.10 × 22.86 mm cover; physically measured 114.30 mm mounting centers; included in R0.8 body |
| PWR-001 | As req. | USB-C PD interface/trigger board | Cradles based on 17.78 × 43.18 mm board plus 2.54 mm solder allowance |
| CAB-001 | 1 | Mobile Must Have fused Peplink DC cable | Bonded 20 AWG pair; 4.10 × 2.40 mm body exit and 4.55 × 2.70 mm clamp channel |
| HW-001 | 4 | M3 heat-set inserts | Verify pilot fit in PETG-CF |
| HW-002 | 4 | M3 lid screws | Length selected after insert installation |
| HW-003 | 2 | M3 clamp screws/inserts | Match strain-relief geometry |
| HW-004 | 2–4 | USB-C panel screws/nuts | M2.5 class; 2.8 mm printed clearance holes |
| HW-005 | 2 | Blue Sea mounting fasteners | M4-class; verify 3.6 mm printed pilot strategy |
| RET-001 | As req. | Miniature cable ties | For integrated tie-down tabs |
| INS-001 | As req. | Adhesive-lined heat shrink | Harness protection |
| WIR-001 | As req. | Appropriately rated stranded wire | Size from verified electrical loads and protection |

## External equipment

- Anker SOLIX C200 DC power source
- Peplink MAX BR1 Pro 5G
- Starlink Mini, positioned outside the enclosure
- iPad, normally powered directly from an available battery USB-C port

## Hold points

Before energized assembly:

1. Use the physically verified R0.5/R0.6 control dimensions.
2. Confirm both USB-C fittings using the three-position coupon and report which screw-center variant fits.
3. Confirm the bonded cable in the 4.10 × 2.40 mm exit and enlarged 4.55 × 2.70 mm clamp channel.
4. Select and document the M3 and M4 insert/fastener method.
5. Verify the exact PD module electrical profiles, ratings, polarity, and thermal behavior.
6. Establish final fuse and wire sizes from measured loads and manufacturer requirements.
7. Test both block coupons and verify that the selected 5.5 mm busbar mounting holes suit the supplied fasteners.
