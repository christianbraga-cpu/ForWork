# SEO research: wedding timeline 4pm ceremony (fast mode, 2026-11-24)

Source: DataForSEO live SERP (Google, desktop, en, depth 10) in Sydney, Melbourne, New York, Dubai and Singapore. Google Ads volume for AU and US. DataForSEO ranked keywords for weddedwonderland.com. Firecrawl for page reading, site map and link checks. Search Console: no current export (latest known Drive export is 2025-05-14, over 45 days old; the Drive search tool was not available this session), so no GSC figures are used.

## STOP: cannibalisation needs a decision before writing

`/expert-advice/wedding-day-timeline-template` (live, index, published 2026-10-21) is titled "Wedding Day Timeline Template for 1pm, 3pm, 4pm, 6pm" and already carries a full 4pm run sheet with and without a first look, sunset logic and destination notes. It ranks #5 organic (absolute 8) in Singapore today for the exact keyword. It is missing from link-map.csv. The proposed split (head owns the general day, new page owns ceremony-time templates) is already taken by this page.

Options for the strategist:
1. **Recommended:** do not create a new URL. Refresh `/expert-advice/wedding-day-timeline-template` to add 2pm and 5pm sheets and retitle it keyword first, e.g. "Wedding Timeline for a 4pm Ceremony and Other Start Times". One URL then owns every ceremony-time query.
2. Keep the new URL only as a 4pm-only deep page (4pm by season and sunset, with and without a first look, destination time zones), and cut the 4pm sheet on the template page to a summary plus a link here. The title "With 2pm to 5pm Options" would then compete with the template page and should drop the range.

The outline in 02-seo.json is written for option 2's shape, so it can be reused for option 1.

## Volume (Google Ads, monthly)
| Keyword | AU | US |
|---|---|---|
| wedding timeline 4pm ceremony | 20 | 480 |
| wedding timeline template 4pm ceremony | no data | no data |
| wedding day timeline 2pm ceremony | 10 | 40 |
| wedding timeline 3pm ceremony | 10 | 30 |
| wedding timeline 5pm ceremony | 10 | 30 |
| wedding day timeline | 260 | 3,600 |
| wedding reception timeline | 210 | 3,600 |

## By region (top organic)
| City | #1 | #2 | #3 | Features |
|---|---|---|---|---|
| Sydney | The Knot (4pm sample) | Laura Alpizar (photographer, 4pm template) | Reddit r/wedding | AI overview, images; Easy Weddings #5 (competitor) |
| Melbourne | Megan Lee Photo (2016) | Cole Studios (AU photographer) | Pinterest | AI overview, video, images |
| New York | WeddingWire forum (2012) | Pinterest | Facebook video | AI overview, video; Lovecation #6 |
| Dubai | Facebook group | Facebook video | Pinterest | AI overview (async), video; Lovecation, timelineforge |
| Singapore | Pinterest | Pinterest | Finds For Her | AI overview (async); **weddedwonderland.com template page #5** |

People Also Ask: not returned in any of the 5 cities. Related searches (Sydney): template, no first look, with first look, printable, simple, free, 4:30pm ceremony, 5pm ceremony. Bliss and Bone did not appear in any top 10 today, so it was not read.

AI overview (Sydney, Melbourne, New York): an hour-by-hour 4pm sample with a first look ending around 10:30 to 11pm, then "without a first look" and "travel and buffers" adjustments, and in New York "check sunset time for your date and location". Cited: The Knot, Laura Alpizar, Mary Kate Davenport, Easy Weddings, Reddit, TikTok.

## Pages read
| Page | Words | Pricing | Real weddings | FAQ/schema | CTA | Images | Strength | Gap |
|---|---|---|---|---|---|---|---|---|
| The Knot 4pm (Sydney #1, AIO) | ~1,100 | none | no | no | hire a planner | 3 + infographic | named planner quotes, first look vs none | no sunset or season, one time only, US only |
| Laura Alpizar (Sydney #2, AIO) | ~1,100 | none | no | no | PDF, contact | ~4 | backwards build, season note on sunset | photographer-centric, 2015, no official sunset source |
| WW template page (Singapore #5) | long | none | no | not checked | Wedded Concierge | 15+ | 1/3/4/6pm sheets, first look minutes, regional | no 2pm or 5pm; overlaps this brief |
| WW head /wedding-day-timeline | ~1,800 | none | no | FAQ block | Wonderland Studio | 2 | method, duration table, 4pm sample | general; also holds a 4pm sample |
Reddit (Sydney #3) not read (forum). Notes in 02-research/pages/.

## Cross-region summary
- Guest counts: The Knot assumes 5 to 6 in hair and makeup; WW head assumes ~100 guests. No page plans by guest count.
- Pricing shown: none anywhere.
- Top concern: "Where do the photos go if we skip the first look?" and "do we miss cocktail hour?" (Facebook threads rank in every city).
- Gap we can own: sunset and season driving the 4pm sheet (southern vs northern summer), an official sunset source linked at the claim, destination time zone and heat, and how the 4pm sheet shifts at 2pm, 3pm and 5pm in one place. Most of this already exists on our template page.
- Regional: AU SERPs mix AU photographers; US and ME SERPs are social-heavy (Facebook, Pinterest, Instagram), so a clear text sheet can win. Intent is the same everywhere.

## recommended_scope
global (one version, Australian English, times as planning examples, sunset via official calculators).

## Our pages and cannibalisation
- `/expert-advice/wedding-day-timeline-template`: owns ceremony-time templates incl. 4pm; ranks for the keyword (Singapore #5). Main conflict.
- `/expert-advice/wedding-day-timeline` (head): H1 "How Do You Build a Wedding Day Timeline, Minute by Minute?"; has an H2 "What does a sample wedding timeline look like for a 4pm ceremony?". Not seen in today's top 10. Which page gets GSC impressions for "wedding day timeline 2pm ceremony" could not be confirmed (no current GSC export; DataForSEO shows no AU or US ranking for it).
- `/your-pre-ceremony-wedding-schedule-sorted`: old pre-ceremony schedule built around a 2pm ceremony. Likely candidate for the 2pm impressions; link to it, do not merge without GSC.
- `/expert-advice/wedding-reception-timeline` and `/wedding-scheduling-hack-a-modern-reception-timeline`: reception intent, two pages on the same intent (the older one ranks US #5 for "modern wedding reception timeline").
- Link map is stale: missing the template page, the reception timeline page and the destination wedding timeline page.

## Sunset source
`https://geodesyapps.ga.gov.au/sunrise` (Geoscience Australia, Sunrise, Sunset and Twilight Times) is live (200). The older `ga.gov.au/scientific-topics/astronomical/sun-rise-and-set` returns 404. The template page uses the US Naval Observatory one-day calculator (`https://aa.usno.navy.mil/data/RS_OneDay`) for non-AU places; live (200) today.
