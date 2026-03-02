# Editorial Story Archetype — Implementation Rules

## 1) Purpose and Archetype Definition

This archetype is for local service businesses that need to convert while also explaining **process, credibility, and decision confidence**.

**Core pattern:** a magazine-style narrative homepage: strong headline, concise narrative chapters, proof inserts, and repeated low-friction CTAs.

Use this archetype when buyers need reassurance before contacting (higher-ticket or trust-sensitive services): roofing, restoration, legal, dental implants, HVAC replacement, landscaping design-build, remodeling.

---

## 2) Research Basis (Condensed)

Implementation decisions align with known UX/CRO evidence and standards:

- **Progressive disclosure + scanning behavior**: users scan first, then commit to reading when structure is obvious. Use short sections, clear headings, pull quotes, and visual anchors.
- **Story framing effect in persuasion**: concrete customer context and process transparency improve trust versus abstract claims.
- **Local trust signal behavior**: reviews, licensing/insurance, service area specificity, and response-time clarity materially influence local provider choice.
- **WCAG 2.x** contrast/focus requirements: non-negotiable for production.
- **Core Web Vitals**: narrative pages can become heavy; enforce image and script budgets.

---

## 3) Distinction Requirements (Must Be Materially Different)

To remain distinct from other archetypes:

### 3.1 Not Split-Screen
- Do **not** use a persistent 50/50 hero lockup.
- Do **not** make the first screen primarily side-by-side text and image.

### 3.2 Not Asymmetric Bento
- Do **not** present above-the-fold information as a multi-card mosaic.
- Do **not** rely on card span hierarchy for primary information architecture.

### 3.3 Editorial Signature
- Use a **single dominant text column** for narrative flow.
- Use occasional supporting side rail/meta blocks (desktop only).
- Use chapter-like section rhythm: problem → method → evidence → offer.

If any reviewer can describe the first viewport as “split hero” or “bento cards,” this archetype fails.

---

## 4) Layout Mechanics

### 4.1 Global Container
- Max width: `1200px`.
- Content measure (narrative body): `62ch–72ch`.
- Horizontal padding:
  - Mobile: `16px`
  - Tablet: `24px`
  - Desktop: `32px`

### 4.2 Structural Pattern
Required flow:
1. Masthead / editorial hero
2. Quick trust strip
3. Story chapter sections (minimum 3)
4. Offer + CTA section
5. FAQ
6. Footer

### 4.3 Chapter Layout (Desktop)
- 12-column grid.
- Main narrative column spans 7-8 columns.
- Optional contextual rail spans 3-4 columns for proof snippets, service-area tags, or micro-CTAs.
- Keep reading order linear in DOM (main story first, rail second).

### 4.4 Mobile Layout
- One column, strict content order.
- Side rail content collapses below each chapter intro.
- No sticky side rail on mobile.

---

## 5) Hierarchy + Content Model

### 5.1 Masthead Components (Required)
- Service + location kicker
- Single H1 with outcome-based promise
- 1 short deck paragraph
- Primary CTA + secondary CTA
- Byline-style credibility line (e.g., licensed, years in business)

### 5.2 Chapter Components (Required)
At least 3 chapters:
- **Chapter 1: The Local Problem Context**
- **Chapter 2: How the Team Solves It (process clarity)**
- **Chapter 3: Real Outcomes and Proof**

Each chapter includes:
- Label (`Chapter 01` etc.)
- H2
- 1-2 short paragraphs
- One concrete data point or specific claim

### 5.3 Proof Inserts (Required)
Across the first 2 viewport heights include at least 3 trust signals:
- Rating + review count
- License/insured/certification
- Warranty/guarantee or years in business

### 5.4 CTA Cadence
- Primary CTA appears in masthead.
- Reinforcement CTA appears after Chapter 2.
- Final CTA appears before FAQ/footer.

---

## 6) Spacing System

Use 8px baseline spacing tokens only:
`4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96`

