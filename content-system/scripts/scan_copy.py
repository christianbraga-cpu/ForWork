#!/usr/bin/env python3
"""Scan a draft for banned phrases, em dashes and overlap with competitor pages.

Usage: python3 -I content-system/scripts/scan_copy.py <draft.md> [competitor_text_dir]
competitor_text_dir: folder of .md/.txt files (e.g. content/posts/<slug>/02-research/pages)
Prints JSON: {"banned": [...], "flagged": {...}, "dashes": n, "overlaps": [...]}
"""
import json
import re
import sys
from pathlib import Path

BANNED_FILE = Path(__file__).resolve().parent.parent / "brand" / "banned-phrases.md"
NGRAM = 12


def phrase_lists():
    banned, flagged, section = [], [], None
    for line in BANNED_FILE.read_text().splitlines():
        if line.startswith("## "):
            section = line[3:].strip().lower()
            continue
        if not line.startswith("- "):
            continue
        item = re.sub(r"\(.*?\)", "", line[2:]).strip()
        terms = [t.strip().strip('"') for t in item.split(",") if t.strip()]
        if section and section.startswith("banned"):
            banned += [t for t in terms if t not in ("—", "–") and "em dash" not in t]
        elif section and section.startswith("flagged"):
            flagged += terms
        elif section and section.startswith("competitor"):
            banned += [t for t in terms if "Any other" not in t]
    return banned, flagged


def words(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def main(draft, comp_dir=None):
    text = Path(draft).read_text()
    lower = text.lower()
    banned, flagged = phrase_lists()
    result = {
        "banned": sorted({b for b in banned if re.search(r"\b" + re.escape(b.lower()) + r"\b", lower)}),
        "flagged": {f: len(re.findall(r"\b" + re.escape(f.lower()) + r"\b", lower)) for f in flagged},
        "dashes": len(re.findall(r"—|\s–\s", text)),
        "overlaps": [],
    }
    result["flagged"] = {k: v for k, v in result["flagged"].items() if v}
    if comp_dir:
        dw = words(text)
        draft_grams = {" ".join(dw[i:i + NGRAM]) for i in range(len(dw) - NGRAM + 1)}
        for f in sorted(Path(comp_dir).glob("*")):
            if f.suffix not in (".md", ".txt"):
                continue
            cw = words(f.read_text(errors="ignore"))
            hits = {" ".join(cw[i:i + NGRAM]) for i in range(len(cw) - NGRAM + 1)} & draft_grams
            if hits:
                result["overlaps"].append({"source": f.name, "count": len(hits), "examples": sorted(hits)[:3]})
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    main(*sys.argv[1:])
