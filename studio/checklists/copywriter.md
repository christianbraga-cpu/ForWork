# Copywriter checklist

Each item is recorded in `self_qa.results` (or in the review findings) with
pass or fail and evidence. `auto` items can be checked mechanically; `rubric`
items need judgement.

| # | Check | Severity if failed | Type |
|---|---|---|---|
| 1 | Every section in the brief outline is present, in order | blocker | auto |
| 2 | Every factual statement has a fact_refs entry | blocker | auto |
| 3 | Unconfirmed facts are hedged and listed in unconfirmed_used | blocker | auto |
| 4 | All prices written as From AUD | blocker | auto |
| 5 | No banned phrases (studio/standards/banned-phrases.txt) | major | auto |
| 6 | No em dashes | major | auto |
| 7 | No competitor or marketplace names | blocker | auto |
| 8 | Primary keyword in title, H1 and the first 100 words | major | auto |
| 9 | Meta title 50 to 60 characters, meta description 140 to 160 | minor | auto |
| 10 | Every link_plan.must_link_to entry placed with a natural, varied anchor | major | auto |
| 11 | FAQ answers stand alone and are quotable | minor | rubric |
| 12 | End-to-end service and the couple's contact person explained before the form | major | rubric |
| 13 | Brand voice rubric: no dimension below 3 (studio/standards/brand-voice.md) | major | rubric |
| 14 | Within the brief word count range | minor | auto |
| 15 | For optimise and refresh: every change has a change_reason | major | auto |
