# Wedded Wonderland Content System

You give it three things: a **title**, a **keyword** and a **target audience**. The team plans, researches, writes, checks and loads the post into the CMS as a Draft.

```
/wedded-blog title="Marrying at an Amalfi Coast Villa" keyword="amalfi coast villa wedding" audience="Australian couples, 30s, AUD 150k+, early planning"
```

## Pipeline

```
00 input
 └─ 01 content-strategist ── brief
     └─ 02 seo-researcher ── SERP by region, gap report, outline, links
         ├─ 03 planner-sme ── source pack (facts, [[VERIFY]] items)      ┐ parallel
         └─ 04 visual-curator ── image plan, licensed images, placeholders ┘
             └─ 05 luxury-writer ── draft
                 └─ 06 editor ── rubric ≥ 4.0, facts, compliance, originality   (max 2 loops)
                     └─ 07 icp-reader × 5 ── reader reactions (isolated)
                         └─ 07b icp-panel-chair ── weighted gate ≥ 3.8, no must-fix (1 revision)
                             └─ 08 final copy
                                 └─ 09 cro-specialist ── CTA, lead magnet, UTMs
                                     └─ 10 distribution ── Pinterest, Instagram, newsletter
                                         └─ 11 cms-publisher ── publish package → CMS Draft → preview
                                             └─ 13 run report
```

Every stage writes a JSON **envelope** (`schemas/envelope.schema.json`) into `content/posts/<slug>/`. The orchestrator reads `status`, `self_qa` and `open_questions` before moving on.

## Files in a post folder

| File | Stage |
|---|---|
| `00-input.json` | Orchestrator |
| `01-brief.json` | Strategist |
| `02-research/serp-<location>.json`, `02-research/report.md`, `02-seo.json` | SEO researcher |
| `03-source-pack.json` | Planner SME |
| `04-images.json`, `images/`, `reference-only/` | Visual curator |
| `05-draft.md` (+ `05-draft-r2.md` …) | Writer |
| `06-edit.json` | Editor |
| `07-icp/<persona>.json`, `07-panel.json` | ICP panel |
| `08-final.md` | Writer (after panel) |
| `09-cro.json` | CRO |
| `10-distribution.json` | Distribution |
| `11-publish-package.json`, `12-cms-report.md`, `screenshots/` | CMS publisher |
| `13-run-report.md`, `backlinks-todo.md`, `run-log.md` | Orchestrator |

## Folders here

| Folder | Contents |
|---|---|
| `brand/` | Voice guide, banned phrases, brand facts, services |
| `personas/` | ICP persona cards (provisional until calibrated) |
| `rubrics/` | Editor rubric, image checklist, link rules, compliance, QA gates |
| `schemas/` | JSON schemas for every stage |
| `research/` | Locations and languages for SERP research |
| `seo/` | Link map (site URL inventory) |
| `images/` | Image register, sources policy, permission email template |
| `cms/` | CMS field map (filled by `/wedded-cms-discovery`) and publish checklist |
| `templates/` | Run report, backlinks to-do |
| `connectors/` | How each data tool is connected, and the `.mcp.json` example |
| `scripts/` | Validation, link map builder, image preparation |

## How long a run takes

Measured on the Lake Como test run (about 2 hours of actual work; the rest of that day was a stage stalled on a permission prompt, now pre-approved):

| Article type | First draft | Finished package |
|---|---|---|
| Single-topic guide | about 45 to 60 min | about 1 to 1.5 hours |
| List of 8 to 10 venues | about 1 to 1.5 hours | about 2 to 3 hours |
| Your checking (shorter VERIFY list) | | about 20 to 40 min |

**Fast mode** (now the default; see the skill): the ring-settings list ran in about 25 minutes, with the first draft at 13 minutes. Legal articles that need deeper fact-checking take about 45 to 60 minutes.

The first draft is sent to you as soon as it exists; the reader panel, CTA and social copy finish afterwards.

## Before the first real run

1. `/wedded-linkmap` to build the site URL inventory.
2. `/wedded-cms-discovery` (in Chrome, logged into the CMS) to fill `cms/field-map.md`.
3. Add licensed images to the Drive library and register them in `images/library-index.csv`.
4. Optional: connect DataForSEO, Semrush/Ahrefs, GSC (see `connectors/README.md`).
5. Optional: `/wedded-calibrate` with CRM data to replace the provisional personas.
