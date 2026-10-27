# CMS report: getting-married-in-italy

**Draft URL / ID:** Not uploaded. There is no browser connection (Claude in Chrome) in this cloud session, and the CMS field map is not confirmed (`content-system/cms/field-map.md` says "NOT YET MAPPED"). Only the package was built.

- Date: 2026-10-27
- Title: Getting Married in Italy as an Australian
- Package: `content/posts/getting-married-in-italy/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/getting-married-in-italy/11-body.md`
- Target URL: https://weddedwonderland.com/destination-weddings/getting-married-in-italy
- CMS slug: getting-married-in-italy
- Primary category: Destination Weddings (= categories[0], fixed by the person)
- Content type: Legal; cluster: Getting Married in Italy

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, all `<!-- fact_xx -->` markers removed, 2 `[[VERIFY]]` markers and 7 image-slot comments kept
- [x] Primary CTA ("Speak with a Wedded Advisor", subtext "No date or town yet? Nothing is too early or too vague.", `utm_content=primary`) placed at the former `<!-- CTA: primary -->` marker after the timeline section, wrapped in `<!-- CTA BLOCK: primary -->`
- [x] Secondary CTA: already in the closing paragraph of `08-final.md` with `utm_content=secondary` (applied at stage 09); no separate block added
- [x] Lead magnet (/magazine): optional, skipped at stage 09; recorded in the package but not placed
- [x] Key takeaways: exactly 4, from `08-final.md`
- [x] FAQ: 8 Q&A pairs, from `08-final.md`
- [x] Categories: Destination Weddings, Italy, Expert Advice; primary_category = Destination Weddings
- [x] Tags (6, from the brief); meta title, meta description and focus keyword from `02-seo.json`; canonical; OG image slot (featured)
- [x] schema_jsonld: Article (publisher Wedded Wonderland, datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (all 8 FAQs)
- [x] Images: all 7 slots from `04-images.json` listed, all `needed`
- [x] verify_items: the 2 markers in the body (Italian civil union law; how Australia treats an Italian unione civile)
- [x] needs_signoff: empty (no fee figures printed)
- [x] draft_note: 2 VERIFY items, "Nic sign-off on prices: none (no prices printed)", 7 image slots needed, 6 deferred business items, 2 person questions
- [x] `python3 -I content-system/scripts/validate.py content/posts/getting-married-in-italy`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 7 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started (images, featured image, title/slug/excerpt/author, body, Key Takeaways, CTA blocks, FAQ, categories and primary category, tags, SEO fields, schema, draft note, Save Draft).

After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Mismatches and open points

- The field map is not confirmed, so no CMS labels could be checked against the package.
- Author: no named author in the inputs; the package uses "Wedded Wonderland" until the byline is confirmed.
- Image alt and caption: none supplied in `04-images.json` (no approved images), so they are left empty rather than made up.
- Body links mix absolute URLs (in the copy) and relative CTA links (from `09-cro.json`). Both are copied as given.
- Person questions:
  1. Print the official fees (DFAT apostille, Atto Notorio, marca da bollo, Nulla Osta) with an as-at date? Any figure needs Nic's sign-off.
  2. Does Wedded Concierge book the Nulla Osta appointment, find interpreters and attend offices (Rome or Milan, Prefettura, comune)?
- Deferred business items (the person's decision): fee model and commissions; deposits, refunds and contracts; From AUD ranges; named Advisor or phone line; a real wedding; Wedded Privileges explanation.

## Next step

Run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS. Confirm the field map, then run `/wedded-blog resume=getting-married-in-italy`. Nothing was published or scheduled.