Rules:
- Masthead top padding: `64-96px desktop`, `40-56px mobile`
- Chapter spacing: `56-80px desktop`, `40-56px mobile`
- Heading-to-body: `12-16px`
- Paragraph-to-paragraph: `12-16px`
- CTA cluster gap: `12px`

No arbitrary spacing values unless tokenized via CSS custom properties.

---

## 7) Typography Rules

### 7.1 Type System
- Serif display font allowed for editorial tone (headline/section heads).
- Sans-serif for body/UI for legibility.

### 7.2 Scale
- H1: `clamp(2.2rem, 5.2vw, 4.5rem)`, line-height `1.02-1.12`, weight `700-800`
- H2: `clamp(1.45rem, 2.2vw, 2.2rem)`, line-height `1.15-1.3`
- Body: `1rem-1.125rem`, line-height `1.6-1.8`
- Labels/meta: `0.78rem-0.9rem`, letter spacing slight positive

### 7.3 Copy Limits
- H1: preferred <= 14 words, hard cap 18
- Deck: <= 32 words
- Paragraph: <= 85 words each
- Pull quote: <= 28 words

---

## 8) Palette, Contrast, and Surface Rules

### 8.1 Palette Roles
- Paper/background: warm light neutral or deep neutral.
- Ink/text: high-contrast near-black or near-white.
- Accent: 1 primary brand accent for CTA and chapter rules.
- Optional support tone for trust markers.

### 8.2 Contrast (Required)
- Body text >= 4.5:1
- Large text >= 3:1
- UI boundaries/icons/focus >= 3:1
- Focus indicators visible regardless of color vision.

### 8.3 Noise Control
- Max 2 accent colors total.
- Avoid heavy gradients behind body copy.
- Decorative textures must never reduce text contrast.

---

## 9) Imagery and Media Rules

- Prefer documentary-style local service imagery (crew in real context).
- Use 1 strong masthead image and optional chapter images; avoid gallery overload.
- Keep image ratio stable to prevent CLS.
- Meaningful images require specific alt text.
- Decorative images must use `alt=""`.

Image performance guidance:
- Hero image target <= 280KB compressed where feasible.
- Use modern formats + lazy-load non-critical images.

---

## 10) CTA + Trust Placement Rules

### 10.1 CTA Style Hierarchy
- Exactly 1 dominant primary style per section.
- Secondary action must be visually quieter.

### 10.2 Required CTA Labels
Use action-oriented, specific labels:
- Good: `Get My On-Site Estimate`, `Call a Missoula Technician`
- Avoid: `Submit`, `Click Here`, `Learn More` (as primary)

### 10.3 Trust Placement
- Trust strip directly after masthead.
- At least one review quote before second CTA.
- Service area specificity (towns/neighborhoods) before final CTA.

---

## 11) Responsive Behavior

Breakpoints:
- Mobile `< 768px`
- Tablet `768-1023px`
- Desktop `>= 1024px`

Rules:
- Maintain reading-first hierarchy at all sizes.
- Never hide critical trust information behind tabs/accordions above fold.
- Keep first CTA visible at `390x844` without horizontal scroll.
- Side rail can become inline cards on small viewports.

---

## 12) Accessibility Requirements (Non-Negotiable)

- Exactly one `<h1>`.
- Semantic landmarks: `<header>`, `<main>`, `<section>`, `<nav>`, `<footer>`.
- Logical heading sequence (`h1 > h2 > h3` as needed).
- Keyboard-operable navigation and CTAs.
- Visible `:focus-visible` styles.
- Respect `prefers-reduced-motion`.
- Form fields (if present) require labels and clear errors.

---

## 13) Conversion Guardrails

- Do not allow story copy to bury CTA for more than one full viewport.
- No fabricated testimonials, ratings, or badges.
- No manipulative urgency timers.
- Keep cognitive load controlled:
  - One dominant H1
  - One primary CTA per cluster
  - Max 5 trust chips in masthead area
- If “free estimate” is promised, friction must remain low (no account required).

---

## 14) Do / Don’t

