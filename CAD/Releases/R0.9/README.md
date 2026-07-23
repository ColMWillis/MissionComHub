# Mission Communications Hub Mk I Enclosure R0.9 Final Draft

Compact refactor based on measured components.

## Overall size
- Body: 146 x 96 x 52 mm
- Wall: 3.0 mm
- Separate 4.0 mm lid with locating lip and raised branding

## Control face
- Voltmeter opening: 45.17 x 26.39 mm
- Power switch opening: 38.55 x 20.77 mm

R0.9 incorporates all physically confirmed interface dimensions into the complete enclosure body. It is the final draft before full assembly testing.

## I/O face
- Two measured panel mounts: 25.4 x 7.62 mm rounded flange, 18.55 mm confirmed screw centers
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
- Confirmed mounting centers: 120.65 mm (4.75 inches)
- Body and coupon use fixed 5.5 mm mounting holes
- Body enlarged to 146 x 96 mm so the covered block and fused block can mount side-by-side

## Cable accommodation
The obsolete PCB-backed USB shelves were removed because the received USB interfaces are cable-backed panel fittings. Routing rails and tie-down tabs retain service loops away from both power blocks.

## Print order
1. Print the final USB-C, control, wire-exit, fused-block, and unfused-block coupons if reconfirmation is desired.
2. Print the body, lid and strain-relief clamp.
3. Record any full-assembly findings before promoting the design to R1.0.

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
- The final USB coupon and both body interfaces use the confirmed 18.55 mm screw centers.
- The Blue Sea 5045 footprint is based on the manufacturer's documented 92.5 x 43.8 mm envelope and 65.1 mm mounting centers.

## Regenerating the files
Python 3.11 or newer is recommended. Install `cadquery` and `trimesh`, then run:

```text
python make_mch_mk1_r09.py
```

The generator writes synchronized STEP, STL, and millimeter-unit 3MF files into a `MissionComHub_MkI_Enclosure_R0.9` folder beside the script.
