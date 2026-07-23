# Assembly Guide — Mk I R0.11 Tall Swapped-Block Body

## 1. Print and verify coupons

Use the intended PETG-CF profile for all coupons.

1. Print `MCH-MkI_control_fit_coupon_R0.11.3mf` if the verified control dimensions need reconfirmation on a different printer profile.
2. Confirm the switch snaps or seats without distorting the coupon.
3. Confirm the voltmeter fits the 45.17 × 26.39 mm opening without rattle or excessive force.
4. The final USB-C interface uses confirmed 18.55 mm screw centers. Reprint the final coupon only if the printer profile changes.
5. The R0.6 body uses the physically verified 4.10 × 2.40 mm Peplink opening. Confirm it again if the printer profile changes.
6. Print the Blue Sea 5045 fused-block coupon and verify both risers at 65.1 mm centers.
7. The final unfused-busbar coupon and body use confirmed 120.65 mm centers and 5.5 mm mounting holes.

Do not use the R0.9/R0.10 body for the final hardware layout. Its lower controls conflict with the 38.10 mm-deep switch.

## 2. Print the enclosure

- Print the body upright.
- Print the clamp flat.
- Print the lid branding-up with support under the broad center panel, or trial a long-edge orientation with a brim.
- Reuse an R0.10 USB-PD carrier if already printed; otherwise print the R0.11 carrier with its guide rails upward.
- Inspect every screw boss, cable-contact edge, panel recess, and locating lip before assembly.

## 3. Install threaded hardware

1. Prove the selected M3 heat-set insert pilot on scrap PETG-CF.
2. Install the four enclosure-lid inserts square to the boss faces.
3. Install four additional M3 inserts into the blind USB-PD carrier bosses under the R0.11 lid.
4. Stop the carrier inserts flush with the boss bottoms; do not force them toward the branded surface.
5. Install the two strain-relief inserts using the verified method.
6. Verify the chosen Blue Sea 5045 mounting method before modifying the 3.6 mm pilots.

Allow inserts to cool before installing screws.

## 4. Mechanical dry fit

1. Install the switch and voltmeter on the control face.
2. Install the two USB-C panel connectors on the I/O face.
3. Route the Peplink bonded pair through its exit.
4. Fit the printed clamp with its 4.55 × 2.70 mm channel and tighten only enough to prevent movement; do not flatten or cut the insulation.
5. Place the Blue Sea 5045 on the I/O-side 65.1 mm mounting centers.
6. Install the battery-input PD sink/trigger card in the carrier's left bay with two small zip ties.
7. Install the Starlink-output PD source card in the right bay with two small zip ties.
8. Attach the populated carrier to the lid's four blind bosses with M3 screws that do not bottom in the inserts.
9. Route dummy cable through the body tie-downs and leave enough service loop to raise the lid.
10. Install the unfused busbar on the control-side 120.65 mm bosses and verify the cover clears the body, relocated lid posts, central cable channel, and populated carrier.

## 5. Lid fit

1. Place the lid locating lip into the body opening without screws.
2. Confirm the seam closes uniformly and all four holes align.
3. Install M3 screws finger-tight, then tighten evenly.
4. Confirm no screw bottoms out and no printed boss cracks.
5. Confirm the carrier guides and USB-PD cards face downward into the enclosure.
6. Confirm no solder joint, component, or wire is compressed when the lid is seated.
7. Verify the switch’s rear body and terminals remain clear of the unfused bus bar before wiring.

## 6. Electrical integration hold point

Before applying power, independently document and verify:

- USB-C PD input and output profiles
- polarity at every DC connection
- fuse ratings and source-side protection
- wire gauge and terminal ratings
- Starlink and Peplink peak loads
- switch and panel-interface DC ratings
- clearance from conductive hardware
- thermal behavior with the lid installed

## 7. Initial energized test

Perform the first test outside an aircraft on a nonflammable surface with current-limited power where practical.

1. Energize the empty distribution system and verify voltage and polarity.
2. Test the Peplink alone.
3. Test Starlink alone.
4. Test both simultaneously.
5. Run the intended maximum load for at least 30 minutes while monitoring cables, connectors, converters, fuse block, switch, and enclosure temperature.

Stop immediately for odor, discoloration, unstable voltage, unexpected resets, or abnormal heating.