### Do
- Write in concrete local language (service + place + response promise).
- Show process transparency in plain language.
- Use pull quotes and proof boxes to break dense text.
- Repeat CTA at natural narrative decision points.

### Don’t
- Turn the page into a generic blog article with no conversion path.
- Use walls of text or paragraphs longer than ~6 lines on desktop.
- Use card mosaics that mimic bento archetype.
- Revert to a split hero with equal side-by-side panels.

---

## 15) QA Checklist (Ship Gate)

### Structure
- [ ] Editorial story flow present (masthead → chapters → offer → FAQ)
- [ ] Not visually or structurally split-screen
- [ ] Not visually or structurally bento

### Conversion
- [ ] Primary CTA visible in first viewport (390x844 + 1366x768)
- [ ] Trust strip appears before heavy narrative body
- [ ] CTA repeated after chapter progression

### Content Quality
- [ ] Chapter claims are specific and believable
- [ ] Local area references are explicit
- [ ] Review/proof data includes numeric specificity

### Accessibility
- [ ] One h1 only
- [ ] Focus states obvious on all interactive controls
- [ ] Contrast targets pass WCAG minimums
- [ ] Meaningful alt text where required

### Responsive + Performance
- [ ] No horizontal overflow at 320px
- [ ] Side rail reflows cleanly to one column
- [ ] Hero and chapter images sized to prevent layout shift
- [ ] LCP candidate optimized and non-blocking

If any critical item fails, block deployment.

---

## 16) Reference Data Schema (Content Contract)

```ts
interface EditorialStoryHomepage {
  brand: {
    name: string;                    // required
    serviceCategory: string;         // e.g., "Roofing & Exteriors"
    location: string;                // e.g., "Missoula, MT"
    phone?: string;                  // tel link, E.164 preferred
    phoneDisplay?: string;
  };

  nav: Array<{ label: string; href: string }>;

  masthead: {
    kicker: string;                  // service + locality cue
    headline: string;                // required
    deck: string;                    // required
    primaryCta: { label: string; href: string };
    secondaryCta?: { label: string; href: string };
    credibilityLine: string;         // e.g., "Licensed • Insured • Since 2009"
    heroImage?: { src: string; alt: string };
  };

  trustStrip: Array<{
    label: string;                   // e.g., "4.9★ Google"
    detail: string;                  // e.g., "From 280+ reviews"
  }>;

  chapters: Array<{
    id: string;
    chapterLabel: string;            // "Chapter 01"
    title: string;
    body: string[];                  // 1..2 paragraphs
    proofPoint: string;              // numeric/specific proof
    railItems?: string[];
    image?: { src: string; alt: string };
  }>; // min length 3

  midCta: {
    headline: string;
    body: string;
    primaryCta: { label: string; href: string };
  };

  serviceArea: {
    title: string;
    areas: string[];                 // min 3 suggested
  };

  faq: Array<{ q: string; a: string }>;

  finalCta: {
    headline: string;
    body?: string;
    primaryCta: { label: string; href: string };
    secondaryCta?: { label: string; href: string };
  };
}
```

---

## 17) Acceptance Tests

### A) Archetype Integrity
- [ ] First viewport reads as editorial masthead, not split hero or bento cards
- [ ] Main narrative column is dominant reading path
- [ ] At least 3 chapters with chapter labels

### B) Conversion Integrity
- [ ] CTA present in masthead, mid-page, and final section
- [ ] >= 3 trust signals visible by end of second viewport
- [ ] Service area specificity shown before final CTA

### C) Accessibility
- [ ] Exactly one h1
- [ ] Keyboard focus order follows reading order
- [ ] `:focus-visible` present and visually strong
- [ ] Contrast requirements pass for text and controls

### D) Responsive
- [ ] No horizontal scrolling at 320px and 390px widths
- [ ] Rail content reflows below chapter body on mobile
- [ ] Touch targets >= 44px height

### E) Performance
- [ ] LCP element optimized (preload if hero image)
- [ ] Non-critical images lazy-loaded
- [ ] No render-blocking JS required for core layout
