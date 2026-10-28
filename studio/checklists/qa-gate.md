# Project Lead QA gate checklist

Each item is recorded in `self_qa.results` (or in the review findings) with
pass or fail and evidence. `auto` items can be checked mechanically; `rubric`
items need judgement.

| # | Check | Severity if failed | Type |
|---|---|---|---|
| 1 | All envelopes validate | blocker | auto |
| 2 | check_page.py: zero blockers | blocker | auto |
| 3 | Fact checker final pass: zero blockers | blocker | auto |
| 4 | Brand voice review: zero blockers, no rubric score below 3 (or accepted in decisions.md) | blocker | auto |
| 5 | Primary ICP persona: no blocker objection at page stage | blocker | auto |
| 6 | Every unconfirmed fact listed in NOTES.md with who signs it off | blocker | auto |
| 7 | Every image slot without cleared rights listed in NOTES.md Images to supply | major | auto |
| 8 | Majors fixed or accepted in decisions.md | major | auto |
| 9 | Revision rounds within config limit | minor | auto |
