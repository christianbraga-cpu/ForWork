# QA checklists

Four layers: **self-check** (producer, recorded in `self_qa`), **peer review**
(a different role), **gates** (go / no-go), **post-publish** (analytics, 14/30/90 days).
Checklist and check IDs are stable: agents cite them in `self_qa.passed` / `failed`
and gates cite them in `checks[].id`.

## Verdicts and severity

| Verdict | Meaning |
|---|---|
| `pass` | Every check passes |
| `pass_with_notes` | Only `medium` / `low` issues |
| `fail` | Any `high` or `blocker` issue |

| Severity | Meaning | Can the strategist waive it? |
|---|---|---|
| `blocker` | Wrong or unsourced high-risk fact, house-rule breach, licence/consent missing, page would mislead a couple | Never |
| `high` | Will hurt ranking, conversion or brand noticeably | Yes, with a recorded reason |
| `medium` | Worth fixing this round | Yes |
| `low` | Polish | Yes |

Peer review pairings: keyword map is reviewed by the strategist in the brief step;
copy by seo-qa (intent) and fact-checker (facts); images by brand-guardian; link
plan by seo-qa; build by technical-qa.

---

## kw_research_v1 (keyword-researcher)

- `KW-01` Primary keyword has volume, difficulty, intent and SERP snapshot for the AU market
- `KW-02` Every secondary keyword is assigned to a brief section or excluded with a reason
- `KW-03` Bargain / low-intent terms (cheap, budget, deal, affordable) are excluded
- `KW-04` Cannibalisation checked against `link-registry.csv` primary keywords
- `KW-05` Questions (PAA, research doc) collected for FAQ candidates
- `KW-06` Every number cites a tool report or the research doc, with a date
- `KW-07` Competitor gaps list at least 3 competitors where data exists

## tech_v1 (technical-seo)

- `TS-01` Requirements cover template, performance budget, schema types, indexing, markup rules
- `TS-02` Existing page (optimise/refresh/audit): title, meta, h1, headings, word count, links, images, schema recorded
- `TS-03` Each finding has severity, evidence and a fix
- `TS-04` Canonical follows `site-rules.md`

## brief_v1 (seo-strategist)

- `BR-01` One-sentence goal names the reader action
- `BR-02` Every section has a purpose, must-cover list and allowed `fact_ids`
- `BR-03` Every target persona's top 3 fears are addressed by at least one section
- `BR-04` Primary keyword placement specified (title, h1, first 100 words)
- `BR-05` FAQs come from real queries (keyword map or research doc)
- `BR-06` Acceptance criteria are testable
- `BR-07` optimise/refresh: every existing section has `keep / change / remove` with a reason
- `BR-08` No section relies on a fact with `publishable: false`

## links_v1 (linking-specialist)

- `LK-01` All `must_link_to` targets from the registry are planned
- `LK-02` 2 to 4 sibling packages linked; no `planned` URLs linked
- `LK-03` No anchor uses another page's primary keyword
- `LK-04` At least 3 back-link tasks for a new page
- `LK-05` Legal or travel claims have an official outbound source
- `LK-06` No competitor or aggregator outbound links; rel attributes set
- `LK-07` Registry row added or updated

## cro_v1 (cro-specialist)

- `CR-01` Form matches the page facts (endpoint, fields, success message), or the existing form is kept unchanged
- `CR-02` A CTA is visible within the first screen on mobile and desktop
- `CR-03` CTA placed after each "proof" section (offers, spaces, FAQ)
- `CR-04` Each primary persona fear has a named answer location
- `CR-05` Chosen offer carries into the form

## copy_v1 (copywriter)

- `CP-01` Every brief section written, in brief order, with the brief's section IDs
- `CP-02` Every factual claim maps to a ledger `fact_id`; anything else is a `[[CONFIRM]]` placeholder
- `CP-03` Primary keyword in title, H1 and first 100 words; used naturally, not more than once per 150 words
- `CP-04` Title tag at most 60 characters, meta description 120 to 155 characters
- `CP-05` No forbidden terms (`brand-voice.md` and brief)
- `CP-06` No em dashes; Australian English; prices as `From AUD 38,550`
- `CP-07` Word count inside the brief range
- `CP-08` Links placed exactly as the link plan, with approved anchors
- `CP-09` FAQ answers are 1 to 3 sentences, answer first
- `CP-10` optimise/refresh: `keep` sections are unchanged

