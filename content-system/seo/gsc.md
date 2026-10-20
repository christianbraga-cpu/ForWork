# Google Search Console data (Drive export, Option A)

Agents read Search Console data from a monthly export saved to Google Drive. There's no live GSC connection.

## Where the export lives
- Drive folder: `Wedded SEO/GSC exports/`
- File name (Search Console's default, don't rename): `weddedwonderland.com-Performance-on-Search-<YYYY-MM-DD>`
- The folder must be in, or shared with, the Google account connected to Claude's **Google Drive** connector.

## How an agent finds the latest export
1. `mcp__Google_Drive__search_files` with
   `title contains 'Performance-on-Search' and mimeType = 'application/vnd.google-apps.spreadsheet'`
   (also try without the mimeType clause, as some are shortcuts).
2. Pick the file with the newest date in its title (fall back to newest `modifiedTime`).
3. `mcp__Google_Drive__read_file_content` with its `fileId`.
4. Record `gsc_export: {file, date, age_days}` in the stage's envelope (`tools_used` + a note in the report).

**Missing or older than 45 days:** say so in the report and carry on without it. Never invent GSC figures.

## Tabs in the export and what they're for

| Tab | Columns | Used for |
|---|---|---|
| **Queries** | Top queries, Clicks, Impressions, CTR, Position | Which searches we already appear for; real wording couples use (secondary keywords, FAQ questions, anchor text) |
| **Pages** | Top pages, Clicks, Impressions, CTR, Position | Cannibalisation (which of our URLs already gets impressions for the topic), choosing strong internal link targets |
| **Countries** | Country, Clicks, Impressions, CTR, Position | Which markets find us (weights the 10 research locations) |
| **Devices** | Device, Clicks, … | Mobile share (layout and Key Takeaways priority) |
| Search appearance, Dates, Filters | | Context only |

## Rules of thumb
- **Cannibalisation:** a page with impressions on the target keyword at position ≤ 20 means the new post must take a different angle or link to it as the main page. Tell the strategist.
- **Quick wins:** queries at positions 5 to 20 with high impressions and low CTR are worth an H2, FAQ question or title tweak.
- The export covers the whole site, not one query. Matching is by substring, so check related wording too (e.g. "italy wedding package", "wedding packages italy").

## Fallback: export file in the repo
If the export can't be put in the connected Drive, download it instead (Search Console → Export → **Download CSV**, which gives a zip of CSVs, one per tab), unzip it and upload the CSVs to `content-system/seo/gsc-exports/<YYYY-MM-DD>/` on this branch (github.com → the repo → branch `claude/keen-heisenberg-5p5pt4` → that folder → **Add file → Upload files**). Agents check this folder when no Drive export is found, and use the newest dated subfolder.
