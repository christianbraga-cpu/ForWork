# Services the blog points to

Every post links to at least one of these. The CRO agent chooses the primary CTA from this list.

| Service | Who it's for | Page | Default CTA wording |
|---|---|---|---|
| **Wedded Concierge** (end-to-end destination planning) | Couples planning abroad who want one person to handle venue, travel, vendors and payments | `/wonderland-concierge` | "Speak with a Wedded Advisor" |
| **Destination packages** | Couples who have a destination or venue in mind | `/packages/<country>/<region>/<venue>` | "See the [venue] offers" |
| **Guest travel + Wedded Privileges** | Couples with many travelling guests | no page yet (`/privileges` 404s); use `/travel` | "Plan travel for your guests" |
| **Wedded Marketplace** | Couples who want to make their own arrangements | `/marketplace` | "Browse venues and vendors" |
| **Wonderland Studio** | Couples organising seating, RSVPs | `/wonderland-studio` (free); tools overview `/wedding-planning-tools` | "Try Wonderland Studio" |
| **Digital magazine** (lead magnet) | Early-stage dreamers | `/magazine` | "Read the free magazine" |

## Choosing the primary CTA
- **Early stage** (dreaming, "what is", "ideas"): magazine or destination guide lead magnet, then Concierge as secondary.
- **Comparing** (costs, "best", "vs", venues): Concierge consultation.
- **Decided** (a named venue or package): the package page.
- **DIY signals** ("find vendors", "list of"): Marketplace, with Concierge as secondary.

## UTM format
`?utm_source=blog&utm_medium=content&utm_campaign=<slug>&utm_content=<cta-position>`
