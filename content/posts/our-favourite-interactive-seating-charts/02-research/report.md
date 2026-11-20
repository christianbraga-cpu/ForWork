# Stage 02 SEO research: Interactive Wedding Seating Charts We Love (refresh)

Run date 2026-11-20, fast mode. SERP source: DataForSEO (live, desktop, depth 10). Keyword: "interactive seating chart wedding". Cities: Sydney, Melbourne, New York, Dubai, Singapore (lean 5-city run). Raw files: `serp-<city>.json`.

## Results by region

| City | What ranks | Our presence | Notes |
|---|---|---|---|
| Sydney | Pinterest repin of our page #1, seatplan.io QR page #2, Pinterest templates #3, felicitations (page now retired) #4, Instagram, magnific, Wedding Waitress how-to | Pinterest repin #1 and image pack only | AI Overview present (text not returned). Related: QR code seating, free, template, australia |
| Melbourne | Pinterest, Etsy, popular-products carousel, magnific, wedding-seating.com compare, Pinterest repins of our page #5 and #9 | Two repins | Shopping heavy |
| New York | Pinterest, AU hire company digital screen #2, seatplan.io #3, app comparison #4, our Facebook post #6, edit.org, Pinterest repin #8 | Facebook and Pinterest only | Full AI Overview: planning tool vs guest-facing display; ideas = QR charts, escort card walls, keepsake tokens, pull-away photo cards |
| Dubai | Paid QR seating ads, Pinterest, Etsy, boardmix, magnific | None | "Where in the World Are You Sitting?" table plan #2 |
| Singapore | Pinterest, magnific, bridesmaidforhire ideas list #4, boardmix | None | Same world-map table plan #2 |

Pages read (Sydney top 3): #1 and #3 are Pinterest pins (not readable articles, skipped). #2 seatplan.io: product page, 3-step QR seat finder, use cases, FAQ (app needed? passcode?), paywalled feature, no ideas content. #4 felicitations: product page retired. Notes in `pages/`.

## Cross-region summary
- Guest counts: not stated on ranking pages except seatplan's "one QR sign handles 200 guests" (vendor claim).
- Pricing shown: Etsy/marketplace products and a hire screen in shopping units; we show no prices (brief).
- Top concern: guests finding their seat fast without a queue, and last-minute changes.
- Gap we can own: no editorial page in any top 10 gives curated interactive display ideas with practical guidance (flow, accessibility, weather, late changes) and a destination angle. Our ideas currently win only through Pinterest/Facebook repins, so the refreshed page itself should earn the click.
- recommended_scope: global.

## Volumes (Google Ads, monthly)
| Keyword | AU | US |
|---|---|---|
| interactive seating chart wedding | 10 | 320 |
| interactive wedding seating chart | 10 | 320 |
| creative seating chart ideas | 10 | 110 |
| wedding seating chart display | 10 | 320 |
| seating chart maker wedding | 90 | 1,300 |
| wedding seating chart ideas | 210 | 4,400 |

US interactive volume peaks June (880) and is down 46% year on year.

## Ranking queries of this URL (DataForSEO Labs)
- US: "interactive wedding seating chart", position 16 (absolute 20), KD 17, new.
- AU: no ranked keywords returned.
- The brief's avg position 3.9 / 1,271 impressions comes from GSC, which this run could not read (no export in `content-system/seo/gsc-exports/`, Drive search not available). Not verified here.

### Protect what ranks
Live page H1 "Our Favourite Interactive Seating Charts", title tag and intro ("Interactive seating charts offer a fun and dynamic way to organise ... seating arrangements"). Live H2s to keep (as H3s, wording close): A Sweet Touch, Table Decor, A Glass of Champagne, A Personal Touch, The Art of Technology, A Pop of Colour, Tropical Wedding Seating Chart. Keep "interactive seating chart(s)" in H1, intro and image alt text; Pinterest repins of these images rank #1 in Sydney.

## Cannibalisation and split
- Head `/expert-advice/wedding-seating-chart`: how-to, timing, table sizes, who sits where, template vs app, alphabetical vs by table, QR "how guests find their seats".
- `/expert-advice/how-to-make-a-wedding-seating-chart` resolves to the head (final URL and canonical). Status code not confirmable from this sandbox (direct HTTP blocked); confirm it is a 301.
- `/expert-advice/where-to-print-wedding-seating-chart` (live 2026-11-18, not in link map): printing, sizes, display at reception, QR on the chart. Closest overlap with "wedding seating chart display".
- Proposed split: this page owns interactive and creative display ideas (+ destination styling); head owns how-to, templates, seating chart maker; where-to-print owns printing and display logistics.

## Internal link checks (Firecrawl, fresh, 2026-11-20)
All 200 and index,follow: head, /wonderland-studio, /expert-advice/what-is-wonderland-studio, /expert-advice/prismm-vs-wonderland-studio, /wedding-planning-tools, /expert-advice/wedding-without-seating-chart (now published, link map still says draft), /expert-advice/where-to-print-wedding-seating-chart. `/22-amazing-table-settings-for-every-wedding-theme` now resolves to `/style-advice/22-amazing-table-settings-for-every-wedding-theme` (URL moved on save); link the new path and check a redirect exists. Same risk applies to this refresh's URL.
