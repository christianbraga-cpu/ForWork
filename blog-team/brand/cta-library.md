# CTA library

The brief picks one primary CTA and optionally one soft CTA. The writer uses
the copy below as written (light edits for context are fine; never change the
promise). In the CMS, CTAs are placed with the shared CTA block, never typed
into the body.

| ID | Use when | Heading | Body | Button | URL |
|---|---|---|---|---|---|
| `concierge_advisor` | Default for consideration and decision pieces | Speak with a Wedded Advisor | One person plans everything with you from Australia, in your time zone, with the fee agreed in writing before any work begins. | Speak with your Wedded Advisor | `/wonderland-concierge` |
| `package_enquiry` | Article centres on a venue with a live profile or package | Enquire about [Venue] | Your Wedded Advisor checks availability, costs it on your dates in AUD and holds the date once you agree. | Enquire now | `/venue/<slug>` if live, else `/wonderland-concierge` |
| `destination_explore` | Awareness pieces, early-stage readers | Explore weddings in [Destination] | See venues, seasons, getting there and marrying legally, all in one place. | Explore [Destination] | `/destinations/<region>/<country>[/<area>-wedding]` (see link map) |
| `packages_browse` | Comparison or round-up pieces | Compare wedding packages | See what each venue includes and where each offer starts, in AUD. | See the packages | `/destination-wedding-packages` or `/destination-packages` |
| `marketplace_diy` | Secondary only, for readers planning themselves | Prefer to plan it yourself? | Browse venues and vendor profiles and contact professionals through the Wedded Marketplace. | Browse vendors | `/vendor` or `/venue` |
| `privileges` | Accommodation and guest-stay pieces | Arrive with Wedded Privileges | Benefits come with every room your guests book, through invitation-only hotel programs. Benefits vary by property. | See wedding and honeymoon travel | `/travel` |
| `wedded_world_melbourne` | Australia or Melbourne posts, until 8 Nov 2026 | Meet us at Wedded World Melbourne | The luxury wedding showcase at 1 Hotel Melbourne, 7 and 8 November 2026. Discover, experience and book. | Get tickets | `/wedded-world/melbourne` |
| `quiz` | Early-stage readers unsure where to marry | Not sure where to marry? | Take the 12-question destination wedding quiz for a ranked top three, an indicative budget and your guest travel. | Take the quiz | `/destination-wedding-quiz` |

## Soft CTA lines (mid-article, one sentence)

- "Your Wedded Advisor can hold a room block for your guests while you decide."
- "If you would rather not manage this yourself, a Wedded Advisor can [task] for you."
- "Every price we quote is in AUD, so there is no currency surprise."
