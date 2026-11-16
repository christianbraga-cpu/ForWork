# CMS report: honeymoon-planner-vs-travel-agent

**Draft URL / ID:** Package ready, not uploaded: no browser (no Chrome) in this session and the CMS field map is not confirmed; a human saves as Draft and clicks Publish. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-16
- Title: Honeymoon Planner vs Travel Agent Compared
- Package: `content/posts/honeymoon-planner-vs-travel-agent/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/honeymoon-planner-vs-travel-agent/11-body.md`
- Booking checklist: `content/posts/honeymoon-planner-vs-travel-agent/booking-checklist.md` (questions to put to any planner or agent)
- Target URL: https://weddedwonderland.com/honeymoon-ideas/honeymoon-planner-vs-travel-agent (CMS slug `honeymoon-planner-vs-travel-agent`)
- Primary category: Honeymoon Ideas (= categories[0]); then Destination Weddings, Planning Guides; type comparison
- New article, no redirect.
- **CMS setup needed first:** the `/honeymoon-ideas` folder (URL path) and the **Honeymoon Ideas** category must exist in the CMS before the draft is saved, or the URL and primary category cannot be set.
- **Draft links:** the body links to `/honeymoon-ideas/honeymoon-planning-service`, `/travel-guides/travel-advisor-benefits` and `/honeymoon-ideas/honeymoon-planner-cost`, which are drafts. Publish all three together with this post, or remove those links before publishing.

## Package build (Part 1)

- [x] Body built from `08-final.md` (checked stable before building): front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 5 image-slot comments kept, all 12 links and the 4 UTM links unchanged, no CTA marker comments, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: per 09-cro.json the existing "Wedded Concierge" link (utm_content=primary) in "Where Wedded Wonderland fits" is the CTA, unchanged (08-final.md had no `<!-- CTA: primary -->` marker to replace)
- [x] Secondary, closing and magnet links unchanged; each utm_content appears exactly once in the body
- [x] No em dashes; Australian English; `scan_copy.py` on `11-body.md`: 0 banned, 0 flagged, 0 dashes, no overlaps
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (4) extracted from the body only
- [x] Categories and tags from the brief; primary_category = Honeymoon Ideas
- [x] Meta title "Honeymoon Planner vs Travel Agent: Questions to Ask" (51 characters) and meta description (149 characters) from `02-seo.json`; no prices, no em dashes
- [x] schema_jsonld: Article (datePublished empty, author and publisher Wedded Wonderland) + BreadcrumbList (Home > Honeymoon Ideas > post) + FAQPage (4)
- [x] Images: 5 slots (featured, doing-it-yourself, side-by-side-questions, why-labels-blur, after-destination-wedding), all `needed`
- [x] verify_items and needs_signoff empty: no `[[VERIFY]]` markers, no prices, nothing for Nic to sign off
- [x] draft_note: "DRAFT. Do not publish until checked", plus image slots, /honeymoon-ideas and Honeymoon Ideas setup, the three draft links, source recheck, the open stage 03 brand flag, "A human clicks Publish"
- [x] `python3 -I content-system/scripts/validate.py content/posts/honeymoon-planner-vs-travel-agent`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (not confirmed)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 5; all `needed`)
- [ ] `/honeymoon-ideas` folder and Honeymoon Ideas category exist in the CMS (not checked; no browser)
- [ ] The person is logged into the CMS in the Chrome tab (no Chrome in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=honeymoon-planner-vs-travel-agent once the field map is confirmed)

1. Create the `/honeymoon-ideas` folder and the Honeymoon Ideas category if they do not exist yet.
2. Source and upload the 5 images with alt text and captions; set the featured image. side-by-side-questions shows people, so it must come from a consented real Wedded Wonderland shoot or model-released licensed stock (never AI); featured, doing-it-yourself, why-labels-blur and after-destination-wedding are still lifes (library, Canva or licensed stock; AI only with Wedded Wonderland approval, labelled "Illustrative image"). No travel agency shopfronts, signage or logos, no airline, hotel, resort, cruise or card brand material, no money or visible figures, no readable names, passport numbers or booking references.
3. Enter title, slug `honeymoon-planner-vs-travel-agent`, excerpt and author ("Wedded Wonderland").
4. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block if the template uses one (text "Request a Wedded Concierge consultation", subtext "The fee is agreed in writing before any work begins.", primary UTM link), and the FAQ (4 pairs).
5. Categories Honeymoon Ideas, Destination Weddings, Planning Guides, then set Honeymoon Ideas as the primary category explicitly; add tags.
6. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
7. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
8. Preview desktop and mobile; check links, the CTA and the breadcrumb (Home > Honeymoon Ideas > post).
9. Before publishing, confirm `/honeymoon-ideas/honeymoon-planning-service`, `/travel-guides/travel-advisor-benefits` and `/honeymoon-ideas/honeymoon-planner-cost` go live at the same time, or remove those three links.

## Mismatches and open points

- Field map not confirmed and no browser, so no CMS labels could be compared with the package.
- `/honeymoon-ideas` and Honeymoon Ideas must exist in the CMS; confirm before saving.
- Three internal links point to draft posts (see above): publish together or remove.
- Stage 03 flag for Nic (not blocking the package): the live Concierge FAQ describes honeymoon help as introductions to travel specialists and partners possibly paying a booking fee, which conflicts with the brand-facts line behind "A honeymoon on its own is planned the same way, with one Wedded Advisor."
- 04-images.json slot placements (after_h2:n) differ from where the final copy places the slots; the body is followed.
