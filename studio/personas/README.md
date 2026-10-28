# Persona panel

Synthetic ICP readers used by the `persona-reader` agent at three points: the
content brief, the copy, and screenshots of the built page.

## The panel

| Persona | Status | Evidence | Primary for |
|---|---|---|---|
| `au-couple-marrying-abroad` | evidence based | about 50 records | package, destination hub |
| `intl-couple-europe-full-service` | evidence based, thin | about 25 to 30 records | |
| `multi-day-cultural-celebration` | evidence based, thin | about 24 records | |
| `intimate-destination-elopement` | evidence based, thin | about 10 records | |
| `aspirational-luxury-couple` | **assumption** | about 11 records, none won | |
| `discerning-skeptic` | adversarial | models CRM leakage | always included |

`status: assumption` personas show where the brand wants to go, not who enquires
today. The Project Lead weights their findings lower and never lets them
override an evidence-based persona.

## Where the evidence came from

Zoho CRM `Consumers` module, analysed 2026-10-28. Two samples were taken (400
records with a contact message, 500 with a budget): 712 unique records and 516
genuine couple enquiries after removing spam, vendor pitches and test entries.

Key findings that shaped the panel:
- Origin: Australia 46%, then the US, UK, Philippines, UAE and Canada.
- About 43% of determinable enquiries are destination weddings. The top destinations
  are Italy, Greece, UAE, Mexico, Bali and Morocco.
- Budget: the modal band is AUD 30,000 to 75,000. Only about 11% are at 150,000 or more.
  Destination couples are not higher budget than local ones.
- Destination weddings skew to 31 to 80 guests. Local cultural weddings run 200 to 400.
- Couples are early: 30 of 49 rated their planning 1 to 3 out of 10.
- Instagram brings about 80% of the leads where the source was asked.
- The first asks are "where do I start" or full planning (about 35), venue first (about 26),
  vendor lists (about 16), then price estimates (about 10).
- The main leakage is after a proposal is sent, with no response from the couple.
- No parent enquirers appear in the sample. A "funding parent" persona is
  therefore not on the panel.

## Known CRM data quality issues (fix these to improve the next refresh)

1. `Budget` defaults to 50,000 on many recent records, and picklist ranges are stored
   concatenated (50000100000 means 50,000 to 100,000).
2. `Reason_for_Not_a_Fit`, `Reason_for_Not_Proceeding` and `Couple_s_Story` are always
   empty, and about 70 of 90 lost records have no reason recorded.
3. `Enquiring_As` is blank on 87% of records.
4. `Local_or_Destination_Wedding` is blank on most records.
5. About 30% of contact form records are spam or B2B pitches.
6. Only 3 genuine couple wins exist in the sample, which is too few for a "won" profile.

## Refresh process (quarterly)

1. Re-pull Consumers (all records, not samples) with the analytics-lead agent's COQL
   queries. Aggregates only.
2. Add 5 to 10 real client interviews, plus sales call notes.
3. Update each persona file and bump `version`.
4. Calibrate: run the panel on the best and worst enquiry-converting live pages. If it
   cannot tell them apart, revise the personas.
5. After each page goes live, compare persona decisions with real behaviour (the
   analytics measurement plan records the predictions).

## Persona file fields

`persona_id`, `name`, `version`, `status`, `evidence`, `fit.page_types`,
`fit.primary_for`, `demographics`, `context`, `jobs_to_be_done`,
`emotional_drivers`, `top_questions`, `objections` (each with a source),
`trust_signals_that_work`, `turn_offs`, `vocabulary`, `verbatims` (anonymised),
`decision_role`, `reading_behaviour`, `device`, `conversion_threshold`, `assumptions`.
