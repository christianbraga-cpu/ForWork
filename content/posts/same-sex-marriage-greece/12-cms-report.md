# CMS report: same-sex-marriage-greece

**Draft URL / ID:** Package ready, not uploaded: no browser in this session; a human saves as Draft and clicks Publish. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-12
- Title: Same-Sex Marriage in Greece and What Couples Need
- Package: `content/posts/same-sex-marriage-greece/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/same-sex-marriage-greece/11-body.md`
- Booking checklist: `content/posts/same-sex-marriage-greece/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/same-sex-marriage-greece (CMS slug `same-sex-marriage-greece`)
- Primary category: Destination Weddings (= categories[0]); then Greece, Planning Guides; type planning_guide (nearest to "Legal"); cluster Getting Married in Greece
- Redirect: none (new article).

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, links and UTMs unchanged, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: per 09-cro.json the existing sentence with the "book a Wedded Concierge consultation" link (utm_content=primary) after the Key takeaways is the CTA, unchanged; marked `<!-- CTA BLOCK: primary -->` (08-final.md had no `<!-- CTA: primary -->` marker to replace)
- [x] Secondary, closing and magnet links unchanged and marked with `<!-- CTA INLINE -->` / `<!-- LEAD MAGNET -->` comments; each utm_content appears once in visible links
- [x] No em dashes; Australian English
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (7) extracted from the body only
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] Meta title (49 characters) and meta description (151 characters) from `02-seo.json`; no "best", no prices, no em dashes
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (7)
- [x] Images: 6 slots (featured, documents, travel-planning, island-setting, venue-terrace, reception-table), all `needed`
- [x] verify_items and needs_signoff empty: no prices, nothing for Nic to sign off
- [x] draft_note: "DRAFT. Do not publish until checked", plus image slots, legal-status recheck, byline, "A human clicks Publish"
- [x] `python3 -I content-system/scripts/validate.py content/posts/same-sex-marriage-greece`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (not checked against the CMS; no browser)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 6; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=same-sex-marriage-greece once the field map is confirmed)

1. Source and upload the 6 images with alt text and captions; set the featured image. featured, island-setting, venue-terrace and reception-table must be real, named places (media kit with written permission or licensed stock, never AI; people only with written couple and guest consent); documents and travel-planning may be an AI still life only with user approval, captioned "Illustrative image".
2. Enter title, slug `same-sex-marriage-greece`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block at `<!-- CTA BLOCK: primary -->` if the template uses one, and the FAQ (7 pairs).
4. Categories Destination Weddings, Greece, Planning Guides, then set Destination Weddings as the primary category explicitly; add tags.
5. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
6. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
7. Preview desktop and mobile; check links, the CTA and the breadcrumb.

## Publish together

The body links: /expert-advice/where-can-same-sex-couples-legally-marry-abroad, /destinations/europe/greece, /destination-weddings/greece-wedding-venues, /destination-weddings/santorini-wedding, /destination-weddings/mykonos-wedding, /destination-weddings/rhodes-wedding-venues and /destination-weddings/greek-orthodox-wedding. Publish them first or together if not yet live, or the links will break.

## Mismatches and open points

- Field map not checked against the CMS (no browser), so no CMS labels could be compared with the package.
- Content type: "Legal" is not a schema value; `planning_guide` used as the nearest.
- Author: no named author in the inputs.
- 09-cro.json refers to a `<!-- CTA: primary -->` marker after the venue questions; 08-final.md has none. CTA block placed after the Key takeaways with the existing primary link.
- 02-seo.json asks the planner SME to reconfirm the legal-status claim live from an official source before publish.
- Image alt, caption, credit and licence: none in `04-images.json`; left empty, not invented.
- Legal and venue items to confirm in writing are in `booking-checklist.md`.
