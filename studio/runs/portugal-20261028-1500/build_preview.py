#!/usr/bin/env python3
"""Build the Portugal copy preview (studio/runs/portugal-20261028-1500/preview.html)
and schema.jsonld from 30-page-copy.json (latest revision). Launch state: only the
[FALLBACK UNTIL THEN] line of every sign-off pair is rendered."""
import html
import json
import re
import sys
from pathlib import Path

RUN = Path("/home/user/ForWork/studio/runs/portugal-20261028-1500")
CONFIG = json.loads(Path("/home/user/ForWork/studio/config.json").read_text())
COPY = json.loads((RUN / "30-page-copy.json").read_text())
assert COPY["revision"] >= 2, COPY["revision"]
P = COPY["payload"]
S = {s["id"]: s for s in P["sections"]}
DOMAIN = CONFIG["brand"]["domain"]
CANON = DOMAIN + "/destinations/europe/portugal"
ENDPOINT = CONFIG["brand"]["enquiry_endpoint"]
ROUTE = CONFIG["brand"]["enquiry_route"]

APPLY_RE = re.compile(r"^\s*-?\s*\[APPLY AFTER SIGN-OFF: ([^\]]+)\]")
FALLBACK = "[FALLBACK UNTIL THEN]"
TODO_URL = "[URL to confirm]"


def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def fact_ids(s):
    return " ".join(re.findall(r"F\d{3}", s))


def inline(md):
    """Escape, then convert [text](url) and **bold**."""
    out, pos = [], 0
    pat = re.compile(r"\[([^\]]+)\]\((\[URL to confirm\]|[^)\s]+)\)")
    for m in pat.finditer(md):
        out.append(esc(md[pos:m.start()]))
        text, url = m.group(1), m.group(2)
        out.append(link(url, text))
        pos = m.end()
    out.append(esc(md[pos:]))
    s = "".join(out)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return s


def link(url, text, cls=None, entry=None, extra=""):
    c = f' class="{cls}"' if cls else ""
    e = f' data-entry-point="{entry}"' if entry else ""
    if url == TODO_URL:
        slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
        return (f'<a{c} href="#url-to-confirm-{slug}" data-url-status="to-confirm"{e}{extra}>{esc(text)}</a>'
                f'<!-- URL to confirm (dev): {esc(text)} -->')
    if url.startswith("http"):
        return f'<a{c} href="{attr(url)}" target="_blank" rel="noopener"{e}{extra}>{esc(text)}</a>'
    return f'<a{c} href="{attr(url)}"{e}{extra}>{esc(text)}</a>'


def strip_md_links(s):
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s).replace("**", "")



# ---------------------------------------------------------------- structure helpers
# The generator parses copy by section id and markdown structure (headings,
# lists, link lines, sign-off markers), never by exact sentences, so copy
# revisions do not break it. Image slots are assigned by position in a section.
LINK_LINE = re.compile(r"^\s*(\[[^\]]+\]\([^)]*\)\s*)+(\([^)]*\))?\s*$")
BTN_RE = re.compile(r"\[(Button[^:\]]*): ([^\]]+)\]\(([^)]+)\)")
NOTE_RE = re.compile(r"\s*\((?:CMS|Dev)[^)]*\)\s*$")


def blocks(md):
    """Split body_md into blank-line separated blocks of non-empty lines."""
    return [[l.rstrip() for l in b.split("\n") if l.strip()] for b in re.split(r"\n\s*\n", md) if b.strip()]


def is_note(line):
    return bool(re.match(r"^(CMS note|CMS:|Placement:|Tabs \(all panels|Hidden at launch|No price slot)", line))


def is_link_line(line):
    return bool(LINK_LINE.match(line))


def resolve_pairs(lines):
    """Launch state for a list of lines: drop APPLY lines, keep FALLBACK text.
    Returns [(text, signoff_ids_or_None)]."""
    out, ids = [], None
    for l in lines:
        m = APPLY_RE.match(l)
        if m:
            ids = fact_ids(m.group(1))
            continue
        if l.startswith(FALLBACK):
            out.append((l[len(FALLBACK):].strip(), ids))
            ids = None
            continue
        out.append((l, None))
    return out


def section_links(sid):
    return S[sid].get("links", [])


def entry_for(sid, url, anchor):
    for l in section_links(sid):
        if l.get("url") == url and l.get("anchor") == anchor:
            return l.get("entry_point")
    return None


def button_line(sid, line, default_entry=None):
    """Render a '[Button...: label](url) ...' line, entry points from the section's links list."""
    parts = []
    for kind, label, url in BTN_RE.findall(line):
        cls = "btn btn--secondary" if "secondary" in kind else "btn"
        parts.append(link(url, label, cls=cls, entry=entry_for(sid, url, label) or default_entry))
    return '<p class="actions">' + " ".join(parts) + "</p>"


def h3_titles(md):
    """Visible H3 titles in launch state (fallback heading replaces the applied one)."""
    titles = []
    for text, _ in resolve_pairs(md.split("\n")):
        m = re.match(r"^### (.+)$", text)
        if m:
            titles.append(m.group(1))
    return titles


def positional(slots, section, label):
    """Return an after_heading hook that hands out slots in order of the H3s."""
    it = iter(slots)
    used = []
    cards = set(h3_titles(S[section]["body_md"]))

    def hook(text):
        if text not in cards:  # only H3 card titles take a slot
            return None
        try:
            s = next(it)
        except StopIteration:
            WARN.append(f"{section}: more H3 cards than image slots ('{text}' has none)")
            return None
        used.append(text)
        return s(text)
    hook.used = used
    return hook


WARN = []

# ---------------------------------------------------------------- image slots
def slot(file, alt, caption=None, tone=None, hero=False, signoff=None, ratio="r32"):
    t = f' data-tone="{tone}"' if tone else ""
    load = ' data-priority="high" data-fetchpriority="high"' if hero else ' data-loading="lazy"'
    so = f' data-signoff="{signoff}"' if signoff else ""
    assert len(alt) <= 125, (file, len(alt))
    fig = (f'<figure class="slot">'
           f'<div class="ph {ratio}"{t} data-img="{file}"{load} role="img" aria-label="{attr(alt)}"></div>')
    if caption:
        fig += f'<figcaption{so}>{esc(caption)}</figcaption>'
    return fig + "</figure>"


def cap(section, key):
    """Caption text; for a sign-off pair return (fallback, ids)."""
    c = S[section]["captions"][key]
    if c.startswith("[APPLY"):
        ids = fact_ids(APPLY_RE.match(c).group(1))
        fb = c.split(FALLBACK, 1)[1].strip()
        return fb, ids
    return c, None


