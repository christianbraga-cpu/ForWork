# External domains

The SEO reviewer blocks any external link to a domain in the blocked list, and
flags any domain that is in neither list for a human decision.

## Approved (link freely when they are the source of a fact)

| Type | Examples |
|---|---|
| Government and consular | smartraveller.gov.au, dfat.gov.au, homeaffairs.gov.au, italian consulate and embassy sites (esteri.it, ambcanberra.esteri.it, conssydney.esteri.it), gov.uk travel advice pages, travel.state.gov |
| Official tourism boards | italia.it, visittuscany.com, visitgreece.gr, indonesia.travel, visitdubai.com, france.fr, spain.info, visitportugal.com |
| Official venue sites | The venue's own domain (e.g. cappuccinacountryresort.com), only for venues we work with or name |
| Airports and transport | Official airport and rail operator sites (e.g. aeroporto.firenze.it, pisa-airport.com, trenitalia.com) |
| US government (added 27 Oct 2026 for US articles) | it.usembassy.gov, travel.state.gov, fam.state.gov, ssa.gov, irs.gov, healthcare.gov, dos.ny.gov, health.ny.gov, cityclerk.nyc.gov, portal.311.nyc.gov, sos.ca.gov, lavote.gov |
| Italian government and consular (added 27 Oct 2026) | consnewyork.esteri.it, conslosangeles.esteri.it and other esteri.it consulates, prefettura.it, comune.<town>.it town halls |
| Jewellery authorities and auction houses (added 27 Oct 2026) | gia.edu, sothebys.com, christies.com, and the official heritage or press page of the house that made a ring (e.g. cartier.com, tiffany.com, harrywinston.com), never their shop pages |
| Royal and Australian government (added 27 Oct 2026) | royal.uk, abf.gov.au |
| Australian government, marriage and documents (added 12 Nov 2026) | greece.embassy.gov.au and other embassy.gov.au missions, ag.gov.au, passports.gov.au, legislation.gov.au, nsw.gov.au (Registry of Births, Deaths and Marriages pages) and other state or territory BDM registry sites: bdm.vic.gov.au, qld.gov.au, wa.gov.au, sa.gov.au, justice.tas.gov.au, accesscanberra.act.gov.au, nt.gov.au (added 13 Nov 2026) |
| Greek government and municipalities (added 12 Nov 2026) | gov.gr, en.mitos.gov.gr, ypes.gr, mfa.gr, metafraseis.services.gov.gr, cityofathens.gr, chania.gr, heraklion.gr and other official Greek municipality sites |
| Fiji government and missions (added 13 Nov 2026) | foreignaffairs.gov.fj (Fiji Ministry of Foreign Affairs), fijiembassy.jp (Embassy of Fiji in Japan; older page, cross-check) |
| Indonesia and France, Australian missions (added 13 Nov 2026) | indonesia.embassy.gov.au, france.embassy.gov.au, consadelaide.esteri.it (Italian Consulate in Adelaide) |
| Major publications, for reported facts (added 27 Oct 2026) | vogue.com, vogue.com.au, people.com, harpersbazaar.com, townandcountrymag.com, bbc.com, apnews.com, reuters.com. Cite as "reported by"; prefer two independent sources for any carat or value |
| Weather and climate | Official meteorological services (e.g. bom.gov.au for comparisons, meteoam.it) |

Use `rel="noopener"` when opening in a new tab. Use `rel="nofollow"` for any
approved-category site you cannot fully vouch for. Use `rel="sponsored"` on
paid or affiliate links.

## Blocked (never link)

- **Competing marketplaces and agencies:** easyweddings.com.au,
  easyweddings.com, and any destination wedding agency or marketplace.
- **Wedding planners' own websites:** planners are partners, but link them
  only through their profile on our site (`/vendor/<slug>`), never their own site.
- **Lead-selling directories:** sites that sell enquiries to venues or vendors
  (e.g. hitched, weddingwire, theknot, zola, bridebook listings).
- **Content farms, AI-spun listicles, and pages ranking for our own keywords.**
- **Ring retailers' celebrity and "lookalike" pages** (they rank for celebrity engagement rings and sell copies); research-only.
- **Venue aggregators used only for cross-checking** (e.g. lalista.com): fine as
  research sources, never as outbound links.

## Research-only

Competitors and aggregators may be **read** for SERP analysis and fact
cross-checks. Their text is never copied and their images are never used.
