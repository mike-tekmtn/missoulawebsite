# Asymmetric Bento Component Spec (for Coding Agents)

## 1) Component Contract

**Component name:** `AsymmetricBentoLocalServiceHero`

**Goal:** Render a conversion-focused, above-the-fold asymmetric bento section for local service businesses.

**Non-goal:** Recreating a split-screen hero (50/50 text-image layout).

---

## 2) Props / Data Schema

```ts
interface AsymmetricBentoProps {
  brand: {
    name: string;                 // required, 2..60 chars
    logoText?: string;            // optional fallback if no logo asset
    phone?: string;               // E.164 preferred, e.g. +14065551234
    phoneDisplay?: string;        // e.g. (406) 555-1234
  };

  nav?: Array<{
    label: string;                // required, 1..24 chars
    href: string;                 // required, absolute/relative URL
  }>;

  primaryCard: {
    eyebrow?: string;             // e.g. "Missoula Plumbing"
    headline: string;             // required, 8..110 chars
    subhead: string;              // required, 20..180 chars
    primaryCta: {
      label: string;              // required, 2..32 chars
      href: string;               // required
      ariaLabel?: string;
    };
    secondaryCta?: {
      label: string;
      href: string;
      ariaLabel?: string;
    };
    trustChips: string[];         // required, length 2..5, each 2..28 chars
    heroImage?: {
      src: string;
      alt: string;                // required if informative image
    };
  };

  proofCard: {
    ratingValue: number;          // required, 0..5, step 0.1
    ratingCount: number;          // required, >= 1
    quote: string;                // required, 8..140 chars
    attribution?: string;         // e.g. "— Sarah K., Franklin to the Fort"
  };

  availabilityCard: {
    title: string;                // required, 2..48 chars
    detail: string;               // required, 8..120 chars
    badge?: string;               // optional, e.g. "Open Today"
  };

  serviceAreaCard: {
    title: string;                // required
    areas: string[];              // required, 1..8 items
    radiusMiles?: number;         // optional, 1..120
  };

  guaranteeCard: {
    title: string;                // required
    bullets: string[];            // required, 2..4 items
  };

  theme?: {
    mode?: "dark" | "light";     // default "dark"
    accentHex?: string;           // default #38bdf8
    canvasHex?: string;           // optional
  };

  seo?: {
    title?: string;
    description?: string;
  };
}
```

---

## 3) Validation Rules

### 3.1 Required Groups
- `brand.name`, `primaryCard`, `proofCard`, `availabilityCard`, `serviceAreaCard`, `guaranteeCard` are required.

### 3.2 Content Constraints
- `primaryCard.headline` SHOULD be <= 16 words.
- `primaryCard.trustChips.length` MUST be between 2 and 5.
- `proofCard.ratingValue` MUST be between `0` and `5`.
- `proofCard.ratingCount` MUST be integer >= 1.
- `serviceAreaCard.areas` MUST contain at least one locality string.
- `guaranteeCard.bullets` MUST have 2-4 concise bullets.

### 3.3 CTA Constraints
- `primaryCard.primaryCta` is mandatory.
- Secondary CTA (if present) must be visually lower emphasis.
- CTA labels must avoid vague generic copy like “Submit”.

### 3.4 Accessibility Constraints
- Exactly one `<h1>`.
- Buttons/links have visible focus outline.
- Color contrast compliance:
  - normal text >= 4.5:1
  - large text >= 3:1
- If `heroImage.src` present and informative, `heroImage.alt` must be non-empty.

### 3.5 Anti-Pattern Guards
Reject render config if:
- Layout mode requests `split`, `half`, `50-50`, or equivalent.
- More than 2 primary-style CTAs are supplied.
- Required trust signals are absent above fold.

---

## 4) Rendering Rules (Deterministic)

1. Render top nav with brand left and links/phone right.
2. Render bento grid with 12-col desktop, 6-col tablet, 1-col mobile.
3. Place cards in this order:
   - `primaryCard` (dominant)
   - `proofCard`
   - `availabilityCard`
   - `serviceAreaCard`
   - `guaranteeCard`
4. On mobile, stack in same order.
5. Preserve strong visual emphasis for primary CTA in first card.

---

## 5) Acceptance Tests

### Test A — Structural Integrity
- [ ] DOM contains exactly one `<h1>`.
- [ ] Contains 5 required cards.
- [ ] Primary card spans more grid area than any other card at desktop width.