def capslot(section, key, file, alt, **kw):
    text, ids = cap(section, key)
    return slot(file, alt, text, signoff=ids, **kw)


# ---------------------------------------------------------------- generic renderer
def render(md, hooks=None, wrap_h3=None, heading_ids=None, skip_first_heading=False):
    """Render a section body_md. hooks: dict of callables keyed by event."""
    hooks = hooks or {}
    heading_ids = heading_ids or {}
    out = []
    para, lst, lst_tag, table = [], [], None, []
    pending = {"ids": None, "as_li": False}
    skipping = False
    carry = None  # sign-off ids carried to body lines under a fallback heading
    in_group = False
    first_heading_done = False

    def flush():
        nonlocal para, lst, lst_tag, table
        if para:
            out.append("<p>" + "<br>".join(para) + "</p>")
            para = []
        if lst:
            out.append(f"<{lst_tag}>" + "".join(lst) + f"</{lst_tag}>")
            lst, lst_tag = [], None
        if table:
            out.append(render_table(table))
            table = []

    def open_group():
        nonlocal in_group
        if wrap_h3:
            close_group()
            out.append(f'<div class="{wrap_h3}">')
            in_group = True

    def close_group():
        nonlocal in_group
        if in_group:
            flush()
            out.append("</div>")
            in_group = False

    def trailing_note(line):
        """Split a trailing '(...)' note after a link line."""
        m = re.match(r"^(.*\))\s+\(([^()]*(?:\([^()]*\))?[^()]*)\)\s*$", line)
        if m and "](" in m.group(1):
            return m.group(1), m.group(2)
        return line, None

    def line_link_html(line, note):
        entry = None
        extra = ""
        if note:
            em = re.search(r"entry_point=([\w-]+)", note)
            entry = em.group(1) if em else None
            rm = re.search(r"prefills Region: (.+)$", note)
            if rm:
                extra += f' data-region="{attr(rm.group(1).strip())}" data-offer="{attr(rm.group(1).strip())}"'
                entry = entry or "region-card"
            if "Celebration from the card" in note:
                entry = entry or "celebrations"
        btns = re.findall(r"\[(Button[^:\]]*): ([^\]]+)\]\(([^)]+)\)", line)
        if btns:
            parts = []
            for kind, label, url in btns:
                cls = "btn btn--secondary" if "secondary" in kind else "btn"
                parts.append(link(url, label, cls=cls, entry=entry, extra=extra))
            comment = f"<!-- {esc(note)} -->" if note and not entry else ""
            return '<p class="actions">' + " ".join(parts) + "</p>" + comment
        # text link line with a note
        m = re.match(r"^\[([^\]]+)\]\(([^)]+)\)$", line.strip())
        if m:
            return f'<p class="textlink">{link(m.group(2), m.group(1), entry=entry, extra=extra)}</p>'
        return f"<p>{inline(line)}</p>"

    for raw in md.split("\n"):
        line = raw.rstrip()
        so = None
        if not line.strip():
            flush()
            carry = None
            continue
        if skipping and not line.startswith(FALLBACK):
            continue
        skipping = False
        if carry and not line.startswith(FALLBACK):
            so = carry
        am = APPLY_RE.match(line)
        if am:
            pending["ids"] = fact_ids(am.group(1))
            pending["as_li"] = line.lstrip().startswith("-")
            if pending["as_li"]:
                # keep list open: do not flush
                pass
            else:
                flush() if not para else None
            out.append(f"<!-- Apply after sign-off ({esc(am.group(1))}): replaced by the fallback line below until then -->")
            skipping = True
            continue
        if line.startswith(FALLBACK):
            so = pending["ids"]
            line = line[len(FALLBACK):].strip()
            if pending["as_li"]:
                lst.append(f'<li data-signoff="{so}">{inline(line)}</li>')
                pending = {"ids": None, "as_li": False}
                continue
            pending = {"ids": None, "as_li": False}
            if line.startswith("#"):
                carry = so
        # CMS and production notes become comments
        if re.match(r"^(CMS note|CMS:|Placement:|Tabs \(all panels|Hidden at launch)", line):
            flush()
            if "add-palace-rules" in line and "palace" in hooks:
                close_group()
                out.append(hooks["palace"]())
            out.append(f"<!-- {esc(line)} -->")
            continue
        if line.startswith("(anchor:") or line.startswith("(Tab label:"):
            m = re.search(r"anchor: #([\w-]+)", line)
            tl = re.search(r"Tab label: ([^;.)]+)", line)
            if tl and "costs" in hooks and "add-cost-bands" in line:
                flush()
                close_group()
                out.append(hooks["costs"](tl.group(1).strip()))
                continue
            if not m and tl:
                m = re.match(r"(.*)", re.sub(r"[^a-z0-9]+", "-", tl.group(1).strip().lower()).strip("-"))
            if m:
                # attach id to last heading
                for i in range(len(out) - 1, -1, -1):
                    if re.match(r"<h[2-4]", out[i]):
                        out[i] = re.sub(r"^<(h[2-4])( id=\"[^\"]*\")?", rf'<\1 id="{m.group(1)}"', out[i], count=1)
                        break
            out.append(f"<!-- {esc(line)} -->")
            continue
        if line.startswith("Table caption:"):
            table.append(("caption", line.split(":", 1)[1].strip()))
            continue
        if line.startswith("|"):
            if para or lst:
                flush()
            if not re.match(r"^\|[-| ]+\|$", line):
                table.append([c.strip() for c in line.strip("|").split("|")])
            continue
        hm = re.match(r"^(#{1,4}) (.+)$", line)
        if hm:
            flush()
            level, text = len(hm.group(1)), hm.group(2)
            if skip_first_heading and not first_heading_done:
                first_heading_done = True
                continue
            first_heading_done = True
            if level == 3 and wrap_h3:
                open_group()
            if level == 2:
                close_group()
            hid = heading_ids.get(text)
            ida = f' id="{hid}"' if hid else ""
            soa = f' data-signoff="{so}"' if so else ""
            out.append(f"<h{level}{ida}{soa}>{inline(text)}</h{level}>")
            if "after_heading" in hooks:
                extra = hooks["after_heading"](text)
                if extra:
                    out.append(extra)
            continue
        lm = re.match(r"^(-|\d+\.) (.+)$", line)
        if lm:
            if para:
                flush()
            tag = "ul" if lm.group(1) == "-" else "ol"
            if lst_tag and lst_tag != tag:
                flush()
            lst_tag = tag
            soa = f' data-signoff="{so}"' if so else ""
            lst.append(f"<li{soa}>{inline(lm.group(2))}</li>")
            continue
        if "](" in line and (line.startswith("[") or re.search(r"\)\s+\([^)]*\)\s*$", line)):
            body, note = trailing_note(line)
            if line.startswith("[Button") or note:
                flush()
                out.append(line_link_html(body, note))
                continue
        if "before_para" in hooks:
            extra = hooks["before_para"](line)
            if extra:
                flush()
                close_group()
                out.append(extra)
        if lst:
            flush()
        txt = inline(re.sub(r"\s+\(external, target _blank, rel noopener\)$", "", line))
        para.append(f'<span data-signoff="{so}">{txt}</span>' if so else txt)
    flush()
    close_group()
    return "\n".join(out)


