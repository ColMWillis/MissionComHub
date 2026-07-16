# Mechanical Design Specification

## 1. Identification

- Product name: Mission Communications Hub
- Mark: Mk I
- Organization mark: GAWG CAP
- Project repository: `ColMWillis/MissionComHub`
- Design stage: Milestone 1 mechanical prototype

## 2. Intended use

The Mk I enclosure shall provide a portable, serviceable housing for 12 VDC power conversion and distribution supporting a Peplink MAX BR1 Pro 5G and future communications accessories. The enclosure is intended for temporary use in CAP aircraft, ground vehicles, and mission bases.

## 3. Governing design principles

1. No exposed energized conductors during normal use.
2. All field connections shall be polarized and replaceable.
3. The enclosure shall be serviceable using common hand tools.
4. Panel modules shall be replaceable without reprinting the main body when practical.
5. The design shall tolerate transport in a flight bag and elevated cockpit temperatures.
6. Printed parts shall avoid support material where practical.
7. Mechanical provisions shall support future electronics without forcing immediate installation.

## 4. Baseline envelope

Target external envelope:

- Width: 210 mm nominal
- Depth: 145 mm nominal
- Height: 60 mm nominal, excluding feet and protruding controls
- Corner radius: 8–12 mm exterior
- Wall thickness: 3.0 mm nominal
- Lid overlap: at least 8 mm
- Lid-to-body labyrinth or tongue-and-groove joint: required

The CAD model shall remain parametric. Dimensions may change after component measurement, but the external envelope should remain under 220 × 155 × 70 mm.

## 5. Material and printing

Primary material: PETG-CF compatible with a Prusa CORE One.

Recommended prototype settings:

- Nozzle: hardened 0.4 or 0.6 mm
- Layer height: 0.20 mm
- Perimeters: 5
- Top/bottom solid layers: 6
- Infill: 30% gyroid
- Brim: as required by the selected PETG-CF
- Supports: none preferred; build plate only where unavoidable
- Insert installation: temperature-controlled heat-set tip

The final 3MF shall include separate objects and recommended orientations rather than merging all components.

## 6. Enclosure architecture

The enclosure shall consist of:

1. Main lower body
2. Removable lid
3. Internal electronics sled
4. Replaceable front I/O panel
5. Replaceable rear I/O panel
6. Cable-retention clips or clamps
7. Optional feet and AMPS mounting adapter

The sled shall lift out after removal of no more than four screws. The body shall not require removal of panel connectors to extract the sled unless wiring harness disconnects are provided.

## 7. Fasteners

- Primary enclosure fasteners: M3 stainless socket-head screws
- Thread interface: M3 brass heat-set inserts
- Minimum lid fasteners: six, with eight preferred
- Inserts shall not be installed closer than 2.0 mm to an exterior wall
- Captive screw geometry is preferred where reliable in PETG-CF
- Self-tapping screws are prohibited for service points

## 8. Branding

The lid shall carry the following centered text:

Mission Communications Hub
Mk I
GAWG CAP

Branding shall be recessed 0.5–0.8 mm or raised no more than 0.6 mm. Letter geometry must be printable with a 0.4 mm nozzle. A multi-material color change may be supported, but the base design shall remain legible in a single material.

No CAP seal or insignia is included in the baseline model.

## 9. External interfaces

### 9.1 Required for Mk I

- One USB-C PD input opening or panel module
- Four Anderson Powerpole output positions
- One master power switch opening
- One round or rectangular voltage display opening
- Accessible fuse replacement without complete enclosure disassembly, if feasible

### 9.2 Reserved

- Two RJ45 keystone positions
- One USB-C auxiliary output
- Two covered SMA-sized knockouts
- One status display position

Reserved openings shall use replaceable blanking plates rather than open holes.

## 10. Connector labeling

Required Powerpole labels:

- PEPLINK
- STARLINK
- AUX 1
- AUX 2

Other required labels:

- USB-C PD IN
- MASTER
- 12 VDC OUTPUTS

Labels shall be recessed or raised and shall not rely solely on adhesive labels.

## 11. Internal layout zones

The mechanical model shall reserve zones for:

- USB-C PD trigger or converter module: 45 × 35 × 18 mm minimum
- Four-circuit fuse block: 110 × 50 × 40 mm target reserve
- Power distribution and wiring bend radius
- Optional 5-port Ethernet switch: 105 × 65 × 30 mm reserve
- Optional embedded controller: 90 × 65 × 25 mm reserve
- Cable service loops and strain relief

No module dimensions are final until physical components are purchased and measured.

## 12. Thermal design

The enclosure shall provide passive ventilation without creating direct access to wiring.

- Intake area: lower side or bottom, minimum 600 mm² aggregate
- Exhaust area: upper rear or opposite side, minimum 600 mm² aggregate
- Vent slots: 2.0–2.5 mm nominal width with internal finger guard or offset geometry
- Airflow path shall cross the conversion module and not be blocked by the sled

The enclosure is not weatherproof. Ventilation openings shall be positioned to reduce direct liquid entry during normal upright use.

## 13. Mounting and restraint

The base shall include:

- AMPS four-hole pattern: 30 × 38 mm
- M4 insert option or through-hole option on a removable adapter plate
- Four non-slip foot positions
- Two external strap channels suitable for a 25 mm retention strap

The design shall not assume permanent aircraft installation.

## 14. Cable management

- Minimum internal wire bend radius: 4× cable outside diameter
- Main bus wiring channels: 8 mm minimum clear width
- Cable tie points: integrated every 40–60 mm along primary routes
- USB-C input: positive retention clamp required
- All panel wiring: strain-relieved independently of solder joints or screw terminals

## 15. Manufacturing tolerances

Initial PETG-CF allowances:

- Sliding panel clearance: 0.30 mm per side
- Lid fit clearance: 0.25–0.35 mm per side
- Heat-set insert pilot dimensions: manufacturer-specific test coupon required
- Circular panel cutouts: nominal component diameter +0.30 mm
- Snap features: prohibited until validated by coupon testing

## 16. Prototype verification gates

Before a full enclosure print:

1. Print connector-panel coupon.
2. Verify all panel cutouts with actual parts.
3. Print lid-joint corner coupon.
4. Verify heat-set insert fit and pull-out resistance.
5. Print 20 mm-high body section to check warping and dimensions.

The first complete print shall be marked `REV 0.1 PROTOTYPE` internally.
