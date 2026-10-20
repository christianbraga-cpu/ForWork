# Image checklist

## Must pass (any fail = image rejected)
- [ ] **Location proven** by register, EXIF GPS, photographer gallery or source page. Not by appearance.
- [ ] **Event proven** if captioned as a real wedding
- [ ] **Season/time matches** the paragraph
- [ ] **Licence covers web/blog use**, and credit noted if required
- [ ] **Consent** for identifiable people; no identifiable children without consent
- [ ] **Not from `reference-only/`**, a competitor, or an unlicensed search result
- [ ] **Not AI-generated** if it depicts a real venue, destination or wedding

## Scored 1 to 5
- Brand fit (light, editorial, uncluttered, consistent grading)
- Story value (shows what the paragraph says)
- Uniqueness (Google Lens via Apify: not widely reused)

## Web preparation
- Descriptive filename: `<keyword>-<venue>-<subject>.webp`
- Hero ≤ 250 KB, inline ≤ 150 KB, longest side 2000 px (hero) / 1400 px (inline)
- Personal EXIF stripped (GPS, serial); copyright kept
- Alt text: what's in the photo, plain language, keyword only if natural, ≤ 125 characters
- Caption: "<Place>, <town>. Photo: <credit>"

## No suitable image
Leave the slot with `file` = planned filename, `status: "needed"`, and a shot brief. Flag `[[IMAGE NEEDED]]` in the run report.
