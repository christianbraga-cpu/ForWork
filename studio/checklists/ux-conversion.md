# UX and Conversion Designer checklist

Each item is recorded in `self_qa.results` (or in the review findings) with
pass or fail and evidence. `auto` items can be checked mechanically; `rubric`
items need judgement.

| # | Check | Severity if failed | Type |
|---|---|---|---|
| 1 | Reuses reference template components; new components justified | major | auto |
| 2 | Primary CTA visible in the first screen on mobile, and a sticky mobile enquire bar | major | auto |
| 3 | End-to-end offer and contact person explained before the form | major | rubric |
| 4 | Form posts to config enquiry_endpoint with route_to, offer, page slug and UTM hidden fields | blocker | auto |
| 5 | Form fields kept to the reference set unless a reason is recorded | minor | auto |
| 6 | Every field labelled, error and success states specified | major | auto |
| 7 | Tap targets 44px or more, WCAG AA contrast | major | auto |
| 8 | Heading order logical (one H1, no skipped levels) | minor | auto |
| 9 | Copy length limits set per component; overruns flagged | minor | auto |
