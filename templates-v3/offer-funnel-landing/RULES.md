# Offer-Funnel Landing Archetype — Implementation Rules

## 1) Purpose + Archetype Definition

This archetype is for local service businesses that want a homepage to behave like a **guided offer funnel** instead of a general brochure.

**Core idea:** one clear offer, one dominant conversion path, and staged reassurance that reduces friction from first scroll to form submit.

Use when the business has a strong front-door offer:
- free on-site estimate
- seasonal tune-up special
- inspection + written quote
- emergency-response promise with clear coverage

---

## 2) Research Basis (Condensed)

Pattern decisions align with established UX/CRO guidance:
- **Scanning behavior is top-biased and left-biased** (NN/g F-pattern): front-load offer clarity and key proof near top.
- **Mobile reading slows on difficult copy** (NN/g mobile reading research): keep copy short, concrete, and step-based.
- **Core Web Vitals (LCP)**: optimize hero and first meaningful offer block for perceived speed.
- **WCAG accessibility requirements**: one h1, visible focus, touch-target minimums, contrast compliance.
- **Funnel principle**: fewer competing actions increases completion likelihood; keep one dominant CTA per stage.

---

## 3) Distinction Requirements (Must Be Materially Different)

To remain distinct from split-screen, asymmetric-bento, editorial-story, utility-dashboard, and map-first:

### 3.1 Not Split-Screen
- Do **not** use equal two-panel hero composition.
- Do **not** lead with text/image 50-50 lockup.

### 3.2 Not Asymmetric Bento
- Do **not** build first viewport as irregular card mosaic.
- Do **not** use decorative card asymmetry as hierarchy.

### 3.3 Not Editorial Story
- Do **not** lead with chapter narrative flow.
- Do **not** require long-form reading before seeing offer + CTA.

### 3.4 Not Utility Dashboard
- Do **not** lead with KPI-heavy operational modules.
- Do **not** use command-center framing as primary identity.

### 3.5 Not Map-First
- Do **not** make map/service-radius visualization the main hero element.

### 3.6 Offer-Funnel Signature (Required)
First viewport must include:
1. Offer headline + value proposition
2. Primary CTA
3. Friction-reduction list (3–5 bullets)
4. Lightweight qualification/progress cue (e.g., “Step 1 of 3”)

If the first viewport could be described as “hero image page,” “bento cards,” or “dashboard,” this archetype fails.

---

## 4) Required Funnel Structure

Required section order:
1. Header + compact nav
2. Offer hero (single-column dominant)
3. Trust strip (proof chips)
4. “How it works” steps (3 steps)
5. Offer details + inclusions/exclusions
6. Objection handling (FAQ/guarantee)
7. Conversion section (form + alternative contact)
8. Footer

No section may introduce more than 2 competing CTAs.

---

## 5) Layout Mechanics

### 5.1 Container
- Max width: `1120px`
- Primary funnel measure: `680–760px`
- Horizontal padding:
  - Mobile: `16px`
  - Tablet: `24px`
  - Desktop: `32px`

### 5.2 Desktop Composition
- Use a **12-column grid** with a dominant offer funnel column (7–8 cols) and a support rail (4–5 cols) for proof/guarantee/form summary.
- Reading order in DOM must remain linear for accessibility.

### 5.3 Mobile Composition
- One column only.
- Header items wrap cleanly; CTA remains obvious above scroll where practical.
- Form inputs and CTA maintain `>=44px` touch target height.

---

## 6) Copy + Hierarchy Rules

### 6.1 Hero Requirements
Must include:
- local service/location eyebrow
- one H1 (outcome + offer)
- one short subhead (<= 30 words)
- primary CTA + secondary fallback CTA (phone/text)
- short “what happens next” line

### 6.2 Offer Messaging
- Lead with concrete benefit and condition.
- Avoid vague “learn more” framing.
- Preferred labels:
  - `Claim My Free On-Site Estimate`
  - `Check Today’s Open Slots`
  - `Call a Local Technician`

