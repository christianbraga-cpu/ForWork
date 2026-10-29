# Run report: Are Lab-Grown Diamonds Worth It?

- **Slug:** lab-grown-diamonds (CMS slug as given)  ·  **Run date:** 2026-10-29  ·  **Status:** Package ready (no Chrome)
- **Mode:** fast mode. Started 00:14 UTC, first draft 00:32, package 00:41. About 28 minutes in total.
- **Draft:** not uploaded (no Chrome in the cloud session; CMS field map not yet confirmed)
- **Word file:** `lab-grown-diamonds-draft.docx`

## Inputs
- Title: Are Lab-Grown Diamonds Worth It?
- Keyword: lab grown diamonds (leading space trimmed)
- Audience: couples in their 30s, affluent, destination weddings and luxury experiences, AUD 150k+
- URL: /style-advice/lab-grown-diamonds · Type: Guide · Cluster: Rings and Jewellery · Primary category: Style Advice

## Time per stage (fast mode)
| Stage | Time |
|---|---|
| Brief | 1 min |
| Images, fact-check (in parallel with SEO) | 2 min, 15 min |
| SEO research (no Firecrawl) | 11 min |
| First draft | 3 min |
| Editor and 5 readers (in parallel) | 3 min |
| Panel chair | 2 min |
| Final copy | 1 min |
| Final check, CTA, social (in parallel) | 2 min |
| Package and finish | 4 min |

## Gates
| Gate | Result | Rounds | Notes |
|---|---|---|---|
| G1 Brief | Pass | 1 | Answers "worth it" without prices: values, grading, disclosure, resale caution |
| G2 Research | Pass | 1 | 5 cities; 12,100/mo AU, difficulty 27; this post owns "lab grown vs natural diamond" (1,000/mo) |
| G3 Sources | Pass | 1 | 27 facts; GIA's current lab-grown report format confirmed via Apify; resale and energy facts unsourced, so left out |
| G4 Images | Needs input | 1 | 7 slots, all placeholders |
| G5 Edit (avg score) | Pass with edits (4.43) | 1 | 8 edits: unsourced cost cell and legal "Yes." fixed, IGI "LG" prefix added, keyword H2, settings link |
| G6 Reader panel (weighted) | Revise (enquire 1.7), 1 must-fix | 1 | Australian Consumer Law moved above the US FTC rules |
| G6b Final blocking check | 5 one-sentence fixes, then 0 blocking | 1 | Unsourced "age and rarity" wording, an implied "we sell no jewellery" line, cost and legal wording tightened |
| G7 Package | Pass | 1 | validate.py: all valid |
| G8 CMS | Not run | | No browser connection |

## Before you publish: human checks
### [[VERIFY]] items (body has none)
- Image: approve "Illustrative image" AI artwork for featured, growth_methods, side_by_side and laser_inscription, or buy licensed stock
- Image: the sample_report mock-up callouts must match GIA's current lab-grown report (Premium or Standard, from 1 October 2025)

### Also before publishing
- Publish the diamond buying guide and ring cuts posts first (both linked), or remove those links
- Spot-check: IGI "LG" inscription prefix, GIA's lab-grown quality assessment details, ACCC green-claims page

### Prices needing Nic's sign-off
- None. No prices printed (three readers asked for a price gap; left out under your no-prices rule).

### Images needed (7 slots, all placeholders)
- featured, side_by_side, laser_inscription, ring_on_hand: licensed photography preferred
- growth_methods, sample_report, decision_checklist: brand graphics built in Canva (no GIA or IGI layouts or logos)

### Questions for you
- Can we say in print that Wedded Wonderland sells no diamonds or rings? Readers trusted "We sell neither." but it isn't in the brand facts, so it was removed. If Nic confirms it, it goes back into the intro.
- Pinterest board names in 10-distribution.json are guesses; confirm
- Top up Firecrawl credits (still returning 402)
- Byline: "Wedded Wonderland"; confirm

### Deferred by you (business confirmation needed)
- Fee model and commissions (including any jeweller referral fees); deposits and payment protection; named Advisor and phone line; private-client route; a real wedding to feature

## What the reader panel said
- Applied: ACL before FTC, cost line pointing to the ring budget article (no prices), who Wedded Wonderland is, travel insurance line, shorter HPHT detail
- Kept because it worked: the money-neutral opening, the paperwork checklist, "Worth it if, think twice if", the heirloom section, dated sources
- Pattern across the ring posts: readers trust the sourcing but enquire little from a ring article; they want the fee model and a real wedding (both deferred)

## Research summary
- SERP: DataForSEO, Sydney, Melbourne, New York, Dubai, Singapore
- Volume (AU): lab grown diamonds 12,100; lab grown diamond engagement rings 4,400; lab grown vs natural diamond 1,000
- Gap we're targeting: a seller-neutral answer that separates settled facts (material, grading, naming rules) from the uncertain (value, environmental claims), with Australian rules first

## Links
- Internal: /wonderland-concierge (primary CTA), /destinations (secondary), ring budget article, diamond buying guide, ring cuts, ring styles, ring settings
- External: GIA 4Cs lab-grown page, GIA lab-grown service, eCFR Part 23 (FTC Guides), FTC 2019 warning letters, ACCC false or misleading claims
- Backlinks to add: see `backlinks-todo.md`

## Distribution assets
- See `10-distribution.json`: 3 Pinterest pins, 8-slide carousel, newsletter section

## Validation
- validate.py: all valid · scan_copy.py: 0 banned, 0 dashes, 0 overlaps
