# Contributing to TOIL

TOIL is the legal baseline for the Tech4Life ecosystem.
Changes here can have enforcement, commercial, and reputational impact.

## Core rules

1. **PRs only.** No direct commits to `main`.
2. **No silent legal drift.**
   - Any substantive change MUST be recorded in `CHANGELOG.md`.
   - Any change to canonical license text MUST follow `AMENDMENTS.md`.
3. **Treat canonical texts as evidence artifacts.**
   - Update release manifests under `license/releases/` when publishing a release.
4. **Prefer minimal diffs.**
   - Small PRs with clear intent.
5. **No contradictory terms.**
   - If a definition changes, update all dependent templates/docs consistently.

## Branch naming
Use:
- `toil/p0-<short-scope>`
- `toil/p1-<short-scope>`
- `toil/p2-<short-scope>`

Examples:
- `toil/p0-release-and-governance-controls`
- `toil/p1-enforcement-annex`

## Review checklist (before opening PR)

- [ ] Is this change substantive/legal-impacting? If yes: updated `CHANGELOG.md`
- [ ] If license text changed: followed `AMENDMENTS.md`
- [ ] Are templates still consistent with license definitions?
- [ ] Are release manifests updated (when releasing)?
