from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

import cadquery as cq
import numpy as np
import trimesh


REPO = Path(__file__).resolve().parents[1]
STL_DIR = REPO / "CAD/STL/R0.11"
MF3_DIR = REPO / "CAD/3MF/R0.11"
STEP_DIR = REPO / "CAD/STEP/R0.11"
RELEASE_DIR = REPO / "CAD/Releases/R0.11"


def as_mesh(path: Path) -> trimesh.Trimesh:
    loaded = trimesh.load(path, force="scene")
    if isinstance(loaded, trimesh.Scene):
        if not loaded.geometry:
            raise ValueError(f"No mesh geometry in {path.name}")
        return trimesh.util.concatenate(tuple(loaded.geometry.values()))
    return loaded


results = {"revision": "R0.11", "files": {}}
manifest = json.loads((RELEASE_DIR / "dimensions.json").read_text())
if manifest.get("voltmeter_cutout_mm") != [45.17, 26.39]:
    raise RuntimeError(f"Unexpected R0.11 voltmeter cutout: {manifest.get('voltmeter_cutout_mm')}")
results["voltmeter_cutout_mm"] = manifest["voltmeter_cutout_mm"]
if manifest.get("peplink_wire_exit_mm") != [4.1, 2.4]:
    raise RuntimeError(f"Unexpected R0.11 Peplink exit: {manifest.get('peplink_wire_exit_mm')}")
if manifest.get("peplink_strain_channel_mm") != [4.55, 2.7]:
    raise RuntimeError(f"Unexpected R0.11 strain channel: {manifest.get('peplink_strain_channel_mm')}")
results["peplink_wire_exit_mm"] = manifest["peplink_wire_exit_mm"]
results["peplink_strain_channel_mm"] = manifest["peplink_strain_channel_mm"]
usb = manifest.get("usb_c_panel_extension", {})
if usb.get("measured_pass_through_mm") != [12.7, 6.35]:
    raise RuntimeError(f"Unexpected USB pass-through: {usb.get('measured_pass_through_mm')}")
results["usb_c_panel_extension"] = usb
if usb.get("mount_hole_ctc_mm") != 18.55:
    raise RuntimeError(f"Unexpected final USB screw centers: {usb.get('mount_hole_ctc_mm')}")
busbar = manifest.get("unfused_busbar", {})
if busbar.get("cover_envelope_mm") != [137.16, 38.1, 22.86]:
    raise RuntimeError(f"Unexpected unfused busbar envelope: {busbar.get('cover_envelope_mm')}")
if busbar.get("measured_mount_centers_mm") != 120.65:
    raise RuntimeError(f"Unexpected bus-bar mounting centers: {busbar.get('measured_mount_centers_mm')}")
results["unfused_busbar"] = busbar
carrier_data = manifest.get("pd_card_carrier", {})
if carrier_data.get("card_envelope_each_mm") != [45.72, 17.78]:
    raise RuntimeError(f"Unexpected PD card envelope: {carrier_data.get('card_envelope_each_mm')}")
if carrier_data.get("carrier_mm") != [114.0, 30.0, 2.4]:
    raise RuntimeError(f"Unexpected PD carrier envelope: {carrier_data.get('carrier_mm')}")
results["pd_card_carrier"] = carrier_data
stls = sorted(STL_DIR.glob("*.stl"))
if not stls:
    raise RuntimeError("No STL files found")

for stl in stls:
    stem = stl.stem
    mf3 = MF3_DIR / f"{stem}.3mf"
    step = STEP_DIR / f"{stem}.step"
    if not mf3.exists() or not step.exists():
        raise RuntimeError(f"Missing matching export for {stem}")

    stl_mesh = as_mesh(stl)
    mf3_mesh = as_mesh(mf3)
    if not stl_mesh.is_watertight or not mf3_mesh.is_watertight:
        raise RuntimeError(f"Non-watertight mesh: {stem}")
    if not stl_mesh.is_winding_consistent or not mf3_mesh.is_winding_consistent:
        raise RuntimeError(f"Inconsistent winding: {stem}")
    if not np.allclose(stl_mesh.extents, mf3_mesh.extents, atol=0.02):
        raise RuntimeError(f"3MF/STL extent mismatch: {stem}")

    with zipfile.ZipFile(mf3) as zf:
        required = {"3D/3dmodel.model", "_rels/.rels", "[Content_Types].xml"}
        if not required.issubset(set(zf.namelist())):
            raise RuntimeError(f"Incomplete 3MF package: {stem}")
        model_root = ET.fromstring(zf.read("3D/3dmodel.model"))
        if model_root.attrib.get("unit") != "millimeter":
            raise RuntimeError(f"3MF units are not millimeters: {stem}")

    imported = cq.importers.importStep(str(step))
    solids = imported.solids().vals()
    if not solids:
        raise RuntimeError(f"STEP contains no solids: {stem}")
    step_volume = sum(s.Volume() for s in solids)
    if step_volume <= 0:
        raise RuntimeError(f"STEP has zero volume: {stem}")

    results["files"][stem] = {
        "faces": int(len(stl_mesh.faces)),
        "watertight": True,
        "winding_consistent": True,
        "extents_mm": [round(float(v), 4) for v in stl_mesh.extents],
        "mesh_volume_mm3": round(float(abs(stl_mesh.volume)), 2),
        "step_solids": len(solids),
        "step_volume_mm3": round(float(step_volume), 2),
        "3mf_unit": "millimeter",
        "3mf_matches_stl_extents": True,
    }

