# CMS report: bali-wedding-venues

**Draft URL / ID:** Not uploaded. Stopped before the CMS: no Chrome or browser connection in this session, and `content-system/cms/field-map.md` is not confirmed. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-18
- Title: 15 Best Bali Wedding Venues From Clifftops to Beaches
- Package: `content/posts/bali-wedding-venues/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/bali-wedding-venues/11-body.md`
- Booking checklist: `content/posts/bali-wedding-venues/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/bali-wedding-venues (CMS slug `bali-wedding-venues`)
- Primary category: Destination Weddings (= categories[0]); then Bali, Venues

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, text otherwise unchanged; no `[[VERIFY]]` markers in the copy
- [x] CTAs from `09-cro.json`: primary (Confirm it through Wedded Concierge), secondary, closing and magnet are existing inline links; each UTM link appears exactly once. `08-final.md` has no `<!-- CTA: primary -->` marker, so no CTA block was inserted
- [x] Key takeaways: exactly 4, verbatim; FAQ: 5 pairs, verbatim
- [x] Meta title "15 Bali Wedding Venues From Clifftops to Beaches" (no "Best"); meta description from `02-seo.json` (151 characters, no prices)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + ItemList (15 venues, official URLs from the source pack) + FAQPage (5)
- [x] Images: 6 slots from `04-images.json`, all `needed`
- [x] verify_items and needs_signoff empty; no prices; no em dashes
- [x] draft_note: "DRAFT ONLY. A human clicks Publish", plus image slots and byline
- [x] `python3 -I content-system/scripts/validate.py content/posts/bali-wedding-venues`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (it is not)
- [ ] Browser available and the person logged into the CMS (no Chrome in this session)
- [ ] Approved images prepared (0 of 6; all `needed`)
- Upload, Save Draft, preview: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Mismatches

None checked: the CMS was not opened.

## Next steps

1. Run `/wedded-cms-discovery` in a Chrome tab where you are logged into the CMS, and confirm the field map.
2. Source the 6 images (venue media kits with written permission or licensed stock; never AI, competitor or search-result images).
3. Run `/wedded-blog resume=bali-wedding-venues` to save the Draft. A human clicks Publish.
