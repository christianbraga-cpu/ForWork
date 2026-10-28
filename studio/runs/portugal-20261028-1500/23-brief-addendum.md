# Brief addendum (Project Lead, after the persona panel on the brief)

Applies on top of 20-content-brief.json. Source: 22-persona-brief-summary.json and D12.

1. **Small weddings welcome.**
   - Region chooser intro: one line inviting elopements and small weddings as well as
     three-day weekends. No guest numbers, no price.
   - Form intro (section 10): the same invitation in a few words.
   - Add an FAQ "Can you have a small wedding or elopement in Portugal?" answered only
     from facts: witnesses optional (F028), the registry route and fee (F024, apply after
     sign-off, fallback without the figure), the 1 month lead time (F021), symbolic option.
     It replaces the weakest of the 10 FAQs (say which in `change_reason`) so the FAQ stays at 10.

2. **Paperwork.** Where the copy says who helps with the legal route, use the live page's
   own claim: the Wedded Advisor walks the couple through the exact route for their
   nationality. Do not claim Wedded Concierge files documents or attends the registry.

3. **Venue charges box.** Reframe the heading and lead-in as what the Wedded Advisor checks
   in every venue contract (rooms and exclusivity, buy-out vs venue fee, per-day or per-guest
   minimums, whether quotes include VAT). Same facts, calmer framing.

4. **Travel time.** Add a drive time only where a fact id exists. Otherwise keep the
   airport code. Never invent a transfer time.

5. **Palace strip order.** First how palaces are booked (through Parques de Sintra), then
   what you can have, then the conditions (state events, nothing fixed to the heritage,
   Monserrate works to Q1 2027).

6. **Do not paper over business gaps.** Do not invent a fee model, a named advisor, an
   on-the-day guarantee, a From price or a positioning line. Where a section needs one, write
   the copy without it and list it in `open_questions` to the user.

## From the UX consult (21-ux-consult.json)

7. **Hero order.** H1, the 3-line quick answer, then the two buttons straight away, then the
   passport link and celebrations line. The hero must also carry one sentence naming
   Wedded Concierge and one Wedded Advisor (no fee or currency claim). Repeat a short Wedded
   Advisor line in the region chooser intro.
8. **FAQ 5** is "When can you get married in Portugal?" (D9), not the "cheaper" question.
   The FAQ heading stays as the user's plan has it ("Get Answers Before You Enquire"); UX's
   rename suggestion goes to the user.
9. **No fee line.** Remove "a Wedded Advisor explains fees in your currency on the first
   call" (D10). Say only that the Wedded Advisor talks the couple through their options.
10. **B9 button** stays "Check your date", exactly as the user's plan lists it. The bar
    pre-fills the B3 form and scrolls to it. UX's "Start your enquiry" suggestion goes to the user.
11. **Sticky mobile bar:** "Wedding in Portugal" plus a button "Speak with a Wedded Advisor"
    (an exact label from the plan). No price.
12. **Routes to the form:** one text link to the form at the end of the Costs tab and the
    Marrying legally tab, and a closing CTA after the FAQ, using the plan's exact labels.
13. **Form copy:** use UX13's field labels, guest bands (the same as B9), Season plus optional
    Year in place of a date field, region options matching the card titles exactly, ceremony
    type options from the plan, a budget prompt in the message placeholder, error messages,
    a consent line, and a success message with no reply-time promise. Hidden fields (approved):
    route_to, destination, page_slug, offer, entry_point and the five UTM fields.
14. **B8 proof strip:** use the non-numeric fallback line rather than hiding the strip, until
    F019 is signed off. **Section 8:** hidden; show the Europe real weddings strip in its place
    only if the CMS has one (mark it as a CMS question).
15. **Copy limits:** follow `payload.scores.copy_limits` in 21-ux-consult.json.
