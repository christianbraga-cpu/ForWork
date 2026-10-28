#!/usr/bin/env python3
"""Automated checks on a page_copy envelope (fast mode, no HTML build needed).

Usage:
  python3 studio/tools/check_copy.py <30-page-copy.json> [--brief 20-content-brief.json] [--facts facts.json] [--out result.json]

Checks the launch text (fallback lines, not sign-off lines): brand rules, sign-off pair
format, meta lengths, keyword placement, FAQ count, links in the link plan, word count and
copy limits that can be measured. Exits 1 if any blocker fails.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "config.json").read_text())
BANNED = [l.strip().lower() for l in (ROOT / "standards" / "banned-phrases.txt").read_text().splitlines()
          if l.strip() and not l.startswith("#")]
COMPETITORS = [c.lower() for c in CONFIG.get("competitor_names", [])]
SIGNOFF_RE = re.compile(r"\[APPLY AFTER SIGN-OFF:?([^\]]*)\]")
FALLBACK = "[FALLBACK UNTIL THEN]"

results = []


def check(cid, ok, severity, detail=""):
    results.append({"check": cid, "pass": bool(ok), "severity": severity, "detail": detail})


def launch_lines(md):
    """Yield the lines visible at launch. A sign-off block runs from the
    [APPLY AFTER SIGN-OFF] line up to the next [FALLBACK UNTIL THEN] line and is
    dropped; the fallback line and everything after it are kept."""
    held = False
    for line in md.splitlines():
        if SIGNOFF_RE.search(line):
            held = True
            continue
        if FALLBACK in line:
            held = False
            yield line.replace(FALLBACK, "").strip()
            continue
        if not held:
            yield line


def plain(text):
    text = "\n".join(l for l in text.splitlines()
                     if not re.match(r"\s*(\||\[Button|Table caption|CMS|Image|Alt:)", l))
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"(?m)^\s*(#{1,6}|[-*]|\d+\.)\s+", "", text)
    text = re.sub(r"CMS note:.*", "", text)
    return text.replace("**", "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("copy")
    ap.add_argument("--brief")
    ap.add_argument("--facts")
    ap.add_argument("--out")
    a = ap.parse_args()
    env = json.loads(Path(a.copy).read_text())
    c = env["payload"]
    brief = json.loads(Path(a.brief).read_text())["payload"] if a.brief else None

    raw_all = "\n".join([c["meta"]["title"], c["meta"]["description"], c["h1"]]
                        + [s["body_md"] for s in c["sections"]]
                        + [q["q"] + "\n" + q["a"] for q in c["faq"]])
    launch = "\n".join(launch_lines(raw_all))
    visible = plain(launch)
    lower = visible.lower()

    # Brand rules on the launch text
    check("no_em_dashes", "—" not in raw_all, "major", f"{raw_all.count(chr(0x2014))} found")
    check("no_en_dashes", "–" not in raw_all, "minor", f"{raw_all.count(chr(0x2013))} found")
    check("no_exclamation_marks", "!" not in visible, "minor")
    hits = [b for b in BANNED if b in lower]
    check("no_banned_phrases", not hits, "major", str(hits))
    comp = [x for x in COMPETITORS if x in lower]
    check("no_competitor_names", not comp, "blocker", str(comp))
    check("advisor_name_case", "Wedded advisor" not in visible and "Wonderland Luxury Advisor" not in visible, "major")
    bare = re.findall(r"(?<!AUD )\$\s?\d[\d,]*", visible)
    check("no_bare_dollar_prices", not bare, "blocker", str(bare[:5]))

    # Sign-off pairs: every sign-off line is followed by a fallback line
    lines = raw_all.splitlines()
    orphan = []
    for i, l in enumerate(lines):
        if SIGNOFF_RE.search(l):
            nxt = next((m for m in lines[i + 1:] if SIGNOFF_RE.search(m) or FALLBACK in m), "")
            if FALLBACK not in nxt:
                orphan.append(l[:80])
    check("signoff_pairs_complete", not orphan, "blocker", str(orphan[:3]))
    if a.facts:
        facts = {f["id"]: f for f in json.loads(Path(a.facts).read_text())["facts"]}
        held = [f for f in facts.values() if f.get("needs_sign_off_by") and f["status"] != "confirmed"]
        nums = {f["id"]: re.findall(r"\d{1,3}(?:,\d{3})+|\d{4,}(?![.\d])", str(f["value"])) for f in held}
        confirmed_nums = {n for f in facts.values() if f["status"] == "confirmed"
                          for n in re.findall(r"\d{1,3}(?:,\d{3})+|\d{4,}", str(f["value"]))}
        nums = {k: [n for n in v if not re.fullmatch(r"(19|20)\d\d", n) and n not in confirmed_nums]
                for k, v in nums.items()}
        leaks = [(fid, n) for fid, ns in nums.items() for n in ns if n in visible]
        check("no_signoff_figures_at_launch", not leaks, "blocker", str(leaks[:5]))

    # Meta and structure
    t, d = c["meta"]["title"], c["meta"]["description"]
    check("title_length", 30 <= len(t) <= 60, "major", f"{len(t)}")
    check("meta_description_length", 140 <= len(d) <= 160, "minor", f"{len(d)}")
    check("faq_count_10", len(c["faq"]) == 10, "major", f"{len(c['faq'])}")
    body_ids = [x for x in c["sections"] if not re.search(r"form|sticky|b9|hidden", x["id"] + x["body_md"][:40], re.I)]
    words = len(plain("\n".join(launch_lines("\n".join([c["h1"]] + [x["body_md"] for x in body_ids]
                                                       + [q["q"] + "\n" + q["a"] for q in c["faq"]])))).split())
    if brief:
        kw = brief["primary_keyword"].lower()
        first100 = " ".join(plain("\n".join(launch_lines(c["sections"][0]["body_md"]))).split()[:100]).lower()
        check("keyword_in_title", kw in t.lower(), "major")
        check("keyword_in_first_100_words", kw in first100, "major")
        lo, hi = brief["word_count_range"]
        check("word_count_in_range", lo <= words <= hi * 1.15, "minor", f"{words} words, brief {lo}-{hi}")
        hrefs = set(re.findall(r"\]\((/[^)#\s]*)", raw_all))
        missing = [l["url"] for l in brief["link_plan"]["must_link_to"]
                   if l["url"].startswith("/") and l["url"].rstrip("/") not in {h.rstrip("/") for h in hrefs}]
        check("link_plan_implemented", not missing, "major", str(missing))
        ids = {s["id"] for s in c["sections"]}
        gaps = [s["id"] for s in brief["section_outline"] if s["id"] not in ids]
        check("outline_sections_present", not gaps, "blocker", str(gaps))
    no_refs = [s["id"] for s in c["sections"] if not s.get("fact_refs") and "Hidden" not in s["body_md"][:40]]
    check("sections_have_fact_refs", not no_refs, "major", str(no_refs))

    failed = {s: [r["check"] for r in results if not r["pass"] and r["severity"] == s] for s in ("blocker", "major", "minor")}
    report = {"copy": a.copy, "revision": env.get("revision"), "launch_word_count": words, "results": results, "failed": failed}
    if a.out:
        Path(a.out).write_text(json.dumps(report, indent=2, ensure_ascii=False))
    for r in results:
        if not r["pass"]:
            print(f"FAIL [{r['severity']}] {r['check']}: {r['detail']}")
    print(f"blockers={len(failed['blocker'])} majors={len(failed['major'])} minors={len(failed['minor'])} "
          f"passed={sum(r['pass'] for r in results)}/{len(results)} words={words}")
    return 1 if failed["blocker"] else 0


if __name__ == "__main__":
    sys.exit(main())
