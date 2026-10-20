# Link rules

## Internal (per post)
| Type | Count | Notes |
|---|---|---|
| Hub (destination or category page) | 1 | e.g. `/destinations/europe/france` |
| Related (posts, venues, packages, real weddings) | 2 to 4 | From the link map, topic-matched |
| Commercial (service page) | 1 to 2 | `/wonderland-concierge`, a package, `/privileges` |

- Anchor text describes the destination page ("how Wedded Privileges works for your guests"). Never "click here".
- Vary anchors; exact-match keyword anchor at most once.
- Don't link the same URL twice. Don't link to `noindex` drafts.
- Every target must be live (scraped OK during this run) and listed in `content-system/seo/link-map.csv`.
- After the draft: list 2 to 3 older pages that should link **to** the new post (`backlinks-todo.md`).

## External
- **Link to:** official sources (embassies, government marriage registries, Smartraveller, tourism boards), the venue's own site, respected editorial sources being cited.
- **Never link to:** competing planners or wedding marketplaces, content farms, affiliate listicles.
- 2 to 5 external links per post.
- All external links: new tab, `rel="noopener"`. Paid/affiliate: add `rel="sponsored"`.
- Government/legal links get a "checked" date in `02-seo.json` and are rechecked by `/wedded-refresh`.