### Test B — Conversion Priority
- [ ] Primary CTA visible in initial viewport at 390x844.
- [ ] At least 3 trust indicators visible above fold.
- [ ] Social proof card includes rating + count + quote.

### Test C — Accessibility
- [ ] Keyboard tab order follows visual order.
- [ ] All interactive elements have `:focus-visible` styles.
- [ ] Contrast ratios pass in both light and dark theme modes.

### Test D — Responsiveness
- [ ] No horizontal scroll at 320px width.
- [ ] Card content does not overflow clipping bounds.
- [ ] Buttons maintain minimum touch target ~44px height.

### Test E — Distinctness from Split-Screen
- [ ] No 2-column 50/50 hero lockup spanning full viewport height.
- [ ] Visual hierarchy driven by card spans and mosaic, not side-by-side paneling.

---

## 6) Example Payloads

### 6.1 Minimal Valid Payload
```json
{
  "brand": { "name": "Summit Home Services" },
  "primaryCard": {
    "headline": "Trusted Same-Day Home Service Across Missoula",
    "subhead": "Licensed pros, clear estimates, and clean job sites—book in minutes.",
    "primaryCta": { "label": "Get My Free Estimate", "href": "/estimate" },
    "trustChips": ["Licensed & Insured", "4.9★ Rated", "Locally Owned"]
  },
  "proofCard": {
    "ratingValue": 4.9,
    "ratingCount": 247,
    "quote": "Fast, respectful, and zero surprise charges."
  },
  "availabilityCard": {
    "title": "Today’s Availability",
    "detail": "2 same-day windows open in Missoula."
  },
  "serviceAreaCard": {
    "title": "Service Area",
    "areas": ["Missoula", "Lolo", "Bonner"],
    "radiusMiles": 35
  },
  "guaranteeCard": {
    "title": "Our Promise",
    "bullets": ["Workmanship warranty", "Upfront pricing", "Background-checked techs"]
  }
}
```

### 6.2 Rich Payload
```json
{
  "brand": {
    "name": "Five Valleys Heating & Air",
    "phone": "+14065550177",
    "phoneDisplay": "(406) 555-0177"
  },
  "nav": [
    { "label": "Services", "href": "/services" },
    { "label": "Financing", "href": "/financing" },
    { "label": "Reviews", "href": "/reviews" },
    { "label": "Contact", "href": "/contact" }
  ],
  "primaryCard": {
    "eyebrow": "Missoula HVAC Experts",
    "headline": "Comfort Restored Fast—Without the Sales Pressure",
    "subhead": "Repair, maintenance, and replacement with transparent options and local technicians you can trust.",
    "primaryCta": { "label": "Book Service Now", "href": "/book" },
    "secondaryCta": { "label": "Call (406) 555-0177", "href": "tel:+14065550177" },
    "trustChips": ["NATE-Certified", "4.9★ from 300+", "24/7 Emergency", "Financing Available"],
    "heroImage": {
      "src": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1400&q=80",
      "alt": "HVAC technician servicing a residential unit"
    }
  },
  "proofCard": {
    "ratingValue": 4.9,
    "ratingCount": 312,
    "quote": "They explained every option clearly and fixed it same day.",
    "attribution": "— Mark T., Missoula"
  },
  "availabilityCard": {
    "title": "Rapid Response",
    "detail": "Most calls returned in under 15 minutes during business hours.",
    "badge": "Open Today"
  },
  "serviceAreaCard": {
    "title": "Proudly Serving",
    "areas": ["Missoula", "East Missoula", "Lolo", "Florence", "Bonner"],
    "radiusMiles": 40
  },
  "guaranteeCard": {
    "title": "Why Homeowners Choose Us",
    "bullets": ["Licensed, bonded, insured", "No-surprise estimates", "Satisfaction guaranteed", "Clean-up after every job"]
  },
  "theme": { "mode": "dark", "accentHex": "#22d3ee" },
  "seo": {
    "title": "Missoula HVAC Service | Five Valleys Heating & Air",
    "description": "Fast local HVAC service with transparent pricing and trusted technicians."
  }
}
```

---

## 7) Implementation Notes for Agents

- Prefer CSS Grid over Flex for card composition.
- Keep card heights content-driven with minimum bounds for rhythm.
- Use `clamp()` typography for responsive scaling.
- Avoid JS dependence for first meaningful paint.
- Expose all textual values as props for CMS population.
