# AI Search (GEO) Specialist checklist

Each item is recorded in `self_qa.results` (or in the review findings) with
pass or fail and evidence. `auto` items can be checked mechanically; `rubric`
items need judgement.

| # | Check | Severity if failed | Type |
|---|---|---|---|
| 1 | At least 5 realistic couple prompts tested, phrased from persona vocabulary | major | auto |
| 2 | Cited domains and pages recorded from DataForSEO LLM mention tools | major | auto |
| 3 | Whether weddedwonderland.com is cited is stated explicitly | blocker | auto |
| 4 | Content requirements are specific and actionable (what statement, where, in what format) | major | rubric |
| 5 | Recommended statements use only facts in facts.json | blocker | auto |
| 6 | Re-test prompts and date set in the stage 8 plan | minor | auto |
