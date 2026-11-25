# Template: Wedding destinations by month (programmatic series)

Built from the February page, `articles/2026-11-24-wedding-destinations-february/` (final, 25 Nov 2026). Use for the remaining months. Live siblings: `/destination-weddings/wedding-destinations-january`, `-may`, `-october`. Structure follows the live siblings and the honeymoon-by-month series; each month must read visibly different (its own calendar events, hemisphere split and wait list), never a reworded copy of another month.

## URL, title and category
- URL: `/destination-weddings/wedding-destinations-<month>` (lower case). Check the live URL first; if 404, it is a new post after a CMS slug check.
- Primary category: **Destination Weddings** (first in `categories[]`). Secondary: Destination Guides only once confirmed in the CMS (CATEGORY-CHECK until then).
- **H1 pattern (title rule, 19 Nov 2026):** keyword first, not a question, 60 characters or fewer, no colons, no dashes. Default: `Wedding Destinations in <Month> and Our 10 Best Picks`.
- **SEO title pattern:** `Wedding Destinations in <Month> for <three-word hook>` (60 characters or fewer, same rules). February used "for Sun, Sand or Snow".
- **TITLE-SERIES note (carry into every month's open items until the user decides):** the live siblings use `10 Best Wedding Destinations in <Month>` H1s, which is not keyword first. The user decides between series consistency and the title rule; once decided, apply it to every month and update this line.
- Meta description: 140 to 155 characters, starts with "Wedding destinations in <Month>", names three contrasting settings and "ranked by season, guest travel and how early to book" (or the month's equivalent).

## Word range
- **2,250 to 2,300 reader words** by `build_docx.py --check` (body plus FAQ, excluding front matter). Do not pad; trim repeats before cutting facts.

## H2 order
1. Intro (no H2): answer "Is <Month> a good time for a wedding?" in the first 100 words, name the hemisphere split, use the primary keyword, end with "Sources current as at <Month Year>".
2. **How we ranked the ten** (criteria line, then four bullets, then the quiz, previous-month sibling and travel-month links).
3. **Our 10 best wedding destinations in <Month>** (ten H3 cards, numbered `1.` to `10.`).
4. **Where to wait for a better month** (three or four places, then the soft CTA line).
5. **Planning a <Month> date abroad** (bullets: the month's calendar events, transfers, weather backup, lead time, the legal side, insurance).
6. **What your concierge handles behind a <Month> date** (brand proof points only; no fees, commissions or names).
7. **<Month> wedding questions answered** (FAQ, five questions as H3s).
8. `[CTA: discovery_call]` closing block.

Key takeaways (five bullets) go in front matter and the CMS Key Takeaways block after the intro. They must not repeat a body sentence word for word.

## Ranking criteria line (use as written, adapt the calendar examples)
> This is an editorial judgement, not a weather score. We weighed four things: **<Month> conditions,** as Smartraveller, a national weather service or our own guide describes them; **guest travel from Australia,** including the transfer at the far end; **what <Month> gives you there** that another month would not; and **what the calendar asks of you,** from <event> to <event>.

Follow with: "No temperature or price appears unless an official source or our own guide publishes it, and travel advice levels are as at <Month Year> and can change."

## Card fields (every card, in this order, bold labels)
- **Why <Month> works.** One official season line linked at the claim, plus one own-page quote, verbatim.
- **The honest caveat.** One real constraint (transfers, storms, Ramadan, fire danger, snow not guaranteed). Where a legal marriage is possible, send readers to the destination's authorities and the Australian embassy (or the celebrant for Australian destinations). Never describe a legal route without a saved official fact.
- **Who it suits.** One line, guest scale or style. Link our destination page here if not linked above.
- **Travel advice.** Smartraveller's exact level, in quotes, linked. Same-country repeats point back ("The UAE level and storm warning above apply here too").
- Image slot marker after selected cards (about seven slots per article, hero after the H1).

Do not repeat the same lead-time or Ramadan sentence in several cards; give it once in a card, once in planning and once in the FAQ at most.

## Source rules
- **Weather and seasons:** official meteorological services only (BoM, NIWA, IPMA, TMD, MeteoSwiss and equivalents in `domains.md`) or Smartraveller, **linked inline at the claim**. Say when a figure is for one station only (for example Hobart, Funchal) or national rather than local.
- **Smartraveller:** advice levels quoted exactly and linked at the claim; re-check every level and any body vs meta conflict on the publish date (VERBATIM-CHECK).
- **Own pages:** quoted verbatim, with `own_page_facts` entries (source URL, accessed date, verified_by) and **verified live** before final. Our pages are attributed in text ("Our Dubai guide says"). If a quote contains a banned style word, quote only the part around it.
- **No invented weather figures:** no temperatures, rainfall, sea temperatures or sunshine hours unless an official source publishes them; no "perfect weather" or guarantees.
- No prices unless from our own live pages, dated and flagged for Nic. No competitor rankings, content or links. No currency conversions unless asked.
- No banned brand words (see the style guide). Brand facts only from `brand-profile.md` or live weddedwonderland.com pages. No Wedded World plug in this series unless asked.
- Legal confirmation always goes to the registering office or authorities and the Australian embassy or consulate (or the celebrant in Australia), never to the concierge.

## Calendar checks (every month)
- **Ramadan and Eid:** check whether either falls in or near the month for any Gulf, North African, Malaysian, Indonesian or Turkish pick. Use an official date if one exists; otherwise attribute to our own page and keep RAMADAN-<year> open. Dates move earlier each year.
- **Public holidays and festivals:** Chinese New Year, Diwali, Easter and Orthodox Easter, Golden Week, school holidays in Australia, national days. Only state a date from an official or own source.
- **Peak-demand days:** Valentine's week (February), Christmas and New Year, Easter. Tie to an own-page or official line if one exists.
- **Seasonal hazards:** cyclone, monsoon, hurricane, bushfire, avalanche and heat warnings from Smartraveller or the national service.

## Where to wait section
- Three or four destinations readers will ask about that do not suit the month, each with the official reason linked at the claim, our own page's better months quoted, and a link to that destination's best-time page.
- Use a non-exact anchor for any best-time page (for example "Our Italy guide", "Bali month by month").
- End with the soft CTA line from `cta-library.md`.

## FAQ set (five questions, 35 to 45 words each, FAQPage schema)
1. Is <Month> a good time for a wedding?
2. What are the best places to get married in <Month> for a beach wedding? (uses the secondary keyword variant once)
3. One calendar question for the month (for example Ramadan in the Gulf, Christmas in Europe, Golden Week in Japan).
4. How far ahead should we book a <Month> wedding abroad?
5. Can we marry in <wait-list destination> in <Month>?

## Links
- About 33 to 37 body links. Internal: previous and next month siblings (only when live), the travel-month and honeymoon-month pages, the quiz, destination pages, best-time pages, `/wonderland-concierge` (soft CTA and concierge section). External: official sources at each claim.
- Never link DRAFT pages; propose retro-links from the siblings and the month's honeymoon and travel pages.

## Open-item checklist (copy into each month and close what does not apply)
- NEW-URL (URL status, Zoho task, plan ref; CMS slug check)
- TITLE-SERIES (see above)
- RAMADAN-<year> or the month's calendar item without an official date
- VERBATIM-CHECK (extracted Smartraveller and met-service lines; body vs meta level conflicts)
- SITE-CONFLICTS (our own pages disagreeing with each other or with Smartraveller; competitor or third-party outbound links on pages we link)
- CATEGORY-CHECK (Destination Guides)
- PERSONA-WIDEN (until the couple persona covers multi-destination pieces)
- LINK-CHECK (every link on publish day, PDFs included)
- AUTHOR
- IMAGE-RIGHTS
- CMS-URL
- SIBLINGS (add next month's link when live)

## QA before hand-off
- `python3 blog-team/scripts/build_docx.py --check articles/<folder>/final.md`: reader words in range, 0 em dashes, 0 en dashes, 0 visible placeholders, no blocked domains.
- Sentence-case H2 and H3, Australian spelling, numbers per style guide, no banned words.
