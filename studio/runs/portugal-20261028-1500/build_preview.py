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
            if "Tab label: Costs" in line and "costs" in hooks:
                flush()
                close_group()
                out.append(hooks["costs"]())
                continue
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
    lines = [l for l in s["body_md"].split("\n") if l.strip()]
    h1 = lines[0][2:]
    assert h1 == P["h1"]
    quick = lines[1:4]
    return f"""
<section class="hero" id="top" aria-labelledby="h1">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <h1 id="h1">{esc(h1)}</h1>
      <p class="lede">{"<br>".join(inline(l) for l in quick)}</p>
      <p class="actions">{link('#regions', 'Find your region in Portugal', cls='btn', entry='hero')} {link('#enquire', 'Speak with a Wedded Advisor', cls='btn btn--secondary', entry='hero')}</p>
      <p class="textlink">{link('#marrying-legally', 'Check the rules for your passport')}</p>
      <p class="brand-line">{esc(lines[6])}</p>
      <p class="small">{esc(lines[7])}</p>
    </div>
    {capslot('s1-hero', 'hero', 'pena-palace-sintra-hills-wedding-in-portugal.jpg',
             'Pena Palace on its wooded hilltop above Sintra, a palace setting for a wedding in Portugal',
             hero=True, ratio='r45')}
  </div>
</section>"""


def b9():
    md = S["b9-qualifier"]["body_md"]
    groups = re.findall(r"^([^\n-][^\n]*\?)\n((?:- [^\n]+\n?)+)", md, re.M)
    names = ["season", "guests", "celebration"]
    fields = []
    for (q, opts), name in zip(groups, names):
        o = "".join(f"<option>{esc(x[2:].strip())}</option>" for x in opts.strip().split("\n"))
        fields.append(f'<div class="field"><label for="b9-{name}">{esc(q)}</label>'
                      f'<select id="b9-{name}" data-b9="{name}"><option value="">Choose</option>{o}</select></div>')
    helper = re.search(r"\n(Your Wedded Advisor confirms[^(]+?)\s*\(CMS", md).group(1)
    return f"""
<section class="b9" aria-label="Check your date">
  <div class="wrap">
    <!-- B9 qualifier bar. CMS note: the button does not submit. It carries the three answers into the matching Season, Guests and Celebration fields of the enquiry form (s10-form), sets entry_point=b9 and scrolls to #enquire. -->
    <div class="b9-bar" role="group" aria-label="Your plans">
      {''.join(fields)}
      <div class="field field--btn"><a class="btn" href="#enquire" id="b9-go" data-entry-point="b9">Check your date</a></div>
    </div>
    <p class="small helper">{esc(helper)}</p>
  </div>
</section>"""


def b8():
    md = S["b8-proof-strip"]["body_md"]
    ids = fact_ids(APPLY_RE.match(md).group(1))
    fb = md.split(FALLBACK, 1)[1].strip()
    return f"""
<section class="b8" aria-label="How this page is checked">
  <!-- Apply after sign-off ({ids}): numeric proof line replaced by the fallback below until then -->
  <div class="wrap"><p data-signoff="{ids}">{esc(fb)}</p></div>
</section>"""


B16_SLOTS = {
    "Pena, Sintra": ("pena", "pena-palace-above-trees-sintra.jpg", "Pena Palace rising above the wooded park in the Sintra hills, wrapped in light mist"),
    "Monserrate, Sintra": ("monserrate", "monserrate-palace-arches-lawns-sintra.jpg", "Monserrate Palace arches above the lawns of its Romantic park in Sintra"),
    "Queluz, Near Lisbon": ("queluz", "queluz-national-palace-facade-dusk.jpg", "Facade of the National Palace of Queluz near Lisbon at dusk"),
    "The Douro Valley": ("douro", "douro-valley-terraced-vineyards.jpg", "Steep terraced vineyards in the Alto Douro Wine Region"),
    "The Algarve Coast": ("ponta_da_piedade", "algarve-coast-clifftops-atlantic.jpg", "Golden clifftops above the Atlantic on the Algarve coast"),
}


