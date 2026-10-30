#!/usr/bin/env python3
"""Validate every envelope in a run folder.

Usage:
  python3 seo-team/tools/validate_run.py seo-team/runs/<run_id>

Checks each *.json against schemas/envelope.schema.json, the intake, fact ledger and
page brief payloads against their own schemas, and that every fact ID cited in the
brief and copy exists in the ledger. Exit code 1 on any error. No dependencies.
"""
import json
import pathlib
import sys

SCHEMAS = pathlib.Path(__file__).resolve().parent.parent / "schemas"
PAYLOAD_SCHEMAS = {
    "intake": "intake.schema.json",
    "fact_ledger": "fact-ledger.schema.json",
    "page_brief": "page-brief.schema.json",
}
TYPES = {
    "object": dict, "array": list, "string": str, "boolean": bool,
    "integer": int, "number": (int, float),
}


def validate(data, schema, path="$"):
    errs = []
    t = schema.get("type")
    if t:
        py = TYPES[t]
        if not isinstance(data, py) or (t in ("integer", "number") and isinstance(data, bool)):
            return [f"{path}: expected {t}, got {type(data).__name__}"]
    if "enum" in schema and data not in schema["enum"]:
        errs.append(f"{path}: '{data}' not in {schema['enum']}")
    if isinstance(data, dict):
        for k in schema.get("required", []):
            if k not in data:
                errs.append(f"{path}: missing '{k}'")
        for k, sub in schema.get("properties", {}).items():
            if k in data:
                errs.extend(validate(data[k], sub, f"{path}.{k}"))
    if isinstance(data, list):
        if "minItems" in schema and len(data) < schema["minItems"]:
            errs.append(f"{path}: fewer than {schema['minItems']} items")
        if "items" in schema:
            for i, item in enumerate(data):
                errs.extend(validate(item, schema["items"], f"{path}[{i}]"))
    if isinstance(data, (int, float)) and not isinstance(data, bool):
        if "minimum" in schema and data < schema["minimum"]:
            errs.append(f"{path}: below minimum {schema['minimum']}")
        if "maximum" in schema and data > schema["maximum"]:
            errs.append(f"{path}: above maximum {schema['maximum']}")
    return errs


def main(run_dir):
    run = pathlib.Path(run_dir)
    envelope = json.loads((SCHEMAS / "envelope.schema.json").read_text())
    loaded, errors = {}, []
    for f in sorted(run.glob("*.json")):
        try:
            doc = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{f.name}: invalid JSON ({e})")
            continue
        loaded[f.name] = doc
        errs = validate(doc, envelope)
        tt = doc.get("task_type")
        if tt in PAYLOAD_SCHEMAS and isinstance(doc.get("payload"), dict):
            ps = json.loads((SCHEMAS / PAYLOAD_SCHEMAS[tt]).read_text())
            errs += validate(doc["payload"], ps, "$.payload")
        if doc.get("status") in ("blocked", "needs_input") and not doc.get("blocked_on"):
            errs.append("$: status is blocked/needs_input but blocked_on is empty")
        errors += [f"{f.name}: {e}" for e in errs]

    ledger = next((d for d in loaded.values() if d.get("task_type") == "fact_ledger"), None)
    if ledger:
        ids = {fct.get("id") for fct in ledger.get("payload", {}).get("facts", [])}
        for name, doc in loaded.items():
            if doc.get("task_type") == "page_brief":
                for s in doc["payload"].get("sections", []):
                    for fid in s.get("fact_ids", []):
                        if fid not in ids:
                            errors.append(f"{name}: section {s.get('id')} cites unknown fact {fid}")
            if doc.get("task_type") == "copy":
                for c in doc["payload"].get("claims", []):
                    if c.get("fact_id") and c["fact_id"] not in ids:
                        errors.append(f"{name}: claim cites unknown fact {c['fact_id']}")
    elif loaded:
        errors.append("no fact_ledger envelope found")

    print(f"{run}: {len(loaded)} envelopes, {len(errors)} errors")
    for e in errors:
        print("  ERROR", e)
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
