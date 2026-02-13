# Amendments Protocol (TOIL)

TOIL changes must be controlled to prevent legal drift and enforcement ambiguity.

## Definitions

- **Substantive change**: changes meaning, rights, obligations, enforcement posture, definitions, or scope.
- **Non-substantive change**: typos, formatting, link fixes, or clarifications that do not alter meaning.

## Rules

1. **Substantive changes MUST:**
   - update `CHANGELOG.md`
   - increment TOIL version (`vMAJOR.MINOR`)
   - include an “Amendment note” in the PR description:
     - what changed
     - why
     - who is impacted
     - effective date guidance
2. **Non-substantive changes SHOULD:**
   - be recorded under `CHANGELOG.md` (patch / housekeeping)

## Effective date posture

- The effective date for any new TOIL version is the merge date into `main` unless otherwise specified.
- Commercial agreements should reference the pinned TOIL version they were executed against.

## Priority of documents

When interpreting TOIL artifacts:
1. `license/TOIL_vX.Y.md` (canonical license terms)
2. Commercial templates (royalty agreement / NDA) when executed with counterparties
3. Legal architecture (interpretive / explanatory unless explicitly designated as normative)

## Release evidence

For each published TOIL version:
- add/update SHA-256 manifests under `license/releases/`
- tag a repo release