def b16():
    s = S["b16-spotlight"]

    def after(text):
        if text in B16_SLOTS:
            key, f, alt = B16_SLOTS[text]
            return capslot("b16-spotlight", key, f, alt)

    def before(line):
        if line.startswith("For the customs behind the day"):
            return ('<div class="strip3">'
                    + capslot("b16-spotlight", "azulejo", "azulejo-tile-wall-detail-portugal.jpg", "Close-up of blue and white azulejo tiles on a Portuguese wall")
                    + capslot("b16-spotlight", "fado", "fado-guitar-portugal.jpg", "A Portuguese guitar used to play fado")
                    + capslot("b16-spotlight", "quinta_staircase", "quinta-stone-staircase-couple-portugal.jpg", "Couple on the stone staircase of a Portuguese quinta before dinner")
                    + "</div>")

    body = render(s["body_md"], hooks={"after_heading": after, "before_para": before}, wrap_h3="card")
    return f'<section class="section section--linen" id="spotlight">\n<div class="wrap">\n{body}\n</div>\n</section>'


S2_SLOTS = {
    "Lisbon, Sintra and Cascais": ("lisbon_sintra_cascais", "lisbon-sintra-cascais-pena-palace-forest.jpg", "Pena Palace above the forest in Sintra, in the Lisbon, Sintra and Cascais region"),
    "The Algarve": ("algarve", "algarve-clifftops-beach-sea-stacks.jpg", "Sea stacks and a sandy beach below the Algarve clifftops"),
    "Porto and the Douro Valley": ("porto_douro", "porto-douro-terraced-vineyards-river.jpg", "Terraced vineyards above the Douro river in the Alto Douro Wine Region"),
    "Comporta and the Alentejo": ("comporta_alentejo", "comporta-alentejo-coast-dunes-dusk.jpg", "Dunes on the Alentejo coast at Comporta at dusk"),
    "Madeira": ("madeira", "madeira-atlantic-cliffs-green-hills.jpg", "Green cliffs above the Atlantic on the island of Madeira"),
}


def palace():
    s = S["add-palace-rules"]
    body = render(s["body_md"])
    return f'<aside class="callout" id="palace-rules" aria-labelledby="palace-h">\n{body.replace("<h3>", "<h3 id=\"palace-h\">", 1)}\n</aside>'


def s2():
    s = S["s2-regions"]

    def after(text):
        if text in S2_SLOTS:
            key, f, alt = S2_SLOTS[text]
            return capslot("s2-regions", key, f, alt, tone="warm")

    body = render(s["body_md"], hooks={"after_heading": after, "palace": palace}, wrap_h3="card region")
    body = body.replace("<h2>", '<h2 id="regions-h">', 1)
    return (f'<section class="section" id="regions" aria-labelledby="regions-h">\n<div class="wrap">\n{body}\n'
            f'<!-- add-beach-line: entered once as the extra line of The Algarve card above (no separate block) -->\n</div>\n</section>')


S3_SLOTS = {
    "A Legal Route for Foreign Couples": ("registry-table-signing-portugal.jpg", "Couple signing the marriage register at a civil registry table in Portugal"),
    "Palaces You Can Book": ("monserrate-gardens-sintra.jpg", "Gardens of the Park and Palace of Monserrate in Sintra"),
    "A UNESCO Wine Landscape": ("douro-slate-terraces-vineyards.jpg", "Slate terraces lined with vines in the Douro Valley"),
    "Beaches and Clifftops": ("algarve-beach-low-sun.jpg", "Algarve beach and clifftops in low evening sun"),
    "Easy to Reach on Three Passports": ("lisbon-arrival-couple-city-street.jpg", "Couple arriving in Lisbon, walking a city street with their luggage"),
}


