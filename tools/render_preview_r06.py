from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import trimesh
import numpy as np

repo = Path(__file__).resolve().parents[1]
root = repo / "CAD/STL/R0.6"
fig = plt.figure(figsize=(18, 7), dpi=120, facecolor="#f1f3f6")
items = [
    ("MCH-MkI_body_R0.6.stl", 28, -45, "Body: controls and interior"),
    ("MCH-MkI_body_R0.6.stl", 28, 45, "Body: I/O and interior"),
    ("MCH-MkI_lid_R0.6.stl", 72, -90, "Branded locating-lip lid"),
]
for i, (filename, elev, azim, title) in enumerate(items, start=1):
    mesh = trimesh.load_mesh(root / filename, force="mesh")
    triangles = mesh.triangles
    normals = mesh.face_normals
    light = np.array([0.35, -0.45, 0.82])
    light /= np.linalg.norm(light)
    shade = 0.35 + 0.55 * np.clip(normals @ light, 0, 1)
    colors = np.column_stack([shade * 0.42, shade * 0.47, shade * 0.54, np.ones_like(shade)])
    ax = fig.add_subplot(1, 3, i, projection="3d")
    poly = Poly3DCollection(triangles, facecolors=colors, edgecolors="none", linewidth=0)
    ax.add_collection3d(poly)
    mins, maxs = mesh.bounds
    center = (mins + maxs) / 2
    span = max(maxs - mins) * 0.54
    ax.set_xlim(center[0]-span, center[0]+span)
    ax.set_ylim(center[1]-span, center[1]+span)
    ax.set_zlim(center[2]-span, center[2]+span)
    ax.set_box_aspect((1,1,1))
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    ax.set_title(title, fontsize=14, pad=10)
fig.tight_layout()
out = repo / "images/R0.6_preview.png"
fig.savefig(out, bbox_inches="tight")
print(out)
