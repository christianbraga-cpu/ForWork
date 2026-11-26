# CMS report: garden-wedding

**Draft URL / ID:** Not uploaded. Package-only mode: the person uploads the post from the Word doc. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not CONFIRMED). Nothing was saved, scheduled or published in the CMS. A human saves as Draft; a human clicks Publish.

**After saving the draft, check the URL is exactly https://weddedwonderland.com/real-weddings/garden-wedding (path `/real-weddings/garden-wedding`). The CMS category bug has moved earlier posts. If it differs, do not publish; fix the primary category or confirm with the dev team first.**

**Real wedding cards: confirm before publishing.** The eight cards under "Real garden weddings from our pages" are text summaries of our own published stories, each linked to the full story. `content-system/brand/brand-facts.md` lists "Real weddings we can feature (with consent)" as deferred, so a person should confirm the eight couples may be featured on this page before publishing. Cards run text-only: an image goes on a card only if it comes from that same wedding's gallery and the register shows the licence and couple consent. Never AI for a real wedding or venue.

**Paige and Todd:** their story URL slug (`/an-autumn-garden-wedding-at-burnham-grove-estate`) contains a venue name. It appears only as the link address; the anchor and copy use the couple's names. Confirm that is acceptable, and keep the venue name out of the card's image file name if an image is added.

