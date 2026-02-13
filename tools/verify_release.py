#!/usr/bin/env python3
"""Verify TOIL release integrity.

Checks:
- All canonical files exist
- LICENSE.md is byte-identical to license/TOIL_vX.Y.md for the active version
- SHA-256 manifest matches current working tree (LF-normalized by .gitattributes)
- Files are valid UTF-8 (no decode errors)

Usage:
  python3 tools/verify_release.py --version 1.0
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_manifest(manifest_path: Path) -> list[tuple[str, str]]:
    # returns list of (expected_hash, rel_path)
    rows: list[tuple[str, str]] = []
    for raw in manifest_path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        parts = raw.split()
        if len(parts) < 2:
            raise ValueError(f"Invalid manifest line: {raw}")
        expected = parts[0]
        rel_path = parts[-1]
        rows.append((expected, rel_path))
    return rows


def assert_utf8(paths: list[Path]) -> None:
    for p in paths:
        try:
            p.read_text(encoding="utf-8")
        except UnicodeDecodeError as e:
            raise RuntimeError(
                f"UTF-8 decode failed for {p.relative_to(REPO_ROOT)}: {e}"
            ) from e


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", required=True, help="TOIL version, e.g., 1.0")
    args = ap.parse_args()

    version = args.version
    license_path = REPO_ROOT / "LICENSE.md"
    canonical_license_path = REPO_ROOT / "license" / f"TOIL_v{version}.md"
    manifest_path = (
        REPO_ROOT / "license" / "releases" / f"TOIL_v{version}.manifest.sha256"
    )

    required = [
        license_path,
        canonical_license_path,
        REPO_ROOT / "license" / "TOIL_Legal_Architecture.md",
        REPO_ROOT / "templates" / f"TOIL_Royalty_Agreement_Template_v{version}.md",
        REPO_ROOT / "templates" / f"Tech4Life_Mutual_NDA_v{version}.md",
        REPO_ROOT / "CHANGELOG.md",
        REPO_ROOT / "AMENDMENTS.md",
        REPO_ROOT / "RELEASING.md",
        manifest_path,
    ]

    missing = [p for p in required if not p.exists()]
    if missing:
        print("Missing required files:")
        for p in missing:
            print(f" - {p.relative_to(REPO_ROOT)}")
        return 2

    # UTF-8 check
    assert_utf8([p for p in required if p.suffix in {".md", ".yml", ".yaml", ".txt"}])

    # Parity check (byte-identical)
    if license_path.read_bytes() != canonical_license_path.read_bytes():
        print("ERROR: LICENSE.md is not byte-identical to canonical license file.")
        print(f"Expected: {canonical_license_path.relative_to(REPO_ROOT)}")
        return 3

    # Manifest check
    manifest_rows = read_manifest(manifest_path)
    failures = []
    for expected, rel in manifest_rows:
        file_path = REPO_ROOT / rel
        if not file_path.exists():
            failures.append((rel, "missing"))
            continue
        actual = sha256_file(file_path)
        if actual != expected:
            failures.append((rel, f"hash_mismatch expected={expected} actual={actual}"))
    if failures:
        print("ERROR: Manifest verification failed:")
        for rel, reason in failures:
            print(f" - {rel}: {reason}")
        return 4

    print("OK: TOIL release integrity verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
