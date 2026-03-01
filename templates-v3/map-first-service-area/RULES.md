# Map-First Service Area Archetype — Implementation Rules

## 1) Purpose + Archetype Definition

This archetype is for local service businesses where **coverage confidence** is the conversion trigger:
users want immediate clarity on _"Do you serve my address, and how fast can you get here?"_

**Core idea:** the first viewport is anchored by an interactive-looking service-area map module plus a clear serviceability action path.

Best fit: mobile mechanics, towing, locksmith, restoration, snow removal, delivery/haul-away, on-site diagnostics, and any radius-based field service.

---

## 2) Material Distinction Requirements (Must Pass)

### 2.1 Not split-screen hero
- Do **not** use a 50/50 text-vs-image slab as the primary above-fold composition.
- If two columns exist on desktop, map must dominate visual priority and area.

### 2.2 Not asymmetric bento
- Do **not** compose first viewport as a mosaic of irregular cards.
- Avoid card-span artistry as hierarchy engine.

### 2.3 Not editorial-story
- Do **not** lead with narrative chapters.
- Long-form prose cannot precede map + CTA + trust essentials.

### 2.4 Not utility-dashboard
- Do **not** frame above fold as operational KPI board with queue-centric density.
- At most 3 compact trust/service chips above fold; no “control room” feel.

### 2.5 Map-First signature
Above fold must include:
1. Service-area map module (dominant)
2. “Check my address” or equivalent serviceability CTA
3. Radius/coverage clarity (miles + locality examples)
4. Fast-contact fallback CTA (call/text)

If a reviewer describes the first viewport as “hero copy with a decorative map,” it fails.

---

## 3) Research Basis (Condensed)

Implementation aligns with practical standards and known local-search behavior:
- Google Business Profile local ranking is driven by **relevance, distance, prominence**; explicit location/service coverage clarity supports user decision confidence.
- Google local presence guidance emphasizes complete business details and area clarity.
- WCAG 2.x contrast/focus/touch target requirements are non-negotiable.
- Core Web Vitals: keep LCP <= 2.5s (p75 target), avoid heavy blocking map scripts for initial layout.

---

## 4) Layout Mechanics

### 4.1 Container and breakpoints
- Max width: `1240px`
- Horizontal padding:
  - Mobile: `16px`
  - Tablet: `24px`
  - Desktop: `32px`
- Breakpoints:
  - Mobile `<768px`
  - Tablet `768-1023px`
  - Desktop `>=1024px`

### 4.2 Above-fold composition
Required order in DOM:
1. Top nav and primary contact action
2. Value statement block (short, local, specific)
3. Primary CTA cluster
4. Map module with coverage overlay
5. Trust micro-strip

Desktop can place value block and map side-by-side, but map must consume **>=55%** of above-fold visual area.

### 4.3 Map module anatomy (required)
- Map canvas (static image, embed, or scripted map)
- Coverage circle/polygon visual cue
- Labelled locality pins/tags (3-8)
- Coverage legend (e.g., “Core 12 mi • Extended 25 mi”)
- Accessible fallback link: “Open map in Google Maps”

---

## 5) Content and Hierarchy Rules

### 5.1 Required content blocks
- **Kicker:** service + location
- **H1:** outcome + location intent
- **Subcopy:** response-time promise + boundary caveat
- **Primary CTA:** address/serviceability check
- **Secondary CTA:** phone/text immediate route
- **Trust strip:** rating + credentials + guarantee (minimum 3 cues)
- **Coverage details:** neighborhoods/towns list

### 5.2 Copy limits
- H1 preferred <= 14 words; hard cap 18
- Subcopy <= 30 words
- Primary CTA <= 5 words
- Coverage labels 1-3 words each
- Trust chip text <= 28 chars per chip

### 5.3 Priority model
- Level A: map + address-check CTA
- Level B: response time + trust strip
- Level C: expanded service area details, FAQ, secondary content

---

## 6) Spacing + Rhythm

Use 8px spacing tokens only:
`4, 8, 12, 16, 24, 32, 40, 48, 64, 80`

Rules:
- Hero top/bottom padding: `40-72px`
- Map card padding: `12-20px`
- CTA cluster gap: `10-12px`
- Trust strip gap: `8-12px`
- Section spacing after hero: `48-72px`

No arbitrary pixel values unless tokenized.

---

## 7) Typography

- Sans stack for clarity (Inter/Manrope/system-ui).
- H1: `clamp(1.9rem, 4.6vw, 3.4rem)`, line-height `1.06-1.15`, weight `750-820`
- Section heads: `clamp(1.2rem, 2.3vw, 2rem)`
- Body: `1rem-1.1rem`, line-height `1.5-1.65`
- Chips/meta: `0.8rem-0.92rem`

