# Utility Dashboard Component Spec (for Coding Agents)

## 1) Component Contract

**Component name:** `UtilityDashboardHomepage`

**Intent:** Render a local-service homepage that behaves like a lightweight operations dashboard with a clear conversion path.

**Must not emulate:**
- Split-screen hero (equal text/media halves)
- Asymmetric bento mosaic hierarchy
- Editorial narrative-first chapter flow above fold

---

## 2) Props / Data Schema

```ts
type Cta = {
  label: string;                     // required, 2..36 chars
  href: string;                      // required, relative/http(s)/tel:
  ariaLabel?: string;
};

type NavItem = {
  label: string;                     // required, 1..24 chars
  href: string;                      // required
};

type KPI = {
  label: string;                     // required, 2..28 chars
  value: string;                     // required, 1..20 chars preferred
  detail?: string;                   // optional, 0..60 chars
  trend?: "up" | "steady" | "down";
};

type QueueItem = {
  area: string;                      // required, e.g. "South Hills"
  jobType: string;                   // required, e.g. "Water heater repair"
  eta: string;                       // required, e.g. "ETA 45 min"
  state: "scheduled" | "en-route" | "pending";
};

interface UtilityDashboardHomepageProps {
  brand: {
    name: string;                    // required
    serviceCategory: string;         // required
    location: string;                // required
    phone?: string;                  // optional tel:+1...
    phoneDisplay?: string;
  };

  nav: NavItem[];                    // required, 3..6 preferred

  masthead: {
    kicker: string;                  // required
    headline: string;                // required, <= 18 words
    subcopy: string;                 // required, <= 28 words
    primaryCta: Cta;                 // required
    secondaryCta?: Cta;              // optional
    trustChips: string[];            // required, 2..5
  };

  statusKpis: KPI[];                 // required, 3..5

  dispatchPanel: {
    statusLabel: string;             // required
    nextWindow: string;              // required
    updatedAt: string;               // required
    channelLabel?: string;           // optional, e.g. "Text + Phone Dispatch"
  };

  queuePanel: {
    title: string;                   // required
    items: QueueItem[];              // required, 3..5
  };

  proofPanel: {
    ratingText: string;              // required, includes rating + volume
    credentials: string[];           // required, 2..4
    guarantee: string;               // required
    testimonial?: {
      quote: string;                 // optional, <= 140 chars
      byline?: string;
    };
  };

  serviceAreaPanel: {
    title: string;                   // required
    localities: string[];            // required, min 3
  };

  faq?: Array<{
    q: string;
    a: string;
  }>;

  finalCta?: {
    headline: string;
    body?: string;
    primaryCta: Cta;
    secondaryCta?: Cta;
  };

  theme?: {
    mode?: "dark" | "light";      // default "dark"
    canvasHex?: string;              // default #0b1220
    surfaceHex?: string;             // default #121c31
    accentHex?: string;              // default #20c997
    warningHex?: string;             // default #ffb020
    textHex?: string;                // default #e9f1ff
  };

  seo?: {
    title?: string;
    description?: string;
  };
}
```

---

## 3) Validation Rules

### 3.1 Required content
- Required: `brand`, `nav`, `masthead`, `statusKpis`, `dispatchPanel`, `queuePanel`, `proofPanel`, `serviceAreaPanel`.
- `statusKpis.length` must be 3..5.
- `queuePanel.items.length` must be 3..5.
- `masthead.trustChips.length` must be 2..5.

### 3.2 Copy and CTA constraints
- `masthead.headline` hard cap 18 words.
- `masthead.subcopy` hard cap 28 words.
- Primary CTA label must be action-oriented.
- Disallow generic primary labels: `submit`, `click here`, `learn more`.
- Maximum 2 buttons per CTA cluster.

### 3.3 Data integrity constraints
- `proofPanel.ratingText` should include both rating and review count.
- Claims must be plausible and specific (no fabricated superlatives).
- Queue `state` controls status badge style; unknown states rejected.

### 3.4 URL safety
- Reject/sanitize `javascript:` URLs in any `href`.

### 3.5 Accessibility constraints
- Exactly one `<h1>` rendered.
- Focus style visible for all interactive controls.
- Minimum touch target ~44px for action controls.
- Contrast meets WCAG thresholds.

