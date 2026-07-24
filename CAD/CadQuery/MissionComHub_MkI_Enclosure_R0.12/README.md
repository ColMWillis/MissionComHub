# Mission Communications Hub Mk I Enclosure R0.12 — Side-by-Side PD Carrier

Compact refactor based on measured components.

## Overall size
- Body: 146 x 96 x 103 mm
- Wall: 3.0 mm
- Separate 4.0 mm lid with locating lip and raised branding

## Control face
- Voltmeter opening: 45.17 x 26.39 mm
- Power switch opening: 38.55 x 20.77 mm

R0.12 reuses the validated R0.11 tall body and replaces the tandem PD carrier and its lid mounting pattern.

## R0.12 collision correction
- Body height: 103.0 mm, increased by 51.0 mm (2.01 inches)
- Measured switch inward depth: 38.10 mm
- Control and USB panel center height: 77.0 mm
- Unfused bus bar: control half, Y=-24.95 mm
- Blue Sea 5045 fused block: I/O half, Y=+22.10 mm
- Tall lid posts moved to the I/O half and kept outside the fused-block footprint

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
- Mounted in the I/O half after the R0.11 block swap

## Unfused bus bar
- Supplied cover envelope: 137.16 x 38.10 x 22.86 mm
- Supplied lower-base length: 119.38 mm
- Confirmed mounting centers: 120.65 mm (4.75 inches)
- Body and coupon use fixed 5.5 mm mounting holes
- Body enlarged to 146 x 96 mm so the covered block and fused block can mount side-by-side
- Mounted in the control half after the R0.11 block swap

## Cable accommodation
The obsolete PCB-backed USB shelves were removed because the received USB interfaces are cable-backed panel fittings. Routing rails and tie-down tabs retain service loops away from both power blocks.

## USB-PD card carrier
- Separate removable carrier: 64.0 x 54.0 x 2.4 mm
- Installs under the lid, centered at X=0, Y=17.0 mm over the fused-block half
- Two open-ended bays for 45.72 x 17.78 mm card envelopes
- Two parallel side-by-side bays; both USB-C sockets point toward +X
- Battery-input PD card occupies the lower-Y bay; Starlink-output PD card occupies the upper-Y bay
- Guide rails move inward 1.0 mm per side and rise to 3.6 mm
- USB ends remain open for attached plugs; screw-terminal ends remain open with 20 mm validated wire-service envelopes
- Two zip ties per card; no undocumented PCB mounting holes are assumed
- Four M3 screws secure the carrier to blind heat-set-insert bosses under the lid
- The flat carrier face mounts against the lid bosses; the guide rails and cards face into the enclosure
- A conservative 8.0 mm card-assembly depth clears the bus-bar cover in the validated assembly

See `PD_CARD_PLACEMENT.md` for the top-view map, assembly order, and wiring paths.

## Print order
1. Stop using the R0.9/R0.10 body for this hardware layout.
2. Reuse the validated R0.11 body; print the R0.12 lid and R0.12 carrier.
3. Do not reuse the tandem R0.10/R0.11 carrier.
4. Install four M3 heat-set inserts in the blind underside bosses.
5. Fit the two cards to the carrier with two small zip ties per card.
6. Attach the populated carrier to the lid with four M3 screws.
7. Reuse the R0.10 strain-relief clamp if already printed; its geometry is unchanged.

## Suggested print settings
- PETG-CF
- 0.4 mm hardened nozzle
- 0.20 mm layer height
- 4 perimeters
- 5 top/bottom layers
- 25-35% gyroid infill
- Body upright; lid branding upward
- Carrier rail-side upward; no support is expected
- Body: supports only where the slicer identifies control/I-O openings as necessary
- Lid: branding upward preserves the visible text; enable snug/organic supports beneath the broad center panel, or test a long-edge orientation with a brim

## Serviceability
- The 4 mm removable lid, corrected locating lip, and raised branding are preserved, with its body-screw holes relocated to the I/O half.
- The entire PD assembly comes away with the lid after four enclosure screws are removed.
- Leave service loops in both USB panel cables and the DC wiring before lifting the lid.
- Mk II shall add a captive hinge/tether so the wire harness never acts as the lid restraint.
- All external component geometry has a fit coupon. Print coupons before the body.
- The final USB coupon and both body interfaces use the confirmed 18.55 mm screw centers.
- The Blue Sea 5045 footprint is based on the manufacturer's documented 92.5 x 43.8 mm envelope and 65.1 mm mounting centers.

## Regenerating the files
Python 3.11 or newer is recommended. Install `cadquery` and `trimesh`, then run:

```text
python make_mch_mk1_r12.py
```

The generator writes synchronized STEP, STL, and millimeter-unit 3MF files into a `MissionComHub_MkI_Enclosure_R0.12` folder beside the script.
