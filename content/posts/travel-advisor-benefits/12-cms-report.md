# CMS report: travel-advisor-benefits

**Draft URL / ID:** Package ready, not uploaded: no browser (no Chrome) in this session and the CMS field map is not confirmed; a human saves as Draft and clicks Publish. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-16
- Title: Travel Advisor Benefits You Cannot Get Booking Alone
- Package: `content/posts/travel-advisor-benefits/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/travel-advisor-benefits/11-body.md`
- Booking checklist: `content/posts/travel-advisor-benefits/booking-checklist.md` (questions to ask any travel advisor)
- Target URL: https://weddedwonderland.com/travel-guides/travel-advisor-benefits (CMS slug `travel-advisor-benefits`)
- Primary category: Travel Guides (= categories[0]); then Destination Weddings, Planning Guides; type planning_guide
- New article, no redirect.
- **CMS setup needed first:** `/travel-guides` is a new folder. The `/travel-guides` folder (URL path) and the **Travel Guides** category must exist in the CMS before the draft is saved, or the URL and primary category cannot be set.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 5 image-slot comments kept, all links and the 4 UTM links unchanged, no CTA marker comments, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: per 09-cro.json the existing "Wedded Concierge" link (utm_content=primary) in "When the trip is a wedding and a honeymoon" is the CTA, unchanged (08-final.md had no `<!-- CTA: primary -->` marker to replace)
- [x] Secondary, closing and magnet links unchanged; each utm_content appears exactly once in the body
- [x] No em dashes; Australian English; `scan_copy.py` on `11-body.md`: no banned or flagged phrases, 0 dashes, no overlaps
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (5) extracted from the body only
- [x] Categories and tags from the brief; primary_category = Travel Guides
- [x] Meta title "Travel Advisor Benefits for Your Destination Wedding" (52 characters) and meta description (151 characters) from `02-seo.json`; no prices, no em dashes
- [x] schema_jsonld: Article (datePublished empty, author and publisher Wedded Wonderland) + BreadcrumbList (Home > Travel Guides > post) + FAQPage (5)
- [x] Images: 5 slots (featured, advisor-planning, benefits-still-life, questions-notebook, honeymoon-destination), all `needed`
- [x] verify_items and needs_signoff empty: no `[[VERIFY]]` markers, no prices, nothing for Nic to sign off
- [x] draft_note: "DRAFT. Do not publish until checked", plus image slots, /travel-guides and Travel Guides setup, source recheck, byline, "A human clicks Publish"
- [x] `python3 -I content-system/scripts/validate.py content/posts/travel-advisor-benefits`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (not confirmed)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 5; all `needed`)
- [ ] `/travel-guides` folder and Travel Guides category exist in the CMS (not checked; no browser)
- [ ] The person is logged into the CMS in the Chrome tab (no Chrome in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=travel-advisor-benefits once the field map is confirmed)

1. Create the `/travel-guides` folder and the Travel Guides category if they do not exist yet.
2. Source and upload the 5 images with alt text and captions; set the featured image. advisor-planning must come from a consented real Wedded Wonderland shoot or licensed stock with model releases (never AI); honeymoon-destination must be a real, named destination or partner venue from a consented, licensed source with the location verified (never AI); featured, benefits-still-life and questions-notebook are still lifes (library, Canva or licensed stock; AI only with Wedded Wonderland approval, labelled "Illustrative image"). No travel brand logos, readable names, passport numbers or booking references.
3. Enter title, slug `travel-advisor-benefits`, excerpt and author (byline to confirm; package uses "Wedded Wonderland").
4. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block if the template uses one (text "Request a Wedded Concierge consultation", subtext "The fee is agreed in writing before any work begins.", primary UTM link), and the FAQ (5 pairs).
5. Categories Travel Guides, Destination Weddings, Planning Guides, then set Travel Guides as the primary category explicitly; add tags.
6. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
7. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
8. Preview desktop and mobile; check links, the CTA and the breadcrumb (Home > Travel Guides > post).

## Mismatches and open points

- Field map not confirmed and no browser, so no CMS labels could be compared with the package.
- `/travel-guides` and Travel Guides are new in the CMS; confirm they exist before saving.
- Byline: no author named in any input; package uses "Wedded Wonderland".
