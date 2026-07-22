# Assembly Guide — Mk I R0.7 Prototype

## 1. Print and verify coupons

Use the intended PETG-CF profile for all coupons.

1. Print `MCH-MkI_control_fit_coupon_R0.7.3mf` if the verified control dimensions need reconfirmation on a different printer profile.
2. Confirm the switch snaps or seats without distorting the coupon.
3. Confirm the voltmeter fits the 45.17 × 26.39 mm opening without rattle or excessive force.
4. Print the AAOTOKK USB-C coupon and verify the flange recess, central opening, and both screw positions.
5. The R0.6 body uses the physically verified 4.10 × 2.40 mm Peplink opening. Confirm it again if the printer profile changes.
6. Print the Blue Sea 5045 fused-block coupon and verify both risers at 65.1 mm centers.
7. Print the provisional unfused-busbar coupon and record where its mounting holes fall within the elongated slots. Do not drill or add body bosses from this coupon until the component's enclosure orientation is resolved.

Do not print the complete body until these fits are accepted.

## 2. Print the enclosure

- Print the body upright.
- Print the clamp flat.
- Print the lid branding-up with support under the broad center panel, or trial a long-edge orientation with a brim.
- Inspect every screw boss, cable-contact edge, panel recess, and locating lip before assembly.

## 3. Install threaded hardware

1. Prove the selected M3 heat-set insert pilot on scrap PETG-CF.
2. Install the four lid inserts square to the boss faces.
3. Install the two strain-relief inserts using the verified method.
4. Verify the chosen Blue Sea 5045 mounting method before modifying the 3.6 mm pilots.

Allow inserts to cool before installing screws.

## 4. Mechanical dry fit

1. Install the switch and voltmeter on the control face.
2. Install the two AAOTOKK panel connectors on the I/O face.
3. Route the Peplink bonded pair through its exit.
4. Fit the printed clamp with its 4.55 × 2.70 mm channel and tighten only enough to prevent movement; do not flatten or cut the insulation.
5. Place the Blue Sea 5045 on its 65.1 mm mounting centers.
6. Trial-fit PD modules in the universal cradles.
7. Route dummy cable through the rails and tie-downs to confirm service-loop clearance.
8. Do not install the unfused busbar in the R0.7 body: its 137.16 mm cover is longer than the 134 mm interior.

## 5. Lid fit

1. Place the lid locating lip into the body opening without screws.
2. Confirm the seam closes uniformly and all four holes align.
3. Install M3 screws finger-tight, then tighten evenly.
4. Confirm no screw bottoms out and no printed boss cracks.

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
