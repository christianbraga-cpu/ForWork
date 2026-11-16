# SEO research: honeymoon planner cost (fast mode, 2026-11-16)

Source: DataForSEO (SERP, Google Ads volume, Labs difficulty, Labs ranked keywords, on-page checks). Apify web-fetch for Sydney top 3 (one round). GSC not read (fast mode).

## Demand (Google Ads, monthly, 2026-11-16)
| Keyword | AU volume | US volume | KD AU | KD US |
|---|---|---|---|---|
| honeymoon planner cost | no data | no data | no data | no data |
| how much does a honeymoon planner cost | no data | no data | no data | no data |
| honeymoon travel agent fees | no data | no data | no data | no data |
| do travel agents charge fees | 70 | 590 | no data | 0 |
| honeymoon cost australia | no data | no data | no data | no data |
| average honeymoon cost | no data | no data | 53 | 6 |
| travel agent fees | 110 | 590 | 0 | 0 |

"No data" = not returned, not zero. The primary is a long tail with no measurable volume; the real fee demand sits in the generic "travel agent fees" / "do travel agents charge fees" pair.

## SERPs per region
| City | Page one shape | PAA | Notable |
|---|---|---|---|
| Sydney | AI Overview; parked domain #1, Pinterest, US trip-cost articles (yodl, fash, celebration), Amazon planner book | average price of a honeymoon; wedding planner cost in Australia; budget destinations; is 4 days enough | No AU page answers the planner fee. Related: "honeymoon planner cost australia" |
| Melbourne | Same as Sydney plus TravelTriangle packages, 2010 finance blog, Tripadvisor forum | same as Sydney | Weak and stale |
| New York | No AI Overview; Reddit and Facebook threads #1 and #2 ("how much do they usually cost?"); two agencies listing paid consultation fees; The Knot, Zola trip-cost; Etsy printables + Popular products | realistic budget; is $5000 enough; is $3,000 enough; 7 day cost | Mixed intent: printable planner products vs service fee vs trip cost |
| Dubai | AI Overview; AED packages, Pinterest, agency guide | average price; wedding planner cost in Dubai; Dubai honeymoon cost | Package-led |
| Singapore | AI Overview; insurer guide, Facebook thread on commission, agency, forums | average price; what a package includes | "How does a travel agent work" is the fee question |

## Sydney top 3 read (one round, no retry)
- #1 moneymoon.com.au: HTTP 200, empty parked page. Nothing to learn.
- #2 Pinterest pin: not fetched (google goto redirect, login wall).
- #3 yodl.travel: goto redirect returned 415 to the fetcher; real URL not in the SERP data. Not read.
- Substitute #4 fash.com average honeymoon cost: read (notes in pages/fash-average-honeymoon-cost.md). Trip-cost tables in USD, never the planner's fee.

## Cross-region summary
- Guest counts: not relevant (honeymoon).
- Pricing shown: every region leads with trip-cost averages or package prices (USD, AED, INR). Two US agencies show their own consultation fees.
- Top concern: "Is a planner worth it, and will they charge me on top of the trip?" (forum threads in NY and Singapore; PAA on planner cost in AU and Dubai).
- Gap we can own: nobody separates the planner's fee from the cost of the trip, explains what a fee should cover, or gives Australian couples the questions to ask (in writing, AUD, commissions, refunds, consumer rights).
- Gap we deliberately do NOT fill: cost-figure demand (averages, "is $X enough", fee amounts). Business decision: the article states no prices or averages. Trip-budget readers are routed to the existing luxury honeymoon budget guide.

## Overlap call
- /expert-advice/luxury-honeymoon-budget-which-destination-suits-yours (live, 2,909 words) already owns honeymoon trip cost and budget. Do not compete: link to it once for trip budget.
- /10-step-to-a-budget-friendly-honeymoon (live) targets saving tips, not planner cost. Only cost-adjacent ranking found: /top-2019-honeymoon-destinations-that-wont-blow-the-budget at #26 AU for "best places to honeymoon on a budget". No WW page ranks for planner/fee terms. Off brand ("budget-friendly", "save"); do not link.
- Sister draft /honeymoon-ideas/honeymoon-planning-service (404, unpublished) has a short cost FAQ; that FAQ should link here and stay one line so this page owns the fee question.
- /travel-guides/travel-advisor-benefits (404, draft): owns "why use an advisor"; this post owns "what it costs and what the fee covers".

recommended_scope: au_focus
