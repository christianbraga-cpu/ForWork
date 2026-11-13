# CMS report: name-change-after-marriage

**Draft URL / ID:** Package ready, not uploaded: no browser in this session; a human saves as Draft and clicks Publish. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-13
- Title: Name Change After Marriage Step by Step in Australia
- Package: `content/posts/name-change-after-marriage/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/name-change-after-marriage/11-body.md`
- Booking checklist: `content/posts/name-change-after-marriage/booking-checklist.md`
- Target URL: https://weddedwonderland.com/expert-advice/name-change-after-marriage (CMS slug `name-change-after-marriage`)
- Primary category: Expert Advice (= categories[0]); then Destination Weddings, Planning Guides; type planning_guide (nearest to "Legal"); cluster Wedding Paperwork (tag)
- Redirect (recommendation only, not actioned): 301 from the live `/how-do-i-change-my-name-after-i-get-married-just-follow-these-4-steps` to `/expert-advice/name-change-after-marriage` at publish, or update that page in place with a slug change.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 5 image-slot comments kept, links and UTMs unchanged, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: per 09-cro.json the existing sentence with the "Wedded Concierge" link (utm_content=primary) at the end of "Changing your name on your passport after marriage" is the CTA, unchanged; marked `<!-- CTA BLOCK: primary -->` (08-final.md had no `<!-- CTA: primary -->` marker to replace)
- [x] Secondary, closing and magnet links unchanged and marked with `<!-- CTA INLINE -->` / `<!-- LEAD MAGNET -->` comments; each utm_content appears once in visible links
- [x] No em dashes; Australian English
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (6) extracted from the body only
- [x] Categories and tags from the brief; primary_category = Expert Advice
- [x] Meta title "Name Change After Marriage in Australia, Step by Step" (53 characters) and meta description (149 characters) from `02-seo.json`; no "best", no prices, no em dashes
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Expert Advice > post) + FAQPage (6)
- [x] Images: 5 slots (featured, checklist-still-life, signing-moment, travel-still-life, destination-celebration), all `needed`
- [x] verify_items and needs_signoff empty: no prices, nothing for Nic to sign off
- [x] draft_note: "DRAFT. Do not publish until checked", plus image slots, rules recheck, redirect, byline, linked guides, "A human clicks Publish"
- [x] `python3 -I content-system/scripts/validate.py content/posts/name-change-after-marriage`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (not checked against the CMS; no browser)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 5; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=name-change-after-marriage once the field map is confirmed)

1. Source and upload the 5 images with alt text and captions; set the featured image. signing-moment and destination-celebration must be real (licensed real wedding or named real venue with written consent; never AI); featured, checklist-still-life and travel-still-life are still lifes (library, Canva or licensed stock; AI only with user approval, captioned "Illustrative image"). No readable names, signatures, document numbers, certificate text or passport data page.
2. Enter title, slug `name-change-after-marriage`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block at `<!-- CTA BLOCK: primary -->` if the template uses one, and the FAQ (6 pairs).
4. Categories Expert Advice, Destination Weddings, Planning Guides, then set Expert Advice as the primary category explicitly; add tags (Wedding Paperwork first).
5. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
6. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
7. Preview desktop and mobile; check links, the CTA and the breadcrumb.
8. At publish (human): set up the recommended 301 from the old live URL, or update that page in place with a slug change.

## Publish together

The body links: /expert-advice/do-you-have-to-register-an-overseas-marriage-at-home, /expert-advice/overseas-marriage-certificate and /expert-advice/what-is-an-apostille-and-does-my-paperwork-need-one. Publish them first or together if not yet live, or the links will break.

## Mismatches and open points

- Field map not checked against the CMS (no browser), so no CMS labels could be compared with the package.
- Content type: "Legal" is not a schema value; `planning_guide` used as the nearest.
- Author: no named author in the inputs.
- 08-final.md had no `<!-- CTA: primary -->` marker; the existing primary link is marked as the CTA block.
- Image alt, caption, credit and licence: none in `04-images.json`; left empty, not invented.
- Name change steps for couples, state by state and for overseas marriages, are in `booking-checklist.md`.
