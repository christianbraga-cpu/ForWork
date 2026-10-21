# Run report: 8 Lake Como Villas You Can Book for an Exclusive-Use Wedding

- **Slug:** lake-como-villa-wedding-exclusive-use · **Run date:** 2026-10-21 · **Status:** Package ready, not uploaded (no browser in this cloud session; CMS field map not confirmed)
- **Draft:** not in the CMS. Upload `11-publish-package.json` + `11-body.md` (strip its front matter if the CMS needs plain body).
- **Test run:** yes

## Inputs
- Title given: "10 Lake Como Villas for an Exclusive-Use Wedding" → **changed to 8** (only 8 villas confirmed as exclusive-use from official sources)
- Keyword: lake como villa wedding exclusive use
- URL: /destination-weddings/lake-como-villa-wedding-exclusive-use · Type: Guide · Cluster: Getting Married in Italy · Primary category: Destination Weddings
- Audience (assumed, not given): Australian couples planning a luxury Lake Como wedding (AUD 150k+) comparing exclusive-use villas

## Gates
| Gate | Result | Rounds | Notes |
|---|---|---|---|
| G1 Brief | Pass | 1 | Comparison guide; primary persona planner_couple |
| G2 Research | Pass | 1 | DataForSEO, 10/10 locations |
| G3 Sources | Pass | 2 | 8 villas confirmed (2 borderline); 60 facts after top-up |
| G4 Images | Continued with placeholders | 1 | 12 slots all "needed"; permission emails skipped by person |
| G5 Edit | Pass with edits (4.29) | 1 | 25 edits; VERIFY markers 56 → 17 |
| G6 Reader panel | Revise (weighted enquiry 2.70) | 1 | Copy fixes applied; 6 business items deferred by person |
| G6b Final blocking check | Pass (4.43) | 1 | No blocking issues |
| G7 Package | Pass | 1 | validate.py: all valid |
| G8 CMS | Not run | | No browser connection; run /wedded-cms-discovery locally first |

## Before you publish: human checks
### [[VERIFY]] items (17)
- minimum nights, check-in and check-out times, and set-up and breakdown windows for each villa
- curfew times and outdoor music rules for each villa on the couple's dates
- in-house or approved-supplier rules for the remaining villas
- Nic sign-off on the Nulla Osta fee before publishing
- Villa Balbiano: total guests sleeping on site and whether other buildings add rooms; seated and standing capacity; minimum nights; music curfew; civil or symbolic ceremony on site; indoor space for dinner and ceremony
- Villa Sola Cabiati, with Grand Hotel Tremezzo: wedding terms; seated and standing capacity; minimum nights; music curfew; civil or symbolic ceremony on site; whether the indoor rooms serve as the rain plan, and for how many
- Relais Villa Vittoria: western-shore placement from an official source; room count and beds; standing capacity; minimum nights; music curfew
- Villa Pliniana: current room count and guest capacity with Sereno Hotels; minimum nights; music curfew; civil or symbolic ceremony on site; indoor ceremony option
- Villa Làrio: eastern-shore placement; room count and guests sleeping on site; seated and standing capacity; minimum nights; music curfew; indoor capacity for dinner and ceremony
- Villa Aura del Lago: whether the whole estate is exclusive during a wedding; standing capacity and marquee size; music curfew; whether a legal ceremony is possible on site; indoor ceremony option
- Villa Cipressi: room count; seated and standing capacity; exclusive-use minimum nights; music curfew and live music rules; current civil-ceremony status and whether non-residents can marry here; indoor capacity
- Villa Lario Resort: standing capacity; minimum nights; music curfew; indoor ceremony option
- Villa d'Este wedding buyout terms
- whether a legally binding civil ceremony can be held at Balbianello
- coach transfer times from Malpensa, Linate and Bergamo to each villa for the wedding date
- step-free access, lifts and accessible rooms at each shortlisted villa
- hotel-to-villa transfer times for each room-block town

### Prices needing Nic's sign-off
- Nulla Osta fee: "the euro equivalent of AUD 80 per Australian citizen" (Australian Embassy Rome, as at October 2026). No venue prices are printed.

### Images needed (12 slots, all placeholders)
- featured, exclusive-use-covers, villa-01 to villa-08, getting-there-boat, guests-stay-town (shot briefs in `04-images.json`)
- Permission emails skipped for this run (contacts saved in `04-images.json`: Balbiano, Pizzo, Sola Cabiati)
- Drive has Villa Balbiano photos and a 2023 Lake Como folder with no licence recorded; partner galleries on /venue pages need the supply agreement checked

### Deferred by you (business confirmation needed)
- Wedded Concierge fee model and whether commissions are taken
- Deposit, refund and contract terms
- A "From AUD" price range for exclusive-use villa weddings
- What Wedded Privileges is (no page; /privileges is a 404)
- A named Advisor / phone line / on-the-day contact
- A real wedding at one of the 8 villas

### Also confirm
- Author byline (package says "Wedded Wonderland")
- Two borderline villas: Villa Sola Cabiati (no wedding mention on its own pages) and Villa Aura del Lago (whole-estate exclusivity)

## What the reader panel said
- Weighted enquiry likelihood 2.70 / 5 (pass mark 3.8). All five readers said "maybe" to the CTA.
- Main blockers were the deferred business items (cost, fee model, contracts, real wedding).
- Fixed: "town to confirm" removed, one "not published" line per villa, 5-column phone-friendly table, airports and guest towns, older-guest access questions, "couples anywhere" line.
- Kept: exclusive-use definition, "beds not dinner seats", Nulla Osta section, ferry detail, Vittoria 30-guest rule, Pliniana details, "we have not printed a fee", AUD and fee-in-writing line.

## Research summary
- SERP source: DataForSEO (all 10 cities). No weddedwonderland.com page in any top 10; /best-lake-como-wedding-venues ranks 69 to 94.
- Volumes (AU/US monthly): "lake como wedding venues" 210/2,900; "lake como wedding villa" 10/90; target phrase no measurable volume.
- Gap targeted: no ranking page limits itself to verified exclusive-use villas or compares house rules.

## Links
- Internal: Lake Como hub, legal guides, cost guide, packages page, /venue/villa-balbiano, /wonderland-concierge (CTAs + inline, all UTM-tagged), /travel, /destination-wedding-guide (lead magnet)
- Backlinks to add from older pages: see `backlinks-todo.md`

## Distribution assets
- 3 Pinterest pins, 8-slide Instagram carousel, newsletter blurb (`10-distribution.json`). Need licensed images before posting.

## Tools used
- DataForSEO, Firecrawl, Apify (fallback fetch), Google Drive, validate.py, scan_copy.py
- Gmail drafts: declined; CMS upload: not available
