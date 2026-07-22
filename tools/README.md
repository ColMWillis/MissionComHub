# Release Tools

The R0.5 validation and preview scripts require Python plus `cadquery`, `trimesh`, `numpy`, and `matplotlib`.

From the repository root:

```text
python tools/validate_release_r05.py
python tools/render_preview_r05.py
```

The validator reads the canonical files under `CAD/3MF/R0.5`, `CAD/STL/R0.5`, and `CAD/STEP/R0.5`. It updates the validation reports and repository checksums under `CAD/Releases/R0.5`.
