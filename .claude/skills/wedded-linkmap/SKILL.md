---
name: wedded-linkmap
description: Build or refresh the weddedwonderland.com URL inventory (content-system/seo/link-map.csv) used for internal linking and cannibalisation checks. Use when the person types /wedded-linkmap, or when /wedded-blog finds the link map stale.
---

# /wedded-linkmap

1. Run `mcp__Lead_MCP__firecrawl_map` with `url: "https://weddedwonderland.com"`, `limit: 5000`, `sitemap: "include"`, `include_subdomains: false`.
2. Save the raw result to `content-system/seo/firecrawl-map-latest.json` (Write tool).
3. If the WeddedAdmin connector is available, call `landing_pages_overview` with `days: 30, limit: 50`, and save `{"<path>": visitors}` to `content-system/seo/traffic-latest.json`.
4. Run:
   ```
   python3 -I content-system/scripts/build_linkmap.py content-system/seo/firecrawl-map-latest.json [content-system/seo/traffic-latest.json]
   ```
5. For rows with an empty `topic`, fill a short topic tag (destination, venue type, planning, fashion, honeymoon…) based on title and path. Leave `primary_keyword` empty unless obvious from the title; it's filled by GSC data later.
6. Mark known drafts (e.g. repo `site/` pages with `noindex`) as `noindex = yes`.
7. Update `content-system/seo/README.md` with the date and row count.
8. Report: rows total, rows by type, top 10 by visitors (if traffic data exists).

Don't commit `firecrawl-map-latest.json` or `traffic-latest.json` (they're in `.gitignore`).
