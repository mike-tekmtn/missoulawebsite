# Asymmetric Bento Archetype — Implementation Rules

## 1) Purpose and Positioning
This archetype is for **local service business homepages** that need fast trust-building and high-intent conversion (calls, quote requests, bookings).

**Core idea:** Instead of one split hero, use an **asymmetric card mosaic** where one primary value card anchors the grid and secondary cards prove trust, speed, scope, and outcomes.

---

## 2) Layout Mechanics (Desktop-First Intent, Mobile-First Build)

### 2.1 Container + Grid
- Use a max content width between **1120px and 1280px**.
- Horizontal page padding:
  - Mobile: `16px`
  - Tablet: `24px`
  - Desktop: `32px`
- Bento grid at desktop: **12 columns**, with a base gap of **16px**.
- All cards must align to a consistent baseline grid; no arbitrary offsets.

### 2.2 Card Spans (Canonical Composition)
Use this default arrangement above the fold:
- **Primary Value Card**: `col-span 7`, `row-span 2`
- **Proof/Review Card**: `col-span 5`, `row-span 1`
- **Speed/Availability Card**: `col-span 3`, `row-span 1`
- **Service Area Card**: `col-span 2`, `row-span 1`
- **Trust/Guarantee Card**: `col-span 5`, `row-span 1`

This creates intentional asymmetry while keeping scan order clear.

### 2.3 Reading Path
Cards must support a Z/F scan:
1. Brand + navigation
2. Primary value card (headline + primary CTA)
3. Proof card (rating/testimonial)
4. Operational certainty cards (availability, area, guarantees)

### 2.4 Distinction From Split-Screen Hero
- Do **not** use a single 50/50 text-image slab.
- No full-height two-panel lockup.
- Visual priority must emerge from **card hierarchy and span**, not from left/right split.

---

## 3) Card Hierarchy and Content Roles

### 3.1 Required Card Types
1. **Primary Value Card (required)**
   - H1, subhead, primary CTA, secondary CTA, 2-4 trust chips.
2. **Social Proof Card (required)**
   - Star rating, review count, one short testimonial.
3. **Availability Card (required)**
   - Response-time promise or schedule cue.
4. **Service Area Card (required)**
   - Explicit geography + mileage/coverage.
5. **Guarantee/Policy Card (required)**
   - Warranty, licensed/insured, satisfaction promise.

### 3.2 Optional Card Types
- Financing/payment options
- Before/after visual
- Team credential snapshot
- Seasonal offer card (must not displace primary CTA)

### 3.3 Priority Weights
- Level A (must dominate): primary value card
- Level B: social proof and guarantee
- Level C: service logistics and extras

---

## 4) Spacing Rhythm

Use an 8pt system.
- Micro: `4px`
- Tight: `8px`
- Base: `16px`
- Sectional: `24px`
- Spacious: `32px`

Rules:
- Card internal padding: **24px desktop / 18-20px mobile**
- Card corner radius: **16px**
- Vertical rhythm between heading and text: **12-16px**
- CTA group gap: **10-12px**

---

## 5) Typography

### 5.1 Stack
- Primary sans for UI and body (Inter/Manrope/system-ui equivalent).
- One display weight for H1 emphasis; avoid decorative fonts.

### 5.2 Scale
- H1: clamp `32px-56px`, line-height `1.05-1.12`, weight `700-800`
- H2/Card titles: `20-28px`, weight `650-750`
- Body: `16-18px`, line-height `1.45-1.65`
- Meta/chips: `12-14px`

### 5.3 Copy Limits
- H1 max: 12 words preferred, 16 hard cap
- Subhead max: 26 words
- Testimonial quote max: 24 words
- Chips: 2-5 words each

---

## 6) Color, Contrast, and Surfaces

### 6.1 Palette Roles
- Background canvas: dark neutral or very light neutral.
- Card surfaces: 2-3 tonal layers max.
- Accent color: single brand accent for CTA and highlights.
- Support color: optional for badges/status.

### 6.2 Contrast Minimums
- Body text: **4.5:1** minimum
- Large text (>=24px regular / >=18.66px bold): **3:1** minimum
- Interactive focus ring must be clearly visible on all surfaces.

