# Editorial Story Component Spec (for Coding Agents)

## 1) Component Contract

**Component name:** `EditorialStoryHomepage`

**Intent:** Build a conversion-driven local-service homepage using a narrative editorial structure.

**Must not emulate:**
- split-screen hero
- asymmetric bento mosaic

---

## 2) Props / Data Schema

```ts
type Cta = {
  label: string;                 // required, 2..36 chars
  href: string;                  // required, http(s), relative, or tel:
  ariaLabel?: string;
};

type NavItem = {
  label: string;                 // required, 1..24 chars
  href: string;                  // required
};

type ImageAsset = {
  src: string;                   // required
  alt: string;                   // required unless decorative usage is explicit
  width?: number;
  height?: number;
};

type TrustItem = {
  label: string;                 // e.g., "4.9★ Google"
  detail: string;                // e.g., "280+ verified reviews"
};

type Chapter = {
  id: string;                    // slug-like unique id
  chapterLabel: string;          // e.g., "Chapter 01"
  title: string;                 // 12..90 chars
  body: string[];                // length 1..2; each 40..520 chars
  proofPoint: string;            // concise, concrete claim (8..120 chars)
  railItems?: string[];          // 1..4 short bullets
  image?: ImageAsset;
};

interface EditorialStoryHomepageProps {
  brand: {
    name: string;                // required
    serviceCategory: string;     // required
    location: string;            // required
    phone?: string;              // optional tel:+1...
    phoneDisplay?: string;
  };

  nav: NavItem[];                // required, 3..6 preferred

  masthead: {
    kicker: string;              // required
    headline: string;            // required
    deck: string;                // required
    credibilityLine: string;     // required
    primaryCta: Cta;             // required
    secondaryCta?: Cta;
    heroImage?: ImageAsset;
  };

  trustStrip: TrustItem[];       // required, min 3 max 5

  chapters: Chapter[];           // required, min 3

  midCta: {
    headline: string;
    body: string;
    primaryCta: Cta;
  };

  serviceArea: {
    title: string;
    areas: string[];             // min 3
  };

  faq: Array<{
    q: string;                   // required
    a: string;                   // required
  }>;                            // min 3 max 6

  finalCta: {
    headline: string;
    body?: string;
    primaryCta: Cta;
    secondaryCta?: Cta;
  };

  theme?: {
    canvasHex?: string;          // default #f7f4ee
    textHex?: string;            // default #1a1a1a
    accentHex?: string;          // default #c4492d
    accentDarkHex?: string;      // default #7f2817
  };

  seo?: {
    title?: string;
    description?: string;
  };
}
```

---

## 3) Validation Rules

### 3.1 Required + Length Constraints
- `masthead.headline` required, max 18 words.
- `masthead.deck` required, max 32 words.
- `trustStrip.length` must be `3..5`.
- `chapters.length` must be `>= 3`.
- each `chapter.body.length` must be `1..2`.
- `faq.length` must be `3..6`.

### 3.2 CTA Rules
- `masthead.primaryCta` required.
- CTA labels must be action-oriented; disallow generic `submit`, `click here` as primary.
- No more than 2 CTA buttons in any single cluster.

### 3.3 Accessibility Rules
- Exactly one `<h1>`.
- Every interactive element has visible `:focus-visible` state.
- If image is informative, `alt` must be non-empty and descriptive.

### 3.4 Security / URL Validation
Reject `javascript:` URLs in any `href`.

### 3.5 Anti-Pattern Guards
Reject or fail lint if any of these are true:
- hero wrapper configured as equal two-column 50/50 at desktop
- above-fold rendered as card mosaic with 4+ independent cards
- more than 2 primary-style CTA buttons rendered in first viewport

---

## 4) Rendering Specification

### 4.1 Section Order (Deterministic)
1. Top nav
2. Masthead
3. Trust strip
4. Story chapters (in array order)
5. Mid-page CTA band
6. Service area module
7. FAQ
8. Final CTA
9. Footer

### 4.2 Masthead Layout
- Full-width section with subtle paper-style texture/background.
- Text block centered within readable measure.
- Optional hero image appears below intro copy (not side-by-side equal split).