def s3():
    s = S["s3-reasons"]

    def after(text):
        if text in S3_SLOTS:
            f, alt = S3_SLOTS[text]
            return slot(f, alt)

    body = render(s["body_md"], hooks={"after_heading": after}, wrap_h3="card")
    return f'<section class="section section--linen" id="why-portugal">\n<div class="wrap">\n{body}\n</div>\n</section>'


S4_SLOTS = {
    "**Quinta.**": ("s4_quinta", "quinta-courtyard-dinner-table-portugal.jpg", "Quinta courtyard laid with a long table for a wedding dinner"),
    "**Palace or pousada.**": ("s4_pousada", "pousada-historic-castle-cloister.jpg", "Stone cloister of a pousada in a historic Portuguese castle"),
    "**Clifftop or beach.**": ("s4_clifftop", "algarve-clifftop-ceremony-aisle.jpg", "Ceremony aisle set on an Algarve clifftop above the Atlantic"),
    "**Vineyard estate.**": ("s4_vineyard", "douro-wine-quinta-vineyard-terrace.jpg", "Vineyard terrace at a wine quinta in the Douro Valley"),
    "**In the city.**": ("s4_city", "lisbon-civil-ceremony-salon.jpg", "Civil wedding ceremony in an ornate salon in Lisbon"),
    "**Catholic church or another faith.**": ("s4_church", "portugal-church-doorway-ceremony.jpg", "Couple at the doorway of a church in Portugal after a Catholic ceremony"),
}


def s4():
    s = S["s4-settings"]
    md = s["body_md"]
    head, rest = md.split("\n\n", 2)[0:2], md.split("\n\n", 2)[2]
    cards = []
    for para in rest.split("\n\n"):
        key = next(k for k in S4_SLOTS if para.startswith(k))
        ck, f, alt = S4_SLOTS[key]
        cards.append(f'<div class="card">{capslot("s4-settings", ck, f, alt)}<p>{inline(para)}</p></div>')
    vc = render(S["add-venue-charges"]["body_md"])
    return f"""
<section class="section" id="settings">
<div class="wrap">
{render(head[0])}
<p>{inline(head[1])}</p>
<div class="grid3">
{chr(10).join(cards)}
</div>
<aside class="callout" id="venue-charges-box">
{vc}
</aside>
</div>
</section>"""


def costs_panel():
    s = S["add-cost-bands"]
    md = s["body_md"]
    # Launch state: drop everything from the APPLY marker to the FALLBACK marker
    m = APPLY_RE.search(md.split("\n\n", 1)[1]) or re.search(r"\[APPLY AFTER SIGN-OFF: ([^\]]+)\]", md)
    ids = fact_ids(m.group(1))
    head = md.split("\n\n", 1)[0]
    after = md.split(FALLBACK, 1)[1]
    fb_line, tail = after.strip().split("\n", 1)
    return (f'<div class="tab-panel" id="costs">\n<!-- Tab label: Costs -->\n'
            f'{render(head)}\n'
            f'<!-- Apply after sign-off ({esc(m.group(1))}): named third-party cost table (Rita Plácido Photography, EUR ranges) replaced by the fallback below until then -->\n'
            f'<p data-signoff="{ids}">{inline(fb_line)}</p>\n'
            f'{render(tail.strip())}\n</div>')


TAB_IDS = {"Getting There": "getting-there", "Entry Rules by Passport": "entry-rules",
           "Marrying Legally, by Passport": "marrying-legally", "What to Wear for Your Weekend": "your-weekend"}


