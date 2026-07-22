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
STL_DIR = REPO / "CAD/STL/R0.5"
MF3_DIR = REPO / "CAD/3MF/R0.5"
STEP_DIR = REPO / "CAD/STEP/R0.5"
RELEASE_DIR = REPO / "CAD/Releases/R0.5"


def as_mesh(path: Path) -> trimesh.Trimesh:
    loaded = trimesh.load(path, force="scene")
    if isinstance(loaded, trimesh.Scene):
        if not loaded.geometry:
            raise ValueError(f"No mesh geometry in {path.name}")
        return trimesh.util.concatenate(tuple(loaded.geometry.values()))
    return loaded


results = {"revision": "R0.5", "files": {}}
manifest = json.loads((RELEASE_DIR / "dimensions.json").read_text())
if manifest.get("voltmeter_cutout_mm") != [45.17, 26.39]:
    raise RuntimeError(f"Unexpected R0.5 voltmeter cutout: {manifest.get('voltmeter_cutout_mm')}")
results["voltmeter_cutout_mm"] = manifest["voltmeter_cutout_mm"]
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

body_extent = results["files"]["MCH-MkI_body_R0.5"]["extents_mm"]
if not np.allclose(body_extent, [140.0, 90.0, 52.0], atol=0.02):
    raise RuntimeError(f"Body envelope is incorrect: {body_extent}")

body_step = cq.importers.importStep(str(STEP_DIR / "MCH-MkI_body_R0.5.step"))
lid_step = cq.importers.importStep(str(STEP_DIR / "MCH-MkI_lid_R0.5.step")).translate((0, 0, 52.0))
intersection = body_step.intersect(lid_step)
interference_volume = sum(s.Volume() for s in intersection.solids().vals())
if interference_volume > 0.05:
    raise RuntimeError(f"Body/lid interference: {interference_volume:.4f} mm^3")
results["assembled_body_lid_interference_mm3"] = round(float(interference_volume), 6)

(RELEASE_DIR / "validation_report.json").write_text(json.dumps(results, indent=2) + "\n")

lines = [
    "# R0.5 Validation Report",
    "",
    "All matching STL, 3MF, and STEP exports passed automated validation.",
    "",
    "R0.5 voltmeter cutout: **45.17 × 26.39 mm** (1.00 mm wider than R0.4; height unchanged).",
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
    "Checks performed: watertightness, winding consistency, positive volume, 3MF package structure and millimeter units, STL/3MF extent agreement, STEP re-import, the 140 × 90 × 52 mm body envelope, and body/lid interference.",
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
