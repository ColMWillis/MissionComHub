# Mission Communications Hub Mk I Enclosure R0.8

Compact refactor based on measured components.

## Overall size
- Body: 146 x 96 x 52 mm
- Wall: 3.0 mm
- Separate 4.0 mm lid with locating lip and raised branding

## Control face
- Voltmeter opening: 45.17 x 26.39 mm
- Power switch opening: 38.55 x 20.77 mm

R0.8 preserves all physically verified control and Peplink cutouts while rebuilding the USB-C interface around the received component and adding the received unfused bus bar to the body.

## I/O face
- Two measured panel mounts: 25.4 x 7.62 mm rounded flange, 19.05 mm nominal screw centers
- Received pass-through body: 12.70 x 6.35 mm
- Printed connector opening: 13.20 x 6.85 mm; M2.5 clearance holes: 2.8 mm
- Flush flange pocket: 25.8 x 8.0 x 0.8 mm deep
- Peplink bonded-cable exit: 4.10 x 2.40 mm rounded slot
- Reduced two-screw strain-relief for the measured 3.81 x 2.03 mm bonded 20 AWG cable
- Strain-relief cable channel: 4.55 x 2.70 mm
- Correctly oriented engraved BATTERY, STARLINK, and PEPLINK labels
- Engraved VOLTAGE and POWER control-face labels

## Blue Sea 5045 mounting
- Documented body footprint reserved: 92.5 x 43.8 mm
- Two internal mounting bosses at 65.1 mm centers
- 3.6 mm pilot holes; verify the chosen M4 fastening method before final assembly
- Full riser coupon included

## Unfused bus bar
- Supplied cover envelope: 137.16 x 38.10 x 22.86 mm
- Supplied lower-base length: 119.38 mm
- Physical mounting centers: 114.30 mm (4.5 inches)
- Body and coupon use fixed 5.5 mm mounting holes
- Body enlarged to 146 x 96 mm so the covered block and fused block can mount side-by-side

## Cable accommodation
The obsolete PCB-backed USB shelves were removed because the received USB interfaces are cable-backed panel fittings. Routing rails and tie-down tabs retain service loops away from both power blocks.

## Print order
1. Print the control, USB-C, wire-exit, fused-block, and unfused-block coupons.
2. Test the switch, voltmeter, both USB-C panel fittings, and bonded Peplink cable.
3. Adjust the parameters at the top of `make_mch_mk1_r08.py` if necessary.
4. Print the body, lid and strain-relief clamp.

## Suggested print settings
- PETG-CF
- 0.4 mm hardened nozzle
- 0.20 mm layer height
- 4 perimeters
- 5 top/bottom layers
- 25-35% gyroid infill
- Body upright; lid branding upward
- Body: supports only where the slicer identifies control/I-O openings as necessary
- Lid: branding upward preserves the visible text; enable snug/organic supports beneath the broad center panel, or test a long-edge orientation with a brim

## Serviceability
- The R0.6 4 mm removable lid, corrected locating lip, M3 corner-boss pattern, and raised branding are preserved.
- All external component geometry has a fit coupon. Print coupons before the body.
- The USB coupon provides 18.80, 19.05, and 19.30 mm screw-center variants; the body uses 19.05 mm.
- The Blue Sea 5045 footprint is based on the manufacturer's documented 92.5 x 43.8 mm envelope and 65.1 mm mounting centers.

## Regenerating the files
Python 3.11 or newer is recommended. Install `cadquery` and `trimesh`, then run:

```text
python make_mch_mk1_r08.py
```

The generator writes a synchronized STEP, STL, and millimeter-unit 3MF for each part into a `MissionComHub_MkI_Enclosure_R0.8` folder beside the script.
