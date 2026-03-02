# Utility Dashboard Archetype — Implementation Rules

## 1) Purpose + Archetype Definition

This archetype is for local service businesses that want the homepage to feel like a **live operations dashboard** while still converting cold traffic.

**Core idea:** show “we are active, accountable, and available now” through operational signals (response times, active jobs, coverage, dispatch certainty), then route users to one primary conversion action.

Use for: plumbing, HVAC, electrical, restoration, pest, towing, garage doors, home services with urgent/operational buying intent.

---

## 2) Distinction Requirements (Materially Different)

To pass archetype integrity, the first viewport must read as a **command center**, not a hero story.

### 2.1 Must NOT become split-screen
- Do not use a persistent 50/50 text-image hero lockup.
- Do not place one giant image panel opposite one giant text panel.

### 2.2 Must NOT become asymmetric bento
- Do not use decorative card mosaic/span-driven composition as primary pattern.
- No irregular card sizes with artistic asymmetry as hierarchy driver.

### 2.3 Must NOT become editorial story
- Do not lead with long narrative chapters.
- Do not rely on prose progression as the primary above-fold information architecture.

### 2.4 Utility Dashboard signature
- Include a **status rail** (KPI chips/cards), an **action panel**, and a **queue/dispatch panel** in first viewport.
- Hierarchy is driven by **operational clarity + conversion controls**, not image drama.
- Text is concise, system-like, and scannable.

---

## 3) Research Basis (Condensed)

Rules align with practical CRO/UX evidence:
- Scanning-first behavior: users decide quickly from top status cues + clear CTA.
- Trust in local services improves with specific, verifiable operational claims (review counts, response windows, coverage).
- Reduced uncertainty improves action rate: explicit ETA/availability and next-step clarity.
- WCAG contrast/focus and touch target standards are mandatory.
- Core Web Vitals: dashboard-like pages must avoid script-heavy widgets that delay first interaction.

---

## 4) Layout Mechanics

### 4.1 Container + grid
- Max width: `1240px`.
- Horizontal padding: `16px` mobile, `24px` tablet, `32px` desktop.
- Desktop layout: 12-column grid.
- Primary dashboard shell (desktop):
  - Left command column: 7 columns (headline, CTA, trust, queue)
  - Right operations column: 5 columns (dispatch panel, proof panel, coverage panel)

### 4.2 Required above-fold modules
1. Utility masthead (service + location + H1 + concise subcopy)
2. Primary action cluster (primary + secondary CTA)
3. Status KPI strip (3-5 items)
4. Dispatch/availability panel
5. Queue/jobs snapshot panel
6. Trust evidence micro-panel

### 4.3 Reading order
1. Brand + nav
2. H1 + availability promise
3. Primary CTA
4. KPI strip
5. Dispatch + queue details
6. Trust proof + service area

### 4.4 Breakpoints
- Mobile: `< 768px`
- Tablet: `768–1023px`
- Desktop: `>= 1024px`

### 4.5 Reflow rules
- Mobile stacks by conversion priority (masthead → CTA → KPI → dispatch → queue → trust).
- Tablet uses 6-column adaptation with dispatch and queue stacked.
- Desktop uses two-column dashboard shell, no equal split.

---

## 5) Hierarchy + Information Density

### 5.1 Priority levels
- **Level A (dominant):** primary value statement + primary CTA + immediate availability statement.
- **Level B:** KPI strip + dispatch panel.
- **Level C:** queue details, trust badges, service area support.

### 5.2 Copy limits (strict)
- H1: <= 14 words preferred, hard cap 18.
- Subcopy: <= 28 words.
- KPI labels: 2-4 words.
- KPI values: <= 14 characters where possible.
- Queue line items: <= 8 words per row.

### 5.3 Density guardrail
- Above fold total text block (excluding nav): target <= 95 words.
- No long paragraphs in dashboard modules.

---

## 6) Spacing, Rhythm, and Surfaces

Use 8px baseline tokens only:
`4, 8, 12, 16, 24, 32, 40, 48, 64, 80`