def s5():
    s = S["s5-plan"]
    md = s["body_md"]
    # Wrap each tab panel: render with wrap_h3 groups, ids on the panel headings
    body = render(md, hooks={"costs": costs_panel}, wrap_h3="tab-panel")
    # move heading ids to the panel wrapper so anchors land on the panel
    for title, tid in TAB_IDS.items():
        body = re.sub(r'<div class="tab-panel">\n<h3( id="[\w-]+")?>' + re.escape(esc(title)),
                      f'<div class="tab-panel" id="{tid}">\n<h3>{esc(title)}', body)
    tabs = ('<nav class="tabs" aria-label="Plan your wedding">'
            '<a href="#getting-there">Getting there</a><a href="#entry-rules">Entry rules</a>'
            '<a href="#marrying-legally">Marrying legally</a><a href="#costs">Costs</a>'
            '<a href="#your-weekend">Your weekend</a></nav>')
    body = body.replace("</p>", "</p>\n" + tabs, 1)  # after the freshness line
    return f'<section class="section section--linen" id="plan">\n<div class="wrap narrow">\n{body}\n</div>\n</section>'


def s6():
    body = render(S["s6-weekend"]["body_md"])
    return (f'<section class="section" id="weekend">\n<div class="wrap split">\n<div>{body}</div>\n'
            + capslot("s6-weekend", "s6", "quinta-long-dinner-table-portuguese-wine.jpg",
                      "Long dinner table with Portuguese wine at a quinta after the ceremony", tone="dusk")
            + "\n</div>\n</section>")


def s7():
    body = render(S["s7-guests"]["body_md"])
    return (f'<section class="section section--sage" id="guests">\n<div class="wrap split">\n<div>{body}</div>\n'
            + capslot("s7-guests", "s7", "quinta-terrace-guests-morning-after.jpg",
                      "Wedding guests at breakfast on a quinta terrace the morning after")
            + "\n</div>\n</section>")


S9_SLOTS = {
    "After the Wedding": ("honeymoon", "madeira-atlantic-coast-honeymoon.jpg", "Madeira's Atlantic coastline seen from a clifftop viewpoint"),
    "Anniversary in the Douro": ("anniversary", "douro-anniversary-wine-tasting-terraces.jpg", "Couple at a wine tasting above the Douro Valley terraces"),
    "Proposal in Sintra": ("proposal", "sintra-pena-park-proposal.jpg", "Proposal in the wooded park below Pena Palace, Sintra"),
    "Vow Renewal on the Algarve": ("vow_renewal", "algarve-clifftop-vow-renewal.jpg", "Couple renewing their vows on an Algarve clifftop above the Atlantic"),
    "Milestone Birthday": ("birthday", "douro-quinta-birthday-lunch.jpg", "Family birthday lunch at a long table at a Douro wine quinta"),
}


def s9():
    md = S["s9-celebrations"]["body_md"]
    parts = md.split("\n\n")
    h2 = parts[0]
    cards = []
    tail = []
    for p in parts[1:]:
        m = re.match(r"^\*\*(.+?)\*\*\n(.+)$", p, re.S)
        if m:
            key, f, alt = S9_SLOTS[m.group(1)]
            cards.append(f'<div class="card">{capslot("s9-celebrations", key, f, alt, tone="warm")}'
                         f'<p class="label">{esc(m.group(1))}</p><p>{inline(m.group(2))}</p></div>')
        else:
            tail.append(p)
    return (f'<section class="section section--linen" id="celebrations">\n<div class="wrap">\n{render(h2)}\n'
            f'<div class="grid3">{"".join(cards)}</div>\n{render(chr(10).join(tail))}\n</div>\n</section>')


def s10():
    body = render(S["s10-advisor"]["body_md"])
    return (f'<section class="section" id="advisor-section">\n<div class="wrap split">\n<div>{body}</div>\n'
            + capslot("s10-advisor", "advisor_band", "wedded-advisor-planning-with-couple.jpg",
                      "Wedded Advisor planning with a couple at a table, laptop and notes open")
            + "\n</div>\n</section>")


