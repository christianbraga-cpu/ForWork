# CMS report: who-can-perform-a-marriage

**Draft URL / ID:** Package ready, not uploaded: no browser in this session; a human saves as Draft and clicks Publish. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-13
- Title: Authorised Marriage Celebrants and Who Can Legally Marry You
- Package: `content/posts/who-can-perform-a-marriage/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/who-can-perform-a-marriage/11-body.md`
- Booking checklist: `content/posts/who-can-perform-a-marriage/booking-checklist.md`
- Target URL: https://weddedwonderland.com/expert-advice/who-can-perform-a-marriage (CMS slug `who-can-perform-a-marriage`)
- Primary category: Expert Advice (= categories[0]); then Destination Weddings, Planning Guides; type planning_guide (nearest to "Legal"); cluster Wedding Paperwork (tag)
- Redirect: none (new article).

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 5 image-slot comments kept, links and UTMs unchanged, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: per 09-cro.json the existing sentence with the "Wedded Concierge" link (utm_content=primary) at the end of "Types of authorised marriage celebrants" is the CTA, unchanged; marked `<!-- CTA BLOCK: primary -->` (08-final.md had no `<!-- CTA: primary -->` marker to replace)
- [x] Secondary, closing and magnet links unchanged and marked with `<!-- CTA INLINE -->` / `<!-- LEAD MAGNET -->` comments; each utm_content appears once in visible links
- [x] No em dashes; Australian English
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (7) extracted from the body only
- [x] Categories and tags from the brief; primary_category = Expert Advice
- [x] Meta title "Who Can Perform a Marriage in Australia? Celebrants Guide" (57 characters) and meta description (153 characters) from `02-seo.json`; no "best", no prices, no em dashes
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Expert Advice > post) + FAQPage (7)
- [x] Images: 5 slots (featured, religious-ceremony, family-reading, signing-table, destination-celebration), all `needed`
- [x] verify_items and needs_signoff empty: no prices, nothing for Nic to sign off
- [x] draft_note: "DRAFT. Do not publish until checked", plus image slots, celebrant rules recheck, byline, linked guides, "A human clicks Publish"
- [x] `python3 -I content-system/scripts/validate.py content/posts/who-can-perform-a-marriage`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (not checked against the CMS; no browser)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 5; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=who-can-perform-a-marriage once the field map is confirmed)

1. Source and upload the 5 images with alt text and captions; set the featured image. featured, religious-ceremony, family-reading and destination-celebration must be real (licensed real wedding or named real venue with written consent; never AI); signing-table is a still life (Canva, licensed stock or real detail shot; AI only with user approval, captioned "Illustrative image"). No legible certificate, register, names, signatures or government crest.
2. Enter title, slug `who-can-perform-a-marriage`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block at `<!-- CTA BLOCK: primary -->` if the template uses one, and the FAQ (7 pairs).
4. Categories Expert Advice, Destination Weddings, Planning Guides, then set Expert Advice as the primary category explicitly; add tags (Wedding Paperwork first).
5. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
6. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
7. Preview desktop and mobile; check links, the CTA and the breadcrumb.

## Publish together

The body links: /expert-advice/how-to-choose-a-wedding-celebrant, /expert-advice/what-is-a-certificate-of-no-impediment-and-who-issues-it, /expert-advice/what-is-an-apostille-and-does-my-paperwork-need-one, /expert-advice/do-you-have-to-register-an-overseas-marriage-at-home and /expert-advice/what-does-a-celebrant-do-and-do-you-need-one-abroad. Publish them first or together if not yet live, or the links will break.

## Mismatches and open points

- Field map not checked against the CMS (no browser), so no CMS labels could be compared with the package.
- Content type: "Legal" is not a schema value; `planning_guide` used as the nearest.
- Author: no named author in the inputs.
- 08-final.md had no `<!-- CTA: primary -->` marker; the existing primary link is marked as the CTA block.
- The body refers to "Our separate guide to the Notice of Intended Marriage" without a link; consider linking /expert-advice/notice-of-intended-marriage once live (copy left unchanged).
- Image alt, caption, credit and licence: none in `04-images.json`; left empty, not invented.
- Celebrant, NOIM, certificate, registry and marrying-abroad items for couples are in `booking-checklist.md`.
