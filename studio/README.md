# Page Studio

A team of specialist agents that creates, optimises, refreshes or audits one
Wedded Wonderland page at a time. You give it four inputs and it produces a
publish-ready package with every unconfirmed fact flagged for sign-off.

## How to start a run

In Claude Code, in this repo, say:

> Run page studio.
> Page: /packages/italy/tuscany/cappuccina-country-resort
> Action: optimise
> Research doc: <Drive link, Notion link, repo path or pasted text>
> Existing page facts: <table or list>

Or type `/page-studio` and paste the filled-in `intake/TEMPLATE.md`.

## The team

| Agent | Role | Stages |
|---|---|---|
| Project Lead (`.claude/skills/page-studio`) | Orchestrates, routes, runs the gates, owns `facts.json` | All |
| `seo-strategist` | Keywords, intent, content brief, internal link plan | 1, 2, review |
| `geo-specialist` | AI search citations and requirements | 1, 8 |
| `fact-checker` | Verifies every claim against facts and official sources | 1, 3, 6 |
| `analytics-lead` | Baseline, CRM signal, tracking, measurement | 1, 5, 9 |
| `ux-conversion` | Outline consult, design spec, enquiry form | 2, 4 |
| `copywriter` | Page copy, meta, FAQ, captions | 3 |
| `visual-lead` | Image selection, rights, file names, alt drafts | 3 |
| `technical-seo` | Builds the HTML, schema, performance, screenshots | 5, 6, review |
| `digital-pr` | Earned links and features plan, draft pitches | 8 |
| `local-seo` | Local signals, only where the brand has a local presence | 8 |
| `persona-reader` | Synthetic ICP reader, one persona at a time | 2b, 3b, 6 |
| `qa-reviewer` | Independent rubric and checklist judge | 3, 6 |

## Workflow

```
Intake ─► 1 Research ─► 2 Architecture ─► 2b Personas ─► 3 Content ─► 3b Personas ─► 4 Design ─► 5 Build ─► 6 QA gate ─► 7 Package ─► 8 Amplify ─► 9 Measure
          SEO, GEO,      SEO + UX          on brief      Copy +        on copy        UX          Tech SEO    automated +   NOTES,      PR, GEO,    Analytics
          facts,                                         visuals,                                 + tracking  reviewers +   Word draft  local
          baseline                                       peer review                                          personas
```

Which stages run depends on the action (`create`, `optimise`, `refresh`, `audit`)
and the scope. Optimise and refresh default to `scope: copy`: research, brief,
copy, persona and fact reviews run in full, but there are no image, layout or code
changes, and the output is a copy change list for the CMS. Ask for `scope: full`
when you want more. The tables are in the skill file.

## QA in three layers

1. **Self-check**: each agent runs its checklist in `checklists/` and records the results in its envelope.
2. **Peer review**: a different role reviews each artefact (SEO lens on copy, fact-checker on copy, technical SEO on images), plus the persona panel.
3. **Gate**: `tools/check_page.py` (automated), the brand voice review, the final fact pass and the persona page review. Rule: zero blockers, majors fixed or accepted in `decisions.md`. At most two revision rounds before the Project Lead decides.

## Handoffs

Every agent writes one envelope JSON file (`schemas/envelope.schema.json`) with a
typed payload (`schemas/payloads/`). `tools/validate_envelope.py` checks every file
before it moves on. A run's files live in `runs/<run_id>/`:

```
00-intake.md          research-doc.md        facts.json         current.html
10-keyword-research   11-ai-search           12-fact-audit      13-baseline
20-content-brief      21-ux-consult          22-persona-brief-summary
30-page-copy          31-image-set           32..34 reviews     35-persona-copy-summary
40-design             50-build-report        51-tracking
60-automated-qa       61-review-brand        62-review-facts-final   63-persona-page-summary
80-pr-plan            81-geo-plan            82-local-plan      90-measurement
persona/<stage>-<persona_id>-r<n>.json       screens/           decisions.md
CHANGELOG.md (optimise, refresh)             SUMMARY.md
```

The page itself goes to `site/<page path>/index.html` with `NOTES.md` and
`CMS-HANDOFF.md` next to it. `CMS-HANDOFF.md` is the file you take to the CMS: a
ready-to-paste prompt for the Claude in Chrome extension, plus an ordered change list
(exact current text, exact new text, reason, what to check after). For pages that
already exist in the CMS it lists changes, not a whole-page replacement.

## Reference page

`site/packages/italy/tuscany/cappuccina-country-resort/` is the reference for
package pages: section set, components, class names, image placeholder slots,
enquiry form, schema graph and the NOTES.md format. New package pages follow it
unless the brief records a reason not to.

## Folders

| Folder | Contents |
|---|---|
| `config.json` | Brand, sign-off owners, source of truth order, markets, QA limits |
| `intake/` | The intake template |
| `templates/` | The CMS handoff template |
| `cms-profile.md` | How the custom CMS is edited (fill in once) |
| `standards/` | Brand voice, banned phrases, linking, images, performance budget |
| `checklists/` | Self-check and review checklists per role, plus the QA gate |
| `schemas/` | Envelope and payload JSON schemas |
| `personas/` | The ICP panel and its evidence (see `personas/README.md`) |
| `tools/` | `validate_envelope.py`, `check_page.py`, `aggregate_personas.py` |
| `runs/` | One folder per run |

## Connectors used

| Connector | Used by | For |
|---|---|---|
| Semrush | SEO, analytics, PR | Keywords, organic research, competitors, backlinks, traffic |
| DataForSEO | SEO, GEO, tech SEO, PR, local | SERP, keyword ideas, intent, difficulty, AI search mentions, Lighthouse, backlinks, business listings |
| Zoho CRM | Analytics, persona refresh | Enquiry demand by destination, persona evidence (aggregates only) |
| Google Drive / Notion | Project Lead | Fetching research docs |
| Lead_MCP (Firecrawl) / Apify | Fact checker, Project Lead | Scraping official venue sites and current pages |
| Canva | Visual lead | Graphics only (maps, comparison cards) |

See the top-level CLAUDE.md for what is still missing.
