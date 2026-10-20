---
name: wedded-calendar
description: Plan a Wedded Wonderland content backlog from a list of titles/keywords/audiences, check each for keyword cannibalisation, and optionally run /wedded-blog for each. Use when the person types /wedded-calendar or gives a list of blog ideas.
---

# /wedded-calendar

`content/calendar.csv` columns: `id,title,keyword,audience,content_type,primary_category,priority,target_month,status,slug,draft_date,published_url,notes`

1. Take the person's list (pasted text, a CSV, or a Drive file). Each item needs title, keyword and audience; infer audience from context only if the person says so, otherwise leave a note.
2. For each item:
   - Check `content-system/seo/link-map.csv` for an existing page on the same keyword or topic (cannibalisation). If found, set `status: conflict` and note the URL.
   - Suggest `content_type` and `primary_category`.
   - If DataForSEO or Semrush/Ahrefs is connected, add AU search volume and difficulty to `notes`.
3. Set `priority`: high for commercial-investigation keywords tied to a package or destination we sell, medium for planning guides, low for trends/news.
4. Append rows with `status: planned`. Show the backlog as a table.
5. If the person says "run them", run `/wedded-blog` for each `planned` row in priority order, one at a time, updating `status` as each finishes.
