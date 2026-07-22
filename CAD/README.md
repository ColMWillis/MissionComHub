# CAD Files

The parametric source of truth is [`CadQuery/make_mch_mk1_r05.py`](CadQuery/make_mch_mk1_r05.py).

R0.5 exports are organized by format:

- [`3MF/R0.5`](3MF/R0.5) — print meshes in millimeter units
- [`STL/R0.5`](STL/R0.5) — triangulated print meshes
- [`STEP/R0.5`](STEP/R0.5) — neutral editable solids for Fusion and other CAD tools
- [`Releases/R0.5`](Releases/R0.5) — README, dimensions, checksums, and validation results

All three export formats were generated from the same CadQuery source. The complete packaged release is under [`../releases/R0.5`](../releases/R0.5).

## R0.5 printable objects

1. Main enclosure body
2. Branded locating-lip lid
3. Peplink bonded-cable strain-relief clamp
4. Control fit coupon
5. AAOTOKK USB-C fit coupon
6. Peplink wire-exit fit coupon

Do not alter a mesh export without updating the parametric source and regenerating every synchronized format.
