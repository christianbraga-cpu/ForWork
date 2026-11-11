# CMS report: corfu-wedding-venues

**Draft URL / ID:** Not uploaded: no browser connection in this session and the CMS field map is not yet confirmed (run /wedded-cms-discovery locally)

- Date: 2026-11-11
- Title: 10 Corfu Wedding Venues With Sea Views (changed from the person's "12 Corfu Wedding Venues With Sea Views" because only 10 venues qualify)
- Package: `content/posts/corfu-wedding-venues/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/corfu-wedding-venues/11-body.md`
- Booking checklist: `content/posts/corfu-wedding-venues/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/corfu-wedding-venues (CMS slug `corfu-wedding-venues`)
- Primary category: Destination Weddings (= categories[0]); type Guide; cluster Getting Married in Greece
- New article, no redirect

## Package build (Part 1)

- [x] Confirmed `08-final.md` already carries the `09-cro.json` copy changes (primary marker filled after the table, secondary inline link closing the Kommeno section, closing brand-facts line) and the 8b edits
- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 12 image-slot comments kept, 3 `[[VERIFY]]` markers kept
- [x] Primary CTA block (Speak with a Wedded Advisor, subtext "The fee is agreed in writing before any work begins.") at the `<!-- CTA: primary -->` marker; the inline sentence after it retagged `utm_content=inline` (as the Crete model); secondary, closing and lead magnet links marked with comments; each `utm_content` link appears once
- [x] Key takeaways: exactly the 4 in the body, copied verbatim; FAQ (6) extracted
- [x] Categories: Destination Weddings, Greece, Venues; primary_category = Destination Weddings; tags (7) from the brief, with "Paleokastritsa" replaced by "Ermones"
- [x] Meta title "Corfu Wedding Venues: 10 With Sea Views" (from `02-seo.json`); meta description rewritten because the SEO version named Kassiopi and Paleokastritsa, where no venue qualified: "Corfu wedding venues with sea views, from Kommeno and Corfu Town to Kalami, Benitses and Ermones, compared on ceremony options, capacity and exclusive use." (155 characters); focus keyword, canonical, OG image slot (featured)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + ItemList (10 venues, official URLs) + FAQPage (6)
- [x] Images: 12 slots in the body (featured, 5 areas, 6 venues), all `needed`
- [x] verify_items: the 3 `[[VERIFY]]` items in the copy (Villa Medusa table cell, Villa Medusa sea view line, Corfu Holiday Palace fresco room), image credits and licences (12) and jump list anchors (1); needs_signoff empty (no prices)
- [x] draft_note: VERIFY items, linked drafts to publish together, mobile table scroll, jump list, image slots, deferred business items
- [x] redirects_recommended: none (new article)
- [x] `python3 -I content-system/scripts/scan_copy.py content/posts/corfu-wedding-venues/11-body.md`: no banned words, 0 dashes, no overlaps; flagged "exclusive" 15 (expected in a venue guide comparing exclusive use), "beautiful" 1, "luxury" 1, "luxurious" 1 (all inside venues' own quoted wording; no change made)
- [x] `python3 -I content-system/scripts/validate.py content/posts/corfu-wedding-venues`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 12 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Publish together

The body links three drafts: /destination-weddings/greece-wedding-venues (twice), /destination-weddings/greece-wedding-packages (once) and /expert-advice/greek-wedding-traditions (once). Publish the Greece venues guide, the Greece packages guide and Greek wedding traditions together with this post, or hold this post until they are live. The Greece venues and packages guides should link down to this post where they mention Corfu.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- `[[VERIFY]]` markers in the copy (publishing blockers): Villa Medusa identity and "Direct Sea View" (table cell and venue entry), and whether Corfu Holiday Palace's Nafsika Hall with the fresco is the Nausica Ballroom.
- Author: no named author in the inputs; package uses "Wedded Wonderland" pending confirmation.
- Image alt, caption, credit and licence: none supplied in `04-images.json`; left empty, not invented.
- `04-images.json` still describes venue-03 to venue-06 as unnamed placeholders with generic file names (dassia-venue, corfu-town-venue, north-east-venue, west-coast-venue), while the body slots are Rodostamo (venue-03), Corfu Holiday Palace (venue-04), San Antonio (venue-05) and Atlantica Grand Mediterraneo (venue-06); its area slots still mention Dassia, Kassiopi and Paleokastritsa. The package uses the `04-images.json` file names as they stand. Normalise `04-images.json`.
- No image slot for Villa Medusa, Eva Palace, Corfu Palace Hotel or The Courti Estate in the body (none planned in `04-images.json`).
- Corfu Palace Hotel publishes no wedding web page; its ItemList URL is the official 2023 wedding proposals PDF linked in the body. Its terms are dated 2023 (the copy says so), so current terms and the sea-view wording go on the booking checklist.
- The at-a-glance table has six columns and must scroll sideways on mobile; check in the mobile preview.
- Jump list anchors (#kommeno, #corfu-town-and-kanoni, #kalami-and-the-north-east, #benitses-and-the-south-east, #ermones-and-the-west-coast) depend on the CMS generating heading IDs; check in preview.
- Booking checklist items flagged for confirmation before quoting: Corfu Palace current terms and sea-view wording, Villa Medusa identity, Holiday Palace fresco room, Angsana legal ceremony option, airport transfer times for San Antonio, Angsana and The Courti Estate; plus step-free access, transfers and whole-property closure at every venue.
- Deferred business items (person's decision): a real Corfu or Greece wedding, fee model and commissions, an Advisor who calls first, referral or assistant contact.

## Next step

Resolve the three `[[VERIFY]]` items, then run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS, confirm the field map, then `/wedded-blog resume=corfu-wedding-venues`. Nothing was published or scheduled.
