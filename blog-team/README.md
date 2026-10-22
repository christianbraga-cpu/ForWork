# Wedded Wonderland blog team

An AI content team that runs inside Claude Code. You give it a **title**, a
**keyword** and a **target audience**. It researches, writes, reviews, critiques
the piece through your ideal clients' eyes, revises, and hands back a
publish-ready article with everything the CMS needs.

## Run it

Open this repo in Claude Code (web, desktop app or terminal) and type:

```
/write-blog "Planning a Tuscany Villa Wedding from Australia" | tuscany wedding planner australia | couples and the parents paying
```

Optional fourth part: `| markets: AU, US, UAE, Singapore`.

## The team

| Stage | Agent | Produces |
|---|---|---|
| Orchestrator | `/write-blog` (Editorial Director) | Gates, merged revision requests, `run-log.md` |
| 0 Strategy | `content-strategist` | `01-serp.json` (top 3 per market), `00-brief.json` |
| 1 Research | `researcher` | `02-research.json` (sourced facts, legal, prices, needs) |
| 2 Draft | `writer` | `03-draft-v1.md` (with claims, links, image slots) |
| 3 Review (parallel) | `editorial-director`, `fact-checker`, `seo-reviewer` | `04-reviews/vN/*.json` |
| 3 Reader panel (parallel) | `icp-reader` × primary, secondary, anti-persona | `04-reviews/vN/reader-*.json` |
| 4 Revise (max 2 loops) | `writer` | `03-draft-vN.md` |
| 5 Images | `photo-curator` | `05-assets.json` |
| 6 Publish package | `copy-editor` | `final.md`, `publish-package.json`, `chrome-upload-prompt.md`, `article.docx` |

## What you get in `articles/<date>-<slug>/`

- **`article.docx`**: sign-off sheet (meta, categories with the primary first,
  CTA, takeaways, image list, prices for Nic, open items) followed by the article.
- **`final.md`**: the article in Markdown with full front matter.
- **`publish-package.json`**: every CMS field, plus Article and FAQ schema.
- **`chrome-upload-prompt.md`**: paste into Claude in Chrome while logged in to
  your CMS. It builds the post, sets the primary category, saves a draft and
  checks the preview. You press Publish.
- **`run-log.md`**: what ran, scores, persona decisions, and what needs a human.

## Connectors (optional, no API keys needed)

The team uses whatever MCP connectors your Claude account has, and falls back
to built-in web search and fetch:

| Connector | Used for | Without it |
|---|---|---|
| DataForSEO | Real Google top 3 per city (Sydney, Dubai, Singapore...) | Web search, not localised per country (noted in the log) |
| Semrush | Volume and difficulty per country | Skipped |
| Firecrawl / Apify | Clean reads of ranking pages | Web fetch |
| Google Drive | Finding your own photos for each image slot | Search terms only |

## Files you should keep up to date

| File | Why |
|---|---|
| `brand/brand-profile.md` | Facts, offers, proof points, house rules |
| `brand/style-guide.md` | Voice and banned phrases |
| `brand/cta-library.md` | Approved CTAs |
| `brand/link-map.md` | Internal links; mark pages LIVE when published |
| `brand/domains.md` | Approved and blocked outbound domains |
| `brand/categories.md` | Your real CMS categories |
| `personas/*.md` | Ideal-client readers; calibrate from Zoho CRM |

## Still to confirm

- [ ] Your CMS, its admin URL and real category list (`categories.md`)
- [ ] Blog URL pattern (assumed `/blog/<slug>`) and named authors
- [ ] Whether Key Takeaways and CTA reusable blocks exist in the CMS
- [ ] Destination hub URLs beyond Italy (`link-map.md`, TO CONFIRM rows)
- [ ] Persona calibration from Zoho CRM enquiries, won deals and lost-deal reasons
- [ ] Image library location (Google Drive folder) for the photo curator

## House rules every agent follows

No invented weddings, quotes, prices or statistics (gaps become `[[NEEDS: ...]]`).
Prices are "From AUD" and go to Nic. No competitor branding, copy, images or
links. Legal claims cite official sources. No em dashes.
