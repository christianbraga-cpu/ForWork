# Run report: Engagement Ring Insurance and How to Get It

- **Slug:** engagement-ring-insurance (CMS slug as given)  ·  **Plan ref:** WW-049  ·  **Run date:** 2026-10-29  ·  **Status:** Package ready (no Chrome)
- **Mode:** fast mode. Started 22:41 UTC, first draft 22:54, package 23:02. About 23 minutes in total.
- **Draft:** not uploaded (no Chrome in the cloud session; CMS field map not yet confirmed)
- **Word file:** `engagement-ring-insurance-draft.docx`

## Inputs
- Title: Engagement Ring Insurance and How to Get It
- Keyword: engagement ring insurance
- Audience: couples in their 30s, affluent, destination wedding and other luxury experiences, AUD 150k+
- URL: /style-advice/engagement-ring-insurance · Type: Guide · Cluster: Rings and Jewellery · Primary category: Style Advice · Plan ref: WW-049 (no plan document with this ref in the repo; recorded as given)

## Time per stage (fast mode)
| Stage | Time |
|---|---|
| Brief | 1 min |
| Images, fact-check (in parallel with SEO) | 1 min, 8 min |
| SEO research (no Firecrawl) | 10 min |
| First draft | 2 min |
| Editor and 5 readers (in parallel) | 2 min |
| Panel chair | 2 min |
| Final copy | 1 min |
| Final check, CTA, social (in parallel) | 2 min |
| Package and finish | 4 min |

## Gates
| Gate | Result | Rounds | Notes |
|---|---|---|---|
| G1 Brief | Pass | 1 | Neutral Australian checklist; general information only; no insurer names, no premiums or limits |
| G2 Research | Pass | 1 | 5 cities; 1,600/mo AU, difficulty 0; page one is almost all insurer sales pages, no regulator or neutral page ranks |
| G3 Sources | Pass | 1 | 24 facts from JAA, Moneysmart, Smartraveller, AFCA, Insurance Council, plus GIA travel advice (read via Apify) |
| G4 Images | Needs input | 1 | 7 slots, all placeholders |
| G5 Edit (avg score) | Pass with edits (4.14) | 1 | 13 edits: TMD added to the compliance line, 3 advice-like sentences made neutral, 5 claims tightened to their sources |
| G6 Reader panel (weighted) | Revise (enquire 1.7), 2 must-fix | 1 | Generic Advisor line replaced with ring handover planning; "first idea to the last dance" cut |
| G6b Final blocking check | 2 one-sentence fixes, then 0 blocking | 1 | Advisor no longer implied to look after the rings; "only Australian sources" corrected (GIA and IGI are cited) |
| G7 Package | Pass | 1 | validate.py: all valid |
| G8 CMS | Not run | | No browser connection |

## Before you publish: human checks
### [[VERIFY]] items
- What a Target Market Determination (TMD) is, in plain words: needs an ASIC or Moneysmart page (both returned 404 today). Or drop the definition and keep only "read the PDS and TMD".

### Also before publishing
- The General Insurance Code of Practice was redrafted and sent to ASIC on 22 October 2026: recheck the Code wording (no figures are stated)
- Publish the diamond buying guide and lab-grown posts first (both linked), or remove those links
- Written as "check your policy" because no neutral source covers it: specified vs blanket contents cover, AFCA time limits, Code timeframes, whether a stone lost from its setting counts as loss or damage, how valuers treat lab-grown stones, when cover starts on a standalone policy

### Prices needing Nic's sign-off
- None. No premiums, excess amounts, limits or percentages printed.

### Images needed (7 slots, all placeholders)
- featured, paperwork, proposal abroad, travelling to the wedding: product-only still lifes; licensed stock or AI "Illustrative image" only if you approve
- three ways to insure, policy checks, claims and AFCA steps: brand graphics built in Canva

### Questions for you
- Primary CTA: the CTA stage chose "Speak with a Wedded Advisor" (/wonderland-concierge) because it sits under the ring handover paragraph; the brief had /destinations as primary (now secondary at the close). Say if you want them swapped.
- Can the "read the PDS and TMD" compliance line be used in social posts? (The social copy currently leaves it out.)
- Plan ref WW-049: confirm where the content plan lives so future runs can read it
- Top up Firecrawl credits (still returning 402)

### Deferred by you (business confirmation needed)
- Fee model and commissions; deposits and who protects them; named Advisor and phone line; real weddings to feature

## What the reader panel said
- Applied: concrete ring handover planning instead of a generic Advisor pitch; cliché close cut; repeated "check your policy" line removed; PDS explainer moved into the policy checks section
- Kept because it worked: the early direct answer, the policy checklist table, the insider travel tips (three rings, police report, cabin bag), the AFCA section, the FAQ
- Not done under your rules: what ring insurance costs (no prices); per-item limits (no figures)

## Research summary
- SERP: DataForSEO, Sydney, Melbourne, New York, Dubai, Singapore
- Volume (AU): engagement ring insurance 1,600; jewellery insurance 2,400; engagement ring insurance australia 170; how to insure an engagement ring 110
- Gap we're targeting: a neutral, sourced checklist that sells no policy, following the ring from purchase through a proposal abroad to the destination wedding and a claim

## Links
- Internal: /wonderland-concierge (primary CTA), /destinations (secondary), ring spend article, diamond buying guide, lab-grown diamonds, ring settings, ring styles, how-to-propose guide, Italy proposal destinations
- External: Moneysmart contents insurance, Insurance Council insurance explained, AFCA make a complaint, Smartraveller travel insurance, Smartraveller theft and robbery
- Backlinks to add: see `backlinks-todo.md` (ring settings, ring styles, ring spend article)

## Distribution assets
- See `10-distribution.json`: 3 Pinterest pins, 8-slide carousel, newsletter section

## Validation
- validate.py: all valid · scan_copy.py: 0 banned, 0 dashes, 0 overlaps
