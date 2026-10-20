# ForWork: Wedded Wonderland

This repo holds Wedded Wonderland (weddedwonderland.com) site drafts and the **AI content team** that writes blog posts end to end.

## Folder map

| Path | What it is |
|---|---|
| `site/` | Page drafts (e.g. `site/packages/italy/tuscany/cappuccina-country-resort/`). Each has a `NOTES.md` with checks still open. |
| `.claude/skills/` | Slash commands: `/wedded-blog`, `/wedded-linkmap`, `/wedded-cms-discovery`, `/wedded-refresh`, `/wedded-calendar`, `/wedded-calibrate` |
| `.claude/agents/` | The specialist subagents (strategist, SEO researcher, planner SME, visual curator, writer, editor, ICP readers, panel chair, CRO, distribution, CMS publisher) |
| `content-system/` | Shared knowledge: brand, personas, rubrics, schemas, locations, link map, image register, CMS field map, templates, scripts, connector setup |
| `content/posts/<slug>/` | One folder per post. Every stage writes its output here. |
| `content/calendar.csv` | Content backlog |

## Starting a post

```
/wedded-blog title="..." keyword="..." audience="..."
```

Read `content-system/README.md` for the full pipeline.

## Non-negotiable rules (all agents)

1. **No invented facts.** If a price, capacity, legal step, distance or date can't be traced to a source, write `[[VERIFY: what to check]]` and list it. Never guess.
2. **No unlicensed images.** Competitor and search-result images are reference only and live in `reference-only/`. AI images are never used for a real venue, destination or wedding.
3. **Never publish.** The CMS step saves a **Draft** only. A human clicks Publish.
4. **Never handle passwords.** Never ask for credentials, keys or tokens in chat. The person logs into the CMS in Chrome themselves, and connector keys live in environment secrets.
5. **Brand terms:** Wedded Wonderland, Wedded Concierge, Wedded Advisor, Wedded Privileges. Prices are "From AUD", and every price needs Nic's sign-off (flag it).
6. **No competitor branding or copy.** Don't reuse Easy Weddings (or any competitor) wording, claims or images.
7. **Australian English** (colour, organise, travelling). Never use em dashes.
8. **Stop cleanly.** If a gate fails twice, a required tool is missing, or the CMS doesn't match the field map, stop and write the run report. Don't work around it.

## Validation

```
python3 -I content-system/scripts/validate.py content/posts/<slug>
```

Checks every stage file against `content-system/schemas/`.
