# CMS report: greece-wedding-packages-all-inclusive

**Draft URL / ID:** Not uploaded. FAST MODE, package only: no browser connection in this session and `content-system/cms/field-map.md` is not confirmed ("NOT YET MAPPED"). Stopped at the package. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-12
- Title: All-Inclusive Greece Wedding Packages Compared
- Package: `content/posts/greece-wedding-packages-all-inclusive/11-publish-package.json` (status `draft`)
- Body: `content/posts/greece-wedding-packages-all-inclusive/11-body.md`
- Booking checklist: `content/posts/greece-wedding-packages-all-inclusive/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/greece-wedding-packages-all-inclusive (CMS slug `greece-wedding-packages-all-inclusive`)
- Primary category: Destination Weddings (= categories[0]); then Greece, Planning Guides; type Comparison; cluster Getting Married in Greece

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA block (Speak with a Wedded Advisor, subtext "Quotes in AUD, inclusions confirmed in writing before you commit.") at the `<!-- CTA: primary -->` marker; the existing consultation sentence after it retagged `utm_content=inline`, as in the santorini-wedding-packages model
- [x] Secondary ("talk to Wedded Concierge"), closing and magnet links unchanged and marked with `<!-- CTA INLINE -->` / `<!-- LEAD MAGNET -->` comments; utm_content primary, inline, secondary, closing and magnet each appear exactly once in visible links. The 09-cro.json secondary copy change was already in 08-final.md, so it was not added twice
- [x] Both `/destination-wedding-packages` links carry no UTMs
- [x] Lead magnet: Wedded Wonderland digital magazine, `/magazine`
- [x] No em or en dashes; no "Wonderland Concierge" in visible text; no amounts of money
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (6) extracted verbatim
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] Meta title "All-Inclusive Greece Wedding Packages Compared" and meta description from `02-seo.json` (145 characters, no prices)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (6)
- [x] Images: 6 slots (featured, what-all-inclusive-means, comparison-crete-rhodes, comparison-corfu-mainland, compare-quotes, australian-angle), all `needed`
- [x] verify_items and needs_signoff empty: no prices printed. Several venues publish prices or money terms (Santorini Gem rental fees in euros, Canaves deposit terms, Abaton and Elounda SA brochures); none were used
- [x] draft_note: "DRAFT ONLY. A human clicks Publish", plus image slots, byline and linked posts
- [x] `validate.py` and `scan_copy.py` run (results below)

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 6; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=greece-wedding-packages-all-inclusive once the field map is confirmed)

1. Run `/wedded-cms-discovery` in a Chrome tab where you are logged into the CMS, and confirm the field map.
2. Source and upload the 6 images with alt text and captions; set the featured image. Venue slots: only a venue whose own package the article describes, from its media kit with written permission, or licensed stock; never AI, competitor or search-result images. compare-quotes and australian-angle: a licensed or Canva flat-lay is preferred; AI only with the person's approval, captioned "Illustrative image".
3. Enter title, slug `greece-wedding-packages-all-inclusive`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
4. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the primary CTA block at the `<!-- CTA BLOCK: primary -->` marker, and the FAQ (6 pairs).
5. **Comparison table:** keep it as a table (6 columns, 10 venues). If the CMS has a responsive table option, set it to stack each row as a card on mobile; otherwise check it scrolls cleanly on a phone in preview.
6. Categories Destination Weddings, Greece, Planning Guides, then set Destination Weddings as the primary category explicitly; add tags.
7. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
8. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
9. Preview desktop and mobile: check images, links, the CTA block, the table on mobile and the breadcrumb.

## Publish together

The body links /destination-weddings/greece-wedding-packages, /crete-wedding-venues, /santorini-wedding-packages, /santorini-wedding-venues, /mykonos-wedding-venues, /corfu-wedding-venues and /greece-wedding-venues#legal. Each has a post folder in this repo; publish any that is still a draft first or together, or the links will break.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- Author: no named author in the inputs.
- Image alt, caption, credit and licence: none in `04-images.json`; left empty, not invented.
- Package details to confirm in writing with each venue are in `booking-checklist.md`.

## Validation

- `python3 -I content-system/scripts/validate.py content/posts/greece-wedding-packages-all-inclusive`: All valid (14 stage files)
- `python3 -I content-system/scripts/scan_copy.py .../11-body.md`: 0 dashes, no overlaps; "all-inclusive" listed as banned is the allowed topic term; flagged "exclusive" 8 (exclusive use, expected) and "bespoke" 3 (venues' own service descriptions)
