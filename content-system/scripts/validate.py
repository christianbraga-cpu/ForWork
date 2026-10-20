#!/usr/bin/env python3
"""Validate a post folder against the content-system schemas.

Usage: python3 -I content-system/scripts/validate.py content/posts/<slug>
Exit code 0 = all present files valid, 1 = problems found.
"""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

SCHEMAS = Path(__file__).resolve().parent.parent / "schemas"

# stage file -> payload schema (None = envelope only)
STAGE_FILES = {
    "01-brief.json": "01-brief.schema.json",
    "02-seo.json": "02-seo.schema.json",
    "03-source-pack.json": "03-source-pack.schema.json",
    "04-images.json": "04-images.schema.json",
    "06-edit.json": "06-edit.schema.json",
    "07-panel.json": "07-panel.schema.json",
    "09-cro.json": "09-cro.schema.json",
    "10-distribution.json": "10-distribution.schema.json",
    "11-publish-package.json": "11-publish-package.schema.json",
}


def load_schema(name):
    return json.loads((SCHEMAS / name).read_text())


def check(path, payload_schema, problems):
    try:
        doc = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        problems.append(f"{path.name}: invalid JSON ({e})")
        return None
    for err in Draft202012Validator(load_schema("envelope.schema.json")).iter_errors(doc):
        problems.append(f"{path.name}: envelope {'/'.join(map(str, err.path))}: {err.message}")
    if payload_schema and isinstance(doc.get("payload"), dict):
        for err in Draft202012Validator(load_schema(payload_schema)).iter_errors(doc["payload"]):
            problems.append(f"{path.name}: payload {'/'.join(map(str, err.path))}: {err.message}")
    return doc


def main(folder):
    folder = Path(folder)
    problems, seen = [], []
    for fname, schema in STAGE_FILES.items():
        p = folder / fname
        if p.exists():
            seen.append(fname)
            doc = check(p, schema, problems)
            if doc and fname == "11-publish-package.json":
                pl = doc.get("payload", {})
                cats = pl.get("categories") or []
                if cats and pl.get("primary_category") != cats[0]:
                    problems.append("11-publish-package.json: primary_category must equal categories[0]")
            if doc and fname == "04-images.json":
                for s in doc.get("payload", {}).get("slots", []):
                    if s.get("status") == "approved" and "reference-only" in s.get("file", ""):
                        problems.append(f"04-images.json: slot {s.get('slot_id')} uses a reference-only image")
    icp = folder / "07-icp"
    if icp.is_dir():
        for p in sorted(icp.glob("*.json")):
            seen.append(f"07-icp/{p.name}")
            check(p, "07-icp.schema.json", problems)

    print(f"Checked {len(seen)} stage files in {folder}")
    for s in seen:
        print(f"  - {s}")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for pr in problems:
            print(f"  ✗ {pr}")
        return 1
    print("All valid.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
