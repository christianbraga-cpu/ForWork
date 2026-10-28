# Facts library

Verified facts reused across runs, so the fact checker only checks what is new.

- `general.json`: facts that are not about one country (passport rules from Smartraveller,
  gov.uk and travel.state.gov in general form; brand facts).
- `<country>.json`: facts for one destination.

Each fact records `verified_on` and `reverify_after` (90 days). In fast mode the fact checker
reuses any fact whose `reverify_after` is in the future, re-checks only expired ones, and adds
new facts to the right file at the end of the run. A fact still `unconfirmed` stays unconfirmed
until someone signs it off; reuse does not upgrade it.