def render_table(rows):
    caption = [r[1] for r in rows if isinstance(r, tuple)]
    rows = [r for r in rows if not isinstance(r, tuple)]
    h = '<div class="table-wrap"><table>'
    if caption:
        h += f"<caption>{esc(caption[0])}</caption>"
    h += "<thead><tr>" + "".join(f'<th scope="col">{esc(c)}</th>' for c in rows[0]) + "</tr></thead><tbody>"
    for r in rows[1:]:
        h += "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>"
    return h + "</tbody></table></div>"


# ---------------------------------------------------------------- sections
def hero():
    s = S["s1-hero"]
    bl = blocks(s["body_md"])
    h1 = next(l[2:] for b in bl for l in b if l.startswith("# "))
    assert h1 == P["h1"], (h1, P["h1"])
    rest = [b for b in bl if not b[0].startswith("# ")]
    btn_i = next(i for i, b in enumerate(rest) if BTN_RE.search(b[0]))
    quick = [l for b in rest[:btn_i] for l in b]
    html_parts = [f'<p class="lede">{"<br>".join(inline(l) for l in quick)}</p>',
                  button_line("s1-hero", rest[btn_i][0])]
    after = rest[btn_i + 1:]
    first_prose = True
    for b in after:
        line = " ".join(b)
        if is_link_line(line):
            m = re.match(r"^\[([^\]]+)\]\(([^)]+)\)", line)
            html_parts.append(f'<p class="textlink">{link(m.group(2), m.group(1))}</p>')
        elif is_note(line):
            html_parts.append(f"<!-- {esc(line)} -->")
        else:
            cls = "brand-line" if first_prose else "small"
            first_prose = False
            html_parts.append(f'<p class="{cls}">{inline(line)}</p>')
    body = "\n      ".join(html_parts)
    return f"""
<section class="hero" id="top" aria-labelledby="h1">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <h1 id="h1">{esc(h1)}</h1>
      {body}
    </div>
    {capslot('s1-hero', 'hero', 'pena-palace-sintra-hills-wedding-in-portugal.jpg',
             'Pena Palace on its wooded hilltop above Sintra, a palace setting for a wedding in Portugal',
             hero=True, ratio='r45')}
  </div>
</section>"""


B9_NAMES = ["season", "guests", "celebration"]


def b9():
    sid = "b9-qualifier"
    fields, helper, notes, btn = [], [], [], ""
    for b in blocks(S[sid]["body_md"]):
        if len(b) > 1 and all(l.startswith("- ") for l in b[1:]):  # question + options
            name = B9_NAMES[len(fields)] if len(fields) < len(B9_NAMES) else f"q{len(fields)}"
            o = "".join(f"<option>{esc(x[2:].strip())}</option>" for x in b[1:])
            fields.append(f'<div class="field"><label for="b9-{name}">{esc(b[0])}</label>'
                          f'<select id="b9-{name}" data-b9="{name}"><option value="">Choose</option>{o}</select></div>')
        elif BTN_RE.search(b[0]):
            kind, label, url = BTN_RE.search(b[0]).groups()
            btn = f'<a class="btn" href="{attr(url)}" id="b9-go" data-entry-point="b9">{esc(label)}</a>'
        elif is_note(b[0]):
            notes.append(" ".join(b))
        else:
            helper.append(NOTE_RE.sub("", " ".join(b)))
    assert len(fields) == 3, f"B9 expected 3 question groups, found {len(fields)}"
    help_html = "".join(f'<p class="small helper">{inline(h)}</p>' for h in helper)
    return f"""
<section class="b9" aria-label="Your plans">
  <div class="wrap">
    {''.join(f'<!-- {esc(n)} -->' for n in notes)}
    <div class="b9-bar" role="group" aria-label="Your plans">
      {''.join(fields)}
      <div class="field field--btn">{btn}</div>
    </div>
    {help_html}
  </div>
</section>"""


def b8():
    lines = resolve_pairs([l for l in S["b8-proof-strip"]["body_md"].split("\n") if l.strip()])
    ps = "".join(f'<p data-signoff="{i}">{inline(t)}</p>' if i else f"<p>{inline(t)}</p>" for t, i in lines)
    return f"""
<section class="b8" aria-label="How this page is checked">
  <!-- Apply after sign-off lines replaced by their fallback until signed off -->
  <div class="wrap">{ps}</div>
</section>"""


# Slots by position: (caption key or None, file, alt). Captions are looked up by key.
B16_SLOTS = [
    ("pena", "pena-palace-above-trees-sintra.jpg", "Pena Palace rising above the wooded park in the Sintra hills, wrapped in light mist"),
    ("monserrate", "monserrate-palace-arches-lawns-sintra.jpg", "Monserrate Palace arches above the lawns of its Romantic park in Sintra"),
    ("queluz", "queluz-national-palace-facade-dusk.jpg", "Facade of the National Palace of Queluz near Lisbon at dusk"),
    ("douro", "douro-valley-terraced-vineyards.jpg", "Steep terraced vineyards in the Alto Douro Wine Region"),
    ("ponta_da_piedade", "algarve-coast-clifftops-atlantic.jpg", "Golden clifftops above the Atlantic on the Algarve coast"),
]
B16_STRIP = [
    ("azulejo", "azulejo-tile-wall-detail-portugal.jpg", "Close-up of blue and white azulejo tiles on a Portuguese wall"),
    ("fado", "fado-guitar-portugal.jpg", "A Portuguese guitar used to play fado"),
    ("quinta_staircase", "quinta-stone-staircase-couple-portugal.jpg", "Couple on the stone staircase of a Portuguese quinta before dinner"),
]


def slot_fn(section, spec, **kw):
    key, f, alt = spec
    if key and key in S[section].get("captions", {}):
        return lambda _t: capslot(section, key, f, alt, **kw)
    if key:
        WARN.append(f"{section}: caption key '{key}' missing in copy; slot rendered without caption")
    return lambda _t: slot(f, alt, **kw)


