# Amendments — TOIL

This document defines how TOIL legal texts and templates may be amended.

## Scope

Applies to:
- `license/TOIL_v*.md`
- `license/TOIL_Legal_Architecture.md`
- `templates/TOIL_Royalty_Agreement_Template_v*.md`
- `templates/Tech4Life_Mutual_NDA_v*.md`
- `LICENSE.md` (must remain identical to the active TOIL version)
- Release evidence under `license/releases/`

## Amendment types

### A) Substantive amendments
Changes that alter:
- rights or obligations
- enforcement posture
- ethical restrictions
- commercial licensing mechanics
- definitions or scope

These must trigger a version bump and a release evidence update.

### B) Non-substantive amendments
Changes that do not alter meaning:
- spelling/grammar
- formatting
- clarifying examples that do not change obligations
- broken links

These may be grouped into a patch-level release tag if desired.

## Approval authority

Substantive legal changes require **explicit approval**.

- **Minimum approvals (current org state):**
  - Founder / acting Legal Steward (until a Legal team exists)

- **Target approvals (scale-ready):**
  - Legal Steward approval (legal-private)
  - Architect consensus for doctrine-impacting changes (per TLOS governance model)
  - Recorded approval in PR (review + decision log reference)

Non-substantive changes may be approved via normal maintainer review.

## Release evidence requirements

For substantive amendments:
1. Update `CHANGELOG.md`
2. Update the `license/releases/TOIL_vX.Y.manifest.sha256`
3. Ensure `LICENSE.md` is byte-identical to `license/TOIL_vX.Y.md`
4. Tag the release

## Effective date posture

Unless explicitly stated, amendments become effective on the date of the tagged release.

Tech4Life & Beyond LLC may publish notice of amendments in the repository history and release notes.
