# CAD Files

The current parametric source of truth is [`CadQuery/make_mch_mk1_r08.py`](CadQuery/make_mch_mk1_r08.py).

R0.8 exports are organized by format:

- [`3MF/R0.8`](3MF/R0.8) — print meshes in millimeter units
- [`STL/R0.8`](STL/R0.8) — triangulated print meshes
- [`STEP/R0.8`](STEP/R0.8) — neutral editable solids for Fusion and other CAD tools
- [`Releases/R0.8`](Releases/R0.8) — README, dimensions, checksums, and validation results

All three export formats were generated from the same CadQuery source. The complete packaged release is under [`../releases/R0.8`](../releases/R0.8).

## R0.8 printable objects

1. Main enclosure body
2. Branded locating-lip lid
3. Peplink bonded-cable strain-relief clamp
4. Control fit coupon
5. Three-position USB-C panel fit coupon
6. Peplink wire-exit fit coupon
7. Blue Sea 5045 fused-block riser coupon
8. Unfused-busbar riser coupon at measured 114.3 mm centers

Do not alter a mesh export without updating the parametric source and regenerating every synchronized format.
