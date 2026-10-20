# QA gates

| Gate | After stage | Checked by | Pass rule | On fail |
|---|---|---|---|---|
| G1 Brief | 01 | Orchestrator | All required fields present, schema valid; no cannibalising URL (or the brief says how it differs) | Strategist redoes once, then stop |
| G2 Research | 02 | Orchestrator | ≥ 7 of 10 locations returned results, or the report explains gaps; outline + links present | Retry the failed locations once with the fallback source |
| G3 Sources | 03 | Orchestrator | Every `must_include` item has a fact or a `[[VERIFY]]` | Planner reruns for missing items once |
| G4 Images | 04 | Orchestrator | Every slot has an approved image or `status: needed`; zero `reference-only` in publishable slots | Curator fixes once |
| G5 Edit | 06 | Editor | Rubric avg ≥ 4.0, no criterion < 3, no blocking issue | Writer revises; **max 2 rounds**, then stop |
| G6 Reader panel | 07b | Panel chair | Weighted enquiry likelihood ≥ 3.8 and no must-fix | Writer revises **once**, editor re-checks blocking issues only |
| G7 Package | 11 | CMS publisher | `11-publish-package.json` valid; all images prepared; CTA + takeaways + categories present | Fix and recheck once |
| G8 CMS | 11 | CMS publisher | Draft saved, preview matches package, primary category confirmed | Stop and report; never publish |

Every stage also runs its own `self_qa` checks. Any `confidence` below 0.7 is listed in the run report for a human to look at.