### 3.6 Anti-pattern guards
Fail lint/render if any true:
- Desktop hero configured as equal split columns.
- Above fold rendered as irregular bento span mosaic.
- Above fold begins with narrative chapter blocks.

---

## 4) Rendering Specification (Deterministic)

Render order:
1. Top navigation bar
2. Dashboard hero shell
   - Masthead + CTA cluster
   - KPI strip
   - Queue panel
   - Dispatch panel
   - Proof panel
   - Service area mini panel
3. Optional FAQ
4. Optional final CTA band
5. Footer

Desktop layout intent:
- Left side emphasizes masthead/CTA/KPI/queue.
- Right side emphasizes live operations and trust validation.

Mobile layout intent:
- One-column with strict priority order preserving conversion path.

---

## 5) Styling Contract

### 5.1 Spacing tokens
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
```

### 5.2 Typography tokens
- `--font-ui`: sans stack
- `--lh-tight`: 1.12
- `--lh-body`: 1.55
- Use tabular numerals for KPI values when available.

### 5.3 Card/module tokens
- Border radius: `14px–18px`
- Border: low-contrast, visible separation
- Elevation: subtle only, avoid dramatic shadows

### 5.4 Button states
- Primary: filled accent
- Secondary: outline/ghost
- `:focus-visible`: 2px+ high-contrast ring

---

## 6) Accessibility Implementation Notes

- Include skip link (`Skip to main content`).
- Use semantic landmarks and heading sequence.
- Status badges must have text labels (not color only).
- Avoid auto-refreshing content without user control.
- Respect `prefers-reduced-motion` for transitions.

---

## 7) Conversion Guardrails (Implementation)

- Place primary CTA before queue detail block in DOM.
- Keep trust evidence visible in first two viewport heights.
- Avoid more than 5 KPIs above fold.
- Do not bury contact actions in nav only.
- If using phone CTA, use tappable `tel:` link.

---

## 8) Do / Don’t for Implementers

### Do
- Make operational status understandable in seconds.
- Use concise labels and clear visual status tags.
- Keep queue rows structurally consistent.

### Don’t
- Don’t overbuild fake analytics charts.
- Don’t make updates depend on heavy client-side frameworks for core render.
- Don’t convert this into a storytelling article page.

---

## 9) QA Checklist

### Structure
- [ ] Required module order followed.
- [ ] One h1 only.
- [ ] Dashboard shell present in first viewport.

### Archetype distinction
- [ ] No equal split hero.
- [ ] No irregular bento mosaic above fold.
- [ ] No editorial chapter-first layout.

### Conversion
- [ ] Primary CTA visible at 390x844.
- [ ] Secondary CTA subordinate.
- [ ] Trust cues visible early.

### Accessibility
- [ ] Keyboard tab order is logical.
- [ ] Focus states visible.
- [ ] Contrast thresholds pass.
- [ ] Touch targets >= 44px.

### Responsive
- [ ] No overflow at 320px.
- [ ] Queue rows remain readable.
- [ ] KPI cards wrap cleanly.

### Performance
- [ ] Initial layout works without JS.
- [ ] No render-blocking dashboard scripts.
- [ ] Non-critical visuals lazy-loaded.

---

## 10) Acceptance Tests

### Test A — Data Validation
**Given** props where primary CTA href is `javascript:alert(1)`
**When** component initializes
**Then** render fails or href is sanitized to safe fallback

### Test B — Archetype Integrity
**Given** valid props at 1366px width
**When** first viewport renders
**Then** user sees masthead + KPI + dispatch/queue modules
**And** page cannot be described as split hero or bento mosaic

### Test C — Conversion Priority
**Given** valid props
**When** rendered at 390x844
**Then** primary CTA is visible without horizontal scrolling
**And** at least one trust cue appears before deep content

### Test D — Accessibility
**Given** keyboard-only navigation
**When** tabbing through nav + CTAs + queue links
**Then** focus order follows visual reading order
**And** every control shows visible focus indicator

### Test E — Responsive Stability
**Given** viewport 320px
**When** modules stack
**Then** no horizontal scrollbar appears
**And** queue/status labels wrap without clipping
