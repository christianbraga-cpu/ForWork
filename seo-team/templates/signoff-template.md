# Sign-off: <page subject>

Run: `<run_id>` · Action: `<action>` · Page: `<url>` · Status: **awaiting_signoff**

The page stays `noindex` until every box below is ticked.

## 1. Prices and offers (price approver: <name>)

- [ ] <price or offer> shown as <text> · ledger <F-id> · source <source>

## 2. Facts still to confirm

- [ ] `[[CONFIRM: ...]]` in section <id> · ask <who>

## 3. Conflicts resolved by the team (check you agree)

- [ ] <topic>: page uses <value> because <reason>; other value <value> from <source>

## 4. Images

- [ ] <slot>: licence <status>, credit <text>, consent <status>

## 5. Links

- [ ] Unverified internal URLs exist: <list>
- [ ] Back-link edits applied on: <list of source pages>

## 6. Brand read (brand owner)

- [ ] Read the page aloud once. Brand gate notes: <summary>

## 7. Unresolved after 2 revision rounds

- [ ] <issue>: options <a> / <b>; team recommends <x> because <reason>

## 8. Publish steps (in order)

- [ ] Apply `CHANGES.md` in the CMS (or deploy `site/<path>/index.html`)
- [ ] Remove `<meta name="robots" content="noindex">`
- [ ] Add the page to the sitemap and request indexing
- [ ] Update `seo-team/architecture/link-registry.csv`: status `live`
- [ ] Submit a test enquiry and confirm it lands in the CRM with the page source
- [ ] Start rank tracking for the keywords in `08-measurement-plan.json`

Signed off by: ________ Date: ________
