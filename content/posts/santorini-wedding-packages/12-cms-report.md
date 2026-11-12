# CMS report: santorini-wedding-packages

**Draft URL / ID:** Not uploaded. FAST MODE, package only: no browser connection in this session and `content-system/cms/field-map.md` is not confirmed ("NOT YET MAPPED"). Stopped at the package. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-12
- Title: Santorini Wedding Packages and What They Include
- Package: `content/posts/santorini-wedding-packages/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/santorini-wedding-packages/11-body.md`
- Booking checklist: `content/posts/santorini-wedding-packages/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/santorini-wedding-packages (CMS slug `santorini-wedding-packages`)
- Primary category: Destination Weddings (= categories[0]); then Greece, Planning Guides; type Guide; cluster Getting Married in Greece

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 7 image-slot comments kept, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA block (Speak with a Wedded Advisor, subtext "Quotes in AUD, inclusions confirmed in writing before you commit.") at the `<!-- CTA: primary -->` marker; the existing consultation sentence after it retagged `utm_content=inline`, as in the santorini-wedding-venues model
- [x] Secondary ("talk to Wedded Concierge"), closing and magnet links unchanged and marked with `<!-- CTA INLINE -->` / `<!-- LEAD MAGNET -->` comments; utm_content primary, inline, secondary, closing and magnet each appear exactly once in visible links. The 09-cro.json secondary copy change was already in 08-final.md, so it was not added twice
- [x] Lead magnet: Wedded Wonderland magazine, `/magazine`
- [x] No em or en dashes; no "Wonderland Concierge" in visible text; no amounts of money
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (6) extracted verbatim
- [x] Categories from the brief; primary_category = Destination Weddings; tags from the brief
- [x] Meta title "Santorini Wedding Packages: What They Include and Leave Out" and meta description from `02-seo.json` (147 characters, no prices)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (6)
- [x] Images: 7 slots (featured, inclusions, ceremony-types, package-types, left-out, compare-quotes, australian-angle), all `needed`
- [x] verify_items and needs_signoff empty: no prices printed. Some venues publish money terms (Santorini Gem rental PDF and policy, Canaves deposit percentage, Grace menu charge); none were used
- [x] draft_note: "DRAFT ONLY. A human clicks Publish", plus image slots, byline and linked drafts
- [x] `python3 -I content-system/scripts/validate.py content/posts/santorini-wedding-packages`: All valid
- [x] `python3 -I content-system/scripts/scan_copy.py content/posts/santorini-wedding-packages/11-body.md`: no banned words, 0 dashes, no overlaps; flagged "exclusive" 7 (exclusive use, expected) and "bespoke" 1 (Andronis's own service description)

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 7; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=santorini-wedding-packages once the field map is confirmed)

1. Run `/wedded-cms-discovery` in a Chrome tab where you are logged into the CMS, and confirm the field map.
2. Source and upload the 7 images with alt text and captions; set the featured image. Venue slots: the venue's own media kit with written permission, or licensed stock; never AI, competitor or search-result images. compare-quotes and australian-angle: a licensed or Canva flat-lay is preferred; AI only with the person's approval, captioned "Illustrative image".
3. Enter title, slug `santorini-wedding-packages`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
4. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the primary CTA block at the `<!-- CTA BLOCK: primary -->` marker, and the FAQ (6 pairs).
5. Categories Destination Weddings, Greece, Planning Guides, then set Destination Weddings as the primary category explicitly; add tags.
6. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
7. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
8. Preview desktop and mobile: check images, links, the CTA block and the breadcrumb.

## Publish together

The body links drafts: /destination-weddings/santorini-wedding-venues, /destination-weddings/santorini-wedding, /destination-weddings/greece-wedding-packages and /expert-advice/greek-wedding-traditions. Publish them first or together, or the links will break.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- Author: no named author in the inputs.
- Image alt, caption, credit and licence: none in `04-images.json`; left empty, not invented.
- Package details to confirm in writing with each venue are in `booking-checklist.md` (including the Santorini Gem villa bathroom count, 4 vs 5).
