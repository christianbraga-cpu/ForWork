# Visual Lead checklist

Each item is recorded in `self_qa.results` (or in the review findings) with
pass or fail and evidence. `auto` items can be checked mechanically; `rubric`
items need judgement.

| # | Check | Severity if failed | Type |
|---|---|---|---|
| 1 | Every image slot in the brief and template has an entry | major | auto |
| 2 | Every image has a rights status; nothing marked cleared without a register id | blocker | auto |
| 3 | No competitor or marketplace imagery | blocker | auto |
| 4 | No AI-generated image presented as a real wedding or venue | blocker | auto |
| 5 | File names are descriptive kebab-case | minor | auto |
| 6 | Alt drafts describe the image in 125 characters or fewer | major | auto |
| 7 | Sequence tells a story (setting, ceremony, details, guests, celebration, stay) | major | rubric |
| 8 | Each image lists the personas it reassures | minor | auto |
| 9 | Crops listed, including Open Graph and a Pinterest 2:3 crop for key images | minor | auto |
