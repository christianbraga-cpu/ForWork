# CMS report: australia-real-wedding

**Draft URL / ID:** Not uploaded. Package-only mode: the person uploads the post from the Word doc. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not CONFIRMED). Nothing was saved, scheduled or published in the CMS. A human saves as Draft; a human clicks Publish.

**After saving the draft, check the URL is exactly https://weddedwonderland.com/real-weddings/australia-real-wedding (path `/real-weddings/australia-real-wedding`). The CMS category bug has moved earlier posts. If it differs, do not publish; fix the primary category or confirm with the dev team first.**

**Real wedding cards: confirm before publishing.** The twelve cards under the coast, country, city, garden and island groups are text summaries of our own published stories, each linked to the full story. `content-system/brand/brand-facts.md` lists "Real weddings we can feature (with consent)" as deferred, so a person should confirm the twelve couples may be featured on this page before publishing. Cards run text-only: an image goes on a card only if it comes from that same wedding's gallery and the register shows the licence and couple consent. Never AI for a real wedding, venue or destination.

**Nick and Lauren:** their story (`/a-refreshing-byron-bay-wedding`) is filed under Fashion and Uncategorized, not Real Weddings (tagged "real wedding"; no sponsored label seen by the editor). Confirm it is an editorial real wedding and not a paid feature before publishing. If it is paid, remove the card.

**Robots recheck:** meta robots were not read for the 8 newly mapped stories (Firecrawl credits exhausted; all returned 200 with a self canonical): Jennifer and Emrah, Stephanie and Simon, Stephanie and Daniil, Kathryn and Ben, Nick and Lauren, Sarah and Damien, Stephanie and Arthur, Jessica and Jarrod. Recheck each is indexable before publishing.

**Legal content:** "The legal steps" and the three legal FAQs are general information as at November 2026, not legal advice (the copy says so). If publishing is delayed, recheck against the Attorney-General's Department first.

**Australia category:** unconfirmed. `01-brief.json` lists "Australia" as a category, but it was inferred from link map topics and nothing confirms it exists in the CMS (the brief suggests "Australia & Pacific" or dropping it). It is left out of the package. Add it only once confirmed in the CMS, after Real Weddings.

