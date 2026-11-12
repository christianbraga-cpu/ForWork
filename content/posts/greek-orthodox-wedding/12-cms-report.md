# CMS report: greek-orthodox-wedding

**Draft URL / ID:** Package ready, not uploaded: no browser in this session; a human saves as Draft and clicks Publish. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-12
- Title: Greek Orthodox Wedding Requirements and Ceremony Explained
- Package: `content/posts/greek-orthodox-wedding/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/greek-orthodox-wedding/11-body.md`
- Booking checklist: `content/posts/greek-orthodox-wedding/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/greek-orthodox-wedding (CMS slug `greek-orthodox-wedding`)
- Primary category: Destination Weddings (= categories[0]); then Greece, Planning Guides; type planning_guide (nearest to "Legal"); cluster Getting Married in Greece
- Redirect: none required (new article). Recommendation only: consider a 301 from /8-symbolic-eastern-orthodox-wedding-traditions-you-might-not-know-about after this post and the traditions guide publish.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, links and UTMs unchanged, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: per 09-cro.json the existing sentence with the "book a Wedded Concierge consultation" link (utm_content=primary) is the CTA, unchanged; the marker is now a `<!-- CTA BLOCK: primary -->` comment
- [x] Secondary, closing and magnet links unchanged and marked with `<!-- CTA INLINE -->` / `<!-- LEAD MAGNET -->` comments; each utm_content appears once in visible links
- [x] No em dashes; Australian English
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (7) extracted from the body only
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] Meta title (58 characters) and meta description (146 characters) from `02-seo.json`; no "best", no prices, no em dashes
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (7)
- [x] Images: 6 slots (featured, documents, stefana, ceremony-detail, island-chapel, venue-chapel), all `needed`
- [x] verify_items and needs_signoff empty: no prices, nothing for Nic to sign off
- [x] draft_note: "DRAFT ONLY. A human clicks Publish", plus image slots, byline and redirect recommendation
- [x] `python3 -I content-system/scripts/validate.py content/posts/greek-orthodox-wedding`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (not checked against the CMS; no browser)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 6; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=greek-orthodox-wedding once the field map is confirmed)

1. Source and upload the 6 images with alt text and captions; set the featured image. featured, island-chapel and venue-chapel must be real, named chapels (media kit with written permission or licensed stock, never AI); documents, stefana and ceremony-detail may be an AI still life only with user approval, captioned "Illustrative image".
2. Enter title, slug `greek-orthodox-wedding`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block at `<!-- CTA BLOCK: primary -->` if the template uses one, and the FAQ (7 pairs).
4. Categories Destination Weddings, Greece, Planning Guides, then set Destination Weddings as the primary category explicitly; add tags.
5. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
6. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
7. Preview desktop and mobile; check links, the CTA and the breadcrumb.

## Publish together

The body links: /expert-advice/greek-wedding-traditions, /destinations/europe/greece, /destination-weddings/greece-wedding-venues, /destination-weddings/santorini-wedding, /destination-weddings/mykonos-wedding and /destination-weddings/rhodes-wedding-venues. Publish them first or together if not yet live, or the links will break.

## Mismatches and open points

- Field map not checked against the CMS (no browser), so no CMS labels could be compared with the package.
- Content type: "Legal" is not a schema value; `planning_guide` used as the nearest.
- Author: no named author in the inputs.
- Image alt, caption, credit and licence: none in `04-images.json`; left empty, not invented.
- Church, Greece-side and chapel items to confirm in writing are in `booking-checklist.md`.