def b16():
    sid = "b16-spotlight"
    hook = positional([slot_fn(sid, s) for s in B16_SLOTS], sid, "cards")
    strip_done = []

    def before(line):
        # the 3-image detail strip goes before the first prose paragraph after the cards
        if not strip_done and "](/" in line and not line.startswith("[Button"):
            strip_done.append(1)
            return '<div class="strip3">' + "".join(slot_fn(sid, s)(None) for s in B16_STRIP) + "</div>"

    body = render(S[sid]["body_md"], hooks={"after_heading": hook, "before_para": before}, wrap_h3="card")
    if not strip_done:
        WARN.append(f"{sid}: no body link line found for the detail strip; strip appended at the end")
        body += '<div class="strip3">' + "".join(slot_fn(sid, s)(None) for s in B16_STRIP) + "</div>"
    return f'<section class="section section--linen" id="spotlight">\n<div class="wrap">\n{body}\n</div>\n</section>'


S2_SLOTS = [
    ("lisbon_sintra_cascais", "lisbon-sintra-cascais-pena-palace-forest.jpg", "Pena Palace above the forest in Sintra, in the Lisbon, Sintra and Cascais region"),
    ("algarve", "algarve-clifftops-beach-sea-stacks.jpg", "Sea stacks and a sandy beach below the Algarve clifftops"),
    ("porto_douro", "porto-douro-terraced-vineyards-river.jpg", "Terraced vineyards above the Douro river in the Alto Douro Wine Region"),
    ("comporta_alentejo", "comporta-alentejo-coast-dunes-dusk.jpg", "Dunes on the Alentejo coast at Comporta at dusk"),
    ("madeira", "madeira-atlantic-cliffs-green-hills.jpg", "Green cliffs above the Atlantic on the island of Madeira"),
]


def palace():
    body = render(S["add-palace-rules"]["body_md"])
    return f'<aside class="callout" id="palace-rules" aria-labelledby="palace-h">\n{body.replace("<h3>", "<h3 id=\"palace-h\">", 1)}\n</aside>'


def region_names():
    return h3_titles(S["s2-regions"]["body_md"])


def s2():
    sid = "s2-regions"
    hook = positional([slot_fn(sid, s, tone="warm") for s in S2_SLOTS], sid, "regions")
    body = render(S[sid]["body_md"], hooks={"after_heading": hook, "palace": palace}, wrap_h3="card region")
    body = body.replace("<h2>", '<h2 id="regions-h">', 1)
    return (f'<section class="section" id="regions" aria-labelledby="regions-h">\n<div class="wrap">\n{body}\n'
            f'<!-- add-beach-line: entered once in the Algarve card above (see its placement note) -->\n</div>\n</section>')


S3_SLOTS = [
    (None, "registry-table-signing-portugal.jpg", "Couple signing the marriage register at a civil registry table in Portugal"),
    (None, "monserrate-gardens-sintra.jpg", "Gardens of the Park and Palace of Monserrate in Sintra"),
    (None, "douro-slate-terraces-vineyards.jpg", "Slate terraces lined with vines in the Douro Valley"),
    (None, "algarve-beach-low-sun.jpg", "Algarve beach and clifftops in low evening sun"),
    (None, "lisbon-arrival-couple-city-street.jpg", "Couple arriving in Lisbon, walking a city street with their luggage"),
]


def s3():
    sid = "s3-reasons"
    hook = positional([slot_fn(sid, s) for s in S3_SLOTS], sid, "reasons")
    body = render(S[sid]["body_md"], hooks={"after_heading": hook}, wrap_h3="card")
    return f'<section class="section section--linen" id="why-portugal">\n<div class="wrap">\n{body}\n</div>\n</section>'


S4_SLOTS = [
    ("s4_quinta", "quinta-courtyard-dinner-table-portugal.jpg", "Quinta courtyard laid with a long table for a wedding dinner"),
    ("s4_pousada", "pousada-historic-castle-cloister.jpg", "Stone cloister of a pousada in a historic Portuguese castle"),
    ("s4_clifftop", "algarve-clifftop-ceremony-aisle.jpg", "Ceremony aisle set on an Algarve clifftop above the Atlantic"),
    ("s4_vineyard", "douro-wine-quinta-vineyard-terrace.jpg", "Vineyard terrace at a wine quinta in the Douro Valley"),
    ("s4_city", "lisbon-civil-ceremony-salon.jpg", "Civil wedding ceremony in an ornate salon in Lisbon"),
    ("s4_church", "portugal-church-doorway-ceremony.jpg", "Couple at the doorway of a church in Portugal after a Catholic ceremony"),
]


def s4():
    sid = "s4-settings"
    head, cards, other = [], [], []
    slots = iter(S4_SLOTS)
    for b in blocks(S[sid]["body_md"]):
        line = " ".join(b)
        if line.startswith("**"):  # a setting card: bold lead-in paragraph
            spec = next(slots, None)
            if spec is None:
                WARN.append(f"{sid}: more settings than image slots")
                cards.append(f'<div class="card"><p>{inline(line)}</p></div>')
            else:
                cards.append(f'<div class="card">{slot_fn(sid, spec)(None)}<p>{inline(line)}</p></div>')
        elif not cards:
            head.append("\n".join(b))
        else:
            other.append("\n".join(b))
    vc = render(S["add-venue-charges"]["body_md"])
    return f"""
<section class="section" id="settings">
<div class="wrap">
{render(chr(10).join(x + chr(10) for x in head))}
<div class="grid3">
{chr(10).join(cards)}
</div>
{render(chr(10).join(other)) if other else ""}
<aside class="callout" id="venue-charges-box">
{vc}
</aside>
</div>
</section>"""


def costs_panel(tab_label="Costs"):
    tid = re.sub(r"[^a-z0-9]+", "-", tab_label.lower()).strip("-")
    body = render(S["add-cost-bands"]["body_md"])
    return f'<div class="tab-panel" id="{tid}">\n<!-- Tab label: {esc(tab_label)} -->\n{body}\n</div>'


def s5():
    sid = "s5-plan"
    md = S[sid]["body_md"]
    body = render(md, hooks={"costs": costs_panel}, wrap_h3="tab-panel")
    # move each panel heading id onto its panel wrapper
    body = re.sub(r'<div class="tab-panel">\n(<!--[^\n]*-->\n)?<h3 id="([\w-]+)">',
                  lambda m: f'<div class="tab-panel" id="{m.group(2)}">\n{m.group(1) or ""}<h3>', body)
    tm = re.search(r"^Tabs \([^)]*\): (.+)$", md, re.M)
    labels = [t.strip() for t in tm.group(1).split("|")] if tm else []
    ids = re.findall(r'<div class="tab-panel" id="([\w-]+)"', body)
    nav = []
    for lab in labels:
        tid = re.sub(r"[^a-z0-9]+", "-", lab.lower()).strip("-")
        if tid not in ids:
            WARN.append(f"{sid}: tab '{lab}' has no panel with id #{tid}")
        nav.append(f'<a href="#{tid}">{esc(lab)}</a>')
    tabs = '<nav class="tabs" aria-label="Plan your wedding">' + "".join(nav) + "</nav>"
    # nav goes right before the first panel
    body = body.replace('<div class="tab-panel"', tabs + '\n<div class="tab-panel"', 1)
    return f'<section class="section section--linen" id="plan">\n<div class="wrap narrow">\n{body}\n</div>\n</section>'


