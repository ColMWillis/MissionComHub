# Contributing

## Workflow

1. Open an issue identifying the requirement or defect.
2. Create a branch named `type/issue-short-description`.
3. Keep CAD source, exported files, and documentation changes in the same pull request when they represent one revision.
4. Include photographs or slicer screenshots for print-fit changes.
5. Do not label a part production-ready until physical fit has been verified.

## Revision markings

Prototype printed parts shall include an internal revision marking, for example:

`MCH-MK1 R0.5 PROTOTYPE`

## CAD exports

Each released mechanical revision should include:

- Native CAD source
- STEP
- STL
- PrusaSlicer 3MF
- Dimensioned PDF drawing
- Changelog entry

Generated exports must also pass the repository validation script, and physical coupon feedback must be recorded before changing a fit-tested dimension.

Binary exports should match the same source-model commit.
