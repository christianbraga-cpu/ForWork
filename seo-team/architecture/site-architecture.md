# Site architecture and linking rules

The linking-specialist designs links from this structure; writers never add links
outside the plan. The registry (`link-registry.csv`) is the source of truth for which
URLs exist and which page owns which keyword. It starts empty and grows with every run.

## Hub and spoke model

Every page belongs to a cluster. The intake assigns a `page_type`; the linking rules follow it.

| Page type | Role | Links down to | Links up to | Links across to |
|---|---|---|---|---|
| `destination_hub` | Commercial hub for a place | Venues, guides, real weddings in that place | Parent destination hub | 2 to 4 sibling destinations |
| `venue` / `package` | Commercial spoke | Real weddings at that venue | Destination hub | 2 to 4 sibling venues |
| `service` | Commercial page for a service (planning, design, guest travel) | Proof (real weddings, case studies) | Services hub | Related services |
| `guide` | Informational (cost, legal, seasons, how-to) | | The commercial page that is the natural next step (required) | Related guides |
| `real_wedding` | Proof | | Venue, destination, services used, planner profile | 2 related real weddings |
| `planner_profile` | E-E-A-T | Weddings they led | Team hub | |
| `home`, `hub` | Navigation | Every hub | | |

## Rules

1. Breadcrumbs on every page below the homepage, with `BreadcrumbList` schema.
2. Every page gets at least one link **up**, the required **down** links for its type,
   and 2 to 4 **across**.
3. Every guide links to at least one commercial page as its natural next step.
4. Click depth: commercial pages within 4 clicks of the homepage; hubs within 2.
5. Anchors are descriptive and natural. A page's `primary_keyword` is used as exact
   anchor only by links pointing to that page, and at most once per linking page.
   Use the registry's `approved_anchors`.
6. Back-link tasks: a new page needs at least 3 existing pages edited to link to it
   (its hub and at least 2 siblings). Tasks go in the link plan and on `SIGNOFF.md` if
   the source page is not in this repo.
7. No orphans. A page with zero planned inbound links fails the SEO gate.
8. URL status in the registry:
   - `live`: confirmed to exist, link freely
   - `unverified`: seen in an existing page or the research doc but not confirmed;
     may be linked, each one goes on `SIGNOFF.md`
   - `planned`: does not exist yet, never linked; log as a future task
   - `draft`: produced by a run, not yet published
9. Registry updates: the linking-specialist adds a row for the run's page and for every
   internal URL it finds in the existing page, research doc or page facts (status
   `unverified` unless the facts confirm it).

## Outbound links

- Link to official sources for legal and travel facts (government, consulate, civil
  registry pages). Required on any legal-requirements content.
- Whether to link to venue or vendor websites is set in the page facts. Default: credit
  vendors on real weddings, do not link venues from commercial pages. **CONFIRM**
- Never link to competitors or aggregator directories.
- `rel="sponsored"` for anything paid, `rel="nofollow"` for anything we cannot vouch for.