- Date: 2026-11-26
- Plan ref: none in any input (calendar.csv row 99)
- Title / H1: Garden Wedding Ideas and What to Plan For (41 characters)
- Meta title: Garden Wedding Ideas and What to Plan For (41)
- Meta description: Garden wedding ideas from our own real garden weddings, with styling for aisles, long tables and dusk lighting, plus the questions to ask your venue first. (155, from `02-seo.json`)
- Focus keyword: garden wedding
- Package: `content/posts/garden-wedding/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/garden-wedding/11-body.md`
- Booking checklist: `content/posts/garden-wedding/booking-checklist.md`
- Target URL: /real-weddings/garden-wedding (slug `garden-wedding`); canonical https://weddedwonderland.com/real-weddings/garden-wedding
- Categories: Real Weddings (primary, = categories[0], set explicitly), Style Advice, Destination Weddings
- Tags: garden wedding, garden party wedding, outdoor wedding, wedding styling, wet weather plan, real weddings
- Status: Draft only. Never Publish or Schedule.
- New article; no redirect.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter and META comments removed, H1 is the title, all 6 `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, prose unchanged (diff against `08-final.md` minus those items is identical)
- [x] All 25 links and the 4 UTM links kept exactly as in `08-final.md`, same order; internal links relative (2 external: Cancer Council sun safety, SA MFS candle fact sheet); no `/destinations/africa` or `/destinations/latin-america-caribbean` link
- [x] Three LINK comments kept in "Destination garden weddings": `<!-- LINK: /destination-weddings/wedding-destinations-november when live -->`, `<!-- LINK: /destination-weddings/oceania-wedding-destinations when live -->`, `<!-- LINK: /destination-weddings/wedding-destinations-march when live -->` (all 404 on 2026-11-26). Add each link when the page is live.
- [x] No `<!-- CTA: primary -->` marker in `08-final.md`, so nothing replaced; no CTA marker comments added. CTA links in place per `09-cro.json`: magnet (end of "The garden party wedding feel"), primary (end of "Garden protection rules"), secondary (end of "Destination garden weddings"), closing; each utm_content appears once
- [x] No `[[VERIFY]]` markers in the copy (none in `08-final.md`)
- [x] Key takeaways (4) and FAQ (5) taken verbatim from the body
- [x] Excerpt: the opening paragraph, verbatim (248 characters)
- [x] Categories and tags from the brief; primary_category = Real Weddings
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Real Weddings > post) + FAQPage (5)
- [x] Images: 6 slots, all `needed`; alt and caption left empty (nothing invented); no AI images
- [x] No prices; needs_signoff empty (nothing for Nic)
- [x] draft_note: "DRAFT. Do not publish until checked:" + image slots, real wedding consent, Paige and Todd slug, LINK comments, URL check, byline
- [x] No em dashes; Australian English
- [x] `python3 -I content-system/scripts/validate.py content/posts/garden-wedding`: All valid (14 stage files)

## CMS checklist (Part 2: not run, package-only mode)

- [ ] `cms/field-map.md` status is CONFIRMED (it says NOT YET MAPPED)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 6)
- [ ] Upload: not started (the person uploads via the Word doc)
- [ ] After save: not started

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person)

1. Confirm the eight real wedding couples may be featured (see above).
2. Source and upload any approved images with alt text and captions; set the featured image (see Images below). If none are approved, the cards run text-only.
3. Title, slug `garden-wedding`, excerpt, author (byline to confirm; package uses "Wedded Wonderland").
4. Paste the body from `11-body.md` (or the Word doc); fill the Key Takeaways block (4) and the FAQ (5). Use the CTA links as they are in the body; don't add a second primary CTA link.
5. Categories Real Weddings, Style Advice and Destination Weddings, then **set Real Weddings as the primary category explicitly**; add tags.
6. SEO: meta title, meta description, focus keyword, canonical, OG image (featured); schema JSON-LD if the CMS has a field.
7. Paste `draft_note` into the internal note field, then **Save Draft**. Never Publish or Schedule.
8. **Check the URL** is exactly /real-weddings/garden-wedding.
9. Preview desktop and mobile: images, links (the eight story links, the two external sources), CTA, breadcrumb (Home > Real Weddings > post).

## Images (6 slots, all needed)

| Slot | Role | Sits in | Rule |
|---|---|---|---|
| featured | featured | Under the H1 | Garden ceremony aisle set for guests; 16:9 with room for a title overlay; no identifiable guests or children without consent |
| real-wedding-cards | inline | "Real garden weddings from our pages" | One image per card, only from that same wedding's licensed gallery, with wedding_id, licence, credit and couple_consent = yes in the register; otherwise text-only. Never a stand-in |
| floral-arch | inline | "Aisles and arches" | Arch at the end of a grass or gravel aisle; flowers by colour and form only |
| long-table | inline | "Long tables and linen" | Long garden banquet table, no people |
| dusk-lighting | inline | "Lighting for dusk" | Festoon lights, lanterns or candles at dusk; time of day from EXIF or register |
| wet-weather-plan | inline | "Wet weather plan and covered space" | Marquee or covered pavilion; no hire branding; must not imply a specific venue offers it |

- Licensed or owned only, registered in `library-index.csv` (0 rows today); **never AI** for a real wedding or venue; competitor or search images only to `reference-only/`.
- No season or flower variety wording in any caption unless a post source states it.
- People only with written couple and guest consent; no children unless consent is recorded.

## Mismatches and open points

- Field map not mapped, so no CMS labels could be compared with the package. Run `/wedded-cms-discovery` before any automated upload.
- Real-wedding features need consent per brand-facts (deferred); see above.
- Paige and Todd story slug contains a venue name; see above.
- `04-images.json` is still `needs_input` (register empty). Re-run stage 04 once images or consent exist.
- Author: no named author in any input.
- Breadcrumb level 2 uses https://weddedwonderland.com/blog/real-weddings (the live real weddings listing in `link-map.csv`); confirm the category archive URL the CMS outputs.
- `link-map.csv` is stale per `02-seo.json` (the Tommy Winkler and Jessica Pappas root URL now redirects to `/trending/`; 7 garden real weddings missing). Suggest `/wedded-linkmap`.
- Backlinks to add (from `02-seo.json`): `/style-advice/wedding-table-decor`, `/real-weddings/beach-wedding`, `/trending/tommy-winkler-jessica-pappas-european-garden-inspired-wedding`, `/style-advice/wedding-centrepieces`.
- `10-distribution.json`: pins, carousel and newsletter image are on hold until images are licensed (with a scope covering social use) and approved; Pinterest boards "Garden Weddings" and "Wedding Ceremony Ideas" may need creating.
- `09-cro.json` open questions (fee model, commissions, deposits, a first phone call, on-the-day contact, Advisor identity, scale, confidentiality) are for /wonderland-concierge, not this post. Its suggested printable lead magnet is the basis of `booking-checklist.md`, not placed on the site.
- Questions for couples are in `booking-checklist.md` and don't block publishing.