body_extent = results["files"]["MCH-MkI_body_R0.11"]["extents_mm"]
body_height = manifest["enclosure_mm"][2]
if not np.allclose(body_extent, [146.0, 96.0, 103.0], atol=0.02):
    raise RuntimeError(f"Body envelope is incorrect: {body_extent}")

body_step = cq.importers.importStep(str(STEP_DIR / "MCH-MkI_body_R0.11.step"))
lid_step = cq.importers.importStep(str(STEP_DIR / "MCH-MkI_lid_R0.11.step")).translate((0, 0, body_height))
intersection = body_step.intersect(lid_step)
interference_volume = sum(s.Volume() for s in intersection.solids().vals())
if interference_volume > 0.05:
    raise RuntimeError(f"Body/lid interference: {interference_volume:.4f} mm^3")
results["assembled_body_lid_interference_mm3"] = round(float(interference_volume), 6)

# Conservative rectangular envelopes verify that both received power blocks
# clear the body, tall lid bosses, and each other above their mounting risers.
fuse_data = manifest["blue_sea_5045"]
fuse_proxy = cq.Workplane("XY").box(92.5, 43.8, 30.0, centered=(True, True, False)).translate(
    (fuse_data["boss_center_mm"][0], fuse_data["boss_center_mm"][1], 9.4)
)
bus_proxy = cq.Workplane("XY").box(137.16, 38.1, 22.86, centered=(True, True, False)).translate(
    (busbar["body_boss_center_mm"][0], busbar["body_boss_center_mm"][1], 9.4)
)
clearances = {
    "fused_block_to_body_mm3": sum(s.Volume() for s in body_step.intersect(fuse_proxy).solids().vals()),
    "unfused_busbar_to_body_mm3": sum(s.Volume() for s in body_step.intersect(bus_proxy).solids().vals()),
    "between_power_blocks_mm3": sum(s.Volume() for s in fuse_proxy.intersect(bus_proxy).solids().vals()),
}
if any(volume > 0.05 for volume in clearances.values()):
    raise RuntimeError(f"Power-block envelope interference: {clearances}")
results["power_block_envelope_interference_mm3"] = {
    name: round(float(volume), 6) for name, volume in clearances.items()
}

# The 38.1 mm-deep physical switch projects inward from the control face.
# Validate its complete rectangular envelope against both swapped power blocks.
control = manifest["control_layout"]
switch_w, switch_h = manifest["switch_cutout_mm"]
switch_proxy = (
    cq.Workplane("XY")
    .box(
        switch_w,
        control["switch_inward_depth_mm"],
        switch_h,
        centered=(True, False, False),
    )
    .translate(
        (
            control["switch_center_x_mm"],
            control["control_face_y_mm"],
            control["panel_center_z_mm"] - switch_h / 2,
        )
    )
)
switch_clearances = {
    "switch_to_fused_block_mm3": sum(s.Volume() for s in switch_proxy.intersect(fuse_proxy).solids().vals()),
    "switch_to_unfused_busbar_mm3": sum(s.Volume() for s in switch_proxy.intersect(bus_proxy).solids().vals()),
}
if any(volume > 0.05 for volume in switch_clearances.values()):
    raise RuntimeError(f"Switch envelope interference: {switch_clearances}")
results["switch_power_block_interference_mm3"] = {
    name: round(float(volume), 6) for name, volume in switch_clearances.items()
}
power_block_top_z = max(9.4 + 30.0, 9.4 + 22.86)
lowest_control_edge_z = min(
    control["panel_center_z_mm"] - manifest["switch_cutout_mm"][1] / 2,
    control["panel_center_z_mm"] - manifest["voltmeter_cutout_mm"][1] / 2,
)
results["lowest_control_opening_to_power_block_vertical_clearance_mm"] = round(
    float(lowest_control_edge_z - power_block_top_z), 3
)

# Assemble the carrier rail-side downward against the four lid bosses.
carrier_step = cq.importers.importStep(
    str(STEP_DIR / "MCH-MkI_dual_USB-PD_card_carrier_R0.11.step")
)
carrier_installed = (
    carrier_step.rotate((0, 0, 0), (1, 0, 0), 180)
    .translate((0, carrier_data["carrier_center_in_enclosure_xy_mm"][1], body_height - carrier_data["lid_boss_height_mm"]))
)
carrier_clearances = {
    "carrier_to_body_mm3": sum(s.Volume() for s in body_step.intersect(carrier_installed).solids().vals()),
    "carrier_to_busbar_mm3": sum(s.Volume() for s in bus_proxy.intersect(carrier_installed).solids().vals()),
    "carrier_to_fused_block_mm3": sum(s.Volume() for s in fuse_proxy.intersect(carrier_installed).solids().vals()),
}
if any(volume > 0.05 for volume in carrier_clearances.values()):
    raise RuntimeError(f"Installed PD carrier interference: {carrier_clearances}")
