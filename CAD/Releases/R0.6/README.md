# Mission Communications Hub Mk I Enclosure R0.6

Compact refactor based on measured components.

## Overall size
- Body: 140 x 90 x 52 mm
- Wall: 3.0 mm
- Separate 4.0 mm lid with locating lip and raised branding

## Control face
- Voltmeter opening: 45.17 x 26.39 mm
- Power switch opening: 38.55 x 20.77 mm

R0.6 preserves the physically verified R0.5 switch and voltmeter openings. It selects the smallest Peplink wire-coupon opening and enlarges the strain-relief cable channel by 0.50 mm overall in both dimensions.

## I/O face
- Two AAOTOKK panel mounts: 33.0 x 25.0 mm flange, 25.0 mm screw centers
- Connector opening: 11.0 x 6.0 mm; M2.5 clearance holes: 2.8 mm
- Flush flange pocket: 33.4 x 25.4 x 0.8 mm deep
- Peplink bonded-cable exit: 4.10 x 2.40 mm rounded slot
- Reduced two-screw strain-relief for the measured 3.81 x 2.03 mm bonded 20 AWG cable
- Strain-relief cable channel: 4.55 x 2.70 mm
- Engraved BATTERY, STARLINK, and PEPLINK labels

## Blue Sea 5045 mounting
- Documented body footprint reserved: 92.5 x 43.8 mm
- Two internal mounting bosses at 65.1 mm centers
- 3.6 mm pilot holes; verify the chosen M4 fastening method before final assembly

## PD board accommodation
Two universal cradles are sized around a 17.78 x 43.18 mm board, with an additional 2.54 mm solder-joint allowance. They are rotated along X to preserve the fuse-block footprint. Routing rails and four zip-tie tabs keep service loops away from fuse terminals.

## Print order
1. Print the three fit coupons.
2. Test the switch, voltmeter, both AAOTOKK receptacles, and bonded Peplink cable.
3. Adjust the parameters at the top of `make_mch_mk1_r06.py` if necessary.
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
- The R0.5 4 mm removable lid, corrected locating lip, M3 corner-boss pattern, and raised branding are preserved.
- All external component geometry has a fit coupon. Print coupons before the body.
- The AAOTOKK flange dimensions came from the supplied dimension image; verify screw spacing and recess fit on the coupon.
- The Blue Sea 5045 footprint is based on the manufacturer's documented 92.5 x 43.8 mm envelope and 65.1 mm mounting centers.

## Regenerating the files
Python 3.11 or newer is recommended. Install `cadquery` and `trimesh`, then run:

```text
python make_mch_mk1_r06.py
```

The generator writes a synchronized STEP, STL, and millimeter-unit 3MF for each part into a `MissionComHub_MkI_Enclosure_R0.6` folder beside the script.
