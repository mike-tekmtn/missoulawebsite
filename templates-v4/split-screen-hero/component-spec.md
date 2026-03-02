# Split-Screen Hero — Component Spec

This spec pairs with `RULES.md` and defines implementation contracts for coding agents.

## 1) Component contract

## `SplitScreenHero` props

```ts
export type SplitScreenHeroProps = {
  eyebrow?: string;
  headline: string;                 // required, 28-72 chars preferred
  supportText: string;              // required, 60-220 chars preferred

  primaryCta: {
    label: string;                  // action-oriented, 2-5 words
    href: string;                   // absolute or relative URL
  };

  secondaryCta?: {
    label: string;
    href: string;
  };

  trustItems?: string[];            // e.g. ["Licensed & Insured", "4.9★ Google", "Serving Missoula"]

  media: {
    src: string;                    // hero image URL/path
    alt: string;                    // required meaningful alt
    focalPoint?: "left" | "center" | "right";
    overlayOpacity?: number;        // 0.25 - 0.65
  };

  layout?: {
    reverseOnDesktop?: boolean;     // default false
    minHeroHeightPx?: number;       // 560-840
  };

  theme?: {
    bgClass?: string;
    textClass?: string;
    accentClass?: string;
    buttonClass?: string;
  };
};
```

## 2) Validation rules

- `headline`, `supportText`, `primaryCta.label`, `primaryCta.href`, `media.src`, `media.alt` are required.
- `overlayOpacity` defaults to `0.45`; clamp to `0.25..0.65`.
- `trustItems` max 5 items.
- `headline` hard max 96 chars.
- `supportText` hard max 260 chars.
- Reject javascript URLs in CTAs.

## 3) Rendering requirements

- Desktop: two-column split (`text` + `media`) with equal visual weight.
- Mobile: stack `text` first, `media` second.
- Primary CTA visible without scrolling on standard laptop viewport (1366x768).
- Trust strip appears directly below CTA cluster.
- Media panel uses overlay for readability.

## 4) Accessibility requirements

- One `h1` only.
- CTA controls keyboard-focus visible (2px+ focus ring).
- Color contrast:
  - body text ≥ 4.5:1
  - large heading/CTA text ≥ 3:1
  - non-text UI indicators ≥ 3:1
- `alt` text required and non-empty.

## 5) Performance requirements

- Hero image should be optimized (WebP/AVIF preferred).
- Target image weight <= 300KB for common desktop breakpoints.
- LCP target <= 2.5s on broadband baseline.
- Avoid blocking scripts in hero region.

## 6) Behavior checklist (agent QA)

- [ ] Required props validate
- [ ] No layout break at 320px width
- [ ] CTA labels are action-oriented and specific
- [ ] Trust items are factual and verifiable
- [ ] Hero text does not overlap media in any breakpoint
- [ ] Focus order follows visual order
- [ ] Contrast checks pass
- [ ] Lighthouse Performance >= 85, Accessibility >= 90 (page-level target)

## 7) Example payload (valid)

```json
{
  "eyebrow": "Missoula Local Service",
  "headline": "Fast, Professional Service From a Team You Can Trust",
  "supportText": "Book with confidence. Clear pricing, quick response times, and reliable local support.",
  "primaryCta": { "label": "Request Estimate", "href": "/contact" },
  "secondaryCta": { "label": "View Services", "href": "/services" },
  "trustItems": ["Licensed & Insured", "4.9★ Google Rating", "Serving Missoula + Nearby"],
  "media": {
    "src": "/images/hero-mountains.webp",
    "alt": "Technician helping homeowner in front of mountain backdrop",
    "focalPoint": "center",
    "overlayOpacity": 0.45
  },
  "layout": { "reverseOnDesktop": false, "minHeroHeightPx": 680 }
}
```

## 8) Example payload (invalid)

```json
{
  "headline": "Hi",
  "primaryCta": { "label": "Click", "href": "javascript:alert(1)" },
  "media": { "src": "", "alt": "" }
}
```

Invalid because required fields missing/unsafe URL/empty media values.
