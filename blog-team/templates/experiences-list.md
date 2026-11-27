# Template: Experience-list travel guides

Built from the couples experiences page, `articles/2026-11-27-couples-experiences/` (final, 27 Nov 2026). Use for other list guides built from experiences rather than destinations (for example anniversary experiences, proposal experiences, winter experiences, experiences in one region). Each guide must have its own list, groups and caveats, never a reworded copy of another guide. Sibling pages own their keywords: never repeat an experience that another live guide lists (couples experiences avoids the 15 days on `/travel-guides/private-tours`).

## URL, title and category
- URL: `/travel-guides/<keyword-slug>` (lower case). Check the live URL first; if it returns 404, it is a new post after a CMS slug check (NEW-URL).
- Primary category: **Travel Guides** (first in `categories[]`, repeated in `primary_category`). Secondary: Honeymoon Ideas or Celebration Ideas, whichever matches the occasion.
- **H1 (title rule, 19 Nov 2026):** keyword first, not a question, 60 characters or fewer, no colons, no dashes. Couples experiences used "Couples Experiences Worth Travelling For".
- **The number goes in an H2, not the H1:** `Our <N> <keyword>`. If the task title leads with the number, keep the H1 keyword first and log TITLE-SERIES.
- **SEO title:** the H1 plus a short qualifier, 50 to 60 characters, same rules ("...Around the World").
- **Meta description:** 140 to 155 characters, starts with the keyword, names two contrasting experiences from the list and ends with what each card gives ("with when to go and one honest caveat for each of the <N>").

## Word range and links
- **2,350 to 2,550 reader words** by `build_docx.py --check` (body plus FAQ, excluding front matter, image and CTA markers). Trim repeats before cutting facts.
- About 45 body links: one link to our pages per card (two only where a named venue needs its `/venue` profile link), plus official sources at each claim. Vary the anchors; do not use "More in our..." on more than one card.

## H2 order
1. Intro (no H2, 80 to 140 words): the reader's occasions, the keyword in the first 100 words, three sample experiences, the season and caveat promise, the sibling-page line ("None repeats the [<N> ...](/travel-guides/...)"), and "Sources are current as at <Month Year>."
2. **What makes a <keyword> worth travelling for** (a short test: place, season, privacy; then one line on why we chose these).
3. **Our <N> <keyword>** (one framing line on seasons as tendencies and on Travel advice lines, then H3 groups and bold-led numbered cards; end with the soft CTA line).
4. **Matching an experience to your occasion** (bullets: honeymoon, anniversary, wedding week, proposal; link the occasion and package pages).
5. **The work behind the experience** (the invisible work: seasonal windows, fallback days, transfers, who is on the ground, how money moves), then a separate bold paragraph **Insurance and entry rules (yours to confirm).**
6. **Fitting experiences into a honeymoon or wedding week** (one or two a week, open days, guests as an optional day on the wedding website).
7. **Planning your <keyword> with Wedded Wonderland** (season, place, experience; `/travel`; Concierge Gift line; the confidentiality and 24-hour reply line).
8. **Frequently asked questions** (five H3 questions, answers in front matter `faq` too).
9. `[CTA: discovery_call]` after the last FAQ answer. Never type the CTA heading, body or button into the body; the CMS CTA block carries it.

Key takeaways (five bullets) go in front matter and the CMS Key Takeaways block after the intro. They must not repeat a body sentence word for word.

## Grouping by type
- Group cards under H3 headings by type of experience, not by destination. Default set: Food and wine; Water and islands; Wildlife; Wellness; Culture and place; Adventure; Slow travel.
- A group may hold one card, but no group may be empty; merge or rename it instead. Put a card in the group its sourced facts support (a grand hotel stay is Culture and place, not Wellness, unless the spa is the sourced draw).
- Number the cards `1.` to `<N>.` straight through the groups. Once reviewers refer to cards by number, keep the numbers stable when you move a card.
- Spread destinations: no more than two cards in the same country unless the guide is about that country, and say so in the wedding-week bullet if several cards share a country (couples experiences: "The Tuscany, Amalfi and Lake Como cards all sit within reach of an Italian wedding week").

## Card fields (every card, in this order)
Cards are bold-led paragraphs, not headings: `**<n>. <Experience, place>.**` followed by the fields below.

- **What.** One or two sentences on the experience and why it suits two people, from our page or an official source. No unregistered superlatives.
- **Where.** The destination, inside the title or the first sentence. Only destinations we plan with a live page. Name a hotel or venue only if it has a `/venue` or `/vendor` profile, and link that profile.
- **When (only if sourced).** `**When:**` followed by the months exactly as our guide or an official source words them, attributed in text ("our Bali guide names the dry season, April to October"). If no source gives a season, drop the When line; never fill it from general knowledge. Do not state the same months twice in one card.
- **Caveat.** `**Caveat:**` one honest trade-off (weather, transfers, crowds, length of stay, a season that does not overlap). Official hazards (cyclones, monsoon, heat, avalanches) are linked at the claim to the official page. Our own guide's claims are attributed, not stated as fact.
- **One link to our page.** The destination, honeymoon or venue page, once per card, with varied wording ("per our Fiji guide", "Start with our Lake Como guide", "is the place to start").
- **Travel advice line (card end).** `**Travel advice:**` Smartraveller's overall level for the country at the time of writing, plus any entry rule it names (traveller declaration, mandatory inbound insurance, health restrictions). It is always the last line of the card, so cards never open as warnings. Include it for every country Smartraveller rates above "exercise normal safety precautions", or where an entry rule applies; one framing sentence under the list H2 says these lines give the level at the time of writing, so the phrase is not repeated in each card.
- Image slot marker after selected cards (about seven per guide, hero after the H1), each with a full brief in `image_slots`, including `must_not_show` for anything that belongs to a sibling page.

