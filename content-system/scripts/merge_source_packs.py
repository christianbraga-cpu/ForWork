#!/usr/bin/env python3
"""Merge parallel planner-sme batch files into one 03-source-pack.json.

Usage: python3 -I content-system/scripts/merge_source_packs.py <post_folder>
Reads <post_folder>/03-source-pack.json (general facts, may be absent) and every
<post_folder>/03-source-pack-part-*.json, then writes the merged 03-source-pack.json.
Batches must use separate fact_id ranges (e.g. part 1: fact_100+, part 2: fact_200+).
"""
import json
import sys
from pathlib import Path

LIST_KEYS = ("facts", "insider_details", "quotes", "real_weddings", "verify_items",
             "needs_signoff", "must_include_coverage")


def main(folder):
    folder = Path(folder)
    parts = sorted(folder.glob("03-source-pack-part-*.json"))
    if not parts:
        sys.exit("No 03-source-pack-part-*.json files found")
    base_path = folder / "03-source-pack.json"
    base = json.loads(base_path.read_text()) if base_path.exists() else None
    docs = ([base] if base else []) + [json.loads(p.read_text()) for p in parts]
    out = docs[0]
    payload = {k: [] for k in LIST_KEYS}
    seen_ids = set()
    for d in docs:
        p = d["payload"]
        for k in LIST_KEYS:
            for item in p.get(k, []):
                if k == "facts":
                    if item["fact_id"] in seen_ids:
                        sys.exit(f"Duplicate fact_id {item['fact_id']}: batches must use separate ranges")
                    seen_ids.add(item["fact_id"])
                if item not in payload[k]:
                    payload[k].append(item)
        if p.get("budget_range_aud") and not payload.get("budget_range_aud"):
            payload["budget_range_aud"] = p["budget_range_aud"]
    out["payload"] = payload
    for k in ("verify_items", "assumptions", "open_questions", "inputs_used", "tools_used"):
        merged = []
        for d in docs:
            for x in d.get(k, []):
                if x not in merged:
                    merged.append(x)
        out[k] = merged
    out["status"] = "complete" if all(d.get("status") == "complete" for d in docs) else "needs_input"
    out["self_qa"]["confidence"] = min(d["self_qa"]["confidence"] for d in docs)
    base_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Merged {len(docs)} files: {len(payload['facts'])} facts, {len(payload['verify_items'])} verify items")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
