# CMS report: oceania-wedding-destinations

**Draft URL / ID:** Not uploaded. Package-only mode: the person uploads the post from the Word doc. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not CONFIRMED). Nothing was saved, scheduled or published in the CMS. A human saves as Draft; a human clicks Publish.

**After saving the draft, check the URL is exactly https://weddedwonderland.com/destination-weddings/oceania-wedding-destinations (path `/destination-weddings/oceania-wedding-destinations`). The category bug has moved earlier posts. If it differs, do not publish; fix the primary category or confirm with the dev team first.**

**Anchor check:** the H2 "Oceania wedding destinations at a glance" must produce the anchor `#oceania-wedding-destinations-at-a-glance`, because the last Key takeaways bullet links to it ("the at-a-glance table"). Check it in preview. If the CMS gives the heading a different ID (or none), remove that link rather than leaving a dead jump link.

**Recheck at publication:** every Smartraveller line is dated "As at November 2026" (cyclone months for seven Pacific entries, the Fiji National State of Disaster and water rationing, the Vanuatu Santo airport restriction, the New Caledonia advice level and update quotes, the Samoa dengue outbreak, the Tonga cyclone outlook, and the getting married overseas advice). Recheck each one on the day of publication. Also confirm the [Cook Islands Ministry of Justice marriage licence page](https://www.justice.gov.ck/marriage-license/) is still current: its page metadata says it was last modified on 17 October 2022 (`03-source-pack.json`), so confirm the notice, three-day and three-month rules with the Ministry if the page is unchanged or unclear.

**Legal content** is general information as at November 2026, not legal advice (the body says so in "Legal or symbolic ceremony").

- Date: 2026-11-26
- Plan ref: WW-303
- Title / H1: Oceania Wedding Destinations From Fiji to Tahiti (48 characters)
- Meta title: Oceania Wedding Destinations From Fiji to Tahiti (48)
- Meta description: Oceania wedding destinations from Fiji and Vanuatu to Tahiti, the Cook Islands, Hawaii and New Zealand, with cyclone season and legal or symbolic options. (154, from `02-seo.json`)
- Focus keyword: oceania wedding destinations
- Package: `content/posts/oceania-wedding-destinations/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/oceania-wedding-destinations/11-body.md`
- Booking checklist: `content/posts/oceania-wedding-destinations/booking-checklist.md`
- Target URL: /destination-weddings/oceania-wedding-destinations (slug `oceania-wedding-destinations`); canonical https://weddedwonderland.com/destination-weddings/oceania-wedding-destinations
- Categories: Destination Weddings (primary, = categories[0], set explicitly), Planning Guides. No "Latin America & Caribbean" or "Africa" category.
- **Oceania category: unconfirmed.** Whether an "Oceania" category exists in the CMS has not been checked (field map not mapped). It is not assigned; do not create one. "Oceania" is a tag only.
- Status: Draft only. Never Publish or Schedule.
- New article; no redirect.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter and META comments removed, H1 is the title, all `<!-- fact_xx -->` markers removed, 7 image-slot comments kept, prose unchanged (diff against `08-final.md` minus those items is identical)
- [x] All 44 links and the 4 UTM links kept exactly as in `08-final.md`, same order; internal links relative; no `/destinations/africa` or `/destinations/latin-america-caribbean` link
- [x] Two LINK comments kept: `<!-- LINK: /destination-weddings/wedding-destinations-november when live -->` (How we chose these Oceania destinations) and `<!-- LINK: /expert-advice/samoan-wedding-traditions when live -->` (Samoa entry). Add each link when the page is live.
- [x] No `<!-- CTA: primary -->` marker in `08-final.md`, so nothing replaced; no CTA marker comments added. CTA links in place per `09-cro.json`: primary (after the at-a-glance table), secondary, magnet, closing; each utm_content appears once
- [x] No `[[VERIFY]]` markers in the copy (none in `08-final.md`)
- [x] Key takeaways (4) and FAQ (5) taken verbatim from the body
- [x] Excerpt: first sentence of each of the two opening paragraphs, verbatim (236 characters). The full opening paragraph is 327 characters, over the schema's 300 limit.
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (5)
- [x] Images: 7 slots, all `needed`; alt and caption left empty (nothing invented); no AI images
- [x] No prices; needs_signoff empty (nothing for Nic)
- [x] draft_note: "DRAFT. Do not publish until checked:" + image slots, licence question, lagoon placement, anchor check, LINK comments, URL check, Smartraveller and Cook Islands rechecks, legal note, byline
- [x] No em dashes; Australian English
- [x] `python3 -I content-system/scripts/validate.py content/posts/oceania-wedding-destinations`: All valid (14 stage files)

## CMS checklist (Part 2: not run, package-only mode)

- [ ] `cms/field-map.md` status is CONFIRMED (it says NOT YET MAPPED)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 7)
- [ ] Upload: not started (the person uploads via the Word doc)
- [ ] After save: not started

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person)

