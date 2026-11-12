# CMS report: santorini-wedding-venues

**Draft URL / ID:** Not uploaded. FAST MODE, package only: no browser connection in this session and `content-system/cms/field-map.md` is not confirmed ("NOT YET MAPPED"). Stopped at the package. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-12
- Title: 13 Best Santorini Wedding Venues With Caldera Views (13 venues qualified; changed from 15)
- Package: `content/posts/santorini-wedding-venues/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/santorini-wedding-venues/11-body.md`
- Booking checklist: `content/posts/santorini-wedding-venues/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/santorini-wedding-venues (CMS slug `santorini-wedding-venues`)
- Primary category: Destination Weddings (= categories[0]); then Greece, Venues; type Guide; cluster Getting Married in Greece
- Redirect: 301 from /7-must-see-santorini-destination-wedding-venues recommended (the person's call, see below)

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 7 image-slot comments kept, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA block (Speak with a Wedded Advisor, subtext "The fee is agreed in writing before any work begins.") at the `<!-- CTA: primary -->` marker; the inline Wedded Concierge sentence after it retagged `utm_content=inline`, as in the Mykonos model
- [x] Secondary, closing and magnet links unchanged and marked with `<!-- CTA INLINE -->` / `<!-- LEAD MAGNET -->` comments; utm_content primary, inline, secondary, closing and magnet each appear exactly once in visible links
- [x] No em dashes; no "Wonderland Concierge" in visible text (anchors name Wedded Concierge)
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (9) extracted verbatim
- [x] Categories from the brief; primary_category = Destination Weddings; tags from the brief minus Fira (no Fira venue)
- [x] Meta title "13 Santorini Wedding Venues With Caldera Views" (no "Best"); meta description from `02-seo.json` with Fira dropped, 145 characters, no prices
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + ItemList (13 venues, official URLs) + FAQPage (9)
- [x] Images: 7 slots in the body (featured, practical-compare, 4 areas, practical-when-to-marry), all `needed`. `04-images.json` slot area-fira is not in the body and was left out of the package
- [x] verify_items and needs_signoff empty (no prices in the copy)
- [x] draft_note: "DRAFT ONLY. A human clicks Publish", plus image slots, byline and the redirect decision
- [x] `python3 -I content-system/scripts/validate.py content/posts/santorini-wedding-venues`: All valid
- [x] `python3 -I content-system/scripts/scan_copy.py content/posts/santorini-wedding-venues/11-body.md`: no banned words, 0 dashes, no overlaps; flagged "exclusive" 21 and "luxury" 2 (expected in a venue guide comparing exclusive use; "luxury" is in venue names and descriptions)

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 7; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=santorini-wedding-venues once the field map is confirmed)

1. Run `/wedded-cms-discovery` in a Chrome tab where you are logged into the CMS, and confirm the field map.
2. Source and upload the 7 images (venue press kits with written permission or licensed stock; never AI, competitor or search-result images), with alt text and captions; set the featured image.
3. Enter title, slug `santorini-wedding-venues`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
4. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the primary CTA block at the `<!-- CTA BLOCK: primary -->` marker, and the FAQ (9 pairs).
5. Categories Destination Weddings, Greece, Venues, then set Destination Weddings as the primary category explicitly; add tags.
6. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
7. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
8. Preview desktop and mobile: the 5-column at-a-glance table must scroll sideways on mobile; check links, the CTA block and the breadcrumb.

## Redirect (the person's call)

Recommended: a 301 from `/7-must-see-santorini-destination-wedding-venues` to `/destination-weddings/santorini-wedding-venues` at publish. The old page targets the same keyword and ranks about #90 to #97 in Australia and falling. Also, the Santorini planning guide draft (/destination-weddings/santorini-wedding) links the old page once in Step 3; point that link here instead (not changed by this run).

## Publish together

The body links drafts: /destination-weddings/santorini-wedding, /destination-weddings/greece-wedding-venues, /destination-weddings/greece-wedding-packages, /destination-weddings/mykonos-wedding-venues, /destination-weddings/paros-wedding-venues and /expert-advice/greek-wedding-traditions. Publish them first or together, or the links will break.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- No `[[VERIFY]]` markers in the copy; image credits and licences (7 slots) are the only publishing blockers.
- Author: no named author in the inputs.
- Image alt, caption, credit and licence: none in `04-images.json`; left empty, not invented.
- H1 keeps "Best" as the person gave it; the copy makes no ranking claim and the meta title drops it.
- Venue details to confirm in writing before quoting are in `booking-checklist.md` (Canaves capacity conflict, Le Ciel and Venetsanos locations, Andronis wedding property, civil marriage with the Municipality of Thira).
