# USB-PD Card Placement — R0.11

This map is viewed from above with the lid removed. The I/O face (BATTERY,
STARLINK, and PEPLINK) is at the top.

```text
                         I/O FACE (+Y)
   BATTERY USB-C           STARLINK USB-C          PEPLINK
          |                       |                    |
+----------------------------------------------------------------+
|                                                                |
|   +----------------------+  +----------------------+            |
|   | BATTERY PD CARD      |  | STARLINK PD CARD     |            |
|   | X = -27, Y = +25     |  | X = +27, Y = +25    |            |
|   | 45.72 x 17.78 mm     |  | 45.72 x 17.78 mm    |            |
|   +----------------------+  +----------------------+            |
|   <--------- removable carrier, under the lid ----------->      |
|                                                                |
|              BLUE SEA 5045 FUSED BLOCK                          |
|                                                                |
|       cable/tie-down channel between the two power blocks       |
|                                                                |
|   ================== UNFUSED BUS BAR ======================      |
|                                                                |
|        VOLTAGE                              POWER                |
+----------------------------------------------------------------+
                       CONTROL FACE (-Y)
```

## Mechanical placement

- Carrier center: **X 0, Y +25.0 mm**.
- Battery card center: **X -27.0, Y +25.0 mm**.
- Starlink card center: **X +27.0, Y +25.0 mm**.
- Card long axes run left-to-right, parallel to the 146 mm enclosure dimension.
- The carrier's flat face seats against the four lid bosses.
- The printed guide rails, labels, zip ties, and cards face downward into the box.
- Install two small zip ties per board using the paired slots.
- R0.11 requires the taller body and its swapped power-block mounting layout.
- The R0.10 carrier itself can be reused because its geometry is unchanged.

## Lid preparation

1. Print the R0.11 lid branding-side upward.
2. Heat-set four M3 inserts into the blind bosses on the underside.
3. Stop each insert flush with the bottom of its boss; do not force it toward the branded surface.
4. Populate the carrier before fastening it to the lid.
5. Use M3 screws short enough to engage the insert without bottoming out; verify length against the actual inserts.

## Card identity

- **Left / BATTERY PD:** the USB-C PD sink/trigger card that negotiates power from the Anker battery.
- **Right / STARLINK PD:** the USB-C PD source card that provides the required profile to the Starlink Mini.
- Do not interchange the cards unless their electrical functions and voltage profiles are confirmed.

## Wiring path

```text
Anker C200
   -> BATTERY panel USB-C cable
   -> BATTERY PD sink/trigger card
   -> master POWER switch
   -> Blue Sea 5045 positive feed and unfused negative bus

Blue Sea fused branch
   -> Peplink bonded cable

Blue Sea fused branch + negative return
   -> STARLINK PD source card
   -> STARLINK panel USB-C cable

Switched positive + negative bus
   -> VOLTAGE meter
```

## Service loops and clearance

- Leave a gentle service loop in both USB panel cables so the lid can be raised before disconnecting them.
- Tie the loops to the body's central tabs; do not pull them tight across fuse or bus-bar terminals.
- Keep all conductors below the lid perimeter and away from the four enclosure screw bosses.
- Automated clearance validation uses a conservative **8.0 mm** total card/component depth.
- Before energizing, close the lid without screws and confirm that no component, solder joint, or wire is being compressed.