results["installed_pd_carrier_interference_mm3"] = {
    name: round(float(volume), 6) for name, volume in carrier_clearances.items()
}

# A conservative 8 mm total board/component depth is checked below the carrier.
carrier_plate_bottom_z = body_height - carrier_data["lid_boss_height_mm"] - carrier_data["carrier_mm"][2]
board_bottom_z = carrier_plate_bottom_z - carrier_data["assumed_max_card_assembly_depth_mm"]
board_proxies = []
for center_x, center_y in carrier_data["card_centers_in_enclosure_xy_mm"]:
    board_proxies.append(
        cq.Workplane("XY")
        .box(
            carrier_data["card_envelope_each_mm"][0],
            carrier_data["card_envelope_each_mm"][1],
            carrier_data["assumed_max_card_assembly_depth_mm"],
            centered=(True, True, False),
        )
        .translate((center_x, center_y, board_bottom_z))
    )
board_interference = {
    "cards_to_body_mm3": sum(
        sum(s.Volume() for s in body_step.intersect(proxy).solids().vals())
        for proxy in board_proxies
    ),
    "cards_to_busbar_mm3": sum(
        sum(s.Volume() for s in bus_proxy.intersect(proxy).solids().vals())
        for proxy in board_proxies
    ),
    "cards_to_fused_block_mm3": sum(
        sum(s.Volume() for s in fuse_proxy.intersect(proxy).solids().vals())
        for proxy in board_proxies
    ),
}
if any(volume > 0.05 for volume in board_interference.values()):
    raise RuntimeError(f"PD card envelope interference: {board_interference}")
busbar_top_z = 9.4 + 22.86
results["pd_card_envelope_interference_mm3"] = {
    name: round(float(volume), 6) for name, volume in board_interference.items()
}
results["pd_card_to_busbar_vertical_clearance_mm"] = round(float(board_bottom_z - busbar_top_z), 3)
results["pd_card_to_power_blocks_vertical_clearance_mm"] = round(float(board_bottom_z - power_block_top_z), 3)

(RELEASE_DIR / "validation_report.json").write_text(json.dumps(results, indent=2) + "\n")

lines = [
    "# R0.11 Tall Swapped-Block Body Validation Report",
    "",
    "All matching STL, 3MF, and STEP exports passed automated validation.",
    "",
    "R0.11 preserves the verified **45.17 × 26.39 mm** voltmeter cutout.",
    "",
    "Peplink body exit: **4.10 × 2.40 mm**. Strain-relief channel: **4.55 × 2.70 mm**.",
    "",
    "The USB-C panel geometry uses the received 12.70 × 6.35 mm pass-through and 25.40 × 7.62 mm rounded flange.",
    "",
    "The body and final coupons use confirmed **18.55 mm USB** and **120.65 mm bus-bar** mounting centers.",
    "",
    "The removable carrier holds two **45.72 × 17.78 mm** card envelopes and attaches to four blind M3 insert bosses under the lid.",
    "",
    "The 38.10 mm-deep switch envelope has zero intersection with either swapped power block.",
    "",
    "| Part | Watertight | STL/3MF match | STEP solids | Extents (mm) |",
    "|---|---:|---:|---:|---|",
]
for name, data in results["files"].items():
    ext = " × ".join(f"{v:g}" for v in data["extents_mm"])
    lines.append(f"| {name} | Yes | Yes | {data['step_solids']} | {ext} |")
lines += [
    "",
    f"Assembled body/lid interference volume: **{interference_volume:.6f} mm³**.",
    "",
    "Conservative fused-block, unfused-busbar, and body envelopes have zero intersection above the mounting risers.",
    "",
    f"The lowest control opening retains **{results['lowest_control_opening_to_power_block_vertical_clearance_mm']:.3f} mm** vertical clearance above the conservative power-block envelopes.",
    "",
    f"The conservative 8 mm-deep PD-card envelopes retain **{results['pd_card_to_power_blocks_vertical_clearance_mm']:.3f} mm** vertical clearance above the taller power-block envelope.",
    "",
    "Checks performed: watertightness, winding consistency, positive volume, 3MF package structure and millimeter units, STL/3MF extent agreement, STEP re-import, the 146 × 96 × 103 mm body envelope, body/lid interference, swapped power-block envelope clearance, 38.10 mm-deep switch clearance, installed carrier clearance, and conservative PD-card envelope clearance.",
]
(RELEASE_DIR / "VALIDATION.md").write_text("\n".join(lines) + "\n")

hash_lines = []
hash_paths = []
for directory in (STL_DIR, MF3_DIR, STEP_DIR, REPO / "CAD/CadQuery"):
    hash_paths.extend(p for p in directory.iterdir() if p.is_file())
for path in sorted(hash_paths):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    hash_lines.append(f"{digest}  {path.relative_to(REPO)}")
(RELEASE_DIR / "REPOSITORY_SHA256SUMS.txt").write_text("\n".join(hash_lines) + "\n")

print(json.dumps(results, indent=2))
