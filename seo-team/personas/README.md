# ICP personas

The critique panel reads every page as these people. They start as **hypotheses**
drawn from the brand's positioning (Australian couples planning weddings abroad, quoted in
AUD, with a dedicated planner). Every field marked `evidence: hypothesis` should be
replaced with patterns from real clients.

| ID | Who | Why they are on the panel |
|---|---|---|
| `icp_intl_couple` | Australian professional couple, 80 to 120 guests, Europe | Core buyer |
| `icp_funding_parent` | Parent co-funding the wedding | Hidden decision-maker; reads for value and safety |
| `icp_multiday_celebration` | Couple planning a multi-day cultural celebration, 200+ guests | Needs proof of scale |
| `icp_intimate` | Couple planning an intimate wedding, under 30 guests, high spend per head | Turned off by big-wedding assumptions |
| `icp_skeptic` | Couple already talking to two other providers | Control: looks for reasons to rule us out. Always on the panel |

## Grounding them in real data

1. Export won and lost deals from Zoho CRM for the last 24 months: origin city, guest
   count, budget band, destination, lead time, loss reason.
2. Pull 10 to 20 consultation notes or call transcripts per segment.
3. For each persona field, replace the hypothesis with the pattern and record the
   evidence (`evidence: "31 of 44 won deals, 2025-2026"`).
4. Copy real phrases into `voice.phrases_they_use`: these are the most valuable lines in the file.
5. Have someone from the community review `icp_multiday_celebration` before it is used
   for a specific culture. The default file is deliberately culture-neutral; add
   variants (for example `icp_multiday_indian_australian`) only from real client patterns.

## Calibration

Every quarter: run `action=audit` on 5 to 10 pages with known enquiry rates. If the
panel's `enquiry_intent` does not rank them in roughly the same order, the personas are
wrong, not the pages. Also show 2 or 3 pages to real past clients and compare.

## File format

See `icp_intl_couple.yaml`. Required top-level keys: `persona_id`, `name`,
`evidence_basis`, `profile`, `context`, `entry_queries`, `jobs_to_be_done`,
`decision_criteria`, `objections_and_fears`, `deal_breakers`, `voice`, `behaviour`.
