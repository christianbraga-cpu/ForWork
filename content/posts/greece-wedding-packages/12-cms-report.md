# CMS report: greece-wedding-packages

**Draft URL / ID:** Not uploaded: no browser connection in this session and the CMS field map is not yet confirmed (run /wedded-cms-discovery locally)

- Date: 2026-11-11
- Title: Greece Wedding Packages and What They Include
- Package: `content/posts/greece-wedding-packages/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/greece-wedding-packages/11-body.md`
- Booking checklist: `content/posts/greece-wedding-packages/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/greece-wedding-packages (CMS slug `greece-wedding-packages`)
- Primary category: Destination Weddings (= categories[0]); type Guide; cluster Getting Married in Greece
- New article, no redirect

## Package build (Part 1)

- [x] Confirmed `08-final.md` already carries the `09-cro.json` copy changes (early Concierge link below Key takeaways removed, primary marker at the end of "What a Greek venue package usually includes", old marker above the secondary removed)
- [x] Body built from `08-final.md`: front matter removed, all `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, no `[[VERIFY]]` markers
- [x] Primary CTA block (Speak with a Wedded Advisor, subtext "The fee is agreed in writing before any work begins.") at the `<!-- CTA: primary -->` marker; the inline sentence after it retagged `utm_content=inline` (as the Crete model); secondary, lead magnet and closing links marked with comments; each `utm_content` link appears once
- [x] Key takeaways: exactly the 4 in the body, copied verbatim; FAQ (5) extracted
- [x] Categories: Destination Weddings, Greece, Planning Guides; primary_category = Destination Weddings; tags (9) from the brief
- [x] Meta title ("Greece Wedding Packages: What They Include and Leave Out") and description, focus keyword, canonical, OG image slot (featured)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (5)
- [x] Images: 6 slots in the body (featured, inclusions, ceremony-types, left-out, compare-quotes, australian-angle), all `needed`
- [x] verify_items: image credits and licences (6) only; needs_signoff empty (no prices)
- [x] draft_note: linked drafts to publish together, keyword split recommendation, image slots, deferred business items
- [x] redirects_recommended: none (new article)
- [x] No em dashes; no "all-inclusive" in copy fields (see the FAQ note below)
- [x] `python3 -I content-system/scripts/scan_copy.py content/posts/greece-wedding-packages/11-body.md`: no banned words, 0 dashes, no overlaps; flagged "exclusive" 8 times (exclusive use is a section topic; no change made) and "bespoke" once (Nana Princess's own name for its fourth option; no change made)
- [x] `python3 -I content-system/scripts/validate.py content/posts/greece-wedding-packages`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 6 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Publish together

The body links three drafts: /destination-weddings/greece-wedding-venues (twice, once with the #getting-legally-married-in-greece-as-australians-in-brief anchor), /destination-weddings/crete-wedding-venues (once) and /expert-advice/greek-wedding-traditions (once). Publish them with this post, or hold this post until they are live. Check the Greece guide anchor lands in preview.

## Keyword split (recommendation only, nothing on the live site changes)

From `02-seo.json`: this guide owns "greece wedding packages" / "greek wedding packages" and the question "are Greek wedding packages all inclusive". /destination-wedding-packages keeps the generic destination wedding packages queries it already ranks for and is the commercial next step, linked twice from this guide. /destination-packages keeps "wedding packages abroad / overseas". The Greece hub keeps "greece wedding" and "weddings in greece". "santorini wedding packages" is a later opportunity for a Santorini section on /destination-wedding-packages, not this guide's target. No weddedwonderland.com page currently ranks for a Greece package query. GSC overlap unconfirmed (fast mode).

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- Author: no named author in the inputs; package uses "Wedded Wonderland" pending confirmation.
- FAQ question "Are Greek wedding packages all inclusive?" is kept verbatim (unhyphenated) from `08-final.md` and the SEO stage's FAQ questions, and is in the FAQPage schema. Confirm the person is happy with this wording; no copy was changed at this stage.
- Excerpt is the first two sentences of the opening paragraph, verbatim (the first sentence alone does not carry the focus keyword).
- Image alt, caption, credit and licence: none supplied in `04-images.json`; left empty, not invented. compare-quotes may be AI only on the person's approval and captioned "Illustrative image"; australian-angle prefers a library or licensed stock image, with AI only as an approved fallback.
- Booking checklist items flagged for confirmation before quoting: Abaton 2027 terms, Lagonissi current package (brochure 2022), whether Melenos's government fees sit inside its costing, Angsana legal ceremony option, Four Seasons ceremony types, Nana Princess full package lists, plus transfers, access and closure questions at every venue.
- Deferred business items (person's decision): fee model and commissions, a named Wedded Advisor or phone line.

## Next step

Run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS, confirm the field map, then `/wedded-blog resume=greece-wedding-packages`. Nothing was published or scheduled.
