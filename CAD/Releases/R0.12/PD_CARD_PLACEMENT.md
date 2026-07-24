# USB-PD Card Placement — R0.12

This map is viewed from above with the lid removed. The I/O face (BATTERY,
STARLINK, and PEPLINK) is at the top.

```text
                         I/O FACE (+Y)
   BATTERY USB-C           STARLINK USB-C          PEPLINK
          |                       |                    |
+----------------------------------------------------------------+
|                                                                |
|               USB-C ends and attached plugs -> +X              |
|          +-------------------------------------------+           |
|          | STARLINK PD  X=0, Y=+29.5               |           |
|          |-------------------------------------------|           |
|          | BATTERY PD   X=0, Y=+4.5                |           |
|          +-------------------------------------------+           |
|     open screw-terminal ends <- 20 mm wire service zone         |
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

- Carrier center: **X 0, Y +17.0 mm**.
- Battery card center: **X 0, Y 4.5 mm**.
- Starlink card center: **X 0, Y +29.5 mm**.
- Card long axes run left-to-right, parallel to the 146 mm enclosure dimension.
- Both USB-C sockets point toward +X; both screw-terminal ends point toward -X.
- Keep at least **20 mm** clear beyond each screw-terminal end for conductors and bend relief.
- The carrier's flat face seats against the four lid bosses.
- The printed guide rails, labels, zip ties, and cards face downward into the box.
- Install two small zip ties per board using the paired slots.
- R0.12 reuses the taller R0.11 body and its swapped power-block mounting layout.
- The tandem R0.10/R0.11 carrier cannot be reused.

## Lid preparation

1. Print the R0.12 lid branding-side upward.
2. Heat-set four M3 inserts into the blind bosses on the underside.
3. Stop each insert flush with the bottom of its boss; do not force it toward the branded surface.
4. Populate the carrier before fastening it to the lid.
5. Use M3 screws short enough to engage the insert without bottoming out; verify length against the actual inserts.

## Card identity

- **Lower-Y / BATTERY PD:** the USB-C PD sink/trigger card that negotiates power from the Anker battery.
- **Upper-Y / STARLINK PD:** the USB-C PD source card that provides the required profile to the Starlink Mini.
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
