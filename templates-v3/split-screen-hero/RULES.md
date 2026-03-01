# Split-Screen Hero RULES.md

**Template scope:** Local service business homepages / landing pages (plumbing, HVAC, roofing, cleaning, landscaping, legal, dental, etc.)

**Goal of this archetype:**
- Communicate service + location + trust in <5 seconds
- Drive primary conversion from above-the-fold (call or form submit)
- Keep visual confidence high without sacrificing speed/accessibility

---

## 0) Research Basis (condensed)

These rules are derived from practical UX/CRO patterns and standards, including:
- **WCAG 2.x / WebAIM contrast guidance:** minimum 4.5:1 for normal text, 3:1 for large text; non-text UI contrast requirements.
- **NN/g scanning behavior (F-pattern):** users scan top/left first; front-load key information and actionable UI.
- **Core Web Vitals guidance (LCP):** hero content is often LCP; optimize hero image/text rendering to hit LCP ≤ 2.5s at p75.
- **Local review behavior studies (e.g., BrightLocal):** trust and review recency/ratings materially influence local service choice.

Use these as non-negotiable constraints for implementation.

---

## 1) Layout System (Split-Screen Hero)

### 1.1 Desktop / large tablet (≥ 1024px)
- Use a **12-column grid** inside a max-width container.
- Hero split:
  - **Left content panel:** 5–6 columns
  - **Right visual panel:** 6–7 columns
- Vertical alignment: center content block relative to hero height.
- Hero min-height: `max(640px, 78vh)` and max-height `900px`.
- Keep left panel readable width: 38–52ch for main copy.

### 1.2 Tablet (768–1023px)
- Shift to **stacked split**:
  - Content first
  - Visual second (or background visual with overlay if necessary)
- Preserve same information hierarchy and CTA order.

### 1.3 Mobile (< 768px)
- Single-column flow only.
- Order:
  1. Eyebrow/service-area line
  2. H1
  3. Supporting copy
  4. Primary CTA
  5. Secondary CTA
  6. Trust row
  7. Image (if not already integrated)
- Do not let image push primary CTA below first viewport on common phones.

### 1.4 Structural requirements
- Hero must include exactly these semantic regions:
  - `header`/hero wrapper
  - primary text group
  - CTA group
  - trust evidence group
  - media group

---

## 2) Spacing Scale & Rhythm

Use an 8px spacing system:
- Tokens: `4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96`

Required spacing rules:
- Eyebrow → H1: `12–16px`
- H1 → support paragraph: `16–24px`
- Support paragraph → CTA row: `24–32px`
- CTA row → trust row: `16–24px`
- Hero top/bottom padding desktop: `64–96px`
- Hero top/bottom padding mobile: `32–56px`

Do not mix arbitrary values (e.g., 13px, 27px) unless design system tokenized.

---

## 3) Typography Hierarchy

### 3.1 Content model
- **Eyebrow:** service category + geography
  - Example: `24/7 Emergency Plumbing • Missoula, MT`
- **H1:** clear offer + audience + location intent
  - Example: `Fast, Licensed Plumbing Repair in Missoula`
- **Support copy (1–2 lines):** response time, guarantee, differentiator
- **CTA labels:** action-first, low ambiguity

### 3.2 Size/line-height targets
- H1 desktop: `clamp(2rem, 4vw, 3.5rem)`; line-height `1.05–1.2`; weight `700–800`
- H1 mobile: `1.75rem–2.25rem`
- Support copy: `1rem–1.25rem`; line-height `1.4–1.6`
- Button text: min `1rem`, weight `600+`

### 3.3 Typographic limits
- H1 max 2 lines desktop, 3 lines mobile.
- Support copy max ~160 characters before wrapping into a second sentence.
- Avoid centered long paragraphs in split layout; left-align for scanability.

---

## 4) Color & Contrast Requirements

Minimum accessibility requirements:
- Body/support text: **≥ 4.5:1** contrast
- Large text (≥24px regular or 18.66px bold): **≥ 3:1**
- Interactive UI components/borders/icons: **≥ 3:1** against adjacent colors
- Focus ring must be clearly visible and not rely on color alone.

Hero-specific rules:
- If text sits over image, use one of:
  - solid scrim overlay (`rgba(0,0,0,0.35+)` equivalent), or
  - gradient overlay beneath text block, or
  - text on solid color panel separated from image.