## images_v1 (visual-seo)

- `IM-01` Every slot has a descriptive filename (lowercase, hyphenated, no camera names)
- `IM-02` Alt text describes the image in under 125 characters, no keyword stuffing; decorative images `alt=""`
- `IM-03` Licence status and scope recorded; anything not `confirmed` is on the sign-off list
- `IM-04` Consent recorded for any identifiable couple or guest; no identifiable minors without consent
- `IM-05` No competitor images; no stock or AI images presented as real weddings, venues or rooms
- `IM-06` Hero `eager` + `fetchpriority=high`; everything else `lazy`
- `IM-07` Size budgets and widths set; aspect ratio set to prevent layout shift
- `IM-08` No hero image reused from another page

## build_v1 (page-builder)

- `BD-01` Every copy section rendered with matching `id`
- `BD-02` `noindex` present
- `BD-03` JSON-LD valid JSON; FAQPage matches visible FAQ text exactly; Product/Offer price matches visible price
- `BD-04` Form endpoint and fields match the conversion spec; existing tracking and scripts preserved
- `BD-05` Images are slots or `<img>` with width/height, alt, loading attributes per image plan
- `BD-06` `tools/check_page.py` run with zero errors
- `BD-07` `CHANGES.md` lists every edit by section (optimise/refresh); outstanding checks and images to supply listed in `04c-build.json`

---

## fact_gate (fact-checker, mode gate)

- `FG-01` Every price on the page matches the ledger and has `signed_off_by` (else sign-off item, `blocker` if it mismatches)
- `FG-02` Capacities, room counts, distances and travel times match the ledger
- `FG-03` Legal claims are sourced from an official source or phrased as "your planner confirms"
- `FG-04` No claim on the page is missing from the ledger (scan visible text and JSON-LD)
- `FG-05` Conflicted facts use the ledger's resolution and are on the sign-off list
- `FG-06` No competitor-only claims reused
- `FG-07` Every `[[CONFIRM]]` placeholder is on the sign-off list

## brand_gate (brand-guardian; a human makes the final call)

- `BG-01` Voice principles in `brand-voice.md` followed
- `BG-02` No forbidden terms; "luxury" at most once and not in a heading
- `BG-03` Brand names used exactly (`site-rules.md`)
- `BG-04` No pressure or discount language
- `BG-05` Images feel real and on brand; no competitor assets
- `BG-06` No em dashes
- `BG-07` Reads well aloud: no sentence over 30 words

## seo_gate (seo-qa)

- `SG-01` Every brief acceptance criterion met (cite each one)
- `SG-02` Primary and secondary keyword coverage as briefed
- `SG-03` Title, meta, H1 unique and within limits
- `SG-04` Heading hierarchy: one H1, no skipped levels
- `SG-05` Internal links match the link plan; anchors approved; no orphan risk
- `SG-06` FAQ answers target the source queries
- `SG-07` Schema types match the brief
- `SG-08` Content serves the briefed intent better than the benchmark competitors (explain)

## technical_gate (technical-qa)

- `TG-01` `tools/check_page.py` passes with zero errors
- `TG-02` JSON-LD parses; required properties present for each type
- `TG-03` Canonical and robots correct
- `TG-04` Mobile render has no horizontal scroll; sticky CTA does not cover content
- `TG-05` LCP element is the hero and not lazy-loaded; performance budget met where measurable
- `TG-06` All internal links resolve to registry URLs (live or unverified)
- `TG-07` Form fields, labels and required attributes correct; keyboard reachable
- `TG-08` Images have alt and dimensions

## icp_panel (icp-critic, persona-synthesizer)

- `IC-01` Every critique quotes the page for each reaction
- `IC-02` Every score has a reason
- `IC-03` Persona deal-breakers checked explicitly
- `IC-04` Critics did not see each other's output
- `IC-05` Synthesis separates consensus (3+ personas, or 2 of 2) from segment issues

## Post-publish (analytics-specialist)

- `PP-14` Day 14: indexed, impressions, primary keyword position, CWV field data
- `PP-30` Day 30: rankings for primary + secondaries, CTR, engagement, enquiries
- `PP-90` Day 90: enquiries, CRM-attributed consultations and signed contracts; underperformers back to the backlog with a diagnosis
