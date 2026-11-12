# CMS report: santorini-or-mykonos-wedding

**Draft URL / ID:** Package ready, not uploaded: no browser in this session; a human saves as Draft and clicks Publish. `content-system/cms/field-map.md` is also not confirmed ("NOT YET MAPPED"). Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-12
- Title: Santorini vs Mykonos for Your Wedding
- Package: `content/posts/santorini-or-mykonos-wedding/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/santorini-or-mykonos-wedding/11-body.md`
- Booking checklist: `content/posts/santorini-or-mykonos-wedding/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/santorini-or-mykonos-wedding (CMS slug `santorini-or-mykonos-wedding`)
- Primary category: Destination Weddings (= categories[0]); then Greece, Planning Guides; type Guide; cluster Getting Married in Greece
- Redirect: none (new article)

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, links and UTMs unchanged, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: per 09-cro.json the existing sentence with the "book a Wedded Concierge consultation" link (utm_content=primary) is the CTA, unchanged; the marker is now a `<!-- CTA BLOCK: primary -->` comment
- [x] Secondary, closing and magnet links unchanged and marked with `<!-- CTA INLINE -->` / `<!-- LEAD MAGNET -->` comments; utm_content primary, secondary, closing and magnet each appear once in visible links
- [x] No em dashes; Australian English
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (5) extracted from the body only
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] Meta title "Santorini or Mykonos Wedding: How the Islands Compare" (53 characters) and meta description (149 characters) from `02-seo.json`; no "best", no prices, no em dashes
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (5)
- [x] Images: 6 slots (featured, santorini-caldera, mykonos-setting, venue-comparison, season, practical), all `needed`
- [x] verify_items and needs_signoff empty: no prices, nothing for Nic to sign off
- [x] draft_note: "DRAFT ONLY. A human clicks Publish", plus image slots and byline
- [x] `python3 -I content-system/scripts/validate.py content/posts/santorini-or-mykonos-wedding`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 6; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=santorini-or-mykonos-wedding once the field map is confirmed)

1. Source and upload the 6 images (venue press kits with written permission or licensed stock; never AI, competitor or search-result images), with alt text and captions; set the featured image. The featured split hero is two licensed photos, each with its own credit.
2. Enter title, slug `santorini-or-mykonos-wedding`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block at `<!-- CTA BLOCK: primary -->` if the template uses one, and the FAQ (5 pairs).
4. Categories Destination Weddings, Greece, Planning Guides, then set Destination Weddings as the primary category explicitly; add tags.
5. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
6. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
7. Preview desktop and mobile: the at-a-glance and Naxos climate tables must scroll sideways on mobile; check links, the CTA and the breadcrumb.

## Publish together

The body links: /destination-weddings/santorini-wedding-venues, /destination-weddings/mykonos-wedding-venues, /destination-weddings/santorini-wedding, /destination-weddings/mykonos-wedding, /destination-weddings/greece-wedding-venues, /destinations/europe/greece and /expert-advice/greek-wedding-traditions. Publish them first or together if not yet live, or the links will break.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- Secondary CTA anchor: 09-cro.json describes it as "ask a Wedded Advisor to test your island", but the final copy reads "book a Wedded Concierge consultation" (same text as the primary). Left unchanged; an editor may want distinct anchor text.
- Author: no named author in the inputs.
- Image alt, caption, credit and licence: none in `04-images.json`; left empty, not invented.
- Venue house rules and legal documents to confirm in writing are in `booking-checklist.md`.
