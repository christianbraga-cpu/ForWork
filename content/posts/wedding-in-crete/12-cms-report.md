# CMS report: wedding-in-crete

**Draft URL / ID:** Not uploaded: no browser connection in this session and the CMS field map is not yet confirmed (run /wedded-cms-discovery locally)

- Date: 2026-11-11
- Title: Wedding in Crete Guide to Seasons, Venues and Costs
- Package: `content/posts/wedding-in-crete/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/wedding-in-crete/11-body.md`
- Booking checklist: `content/posts/wedding-in-crete/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/wedding-in-crete (CMS slug `wedding-in-crete`)
- Primary category: Destination Weddings (= categories[0]); type Guide; cluster Getting Married in Greece
- New article, no redirect

## Package build (Part 1)

- [x] Confirmed `08-final.md` already carries the `09-cro.json` copy change (secondary lead-in now "When you are ready to settle the season, the venue and the guest rooms")
- [x] Body built from `08-final.md`: front matter removed, all `<!-- fact_xx -->` and `<!-- crete-venues fact_xx -->` markers removed, 6 image-slot comments kept, the one `[[VERIFY]]` marker kept (Elounda Collection lead times, "A planning timeline")
- [x] Primary CTA block (Speak with a Wedded Advisor, subtext "The fee is agreed in writing before any work begins.") at the `<!-- CTA: primary -->` marker; the inline sentence after it retagged `utm_content=inline` (as the Greece packages model); secondary, lead magnet and closing links marked with comments; each `utm_content` link appears once as a link
- [x] Key takeaways: exactly the 4 in the body, copied verbatim; FAQ (6) extracted
- [x] Categories: Destination Weddings, Greece, Crete, Planning Guides; primary_category = Destination Weddings; tags (8) from the brief
- [x] Meta title ("Wedding in Crete: Seasons, Venues and Cost Drivers") and description, focus keyword "wedding in crete", canonical, OG image slot (featured)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (6)
- [x] Images: 6 slots in the body (featured, seasons, choosing-area, costs, getting-there, timeline), all `needed`
- [x] verify_items: the Elounda Collection 2027 lead times plus image credits and licences (6); needs_signoff empty (no prices)
- [x] draft_note: VERIFY item, image slots, linked drafts to publish together, keyword split, mobile scrolling for the five-column climate table, deferred business items
- [x] redirects_recommended: none (new article)
- [x] No em dashes
- [x] `python3 -I content-system/scripts/scan_copy.py content/posts/wedding-in-crete/11-body.md`: no banned words, 0 dashes, no overlaps; flagged "exclusive" 6 times (exclusive use is a cost driver the section covers; no change made)
- [x] `python3 -I content-system/scripts/validate.py content/posts/wedding-in-crete`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 6 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture. When it is, check on mobile that the five-column climate table scrolls sideways rather than squashing.

## Publish together

The body links four drafts: /destination-weddings/crete-wedding-venues (twice), /destination-weddings/greece-wedding-packages (once), /destination-weddings/greece-wedding-venues (twice, once with the #getting-legally-married-in-greece-as-australians-in-brief anchor) and /expert-advice/greek-wedding-traditions (once). Publish them with this post, or hold this post until they are live. Check the Greece guide anchor lands in preview.

## Keyword split (recommendation only, nothing on the live site changes)

From `02-seo.json`: this guide owns "wedding in crete", "crete wedding", "getting married in crete", "destination wedding crete", "best time to get married in crete", "crete wedding season", "crete wedding cost" and "wedding crete greece". The Crete venues guide owns "crete wedding venues", "best wedding venues in crete", luxury and beach venue queries and venue names, and should not use "wedding in crete" in its title, H1 or meta. The Greece packages guide owns "crete wedding packages" / "wedding in crete packages". The Greece venues guide owns Greece-wide venue and legal queries; the hub keeps Greece-wide terms. No weddedwonderland.com page currently ranks for any Crete query.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- `[[VERIFY]]`: Elounda Collection document lead times (2025 PDF) must be confirmed for 2027 dates before publishing; remove the marker once confirmed.
- Title vs keyword split: `02-seo.json` says this guide keeps "venue" out of its title and H1, but the person's fixed title contains "Venues". Title kept as given; confirm.
- Author: no named author in the inputs; package uses "Wedded Wonderland" pending confirmation.
- Excerpt is the first two sentences of the opening paragraph, verbatim (the first sentence alone does not carry the focus keyword).
- Image alt, caption, credit and licence: none supplied in `04-images.json`; left empty, not invented. costs and timeline may be AI only on the person's approval and captioned "Illustrative image"; seasons and getting-there are destination images and never AI.
- Booking checklist items flagged for confirmation before quoting: Elounda Collection 2027 lead times and 40-day registration, Abaton 2027 terms, Sea View later finish and any charge, St. Nicolas Bay and Caramel capacity, plus transfers for guests who won't drive, step-free access, whole-property closure, deposits and cancellation at every venue.
- Deferred business items (person's decision): fee model and commissions, whether the first step is a free call with a real person, work with couples outside Australia, a real Crete wedding to show, a named Wedded Advisor or phone line.

## Next step

Run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS, confirm the field map, then `/wedded-blog resume=wedding-in-crete`. Nothing was published or scheduled.
