# Template: Wedding destinations by region (programmatic series)

Built from the Africa page, `articles/2026-11-26-africa-wedding-destinations/` (final, 26 Nov 2026). Use for other regions (for example Asia, the Pacific, the Middle East, Latin America and the Caribbean, Europe). Card pattern adapted from `month-destinations.md`. Each region must read visibly different (its own groups, legal picture and guest entry steps), never a reworded copy of another region.

## URL, title and category
- URL: `/destination-weddings/<region>-wedding-destinations` (lower case). Check the live URL first; if 404, it is a new post after a CMS slug check.
- Primary category: **Destination Weddings** (first in `categories[]`). Secondary: Destination Guides only once confirmed in the CMS (fall back to Destination Weddings only).
- **H1 pattern (title rule, 19 Nov 2026):** keyword first, not a question, 60 characters or fewer, no colons, no dashes. Default: `<Region> Wedding Destinations From <Setting A> to <Setting B>` (Africa used "From Safari to Coast").
- **The number goes in an H2, not the H1:** `Our <N> <region> wedding destinations`. If the Zoho task or the user gives a title that starts with the number (for example "12 Africa Wedding Destinations..."), keep the H1 keyword first and move the number to the H2.
- **TITLE-SERIES note (carry into every region's open items until the user decides):** the task titles lead with the number, which is not keyword first. The user decides between the task title and the title rule; once decided, apply it to every region and update this line.
- **SEO title pattern:** `<Region> Wedding Destinations From <A> to the <B>` (60 characters or fewer, same rules). Africa used "From Safari Camps to the Coast".
- Meta description: 140 to 155 characters, starts with "<Region> wedding destinations", names three or four contrasting places and "with seasons, legal steps and guest travel" (or the region's equivalent).

## Word range
- **2,350 to 2,480 reader words** by `build_docx.py --check` (body plus FAQ, excluding front matter). Brief range 2,200 to 2,800; aim for the band above. Do not pad; trim repeats before cutting facts.

## H2 order
1. Intro (no H2): name the region's three or four kinds of wedding, use the primary keyword in the first 100 words (not as the opening words), then "Here are our <N> picks for a <region adjective> destination wedding, ranked," and end with "Sources current as at <Month Year>".
2. **How we chose these <N>** (criteria line, five bullets, the editorial reason for the top places, then the quiz link).
3. **Our <N> <region> wedding destinations** (H3 cards numbered `1.` to `<N>.`, grouped by kind of wedding; end with the soft CTA line).
4. **Planning a wedding in <region> from Australia** (bold-led paragraphs: legal at home and celebration abroad; guest entry steps; health and insurance; who handles what).
5. **<Region> wedding questions answered** (FAQ, five questions as H3s).
6. `[CTA: discovery_call]` closing block only. Do not type a CTA heading or body into the article; the CMS CTA block carries it.

Key takeaways (five bullets) go in front matter and the CMS Key Takeaways block after the intro. They must not repeat a body sentence word for word.

## How we chose (criteria, use as written)
> This is an editorial judgement, not a weather score or a popularity list. We weighed five things:
- **Setting.** What the place gives a wedding that another would not.
- **Season.** Only as Smartraveller, a national weather service or our own guides describe it.
- **Legal or symbolic.** Is there an official legal route for foreigners? Where there is not, confirm the legal route with that country's embassy before you plan.
- **Smartraveller level.** Quoted exactly, as at <Month Year>. Levels can change, so check again before you book and before guests fly.
- **Guest travel.** Entry steps, transfers and how far everyone has to go.

Say the embassy line once here. Cards with a legal gap then keep a short line ("Confirm with the embassy.").

## Card fields (every card, in this order, bold labels)
- **Why it works.** The setting in one or two sentences, plus guest scale or style. Link our destination page or a real wedding we have featured (never "our client"). No unregistered superlatives ("easiest", "best").
- **Season.** As sourced only: Smartraveller or a national weather service linked inline at the claim, and our own guide attributed in text ("Our honeymoon guide puts..."). Say when a line is national rather than local. If no local season is sourced, send readers to the national weather service ("check the Cape Town season with the South African Weather Service") and open SEASON-CHECK. Never state months, temperatures or rainfall that no source gives. Where you combine two sources, word it as your reading ("Read together, that puts...").
- **Legal or symbolic.** Either the official legal route, linked at the claim to the government or embassy page, then "Confirm the current process with <authority>"; or, where no official fact is saved, the embassy line ("Confirm with the embassy, or hold a symbolic ceremony after a legal wedding at home") plus a FACT-GAP-LEGAL item. Never describe a legal route from our own page alone. Same-sex recognition only from Smartraveller; where it is not sourced, send readers to the local laws section of that country's Smartraveller page and open SAME-SEX-FACTS.
- **Travel advice.** The closing line of every card: Smartraveller's exact level in quotes, linked, plus any area or hazard note it gives ("with higher levels in some areas"). Same-country repeats point back ("The South Africa level above applies here too"). Shared destinations (for example Victoria Falls) give both countries' levels and say "choose your side first".
- Image slot marker after selected cards (about seven slots per article, hero after the H1).

Do not repeat the embassy, legal-at-home or entry-step sentences in several cards; give each once in a card, once in planning and once in the FAQ at most.

## Source rules
- **Never state government fees in an overview.** No marriage licence, certificate or registration fees, even when official; link the legal page instead. Fee conflicts between official pages and our pages go to SITE-CONFLICTS for Nic and the web team.
- **Never link hidden hub pages.** Do not link the region hub (`/destinations/<region>`) or any `/destinations/<region>/*` page that is hidden, 404 or in Review in Zoho. Log them as <REGION>-HUB-404 and retro-link once live. No DRAFT links.
- **Check og:url for redirects.** Every internal and external link must return HTTP 200 with `og:url` equal to the linked URL; if a page redirects, link the final URL (Africa: the old expert-advice honeymoon URL redirects to `/honeymoon-ideas/african-honeymoon`).
- **Smartraveller:** levels quoted exactly and linked at the claim; mark extractions and re-check them on the publish date (VERBATIM-CHECK).
- **Official domains:** foreign government domains (for example dirco.gov.za, statelaw.go.ke, ics.gov.sc) need DOMAINS-ADD approval in `domains.md`.
- **Own pages:** attributed in text and checked live before final; when one of our pages maps seasons to countries by inference, open a COUNTRY-CHECK item.
- **Health:** malaria, vaccinations and light-aircraft luggage point to Smartraveller and the GP (or the operator) only, with no zones or limits stated unless sourced (HEALTH-FACTS).
- No prices, no currency conversions, no temperatures unless an official source publishes them. No competitor lists, content or links. No banned brand words, and none of the words the style guide or merged reviews rule out for perks (say "free" only where the CTA library does). No Wedded World plug unless asked.
- **Legal confirmation always goes to the authorities** (registering office, civil status office, home affairs department or registrar) and the embassy, never to the concierge. The concierge "builds the legal steps into the timeline".
- Brand facts only from `brand-profile.md` (Concierge in Sydney, one dedicated point of contact, wedding and travel under one roof, vendors our team has worked with in-market, guest travel and accommodation, deposits, payments and currency across borders).

## FAQ set (five questions, 35 to 45 words each, FAQPage schema)
1. What is the best month for a wedding in <region>?
2. Can foreigners marry legally in <region>?
3. Can same-sex couples marry in <region>? (sourced lines only, linked)
4. How many guests can we bring to a <region kind> wedding? (no invented capacities)
5. Is <region> safe for our wedding guests? (levels by country, as at <Month Year>)

## Links
- About 40 to 45 body links. Internal: our destination and legal pages, real weddings we have featured, the honeymoon page for the region, the quiz, the relevant Wonderland Studio template, `/wonderland-concierge` (soft CTA and planning section). External: official sources at each claim, Smartraveller for every level.
- Use non-exact anchors for pages that own their keyword; propose retro-links from those pages.

## Open-item checklist (copy into each region and close what does not apply)
- NEW-URL (URL status, Zoho task, plan ref; CMS slug check)
- TITLE-SERIES (number in the task title vs keyword-first H1)
- <REGION>-HUB-404 (hidden or 404 hub and country pages; Zoho task IDs)
- FACT-GAP-LEGAL (each country with no official legal page)
- DOMAINS-ADD (foreign government domains to approve)
- SITE-CONFLICTS (fee or timing conflicts between official pages and ours; no fees stated in the article)
- SEASON-CHECK (local seasons not sourced; extracted weather lines)
- VERBATIM-CHECK (extracted Smartraveller lines; re-check levels on the publish date)
- <PAGE>-COUNTRY-CHECK (own-page lines mapped to countries by inference)
- SAME-SEX-FACTS (countries without a sourced line)
- HEALTH-FACTS (malaria, vaccinations, light-aircraft caveats)
- LINK-MAP-ADD (useful pages not yet in `link-map.md`)
- PERSONA-WIDEN (until the couple persona covers multi-destination pieces)
- LINK-CHECK (every link on publish day, HTTP 200, og:url, no redirects)
- AUTHOR
- IMAGE-RIGHTS
- CMS-URL

## QA before hand-off
- `python3 blog-team/scripts/build_docx.py --check articles/<folder>/final.md`: reader words in range, 0 em dashes, 0 en dashes, 0 visible placeholders, no blocked domains.
- Sentence-case H2 and H3, Australian spelling, numbers per style guide, no banned words, no government fees, no hub links.
