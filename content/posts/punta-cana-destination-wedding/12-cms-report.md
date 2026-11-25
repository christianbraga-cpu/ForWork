# CMS report: punta-cana-destination-wedding

**Draft URL / ID:** Not uploaded. No browser in this cloud session, and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED` (not CONFIRMED). Nothing was saved, scheduled or published in the CMS. A human saves as Draft; a human clicks Publish.

**After saving the draft, check the URL is exactly https://weddedwonderland.com/destination-weddings/punta-cana-destination-wedding. The category bug has moved earlier posts (for example /wedding-rsvp-website to /expert-advice/wedding-rsvp-website, and /expert-advice/should-you-marry-legally-abroad-or-have-a-symbolic-ceremony to /expert-advice/symbolic-ceremony). If it differs, do not publish; fix the primary category or confirm with the dev team first.**

- Date: 2026-11-25
- Title / H1: Punta Cana Destination Wedding Guide (36 characters)
- Package: `content/posts/punta-cana-destination-wedding/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/punta-cana-destination-wedding/11-body.md`
- Booking checklist: `content/posts/punta-cana-destination-wedding/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/punta-cana-destination-wedding (slug `punta-cana-destination-wedding`)
- Categories: Destination Weddings (primary, = categories[0], set explicitly), Dominican Republic (existence not confirmed, see below), Planning Guides. No Latin America & Caribbean category.
- New article; no redirect.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter and META comments removed, H1 is the title, all `<!-- fact_xx -->` markers removed, prose, links and UTMs unchanged (diff clean)
- [x] Only the 4 IMAGE SLOT comments kept. **No CTA marker comments added** (user rule). `08-final.md` had no `<!-- CTA: primary -->` marker, so nothing was replaced; the CTAs are the inline links already in the copy (primary, secondary, magnet, closing; each utm_content appears once)
- [x] No `[[VERIFY]]` markers in the copy (none in `08-final.md`)
- [x] Key takeaways (4) and FAQ (6) taken verbatim from the body
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] Meta title "Punta Cana Destination Wedding Guide for Luxury Couples" (55); meta description from the META comment (148); focus keyword "punta cana destination wedding"; canonical set; OG image = featured slot
- [x] Excerpt = the meta description (no excerpt in any stage file; the opening paragraph is 329 characters, over the 300 limit)
- [x] schema_jsonld: Article (author and publisher Wedded Wonderland, datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (6, links reduced to anchor text)
- [x] Images: 4 Punta Cana slots, all `needed`; alt and caption left empty (nothing invented)
- [x] No prices in the copy. fact_023 (the JCE civil registry fee) is in `needs_signoff` for Nic only
- [x] Legal H2 carries "General information as at November 2026, not legal advice"; so does the legal FAQ answer
- [x] Nothing implies the Wedded Advisor handles legal paperwork (the body says the registry booking, documents and timing remain the couple's responsibility)
- [x] draft_note: "DRAFT. Do not publish until checked:" + Nic sign-off items, image slots, category check, URL check, byline
- [x] No em dashes; Australian English
- [x] `python3 -I content-system/scripts/validate.py content/posts/punta-cana-destination-wedding`: All valid (14 files)

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (it says NOT YET MAPPED)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 4)
- [ ] Logged into the CMS in a Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=punta-cana-destination-wedding once the field map is confirmed)

1. Source and upload the 4 images with alt text and captions; set the featured image (see Images below).
2. Title "Punta Cana Destination Wedding Guide", slug `punta-cana-destination-wedding`, excerpt, author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md`; fill the Key Takeaways block (4) and the FAQ (6). If the template has a CTA block, do not add a second copy of the primary link; the CTAs are already inline.
4. Categories: Destination Weddings, Dominican Republic (only if it exists), Planning Guides. Then **set Destination Weddings as the primary category explicitly**. Never pick a Latin America & Caribbean category. Add the 8 tags.
5. SEO: meta title, meta description, focus keyword, canonical, OG image (featured); schema JSON-LD if the CMS has a field.
6. Paste `draft_note` into the internal note field, then **Save Draft**. Never Publish or Schedule.
7. **Check the URL** is exactly https://weddedwonderland.com/destination-weddings/punta-cana-destination-wedding.
8. Preview desktop and mobile: images, links (9 external official links to 7 URLs, 8 internal links, plus the 4 UTM links), breadcrumb (Home > Destination Weddings > post), and the italic legal notice under the legal H2.

## Images (4 slots, all needed)

| Slot | Role | Brief |
|---|---|---|
| featured | featured | Beach ceremony set-up on the sand, no guests seated |
| wet-weather-ceremony | inline | Covered or shaded ceremony space (gazebo, palapa, pergola or covered terrace) |
| welcome-event | inline | Guest welcome drinks, no identifiable people without written consent |
| reception-dusk | inline | Beachfront reception at blue hour |

- Real Punta Cana locations only: licensed or owned, **never AI**.
- Location verified by register row, EXIF GPS or the photographer's named gallery; month taken recorded so the caption and any season reference are true.
- No resort names, logos, signage, wristbands or branded linen. Captions name the town only.
- People only with written consent; no identifiable children.
- No images in the register (library-index.csv has no Punta Cana, Dominican Republic or Caribbean rows); 10-distribution pins are on hold for the same images.

## Mismatches and open points

- Field map not mapped, so no CMS labels could be compared with the package. Run `/wedded-cms-discovery` first.
- **Dominican Republic category: not confirmed.** There is no Dominican Republic category archive in `link-map.csv` (category listings seen include /blog/destination-weddings, /blog/europe, /blog/united-states-of-america, but none for the Dominican Republic). Confirm it exists in the CMS before assigning. If it doesn't, ask the content owner whether to create it; do not substitute a Latin America & Caribbean category. Planning Guides is also not visible as an archive in the link map; confirm it too.
- Nic: fact_023 (JCE civil registry fee) is held for Nic only and is not in the copy; and the 07-panel item on whether the post may explain how the Wedded Advisor fee works is still open (no fee, commission or scope wording until signed off).
- Author: no named author in any input.
- Breadcrumb level 2 uses https://weddedwonderland.com/destination-weddings, which is not a row in `link-map.csv`; confirm the category archive URL.
- Internal link `/expert-advice/symbolic-ceremony` is the live target the older symbolic-ceremony URL now 301s to (link map, seen 2026-11-24); check it resolves in preview.
- The tag "Caribbean weddings" is from the brief and is a tag, not a category.
- Lines dated "As at November 2026" (Smartraveller, the legal notice) need rechecking if publishing slips past November 2026.
- 02-seo verify items (NHC peak date, Santo Domingo normals, flight routes) are not claims in the copy, so they don't block. The source-pack items on the Australian single-status document, notice period, days in country, witnesses or padrinos and name change are written in the article as questions to check, and are in `booking-checklist.md`.
- `09-cro.json` open questions (Advisor fee model, commissions, who is accountable on the day, private channel, scale) are for /wonderland-concierge, not this post.
