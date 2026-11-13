# CMS report: best-time-to-get-married-in-greece

**Draft URL / ID:** Package ready, not uploaded: no browser in this session; a human saves as Draft and clicks Publish. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-13
- Title: Best Time to Get Married in Greece by Month
- Package: `content/posts/best-time-to-get-married-in-greece/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/best-time-to-get-married-in-greece/11-body.md`
- Booking checklist: `content/posts/best-time-to-get-married-in-greece/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/best-time-to-get-married-in-greece (CMS slug `best-time-to-get-married-in-greece`)
- Primary category: Destination Weddings (= categories[0]); then Greece, Planning Guides; type planning_guide (Guide); cluster Getting Married in Greece
- Redirect: none (new article).

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, links and UTMs unchanged, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: the existing sentence after the Key takeaways (utm_content=primary) is unchanged and marked `<!-- CTA INLINE: primary -->`; the CMS CTA block is marked `<!-- CTA BLOCK: primary -->` after the month scenarios, per 09-cro.json (08-final.md had no `<!-- CTA: primary -->` marker to replace)
- [x] Secondary, closing and magnet links unchanged and marked; each utm_content appears once in visible links
- [x] No em dashes; Australian English
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (4) extracted from the body only
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] Meta title (43 characters) and meta description (147 characters) from `02-seo.json`; no prices, no em dashes
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (4)
- [x] Images: 6 slots (featured, planning-still-life, spring-setting, high-summer-setting, autumn-setting, green-season-ionian-crete), all `needed`
- [x] verify_items and needs_signoff empty: no prices, nothing for Nic to sign off
- [x] draft_note: "DRAFT. Do not publish until checked", plus image slots, mobile table scroll, byline, "A human clicks Publish"
- [x] `python3 -I content-system/scripts/validate.py content/posts/best-time-to-get-married-in-greece`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (not checked against the CMS; no browser)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 6; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=best-time-to-get-married-in-greece once the field map is confirmed)

1. Source and upload the 6 images with alt text and captions; set the featured image. featured, spring-setting, high-summer-setting, autumn-setting and green-season-ionian-crete must be real, named venues with the month proven by register row, media kit or EXIF (never AI; people only with written couple and guest consent); planning-still-life may be an AI still life only with user approval, captioned "Illustrative image".
2. Enter title, slug `best-time-to-get-married-in-greece`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block at `<!-- CTA BLOCK: primary -->` if the template uses one, and the FAQ (4 pairs).
4. Categories Destination Weddings, Greece, Planning Guides, then set Destination Weddings as the primary category explicitly; add tags.
5. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
6. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
7. Preview desktop and mobile; check links, the CTA, the breadcrumb and the month table.

## Mobile: month table

The month table ("Greece wedding weather by month, April to October") has 6 columns (month plus 5 stations) and needs horizontal scroll on mobile. Wrap it in a horizontally scrollable container (or use the CMS's responsive table option) so the page itself does not scroll sideways, and check it in the mobile preview. The Kerkyra April cell is blank by design (Kerkyra is shown for May to October only).

## Publish together

The body links: /destination-weddings/greece-wedding-venues, /destination-weddings/greek-orthodox-wedding, /destination-weddings/santorini-wedding, /destination-weddings/mykonos-wedding, /destination-weddings/santorini-wedding-venues, /destination-weddings/mykonos-wedding-venues, /destination-weddings/paros-wedding-venues, /destination-weddings/wedding-in-crete, /destination-weddings/crete-wedding-venues, /destination-weddings/rhodes-wedding-venues, /destination-weddings/corfu-wedding-venues and /destinations/europe/greece. Per 02-seo.json, greece-wedding-venues and greek-orthodox-wedding are drafts: publish them first or together, or those links will break.

## Mismatches and open points

- Field map not checked against the CMS (no browser), so no CMS labels could be compared with the package.
- Author: no named author in the inputs.
- 09-cro.json refers to a `<!-- CTA: primary -->` marker after the month scenarios; 08-final.md has none. The CTA block is marked at that position.
- External links (HNMS, Smartraveller, Archdiocese) not yet set verified_live in 02-seo.json; planner SME to recheck before publish.
- Image alt, caption, credit and licence: none in `04-images.json`; left empty, not invented.
- Venue season dates, Orthodox dates and public holidays to confirm for a couple's date are in `booking-checklist.md`.
