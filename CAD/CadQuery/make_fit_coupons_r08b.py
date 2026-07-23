import json
from pathlib import Path

import cadquery as cq
from cadquery import exporters
import trimesh


OUT = Path(__file__).resolve().parents[2] / "CAD/Releases/R0.8/fit-refinement-r08b"
OUT.mkdir(parents=True, exist_ok=True)

USB_NAME = "MCH-MkI_USB-C_panel_fit_coupon_18.60-18.65_R0.8B"
BUS_NAME = "MCH-MkI_unfused_busbar_riser_coupon_120.65mm_R0.8B"


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


def engrave(object_, label, x, y, size=3.2):
    try:
        marking = (
            cq.Workplane("XY")
            .workplane(offset=3.2)
            .center(x, y)
            .text(label, size, 0.45, font="DejaVu Sans", halign="center", valign="center")
        )
        return object_.cut(marking)
    except Exception as error:
        print("Label warning:", error)
        return object_


def export_part(name, object_, metadata):
    stl = OUT / f"{name}.stl"
    step = OUT / f"{name}.step"
    mf3 = OUT / f"{name}.3mf"
    exporters.export(object_, str(stl), tolerance=0.07, angularTolerance=0.12)
    exporters.export(object_, str(step))
    mesh = trimesh.load_mesh(stl, force="mesh")
    mesh.export(mf3)
    metadata.update(
        {
            "name": name,
            "watertight": bool(mesh.is_watertight),
            "winding_consistent": bool(mesh.is_winding_consistent),
            "extents_mm": [round(float(value), 3) for value in mesh.extents],
        }
    )
    (OUT / f"{name}.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(metadata, indent=2))


# USB-C two-position refinement coupon.
plate_w = 68.0
plate_h = 34.0
plate_t = 3.2
usb_cut_w = 13.20
usb_cut_h = 6.85
flange_w = 25.80
flange_h = 8.02
recess_depth = 0.80
screw_d = 2.80

usb_coupon = rounded_rect(plate_w, plate_h, plate_t, 3.0)
usb_variants = [(-17.0, 18.65, "18.65"), (17.0, 18.60, "18.60")]
for center_x, screw_ctc, label in usb_variants:
    through = rounded_rect(
        usb_cut_w, usb_cut_h, plate_t + 2.0, usb_cut_h / 2 - 0.10, z0=-1.0
    ).translate((center_x, 3.0, 0))
    usb_coupon = usb_coupon.cut(through)
    for dx in (-screw_ctc / 2, screw_ctc / 2):
        screw = (
            cq.Workplane("XY")
            .center(center_x + dx, 3.0)
            .circle(screw_d / 2)
            .extrude(plate_t + 2.0)
            .translate((0, 0, -1.0))
        )
        usb_coupon = usb_coupon.cut(screw)
    pocket = rounded_rect(
        flange_w,
        flange_h,
        recess_depth + 0.2,
        flange_h / 2 - 0.05,
        z0=plate_t - recess_depth,
    ).translate((center_x, 3.0, 0))
    usb_coupon = usb_coupon.cut(pocket)
    usb_coupon = engrave(usb_coupon, label, center_x, -10.5)

export_part(
    USB_NAME,
    usb_coupon,
    {
        "plate_mm": [plate_w, plate_h, plate_t],
        "positions_left_to_right_mm": [18.65, 18.60],
        "connector_cutout_mm": [usb_cut_w, usb_cut_h],
        "flange_recess_mm": [flange_w, flange_h, recess_depth],
        "screw_hole_diameter_mm": screw_d,
    },
)


# Unfused bus-bar coupon with holes moved 0.25 inch farther apart.
bus_cover_l = 137.16
bus_w = 38.10
bus_ctc = 4.75 * 25.4  # 120.65 mm
bus_hole_d = 5.50
bus_coupon = rounded_rect(bus_cover_l + 2.0, bus_w + 6.0, 3.2, 4.0)
for dx in (-bus_ctc / 2, bus_ctc / 2):
    boss = cq.Workplane("XY").center(dx, 0).circle(6.5).extrude(6.0).translate((0, 0, 3.2))
    hole = cq.Workplane("XY").center(dx, 0).circle(bus_hole_d / 2).extrude(7.0).translate((0, 0, 2.7))
    bus_coupon = bus_coupon.union(boss).cut(hole)
bus_coupon = engrave(bus_coupon, "120.65 mm", 0, -17.0, size=3.6)

export_part(
    BUS_NAME,
    bus_coupon,
    {
        "plate_mm": [bus_cover_l + 2.0, bus_w + 6.0, 3.2],
        "mounting_centers_mm": bus_ctc,
        "mounting_centers_inches": 4.75,
        "mount_hole_diameter_mm": bus_hole_d,
    },
)