def s6():
    body = render(S["s6-weekend"]["body_md"])
    return (f'<section class="section" id="weekend">\n<div class="wrap split">\n<div>{body}</div>\n'
            + slot_fn("s6-weekend", ("s6", "quinta-long-dinner-table-portuguese-wine.jpg",
                      "Long dinner table with Portuguese wine at a quinta after the ceremony"), tone="dusk")(None)
            + "\n</div>\n</section>")


def s7():
    body = render(S["s7-guests"]["body_md"])
    return (f'<section class="section section--sage" id="guests">\n<div class="wrap split">\n<div>{body}</div>\n'
            + slot_fn("s7-guests", ("s7", "quinta-terrace-guests-morning-after.jpg",
                      "Wedding guests at breakfast on a quinta terrace the morning after"))(None)
            + "\n</div>\n</section>")


S9_SLOTS = [
    ("honeymoon", "madeira-funchal-south-coast.jpg", "Funchal on the south coast of Madeira, seen from above the bay"),
    ("anniversary", "douro-anniversary-wine-tasting-terraces.jpg", "Couple at a wine tasting above the Douro Valley terraces"),
    ("proposal", "sintra-pena-park-proposal.jpg", "Proposal in the wooded park below Pena Palace, Sintra"),
    ("vow_renewal", "algarve-clifftop-vow-renewal.jpg", "Couple renewing their vows on an Algarve clifftop above the Atlantic"),
    ("birthday", "douro-quinta-birthday-lunch.jpg", "Family birthday lunch at a long table at a Douro wine quinta"),
]


def s9():
    sid = "s9-celebrations"
    cards, head, tail = [], [], []
    slots = iter(S9_SLOTS)
    for b in blocks(S[sid]["body_md"]):
        m = re.match(r"^\*\*(.+?)\*\*$", b[0])
        if m and len(b) > 1:  # styled label + body line(s)
            spec = next(slots, None)
            img = slot_fn(sid, spec, tone="warm")(None) if spec else ""
            if spec is None:
                WARN.append(f"{sid}: more cards than image slots")
            cards.append(f'<div class="card">{img}<p class="label">{inline(m.group(1))}</p>'
                         f'<p>{"<br>".join(inline(l) for l in b[1:])}</p></div>')
        elif not cards:
            head.append("\n".join(b))
        else:
            tail.append("\n".join(b))
    return (f'<section class="section section--linen" id="celebrations">\n<div class="wrap">\n{render(chr(10).join(head))}\n'
            f'<div class="grid3">{"".join(cards)}</div>\n{render(chr(10) + chr(10).join(tail))}\n</div>\n</section>')


def s10():
    body = render(S["s10-advisor"]["body_md"])
    return (f'<section class="section" id="advisor-section">\n<div class="wrap split">\n<div>{body}</div>\n'
            + slot_fn("s10-advisor", ("advisor_band", "wedded-advisor-planning-with-couple.jpg",
                      "Wedded Advisor planning with a couple at a table, laptop and notes open"))(None)
            + "\n</div>\n</section>")


def form_spec():
    """Parse the s10-form body by its bold-labelled blocks."""
    md = S["s10-form"]["body_md"]
    spec = {"intro": [], "fields": [], "button": "", "consent": "", "errors": [], "success": {}, "hidden": []}
    heading = None
    for b in blocks(md):
        first = b[0]
        if first.startswith("### "):
            heading = first[4:]
            continue
        if first.startswith("(anchor:"):
            continue
        lab = re.match(r"^\*\*([^*]+?):?\*\*:?\s*(.*)$", first)
        if not lab:
            if not spec["fields"]:
                spec["intro"].append(" ".join(b))
            continue
        key, rest = lab.group(1).lower(), lab.group(2)
        items = [l[2:].strip() for l in b[1:] if l.startswith("- ")]
        if key.startswith("visible fields"):
            for it in items:
                m = re.match(r"^(.+?)(?:\s*\((required|optional)\))?(?::\s*(.+)|\? Placeholder:\s*(.+))?$", it)
                label, flag, opts, ph = m.group(1).strip(), m.group(2), m.group(3), m.group(4)
                if ph is not None:
                    label += "?"
                spec["fields"].append({"label": label, "flag": flag,
                                       "options": [o.strip() for o in opts.split("|")] if opts else None,
                                       "placeholder": ph})
        elif key.startswith("button"):
            spec["button"] = rest.strip()
        elif key.startswith("consent"):
            spec["consent"] = re.sub(r"\s*\(Dev:[^)]*\)\s*$", "", rest).strip()
        elif key.startswith("error"):
            spec["errors"] = [tuple(x.split(": ", 1)) for x in items]
        elif key.startswith("success"):
            spec["success"] = dict(x.split(": ", 1) for x in items)
        elif key.startswith("hidden"):
            spec["hidden"] = items
    spec["heading"] = heading
    return spec


FIELD_NAMES = {"first name": ("first_name", "text", "given-name"), "last name": ("last_name", "text", "family-name"),
               "email": ("email", "email", "email"), "phone": ("phone", "tel", "tel"),
               "region": ("region", None, None), "season": ("season", None, None), "year": ("year", None, None),
               "how many guests?": ("guests", None, None), "what are you celebrating?": ("celebration", None, None),
               "ceremony type": ("ceremony_type", None, None), "anything we should know?": ("message", None, None)}


