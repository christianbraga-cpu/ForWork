# Claude in Chrome: CMS upload prompt (Honeymoon itinerary)

Paste everything below the first rule into the Claude side panel in Chrome while
logged in to the CMS. Upload the five images to the media library first if
direct uploads are unreliable. Never type or share a password in this prompt;
log in by hand before you paste it.

**DRAFT ONLY. Never publish. Follow the NEW-URL check below: update the existing post as a draft if it exists, otherwise create a new draft post.**

---

Open [[NEEDS: CMS admin URL]] in a new tab. If a login screen appears, stop and
ask me to log in; never enter, read or store a password.

**NEW-URL check first (Zoho WC3-T1011).** /travel-guides/honeymoon-itinerary
returned 404 on 23 Nov 2026. In Posts, search for "honeymoon-itinerary" and
"Honeymoon Itinerary" across All, Drafts, Pending and Trash, and check whether a
post with the slug honeymoon-itinerary already exists.

- **If it exists:** open that post and UPDATE it in place with the details
  below, saved as a DRAFT only. Keep the slug exactly as it is. If the post is
  live, do not click Update, Publish or Schedule; use the CMS's save-as-draft or
  revision option, and if there is no way to save a draft revision without
  changing the live post, stop and tell me.
- **If it does not exist:** create a NEW post with slug honeymoon-itinerary in
  Travel Guides and save it as a draft.

Either way the slug must be exactly honeymoon-itinerary; if the CMS offers
honeymoon-itinerary-2 or similar, stop and list it. Do not add any redirect.
Work carefully and do not click Publish, Update on a live post, or Schedule.

