# Offer-Funnel Landing Component Spec (for Coding Agents)

## 1) Component Contract

**Component name:** `OfferFunnelLandingHomepage`

**Intent:** Implement a conversion-focused local-service homepage centered on a single offer funnel with staged reassurance.

**Must remain distinct from:**
- split-screen hero
- asymmetric bento
- editorial story
- utility dashboard
- map-first service area

---

## 2) Props / Data Schema

```ts
type Cta = {
  label: string;                  // required, 2..40 chars
  href: string;                   // required, relative/http(s)/tel:
  ariaLabel?: string;
};

type NavItem = {
  label: string;                  // required, 1..24 chars
  href: string;                   // required
};

type TrustChip = {
  label: string;                  // required, e.g. "4.9★ from 300+ reviews"
  tone?: "neutral" | "accent" | "positive";
};

type Step = {
  title: string;                  // required, <= 48 chars
  detail: string;                 // required, <= 24 words
};

type OfferListItem = {
  text: string;                   // required
  included: boolean;              // true = included, false = not included
};

type FaqItem = {
  q: string;
  a: string;
};

interface OfferFunnelLandingHomepageProps {
  brand: {
    name: string;                 // required
    serviceCategory: string;      // required
    location: string;             // required
    phone?: string;               // optional, tel:+1...
    phoneDisplay?: string;
  };

  nav: NavItem[];                 // required, 3..6 preferred

  hero: {
    eyebrow: string;              // required
    headline: string;             // required, <= 18 words
    subcopy: string;              // required, <= 30 words
    primaryCta: Cta;              // required
    secondaryCta?: Cta;           // optional
    nextStepText: string;         // required, e.g. "Step 1 of 3: tell us your ZIP"
    trustChips: TrustChip[];      // required, 3..5
  };

  howItWorks: {
    title: string;                // required
    steps: Step[];                // required, exactly 3
  };

  offerDetails: {
    title: string;                // required
    summary: string;              // required
    items: OfferListItem[];       // required, 4..10
    reinforcementCta?: Cta;       // optional
  };

  guarantee: {
    title: string;                // required
    bullets: string[];            // required, 2..5
  };

  faq: FaqItem[];                 // required, 3..6

  conversion: {
    title: string;                // required
    intro: string;                // required
    fields: Array<{
      name: "fullName" | "phone" | "email" | "zip" | "serviceNeed";
      label: string;
      type: "text" | "tel" | "email" | "textarea";
      required?: boolean;
      placeholder?: string;
    }>;                           // required, 3..6 fields
    submitLabel: string;          // required
    alternateCta?: Cta;           // optional, usually call
    disclaimer?: string;          // optional
  };

  seo?: {
    title?: string;
    description?: string;
  };

  theme?: {
    canvasHex?: string;           // default #f6f8fc
    inkHex?: string;              // default #0f172a
    accentHex?: string;           // default #1d4ed8
    accentDarkHex?: string;       // default #1e3a8a
    successHex?: string;          // default #0f766e
    cardHex?: string;             // default #ffffff
  };
}
```

---

## 3) Validation Rules

### 3.1 Required Groups
Required:
- `brand`, `nav`, `hero`, `howItWorks`, `offerDetails`, `guarantee`, `faq`, `conversion`

### 3.2 Cardinality and Limits
- `hero.trustChips.length` must be `3..5`
- `howItWorks.steps.length` must be exactly `3`
- `offerDetails.items.length` must be `4..10`
- `faq.length` must be `3..6`
- `conversion.fields.length` must be `3..6`

### 3.3 Copy Limits
- `hero.headline` <= 18 words
- `hero.subcopy` <= 30 words
- each `howItWorks.steps[i].detail` <= 24 words

### 3.4 CTA Rules
- `hero.primaryCta` required and action-specific.
- Maximum 2 CTA buttons per cluster.
- Disallow generic primary CTA labels: `Submit`, `Click Here`, `Learn More`.

### 3.5 URL Safety
Reject/sanitize `javascript:` in all hrefs.

### 3.6 Accessibility Rules
- Exactly one `<h1>`.
- Form controls must have associated `<label>`.
- Focus-visible states required on links, buttons, and fields.
- Touch targets >= 44px.

### 3.7 Archetype Anti-Pattern Guards
Fail lint/render if:
- desktop first viewport is equal split hero
- above fold is irregular bento card matrix
- long editorial chapter lead appears before offer CTA
- KPI-heavy operations board dominates first viewport
- map visualization dominates first viewport

---

## 4) Deterministic Rendering Order

1. Header + nav + phone action
2. Offer hero (eyebrow, h1, subcopy, CTA cluster, step cue)
3. Trust chips strip
4. How-it-works 3-step sequence
5. Offer details (included/not included) + reinforcement CTA
6. Guarantee block
7. FAQ accordion/details
8. Conversion form section + alternate contact
9. Footer

---

## 5) Styling Contract

### 5.1 Spacing Tokens
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

### 5.2 Typography
- UI/body sans stack
- `h1` via `clamp(2rem, 5vw, 3.5rem)`
- body line-height >= `1.55`

### 5.3 Buttons and Inputs
- Height >= 44px
- Primary filled accent, secondary outline/ghost
- Strong focus ring (2px+ high contrast)

### 5.4 Surfaces
- Neutral page background
- Elevated cards for steps/details/form
- Subtle border + shadow, avoid visual noise

---

## 6) Accessibility Notes

- Add skip link at top of page.
- Preserve semantic landmarks and heading order.
- FAQ can use `<details>/<summary>` for native keyboard behavior.
- Do not rely on color alone for included/excluded offer items; add icon/text label.

---

## 7) Conversion Guardrails

- Keep primary CTA visible near top on mobile.
- Repeat CTA after offer details and in conversion section.
- Keep form friction low; no account creation wall.
- Use plain-language next-step expectation copy.

---

## 8) QA Checklist

### Structure
- [ ] Sections render in deterministic order
- [ ] Exactly one h1
- [ ] Three-step how-it-works present

### Distinction
- [ ] Not split hero
- [ ] Not bento mosaic
- [ ] Not editorial lead
- [ ] Not utility dashboard
- [ ] Not map-first

### Conversion
- [ ] Primary CTA visible at 390x844
- [ ] Trust chips visible before long content
- [ ] Conversion form includes low-friction required fields only

### Accessibility
- [ ] Labeled form fields
- [ ] Visible focus styles for all interactive elements
- [ ] Touch targets >= 44px
- [ ] Contrast thresholds pass

### Responsive
- [ ] No horizontal overflow at 320px
- [ ] Header/nav wraps without overlap
- [ ] CTA cluster stacks cleanly on narrow screens

### Performance
- [ ] Offer headline + CTA render without JS
- [ ] Non-critical media lazy-loaded
- [ ] Minimal external dependencies

---

## 9) Acceptance Tests

### Test A — Archetype Integrity
Given valid props at 1366x768,
when page renders,
then first viewport presents a single offer funnel with clear CTA and step cue.

### Test B — Mobile CTA Clarity
Given valid props at 390x844,
when page loads,
then primary CTA is visible and no horizontal scroll exists.

### Test C — Form Accessibility
Given keyboard-only interaction,
when tabbing through conversion form,
then each control is reachable, labeled, and visibly focused.

### Test D — Data Safety
Given a CTA href of `javascript:alert(1)`,
when validating props,
then href is rejected or sanitized.

### Test E — Trust Placement
Given valid props,
when user reaches second viewport,
then at least 3 trust cues are visible before deep FAQ content.
