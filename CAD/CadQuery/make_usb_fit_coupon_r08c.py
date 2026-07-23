import json
from pathlib import Path

import cadquery as cq
from cadquery import exporters
import trimesh


OUT = Path(__file__).resolve().parents[2] / "CAD/Releases/R0.8/usb-refinement-r08c"
OUT.mkdir(parents=True, exist_ok=True)

NAME = "MCH-MkI_USB-C_panel_fit_coupon_18.55mm_R0.8C"
PLATE_W = 36.0
PLATE_H = 34.0
PLATE_T = 3.2
SCREW_CTC = 18.55
SCREW_D = 2.80
USB_CUT_W = 13.20
USB_CUT_H = 6.85
FLANGE_W = 25.80
FLANGE_H = 8.02
RECESS_DEPTH = 0.80


def rounded_rect(w, h, depth, radius, z0=0.0):
    shape = cq.Workplane("XY").rect(w - 2 * radius, h).extrude(depth).translate((0, 0, z0))
    shape = shape.union(
        cq.Workplane("XY").rect(w, h - 2 * radius).extrude(depth).translate((0, 0, z0))
    )
    for x in (-w / 2 + radius, w / 2 - radius):
        for y in (-h / 2 + radius, h / 2 - radius):
            shape = shape.union(
                cq.Workplane("XY").center(x, y).circle(radius).extrude(depth).translate((0, 0, z0))
            )
    return shape


coupon = rounded_rect(PLATE_W, PLATE_H, PLATE_T, 3.0)
through = rounded_rect(
    USB_CUT_W, USB_CUT_H, PLATE_T + 2.0, USB_CUT_H / 2 - 0.10, z0=-1.0
).translate((0, 3.0, 0))
coupon = coupon.cut(through)

for dx in (-SCREW_CTC / 2, SCREW_CTC / 2):
    screw = (
        cq.Workplane("XY")
        .center(dx, 3.0)
        .circle(SCREW_D / 2)
        .extrude(PLATE_T + 2.0)
        .translate((0, 0, -1.0))
    )
    coupon = coupon.cut(screw)

pocket = rounded_rect(
    FLANGE_W,
    FLANGE_H,
    RECESS_DEPTH + 0.2,
    FLANGE_H / 2 - 0.05,
    z0=PLATE_T - RECESS_DEPTH,
).translate((0, 3.0, 0))
coupon = coupon.cut(pocket)

try:
    marking = (
        cq.Workplane("XY")
        .workplane(offset=PLATE_T)
        .center(0, -10.5)
        .text("18.55", 3.2, 0.45, font="DejaVu Sans", halign="center", valign="center")
    )
    coupon = coupon.cut(marking)
except Exception as error:
    print("Label warning:", error)

stl = OUT / f"{NAME}.stl"
step = OUT / f"{NAME}.step"
mf3 = OUT / f"{NAME}.3mf"
exporters.export(coupon, str(stl), tolerance=0.07, angularTolerance=0.12)
exporters.export(coupon, str(step))
mesh = trimesh.load_mesh(stl, force="mesh")
mesh.export(mf3)

manifest = {
    "name": NAME,
    "plate_mm": [PLATE_W, PLATE_H, PLATE_T],
    "screw_centers_mm": SCREW_CTC,
    "connector_cutout_mm": [USB_CUT_W, USB_CUT_H],
    "flange_recess_mm": [FLANGE_W, FLANGE_H, RECESS_DEPTH],
    "screw_hole_diameter_mm": SCREW_D,
    "watertight": bool(mesh.is_watertight),
    "winding_consistent": bool(mesh.is_winding_consistent),
    "extents_mm": [round(float(value), 3) for value in mesh.extents],
}
(OUT / f"{NAME}.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps(manifest, indent=2))