- Never place small trust text directly on high-detail photo regions.

CTA color rules:
- Primary CTA must be highest visual prominence in hero.
- Secondary CTA must remain clearly interactive but lower emphasis.
- Do not use two equally loud “primary-looking” buttons.

---

## 5) Image / Media Treatment

### 5.1 Content requirements
- Prefer authentic local-service imagery (team, truck, in-field work, real environment).
- Avoid generic stock handshake/office images unless no alternative.
- Show service context relevant to H1 claim.

### 5.2 Composition rules
- Reserve safe area where text overlays (if overlay approach used).
- Subject should not be clipped at key recognition points (face/logo/tool/action).
- Right panel image should support directionality toward CTA/content (gaze/lines pointing inward).

### 5.3 Technical rules
- Provide responsive sources (`srcset/sizes`).
- Use modern formats (AVIF/WebP with fallback).
- Preload only the actual LCP hero asset.
- Set explicit width/height (or aspect-ratio) to avoid CLS.
- Aim hero media payload budget: typically `<= 250KB` compressed for initial render where feasible.

---

## 6) CTA Placement & Copy Rules

### 6.1 CTA architecture
- **Primary CTA** = highest-intent action:
  - `Call Now`, `Get Fast Quote`, `Schedule Service Today`
- **Secondary CTA** = lower-friction alternative:
  - `Check Availability`, `View Services`, `Request Callback`

### 6.2 Placement
- CTA row must appear directly under support copy.
- Desktop: horizontal CTA group (primary first in DOM and visual order).
- Mobile: stacked buttons, primary first.

### 6.3 Copy constraints
- Start with strong verb.
- Keep ≤ 4 words ideal, ≤ 6 max.
- Avoid vague labels (`Submit`, `Learn More`) as primary CTA.
- If promise is speed-based, include time anchor nearby (e.g., `Same-Day Response`).

### 6.4 Click targets
- Minimum touch target: 44x44 CSS px (prefer 48px height).
- Maintain clear hover/active/focus states.

---

## 7) Trust Block Rules (Above-the-Fold)

Include one compact trust row in hero with 2–4 signals max.

Allowed trust items:
- Star rating + review count + source
- Years in business
- License/bonded/insured badges (real only)
- Guarantees/warranty badge
- Local membership/accreditation logos

Trust copy rules:
- Must be specific and verifiable (e.g., `4.9★ from 327 Google reviews`)
- Avoid unverifiable superlatives (`#1 best in town`) unless substantiated.
- Include recency where possible in deeper section, not necessarily in tiny hero row.

Visual rules:
- Keep icons/logos monochrome or low-saturation to avoid competing with primary CTA.
- Trust row should support, not dominate, the conversion path.

---

## 8) Responsive Behavior Rules

### 8.1 Breakpoint behavior
- `>= 1280px`: full split, generous spacing, max readable line length enforced.
- `1024–1279px`: split maintained, tighten gutters.
- `768–1023px`: stacked mode with content-first.
- `<768px`: single column, compressed spacing, persistent conversion visibility.

### 8.2 Must-haves on mobile
- Phone CTA tappable without zoom.
- No text-over-image legibility failures.
- No horizontal scroll.
- Critical trust signals remain visible without excessive scrolling.

### 8.3 Sticky/mobile action pattern (optional but recommended)
- For local services, optional sticky bottom bar:
  - `Call` (primary)
  - `Get Quote` (secondary)
- Must not obscure form fields or cookie banners.

---

## 9) Accessibility Rules (Non-Negotiable)

- One H1 per page hero.
- Use semantic landmarks and accessible name for hero region if needed.
- All CTAs keyboard reachable, visible focus state.
- Decorative media set `alt=""`; informative hero images have meaningful alt.
- Icon-only trust badges require text labels for screen readers.
- Do not rely on color only to indicate links/states.
- Respect reduced-motion preferences for hero animations.
- Any auto-rotating hero content is discouraged; if used, provide pause controls.

---

## 10) Conversion Guardrails

### 10.1 Message clarity
Hero must answer instantly:
1. What service is offered?
2. Where is it offered?
3. Why trust this provider?
4. What should I do next?

If any answer is missing above the fold, hero fails.

