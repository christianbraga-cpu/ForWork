# CMS report: mykonos-wedding-venues

**Draft URL / ID:** Not uploaded: no browser connection in this session and the CMS field map is not yet confirmed (run /wedded-cms-discovery locally)

- Date: 2026-11-11
- Title: 10 Mykonos Wedding Venues for a Cycladic Celebration
- Package: `content/posts/mykonos-wedding-venues/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/mykonos-wedding-venues/11-body.md`
- Booking checklist: `content/posts/mykonos-wedding-venues/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/mykonos-wedding-venues (CMS slug `mykonos-wedding-venues`)
- Primary category: Destination Weddings (= categories[0]); type Guide; cluster Getting Married in Greece
- New article, no redirect

## Package build (Part 1)

- [x] Confirmed `08-final.md` already carries the `09-cro.json` copy change (primary marker filled after the table) and the 8b edits; secondary, closing and magnet links were already in place
- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 11 image-slot comments kept, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA block (Speak with a Wedded Advisor, subtext "The fee is agreed in writing before any work begins.") at the `<!-- CTA: primary -->` marker; the inline sentence after it retagged `utm_content=inline` (as the Corfu model); secondary, closing and lead magnet links marked with comments; each `utm_content` link appears once
- [x] Key takeaways: exactly the 4 in the body, copied verbatim; FAQ (6) extracted
- [x] Categories: Destination Weddings, Greece, Venues; primary_category = Destination Weddings; tags (7) from the brief, unchanged
- [x] Meta title "Mykonos Wedding Venues: 10 for a Cycladic Celebration" (from `02-seo.json`); meta description kept from `02-seo.json` because Ornos, Psarou, Elia and Agios Sostis all have a venue in the body (144 characters); focus keyword, canonical, OG image slot (featured)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + ItemList (10 venues, official URLs) + FAQPage (6)
- [x] Images: 11 slots in the body (featured, 5 areas, 5 venues), all `needed`
- [x] verify_items: image credits and licences only (11); needs_signoff empty (no prices)
- [x] draft_note: linked drafts to publish together, mobile table scroll, jump list, image slots, deferred business items
- [x] redirects_recommended: none (new article)
- [x] `python3 -I content-system/scripts/scan_copy.py content/posts/mykonos-wedding-venues/11-body.md`: no banned words, 0 dashes, no overlaps; flagged "exclusive" 14 (expected in a venue guide comparing exclusive use) and "luxury" 1 (the venue's own name, "Santa Marina, a Luxury Collection Resort"); no change made
- [x] `python3 -I content-system/scripts/validate.py content/posts/mykonos-wedding-venues`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 11 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Publish together

The body links three drafts: /destination-weddings/greece-wedding-venues (twice), /destination-weddings/greece-wedding-packages (once) and /expert-advice/greek-wedding-traditions (once). Publish the Greece venues guide, the Greece packages guide and Greek wedding traditions together with this post, or hold this post until they are live. The Greece venues and packages guides should link down to this post where they mention Mykonos.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- No `[[VERIFY]]` markers in the copy. Publishing blockers are image credits and licences (11 slots) only.
- Author: no named author in the inputs; package uses "Wedded Wonderland" pending confirmation.
- Image alt, caption, credit and licence: none supplied in `04-images.json`; left empty, not invented.
- `04-images.json` still uses generic file names for three slots: venue-04 (`mykonos-wedding-venues-south-coast-venue-ceremony-setting.webp`) is Mykonos Blu in the body, and venue-05 (`mykonos-wedding-venues-villa-venue-ceremony-setting.webp`) and area-villas-events (`mykonos-wedding-venues-villas-events-setting.webp`) are ZeNIT Events Center, an event venue, not a villa. The package uses the `04-images.json` file names as they stand. Normalise `04-images.json`.
- No image slot for Katikies Mykonos, Mykonos Grand, Saint John, Petasos or Myconian Ambassador in the body (none planned in `04-images.json`).
- The at-a-glance table has five columns and must scroll sideways on mobile; check in the mobile preview.
- Jump list anchors (#agios-ioannis-and-ornos, #psarou-and-platis-gialos, #elia, #agios-sostis-and-the-north-coast, #a-hilltop-event-venue-above-paradise-beach) and the #where-the-chapels-are link depend on the CMS generating heading IDs; check in preview.
- Booking checklist items flagged for confirmation before quoting: Mykonos Grand Orthodox rule, Katikies children over 13 and whole-hotel take-over, Mykonos Blu 2027 reopening date and ceremony types, Petasos ceremony location and types, Myconian Ambassador chapel location and size, Mykonos Lolita capacity and civil ceremony registration, which Myconian Elia hotel's chapel and ballroom, Saint John room count and which spaces reach 800, ZeNIT capacity, Santa Marina brochure; plus step-free access, transfers and whole-property closure at every venue.
- Deferred business items (person's decision): a real Mykonos or Greece wedding, fee model and commissions, an Advisor who calls first, referral or assistant contact, mobility checks by venue.

## Next step

Source and license the 11 images, then run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS, confirm the field map, then `/wedded-blog resume=mykonos-wedding-venues`. Nothing was published or scheduled.
