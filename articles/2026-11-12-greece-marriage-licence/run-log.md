# Run log: Greece Marriage Licence and the Eight-Day Wait Explained

A first attempt (12 Nov 2026) was cancelled by the user before stage 0 ran, because plan mode was still on. This run restarts from the same inputs.

## Inputs (from the user, 12 Nov 2026)
- Title: Greece Marriage Licence and the Eight-Day Wait Explained
- Primary keyword: greece marriage licence
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/destination-weddings/greece-marriage-licence
- Slug: greece-marriage-licence
- Primary CMS category: Destination Weddings (confirmed)
- Type: Legal. Cluster: Wedding Traditions (as given by the user).
- Language: Australian English, AUD (house default); EUR where sourced
- Personas: primary `couple` (fears adapted to the legal topic), secondary `paying_parent` (advisory), anti `bargain_hunter`
- Markets: Sydney, Melbourne (lead); London, New York, Dubai, Singapore
- Event link: `/wedded-world` (Melbourne event finished 8 Nov 2026)
- Legal sources: official only (Australian Embassy Athens, Smartraveller, DFAT apostille, gov.gr and municipalities, Greek consulates in Australia, Attorney-General's Department)
- Pipeline: full (all stages, up to 2 loops); user toggles /fast
- Tools: Firecrawl was out of credits on 29 Oct; agents try it once, then Apify web-fetch, then WebSearch
- Brand sources: live site only (brand-profile.md)

## Stages
- **Stage 0 (content-strategist):** DONE. Volumes very low (most variants no data; "getting married in greece" 10 / 90 / 260 AU / US / UK): a trust and People Also Ask page. SERP: Facebook threads hold most top 3 slots in Sydney, Melbourne and Singapore; no sourced Australian guide ranks. DataForSEO failed for London and Dubai (WebSearch fallback); Firecrawl out of credits (Apify web-fetch used). **Eight-day finding:** gov.gr (updated 5 Nov 2026) and the Municipality of Athens say one week (7 days) after a complete file; "eight days" appears only on commercial pages. Couples living abroad may be asked for a home-country licence instead (Australia: DFAT CNI); confirm by municipality. Possible conflict: Australian Embassy says only Greek Foreign Ministry translations; Interior Ministry lists that service as abolished in 2021. Title decision sent to the user. Cannibalisation: partial with /destinations/europe/greece and /expert-advice/overseas-marriage-certificate. Brief: 8 H2s, 1,900 to 2,400 words, discovery_call, 17 official sources. Orchestrator added two live Greece pages to link-map.
- **Title decision (user, 12 Nov 2026):** keep "Greece Marriage Licence and the Eight-Day Wait Explained". The article is written as a myth-buster: the first section states plainly that official sources give one week from a complete application, and explains where "eight days" comes from (submission day plus seven). Stage 1 (researcher) running.
