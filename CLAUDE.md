# ForWork

Wedded Wonderland web pages (`site/`) and Page Studio (`studio/`), the agent team
that creates, optimises, refreshes and audits those pages.

## Page work

Any request to create, optimise, refresh or audit a page goes through the
`page-studio` skill (`.claude/skills/page-studio/SKILL.md`). It needs four inputs:
the page, the action, the research doc and the existing page facts. Start with
`studio/README.md`.

## Rules for everything in this repo

- Australian English. No em dashes anywhere.
- Prices are "From AUD x" and need sign-off (see `studio/config.json`).
- Never reuse competitor or marketplace branding, copy or images.
- Pages never show venue or supplier contact details; enquiries route to Wedded Concierge.
- Unconfirmed facts are hedged on the page and listed in the page's NOTES.md.
- Pages carry `noindex` until every fact needing sign-off is confirmed.
- CRM data is used as aggregates only. Never copy personal data into the repo.

## Tools

```bash
python3 studio/tools/validate_envelope.py <file.json>
python3 studio/tools/check_page.py <index.html> --facts <facts.json> --brief <brief.json>
python3 studio/tools/check_copy.py <30-page-copy.json> --brief <brief.json> --facts <facts.json>
python3 studio/tools/aggregate_personas.py <run_dir> <brief|copy|page>
node studio/tools/review_docx.js <run_dir> <out.docx> "<Page>"   # simple review doc (default)
node studio/tools/handoff_docx.js <run_dir> <out.docx>             # technical handoff for dev
```
