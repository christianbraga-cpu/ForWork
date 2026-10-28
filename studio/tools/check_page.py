#!/usr/bin/env python3
"""Automated QA checks for a built Page Studio page.

Usage:
  python3 studio/tools/check_page.py <index.html> [--facts facts.json] [--brief 20-content-brief.json] [--out result.json]

Checks metadata, headings, schema, FAQ parity, prices, links, images, the
enquiry form, contact details, banned phrases and em dashes. Prints a summary
and exits 1 if any blocker fails.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "config.json").read_text())
BANNED = [l.strip().lower() for l in (ROOT / "standards" / "banned-phrases.txt").read_text().splitlines()
          if l.strip() and not l.startswith("#")]

results = []


def check(cid, ok, severity, detail=""):
    results.append({"check": cid, "pass": bool(ok), "severity": severity, "detail": detail})


def visible_text(soup):
    clone = BeautifulSoup(str(soup), "html.parser")
    for tag in clone(["script", "style", "noscript", "template"]):
        tag.decompose()
    return " ".join(clone.get_text(" ").split())


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", " ".join(s.lower().split()))


def load_json(path):
    return json.loads(Path(path).read_text()) if path else None


def payload(doc):
    return doc.get("payload", doc) if doc else None


def run(html_path, facts, brief):
    html = Path(html_path).read_text()
    soup = BeautifulSoup(html, "html.parser")
    text = visible_text(soup)
    domain = urlparse(CONFIG["brand"]["domain"]).netloc

    # Metadata
    html_tag = soup.find("html")
    check("lang_en_au", html_tag and html_tag.get("lang") == CONFIG["brand"]["locale"], "major",
          f"lang={html_tag.get('lang') if html_tag else None}")
    title = (soup.title.string or "").strip() if soup.title else ""
    check("title_length", 30 <= len(title) <= 65, "major", f"{len(title)} chars: {title}")
    desc = soup.find("meta", attrs={"name": "description"})
    d = desc.get("content", "") if desc else ""
    check("meta_description_length", 120 <= len(d) <= 165, "major", f"{len(d)} chars")
    canon = soup.find("link", rel="canonical")
    check("canonical_present", canon and canon.get("href", "").startswith(CONFIG["brand"]["domain"]), "blocker",
          canon.get("href") if canon else "missing")
    for prop in ("og:title", "og:description", "og:url"):
        check(f"{prop}_present", soup.find("meta", property=prop), "minor")

    # Headings
    h1s = soup.find_all("h1")
    check("single_h1", len(h1s) == 1, "major", f"{len(h1s)} h1 tags")
    levels = [int(h.name[1]) for h in soup.find_all(re.compile("^h[1-6]$"))]
    skips = [f"h{a}->h{b}" for a, b in zip(levels, levels[1:]) if b > a + 1]
    check("heading_order", not skips, "minor", ", ".join(skips[:5]))

    # Robots vs facts needing sign-off
    robots = soup.find("meta", attrs={"name": "robots"})
    noindex = bool(robots and "noindex" in robots.get("content", ""))
    pending = []
    if facts:
        pending = [f["id"] for f in facts["facts"] if f["status"] in ("unconfirmed", "conflict")]
    check("noindex_while_unconfirmed", noindex or not pending, "blocker",
          f"noindex={noindex}, unconfirmed facts={pending[:10]}")

    # JSON-LD
    graphs = []
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or "")
            graphs += data.get("@graph", [data]) if isinstance(data, dict) else data
            check("jsonld_parses", True, "blocker")
        except json.JSONDecodeError as exc:
            check("jsonld_parses", False, "blocker", str(exc))
    types = sorted({g.get("@type") for g in graphs if isinstance(g, dict) and isinstance(g.get("@type"), str)})
    if brief:
        missing = [t for t in brief.get("schema_types", []) if t not in types]
        check("schema_types_from_brief", not missing, "major", f"missing {missing}, found {types}")
    for g in graphs:
        if g.get("@type") == "FAQPage":
            nt = norm(text)
            absent = [q["name"] for q in g.get("mainEntity", []) if norm(q["name"]) not in nt]
            check("faq_schema_matches_visible", not absent, "blocker", f"not visible: {absent[:3]}")
        offers = g.get("offers")
        if isinstance(offers, dict):
            check("offer_currency_aud", offers.get("priceCurrency") == CONFIG["brand"]["currency"], "blocker",
                  str(offers.get("priceCurrency")))

    # Prices
    bare = re.findall(r"(?<!AUD )(?<!AUD)\$\s?\d[\d,]*", text)
    check("prices_use_from_aud", not bare, "blocker", f"bare prices: {bare[:5]}")
    aud = re.findall(r"(.{0,12})AUD\s?\d[\d,]*", text)
    no_from = [a for a in aud if "from" not in a.lower()]
    check("aud_prices_prefixed_from", not no_from, "major", f"{len(no_from)} AUD prices without 'From'")

    # Contact details (venue or supplier contacts must not appear)
    emails = [e for e in re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text) if domain not in e]
    phones = re.findall(r"\+\d[\d\s().-]{7,}\d", text)
    check("no_third_party_contacts", not emails and not phones, "blocker", f"emails={emails[:3]} phones={phones[:3]}")

    # Links
    internal, external = [], []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        host = urlparse(href).netloc
        if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
            continue
        (internal if (not host or host.endswith(domain)) else external).append(a)
    bad_anchor = [a.get_text(strip=True) for a in internal + external
                  if a.get_text(strip=True).lower() in ("click here", "here", "read more", "link")]
    check("descriptive_anchors", not bad_anchor, "minor", f"{bad_anchor[:5]}")
    unsafe = [a["href"] for a in external if a.get("target") == "_blank" and "noopener" not in (a.get("rel") or [])]
    check("external_links_noopener", not unsafe, "minor", f"{unsafe[:5]}")
    if brief:
        hrefs = {urlparse(a["href"]).path.rstrip("/") for a in internal}
        missing = [l["url"] for l in brief["link_plan"]["must_link_to"]
                   if urlparse(l["url"]).path.rstrip("/") not in hrefs]
        check("link_plan_implemented", not missing, "major", f"missing {missing}")
        cap = brief["link_plan"].get("max_internal_links")
        if cap:
            check("internal_link_cap", len(internal) <= cap * 3, "minor", f"{len(internal)} internal links")

    # Images
    imgs = soup.find_all("img")
    no_alt = [i.get("src") for i in imgs if i.get("alt") is None]
    check("img_alt_present", not no_alt, "major", f"{no_alt[:5]}")
    no_dims = [i.get("src") for i in imgs if not (i.get("width") and i.get("height"))]
    check("img_dimensions_set", not no_dims, "major", f"{no_dims[:5]}")
    if imgs:
        check("hero_not_lazy", imgs[0].get("loading") != "lazy", "major", imgs[0].get("src", ""))
    bad_names = [i.get("src") for i in imgs if re.search(r"(IMG|DSC|image)[_-]?\d+", i.get("src", ""), re.I)]
    check("img_descriptive_filenames", not bad_names, "minor", f"{bad_names[:5]}")
    placeholders = soup.select(".ph[data-img]")
    check("image_placeholders_listed", True, "minor", f"{len(placeholders)} placeholder slots awaiting images")

    # Enquiry form
    form = soup.find("form")
    if form:
        check("form_action", form.get("action") == CONFIG["brand"]["enquiry_endpoint"], "blocker", form.get("action", ""))
        route = form.find("input", attrs={"name": "route_to"})
        check("form_route_to", route and route.get("value") == CONFIG["brand"]["enquiry_route"], "blocker")
        unlabelled = [i.get("name") for i in form.find_all(["input", "select", "textarea"])
                      if i.get("type") not in ("hidden", "submit") and not i.get("aria-label")
                      and not (i.get("id") and form.find("label", attrs={"for": i.get("id")}))
                      and not i.find_parent("label")]
        check("form_fields_labelled", not unlabelled, "major", f"{unlabelled[:5]}")
    else:
        check("form_present", False, "blocker", "no enquiry form")

    # Copy rules
    check("no_em_dashes", chr(0x2014) not in text, "major", f"{text.count(chr(0x2014))} found")
    lowered = text.lower()
    hits = [b for b in BANNED if b in lowered]
    check("no_banned_phrases", not hits, "major", f"{hits}")
    words = len(text.split())
    if brief:
        lo, hi = brief["word_count_range"]
        check("word_count_in_range", lo * 0.8 <= words <= hi * 1.5, "minor", f"{words} words, brief {lo}-{hi}")

    return {"page": str(html_path), "word_count": words, "schema_types": types,
            "internal_links": len(internal), "external_links": len(external),
            "results": results,
            "failed": {s: [r["check"] for r in results if not r["pass"] and r["severity"] == s]
                       for s in ("blocker", "major", "minor")}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--facts")
    ap.add_argument("--brief")
    ap.add_argument("--out")
    args = ap.parse_args()
    report = run(args.html, load_json(args.facts), payload(load_json(args.brief)))
    if args.out:
        Path(args.out).write_text(json.dumps(report, indent=2, ensure_ascii=False))
    for r in results:
        if not r["pass"]:
            print(f"FAIL [{r['severity']}] {r['check']}: {r['detail']}")
    f = report["failed"]
    print(f"blockers={len(f['blocker'])} majors={len(f['major'])} minors={len(f['minor'])} "
          f"passed={sum(r['pass'] for r in results)}/{len(results)}")
    return 1 if f["blocker"] else 0


if __name__ == "__main__":
    sys.exit(main())
