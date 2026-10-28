# Decisions: Portugal run

Project Lead decisions, with reasons. The user can overturn any of them.

## D1. Follow the Portuguese registry (IRN) over the Australian Embassy page
Where IRN and the Australian Embassy Lisbon page differ (6 months vs 3 months to marry
after approval; translation rules), the copy follows IRN, the Portuguese authority
that runs civil marriage. Government source of the country where the marriage happens
outranks a foreign embassy summary. The difference is listed in NOTES.md for the T20
legal page owner.

## D2. Live page: hold changes that depend on unsigned facts, do not add noindex
The repo rule is "noindex until every fact needing sign-off is confirmed". That rule is
for new pages. This page is live and indexed. Adding noindex to a live page to publish
unconfirmed facts would be the wrong trade. Instead:
- Copy that depends on a fact needing sign-off (the EUR 120 registry fee, third-party
  cost ranges, the US notarial fee, the Blue Flag line, the founder quote, the B8 proof
  strip numbers) is marked **"Apply only after sign-off"** in CMS-HANDOFF.md, with a
  fallback line to use until then.
- Everything else can go live as soon as it is applied.
- The automated `noindex_while_unconfirmed` check on the preview is accepted as a known
  failure for this reason.

## D3. Australian CNI: hedge, do not state
No official source says whether Portugal accepts a CNI issued in Australia (F041). The copy
says the Australian Embassy in Lisbon can issue a CNI (F038) and tells couples to confirm
with the Registo Civil or the Embassy of Portugal in Canberra which document they need.
No claim that an Australian-issued CNI is accepted.

## D4. Official fees are not WW prices
The EUR 120 civil registry fee is a government fee, not a Wedded Wonderland price, so the
"From AUD" rule does not apply to it. It still waits for Nic's sign-off (per config) before
it is shown, under D2.

## D5. Primary persona for this page
The CRM has no Australian Portugal enquiries and only 2 to 3 real Portugal enquiries
(US, Canada). US and UK hold about 97% of search demand. Primary persona:
`intl-couple-europe-full-service`. Secondary: `au-couple-marrying-abroad` (home market),
`intimate-destination-elopement`. Always: `discerning-skeptic`.

## D6. Other branches are not used
Per the user, the France and Greece pages and the content system on other branches are
not approved and are not referenced in this run.

## D7. Title
Approved: "Wedding in Portugal | Venues by Region | Wedded Wonderland" (58 characters). The full
brand name fits, so the "| WW" version in the doc is not needed.

## D8. Cost sources
Name only Rita Plácido Photography (a photographer, not a competing planner), unlinked,
with the year. Kay Northrup Events is a wedding planner that ranks for our terms, so it is
not named (no competitor branding). All cost lines still wait for Nic's sign-off (D2).
This overrides the doc's open question 6; the user can reverse it.

## D9. FAQ 5
Replace "Is a wedding in Portugal cheaper than at home?" (no sourced comparison) with the UK
People Also Ask question "When can you get married in Portugal?", answered from F021 to F023
and the season facts.

## D10. Section 10: no fee, currency or on-the-day claims
No approved wording exists in this branch for how Wedded Concierge fees work, the currency,
or what happens if something goes wrong on the day. Section 10 describes the steps and the
one Wedded Advisor only. The question goes to the user in SUMMARY.md.

## D11. Persona panel for this page
Panel: intl-couple-europe-full-service (primary), au-couple-marrying-abroad,
intimate-destination-elopement, discerning-skeptic. 3 runs each. The cultural and
aspirational personas are left out: no Portugal CRM signal for either, and the run cost
should stay in proportion to a P3 fix.

## D12. Persona panel on the brief: what copy can fix and what it cannot
12 runs: 11 save for later, 1 leave (skeptic), 0 enquire. Recurring gaps, sorted:

Copy can fix (sent to the copywriter as a brief addendum, 23-brief-addendum.md):
- Small groups look unwelcome: add a sourced small-wedding FAQ (witnesses optional, registry
  route) and an explicit invitation for elopements and small weddings in the region chooser
  and form intro. No small-wedding price (no source).
- "Who handles the paperwork": reuse the live page's own claim that the Wedded Advisor walks the
  couple through the route for their nationality. No new capability claims.
- The venue charges box reads as a warning: reframe as "what your Wedded Advisor checks in every
  venue contract", same facts.
- Travel time: add drive times only where a fact exists; otherwise airport codes only.
- H1 promises a Sintra palace while the strip warns of state-event cancellations: keep the H1
  (user's plan), but the palace strip leads with how to book, then the conditions.

Copy cannot fix (business answers needed, go to the user in SUMMARY.md):
- Proof: B8 numbers need sign-off (F019); only 2 Portugal real weddings exist (B6 needs 3).
- How Wedded Concierge charges, in what currency, and what is included (D10).
- A named Wedded Advisor or senior planner for Portugal.
- What happens on the day if something goes wrong.
- Any "From AUD" Portugal price (none exists; 0 packages).
- Why an Australian-based firm for a Portugal wedding (an approved positioning line).

Known tool limit: the aggregator matches objections by text, so the same concern worded
differently across runs (for example "no Portugal proof") can fall below the 2-run filter. The
Project Lead read all 12 reviews and included those concerns above.

## D13. UX consult calls
Approved: hero order and Wedded Concierge sentence in the hero, sticky bar copy without a
price, text links to the form from the Costs and Legal tabs, UX13 form copy with Season plus
Year, and the hidden field list. Kept as the user's plan states (UX suggestions go to the
user): the B9 button "Check your date" and the FAQ heading "Get Answers Before You Enquire".
FAQ 5 and the fee line fixed through the addendum, not a second brief round, to save a cycle.

## D14. Copy round 1 calls
- Headings use the title case in the user's section plan (it is page-specific and the user's
  own). studio/standards/brand-voice.md says sentence case; that standard was drafted by
  Claude, so the user's plan wins. Flag to the user to settle the standard.
- Word count: cut to the brief range in revision 2 (remove the When to go table and the
  Timeline tab duplicates, about 160 words, plus any other repetition the reviews find).
- Hidden field `entry_point=celebrations` approved for the celebrations section links.
- Official external source links in the legal tab are allowed (linking.md permits official
  sources).
- Hero and closing buttons go to the on-page form; /wonderland-concierge is linked in s10.

## D15. Revision 2 calls on the copy reviews
- F088 brand sentence: confirmed only in the live page's own wording ("pairs you with a Wedded
  Advisor who plans with you from the first enquiry to the last dance"). No markets, numbers or
  extra capabilities. Use it once in the hero and once in s10, nowhere else.
- On-the-day coordinator (FC3-10) and Wonderland Studio "Start for free" (FC3-13): kept, because
  the user's own plan lists them (doc section 4 rows 6 and 7). Written as "can include", no guarantee.
- Wedded Privileges (FC3-11): drop "Portugal properties are still being confirmed". Name the
  programme and say the Wedded Advisor explains what applies. No benefits listed.
- Consent line (FC3-12): neutral "By sending this form you agree to our Privacy Policy", with the
  Privacy Policy URL marked for dev to confirm.
- SEO-01: H2s stay as the user's plan sets them. "Portugal wedding venues" goes in og_title, the
  first sentence (already), the s2 intro and the s4 intro, and one region card line. The question
  of allowing it in an H2 goes to the user.
- Passport order (persona finding): US, UK, then AU in the passport tabs and FAQ answers, because US
  and UK hold about 97% of demand (D5). AU stays complete.
