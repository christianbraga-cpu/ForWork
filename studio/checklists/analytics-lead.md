# Analytics and CRM Lead checklist

Each item is recorded in `self_qa.results` (or in the review findings) with
pass or fail and evidence. `auto` items can be checked mechanically; `rubric`
items need judgement.

| # | Check | Severity if failed | Type |
|---|---|---|---|
| 1 | No personal data copied from the CRM; aggregates only | blocker | auto |
| 2 | CRM data quality caveats applied (default 50,000 budgets, concatenated ranges) | major | rubric |
| 3 | Events specified: enquiry_start, enquiry_submit, offer_select, cta_click, faq_open, gallery_open, scroll_depth | major | auto |
| 4 | Hidden fields map to Zoho Consumers API names | blocker | auto |
| 5 | No personal data in analytics events | blocker | auto |
| 6 | KPIs have targets and a review date | major | auto |
| 7 | Persona predictions captured for comparison with real behaviour | minor | auto |
