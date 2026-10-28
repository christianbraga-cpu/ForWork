# Persona reader (validity checks the Project Lead runs on each review) checklist

Each item is recorded in `self_qa.results` (or in the review findings) with
pass or fail and evidence. `auto` items can be checked mechanically; `rubric`
items need judgement.

| # | Check | Severity if failed | Type |
|---|---|---|---|
| 1 | Reviewer read only the persona file and the artefact | blocker | auto |
| 2 | Every reaction quotes the exact text | major | auto |
| 3 | All persona top_questions appear in questions_answered | blocker | auto |
| 4 | A decision of enquire with a top question answered no is treated as invalid and re-run | major | auto |
| 5 | Voice matches persona vocabulary, not marketing language | minor | rubric |