- Date: 2026-11-26
- Plan ref: none in any input
- Title / H1: Australia Real Weddings From Coast to Country (45 characters)
- Meta title: Australia Real Weddings From Coast to Country (45)
- Meta description: Australia real wedding stories from our own pages, grouped by coast, country, city, garden and island, with the questions to ask your venue first. (146, from `02-seo.json`)
- Focus keyword: australia real wedding
- Package: `content/posts/australia-real-wedding/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/australia-real-wedding/11-body.md`
- Booking checklist: `content/posts/australia-real-wedding/booking-checklist.md`
- Target URL: /real-weddings/australia-real-wedding (slug `australia-real-wedding`); canonical https://weddedwonderland.com/real-weddings/australia-real-wedding
- Categories: Real Weddings (primary, = categories[0], set explicitly), Destination Weddings. Australia: unconfirmed, not added.
- Tags: australia real wedding, real weddings australia, australian weddings, beach wedding, vineyard wedding, garden wedding, island wedding, notice of intended marriage
- Status: Draft only. Never Publish or Schedule.
- New article; no redirect.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter and META comments removed, H1 is the title, all 13 `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, prose unchanged (line diff against `08-final.md` shows only those items)
- [x] All 27 links and the 4 UTM links kept exactly as in `08-final.md`, same order; internal links relative (3 external: Attorney-General's Department celebrant register, Bureau of Meteorology climate table, Cancer Council sun safety); no `/destinations/africa` or `/destinations/latin-america-caribbean` link
- [x] LINK comment kept in "Real weddings in Australian gardens": `<!-- LINK: /real-weddings/garden-wedding when live (anchor: garden wedding ideas and what to plan for) -->` (draft, 404 on 2026-11-26). Add the link when the garden facet is live.
- [x] No `<!-- CTA: primary -->` marker in `08-final.md`, so nothing replaced; no CTA marker comments added. CTA links in place per `09-cro.json`: primary (opening paragraph of "What these weddings share"), magnet (end of "Keeping the guest list close"), secondary (end of "Guests who fly in"), closing; each utm_content appears once
- [x] No `[[VERIFY]]` markers in the copy (none in `08-final.md`)
- [x] Key takeaways (4) and FAQ (5) taken verbatim from the body
- [x] Excerpt: the opening paragraph, verbatim (189 characters)
- [x] Categories and tags from the brief (Australia left out as unconfirmed); primary_category = Real Weddings
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Real Weddings > post) + FAQPage (5)
- [x] Images: 6 slots, all `needed`; alt and caption left empty (nothing invented); no AI images
- [x] No prices; needs_signoff empty (nothing for Nic)
- [x] draft_note: "DRAFT. Do not publish until checked:" + image slots, real wedding consent, Nick and Lauren, robots recheck, legal date, venue-name slugs, LINK comment, Australia category, URL check, byline
- [x] No em dashes; Australian English
- [x] `python3 -I content-system/scripts/validate.py content/posts/australia-real-wedding`: All valid

## CMS checklist (Part 2: not run, package-only mode)

- [ ] `cms/field-map.md` status is CONFIRMED (it says NOT YET MAPPED)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 6)
- [ ] Upload: not started (the person uploads via the Word doc)
- [ ] After save: not started

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person)

1. Confirm the twelve real wedding couples may be featured, and that Nick and Lauren's story is not a paid feature (see above).
2. Recheck robots for the 8 newly mapped stories.
3. Source and upload any approved images with alt text and captions; set the featured image (see Images below). If none are approved, the cards run text-only.
4. Title, slug `australia-real-wedding`, excerpt, author (byline to confirm; package uses "Wedded Wonderland").
5. Paste the body from `11-body.md` (or the Word doc); fill the Key Takeaways block (4) and the FAQ (5). Use the CTA links as they are in the body; don't add a second primary CTA link.
6. Categories Real Weddings and Destination Weddings, then **set Real Weddings as the primary category explicitly**; add Australia only if it is confirmed to exist. Add tags.
7. SEO: meta title, meta description, focus keyword, canonical, OG image (featured); schema JSON-LD if the CMS has a field.
8. Paste `draft_note` into the internal note field, then **Save Draft**. Never Publish or Schedule.
9. **Check the URL** is exactly /real-weddings/australia-real-wedding.
10. Preview desktop and mobile: images, links (the twelve story links, the three external sources), CTA, breadcrumb (Home > Real Weddings > post).

## Images (6 slots, all needed)

| Slot | Role | Sits in | Rule |
|---|---|---|---|
| featured | featured | Under the H1 | Australian coastal headland or clifftop ceremony set for guests; 16:9 with room for a title overlay; no identifiable guests or children without consent |
| real-wedding-cards | inline | Each story card | One image per card, only from that same wedding's licensed gallery, with wedding_id, licence, credit and couple_consent = yes in the register; otherwise text-only. Never a stand-in |
| coast | inline | "Real weddings by the coast and beach" | Beach or coastal lawn set for a ceremony; no tide, season or weather claims |
| country-vineyard | inline | "Real weddings in country and vineyard settings" | Long table or ceremony seating by vines or paddocks; no grape, harvest or season claims |
| city | inline | "Real weddings in the city" | Skyline view or heritage interior; no branding or fit-out that names a venue |
| island-reef | inline | "Real weddings on an island" | Queensland reef island setting; no resort buildings or branding; no weather claims unless BoM-sourced |

- Licensed or owned only, registered in `library-index.csv` (0 rows today); **never AI** for a real wedding, venue or destination; competitor or search images only to `reference-only/`.
- People only with written couple and guest consent; no children unless consent is recorded.
- Keep venue names out of image file names (Paige and Todd's and Stephanie and Daniil's story slugs contain venue names).

## Mismatches and open points

- Field map not mapped, so no CMS labels could be compared with the package. Run `/wedded-cms-discovery` before any automated upload.
- Real-wedding features need consent per brand-facts (deferred); see above.
- Nick and Lauren filed under Fashion; confirm not a paid feature; see above.
- Robots not read for 8 newly mapped stories; see above.
- Australia category unconfirmed; see above.
- Venue names in link slugs (link address only; anchors and copy use the couple's names): Paige and Todd (`/an-autumn-garden-wedding-at-burnham-grove-estate`), Stephanie and Daniil (`/real-wedding-ballet-couple-tie-the-knot-at-australias-wandin-valley`). Confirm acceptable.
- Stephanie and Simon links to `/real-wedding-stephen-and-simon` (the live slug says "stephen"); kept exactly as in `08-final.md`.
- Stephanie and Arthur: the story never pairs the names; the card uses bride first per `02-seo.json` and the editor. Confirm.
- `09-cro.json` quotes an earlier wording of the secondary CTA sentence; the `08-final.md` wording is kept unchanged ("For a wedding in Australia or abroad, a Wedded Advisor at Wedded Concierge plans the venue, travel, vendors and payments, keeps to your time zone and quotes in AUD for Australian couples.").
- `04-images.json` is still `needs_input` (register empty). Re-run stage 04 once images or consent exist.
- Author: no named author in any input.
- Breadcrumb level 2 uses https://weddedwonderland.com/blog/real-weddings (the live real weddings listing in `link-map.csv`); confirm the category archive URL the CMS outputs.
- Backlinks to add (from `02-seo.json`): `/blog/real-weddings` (hub row or module), `/real-weddings/garden-wedding` (draft), `/real-weddings/beach-wedding`, `/these-real-weddings-in-victoria-are-completely-stunning`, `/a-picturesque-wedding-on-hayman-island` (and the same line on each featured story).
- `10-distribution.json`: pins, carousel and newsletter image are on hold until images are licensed (with a scope covering social use) and approved; Pinterest boards "Australian Weddings" and "Country and Vineyard Weddings" may need creating; set the Instagram bio link while the carousel runs.
- `09-cro.json` open questions (fee model, commissions, deposits, a first phone call, on-the-day contact, Advisor identity, whether we planned the featured weddings, scale, confidentiality) are for /wonderland-concierge, not this post. Its suggested printable venue question checklist is the basis of `booking-checklist.md`, not placed on the site.
- Questions for couples are in `booking-checklist.md` and don't block publishing.
