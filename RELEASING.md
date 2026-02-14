# Releasing & Versioning (TOIL)

TOIL is a legal baseline. Versioning must be **auditable** and **evidence-grade**.

## Canonical document set (TOIL legal baseline)

For a given TOIL release, the canonical set includes:
- `LICENSE.md` (must remain byte-identical to `license/TOIL_vX.Y.md`)
- `license/TOIL_vX.Y.md`
- `license/TOIL_Legal_Architecture.md` (versioned as needed)
- `templates/TOIL_Royalty_Agreement_Template_vX.Y.md`
- `templates/Tech4Life_Mutual_NDA_vX.Y.md`
- `CHANGELOG.md`
- `AMENDMENTS.md`
- `RELEASING.md`
- Release manifests under `license/releases/`

## Version model

- **TOIL version**: `vMAJOR.MINOR`
  - MAJOR: breaking legal/behavior change or enforcement semantics change
  - MINOR: additive clarifications that do not change core rights/obligations
- **Repository release tags** (recommended): `toil-vMAJOR.MINOR.PATCH`

## Evidence requirement (hash manifests)

For each release:
1. Generate the canonical SHA-256 manifest with `python3 tools/build_release_manifest.py --version X.Y`.
2. Commit the updated manifest under `license/releases/`.
3. Tag the release.

## Notes

- Draft changes may exist on branches, but canonical meaning is tied to:
  - merged main history
  - changelog entries
  - release manifests
  - tags