def form():
    sp = form_spec()

    def err_for(label, kind):
        for k, v in sp["errors"]:
            if k.lower().startswith(label.lower()) and kind in k.lower():
                return v
        return None

    rows = []
    for f in sp["fields"]:
        lk = f["label"].lower()
        name, typ, ac = FIELD_NAMES.get(lk, (re.sub(r"[^a-z0-9]+", "_", lk).strip("_"), "text", None))
        fid = "f-" + name.replace("_", "-")
        opt = ' <span class="opt">(optional)</span>' if f["flag"] == "optional" else ""
        req = " required" if f["flag"] == "required" else ""
        msgs = ""
        for kind, attrname in (("empty", "data-msg-required"), ("not valid", "data-msg-invalid")):
            e = err_for(f["label"], kind)
            if e:
                msgs += f' {attrname}="{attr(e)}"'
        lab = f'<label for="{fid}">{esc(f["label"])}{opt}</label>'
        if f["options"]:
            o = "".join(f"<option>{esc(x)}</option>" for x in f["options"])
            ctl = f'<select id="{fid}" name="{name}"{req}><option value="">Choose</option>{o}</select>'
        elif f["placeholder"] is not None:
            ctl = f'<textarea id="{fid}" name="{name}" rows="4" placeholder="{attr(f["placeholder"])}"></textarea>'
        else:
            acs = f' autocomplete="{ac}"' if ac else ""
            ctl = f'<input id="{fid}" name="{name}" type="{typ or "text"}"{acs}{req}{msgs}>'
        rows.append(f'<div class="field">{lab}{ctl}</div>')
    # hidden fields from the copy's list
    hidden = []
    for h in sp["hidden"]:
        names, _, val = h.partition(" = ")
        for n in [x.strip() for x in names.split(",")]:
            fixed = val.strip() if re.fullmatch(r"[\w/.-]+", val.strip()) else ""
            hidden.append(f'<input type="hidden" name="{attr(n)}" value="{attr(fixed)}">')
    hidden_note = "; ".join(sp["hidden"])
    assert any('name="route_to" value="' + ROUTE + '"' in h for h in hidden), "route_to hidden field missing"
    submit_err = err_for("Submit failed", "") or ""
    succ = sp["success"]
    return f"""
<section class="section section--sage" id="enquire" aria-labelledby="enquire-h">
<div class="wrap narrow">
<h3 id="enquire-h">{esc(sp['heading'])}</h3>
{''.join(f'<p>{inline(i)}</p>' for i in sp['intro'])}
<form class="enquiry" action="{ENDPOINT}" method="post" novalidate>
  <!-- Hidden fields (from the copy's form section): {esc(hidden_note)} -->
  {''.join(hidden)}
  {chr(10).join(rows)}
  <p class="form-error" role="alert" hidden data-msg-submit="{attr(submit_err)}"></p>
  <button class="btn btn--full" type="submit">{esc(sp['button'])}</button>
  <p class="small consent">{inline(sp['consent'])}</p>
</form>
<template id="enquiry-success"><div class="success" role="status"><h4>{esc(succ.get('Heading', ''))}</h4><p>{esc(succ.get('Body', ''))}</p></div></template>
</div>
</section>"""


def faq_items():
    items = []
    for i, f in enumerate(P["faq"], 1):
        vis, schema_txt = [], []
        pending = None
        for line in f["a"].split("\n"):
            am = APPLY_RE.match(line)
            if am:
                pending = fact_ids(am.group(1))
                continue
            if line.startswith(FALLBACK):
                t = line[len(FALLBACK):].strip()
                vis.append(f'<span data-signoff="{pending}">{inline(t)}</span>')
                schema_txt.append(strip_md_links(t))
                pending = None
                continue
            vis.append(inline(line))
            schema_txt.append(strip_md_links(line))
        items.append((f"{i}. {f['q']}", f["q"], " ".join(vis), " ".join(schema_txt)))
    return items


def faq():
    items = faq_items()
    body = S["s11-faq"]["body_md"]
    for f in P["faq"]:
        if not (f["q"] in body and f["a"] in body):
            WARN.append(f"s11-faq body and payload.faq differ for '{f['q']}' (payload.faq rendered)")
    h2 = next((l[3:] for l in body.split("\n") if l.startswith("## ")), S["s11-faq"]["heading"])
    qa = "\n".join(f'<div class="qa"><h3>{esc(h)}</h3><p>{a}</p></div>' for h, _, a, _ in items)
    notes = "".join(f"<!-- {esc(l)} -->" for l in body.split("\n") if is_note(l))
    return f"""
<section class="section" id="faq" aria-labelledby="faq-h">
<div class="wrap narrow">
<h2 id="faq-h">{esc(h2)}</h2>
<div class="faq">
{qa}
</div>
{notes}
</div>
</section>"""


def closing():
    sid = "closing-cta"
    prose, btns = [], []
    for b in blocks(S[sid]["body_md"]):
        line = " ".join(b)
        if BTN_RE.search(line):
            btns.append(button_line(sid, line))
        elif not is_note(line):
            prose.append(f"<p>{inline(line)}</p>")
    return f"""
<section class="closing" aria-label="Closing call to action">
<div class="wrap narrow">{''.join(prose)}{''.join(btns)}</div>
</section>"""


def s12():
    sid = "s12-articles"
    out, cards = [], []
    for b in blocks(S[sid]["body_md"]):
        m = re.match(r"^\[([^\]]+)\]\(([^)]+)\)$", b[0])
        if m and len(b) == 2 and not b[1].startswith("- "):  # article card: link line + description
            cards.append(f'<div class="card article">{link(m.group(2), m.group(1), cls="card-title")}<p class="small">{inline(b[1])}</p></div>')
            continue
        if cards:
            out.append('<div class="grid2">' + "".join(cards) + "</div>")
            cards = []
        r = render("\n".join(b))
        out.append(re.sub(r"<p><strong>([^<]+)</strong></p>", r'<p class="label">\1</p>', r))
    if cards:
        out.append('<div class="grid2">' + "".join(cards) + "</div>")
    return f'<section class="section section--linen" id="articles">\n<div class="wrap">\n' + "\n".join(out) + "\n</div>\n</section>"


def s13():
    body = render(S["s13-europe"]["body_md"])
    body = body.replace("<ul>", '<ul class="chips">', 1)
    return f'<section class="section" id="europe">\n<div class="wrap">\n{body}\n</div>\n</section>'


def sticky():
    sid = "sticky-bar"
    label, btn, notes = "", "", []
    for b in blocks(S[sid]["body_md"]):
        line = " ".join(b)
        m = re.match(r"^Label:\s*(.+)$", line)
        if m:
            label = m.group(1)
        elif BTN_RE.search(line):
            kind, lab, url = BTN_RE.search(line).groups()
            btn = link(url, lab, cls="btn", entry=entry_for(sid, url, lab) or "sticky")
        else:
            notes.append(line)
    return f"""
<div class="sticky-cta" id="sticky-cta" aria-label="Enquire">
  <!-- Mobile sticky bar. {esc(' '.join(notes))} -->
  <span class="sticky-label">{esc(label)}</span>
  {btn}
</div>"""