Rules:
- Module padding: `20px` mobile, `24px` desktop.
- Module gap: `16px` mobile, `20px` desktop.
- Border radius: `14–18px`, consistent across dashboard cards.
- CTA row gap: `10–12px`.
- Section vertical spacing: `40–72px`.

No arbitrary one-off spacing values unless tokenized.

---

## 7) Typography

### 7.1 Type stack
- Single modern sans stack (Inter/Manrope/system-ui equivalent) for dashboard clarity.
- Numeric values can use tabular numerals where available.

### 7.2 Scale
- H1: `clamp(2rem, 4vw, 3.4rem)`, line-height `1.05–1.15`, weight `750–800`.
- H2/module titles: `1.05rem–1.35rem`, weight `650–720`.
- Body: `0.98rem–1.05rem`, line-height `1.45–1.6`.
- KPI value: `1.15rem–1.55rem`, weight `700+`.
- Meta labels: `0.78rem–0.9rem`.

### 7.3 Content tone
- Operational, specific, local.
- Avoid hype language; prefer measurable statements.

---

## 8) Palette, Contrast, Visual System

### 8.1 Palette roles
- Background canvas: dark-slate or light-neutral with subtle elevation layers.
- Surface layers: 2-3 tones max.
- One primary accent for CTA and active states.
- One support color for status (e.g., success/available).

### 8.2 Contrast rules
- Body text >= 4.5:1.
- Large text >= 3:1.
- Non-text UI indicators and borders >= 3:1.
- Focus ring must be obvious on all surfaces.

### 8.3 Noise control
- No heavy gradients behind dense data text.
- No animated charts that distract from CTA.
- Keep iconography minimal and legible.

---

## 9) Data Card Strategy

### 9.1 KPI strip (required)
Must include 3-5 KPI cards/chips above fold. Recommended set:
- Average callback time
- Jobs completed this month
- Verified rating + review count
- Coverage / service area count
- First-visit fix rate (if truthful)

### 9.2 Dispatch panel (required)
Include:
- Current status (e.g., “Dispatch board: Live”)
- Next available window
- “Last updated” timestamp style line (can be static text placeholder in template)

### 9.3 Queue panel (required)
Include 3-5 queue rows:
- Neighborhood/area
- Service type
- ETA/status tag

### 9.4 Data integrity
- Values must be plausible and non-deceptive.
- Mark sample/demo values clearly in code comments when template data is mock.

---

## 10) CTA + Trust Placement

### 10.1 CTA hierarchy
- Primary CTA required above fold in masthead module.
- Secondary CTA optional, lower emphasis.
- Do not render more than 2 CTA buttons in any cluster.

### 10.2 CTA copy
- Action-first, specific:
  - “Get My Fast Estimate”
  - “Call Dispatch Now”
- Avoid generic primary labels (`Submit`, `Learn More`, `Click Here`).

### 10.3 Trust placement
Above fold include at least 3 trust cues across modules:
- Rating + review volume
- Licensed/insured
- Warranty/guarantee or years in business

### 10.4 Friction rules
- Phone link must be touch-friendly (`>=44px` height).
- Conversion path should not require account creation.

---

## 11) Responsive Behavior + Interaction

- Ensure primary CTA appears in initial view at `390x844` where practical.
- No horizontal overflow at `320px`.
- No hover-only critical content.
- Keep queue rows readable on small screens (wrap/stack tags as needed).
- Optional sticky mobile action bar allowed if it does not obstruct content/forms.

---

## 12) Accessibility Requirements (Non-negotiable)

