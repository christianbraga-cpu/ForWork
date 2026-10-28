#!/usr/bin/env python3
"""Validate Page Studio envelopes (and facts.json) against the schemas.

Usage:
  python3 studio/tools/validate_envelope.py <file.json> [<file.json> ...]

A file named facts.json is validated as a fact ledger. Anything else is
validated as an envelope, with its payload checked against the schema for
its payload_type. Exits 1 if any file is invalid.
"""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

SCHEMAS = Path(__file__).resolve().parent.parent / "schemas"


def build_registry():
    resources = []
    for path in SCHEMAS.rglob("*.schema.json"):
        schema = json.loads(path.read_text())
        resources.append((schema["$id"], Resource.from_contents(schema)))
    return Registry().with_resources(resources)


def load_schema(rel):
    return json.loads((SCHEMAS / rel).read_text())


def validate(path, registry):
    try:
        doc = json.loads(Path(path).read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read JSON: {exc}"]
    rel = "payloads/fact_ledger.schema.json" if Path(path).name == "facts.json" else "envelope.schema.json"
    validator = Draft202012Validator(load_schema(rel), registry=registry, format_checker=FormatChecker())
    errors = []
    for err in sorted(validator.iter_errors(doc), key=lambda e: list(e.absolute_path)):
        where = "/".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"{where}: {err.message}")
    errors += em_dash_check(doc)
    return errors


def em_dash_check(doc):
    text = json.dumps(doc, ensure_ascii=False)
    return ["contains an em dash (brand rule: never use em dashes)"] if chr(0x2014) in text else []


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    registry = build_registry()
    failed = False
    for path in argv:
        errors = validate(path, registry)
        if errors:
            failed = True
            print(f"INVALID {path}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"OK {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