1. Source and upload the 7 images with alt text and captions; set the featured image (see Images below).
2. Title, slug `oceania-wedding-destinations`, excerpt, author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md` (or the Word doc); fill the Key Takeaways block (4) and the FAQ (5). Use the CTA links as they are in the body; don't add a second primary CTA link.
4. Categories Destination Weddings and Planning Guides, then **set Destination Weddings as the primary category explicitly**; add tags. Don't add an Oceania category.
5. SEO: meta title, meta description, focus keyword, canonical, OG image (featured); schema JSON-LD if the CMS has a field.
6. Paste `draft_note` into the internal note field, then **Save Draft**. Never Publish or Schedule.
7. **Check the URL** is exactly /destination-weddings/oceania-wedding-destinations.
8. Preview desktop and mobile: images, links, CTA, breadcrumb (Home > Destination Weddings > post), the Key takeaways jump link to `#oceania-wedding-destinations-at-a-glance`, and the 5-column at-a-glance table (10 rows) on mobile.
9. On publication day: recheck the Smartraveller lines and the Cook Islands Ministry of Justice page (see above).

## Images (7 slots, all needed)

| Slot | Role | Sits in | Rule |
|---|---|---|---|
| featured | featured | Under the H1 | South Pacific island beach or lagoon ceremony setup at a listed destination; 16:9 with room for a title overlay |
| melanesia | inline | Opening "Melanesia wedding destinations" | Location verified as Fiji, never inferred from appearance |
| polynesia | inline | Opening "Polynesia wedding destinations" | Any listed Polynesian island; licensed stock with location in the register (Hawaii is the only Polynesia entry with our guide) |
| lagoon | inline | Tahiti and French Polynesia entry | `04-images.json` allows Tahiti, Bora Bora or Rarotonga. Use a French Polynesia image here, or move the slot to the Cook Islands entry if the image shows Rarotonga. Island named only as the register or EXIF records it |
| new-zealand | inline | Opening "New Zealand for a lake or vineyard wedding" | New Zealand lakeside, lodge lawn or vineyard; matches our New Zealand guide |
| australia | inline | Opening "An Australian island wedding" | Location verified as the Queensland islands, never inferred from appearance |
| planning | inline | "What to plan for a wedding in the Pacific" | Flat-lay, no real place; owned, licensed or Canva brand asset. Not generated; AI illustrative only with orchestrator approval and an "illustrative" label |

- Every place image shows a real destination: licensed or owned only, **never AI**, location proven by register row, EXIF or source page.
- Month taken recorded for every place image; no season, wet season, dry season or cyclone wording in any caption (weather stays in the copy).
- People only with written couple and guest consent.
- **Own-site gallery licence (open question):** the Fiji venue galleries and the Hayman Island guide imagery on weddedwonderland.com may be used only if the partner agreements allow blog use. Not confirmed; images not viewed or location-verified.

## Mismatches and open points

- Field map not mapped, so no CMS labels could be compared with the package. Run `/wedded-cms-discovery` before any automated upload.
- Oceania category: existence unconfirmed (see above).
- `04-images.json` is still `needs_input`; its lagoon slot left the H3 open (planner-sme question). Re-run stage 04 once photos exist.
- The New Zealand source link is `https://niwa.co.nz/climate-and-weather/monthly/climate-summary-november-2025` with the anchor "Earth Sciences New Zealand's summary of that month". Kept as written; check it resolves in preview.
- Backlinks to add (from `02-seo.json`): `/destinations/oceania` hub (carries its own VERIFY on the hub sentence), `/destinations/oceania/fiji`, `/destination-weddings/get-married-in-new-zealand` and `/destination-weddings/getting-married-in-hawaii` (both carry a VERIFY on the placement sentence).
- Author: no named author in any input.
- Breadcrumb level 2 uses https://weddedwonderland.com/destination-weddings; confirm the category archive URL.
- `10-distribution.json`: pins, carousel and newsletter image are on hold until the images are licensed and approved; Pinterest board names to confirm.
- `09-cro.json` open questions (fee model, commissions, deposits, a first phone call, on-the-day contact, security and confidentiality) are for /wonderland-concierge, not this post.
- Questions for couples are in `booking-checklist.md` and don't block publishing.