Avoid decorative display fonts that reduce map-label legibility.

---

## 8) Color + Contrast

### 8.1 Palette roles
- Canvas: light neutral or deep neutral
- Map module: distinct surface with clear boundary
- One primary accent for CTA and map highlights
- One support color for status (optional)

### 8.2 Contrast minimums
- Body text: >= 4.5:1
- Large text: >= 3:1
- Focus rings/UI boundaries: >= 3:1

### 8.3 Visual constraints
- Keep map overlays readable; avoid saturated heatmaps behind labels.
- No more than 2 accent hues in first viewport.

---

## 9) Map UX and Interaction Rules

- Map must not trap vertical scrolling on mobile.
- If using iframe/embed, load lazily where possible and provide static poster fallback.
- Add explicit “Open full map” link for navigation apps.
- Keep at least one non-map path to conversion (call/text CTA).
- Do not require pinch-zoom to understand coverage.

---

## 10) CTA + Trust Rules

### 10.1 CTA requirements
- Primary CTA above fold and visually dominant.
- Secondary CTA clearly interactive but subordinate.
- Never more than 2 CTA buttons in one cluster.

### 10.2 CTA copy
Preferred primary patterns:
- “Check My Address”
- “See If We Serve You”
- “Find My Service Window”

Avoid generic primary labels (`Submit`, `Get Started`, `Learn More`).

### 10.3 Trust requirements (first 2 viewport heights)
Minimum 3 cues across hero area:
- Rating + review count
- Licensed/insured/certified
- Warranty/guarantee or years in business

---

## 11) Accessibility Rules (Non-negotiable)

- Exactly one `<h1>`.
- Semantic landmarks: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`.
- Keyboard focus order follows visual order.
- All actionable elements have visible `:focus-visible`.
- Map or map image must have accessible name/alt context.
- Decorative map ornaments must be `aria-hidden="true"`.
- Touch targets >= 44px height.

---

## 12) Performance Rules

- No JS required for initial layout.
- If interactive map is used, defer non-critical scripts.
- LCP candidate should be text block or optimized static map poster.
- Prefer compressed modern image formats for map poster.
- Avoid autoplay media in hero.

---

## 13) Conversion Guardrails

- Above fold must answer within 5 seconds:
  1. What service?
  2. Which area?
  3. How fast?
  4. What next action?
- Do not hide coverage boundaries behind modal walls.
- No fake urgency or fabricated “live” map status.
- If “same-day” is claimed, include a realistic qualifier.

---

## 14) Do / Don’t

### Do
- Show named nearby neighborhoods/towns on or near map.
- Make address-check CTA the main path.
- Pair map with concise trust evidence.
- Keep mobile map height moderate so CTA remains visible.

### Don’t
- Don’t reduce map to tiny decorative thumbnail.
- Don’t imitate dashboard KPI wall.
- Don’t use bento tile mosaics for above-fold hierarchy.
- Don’t push primary CTA below map-only content on phones.

---

## 15) QA Checklist (Ship Gate)

### Archetype Integrity
- [ ] First viewport clearly map-first
- [ ] Not split hero, bento mosaic, editorial lead, or utility dashboard
- [ ] Map module visually dominant at desktop

### Conversion
- [ ] Primary CTA visible at 390x844 without horizontal scroll
- [ ] Secondary CTA subordinate and clear
- [ ] Service radius/localities explicit

### Trust + Content
- [ ] >= 3 trust cues visible by end of second viewport
- [ ] Coverage claims specific and plausible
- [ ] CTA copy action-oriented and specific

### Accessibility
- [ ] One h1 only
- [ ] Keyboard/focus states verified
- [ ] Contrast thresholds pass
- [ ] Touch targets >= 44px

### Responsive + Performance
- [ ] No horizontal overflow at 320px
- [ ] Mobile map does not hide CTA clarity
- [ ] Core layout renders without JS
- [ ] LCP target strategy documented

If any critical item fails, block release.

---

## 16) Acceptance Tests

### A) Map-First Integrity
- [ ] At 1366x768, map module is primary visual anchor and occupies majority hero area.
- [ ] Reviewer can identify service area + action path in <5 seconds.

### B) Mobile Conversion
- [ ] At 390x844, primary CTA appears before map fold break.
- [ ] Header/nav does not crowd hero copy or CTAs.

### C) Accessibility
- [ ] Keyboard can reach nav, CTA, and map link in logical order.
- [ ] Focus styles clearly visible on dark and light surfaces.

### D) Responsive Stability
- [ ] No clipped locality labels at 320px.
- [ ] No horizontal scroll on any primary section.

### E) Performance
- [ ] Initial paint does not depend on remote map JS.
- [ ] Non-critical map enhancements load progressively.
