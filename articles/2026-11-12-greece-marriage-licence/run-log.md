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
- **Stage 1 lost:** the researcher was lost (likely a container restart) before saving any file. Not noticed until the user asked. Run switched to FAST MODE (SKILL.md "Fast mode"): two parallel research batches (A: Greek side, B: Australian side), writer, three parallel reviews, one revision loop, copy editor writes image briefs.
- **Stage 1 fast (2 batches, about 3.5 min each):** DONE. A (Greek side): 35 facts. **gov.gr civil licence entry (updated 5 Nov 2026) gives "Deadline of completion: 8 days" = 7-day objection wait + 1 day to grant; the title is officially supported** (corrects stage 0). Clock starts on a complete application incl. newspaper notice. Couples living abroad: a foreign certificate naming the other spouse counts as the licence (Interior Ministry circular 4 Jan 2019); Chania and Heraklion apply it (no Greek licence, notice or wait). Translations: Embassy page outdated; since 1 Sep 2021 Greek MFA Register of Certified Translators (Law 4781/2021) or a Greek consulate; no official source mentions NAATI. Thira and Mykonos unconfirmed. B (Australian side): 15 facts. CNI AUD 181, apostille AUD 105 (2026, CPI each 1 Jan), no published processing time or validity; no Australian registration step; recognition under Part VA; name change needs a state BDM certificate, translation required, some states refuse overseas certificates. Open: does the DFAT CNI name the spouse (decides whether the Chania/Heraklion no-wait route applies).
- **Stage 2 fast (writer, 4 min):** DONE. 03-draft-v1.md. --check: 2,441 reader words (41 over the 2,400 cap; trim in revision), 0 dashes, 0 placeholders, 12 external domains, none blocked. 59 claims, 25 links. Orthodox FAQ swapped for a same-sex FAQ (check sourcing). **Decision (default, change if you want):** Greek government and municipality domains approved in domains.md as official sources.
- **Stage 3 fast (3 parallel reviews, about 2 min):** accuracy FAIL 3.6 (blocker: Heraklion does not require the partner to be named; majors: 'apply' the 2019 circular is inference, C-04 rests on medium-confidence F-028, 'every Australian document' overstated). SEO FAIL 4.2 (keyword in no H2; 41 words over). reader:couple 3/3/3/3 ("ask your town hall" fatigue, vague money line, jargon, CONCIERGE-PAY). **Decision (default, change if you want):** C-04 softened to "indicates"; a Greek reader must confirm the circular before publish (N-11).
- **Stage 4 fast (one loop, 5 min):** DONE. 03-draft-v2.md applies all 20 merged items. --check: 2,378 reader words, 0 dashes, 0 placeholders, 11 domains, none blocked. YAML valid; 60 claims, 24 links. "Questions to send your town hall" checklist added. No re-review (fast mode); copy editor checks voice.