- Exactly one `<h1>`.
- Landmarks: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`.
- Logical heading order.
- Keyboard reachable controls with visible `:focus-visible`.
- Meaningful text labels for status chips/icons.
- Respect `prefers-reduced-motion`.
- Use ARIA only when native semantics are insufficient.

---

## 13) Conversion Guardrails

- Do not bury CTA under dense data blocks.
- Keep one dominant primary action per viewport region.
- No fake urgency/scarcity timers.
- No fabricated ratings/testimonials/certifications.
- If “fast estimate” is promised, keep path short and obvious.

---

## 14) Do / Don’t

### Do
- Show concrete ops clarity: callback time, active window, coverage.
- Keep modules compact with clear labels.
- Tie trust to specific numbers and credentials.
- Use dashboard visual language without requiring user interpretation.

### Don’t
- Don’t emulate a card-mosaic bento artboard.
- Don’t switch to long editorial storytelling above fold.
- Don’t use image-first composition that weakens utility cues.
- Don’t overwhelm with more than 5 KPIs in first viewport.

---

## 15) QA Checklist (Ship Gate)

### Structure + Archetype
- [ ] First viewport reads as utility dashboard command center.
- [ ] Not split-screen, not bento mosaic, not editorial chapter lead.
- [ ] Required modules (masthead, CTA, KPI, dispatch, queue, trust) present.

### Conversion
- [ ] Primary CTA visible and dominant above fold.
- [ ] Secondary CTA visually subordinate.
- [ ] At least 3 trust cues visible by end of second viewport.

### Content + Data
- [ ] KPI labels/values concise and scannable.
- [ ] Queue and dispatch details understandable in <5 seconds.
- [ ] Claims are specific and believable.

### Accessibility
- [ ] One h1 only.
- [ ] Focus states obvious and keyboard flow correct.
- [ ] Contrast targets pass.
- [ ] Touch targets >= 44px.

### Responsive + Performance
- [ ] No horizontal scroll at 320px.
- [ ] Module stack order preserves conversion priority.
- [ ] Core layout works without JS.
- [ ] No heavy, render-blocking dashboard scripts.

If any critical item fails, block release.

---

## 16) Reference Content Schema (Contract)

```ts
interface UtilityDashboardHomepage {
  brand: {
    name: string;
    serviceCategory: string;         // e.g. "Emergency Plumbing"
    location: string;                // e.g. "Missoula, MT"
    phone?: string;                  // tel link, E.164 preferred
    phoneDisplay?: string;
  };

  nav: Array<{ label: string; href: string }>;

  masthead: {
    kicker: string;                  // service + location cue
    headline: string;                // required
    subcopy: string;                 // concise value statement
    primaryCta: { label: string; href: string };
    secondaryCta?: { label: string; href: string };
    trustChips: string[];            // 2..5 items
  };

  kpis: Array<{
    label: string;
    value: string;
    detail?: string;
  }>; // 3..5

  dispatch: {
    statusLabel: string;             // e.g. "Dispatch board: Live"
    nextWindow: string;              // e.g. "Next arrival window: 11:30–1:00"
    updatedAt: string;               // e.g. "Updated 4 minutes ago"
  };

  queue: Array<{
    area: string;
    jobType: string;
    eta: string;
    state: "scheduled" | "en-route" | "pending";
  }>; // 3..5 rows

  proofPanel: {
    ratingText: string;              // e.g. "4.9★ from 312 reviews"
    credentials: string[];           // e.g. ["Licensed", "Insured"]
    guarantee: string;               // e.g. "2-year workmanship guarantee"
  };

  serviceArea: {
    title: string;
    localities: string[];            // min 3
  };

  faq?: Array<{ q: string; a: string }>;

  finalCta?: {
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
- [ ] At desktop width, above fold contains KPI strip + dispatch + queue modules.
- [ ] No equal 50/50 split hero lockup.
- [ ] No irregular bento card mosaic as primary composition.

### B) Conversion Integrity
- [ ] Primary CTA is visible at 390x844.
- [ ] Primary CTA appears before any long explanatory section.
- [ ] Trust proof appears before or alongside dispatch modules.

### C) Accessibility
- [ ] Exactly one h1.
- [ ] Keyboard focus order matches visual order.
- [ ] `:focus-visible` passes visual prominence check.
- [ ] Text + control contrast pass thresholds.

### D) Responsive
- [ ] No horizontal overflow at 320px and 390px.
- [ ] Queue rows remain legible and do not clip.
- [ ] Touch target minimums met on nav and CTAs.

### E) Performance
- [ ] No JS dependency for initial module layout.
- [ ] Non-critical visuals lazy-loaded.
- [ ] LCP candidate (headline/hero image if present) optimized and fast.
