# Pipeline

The orchestrator (`/seo-page` skill, running in the main session) owns this pipeline.
Agents never call each other; they read files from the run folder and write one
envelope each. The orchestrator moves the run between states.

## State machine

```
intake → researched → briefed → produced → in_qa ─┬─→ awaiting_signoff → (human) approved → published → measuring
                                     ▲            │
                                     └── revise ◄─┘   (max 2 revision rounds, then escalate)
```

`audit` runs stop at `in_qa` and finish with a report (`audit_complete`).
The pipeline never moves a run past `awaiting_signoff`. Humans do that.

## Phases

| # | Phase | Agent(s) | Reads | Writes | Runs in parallel with |
|---|---|---|---|---|---|
| 0 | Intake | orchestrator | the four inputs | `inputs/`, `00-intake.json` | |
| 0b | Fact Ledger | fact-checker (mode `ledger`) | facts, research, existing page | `00-fact-ledger.json` | |
| 1a | Keyword research | keyword-researcher | intake, research, ledger | `01a-keyword-map.json` | 1b, 1c |
| 1b | Technical audit + requirements | technical-seo | existing page, registry | `01b-tech-audit.json` | 1a, 1c |
| 1c | AI search baseline | ai-search-specialist | research, ledger | `01c-ai-search-baseline.json` | 1a, 1b |
| 2a | Page Brief | seo-strategist | everything from 0 and 1 | `02a-page-brief.json` | |
| 2b | Link plan | linking-specialist | brief, registry, ledger | `02b-link-plan.json` | 2c, 7, 8 |
| 2c | Conversion spec | cro-specialist | brief, personas, site rules | `02c-conversion-spec.json` | 2b, 7, 8 |
| 3 | SME questions | orchestrator | ledger gaps, brief `open_questions` | `03-sme-questions.md` | 2b, 2c |
| 4a | Copy | copywriter | brief, ledger, link plan, conversion spec | `04a-copy.md`, `04a-copy.json` | 4b |
| 4b | Images | visual-seo | brief, ledger, existing page | `04b-images.json` | 4a |
| 4c | Build | page-builder | 4a, 4b, 2b, 2c, 1b | page at site path, `04c-build.json` | |
| 5 | QA gates | fact-checker (mode `gate`), brand-guardian, seo-qa, technical-qa | built page + all above | `05-qa-fact.json`, `05-qa-brand.json`, `05-qa-seo.json`, `05-qa-technical.json` | each other |
| 5a | Persona panel | icp-critic × N | screenshots + page | `05-icp-<persona>.json` | each other |
| 5b | Synthesis | persona-synthesizer | all `05-icp-*` | `05-icp-synthesis.json` | |
| 5c | Revision decision | seo-strategist (mode `arbitrate`) | all `05-*` | `05-revisions.json` | |
| 6 | Sign-off pack | orchestrator | everything | `REPORT.md`, `SIGNOFF.md` | |
| 7 | Amplify plan | digital-pr, ai-search-specialist (mode `plan`) | brief, ledger, registry | `07a-pr-plan.json`, `07b-entity-plan.json` | 2b to 5 |
| 8 | Measurement plan | analytics-specialist | brief, conversion spec | `08-measurement-plan.json` | 2b to 5 |

Phases 7 and 8 only need the brief, so they start straight after 2a and run while the
page is produced.

## Action routing

| Phase | create | optimise | refresh | audit |
|---|---|---|---|---|
| 0, 0b | yes | yes | yes (ledger is a **diff** against the live page) | yes |
| 1a keywords | yes | yes | only if research doc has new keyword data | yes |
| 1b tech audit | requirements only | full audit + requirements | quick audit | full audit |
| 1c AI search | yes | yes | skip | yes |
| 2a brief | full brief | brief with `keep / change / remove` per section | change list only | skip |
| 2b links | yes | yes | only if URLs changed | audit mode |
| 2c CRO | yes | yes | skip | audit mode |
| 4a copy | all sections | changed sections; untouched sections kept verbatim | affected sections | skip |
| 4b images | yes | yes | only if image facts changed | audit mode |
| 4c build | new page | edit existing page | edit existing page | skip |
| 5 gates | all four | all four | fact + technical | all four, on the existing page |
| 5a personas | full panel | full panel | primary ICP + skeptic | full panel |
| 5c revisions | yes | yes | yes | skip (findings go in the report) |
| 7, 8 | yes | yes | skip | yes |

## Panel selection

The brief's `target_icps` plus `icp_skeptic`, always. If the brief names no ICP,
use `icp_intl_couple` and `icp_funding_parent`.

## Revision loop

1. Strategist reads every gate and the persona synthesis, writes `05-revisions.json`:
   a list of tasks, each with `owner`, `issue`, `evidence` (quotes), `priority`.
2. Orchestrator sends each task to its owner. Owners write a new version of their
   envelope (`version` + 1). The page builder rebuilds.
3. Only gates and personas that failed or flagged the changed sections re-run.
4. After **2 rounds**, anything still failing goes to `SIGNOFF.md` under
   "Unresolved, needs a human decision" with both sides of the argument.

A gate `fail` with `severity: blocker` (for example a wrong price, a legal claim
with no source, an image with no licence) can never be waived by the strategist.
It is either fixed or stays on the sign-off list and the page stays `noindex`.

## Escalation rules

- Two agents disagree twice on the same point: strategist decides, records the
  reason in `05-revisions.json` under `decisions`.
- An agent returns `status: blocked`: orchestrator resolves it from the inputs if it
  can; otherwise adds it to `03-sme-questions.md` and continues with a placeholder.
- A fact conflict between page facts and research doc: page facts win, conflict is
  listed in the ledger and on the sign-off list.

## File naming

`<phase>-<role-or-topic>.json`, one envelope per file. A revised output overwrites
the file with `version` incremented and the previous version copied to
`history/<file>.v<n>.json`.
