# TOIL Release Evidence (SHA-256)

This folder contains SHA-256 manifests for **canonical TOIL legal baseline** artifacts.

## Why this exists
- Evidence-grade pinning of the exact text used for a release
- Reduced ambiguity during enforcement, audits, and partner diligence

## Canonical set (v1.0 baseline)
Manifests should cover (at minimum):
- `LICENSE.md`
- `license/TOIL_v1.0.md`
- `license/TOIL_Legal_Architecture.md`
- `templates/TOIL_Royalty_Agreement_Template_v1.0.md`
- `templates/Tech4Life_Mutual_NDA_v1.0.md`
- `CHANGELOG.md`
- `AMENDMENTS.md`
- `RELEASING.md`

## Verification
Locally (or in CI), verify the baseline with:

```bash
python3 tools/verify_release.py --version 1.0
