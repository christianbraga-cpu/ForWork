# CMS report: get-married-in-new-zealand

**Draft URL / ID:** not uploaded. Stopped before the CMS: no Chrome (browser tool) in this session, and `content-system/cms/field-map.md` is not confirmed. Nothing was saved, scheduled or published in the CMS. A human saves as Draft and clicks Publish, or run `/wedded-blog resume=get-married-in-new-zealand` once the field map is confirmed and a browser is available.

- Date: 2026-11-17
- Title: How to Get Married in New Zealand as an Australian
- Series: fifth post in the "Getting Married in {Country}" series
- Package: `content/posts/get-married-in-new-zealand/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/get-married-in-new-zealand/11-body.md`
- Booking checklist: `content/posts/get-married-in-new-zealand/booking-checklist.md` (questions only, no amounts)
- Target URL: https://weddedwonderland.com/destination-weddings/get-married-in-new-zealand (slug `get-married-in-new-zealand`)
- Primary category: Destination Weddings (= categories[0]); then New Zealand, Australia & Pacific, Planning Guides

## Package build (Part 1)

- [x] Body: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 6 image-slot comments kept verbatim, text and links otherwise unchanged
- [x] Primary CTA "Speak with Wedded Concierge" (09-cro.json) is the existing inline link in "Venues and planning"; 08-final.md has no `<!-- CTA: primary -->` marker
- [x] Exactly 4 key takeaways and 5 FAQ pairs, verbatim from the body
- [x] Meta title and description from 02-seo.json
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (5)
- [x] Images: 6 slots from 04-images.json, all `needed`
- [x] CTA from 09-cro.json; verify_items empty; status draft
- [x] No prices, no em dashes
- [x] `python3 -I content-system/scripts/validate.py content/posts/get-married-in-new-zealand`: All valid

## CMS checklist (Part 2: not run)

- [ ] Field map status CONFIRMED (not confirmed)
- [ ] Browser available and person logged in (no Chrome in this session)
- [ ] Approved images (0 of 6)
- [ ] `/destination-weddings` folder and Destination Weddings category exist (not checked)

## Screenshots

None. Nothing was uploaded.

## Mismatches and open points

- No CMS labels compared: field map not confirmed and no browser.
- Four image-slot comments carry a `[[VERIFY licence]]` note on Tourism New Zealand media (from 04-images.json). It is an internal comment, not article copy; verify_items left empty as instructed. Resolve before any Tourism NZ image is used.
- Series sister links (Hawaii, Mauritius, Seychelles, Costa Rica) are drafts: publish together or remove that sentence.
- Brief tag `Getting Married in {Country}` kept as given.
