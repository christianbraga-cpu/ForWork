# Fact Checker checklist

Each item is recorded in `self_qa.results` (or in the review findings) with
pass or fail and evidence. `auto` items can be checked mechanically; `rubric`
items need judgement.

| # | Check | Severity if failed | Type |
|---|---|---|---|
| 1 | Every factual claim in the artefact is listed and classified | blocker | auto |
| 2 | Every classification cites a fact id or a source URL | blocker | auto |
| 3 | Conflicts between sources are listed explicitly with both values | blocker | auto |
| 4 | Source tier follows config.source_of_truth_order | major | auto |
| 5 | Prices, capacities, room counts, distances, legal or visa claims all checked | blocker | auto |
| 6 | Proposed new facts are unconfirmed unless an official source states them plainly | major | rubric |
| 7 | No marketplace or competitor listing used as the only source for a confirmed fact | major | auto |