def form():
    md = S["s10-form"]["body_md"]
    intro = re.search(r"\n\n(Tell us your region[^\n]+)", md).group(1)

    def opts(label):
        line = re.search(r"^- " + re.escape(label) + r": (.+)$", md, re.M).group(1)
        return [o.strip() for o in line.split("|")]

    def select(fid, name, label, options, required=False, optional=False):
        lab = esc(label) + (' <span class="opt">(optional)</span>' if optional else "")
        req = " required" if required else ""
        o = "".join(f"<option>{esc(x)}</option>" for x in options)
        return (f'<div class="field"><label for="{fid}">{lab}</label>'
                f'<select id="{fid}" name="{name}"{req}><option value="">Choose</option>{o}</select></div>')

    errs = dict(re.findall(r"^- ([^:]+): (.+)$", md.split("**Error messages:**")[1].split("**Success")[0], re.M))
    succ_h = re.search(r"- Heading: (.+)", md).group(1)
    succ_b = re.search(r"- Body: (.+)", md).group(1)
    hidden = {"route_to": ROUTE, "destination": "Portugal", "page_slug": "/destinations/europe/portugal",
              "offer": "", "entry_point": ""}
    hid = "".join(f'<input type="hidden" name="{k}" value="{attr(v)}">' for k, v in hidden.items())
    hid += "".join(f'<input type="hidden" name="{u}" value="">' for u in
                   ("utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"))
    return f"""
<section class="section section--sage" id="enquire" aria-labelledby="enquire-h">
<div class="wrap narrow">
<h3 id="enquire-h">Tell Us Your Plans</h3>
<p>{esc(intro)}</p>
<form class="enquiry" action="{ENDPOINT}" method="post" novalidate>
  <!-- Hidden fields (approved, addendum 13, UX13, D13). entry_point = hero | b9 | region-card | tab-link | celebrations | closing | sticky; offer = region card title when opened from a region card, otherwise blank; utm_* captured from the URL. -->
  {hid}
  <div class="row2">
    <div class="field"><label for="f-first">First name</label><input id="f-first" name="first_name" type="text" autocomplete="given-name" required data-msg-required="{attr(errs['First name empty'])}"></div>
    <div class="field"><label for="f-last">Last name</label><input id="f-last" name="last_name" type="text" autocomplete="family-name" required data-msg-required="{attr(errs['Last name empty'])}"></div>
  </div>
  <div class="row2">
    <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required data-msg-required="{attr(errs['Email empty'])}" data-msg-invalid="{attr(errs['Email not valid'])}"></div>
    <div class="field"><label for="f-phone">Phone <span class="opt">(optional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
  </div>
  {select('f-region', 'region', 'Region', opts('Region'))}
  <div class="row2">
    {select('f-season', 'season', 'Season', opts('Season'))}
    {select('f-year', 'year', 'Year', opts('Year (optional)'), optional=True)}
  </div>
  {select('f-guests', 'guests', 'How many guests?', opts('How many guests?'))}
  {select('f-celebration', 'celebration', 'What are you celebrating?', opts('What are you celebrating?'))}
  {select('f-ceremony', 'ceremony_type', 'Ceremony type', opts('Ceremony type (optional)'), optional=True)}
  <div class="field"><label for="f-notes">Anything we should know?</label><textarea id="f-notes" name="message" rows="4" placeholder="Budget, dates you have in mind, anything else"></textarea></div>
  <p class="form-error" role="alert" hidden data-msg-submit="{attr(errs['Submit failed'])}"></p>
  <button class="btn btn--full" type="submit">Send your enquiry</button>
  <p class="small consent">By sending this form you agree to our {link(TODO_URL, 'Privacy Policy')}.</p>
</form>
<template id="enquiry-success"><div class="success" role="status"><h4>{esc(succ_h)}</h4><p>{esc(succ_b)}</p></div></template>
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
    # check the s11 body says the same thing as payload.faq
    body = S["s11-faq"]["body_md"]
    for f in P["faq"]:
        assert f["q"] in body and f["a"] in body, f["q"]
    qa = "\n".join(f'<div class="qa"><h3>{esc(h)}</h3><p>{a}</p></div>' for h, _, a, _ in items)
    return f"""
