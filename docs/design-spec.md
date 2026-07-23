# Mechanical Design Specification — Mk I R0.9 Final Draft

## Identification and scope

- Product: Mission Communications Hub
- Marking: `Mission Communications Hub / Mk I / GAWG CAP`
- Revision: R0.9 final draft
- Function: portable power-interface enclosure for Peplink MAX BR1 Pro 5G and Starlink Mini
- External source: Anker SOLIX C200 DC or equivalent USB-C PD source

The enclosure does not contain the Peplink, Starlink Mini, iPad, battery, or certified avionics. The Starlink Mini remains external so it can be positioned at a window. An iPad may be powered directly from an available battery port and is not assigned a dedicated R0.5 enclosure connector.

## Envelope and construction

| Feature | R0.7 value |
|---|---:|
| Body envelope | 146 × 96 × 52 mm |
| Wall thickness | 3.0 mm |
| Bottom thickness | 3.2 mm |
| External corner radius | 6.0 mm |
| Lid plate | 4.0 mm |
| Lid locating-lip depth | 3.5 mm |
| Lid clearance | 0.35 mm per side |
| Lid fasteners | Four M3 positions |

The body and lid are separate, serviceable printed parts. R0.3 corrected the inherited locating-lip interference and added clearance pockets around the body’s corner bosses. Automated assembly checking reports 0 mm³ body/lid interference.

## Control face

- Power switch nominal body: 38.10 × 20.32 mm
- Switch cutout: 38.55 × 20.77 mm
- Voltmeter nominal supplied size: 45.72 × 27.94 mm
- Fit-tested R0.5/R0.6 voltmeter cutout: 45.17 × 26.39 mm
- Outside control labels: `VOLTAGE` and `POWER`

The voltmeter opening evolved through physical coupon testing:

- R0.3: 46.17 × 28.39 mm — retained but rattled
- R0.4: 44.17 × 26.39 mm — correct vertically, tight horizontally
- R0.5: 45.17 × 26.39 mm — adds 0.50 mm on each side

## I/O face

Two received cable-backed USB-C panel-mount positions are labeled `BATTERY` and `STARLINK`. R0.8 retains the corrected outside-reading label orientation.

| Feature | Dimension |
|---|---:|
| Measured pass-through body | 12.70 × 6.35 mm |
| Printed pass-through | 13.20 × 6.85 mm |
| Measured rounded flange | 25.40 × 7.62 mm |
| Flush recess | 25.80 × 8.02 × 0.8 mm deep |
| Confirmed screw centers | 18.55 mm |
| Screw clearance | 2.8 mm diameter |

The body and final USB coupon use the physically confirmed 18.55 mm centers.

The `PEPLINK` exit is designed around a measured bonded red/black 20 AWG pair:

- Cable: 3.81 × 2.03 mm
- Fit-tested body exit: 4.10 × 2.40 mm
- R0.6 strain-relief channel: 4.55 × 2.70 mm
- Clamp: 18 × 10 × 3.6 mm with two M3 positions

The smallest R0.5 wire-coupon opening fit correctly. The first strain-relief channel was too tight, so R0.6 adds 0.50 mm overall in both channel dimensions without changing the cover footprint or screw spacing.

## Internal geometry

- Blue Sea Systems 5045 reserved envelope: 92.5 × 43.8 mm
- Mounting-boss centers: 65.1 mm
- Boss pilot holes: 3.6 mm; final M4 fastening method must be physically verified
- Unfused busbar cover envelope: 137.16 × 38.10 × 22.86 mm
- Unfused busbar mounting centers: physically confirmed 120.65 mm
- Unfused busbar mounting-hole diameter in R0.8: 5.5 mm
- Four zip-tie tabs occupy the clear channel between the power blocks

The Blue Sea 5045 coupon uses 65.1 mm centers. R0.9 mounts the received unfused busbar at its confirmed 120.65 mm centers. The 146 × 96 mm enclosure, relocated lid posts, and cable-backed USB layout are retained from R0.8.

## Material and printing

- Printer target: Prusa CORE One
- Material: PETG-CF
- Hardened 0.4 mm nozzle
- 0.20 mm layer height
- 4 perimeters
- 5 top and bottom layers
- 25–35% gyroid infill

Print fit coupons first. The body is printed upright. The raised branding complicates the lid orientation: printing branding-up requires support beneath the broad center panel; a long-edge orientation with a brim may also be tested.

## Branding

The lid carries centered raised text:

```text
Mission Communications Hub
Mk I
GAWG CAP
```

No CAP seal or insignia is included.

## Validation

R0.9 passed automated checks for:

- watertight STL and 3MF meshes
- consistent mesh winding and positive volume
- millimeter-unit 3MF package structure
- matching STL and 3MF extents
- successful STEP solid re-import
- exact 146 × 96 × 52 mm body envelope
- zero body/lid intersection when assembled
- zero conservative-envelope intersection between either power block and the body or the other block

Automated validation does not replace physical fit, load, thermal, vibration, restraint, or electrical testing.
