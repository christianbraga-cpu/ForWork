---
name: wedded-refresh
description: 30/90-day review of a published Wedded Wonderland post. Rechecks rankings across the research locations, broken links, outdated facts and GSC performance, and writes a refresh brief. Use when the person types /wedded-refresh url=<url or slug>.
---

# /wedded-refresh

1. Find the post folder (`content/posts/<slug>/`) from the URL or slug. If none exists, create `content/posts/<slug>/` with just a `00-input.json` holding the URL.
2. **Rankings:** rerun the primary keyword SERP in every location in `content-system/research/locations.yaml` (same source order as the seo-researcher). Record our position (or "not in top 10") and the new top 3.
3. **GSC:** if connected (live MCP or the latest Drive export in `Wedded SEO/GSC exports/`), pull clicks, impressions, CTR and average position for the URL and its top queries.
4. **Links:** scrape the live page with Firecrawl; check every link is live; recheck government/legal links and compare to the facts in `03-source-pack.json`.
5. **Facts:** for each fact with `checked` older than 90 days, re-scrape its source; flag changes.
6. **Conversions:** if WeddedAdmin is connected, note enquiries attributed to `utm_campaign=<slug>`.
7. Write `content/posts/<slug>/refresh-<YYYY-MM-DD>.md`:
   - Verdict: **keep**, **refresh**, **merge** (with which URL) or **retire**
   - Ranks but doesn't convert → CRO changes; converts but doesn't rank → SEO changes
   - A short refresh brief (new H2s, facts to update, links to fix, new competitors' angles)
8. If the verdict is refresh, offer to run `/wedded-blog resume=<slug>` from the writer stage using the refresh brief.
