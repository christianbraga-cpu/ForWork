# CMS report: best-time-to-get-married-in-bali

**Draft URL / ID:** Not uploaded. Stopped before the CMS: no Chrome or browser tool in this session, and `content-system/cms/field-map.md` is not confirmed. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-18
- Title: Best Time to Get Married in Bali by Month
- Package: `content/posts/best-time-to-get-married-in-bali/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/best-time-to-get-married-in-bali/11-body.md`
- Booking checklist: `content/posts/best-time-to-get-married-in-bali/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/best-time-to-get-married-in-bali (CMS slug `best-time-to-get-married-in-bali`)
- Primary category: Destination Weddings (= categories[0]); then Bali, Planning Guides
- Redirect: none (new article)

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 5 image-slot comments kept, text, links and UTMs unchanged
- [x] CTA links marked in place (primary, secondary, closing, lead magnet) per `09-cro.json`; `08-final.md` had no `<!-- CTA: primary -->` marker to replace
- [x] Key takeaways: exactly 4, verbatim; FAQ: 5 pairs from the body
- [x] Meta title (41 characters) and meta description (149 characters) from `02-seo.json`; description names no best month
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage
- [x] Images: 5 slots (featured, dry-season, wet-season, dates-to-plan-around, which-months-suit-you), all `needed`
- [x] verify_items and needs_signoff empty: no prices, nothing for Nic to sign off
- [x] No em dashes, no prices, no banned brand words
- [x] `python3 -I content-system/scripts/validate.py content/posts/best-time-to-get-married-in-bali`: All valid

## CMS checklist (Part 2: not run)

- [ ] Images, featured image, title/slug/excerpt/author, body, Key Takeaways, CTA, FAQ, categories and primary category, tags, SEO, schema, draft note, Save Draft
- [ ] Preview screenshots (desktop and mobile): none taken

## Mismatches

None checked: the CMS was not opened. To continue, confirm the field map (`/wedded-cms-discovery`), log into the CMS in Chrome, then run `/wedded-blog resume=best-time-to-get-married-in-bali`. A human clicks Publish.
