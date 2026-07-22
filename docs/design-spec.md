# Mechanical Design Specification — Mk I R0.7

## Identification and scope

- Product: Mission Communications Hub
- Marking: `Mission Communications Hub / Mk I / GAWG CAP`
- Revision: R0.7 prototype
- Function: portable power-interface enclosure for Peplink MAX BR1 Pro 5G and Starlink Mini
- External source: Anker SOLIX C200 DC or equivalent USB-C PD source

The enclosure does not contain the Peplink, Starlink Mini, iPad, battery, or certified avionics. The Starlink Mini remains external so it can be positioned at a window. An iPad may be powered directly from an available battery port and is not assigned a dedicated R0.5 enclosure connector.

## Envelope and construction

| Feature | R0.7 value |
|---|---:|
| Body envelope | 140 × 90 × 52 mm |
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

Two AAOTOKK USB-C panel-mount positions are labeled `BATTERY` and `STARLINK`.
R0.7 corrects all three I/O labels so they read correctly when viewed from outside the enclosure.

| Feature | Dimension |
|---|---:|
| Flange | 33.0 × 25.0 mm |
| Flush recess | 33.4 × 25.4 × 0.8 mm deep |
| Connector aperture | 11.0 × 6.0 mm |
| Screw centers | 25.0 mm |
| Screw clearance | 2.8 mm diameter |

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
- Two universal PD-board cradles based on 17.78 × 43.18 mm boards
- Additional solder-joint allowance: 2.54 mm
- Raised routing rails and four zip-tie tabs keep service loops away from fuse terminals

The Blue Sea 5045 coupon uses the documented 65.1 mm centers. The separate unfused-busbar coupon is provisional: its supplied image indicates a 137.16 × 38.10 × 22.86 mm cover and 119.38 mm base, but does not dimension the mounting centers. The coupon therefore uses elongated slots around an estimated 106.5 mm center distance. The cover exceeds the body's 134 mm internal length by 3.16 mm, so no unfused-busbar bosses have been added to the body.

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

R0.7 passed automated checks for:

- watertight STL and 3MF meshes
- consistent mesh winding and positive volume
- millimeter-unit 3MF package structure
- matching STL and 3MF extents
- successful STEP solid re-import
- exact 140 × 90 × 52 mm body envelope
- zero body/lid intersection when assembled

Automated validation does not replace physical fit, load, thermal, vibration, restraint, or electrical testing.