<section class="section" id="faq" aria-labelledby="faq-h">
<div class="wrap narrow">
<h2 id="faq-h">Get Answers Before You Enquire</h2>
<div class="faq">
{qa}
</div>
<!-- CMS note: FAQPage schema uses the visible text word for word; while a sign-off is pending, schema carries the FALLBACK text. In schema, the FAQ 1 link becomes plain text. -->
</div>
</section>"""


def closing():
    md = S["closing-cta"]["body_md"]
    first = md.split("\n\n")[0]
    return f"""
<section class="closing" aria-label="Speak with a Wedded Advisor">
<div class="wrap narrow"><p>{esc(first)}</p><p class="actions">{link('#enquire', 'Speak with a Wedded Advisor', cls='btn', entry='closing')}</p></div>
</section>"""


def s12():
    md = S["s12-articles"]["body_md"]
    parts = md.split("\n\n")
    out = [render(parts[0]), '<div class="grid2">']
    for p in parts[1:3]:
        a, d = p.split("\n")
        m = re.match(r"\[(.+)\]\((.+)\)", a)
        out.append(f'<div class="card article">{link(m.group(2), m.group(1), cls="card-title")}<p class="small">{esc(d)}</p></div>')
    out.append("</div>")
    out.append(render("\n\n".join(parts[3:])).replace("<p><strong>Trending row</strong></p>", '<p class="label">Trending row</p>'))
    return f'<section class="section section--linen" id="articles">\n<div class="wrap">\n' + "\n".join(out) + "\n</div>\n</section>"


def s13():
    body = render(S["s13-europe"]["body_md"])
    body = body.replace("<ul>", '<ul class="chips">', 1)
    return f'<section class="section" id="europe">\n<div class="wrap">\n{body}\n</div>\n</section>'


def sticky():
    return """
<div class="sticky-cta" id="sticky-cta" aria-label="Enquire">
  <!-- Mobile sticky bar. No price slot. Hidden while the enquiry form is in view. -->
  <span class="sticky-label">Wedding in Portugal</span>
  <a class="btn" href="#enquire" data-entry-point="sticky">Speak with a Wedded Advisor</a>
</div>"""


# ---------------------------------------------------------------- schema
REGIONS = ["Lisbon, Sintra and Cascais", "The Algarve", "Porto and the Douro Valley",
           "Comporta and the Alentejo", "Madeira"]


def schema():
    org = {"@type": "Organization", "@id": DOMAIN + "/#organization", "name": CONFIG["brand"]["name"],
           "url": DOMAIN + "/"}
    dest = {"@type": "TouristDestination", "@id": CANON + "#destination", "name": "Portugal",
            "url": CANON,
            "description": P["meta"]["description"],
            "containedInPlace": {"@type": "Continent", "name": "Europe"},
            "touristType": "Couples planning a destination wedding"}
    il = {"@type": "ItemList", "@id": CANON + "#regions", "name": "Choose Your Region of Portugal",
          "numberOfItems": len(REGIONS),
          "itemListElement": [{"@type": "ListItem", "position": i, "name": r} for i, r in enumerate(REGIONS, 1)]}
    svc = {"@type": "Service", "@id": CANON + "#concierge", "name": CONFIG["brand"]["concierge_name"],
           "serviceType": "Destination wedding planning",
           "description": "Wedded Concierge pairs you with a Wedded Advisor who plans with you from the first enquiry to the last dance.",
           "provider": {"@id": org["@id"]},
           "areaServed": {"@type": "Country", "name": "Portugal"},
           "url": DOMAIN + "/wonderland-concierge"}
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
<!-- PREVIEW ONLY (Page Studio run portugal-20261028-1500, Stage 5, copy scope). Not the deliverable; launch state with fallback lines for every sign-off pair. -->
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
    print("ok", len(doc))
