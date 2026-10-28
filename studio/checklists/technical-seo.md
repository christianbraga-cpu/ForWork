# Technical SEO checklist

Each item is recorded in `self_qa.results` (or in the review findings) with
pass or fail and evidence. `auto` items can be checked mechanically; `rubric`
items need judgement.

| # | Check | Severity if failed | Type |
|---|---|---|---|
| 1 | check_page.py has no blocker failures | blocker | auto |
| 2 | noindex present while any fact needing sign-off is unconfirmed | blocker | auto |
| 3 | Canonical, lang en-AU, title, meta description, Open Graph present | major | auto |
| 4 | JSON-LD parses; FAQPage matches visible FAQ exactly; Offer currency AUD | blocker | auto |
| 5 | No unconfirmed fact in schema without the on-page hedge | blocker | rubric |
| 6 | Internal links match the copy and link plan; external links noopener | major | auto |
| 7 | Images have width and height; hero not lazy; below-fold lazy | major | auto |
| 8 | Performance budget met (Lighthouse), or not_run with the reason | major | auto |
| 9 | Mobile and desktop screenshots saved | major | auto |
| 10 | No venue or supplier contact details on the page | blocker | auto |
| 11 | Reference page structure and class names followed | minor | rubric |
