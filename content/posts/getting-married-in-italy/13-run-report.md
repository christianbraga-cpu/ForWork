# Run report: Getting Married in Italy as an Australian

- **Slug:** getting-married-in-italy  ·  **Run date:** 2026-10-26 to 2026-10-27  ·  **Status:** Package ready (no Chrome)
- **Draft:** not uploaded (no Chrome in the cloud session; CMS field map not yet confirmed)
- **Word file:** `getting-married-in-italy-draft.docx`

## Inputs
- Title: Getting Married in Italy as an Australian
- Keyword: getting married in italy as an australian (corrected by the person mid-run; "getting married in italy" is secondary)
- Audience: Australian couples in their 30s, affluent, about AUD 130k budget
- URL: /destination-weddings/getting-married-in-italy · Type: Legal · Cluster: Getting Married in Italy · Primary category: Destination Weddings

## Gates
| Gate | Result | Rounds | Notes |
|---|---|---|---|
| G1 Brief | Pass (0.82) | 1 | AU-specific legal guide; overlap with the general /expert-advice/ legal guide handled by linking |
| G2 Research | Pass (0.80) | 1 | DataForSEO 10/10 locations; scope au_focus; report.md saved from payload |
| G3 Sources | Pass (0.85) | 1 | 45 official facts; Atto Notorio added as a must-include |
| G4 Images | Pass (0.85) | 1 | 7 slots, all placeholders |
| G5 Edit (avg score) | Pass with edits (4.57) | 1 | 17 edits, 0 blocking |
| G6 Reader panel (weighted) | Revise (enquire 2.0) | 1 | 3 must-fix copy items applied; gap is mostly deferred business answers and the fee decision |
| G6b Final blocking check | Revise, then 0 blocking | 1 | 2 one-sentence fixes applied |
| G7 Package | Pass | 1 | validate.py: all valid |
| G8 CMS | Not run | | No browser connection; run /wedded-cms-discovery locally first |

## Before you publish: human checks
### [[VERIFY]] items (2)
- Italy offers same-sex couples a civil union, not marriage (confirm against Law 76/2016 and D.Lgs. 7/2017)
- How Australia treats an Italian unione civile (no Australian government source found as at October 2026)

### Booking checklist (not publishing blockers)
- See `booking-checklist.md` (5 items: Embassy/Consulate-General, state consulate, comune, Catholic parish, Prefettura)

### Prices needing Nic's sign-off
- None. No fee figures are printed; every fee reads "a fee applies".

### Questions for you
- Print official government fees with an "as at" date (needs Nic)? Source pack has DFAT apostille A$105 (2026), marca da bollo EUR 16, Sydney Atto Notorio EUR 28; the Nulla Osta fee conflicts across official pages (A$80 / A$88 / A$90).
- Does Wedded Concierge book the Nulla Osta appointment, find interpreters and attend the Prefettura and comune with couples? If yes, add to brand-facts.md.
- Byline: package uses "Wedded Wonderland"; confirm.

### Images needed (7 slots, all placeholders)
- featured, piazza, documents, civil-ceremony, symbolic-ceremony, certificate, same-sex (shot briefs in `04-images.json`)
- No licensed Italy wedding images in the Drive library or Canva; "Italy Inspires" event photos are unregistered and not used

### Low-confidence stages (< 0.7)
- None

### Deferred by you (business confirmation needed)
- Fee model and commissions; deposits, refunds and contracts; "From AUD" ranges; Wedded Privileges; named Advisor and phone line; a real wedding to feature

## What the reader panel said
- Must-fix (and how it was fixed): who does what (sourced in-person steps added, Advisor claims limited to brand facts); "Your Wedded Advisor confirms" cut from 10 to 3; quieter close with "the fee is agreed in writing before any work begins"
- Also applied: Australians living abroad, two-column timeline table for phones, a "start early" takeaway (still 4), privacy line, plain-English glosses, CTA reworded for couples without a date
- Kept because it worked: the opening CNI correction, consulate-by-consulate detail, Embassy quote, "Not published" honesty, recognition and surname section, FAQ

## Research summary
- SERP source: DataForSEO (10 cities), Firecrawl page reads
- Locations checked / failed: 10 / 0 (one Dubai Arabic call retried)
- Gap we're targeting: competitors are outdated or contradict each other on fees, validity and witnesses; a source-traced Australian guide with a timeline from Australia
- Rankings: weddedwonderland.com has no AU top-100 ranking for these terms yet
- Search Console: only export in Drive is from 2025-05-14 (not used); upload a current one
- Link map: 3 live pages missing (/destination-weddings/wedding-planner-italy, venice legal, is gay marriage legal in italy); run /wedded-linkmap

## Links
- Internal: /destinations/europe/italy, the general legal guide, register-an-overseas-marriage, legal vs symbolic, same-sex abroad, /wonderland-concierge
- External (official): Embassy Rome PDF, Italian Consulate Sydney, Smartraveller (2), DFAT notarial fees
- Backlinks to add from older posts: see `backlinks-todo.md` (one older page wrongly calls the Nulla Osta a CNI; correct it)

## Distribution assets
- See `10-distribution.json`: 3 Pinterest pins, 8-slide Instagram carousel, newsletter section

## Tools used
- DataForSEO (SERP, volume, difficulty, related, ranked keywords), Firecrawl (scrape, search, map), Google Drive, Canva, scripts: validate.py, scan_copy.py, md_to_docx.js