# ---------------------------------------------------------------- schema
def brand_sentence():
    """The hero paragraph that follows the passport text link (F088 brand line)."""
    bl = blocks(S["s1-hero"]["body_md"])
    for i, b in enumerate(bl):
        if is_link_line(" ".join(b)) and not BTN_RE.search(b[0]) and i + 1 < len(bl):
            return " ".join(bl[i + 1])
    return None


def schema():
    org = {"@type": "Organization", "@id": DOMAIN + "/#organization", "name": CONFIG["brand"]["name"],
           "url": DOMAIN + "/"}
    dest = {"@type": "TouristDestination", "@id": CANON + "#destination", "name": "Portugal",
            "url": CANON,
            "description": P["meta"]["description"],
            "containedInPlace": {"@type": "Continent", "name": "Europe"},
            "touristType": "Couples planning a destination wedding"}
    regions = region_names()
    s2h = next(l[3:] for l in S["s2-regions"]["body_md"].split("\n") if l.startswith("## "))
    il = {"@type": "ItemList", "@id": CANON + "#regions", "name": s2h,
          "numberOfItems": len(regions),
          "itemListElement": [{"@type": "ListItem", "position": i, "name": r} for i, r in enumerate(regions, 1)]}
    svc = {"@type": "Service", "@id": CANON + "#concierge", "name": CONFIG["brand"]["concierge_name"],
           "serviceType": "Destination wedding planning",
           "provider": {"@id": org["@id"]},
           "areaServed": {"@type": "Country", "name": "Portugal"},
           "url": DOMAIN + "/wonderland-concierge"}
    bs = brand_sentence()
    if bs:
        svc["description"] = strip_md_links(bs)
    bc = {"@type": "BreadcrumbList", "@id": CANON + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
        {"@type": "ListItem", "position": 2, "name": "Destinations", "item": DOMAIN + "/destinations"},
        {"@type": "ListItem", "position": 3, "name": "Europe", "item": DOMAIN + "/destinations/europe"},
        {"@type": "ListItem", "position": 4, "name": "Portugal", "item": CANON}]}
    faqp = {"@type": "FAQPage", "@id": CANON + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for _, q, _, a in faq_items()]}
    return {"@context": "https://schema.org", "@graph": [dest, il, svc, bc, faqp, org]}


# ---------------------------------------------------------------- page
CSS = """
:root{--ink:#22201c;--ink-soft:#55504a;--line:#ddd6cb;--bg:#fbf8f3;--white:#fff;--linen:#f3eee6;--sage:#e9ece4;--accent:#7a5c3e;--accent-ink:#fff;--ph:#d9d3c8;--ph-warm:#dccbb4;--ph-dusk:#c9c3cf}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-text-size-adjust:100%}
h1,h2,h3,h4{line-height:1.25;margin:1.4em 0 .5em;font-weight:650}
h1{font-size:clamp(1.8rem,5.5vw,2.8rem);margin-top:.2em}
h2{font-size:clamp(1.45rem,4vw,2rem)}
h3{font-size:1.15rem}
h4{font-size:1.02rem}
p{margin:.6em 0}
a{color:var(--accent)}
.wrap{max-width:1160px;margin:0 auto;padding:0 16px}
.narrow{max-width:820px}
header.site{background:var(--white);border-bottom:1px solid var(--line)}
header.site .wrap{display:flex;justify-content:space-between;align-items:center;min-height:56px;gap:12px}
.brand{font-weight:700;letter-spacing:.02em;text-decoration:none;color:var(--ink)}
.crumbs{font-size:.85rem;color:var(--ink-soft);padding:10px 16px}
.crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:4px}
.crumbs li+li::before{content:"/";margin-right:4px;color:var(--line)}
.section{padding:40px 0}
.section--linen{background:var(--linen)}
.section--sage{background:var(--sage)}
.hero{padding:16px 0 32px}
.hero-grid{display:grid;gap:20px}
.lede{font-size:1.08rem}
.brand-line{font-weight:600}
.small{font-size:.9rem;color:var(--ink-soft)}
.actions{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0}
.btn{display:inline-block;background:var(--accent);color:var(--accent-ink);text-decoration:none;padding:12px 18px;border-radius:6px;font-weight:600;border:2px solid var(--accent);font-size:1rem;cursor:pointer;text-align:center}
.btn--secondary{background:transparent;color:var(--accent)}
.btn--full{width:100%}
.textlink a{font-weight:600}
.slot{margin:0 0 12px}
.ph{background:var(--ph);border-radius:6px;width:100%;position:relative;overflow:hidden}
.ph::after{content:attr(data-img);position:absolute;left:8px;bottom:6px;font-size:.7rem;color:#6b645a;max-width:calc(100% - 16px);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.ph[data-tone=warm]{background:var(--ph-warm)}
.ph[data-tone=dusk]{background:var(--ph-dusk)}
.r32{aspect-ratio:3/2}.r45{aspect-ratio:4/5}
figcaption{font-size:.85rem;color:var(--ink-soft);margin-top:6px}
.b9{background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:16px 0}
.b9-bar{display:grid;gap:12px}
.b8{background:var(--ink);color:#f3eee6;padding:12px 0;font-size:.95rem}
.b8 p{margin:0}
.field{display:flex;flex-direction:column;gap:4px;margin-bottom:12px}
.field label{font-weight:600;font-size:.95rem}
.opt{font-weight:400;color:var(--ink-soft)}
input,select,textarea{font:inherit;padding:11px 12px;border:1px solid #b9b0a3;border-radius:6px;background:var(--white);color:var(--ink);width:100%}
.field--btn{justify-content:flex-end}
.card{background:var(--white);border:1px solid var(--line);border-radius:8px;padding:14px;margin:0 0 16px}
.card h3{margin-top:.2em}
.card .slot{margin:4px 0 12px}
.card>.slot:first-child{margin:-14px -14px 12px}
.card>.slot:first-child .ph{border-radius:8px 8px 0 0}
.card>.slot:first-child figcaption{padding:0 14px}
.region ul{padding-left:18px}
.callout{background:var(--white);border-left:4px solid var(--accent);padding:4px 16px 12px;margin:20px 0;border-radius:0 8px 8px 0}
.strip3{display:grid;gap:12px;margin:16px 0}
.grid3,.grid2{display:grid;gap:16px}
.split{display:grid;gap:20px;align-items:start}
.tabs{display:flex;gap:8px;overflow-x:auto;padding:8px 0 12px;margin:8px 0 8px;-webkit-overflow-scrolling:touch}
.tabs a{flex:none;border:1px solid var(--line);background:var(--white);border-radius:999px;padding:6px 14px;text-decoration:none;color:var(--ink);font-size:.9rem}
.tab-panel{background:var(--white);border:1px solid var(--line);border-radius:8px;padding:4px 16px 12px;margin:16px 0;scroll-margin-top:12px}
.table-wrap{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{border-bottom:1px solid var(--line);padding:8px;text-align:left}
.qa{border-bottom:1px solid var(--line);padding:4px 0 10px}
.qa h3{margin-top:1em}
.label{font-weight:700;margin-bottom:.2em}
.card .label{margin-top:0}
.card-title{font-weight:700;font-size:1.05rem}
.chips{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:8px}
.chips a{display:inline-block;border:1px solid var(--line);background:var(--white);border-radius:999px;padding:8px 14px;text-decoration:none}
.closing{background:var(--ink);color:#f3eee6;padding:32px 0;text-align:center}
.closing .actions{justify-content:center}
.closing .btn{background:#f3eee6;color:var(--ink);border-color:#f3eee6}
.enquiry{background:var(--white);border:1px solid var(--line);border-radius:8px;padding:16px}
.row2{display:grid;gap:0 12px}
.consent{margin-top:10px}
footer.site{padding:24px 0 96px;font-size:.85rem;color:var(--ink-soft);border-top:1px solid var(--line)}
.sticky-cta{position:fixed;left:0;right:0;bottom:0;z-index:60;background:var(--white);border-top:1px solid var(--line);padding:10px 16px;display:flex;gap:12px;align-items:center;justify-content:space-between;box-shadow:0 -2px 10px rgba(0,0,0,.06);transition:transform .2s}
.sticky-cta .btn{padding:10px 14px;font-size:.95rem}
.sticky-label{font-weight:600;font-size:.9rem;line-height:1.3}
body{padding-bottom:72px}
.sticky-cta.is-hidden{transform:translateY(110%)}
@media (min-width:700px){
  .b9-bar{grid-template-columns:repeat(3,1fr) auto;align-items:end}
  .b9-bar .field{margin:0}
  .grid2,.row2{grid-template-columns:1fr 1fr}
  .grid3,.strip3{grid-template-columns:repeat(3,1fr)}
  #spotlight .wrap,#regions .wrap,#why-portugal .wrap{display:grid;grid-template-columns:repeat(2,1fr);gap:0 16px}
  #spotlight .wrap>*:not(.card),#regions .wrap>*:not(.card),#why-portugal .wrap>*:not(.card){grid-column:1/-1}
}
@media (min-width:1000px){
  .hero-grid{grid-template-columns:1.1fr .9fr;align-items:center}
  .split{grid-template-columns:1.2fr .8fr}
  #spotlight .wrap,#regions .wrap,#why-portugal .wrap{grid-template-columns:repeat(3,1fr)}
  .sticky-cta{display:none}
  body{padding-bottom:0}
}
"""