## Source rules
- Every season, figure, distance and safety line maps to a claim ID and a research fact. No source, no claim: cut it or mark it `[[NEEDS: ...]]` in the draft (never visible in the final).
- **Official sources linked inline at the claim:** Smartraveller for hazards, levels and entry rules; the relevant authority for permits and park or marine rules (for example the Great Barrier Reef Marine Park Authority). Any domain not in `domains.md` needs DOMAINS-ADD approval; say in the open item what to cut if it is refused.
- **Own pages:** attribute in text ("our Oceania honeymoon guide puts..."). If a source page is not in `link-map.md`, attribute it but do not link it (LINK-MAP-ADD).
- **Smartraveller levels:** exact wording, re-checked on the publish date (VERBATIM-RECHECK). Weather extractions are medium confidence until re-checked.
- **Prices:** only if sourced, in the original currency, with the source and date, logged for Nic (NIC-SIGNOFF). Follow the AUD-EXCEPTION ruling in the merged review for conversions. No Concierge prices.
- **Named operators:** none unless they have a `/vendor` profile. Name the experience generically instead and log the operator as an open item (couples experiences: ORIENT-EXPRESS).
- **Entry and legal rules:** the reader confirms them for their own passports with Smartraveller and the embassy or consulate; never the concierge as the authority.
- **Brand facts** only from `brand-profile.md` (one dedicated point of contact, wedding and travel under one roof, deposits, payments and currency across borders, 50,000+ vendors filtered to the ones our team has worked with in-market, Travel and Honeymoon Concierge step). No fees, commission, team hours or in-country staff claims.
- **Never:** em or en dashes; "complimentary"; "most couples"; Wonderland Benefits or eligible-stays perks; weather or availability promises; named planners or people; competitor content or links; a Wedded World plug unless the brief asks for one; DRAFT or unfetched pages (check og:url before linking).

## FAQ set (five questions, FAQPage schema)
1. What are good <keyword> abroad?
2. How far ahead should experiences be booked?
3. Are adventure experiences covered by travel insurance? (Smartraveller, linked)
4. Can experiences be added to a honeymoon package?
5. What is a good experience gift for a couple? (Concierge Gift)

## Open-item checklist (copy into each guide and close what does not apply)
- NEW-URL (URL status, Zoho task and plan ref; CMS slug check)
- TITLE-SERIES (number in the task title vs keyword-first H1)
- SHORTLIST-SWAP (brief items with no research fact, and what replaced them; unused planned links)
- META-CHANGE (meta differs from the brief)
- RETRO-LINK (links to add from sibling guides after publish; DRAFT pages to link once live)
- DOMAINS-ADD (official domains not in `domains.md`, and what to cut if refused)
- LINK-MAP-ADD (source pages not yet in `link-map.md`)
- UNFETCHED-LINKS (pages not linked until og:url is confirmed)
- NIC-SIGNOFF (every figure, currency and source)
- VERBATIM-RECHECK (extracted Smartraveller and weather lines; levels on the publish date)
- OFFICIAL-SOURCE gaps (own-page claims that need an official source before they can be stated as fact, for example STINGER-OFFICIAL)
- PARKS or PERMITS (park, marine or permit rules not researched and so not stated)
- VENUE-NAMING (`/venue` vs `/vendor` profile rule for named hotels)
- OPERATOR names (operators removed for lack of a `/vendor` profile)
- CONCIERGE-PAY and TEAM-LOCATION (reader questions with no brand source)
- PERSONA-WIDEN (until the couple persona covers multi-destination pieces)
- WEDDED-WORLD-RULE (link-map rule 2 vs no Wedded World plug)
- LINK-CHECK (every link on publish day, HTTP 200, og:url, no redirects)
- AUTHOR
- IMAGE-RIGHTS and IMAGE-ASSETS (licences, credits, consent; proposed file names if there is no asset plan)
- CMS-URL (admin URL, category path, Key Takeaways and CTA blocks)

## QA before hand-off
- `python3 blog-team/scripts/build_docx.py --check articles/<folder>/final.md`: reader words in range, 0 em dashes, 0 en dashes, 0 visible placeholders, no blocked domains.
- Sentence-case H2 and H3, Australian spelling, numbers per the style guide, "luxury" no more than twice, no banned words, a Travel advice line at the end of every card that needs one, one link to our pages per card, and the CTA as a block marker only.
