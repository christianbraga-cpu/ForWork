# SEO page team

A team of 17 specialist agents that takes any page (destination, venue, service, guide,
real wedding, hub) from research to a sign-off-ready build. There is no fixed template:
the page's structure comes from the research doc, the page facts and the existing page. You give it four things; it gives you a finished page, a QA trail and a
short list of decisions only a human can make.

## What you give it

| Input | What it is | Example |
|---|---|---|
| **page** | The live URL, site path, or HTML file the work is about | `https://example.com/destinations/amalfi-coast` |
| **action** | What to do (see below) | `optimise` |
| **research** | The full research doc: the starting point for keywords, competitors, SERP notes, subject detail | `inputs/amalfi-research.docx` |
| **facts** | Existing page facts: what is already known and verified about the page and its subject (prices, capacities, inclusions, names, form, sign-offs) | `inputs/amalfi-facts.md` (use `templates/page-facts-template.md`) |

Files can be Markdown, text, .docx, PDF or pasted text.

### Actions

| Action | Use it when | What runs |
|---|---|---|
| `create` | The page does not exist yet | Every phase |
| `optimise` | The page exists and should rank and convert better | Audit first, then every phase, preserving the URL and anything that already works |
| `refresh` | Facts, prices, seasons or offers changed | Fact diff, rewrite affected sections only, Fact + Technical gates, reduced persona panel |
| `audit` | You want a diagnosis, no changes | Research, audit, all QA gates and the persona panel in read-only mode, then a report |

## How to run it

```
/seo-page page=https://example.com/destinations/amalfi-coast action=optimise research=inputs/amalfi-research.docx facts=inputs/amalfi-facts.md
```

## What you get back

A run folder at `seo-team/runs/<YYYY-MM-DD>-<slug>-<action>/`:

```
inputs/                     copies of the four inputs
00-intake.json              normalised inputs, action plan
00-fact-ledger.json         every fact with its source and status
01a-keyword-map.json        keyword researcher
01b-tech-audit.json         technical SEO (existing pages) and technical requirements
01c-ai-search-baseline.json AI search / entity baseline
02a-page-brief.json         strategist: the contract every producer works to
02b-link-plan.json          internal + outbound links, back-link tasks
02c-conversion-spec.json    CRO: enquiry flow and trust placement
03-sme-questions.md         questions only planners / the venue can answer
04a-copy.md / .json         copywriter
04b-images.json             image plan, alt text, captions, rights status
04c-build.json              page builder (the page itself is written to site/)
05-qa-*.json                fact, brand, SEO and technical gates
05-screens/                 mobile and desktop screenshots (PNGs are git-ignored)
05-icp-*.json               one critique per persona
05-icp-synthesis.json       merged persona findings
07a-pr-plan.json            inbound link and PR opportunities
07b-entity-plan.json        AI search / entity consistency actions
08-measurement-plan.json    tracking and 14/30/90 day checks
CHANGES.md                  every edit, section by section (optimise/refresh)
REPORT.md                   what was done, scores, what changed and why
SIGNOFF.md                  the human checklist: prices, claims, images, publish steps
```

The page is written to `site/<path>/index.html` (for example `site/destinations/amalfi-coast/index.html`)
with `noindex` on. For a live page that is not in this repo, the orchestrator saves a snapshot of
the live HTML to `inputs/existing-page.html` and the builder edits a copy of it, so the site's own
header, footer, scripts and tracking are preserved. `CHANGES.md` in the run folder lists every
edit so a developer can apply it to the CMS.

## What still needs a human

The team never publishes and never treats its own guesses as facts. `SIGNOFF.md`
always lists:

- Prices and offers (price approver in `brand/site-rules.md`)
- Any claim still marked `[[CONFIRM: ...]]`
- Image rights and couple consent
- Final brand read
- Publish steps: remove `noindex`, apply back-link edits, request indexing

## Folder map

| Path | Purpose |
|---|---|
| `.claude/skills/seo-page/SKILL.md` | The orchestrator: runs the phases and routes work |
| `.claude/agents/*.md` | The 17 team members |
| `workflows/pipeline.md` | Phases, action routing, state machine, revision rules |
| `brand/` | Voice guide and house rules |
| `architecture/` | Site architecture and the link registry |
| `personas/` | ICP personas for the critique panel |
| `schemas/` | Message envelope, intake, fact ledger, page brief, payload specs |
| `qa/checklists.md` | Every self-check and gate, with stable IDs |
| `templates/` | Page facts input, SME questions, report and sign-off templates |
| `tools/` | Deterministic checks: page linter, run validator, screenshot renderer |

## Keeping it sharp

1. **Ground the personas.** They start as hypotheses. Replace the evidence sections with
   patterns from Zoho CRM won/lost deals and consultation notes (see `personas/README.md`).
2. **Confirm the voice guide** with the brand owner (`brand/brand-voice.md`, items marked CONFIRM).
3. **Keep the link registry current.** Every published page adds a row
   (`architecture/link-registry.csv`).
4. **Calibrate.** Run `action=audit` on pages whose enquiry rate you know. If the persona
   panel's `enquiry_intent` scores do not rank them in the same order, adjust the personas.
