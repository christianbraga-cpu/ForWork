#!/usr/bin/env python3
"""Deterministic on-page checks for a built page.

Usage:
  python3 seo-team/tools/check_page.py <page.html> [--registry seo-team/architecture/link-registry.csv]
      [--primary "keyword"] [--allow-index] [--json]

Exit code 1 when any error is found. Used by the page-builder (BD-06) and
technical-qa (TG-01). No third-party dependencies.
"""
import argparse
import csv
import json
import re
import sys
from html.parser import HTMLParser

FORBIDDEN = [
    "cheap", "affordable", "budget-friendly", "bargain", "discount",
    "fairytale", "dream come true", "magical", "once in a lifetime",
    "breathtaking", "stunning", "world-class", "unparalleled", "nestled",
    "seamless", "stress-free", "hassle-free", "book now", "hurry", "limited time",
]
SKIP_TEXT = {"script", "style", "noscript", "template"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.html_lang = None
        self.title = ""
        self.metas = []
        self.links = []
        self.headings = []
        self.images = []
        self.anchors = []
        self.jsonld = []
        self.forms = []
        self.text = []
        self._cur_heading = None
        self._cur_anchor = None
        self._in_title = False
        self._in_jsonld = False
        self._jsonld_buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if tag == "html":
            self.html_lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            self.metas.append(a)
        elif tag == "link":
            self.links.append(a)
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._cur_heading = [int(tag[1]), ""]
        elif tag == "img":
            self.images.append(a)
        elif tag == "a":
            self._cur_anchor = [a, ""]
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_jsonld = True
            self._jsonld_buf = []
        elif tag == "form":
            self.forms.append(a)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        while self.stack:
            if self.stack.pop() == tag:
                break
        if tag == "title":
            self._in_title = False
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._cur_heading:
            self.headings.append((self._cur_heading[0], self._cur_heading[1].strip()))
            self._cur_heading = None
        elif tag == "a" and self._cur_anchor:
            self.anchors.append((self._cur_anchor[0], self._cur_anchor[1].strip()))
            self._cur_anchor = None
        elif tag == "script" and self._in_jsonld:
            self.jsonld.append("".join(self._jsonld_buf))
            self._in_jsonld = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_jsonld:
            self._jsonld_buf.append(data)
            return
        if any(t in SKIP_TEXT for t in self.stack):
            return
        if self._cur_heading is not None:
            self._cur_heading[1] += data
        if self._cur_anchor is not None:
            self._cur_anchor[1] += data
        self.text.append(data)


def load_registry(path):
    if not path:
        return None
    try:
        with open(path, newline="", encoding="utf-8") as f:
            return {row["url"].rstrip("/") or "/": row for row in csv.DictReader(f)}
    except FileNotFoundError:
        return None


def walk_jsonld(node, found):
    if isinstance(node, dict):
        t = node.get("@type")
        if t:
            found.append(node)
        for v in node.values():
            walk_jsonld(v, found)
    elif isinstance(node, list):
        for v in node:
            walk_jsonld(v, found)


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def check(path, registry_path=None, primary=None, allow_index=False):
    errors, warnings, info = [], [], {}
    with open(path, encoding="utf-8") as f:
        p = Page()
        p.feed(f.read())

    def meta(name=None, prop=None):
        for m in p.metas:
            if name and (m.get("name") or "").lower() == name:
                return m.get("content")
            if prop and (m.get("property") or "").lower() == prop:
                return m.get("content")
        return None

    text = norm(" ".join(p.text))
    words = len(text.split())
    info["word_count"] = words

    if not p.html_lang:
        errors.append("html: missing lang attribute")

    title = p.title.strip()
    info["title"] = title
    if not title:
        errors.append("title: missing")
    elif len(title) > 60:
        warnings.append(f"title: {len(title)} chars (max 60)")

    desc = meta(name="description")
    info["meta_description"] = desc
    if not desc:
        errors.append("meta description: missing")
    elif not 120 <= len(desc) <= 155:
        warnings.append(f"meta description: {len(desc)} chars (target 120 to 155)")

    robots = (meta(name="robots") or "").lower()
    info["robots"] = robots
    if not allow_index and "noindex" not in robots:
        errors.append("robots: noindex missing (required until sign-off)")

    canon = [l.get("href") for l in p.links if (l.get("rel") or "").lower() == "canonical"]
    info["canonical"] = canon[0] if canon else None
    if len(canon) != 1:
        errors.append(f"canonical: expected 1, found {len(canon)}")
    elif not canon[0].startswith("http"):
        errors.append("canonical: must be absolute")

    if not meta(prop="og:title"):
        warnings.append("og:title missing")

    h1s = [h for lvl, h in p.headings if lvl == 1]
    info["h1"] = h1s
    if len(h1s) != 1:
        errors.append(f"h1: expected 1, found {len(h1s)}")
    prev = 0
    for lvl, h in p.headings:
        if prev and lvl > prev + 1:
            warnings.append(f"heading skip: h{prev} to h{lvl} at '{h[:50]}'")
        prev = lvl

    if primary:
        kw = norm(primary)
        first100 = " ".join(text.split()[:100])
        info["primary_keyword"] = {
            "in_title": kw in norm(title),
            "in_h1": any(kw in norm(h) for h in h1s),
            "in_first_100_words": kw in first100,
            "occurrences": text.count(kw),
        }
        for k in ("in_title", "in_h1", "in_first_100_words"):
            if not info["primary_keyword"][k]:
                warnings.append(f"primary keyword not {k.replace('_', ' ')}")

    raw_visible = " ".join(p.text)
    if "\u2014" in raw_visible:
        errors.append(f"em dash found in visible text ({raw_visible.count(chr(0x2014))}x)")
    for term in FORBIDDEN:
        if re.search(r"\b" + re.escape(term) + r"\b", text):
            warnings.append(f"forbidden term: '{term}'")
    if len(re.findall(r"\bluxury\b", text)) > 1:
        warnings.append("'luxury' used more than once")
    placeholders = re.findall(r"\[\[CONFIRM:[^\]]*\]\]", raw_visible)
    info["confirm_placeholders"] = len(placeholders)
    if placeholders:
        warnings.append(f"{len(placeholders)} [[CONFIRM]] placeholders (must be on SIGNOFF.md)")

    for i, img in enumerate(p.images):
        src = img.get("src") or img.get("data-src") or f"img#{i}"
        if "alt" not in img:
            errors.append(f"img {src}: missing alt")
        if not (img.get("width") and img.get("height")):
            warnings.append(f"img {src}: missing width/height")
        if i == 0 and img.get("loading") == "lazy":
            warnings.append(f"img {src}: first image is lazy-loaded (likely LCP)")
    info["images"] = len(p.images)

    registry = load_registry(registry_path)
    internal, external = [], []
    for a, label in p.anchors:
        href = a.get("href") or ""
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        if href.startswith("http"):
            external.append((href, a.get("rel", ""), label))
        else:
            internal.append((href.split("#")[0].split("?")[0].rstrip("/") or "/", label))
        if not label and not a.get("aria-label"):
            warnings.append(f"link {href}: no anchor text")
        if norm(label) in ("click here", "here", "read more", "learn more"):
            warnings.append(f"link {href}: generic anchor '{label}'")
    info["internal_links"] = len(internal)
    info["external_links"] = len(external)
    if registry is not None:
        for href in sorted({h for h, _ in internal}):
            row = registry.get(href)
            if row is None:
                warnings.append(f"internal link {href}: not in registry")
            elif row.get("status") == "planned":
                errors.append(f"internal link {href}: registry status is planned (page does not exist)")
            elif row.get("status") == "unverified":
                warnings.append(f"internal link {href}: unverified (put on SIGNOFF.md)")

    types = []
    for i, block in enumerate(p.jsonld):
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            errors.append(f"JSON-LD block {i}: invalid JSON ({e})")
            continue
        nodes = []
        walk_jsonld(data, nodes)
        for n in nodes:
            t = n.get("@type")
            types.extend(t if isinstance(t, list) else [t])
            if t == "FAQPage":
                for q in n.get("mainEntity", []):
                    qn = norm(q.get("name", ""))
                    if qn and qn not in text:
                        errors.append(f"FAQPage question not visible on page: '{q.get('name')[:60]}'")
            if t == "Offer" and n.get("price"):
                price = str(n["price"])
                pretty = f"{int(float(price)):,}" if re.fullmatch(r"\d+(\.\d+)?", price) else price
                if pretty not in raw_visible and price not in raw_visible:
                    errors.append(f"Offer price {price} not visible on page")
    info["schema_types"] = sorted(set(t for t in types if isinstance(t, str)))

    info["forms"] = [f.get("action") for f in p.forms]
    return {"file": path, "errors": errors, "warnings": warnings, "info": info}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("page")
    ap.add_argument("--registry", default="seo-team/architecture/link-registry.csv")
    ap.add_argument("--primary")
    ap.add_argument("--allow-index", action="store_true", help="Do not require noindex (audit of a live page)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    r = check(args.page, args.registry, args.primary, args.allow_index)
    if args.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
    else:
        print(f"{r['file']}: {len(r['errors'])} errors, {len(r['warnings'])} warnings")
        for e in r["errors"]:
            print("  ERROR", e)
        for w in r["warnings"]:
            print("  warn ", w)
        print("  info ", json.dumps(r["info"], ensure_ascii=False))
    sys.exit(1 if r["errors"] else 0)


if __name__ == "__main__":
    main()