1. **Title:** Honeymoon Itinerary Template and Two Week Sample
2. **Slug / permalink:** honeymoon-itinerary (full URL https://weddedwonderland.com/travel-guides/honeymoon-itinerary)
3. **Body:** paste the article below. Convert headings to Heading blocks (H2,
   H3), bullet and numbered lists to List blocks, the "- [ ]" lines under
   "Before you go" to a Checklist block (or a List block if there is none), and
   FAQ to the FAQ block if the site has one. Replace each `[IMAGE: file]` line
   with that image (see step 6). Keep all 22 links as given; external links
   (passports.gov.au, smartraveller.gov.au) get rel="noopener"; internal links
   get no rel. Do not edit copy.
   **The itinerary template must be a native Table block**, not pasted text, a
   code block or an image: 8 columns (Day and date, Base, Morning, Afternoon,
   Evening, Transfer and timing, Booked (yes/no), Notes), a header row, and 14
   rows Day 1 to Day 14 with the other cells empty. Directly above the table,
   keep the header block as four separate Paragraph blocks with the labels in
   bold: "Passports: names as printed and expiry dates", "Insurance policy and
   emergency line:", "Emergency contacts:", "Your advisor's number:".
4. **Key Takeaways:** insert the reusable "Key Takeaways" block right after the
   intro paragraph, with these bullets:
   - Plan the shape of the honeymoon first (arrival and rest days, how many bases, which day you travel between them) and choose the places second.
   - Our two week sample uses two bases with a dedicated travel day between them, a gentle first two days and an open final morning before the flight home.
   - Check your passport validity and allow at least six weeks for a new one (see Documents below).
   - Choose travel insurance that covers every country on the trip, including stopovers and transit points, and check which activities the policy excludes.
   - Book the honeymoon in the name on the passport you will carry, and book a doctor's visit at least eight weeks before you fly.
5. **CTA:** insert the reusable CTA block "discovery_call" at the `[CTA: discovery_call]`
   marker at the end of the article. Heading: "Not sure where to start? Book a free Discovery Call". Body: "A free, no-obligation call with a Wedded Wonderland advisor to talk through your honeymoon and point you toward the right next step." Button:
   "Book a free call" linking to /wonderland-concierge.
   If the shared block body differs from the exact body above in any word,
   override the body on this post with the exact body above. Do not edit the
   shared block itself.
6. **Images:** from the media library, insert these files where their marker is.
   Set alt text and caption exactly as given. Set
   honeymoon-itinerary-couple-terrace-printed-plan-01.webp as the featured image.
   All file names are placeholders until the real files are uploaded; if a file
   is missing, leave the marker in place and list it. Never substitute an image
   from a third party site.

   | Slot | File | Alt text | Caption |
   |---|---|---|---|
   | hero (featured) | honeymoon-itinerary-couple-terrace-printed-plan-01.webp | A couple sit at a small terrace table with a printed honeymoon itinerary and two coffees in late afternoon light | Plan the shape first, then the places. |
   | template | honeymoon-itinerary-template-printed-page-passports-01.webp | A printed honeymoon itinerary template with a blank day-by-day table, a pen and two closed passports on a table | One page per base, filled in together. |
   | two-week-sample | honeymoon-rest-day-couple-pool-lounger-01.webp | A couple read on loungers beside a quiet pool on a slow honeymoon morning | A rest day is part of the plan. |
   | travel-day | honeymoon-travel-day-transfer-carry-on-bags-01.webp | Two carry-on bags are loaded into a private transfer as a honeymoon couple prepare to change bases | Give the move between bases a day of its own. |
   | documents | honeymoon-travel-documents-folder-passport-01.webp | A folder of printed travel bookings beside a closed passport on a desk under lamp light | Documents, health and timing, sorted early. |

7. **Categories:** tick Travel Guides (untick Uncategorised or any other
   category and list what you removed). Then set **Travel Guides** as the
   primary category using the "Make primary" control (Yoast or RankMath).
   Ticking order does not set the primary.
8. **Tags:** honeymoon, itinerary template, travel planning, after the wedding, travel documents
9. **Excerpt:** Plan the shape of your honeymoon before the places: a printable day-by-day honeymoon itinerary template, a two week sample built around rest days, two bases and one travel day, the work behind each transfer, and the official passport, visa, insurance and health checks for Australians, linked at the source.
10. **SEO fields:** SEO title "Honeymoon Itinerary Template and Two Week Sample Plan". Meta description "A printable honeymoon itinerary template and a two week sample plan, with the passport, visa, insurance and health checks Australians need before flying."
11. **Author:** [[NEEDS: named author]] (leave the default author if none is given, and list it)
12. **Save as draft. Do not publish.** Never click Publish or Schedule, and never click Update on a live post.

Then open the draft preview and check: every image loaded and has alt text; all
22 links work, including the official passports.gov.au and smartraveller.gov.au
links; the template renders as a real table with 8 columns and 14 day rows,
with the four-line header block above it, and scrolls or stacks cleanly on
mobile; the checklist renders as a list; the Key Takeaways and CTA blocks are
present and the discovery_call body matches step 5; the breadcrumb shows Travel
Guides; the permalink is /travel-guides/honeymoon-itinerary; the SEO fields are
filled. Check the rendered title tag: it must read "Honeymoon Itinerary Template
and Two Week Sample Plan" with no dash and no site-name suffix after a
separator. If the SEO plugin adds one, list it; do not change site-wide
settings. If you updated an existing post, confirm the live version is
unchanged. Take a desktop and a mobile screenshot. List anything that did not
work, and say whether you created a new draft post or saved a draft of an
existing one.

---

## Article body

# Honeymoon Itinerary Template and Two Week Sample

[IMAGE: honeymoon-itinerary-couple-terrace-printed-plan-01.webp]

A honeymoon itinerary is the one document that lets you stop planning. Two weeks away after months of wedding decisions sounds simple, until you are deciding on day three whether to change hotels or stay put. So settle the shape of the trip first: where you arrive and rest, where you move, and where you leave room to do nothing at all. The places follow easily after that.

Below is a printable template to fill in together, a two week sample built by purpose rather than by hotel, the work behind each travel day, and the passport, visa, insurance and health checks Australians need before flying. If you are leaving straight from a destination wedding, there is a section for that too. Sources current as at November 2026.

## How to use this honeymoon itinerary template

Decide how many bases you want, which days are for travel and which are for rest, then match destinations and stays to that frame. Work through it in three passes.

1. **Shape.** Count the nights. Mark the arrival day, any travel day between bases and the last full day before you fly home.
2. **Bookings.** Fill in stays first, then flights and transfers, then private experiences, then restaurants, the order on our [seven-day trip planner](/travel-guides/weekly-itinerary-template).
3. **Details.** Add confirmation numbers, meeting points and each driver's contact in the notes column, so neither of you has to search an inbox at the kerb.

If your trip is a single week in one place, the seven-day planner may be all you need.

## The honeymoon itinerary template

Print one page per base, or keep it as a shared document you can both open on your phones, with an offline copy saved before departure and each property's address in the local language where useful. If someone else is planning with you, [brief your advisor with this template](/travel-guides/how-to-brief-a-travel-advisor).

[IMAGE: honeymoon-itinerary-template-printed-page-passports-01.webp]

**Passports:** names as printed and expiry dates

**Insurance policy and emergency line:**

**Emergency contacts:**

**Your advisor's number:**

| Day and date | Base | Morning | Afternoon | Evening | Transfer and timing | Booked (yes/no) | Notes |
|---|---|---|---|---|---|---|---|
| Day 1 | | | | | | | |
| Day 2 | | | | | | | |
| Day 3 | | | | | | | |
| Day 4 | | | | | | | |
| Day 5 | | | | | | | |
| Day 6 | | | | | | | |
| Day 7 | | | | | | | |
| Day 8 | | | | | | | |
| Day 9 | | | | | | | |
| Day 10 | | | | | | | |
| Day 11 | | | | | | | |
| Day 12 | | | | | | | |
| Day 13 | | | | | | | |
| Day 14 | | | | | | | |

**How to fill it in**

- **Base:** where you sleep that night, with the address.
- **Morning, afternoon, evening:** one core experience a day is often enough, and we would not plan more than two.
- **Transfer and timing:** any flight, transfer or drive that day, the pick-up time and who is meeting you.
- **Booked:** write yes only once you hold a written confirmation.
- **Notes:** confirmation numbers, meeting points and the driver's contact.

**Before you go**

- [ ] Both passports valid for at least six months beyond the end of the trip
- [ ] Every booking in the names on your passports
- [ ] Visas or entry approvals for every country you visit or transit through
- [ ] Travel insurance covering every country and stopover, with the policy read
- [ ] A doctor's appointment at least eight weeks before you fly
- [ ] Enough medicine for the whole trip, with copies of prescriptions and a doctor's letter
- [ ] Copies of passports, visas and key documents, with one set left with someone you trust
- [ ] Hard copies of flight, accommodation and experience bookings
- [ ] This itinerary shared with family or a friend
- [ ] Subscribed to Smartraveller email updates and alerts
- [ ] An offline copy of this template on both phones

## A two week sample honeymoon itinerary

This is a structure, not a booking. It assumes a long-haul flight from Australia, two bases and one travel day between them. Swap in your own places and keep the rhythm.

[IMAGE: honeymoon-rest-day-couple-pool-lounger-01.webp]

**Days 1 and 2: arrive and rest.** Keep the first day light: check in, eat well, sleep. On long-haul trips we keep the first two days gentle and schedule more demanding activities from the third day onwards. That is our planning approach to jet lag, not medical advice.

**Days 3 to 6: settle into the first base.** For a honeymoon we favour slower mornings, longer evenings and time to enjoy the property itself, rather than treating every day as a chance to explore. Build in a rest day or half-day around the middle, so Day 5 might hold nothing but the pool and a long dinner.

**Day 7: the travel day.** Whenever the base changes, we recommend a dedicated transfer day, and we keep it flexible. Check out without hurrying, travel, arrive in daylight if you can, and book nothing that evening beyond dinner where you are sleeping. If the route includes a stopover, check the passport rule under Documents below.

[IMAGE: honeymoon-travel-day-transfer-carry-on-bags-01.webp]

**Days 8 to 12: the second base.** Choose a contrast to the first: if the first week was water and quiet, the second might be streets to walk, markets and tables to book. Plan another half-day of rest. If a boat day, a dive or a safari drive is on the list, check your insurance covers it.

**Days 13 and 14: a slow finish.** Leave the last full day loosely planned and the final morning open before the flight home. Pack the night before, so the last breakfast is a breakfast and not a checklist.

What fills each block depends on where you go, so browse our [destination pages](/destinations) for ideas.

## Travel days, transfers and the work you do not see

A calm honeymoon rests on work settled before anyone packs.

**Transfers.** Book every airport and inter-base transfer in both your names with a set pick-up point, and write that point and the driver's contact in the notes column.

**Connections.** Leave a generous buffer around any connecting flight, and keep the travel day free of anything that cannot move if a flight runs late.

**A second plan for each day.** Give every planned experience a wet-weather or rest alternative, written beside it, so a change in the forecast becomes a choice rather than a scramble.

**The last day.** If your flight leaves late in the day, ask the property in writing whether it can hold your luggage after check-out, and plan where you will spend the hours in between.

**Who to call.** Agree before you leave who you contact if a flight changes, and write the number in the template header. When we plan the honeymoon through our [wedding and honeymoon travel](/travel) service, it is one connected trip rather than a stack of separate bookings, we stay reachable while you are away, and you message one point of contact, not a call centre queue. To see what that involves, read [what a honeymoon planning service covers](/honeymoon-ideas/honeymoon-planning-service).

## Adapting it to your trip

**Straight after a destination wedding.** If you fly out the morning after a wedding week, make Day 1 a rest day and move the first real experience to Day 3 or later. Send wedding outfits and extra luggage home with family where you can, and agree a handover with your wedding team so the final details are theirs to close. If you married in Italy, Greece or Bali, start there. Then think about names: after a change of family name through marriage, you can get a new passport or keep your current one, and the Australian Passport Office recommends [booking travel in the name that is in your passport](https://www.passports.gov.au/change-name-or-gender).

**How long to go.** As a starting point, we suggest: seven days, one base with rest first and a slow finish; ten days, two bases with one travel day; three weeks, a third base only if each base gets four nights or more. Set the nights with our guide to [how long a honeymoon should be, by destination](/expert-advice/how-long-is-a-honeymoon-a-guide-by-destination) and the months with [when to go on honeymoon](/expert-advice/a-guide-on-when-to-go-on-honeymoon).

A free Discovery Call with a Wedded Wonderland advisor is [a quick way to test your two bases](/wonderland-concierge) before anything is booked.

## Documents, health and timing before you go

Start early: Smartraveller says to [allow at least six weeks to get a passport](https://www.smartraveller.gov.au/our-role/passport-services) and to get a basic health check at least 8 weeks before you go. Confirm the passport, visa and entry requirements for your own passports with the authority that decides: the Australian Passport Office or Smartraveller (DFAT) for your Australian passport, and each destination's embassy or consulate for visas and entry.

[IMAGE: honeymoon-travel-documents-folder-passport-01.webp]

**Passports.** Smartraveller's essentials checklist says your passport should be valid for at least six months beyond the end of your trip. Smartraveller adds that some countries and airlines apply a six-month rule even when you are only transiting. Where possible, do not book flights without a valid passport, and Australian dual nationals should depart and enter Australia on their Australian passport.

**Visas.** Get the right visa for every country you visit or transit through, and check with each destination's embassy or consulate before every trip, because rules can change at short notice and [Smartraveller cannot tell you which visa to get](https://www.smartraveller.gov.au/travel-essentials/getting-foreign-visa). Some countries hold your passport during processing, so apply early.

**Insurance.** Smartraveller says [the right travel insurance is as essential as a passport](https://www.smartraveller.gov.au/travel-essentials/travel-insurance). Choose a policy that covers every country, including stopovers and transit points, and check whether cancellation is covered if the advice level rises after you book. Read the Product Disclosure Statement, check the excluded activities (insurers exclude many, even cruises) and declare all pre-existing health conditions. Medical assistance is usually the highest unexpected cost for Australians overseas, and the Australian Government cannot pay travellers' bills.

**Doctor's visit.** Smartraveller's essentials checklist says to [get a basic health check at least 8 weeks before you go](https://www.smartraveller.gov.au/travel-essentials/essentials-checklist), and its travel health page says to [see your doctor 6 to 8 weeks before you go](https://www.smartraveller.gov.au/travel-essentials/travel-health), so booking at least eight weeks out satisfies both.

**Medicines.** Smartraveller says to check your medication is legal and available where you are going, take enough for the whole trip, and carry copies of your prescription and a letter from your doctor.

**Updates.** Smartraveller no longer asks you to register your trip. Instead, [subscribe to Smartraveller's email updates and alerts](https://www.smartraveller.gov.au/our-role/smartraveller-subscription) as soon as you start thinking about heading overseas.

## Honeymoon itineraries by destination

We are adding day-by-day honeymoon itineraries for individual destinations to this page as they are published. Until then, these guides help you choose your two bases:

- The [best honeymoon destinations in Asia](/expert-advice/best-asia-honeymoon-destinations-where-to-go-and-when-to-visit), with when to visit
- [Private safari and island honeymoons in Africa](/expert-advice/african-honeymoons-private-safari-and-island-escapes-by-season), by season

## When to hand it to a planner

Hand it over when the template stops being enjoyable: two or more bases, flights that depend on each other, or a wedding still to run in the weeks before. That is the point where one missed transfer can unpick three bookings.

Our [honeymoon packages page](/destination-honeymoon-packages) says every package is fully curated, covering transfers, private dining, spa rituals and sunset experiences, all coordinated by one team.

If Wedded Wonderland Concierge is already advising on your destination wedding, honeymoon travel is part of the same Destination Wedding and Celebration Concierge service, with one dedicated point of contact and wedding and travel under one roof.

If you are still deciding who should plan it, read [what a honeymoon planner does](/honeymoon-ideas/honeymoon-planner), [what a planner's fee covers](/honeymoon-ideas/honeymoon-planner-cost) and [whether a planner or travel agent suits you](/honeymoon-ideas/honeymoon-planner-vs-travel-agent).

## Frequently asked questions

### How many places should we visit on a two week honeymoon?

Two bases is a comfortable rhythm for two weeks. Our sample uses two, with a dedicated transfer day whenever the base changes, so packing, checking out and travelling get a day of their own rather than crowding a holiday day.

### How many days should a honeymoon itinerary be?

As a starting point, we suggest seven days with one base, rest first and a slow finish; ten days with two bases and one travel day; or three weeks, adding a third base only if each base gets four nights or more. Destination and season shape the rest.

### Should we plan every day of the honeymoon?

Plan the shape, then leave space. We keep to one core experience a day, two at most, build in a rest day or half-day around the middle and leave the final morning open. Write every booking into the template so the unplanned hours can be exactly that.

### When should we start planning the honeymoon itinerary?

Our [package lead times](/destination-packages) put the ideal lead time for a honeymoon at six to nine months, to lock in the right suite category. Our seven-day trip planner suggests booking stays first, then flights and transfers, then private experiences and restaurants, and notes that these are indicative windows that vary by destination, season and experience.

### Can someone plan and book the whole itinerary for us?

We plan the honeymoon as one connected trip: you share your travel window and the kind of trip you picture, choose from a tailored shortlist, and we coordinate transfers, dining, spa and private experiences so every reservation is in place when you arrive. Visa and entry rules stay yours to confirm with each embassy or consulate.

[CTA: discovery_call]
