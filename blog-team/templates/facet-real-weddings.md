# Template: Real weddings facet page (by destination)

Built from the Italy page, `articles/2026-11-26-italy-real-wedding/` (final, 26 Nov 2026). Use for any destination facet that gathers our own published real weddings (for example France, Greece, Bali, Mexico). A facet page is a curated hub of weddings already live on weddedwonderland.com, grouped by region, with one card per wedding. It is not a gallery of other sites' weddings and not a case study of our planning work.

## URL, title and category
- URL: `/real-weddings/<destination>-real-wedding` (lower case). Check the live URL first; if 404, it is a new post after a CMS slug check (NEW-URL).
- Primary category: **Real Weddings** (first in `categories[]`, repeated in `primary_category`). Secondary: Destination Weddings.
- **H1 pattern (title rule, 19 Nov 2026):** keyword first, not a question, 60 characters or fewer, no colons, no dashes. Default: `<Destination> Real Weddings to Inspire Your Celebration`.
- **SEO title pattern:** `<Destination> Real Wedding Inspiration from <Region A> to <Region B>` (60 characters or fewer, same rules). Italy used "from Lake Como to Sicily".
- Meta description: 140 to 155 characters, starts with "<Destination> real wedding stories by region", names three to five regions with a concrete setting each (villas, balconies, estates), ends with "and what each couple chose".
- Tags: 3 to 6, lower case, the destination plus its regions (for example `italy, lake como, amalfi coast, tuscany, puglia, sicily`). Do not repeat category names as tags.

## Word range
- **1,800 to 1,900 reader words** by `build_docx.py --check` (body plus FAQ, excluding front matter and markers). 10 to 12 cards. Do not pad; trim styling lines before cutting facts.

## H2 order
1. Intro (no H2): what a real wedding there looks like once guests arrive, the number of weddings, the framing line (below), what each card gives, a link to `/blog/real-weddings`, then "Sources current as at <Month Year>".
2. **<Region> real weddings** (one H2 per region, in the order readers search them; two to three cards each, one card allowed for a smaller region).
3. **Planning your own <Destination> wedding** (season, ceremony and legal route, cost, venues, Smartraveller level, the destination guide, then one Concierge sentence from brand-profile proof points).
4. **<Destination> real wedding questions answered** (FAQ, four questions as H3s).
5. `[CTA: discovery_call]` closing block (never typed into the body).

Key takeaways (five bullets) go in front matter and the CMS Key Takeaways block after the intro. They must not repeat a body sentence word for word.

## Region H2s
- Heading: `<Region> real weddings` in sentence case (for example "Lake Como real weddings", "Amalfi Coast real weddings").
- Intro: **one sentence** on how the region feels across these weddings, with **one guide link only** (the region hub or our region guide, non-exact anchor where another page owns the exact term).
- Combine thin regions only if the page states both (do not merge regions to hide a gap; split instead).

## Card fields (every card, in this order)
- **H3:** `<Couple names as published> at <Venue>, <Town>`.
- **Venue.** Town and venue as the page gives them. Link `/venue/<slug>` **only if it is the same venue** (Villa Balbiano is not Villa del Balbianello).
- **When.** Month and year **only if the page states them**; otherwise omit the label. Never take a month from a brief, a title or an image.
- **Ceremony.** As worded on the page (Catholic Mass, Maronite blessing, Gujarati Hindu ceremony, celebrant). Never call a ceremony symbolic or legal unless the page says so.
- **Body (two to three sentences):** the couple names as published, **linked to their wedding page in the first sentence** (alternate names only and names plus place as anchors; never "See the full wedding"). One distinguishing line (setting, guest mix, format or a moment) and **one style line** only.
- **Quote:** one short quote if the page captured it, attributed as the page gives it ("as our feature describes it", "Sharlene told us", "as the page reports it"). Keep the source's spelling inside quotes.
- **Credit:** photographer credit in italics, exactly as published (handle or name), plain text, not linked.
- Image slot marker after selected cards (about half the cards).

## Framing rules
- Framing line in the intro, once: "All were featured on Wedded Wonderland". Never "our clients", "we planned", "our couples".
- **Never say who planned a wedding** (no planner, no self-planned note).
- **No prices, no guest counts and no planner partners.** Budgets point to our cost guide. If a page calls a planner a partner or network member, leave it out (PARTNER-HOLD) until marketing confirms.
- Australian couples: say "from Sydney" or "from Australia" only where the page says so.
- No competitor real weddings, images or links. No Wedded World plug unless the brief asks.
- Legal lines: attribute to our own legal guide and send readers to the registering office or consulate (and Smartraveller for recognition in Australia). Never state a legal route without a saved official or own-page fact.
- No em or en dashes; no banned style words; no visible placeholder markers.

## Overlap and links
- Link `/blog/real-weddings` in the intro (the global category listing) and the complete destination guide in Planning, so the facet does not compete with either.
- One guide link per region intro; one soft CTA line (`destination_explore`, for example "To compare regions, explore weddings in <Destination>.") at the end of a middle region.
- Each wedding page linked once, from the couple names. About 30 to 35 links in total.

## Images
- **Only from the featured weddings**, from that wedding's own gallery, with the photographer credit as published in the caption (IMAGE-RIGHTS, PHOTOGRAPHER-CREDIT).
- Captions name a month only if the page states it.
- Where a page has no featured image, flag IMAGE-GAP: pick from the gallery only, or give the card no slot. Never fill a gap with stock or another wedding.

## Publish-day checks
- **og:url:** every linked wedding page and new link returns 200, og:url equals the URL, no redirects (OG-URL-CHECK). Do not link DRAFT or redirecting URLs.
- **Redirect check:** the facet URL itself is 404 before creating; no redirect is added in the CMS.
- **LINK-CHECK:** all links at publish (HTTP 200, no redirects).

## Open-item checklist (carry each that applies)
- NEW-URL (404 confirmed; CMS slug check before creating)
- ZOHO-TASK (task found or to be created)
- CATEGORY-CONSENT (couples' consent covers a roundup under Real Weddings)
- IMAGE-RIGHTS (reuse confirmed with each photographer)
- PHOTOGRAPHER-CREDIT (credit format confirmed)
- IMAGE-GAP (pages with no featured image)
- <DESTINATION>-LEGAL-OFFICIAL (official marriage source, if none in the pack)
- VENUE-CHECK (any venue name read from a field rather than the page text)
- PARTNER-HOLD (planners called partners on any page)
- OG-URL-CHECK
- SERP-PARTIAL (if only some locations returned SERP data)
- WEDDED-WORLD (no plug, per brief)
- LINK-CHECK
- AUTHOR
- CMS-URL
