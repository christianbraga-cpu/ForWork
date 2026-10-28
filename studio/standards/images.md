# Image standard

Owners: Visual Lead (selection, rights), Copywriter (alt text and captions),
Technical SEO (delivery), UX (layout).

## Rights (blockers if missing)

- Every published image has a rights entry: register id, photographer or source,
  licence scope (web, social, paid, print), expiry, credit wording, couple consent.
- Never reuse competitor or marketplace images.
- Venue media kits only with written permission.
- Never present an AI-generated image as a real wedding or a real venue. Concept or
  mood imagery must be labelled as such.
- Remove EXIF GPS data before upload. Keep copyright and credit metadata.

## Selection

- Real weddings and the venue's own photography, never stock.
- Sequence tells a story: setting, ceremony, details, guests, celebration, stay.
- Each image earns its place by reassuring a persona (guest experience, scale,
  logistics, calm).
- Show the diversity of couples and cultures we actually serve.

## Files

- File names describe the picture, in kebab-case:
  `cappuccina-villa-terrace-ceremony-san-gimignano.jpg`, never `IMG_4821.jpg`.
- Formats: AVIF with WebP fallback; JPEG as a last resort.
- Responsive widths: 480, 768, 1200, 1600, 2400.
- Always set `width` and `height`.
- Sizes: see `performance-budget.json`.

## Words

- **Alt text** describes what is in the image, for screen readers first: "Couple
  exchanging vows on a terrace facing San Gimignano's towers at sunset". 125
  characters or fewer. No keyword stuffing. Decorative images: `alt=""`.
- **Captions** add place, scale or proof: "Villa terraces, up to 200 guests. Photo: [credit]".
- **Credit** on every image where the licence requires it (and ideally on all).

## Delivery

- Hero: preloaded, `fetchpriority="high"`, never lazy-loaded.
- Below the fold: `loading="lazy"`.
- Until real images are supplied, use the reference page's placeholder slots
  (`<div class="ph" data-img="file-name.jpg">`) and list each one in NOTES.md
  "Images to supply".
- Open Graph image chosen deliberately (1200x630).
- Pinterest-friendly 2:3 crop for 2 to 3 key images.
- `ImageObject` schema with creator, credit and licence once images are final.
