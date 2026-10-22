# QA rubrics and gate logic

## Severity

| Severity | Meaning | Gate effect |
|---|---|---|
| **blocker** | Factual or legal error, invented fact/quote/price, competitor link or material, plagiarism, brand-safety issue, off-brief angle, em dash in final copy | Any one = fail |
| **major** | Voice drift, banned phrase, weak structure, missing CTA/takeaways/FAQ, missing keyword placement, broken link rule, primary persona fear only "touched" | 2 or more = fail |
| **minor** | Wording, rhythm, small style points | Never blocks; fixed in revision |

## Gate logic (applied by the orchestrator)

A dimension **passes** when: no blockers, at most 1 major, and every rubric line
scores 4 or 5. The draft passes the review gate when every dimension passes
and the persona rules below are met. Maximum 2 revision loops; after the 2nd
failed re-review, stop and report the open issues.

## Scoring anchors (all rubric lines are 1 to 5)

- **5** Publishable in a top travel title as is.
- **4** Good; small fixes only.
- **3** Acceptable but generic or uneven; needs work.
- **2** Clear problems a reader would notice.
- **1** Fails the line entirely.

## Rubrics by dimension

### Brief (orchestrator checks before research)
- Audience and funnel stage are clear
- Keyword has real intent and fits the brand
- Angle beats the SERP top 3 on at least one gap
- Ties to a service and a CTA from the library

### Research pack (fact-checker reads it during the accuracy review)
- Every fact has a source URL and a source date
- Legal facts come from official sources checked within 12 months
- Nothing invented; gaps marked `[[NEEDS: ...]]`

### `voice` (editorial-director)
- `style_match`: follows style-guide structure and mechanics
- `specificity`: concrete names, months, distances, numbers; no filler adjectives
- `invisible_work`: shows what end-to-end planning actually handles
- `two_readers`: gives the couple something to imagine and the payer something to trust
- `brief_fidelity`: delivers the brief's angle and every `must_include`
- `brand_accuracy`: brand names, offers, process and proof points used correctly

### `accuracy` (fact-checker)
- `claims_verified`: every claim in the register traced to a source that says it
- `legal_current`: legal claims from official sources within 12 months, with the Advisor caveat
- `no_inventions`: no invented weddings, quotes, prices, capacities or stats
- `prices_rule`: every price is "From AUD", flagged for Nic
- `no_guarantees`: no promises about weather, availability or outcomes

### `seo` (seo-reviewer)
- `keyword_placement`: primary keyword in H1, first 100 words, 1 H2, meta title, slug
- `meta`: SEO title 50 to 60 chars, meta description 140 to 155 chars, both compelling
- `internal_links`: hub + 1 service + 2 related (when they exist), descriptive varied anchors
- `external_links`: only approved domains, correct rel, none blocked, all reachable
- `structure`: takeaways, FAQ (4 to 6), H2s answer real queries, no stuffing (density under 1.5%)
- `serp_gap`: covers at least one gap the top 3 miss

### `reader:<persona_id>` (icp-reader)
Scores: `relevance`, `trust`, `clarity`, `would_enquire`.
- **Primary persona:** `trust` and `would_enquire` must be 4 or more; any top-2
  fear `ignored` = blocker, `touched` = major.
- **Secondary persona:** advisory, but `clarity` under 3 = major.
- **Anti-persona (`bargain_hunter`):** `would_enquire` 4 or more = blocker.

### Images (photo-curator self-check; orchestrator confirms)
- Each slot brief matches its paragraph (place, season, moment, culture, scale)
- Source plan follows the preference order; no competitor or reference-only image proposed
- Alt text plain and specific; captions add context; credits listed
- Rights fields filled; anything unknown marked `[[NEEDS: licence]]`

### Publish package (copy-editor self-check)
- Zero spelling errors in place and brand names; Australian spelling
- No em dashes anywhere
- Every field the CMS needs is present (see schemas)
- Categories: first is primary; tags 3 to 6
- All `[[NEEDS]]` items listed for humans
