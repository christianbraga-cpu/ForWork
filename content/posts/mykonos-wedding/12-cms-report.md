# CMS report: mykonos-wedding

**Draft URL / ID:** Not uploaded: stopped at the package (fast mode, no browser connection in this session) and the CMS field map is not yet confirmed (run /wedded-cms-discovery locally)

- Date: 2026-11-11
- Title: Mykonos Wedding Guide to Venues, Seasons and Paperwork
- Package: `content/posts/mykonos-wedding/11-publish-package.json` (status `draft`)
- Body: `content/posts/mykonos-wedding/11-body.md`
- Booking checklist: `content/posts/mykonos-wedding/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/mykonos-wedding (CMS slug `mykonos-wedding`)
- Primary category: Destination Weddings (= categories[0]); categories Destination Weddings, Greece, Mykonos, Planning Guides
- New article, no redirect

## Package build (Part 1)

- [x] Confirmed `08-final.md` already carries the `09-cro.json` secondary link in the cost section
- [x] Body built from `08-final.md`: front matter and all `<!-- fact_xx -->` markers removed, 7 image-slot comments kept, no `[[VERIFY]]` markers in the copy, links unchanged
- [x] Primary CTA block (Speak with a Wedded Advisor, subtext "The fee is agreed in writing before any work begins.") at the `<!-- CTA: primary -->` marker; the inline sentence after it retagged `utm_content=inline`; secondary, lead magnet and closing links marked with comments; primary, secondary, magnet and closing each appear once as a visible link
- [x] Key takeaways: exactly the 4 in the body, copied verbatim; FAQ (6) extracted
- [x] Categories and tags (6) from the brief; primary_category = Destination Weddings
- [x] Meta title and description from `02-seo.json`, focus keyword "mykonos wedding", canonical, OG image slot (featured); excerpt = meta description
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (6)
- [x] Images: 7 slots (featured, why-mykonos, venues-area-type, seasons, paperwork, getting-there, house-rules-booking), all `needed`
- [x] verify_items empty; needs_signoff empty (no prices)
- [x] draft_note: Draft only, a human clicks Publish; image slots, linked pages, mobile table, deferred business items
- [x] No em dashes; no "Wonderland Concierge" in visible text
- [x] `python3 -I content-system/scripts/scan_copy.py content/posts/mykonos-wedding/11-body.md`: no banned words, 0 dashes, no overlaps; flagged "exclusive" 7 times (exclusive use is a house rule and cost driver the guide covers) and "luxury" once (the official tourism line); no change made
- [x] `python3 -I content-system/scripts/validate.py content/posts/mykonos-wedding`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 7 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started. After save: not started.

## What to do in the CMS (once the field map is confirmed)

Follow `content-system/cms/publish-checklist.md` in order, from `11-publish-package.json`:

1. Images first: upload each approved slot with alt and caption; set `featured` as the featured image.
2. Title, slug `mykonos-wedding`, excerpt, author.
3. Body from `11-body.md`; place the image slots at their comments, and drop the HTML comments themselves.
4. Key Takeaways block: the 4 items in `key_takeaways`.
5. CTA block at `<!-- CTA BLOCK: primary -->` (text, subtext, link). If the CMS has no CTA block, keep the inline fallback sentence.
6. FAQ block: the 6 pairs in `faq`.
7. Categories, then set Destination Weddings as the primary category explicitly; then tags.
8. SEO fields: meta title, meta description, focus keyword, canonical, OG image.
9. Schema field (if present): `schema_jsonld`; fill datePublished at publish time.
10. Internal note: `draft_note`.
11. Save Draft. Never Publish or Schedule; a human clicks Publish.
12. Preview: screenshot desktop and mobile into `content/posts/mykonos-wedding/screenshots/`; check images, links (the jump link to "Getting your guests to Mykonos"), CTA, breadcrumb and that the Naxos table scrolls on mobile.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- Author: no named author in the inputs; package uses "Wedded Wonderland" pending confirmation.
- Image alt, caption, credit and licence: none supplied in `04-images.json`; left empty, not invented. Every slot is a real place or venue and never AI.
- Linked pages: confirm the Mykonos venues guide, Santorini wedding, Paros venues, Greece venues, Greece packages, Greek wedding traditions and the Greece hub are live, or publish them together.
- Booking checklist items (not blockers): Municipality of Mykonos civil marriage steps and fees, CNI, apostille and translation questions, each venue's "Not published" items, deposits, cancellation, exclusive-use days and music times at every venue.
- Deferred business items (person's decision): fee model and commissions, deposits, a named Wedded Advisor or first call, real Mykonos weddings to show.

## Next step

Run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS, confirm the field map, then `/wedded-blog resume=mykonos-wedding`. Nothing was published or scheduled.
