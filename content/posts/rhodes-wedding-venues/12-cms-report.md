# CMS report: rhodes-wedding-venues

**Draft URL / ID:** Package ready, not uploaded: no browser in this session; a human saves as Draft and clicks Publish. `content-system/cms/field-map.md` is also not confirmed ("NOT YET MAPPED"). Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-12
- Title: 9 Rhodes Wedding Venues From Lindos to Rhodes Town
- Package: `content/posts/rhodes-wedding-venues/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/rhodes-wedding-venues/11-body.md`
- Booking checklist: `content/posts/rhodes-wedding-venues/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/rhodes-wedding-venues (CMS slug `rhodes-wedding-venues`)
- Primary category: Destination Weddings (= categories[0]); then Greece, Venues; type Guide; cluster Getting Married in Greece
- Redirect: none (new article)

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 7 image-slot comments kept, links and UTMs unchanged, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: per 09-cro.json the existing sentence with the "book a Wedded Concierge consultation" link (utm_content=primary) is the CTA, unchanged; the marker is now a `<!-- CTA BLOCK: primary -->` comment
- [x] Secondary, closing and magnet links unchanged and marked with `<!-- CTA INLINE -->` / `<!-- LEAD MAGNET -->` comments; utm_content primary, secondary, closing and magnet each appear once in visible links
- [x] No em dashes; Australian English
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (6) extracted from the body only
- [x] Categories from the brief; primary_category = Destination Weddings; tag "Rhodes Old Town" changed to "Rhodes Town" (no Old Town venue)
- [x] Meta title "9 Rhodes Wedding Venues From Lindos to Rhodes Town" (50 characters); meta description from `02-seo.json` with "the medieval Old Town" replaced by "Rhodes Town", 143 characters, no prices
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (6)
- [x] Images: 7 slots (featured, practical-compare, area-lindos-south-east, area-old-town, area-east-coast, area-west-coast, practical-when-to-marry), all `needed`
- [x] verify_items and needs_signoff empty: no prices, nothing for Nic to sign off
- [x] draft_note: "DRAFT ONLY. A human clicks Publish", plus image slots and byline
- [x] `python3 -I content-system/scripts/validate.py content/posts/rhodes-wedding-venues`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 7; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=rhodes-wedding-venues once the field map is confirmed)

1. Source and upload the 7 images (venue press kits with written permission or licensed stock; never AI, competitor or search-result images), with alt text and captions; set the featured image.
2. Enter title, slug `rhodes-wedding-venues`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block at `<!-- CTA BLOCK: primary -->` if the template uses one, and the FAQ (6 pairs).
4. Categories Destination Weddings, Greece, Venues, then set Destination Weddings as the primary category explicitly; add tags.
5. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
6. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
7. Preview desktop and mobile: the at-a-glance and climate tables must scroll sideways on mobile; check links, the CTA and the breadcrumb.

## Publish together

The body links drafts or pages: /destination-weddings/greece-wedding-venues, /destination-weddings/greece-wedding-packages, /destination-weddings/greece-wedding-packages-all-inclusive and /expert-advice/greek-wedding-traditions. Publish them first or together if not yet live, or the links will break.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- Image area-old-town: the slot brief asks for the Old Town or Rhodes city; use a Rhodes city venue image (no venue is inside the Old Town walls).
- Author: no named author in the inputs.
- Image alt, caption, credit and licence: none in `04-images.json`; left empty, not invented.
- Venue house rules and legal documents to confirm in writing are in `booking-checklist.md`.