### 6.3 Proof Requirements
By end of second viewport include at least 3 trust elements:
- rating + review count
- licensing/insurance
- guarantee or years in business

---

## 7) Spacing, Rhythm, and Density

Use 8px baseline tokens only:
`4, 8, 12, 16, 24, 32, 40, 48, 64, 80`

Rules:
- hero vertical padding: `40–72px`
- section gaps: `40–64px`
- card padding: `16–24px`
- CTA cluster gap: `10–12px`

Density guardrail:
- Above fold text body (excluding nav) target <= 90 words.

---

## 8) Typography Rules

- Sans-serif primary stack for high legibility.
- H1: `clamp(2rem, 5vw, 3.5rem)` line-height `1.05–1.15` weight `750–850`
- H2: `clamp(1.25rem, 2.4vw, 2rem)`
- Body: `1rem–1.06rem`, line-height `1.55–1.7`
- Microcopy/meta: `0.82rem–0.92rem`

Copy limits:
- H1 <= 18 words
- Subhead <= 30 words
- Step description <= 24 words each

---

## 9) Visual Style Rules

- Palette: one primary accent + one success/support tone + neutral surfaces.
- Keep backgrounds clean; avoid noisy imagery behind offer copy.
- If hero image exists, it must be subordinate and non-blocking to offer clarity.

---

## 10) Conversion Guardrails

- Exactly one visually dominant primary CTA in each CTA cluster.
- Repeat CTA at 3 points: hero, post-offer-details, conversion section.
- No fake countdown timers or manipulative scarcity claims.
- No fabricated testimonials/review counts.
- Keep form short (name/contact + brief need) unless legally required fields exist.

---

## 11) Accessibility Requirements (Non-negotiable)

- Exactly one `<h1>`.
- Semantic landmarks: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`.
- Visible `:focus-visible` on all interactive controls.
- Contrast minimums:
  - body text >= 4.5:1
  - large text >= 3:1
  - UI controls/focus >= 3:1
- Touch targets `>=44px`.
- Respect `prefers-reduced-motion`.

---

## 12) Performance Rules

- First paint must deliver offer headline + CTA without JS dependency.
- Keep LCP candidate lightweight (text-first hero or optimized media).
- Lazy-load non-critical images.
- Avoid heavy third-party scripts in initial render path.

---

## 13) Mobile QA Criteria (Ship Gate)

At `390x844` and `360x800`:
- [ ] Brand + nav readable without overlap
- [ ] Primary CTA clearly visible near top
- [ ] Hero subcopy remains <= 4 lines
- [ ] No horizontal overflow
- [ ] CTA tap targets >= 44px
- [ ] Conversion section remains understandable without zoom

At `320px`:
- [ ] No clipped buttons/input fields
- [ ] No text collision in header/nav

---

## 14) Do / Don’t

### Do
- Keep the page focused on one offer journey.
- Use explicit next-step language to reduce anxiety.
- Support CTA with concrete proof and guarantee.

### Don’t
- Don’t turn this into a general multipurpose homepage.
- Don’t overload with competing navigation or feature grids.
- Don’t bury form until deep scroll after long prose.

---

## 15) Acceptance Tests

### A) Archetype Integrity
- [ ] First viewport reads as offer funnel, not split hero/bento/editorial/dashboard/map-first.
- [ ] Step/progress cue appears near hero offer.

### B) Conversion Integrity
- [ ] Primary CTA visible at 390x844.
- [ ] Trust strip appears before long content.
- [ ] Conversion form appears with minimal friction.

### C) Accessibility
- [ ] One h1 only.
- [ ] Keyboard tab order logical.
- [ ] Focus visible and contrast compliant.

### D) Responsive
- [ ] No horizontal scroll at 320px/390px.
- [ ] Header/nav/CTA remain clear and tappable.

### E) Performance
- [ ] Hero + CTA render without JS.
- [ ] Non-critical visuals are lazy-loaded.