### 6.3 Visual Noise Control
- Avoid more than 1 gradient-heavy card in first viewport.
- Do not place patterned photos behind paragraph text unless overlay guarantees contrast.

---

## 7) Imagery and Media

- Use authentic service-context imagery (crew, truck, tools, homeowner context).
- Preferred hero image treatment inside a card, not full-page takeover.
- If image is decorative, set empty alt (`alt=""`).
- If meaningful, alt must describe service context concisely.
- Avoid stock images that look corporate-generic or geographically irrelevant.

---

## 8) CTA + Trust Placement Rules

### 8.1 Primary CTA
- Must appear in primary card, above fold, as first strong button.
- Label should be action + intent: e.g., “Get My Free Estimate”.

### 8.2 Secondary CTA
- Must be lower emphasis than primary (outline/ghost/text button).
- Typical purpose: call now, view services, or financing details.

### 8.3 Trust Elements
- At least **three trust markers** visible above fold:
  - rating/review count
  - licensed/insured
  - warranty/guarantee or years in business

### 8.4 Contact Friction
- Phone number tap target min **44px** height.
- Quote form entry path should not require account creation.

---

## 9) Responsive Behavior

### 9.1 Breakpoints
- Mobile: `< 768px`
- Tablet: `768-1023px`
- Desktop: `>= 1024px`

### 9.2 Reflow
- Mobile: cards stack in priority order (A -> B -> C).
- Tablet: use 6-column adaptation; primary card spans full width.
- Desktop: 12-column asymmetric composition.

### 9.3 Interaction
- Keep primary CTA visible without scrolling on common mobile heights (~740px).
- Avoid hover-only disclosure for critical information.

---

## 10) Accessibility Rules

- One clear `<h1>` only.
- Semantic landmarks: `<header>`, `<main>`, `<section>`, `<nav>`, `<footer>` as appropriate.
- Keyboard focus order must follow visual reading order.
- All actionable controls have visible focus states.
- Use ARIA only when native semantics are insufficient.
- Icons need text labels nearby or `aria-hidden="true"` when decorative.

---

## 11) Conversion Guardrails

- Do not bury CTAs below dense explanatory text.
- Do not show more than 2 competing primary-style buttons.
- Keep above-the-fold cognitive load limited:
  - max 1 headline
  - max 1 testimonial snippet
  - max 5 chips
- Avoid fake urgency (“Only 1 slot left”) unless data-driven and real-time.
- Do not hide pricing model if “free estimate” is promised.

---

## 12) Do / Don’t Examples

### Do
- Use a dominant value card with concise outcome-driven promise.
- Pair proof with specifics (4.9★ from 240+ reviews).
- Show local relevance (neighborhoods, radius, response window).
- Keep card content scannable and short.

### Don’t
- Don’t mimic split-screen hero by stretching one image half across viewport.
- Don’t place long paragraphs inside small cards.
- Don’t mix many accent colors that dilute CTA salience.
- Don’t rely on carousels for critical proof content.

---

## 13) QA Checklist (Ship Gate)

### Structure
- [ ] Layout uses asymmetric multi-card bento, not split-screen
- [ ] Primary card is visibly dominant
- [ ] Required card types all present

### Content + Conversion
- [ ] Primary CTA above fold and obvious
- [ ] Secondary CTA visually subordinate
- [ ] Minimum 3 trust indicators above fold
- [ ] Service area and availability explicitly stated

### Visual + Brand
- [ ] Spacing follows 8pt rhythm
- [ ] Card radii/padding consistent
- [ ] Accent color reserved mainly for CTA/highlight

### Accessibility
- [ ] Contrast meets WCAG minimums
- [ ] Keyboard navigation and focus states verified
- [ ] Alt text quality checked
- [ ] No critical hover-only interactions

### Responsive
- [ ] Mobile stack order preserves conversion priority
- [ ] No overflow/cutoff in cards at 320px width
- [ ] CTA remains easy to reach on mobile

If any item fails, block deployment until corrected.