### 10.2 Friction limits
- Do not place >2 CTAs in hero row.
- Do not place multi-field forms in split hero unless the business model requires quote-first flows.
- If form exists, max 3 fields in hero (name, contact, need) plus explicit privacy reassurance.

### 10.3 Honesty constraints
- No fake urgency timers.
- No false scarcity language.
- No fabricated ratings/testimonials/logos.

### 10.4 Performance guardrails
- Hero must not block first interaction with heavy JS.
- Avoid autoplay video in hero on mobile.
- LCP target: ≤ 2.5s (p75), CLS < 0.1, INP in “good” range.

---

## 11) DO / DON’T Examples

### Layout
**DO**
- Put offer + location + CTA on left, supporting service image on right.
- Keep first visible viewport focused on one primary action.

**DON’T**
- Split into equally busy left/right panels with competing messages.
- Hide primary CTA below fold on laptop/mobile.

### Copy
**DO**
- `Emergency HVAC Repair in Missoula — Tech at Your Door Today`
- `Call Now` / `Get Same-Day Quote`

**DON’T**
- `Welcome to Our Website`
- `Click Here` / `Submit`

### Trust
**DO**
- `4.9★ from 327 Google reviews`
- `Licensed • Bonded • Insured`

**DON’T**
- `Best Service Ever`
- Badge soup with 10 tiny unreadable logos

### Accessibility
**DO**
- Ensure button text contrast and keyboard focus ring pass checks.

**DON’T**
- Place white 14px text over bright/high-detail image without overlay.

### Performance
**DO**
- Serve compressed hero image with dimensions and preload hint.

**DON’T**
- Load 2MB background video as default hero media.

---

## 12) QA Checklist (Implementation-Ready)

Use this as pre-merge gate. Every item should be pass/fail.

### A. Structure & Content
- [ ] Hero has eyebrow, H1, support copy, CTA group, trust row, media block.
- [ ] H1 states service + local intent clearly.
- [ ] Primary CTA appears above fold at common desktop and mobile sizes.

### B. Visual Hierarchy
- [ ] Primary CTA is visually dominant over secondary CTA.
- [ ] H1 and CTA are the first two focal points in a 3-second glance test.
- [ ] No visual clutter competing with conversion action.

### C. Spacing/Typography
- [ ] Spacing follows 8px token scale.
- [ ] H1 line length and wrapping stay within limits across breakpoints.
- [ ] Body/support copy remains readable (size and line-height).

### D. Contrast/Accessibility
- [ ] Normal text contrast meets 4.5:1 minimum.
- [ ] Large text/UI contrast meets required thresholds.
- [ ] Keyboard navigation and visible focus states verified.
- [ ] Alt text usage is correct (decorative vs informative media).

### E. Responsive
- [ ] No horizontal overflow at 320px width.
- [ ] CTA tap targets meet minimum size.
- [ ] Mobile order preserves conversion sequence (message -> CTA -> trust).

### F. Trust & Credibility
- [ ] Trust claims are specific and verifiable.
- [ ] No fake or unsubstantiated social proof.
- [ ] Trust row supports CTA instead of overpowering hero.

### G. Performance
- [ ] Hero LCP asset optimized and correctly prioritized.
- [ ] No heavy blocking scripts tied to hero render.
- [ ] CLS is controlled (dimensions/aspect ratio set for media).

### H. Conversion Integrity
- [ ] Primary CTA copy is action-specific, not generic.
- [ ] Max 2 hero CTAs.
- [ ] No deceptive urgency/scarcity patterns.

---

## 13) Hand-off Notes for Coding Agents

When implementing this template:
1. Build with tokenized spacing/typography variables (no hardcoded random values).
2. Enforce breakpoint-specific layout behavior exactly as described.
3. Add automated checks where possible:
   - Lighthouse CI (LCP/CLS/INP)
   - axe-core accessibility scan
   - visual regression snapshots at 375, 768, 1024, 1440 widths
4. Keep content slots explicit in component API:
   - `eyebrow`, `headline`, `subcopy`, `primaryCta`, `secondaryCta`, `trustItems[]`, `heroMedia`
5. Reject content payloads that violate constraints (too-long headlines, too many trust items, generic CTA labels).

This file is the source-of-truth for split-screen hero implementation and QA acceptance.