JS = r"""
(function(){
  var form=document.querySelector('form.enquiry');if(!form)return;
  function setVal(name,v){var el=form.elements[name];if(!el||!v)return;
    for(var i=0;i<el.options.length;i++){if(el.options[i].text===v){el.selectedIndex=i;return;}}}
  var q=new URLSearchParams(location.search);
  ['utm_source','utm_medium','utm_campaign','utm_term','utm_content'].forEach(function(k){if(q.get(k))form.elements[k].value=q.get(k);});
  document.querySelectorAll('a[href="#enquire"][data-entry-point]').forEach(function(a){
    a.addEventListener('click',function(){
      form.elements.entry_point.value=a.getAttribute('data-entry-point');
      form.elements.offer.value=a.getAttribute('data-offer')||'';
      if(a.getAttribute('data-region'))setVal('region',a.getAttribute('data-region'));
      if(a.id==='b9-go'){
        setVal('season',document.getElementById('b9-season').selectedOptions[0].text);
        setVal('guests',document.getElementById('b9-guests').selectedOptions[0].text);
        setVal('celebration',document.getElementById('b9-celebration').selectedOptions[0].text);
      }
    });
  });
  var bar=document.getElementById('sticky-cta');
  if(bar&&'IntersectionObserver' in window){
    new IntersectionObserver(function(es){es.forEach(function(e){bar.classList.toggle('is-hidden',e.isIntersecting);});},{threshold:0.05}).observe(document.getElementById('enquire'));
  }
})();
"""


def page():
    m = P["meta"]
    ld = schema()
    body = "\n".join([
        hero(), b9(), b8(), b16(), s2(), s3(), s4(), s5(), s6(), s7(),
        "<!-- s8-real-weddings: hidden at launch (F018: 2 of the 3 Portugal real weddings needed for B6). "
        "Show the Europe real weddings strip here only if the CMS has one; otherwise the slot stays empty. -->",
        s9(), s10(), form(), faq(), closing(), s12(), s13(),
    ])
    doc = f"""<!doctype html>
<html lang="{CONFIG['brand']['locale']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- PREVIEW ONLY (Page Studio run portugal-20261028-1500, Stage 5, copy scope, copy revision {COPY['revision']}). Not the deliverable; launch state with fallback lines for every sign-off pair. -->
<title>{esc(m['title'])}</title>
<meta name="description" content="{attr(m['description'])}">
<meta name="robots" content="index, follow">
<!-- D2: live, indexed page; changes that depend on unsigned facts are held, so no noindex. -->
<link rel="canonical" href="{CANON}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{CONFIG['brand']['name']}">
<meta property="og:locale" content="en_AU">
<meta property="og:url" content="{CANON}">
<meta property="og:title" content="{attr(m['og_title'])}">
<meta property="og:description" content="{attr(m['og_description'])}">
<!-- og:image (1200x630) to add once the hero image is final and cleared for rights -->
<meta name="twitter:card" content="summary_large_image">
<style>{CSS}</style>
<script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
</script>
</head>
<body>
<header class="site"><div class="wrap"><a class="brand" href="/">Wedded Wonderland</a></div></header>
<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>
<li><a href="/">Home</a></li><li><span>Destinations</span></li><li><a href="/destinations/europe">Europe</a></li><li aria-current="page">Portugal</li>
</ol></nav>
<!-- Breadcrumb: "Destinations" is not linked in the preview because its hub URL is not confirmed in this run; schema uses /destinations (dev to confirm). -->
<main>
{body}
</main>
{sticky()}
<script>{JS}</script>
</body>
</html>
"""
    return doc, ld


if __name__ == "__main__":
    doc, ld = page()
    (RUN / "preview.html").write_text(doc)
    (RUN / "schema.jsonld").write_text(
        '<script type="application/ld+json">\n' + json.dumps(ld, indent=2, ensure_ascii=False) + "\n</script>\n"
        if "--script" in sys.argv else json.dumps(ld, indent=2, ensure_ascii=False) + "\n")
    print("ok", len(doc), "revision", COPY["revision"])
    for w in WARN:
        print("WARN", w)
