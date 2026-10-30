# House rules

Rules every page must follow, whatever its type. A breach is a `blocker` at the gates.
Values marked **CONFIRM** are defaults to check with the brand owner once; after that,
remove the marker.

Page-specific rules (offers, form fields, sections) do **not** belong here. They come
from the page facts and research doc for each run.

## Facts and claims

- Only facts in the run's Fact Ledger may be published. Page facts outrank the
  research doc, which outranks the existing page, which outranks the web.
- High-risk facts (prices, capacities, legal steps, travel times, inclusions) need a
  named source. Prices need a named approver in the page facts (`signed_off_by`).
- Anything unconfirmed is written as `[[CONFIRM: ...]]` and goes on `SIGNOFF.md`.

## Commercial (CONFIRM)

- Currency: AUD unless the page facts say otherwise. Format `From AUD 38,550`.
- Any "from" price is explained (what it assumes, and that the final cost is confirmed
  for the couple's dates and guest count).
- Price approver: named in each run's page facts. No approver, no live price.

## Conversion (CONFIRM)

- Every commercial page has one primary enquiry action. Endpoint, fields and response
  promise come from the page facts; if missing, the builder keeps the existing page's
  form unchanged (optimise/refresh) or adds a placeholder and a `dev_team` sign-off item (create).
- No pressure tactics (countdowns, "only X left").

## Competitors and sources

- Never reuse competitor branding, copy, claims or images.
- Competitor pages are research for structure and facts to verify, never a source to publish from.
- Images must have a recorded licence. See `seo-team/qa/checklists.md` (`images_v1`).

## Brand names (CONFIRM)

Use names exactly as the page facts or research doc give them. Record each brand,
programme and service name in the ledger (`category: brand_programme`) so every agent
spells them the same way.

## Indexing

- New and changed pages keep `<meta name="robots" content="noindex">` until
  `SIGNOFF.md` is complete. Removing it is a human step.
- Canonical: the page's absolute URL as given in the intake (no trailing slash unless
  the existing page uses one).
- `optimise` and `refresh` never change the URL. If the strategist believes the URL
  should change, it goes on `SIGNOFF.md` with a 301 redirect plan.

## Existing site chrome

For `optimise` and `refresh`, keep the existing page's header, footer, scripts,
tracking and stylesheet untouched. Only edit the content area and head tags the brief
covers. For `create`, mirror the closest existing page the intake identifies, or build
with neutral styles and list "apply site template" on `SIGNOFF.md`.
