# R0.12 Side-by-Side PD Carrier and Lid Validation Report

All matching STL, 3MF, and STEP exports passed automated validation.

R0.12 preserves the verified **45.17 × 26.39 mm** voltmeter cutout.

Peplink body exit: **4.10 × 2.40 mm**. Strain-relief channel: **4.55 × 2.70 mm**.

The USB-C panel geometry uses the received 12.70 × 6.35 mm pass-through and 25.40 × 7.62 mm rounded flange.

The body and final coupons use confirmed **18.55 mm USB** and **120.65 mm bus-bar** mounting centers.

The compact removable carrier holds two side-by-side **45.72 × 17.78 mm** card envelopes and attaches to four blind M3 insert bosses under the lid.

Both attached USB plug envelopes and both 20 mm screw-terminal wire-service envelopes clear the body and power blocks.

The 38.10 mm-deep switch envelope has zero intersection with either swapped power block.

| Part | Watertight | STL/3MF match | STEP solids | Extents (mm) |
|---|---:|---:|---:|---|
| MCH-MkI_BlueSea5045_fused_block_riser_coupon_R0.12 | Yes | Yes | 1 | 100 × 52 × 9.2 |
| MCH-MkI_USB-C_final_fit_coupon_R0.12 | Yes | Yes | 1 | 36 × 34 × 3.2 |
| MCH-MkI_body_R0.12 | Yes | Yes | 1 | 146 × 96 × 103 |
| MCH-MkI_control_fit_coupon_R0.12 | Yes | Yes | 1 | 105 × 42 × 3.2 |
| MCH-MkI_dual_USB-PD_card_carrier_R0.12 | Yes | Yes | 1 | 64 × 54 × 6 |
| MCH-MkI_lid_R0.12 | Yes | Yes | 1 | 146 × 96 × 9.3 |
| MCH-MkI_peplink_strain_relief_R0.12 | Yes | Yes | 1 | 18 × 10 × 3.6 |
| MCH-MkI_unfused_busbar_riser_coupon_R0.12 | Yes | Yes | 1 | 139.16 × 44.1 × 9.2 |
| MCH-MkI_wire_exit_fit_coupon_R0.12 | Yes | Yes | 1 | 60 × 25 × 3.2 |

Assembled body/lid interference volume: **0.000000 mm³**.

Conservative fused-block, unfused-busbar, and body envelopes have zero intersection above the mounting risers.

The lowest control opening retains **24.405 mm** vertical clearance above the conservative power-block envelopes.

The conservative 8 mm-deep PD-card envelopes retain **45.100 mm** vertical clearance above the taller power-block envelope.

Checks performed: watertightness, winding consistency, positive volume, 3MF package structure and millimeter units, STL/3MF extent agreement, STEP re-import, the 146 × 96 × 103 mm body envelope, body/lid interference, swapped power-block envelope clearance, 38.10 mm-deep switch clearance, installed carrier clearance, and conservative PD-card envelope clearance.
