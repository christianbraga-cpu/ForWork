# Stage 02 SEO research: turkish-wedding-traditions (fast mode, 2026-11-02)

Source: DataForSEO (SERP, volume, difficulty, related, ranked keywords, on_page). Pages read with Apify web-fetch.
GSC: not read. No Google Drive connector in this session and `content-system/seo/gsc-exports/` holds only a README. No GSC figures quoted.

## Refresh: what the old page already earns
- `/culture/8-turkish-wedding-traditions-you-didnt-know`: HTTP 200, indexable, 1,860 words, title 72 chars (too long), published 2017-06-06, modified 2026-10-21. DataForSEO ranked_keywords for this exact URL: no rows in AU or US (the index still attributes rankings to the legacy URL below).
- Domain filter 'turk' (AU): `/5-turkish-wedding-traditions-you-didnt-know` ranks #1 "turkish weddings" (140), #1 "traditional turkish weddings" (90), #2 "turkish wedding traditions" (90), #2 "turkish wedding" (140), #2 "wedding traditions turkey", #3 "turkish traditions wedding", #6 "henna night turkish", #7 "henna night turkey", #24 "turkish henna". This is the old slug of the same article (now under /culture/). Status of the legacy slug not confirmed (curl blocked in this sandbox).
- The old page is cited in Google's AI overview in Sydney, Melbourne and New York, and shows in the Singapore image pack. **Protect this with a 301 chain: legacy slug and /culture/ URL both to /expert-advice/turkish-wedding-traditions, no chains.**
- Other Turkish pages (both HTTP 200 today): `/how-to-plan-a-turkish-wedding` (721 words, H2 "Customs and traditions"), `/spotlight-on-turkish-wedding-destinations-the-best-places-to-tie-the-knot` (639 words, Istanbul, Cappadocia, Bodrum, Antalya). Neither appears in ranked keywords for 'turk' in AU. `/10-wedding-dress-designers-based-in-turkiye-you-shouldnt-miss` ranks #31/#36 for dress terms (no overlap).

## Keyword data (Australia, Google Ads)
| Keyword | Vol | KD |
|---|---|---|
| turkish wedding | 140 | n/a |
| turkish wedding traditions | 90 | 0 |
| turkish wedding customs | 90 | n/a |
| turkish henna night | 90 | 0 |
| kina gecesi | 90 | n/a |
| getting married in turkey | 10 | n/a |
| turkish wedding dress (related) | 210 | transactional, not this page |
Related (10/mo each): gifts, red ribbon, wedding night, dance, culture marriage rules; modern turkish wedding traditions (no volume).

## Region tables (top organic)
| Region | 1 | 2 | 3 | Features |
|---|---|---|---|---|
| Sydney | antalyatouristinformation (15 customs, 2022) | hauteweddingfrance (short, 2019) | Facebook group | AI overview cites us; PAA; video; images |
| Melbourne | same as Sydney | | | same |
| New York | "Wedding Culture in Turkey" | dailysabah | "Similarities and differences..." | AI overview cites us; PAA |
| Dubai | antalyatouristinformation | turkiyetoday | guidesforbrides | PAA; AI overview (async) |
| Singapore | turkiyetoday | pataaree | ternevents | our page in image pack |

PAA everywhere: Who pays for the wedding in Turkish culture? / Why do Turkish brides wear a red ribbon? (NY: significance of the red ribbon) / Do the bride and groom sleep together the night before? / Albanian traditions (off-topic).

## Pages read (Sydney top 3, Facebook skipped, #4 read instead)
| Page | Words (approx) | Headings | Pricing | Real weddings | FAQ/schema | CTA | Images | Strengths | Gaps |
|---|---|---|---|---|---|---|---|---|---|
| antalyatouristinformation.com | ~1,500 | 15 numbered H2s, rough wedding order | none | no | Article schema, no FAQ | quote form (planner) | 5 | broad coverage, kiz isteme wording, nikah step | salted coffee and foot-stepping as fact; "something old/new/borrowed/blue" presented as Turkish; no sources; 2022 |
| hauteweddingfrance.com | ~400 | none | none | no | no | message us | 1 | shoe-signing, red sash | thin, unsourced, 2019 |
| istanbultours.com | ~900 | question H2s | none | no | no | tour booking | 1 | question-led headings, nikah with two witnesses, regional dances | unsourced, "Kina" without diacritics, sales CTA |
Saved: `02-research/pages/antalyatouristinformation-turkish-traditions.md`, `hauteweddingfrance-turkish-wedding-traditions.md`, `istanbultours-turkish-wedding-experience.md` (reference only, originality check).

## Cross-region summary
- Guest counts: only antalyatouristinformation mentions scale ("500 or more" at provincial engagements), unsourced.
- Pricing shown: none on any page.
- Top concern (PAA): who pays, and what the red ribbon means.
- Common angles: numbered listicle; salted coffee; red sash; gold pinning; henna night; foot-stepping.
- Gap we can own: wedding order from asking to halay; sourced vs "often told" labelling; legal civil marriage for Australians with official sources; Smartraveller levels; regional variation; Turkish spelling with diacritics. No page-one result does any of these.
- Regional differences: AU SERPs identical and cite us; NY leans editorial (Daily Sabah); Dubai/Singapore lean planners and Turkish media.

## recommended_scope: au_focus
One page, Australian reader, with the legal and travel sections for Australians. SERPs are near identical across regions; no regional versions needed.

## Link checks (2026-11-02, DataForSEO on_page)
200: old /culture page, /destinations/europe/turkey, /why-is-turkey-so-popular-for-destination-weddings, /10-exquisite-venues-in-turkiye-to-consider-for-your-destination-wedding, /magazine, /how-to-plan-a-turkish-wedding, /spotlight-on-..., ich.unesco.org Turkish coffee, ktb.gov.tr wedding tradition.
404: /expert-advice/wedding-traditions (pillar, still a draft).
Timeout: smartraveller.gov.au Türkiye page (planner already holds 02-research/pages/smartraveller.md).
Not checked (time): /wonderland-concierge, Australian Embassy Ankara pages.
