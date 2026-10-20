#!/usr/bin/env python3
"""Turn a Firecrawl map result (saved as JSON) into content-system/seo/link-map.csv.

Usage: python3 -I content-system/scripts/build_linkmap.py <firecrawl_map.json> [traffic.json]
- firecrawl_map.json: the raw result of firecrawl_map (object with "links", or a list)
- traffic.json (optional): {"<path>": visitors, ...} from WeddedAdmin landing_pages_overview
Keeps existing rows' manual columns (primary_keyword, topic, notes) when the URL is already in the CSV.
"""
import csv
import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

OUT = Path(__file__).resolve().parent.parent / "seo" / "link-map.csv"
FIELDS = ["path", "url", "type", "title", "description", "primary_keyword", "topic", "visitors_30d", "noindex", "last_seen", "notes"]

TYPE_RULES = [
    ("/wonderland-concierge", "commercial"), ("/concierge", "commercial"), ("/privileges", "commercial"),
    ("/marketplace", "commercial"), ("/packages/", "package"), ("/venue/", "venue"), ("/vendor/", "vendor"),
    ("/destinations", "hub"), ("/au/", "hub"), ("/magazine", "magazine"), ("/expert-advice/", "article"),
    ("/style-advice/", "article"), ("/featured/", "article"), ("/trending/", "news"), ("/style/", "article"),
]
SKIP = ("/search", "/privacy", "/terms", "/contact", "/login", "/cart")


def classify(path):
    if path in ("", "/"):
        return "home"
    for prefix, t in TYPE_RULES:
        if path.startswith(prefix):
            return "hub" if t == "venue" and path.rstrip("/") == "/venue" else t
    return "article"


def main(map_file, traffic_file=None):
    raw = json.loads(Path(map_file).read_text())
    links = raw.get("links", raw) if isinstance(raw, dict) else raw
    traffic = json.loads(Path(traffic_file).read_text()) if traffic_file else {}
    existing = {}
    if OUT.exists():
        with OUT.open() as f:
            existing = {r["path"]: r for r in csv.DictReader(f)}
    rows = {}
    for item in links:
        url = item if isinstance(item, str) else item.get("url", "")
        p = urlparse(url)
        if "weddedwonderland.com" not in p.netloc:
            continue
        path = p.path.rstrip("/") or "/"
        if path.startswith(SKIP):
            continue
        old = existing.get(path, {})
        rows[path] = {
            "path": path, "url": f"https://weddedwonderland.com{path if path != '/' else ''}",
            "type": classify(path),
            "title": (item.get("title") if isinstance(item, dict) else "") or old.get("title", ""),
            "description": (item.get("description") if isinstance(item, dict) else "") or old.get("description", ""),
            "primary_keyword": old.get("primary_keyword", ""), "topic": old.get("topic", ""),
            "visitors_30d": traffic.get(path, old.get("visitors_30d", "")),
            "noindex": old.get("noindex", ""), "last_seen": date.today().isoformat(), "notes": old.get("notes", ""),
        }
    for path, old in existing.items():  # keep rows not in this crawl (e.g. drafts) but don't refresh last_seen
        rows.setdefault(path, old)
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for path in sorted(rows):
            w.writerow({k: rows[path].get(k, "") for k in FIELDS})
    print(f"Wrote {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    main(*sys.argv[1:])