### 4.3 Chapter Layout
- Desktop: 12-col grid, main text (7-8 cols), side rail (3-4 cols).
- Mobile: one-column stack, rail modules moved below chapter body.
- Use chapter divider rules and labels for editorial pacing.

### 4.4 Trust Elements
- Trust strip must appear immediately after masthead.
- Visual style: low-noise chips or mini-stat rows.

### 4.5 CTA Recurrence
- Maintain one prominent CTA in masthead, mid-section, and end-section.
- Secondary CTA optional and lower visual emphasis.

---

## 5) Styling Contract

### 5.1 Spacing Tokens
Define tokens:
```css
--s-1: 4px;
--s-2: 8px;
--s-3: 12px;
--s-4: 16px;
--s-5: 24px;
--s-6: 32px;
--s-7: 40px;
--s-8: 48px;
--s-9: 64px;
--s-10: 80px;
```

### 5.2 Typography Tokens
- `--font-display`: serif stack
- `--font-body`: sans stack
- body line-height `>= 1.6`

### 5.3 Buttons
- Min touch target `44px` height.
- Primary filled accent; secondary outlined or ghost.
- Focus ring minimum 2px with high contrast.

### 5.4 Color & Contrast
- Body text contrast >= 4.5:1.
- Large headings >= 3:1.
- Controls + focus rings >= 3:1 against adjacent background.

---

## 6) Accessibility Implementation Notes

- Add skip link (`Skip to content`).
- Landmarks: `header`, `main`, `footer`, named `nav`.
- FAQ can use semantic `<details>/<summary>` or explicit buttons with ARIA controls.
- Never rely on color-only cues.
- Respect reduced-motion media query.

---

## 7) Conversion Guardrails (Implementation)

- Max one primary CTA button per CTA cluster.
- Keep first conversion opportunity above fold on mobile.
- Insert proof before second CTA.
- Keep section intros concise; avoid >2 paragraphs before first CTA repeat.
- Claims in proof modules must be specific (numbers, certifications, dates).

---

## 8) Do / Don’t for Implementers

### Do
- Build for readability first, then enhance with visuals.
- Keep chapter rhythm consistent.
- Use local references naturally.

### Don’t
- Don’t place long text directly on busy imagery.
- Don’t create card-heavy dashboard aesthetic.
- Don’t over-animate section reveals.

---

## 9) QA Checklist

### Structure
- [ ] Section order matches rendering specification
- [ ] At least 3 story chapters rendered
- [ ] One h1 only

### Archetype Distinction
- [ ] No 50/50 split hero at desktop
- [ ] No bento mosaic above fold

### Conversion
- [ ] Masthead CTA visible at 390x844
- [ ] Mid CTA and final CTA both present
- [ ] Trust strip appears before chapter body

### Accessibility
- [ ] Keyboard tab flow logical
- [ ] All controls have visible focus style
- [ ] Contrast passes thresholds

### Responsive
- [ ] No horizontal overflow at 320px
- [ ] Side rail stacks cleanly on mobile
- [ ] Buttons remain >=44px tall

### Performance
- [ ] Hero image optimized and sized
- [ ] Non-critical images lazy-loaded
- [ ] No blocking JS needed for core layout

---

## 10) Acceptance Tests

### Test A — Data Validation
- Given invalid `javascript:` CTA href
- When component initializes
- Then render is rejected or href sanitized to safe fallback

### Test B — Editorial Shape
- Given valid props
- When rendered at 1440px width
- Then masthead is single-flow narrative and not equal split

### Test C — Trust & Conversion
- Given valid props
- When rendered
- Then trust strip appears immediately below masthead and before first chapter
- And primary CTA is visible without scroll at 390x844

### Test D — Accessibility
- Given rendered page
- When traversing by keyboard
- Then focus order follows visual reading order
- And every button/link has visible focus

### Test E — Responsiveness
- Given viewport 320px
- When layout reflows
- Then no horizontal scrollbar appears
- And chapter rail content moves below body copy
