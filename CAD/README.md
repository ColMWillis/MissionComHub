# CAD Files

The current parametric source of truth is [`CadQuery/make_mch_mk1_r09.py`](CadQuery/make_mch_mk1_r09.py).

R0.9 final-draft exports are organized by format:

- [`3MF/R0.9`](3MF/R0.9) — print meshes in millimeter units
- [`STL/R0.9`](STL/R0.9) — triangulated print meshes
- [`STEP/R0.9`](STEP/R0.9) — neutral editable solids for Fusion and other CAD tools
- [`Releases/R0.9`](Releases/R0.9) — README, dimensions, checksums, and validation results

All three export formats were generated from the same CadQuery source. The complete packaged release is under [`../releases/R0.9`](../releases/R0.9).

## R0.9 printable objects

1. Main enclosure body
2. Branded locating-lip lid
3. Peplink bonded-cable strain-relief clamp
4. Control fit coupon
5. Final 18.55 mm USB-C fit coupon
6. Peplink wire-exit fit coupon
7. Blue Sea 5045 fused-block riser coupon
8. Unfused-busbar riser coupon at confirmed 120.65 mm centers

## R0.8A USB-C refinement coupon

`MCH-MkI_USB-C_panel_fit_coupon_18.70-18.75_R0.8A` is a focused two-position coupon created after the 18.80 mm position was slightly loose. The left opening is 18.75 mm and the right opening is 18.70 mm. The enclosure body is not changed until this coupon identifies the preferred fit.

## R0.8B fit refinement coupons

- `MCH-MkI_USB-C_panel_fit_coupon_18.60-18.65_R0.8B`: left position 18.65 mm; right position 18.60 mm.
- `MCH-MkI_unfused_busbar_riser_coupon_120.65mm_R0.8B`: fixed 120.65 mm (4.75 inch) mounting centers, 0.25 inch farther apart than the prior coupon.

Both measurements are engraved on their coupons. The enclosure body remains at the R0.8 dimensions until physical coupon testing identifies the final values.

## R0.8C USB-C refinement coupon

`MCH-MkI_USB-C_panel_fit_coupon_18.55mm_R0.8C` is a compact single-position coupon at 18.55 mm screw centers. This fit and the 120.65 mm busbar value were subsequently confirmed and incorporated into the R0.9 final draft.

Do not alter a mesh export without updating the parametric source and regenerating every synchronized format.
