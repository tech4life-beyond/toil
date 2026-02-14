#!/usr/bin/env python3
"""Build or check TOIL release manifest for a given version.

Usage:
  python3 tools/build_release_manifest.py --version 1.0
  python3 tools/build_release_manifest.py --version 1.0 --check
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_files(version: str) -> list[Path]:
    return [
        REPO_ROOT / "LICENSE.md",
        REPO_ROOT / "license" / f"TOIL_v{version}.md",
        REPO_ROOT / "license" / "TOIL_Legal_Architecture.md",
        REPO_ROOT / "templates" / f"TOIL_Royalty_Agreement_Template_v{version}.md",
        REPO_ROOT / "templates" / f"Tech4Life_Mutual_NDA_v{version}.md",
        REPO_ROOT / "CHANGELOG.md",
        REPO_ROOT / "AMENDMENTS.md",
        REPO_ROOT / "RELEASING.md",
    ]


def render_manifest_lines(files: list[Path]) -> list[str]:
    return [f"{sha256_file(p)}  {p.relative_to(REPO_ROOT).as_posix()}" for p in files]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", required=True, help="TOIL version, e.g., 1.0")
    ap.add_argument(
        "--check",
        action="store_true",
        help="check manifest is current without rewriting it",
    )
    args = ap.parse_args()

    files = canonical_files(args.version)
    missing = [p for p in files if not p.exists()]
    if missing:
        print("Missing required files:")
        for p in missing:
            print(f" - {p.relative_to(REPO_ROOT)}")
        return 2

    manifest_path = (
        REPO_ROOT / "license" / "releases" / f"TOIL_v{args.version}.manifest.sha256"
    )
    expected_text = "\n".join(render_manifest_lines(files)) + "\n"

    if args.check:
        if not manifest_path.exists():
            print(f"ERROR: Missing manifest {manifest_path.relative_to(REPO_ROOT)}")
            print(
                f"Run: python3 tools/build_release_manifest.py --version {args.version} and commit the result."
            )
            return 3

        actual_text = manifest_path.read_text(encoding="utf-8")
        if actual_text != expected_text:
            print(
                f"ERROR: Manifest is out of date: {manifest_path.relative_to(REPO_ROOT)}"
            )
            diff = difflib.unified_diff(
                actual_text.splitlines(),
                expected_text.splitlines(),
                fromfile="committed",
                tofile="expected",
                lineterm="",
            )
            print("\n".join(diff))
            print(
                f"Run: python3 tools/build_release_manifest.py --version {args.version} and commit the updated manifest."
            )
            return 4

        print(f"OK: Manifest is up to date: {manifest_path.relative_to(REPO_ROOT)}")
        return 0

    manifest_path.write_text(expected_text, encoding="utf-8")
    print(f"Wrote {manifest_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
