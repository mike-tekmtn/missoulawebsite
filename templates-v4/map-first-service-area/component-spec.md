# Map-First Service Area Component Spec (for Coding Agents)

## 1) Component Contract

**Component name:** `MapFirstServiceAreaHomepage`

**Intent:** Build a local-service homepage where map-based serviceability is the dominant conversion driver.

**Must remain distinct from:**
- split-screen hero
- asymmetric bento
- editorial story
- utility dashboard

---

## 2) Props / Data Schema

```ts
type Cta = {
  label: string;                    // required, 2..36 chars
  href: string;                     // required, relative/http(s)/tel:
  ariaLabel?: string;
};

type NavItem = {
  label: string;                    // required, 1..24 chars
  href: string;                     // required
};

type TrustChip = {
  label: string;                    // required, e.g. "4.9★ from 312 reviews"
  tone?: "neutral" | "positive" | "accent";
};

type CoverageZone = {
  name: string;                     // required, e.g. "Core Zone"
  radiusMiles: number;              // required, 1..100
  etaText: string;                  // required, e.g. "Typically 45–90 min"
  colorHex?: string;                // optional zone highlight
};

type LocalityPin = {
  name: string;                     // required, e.g. "Downtown"
  xPercent: number;                 // required, 0..100
  yPercent: number;                 // required, 0..100
  tier?: "core" | "extended";
};

type MapAsset = {
  src: string;                      // required static map/poster image
  alt: string;                      // required descriptive alt
  width?: number;                   // recommended for CLS control
  height?: number;
  mapsLink?: string;                // optional external map URL
};

interface MapFirstServiceAreaHomepageProps {
  brand: {
    name: string;                   // required
    serviceCategory: string;        // required, e.g. "Mobile Auto Glass Repair"
    location: string;               // required, e.g. "Missoula, MT"
    phone?: string;                 // optional tel:+1...
    phoneDisplay?: string;
  };

  nav: NavItem[];                   // required, 3..6 preferred

  hero: {
    kicker: string;                 // required, service + geo cue
    headline: string;               // required, <=18 words hard cap
    subcopy: string;                // required, <=30 words hard cap
    primaryCta: Cta;                // required (address/service check)
    secondaryCta?: Cta;             // optional (call/text fallback)
    trustChips: TrustChip[];        // required, length 3..5
  };

  mapPanel: {
    title: string;                  // required
    mapAsset: MapAsset;             // required
    zones: CoverageZone[];          // required, length 1..3
    localityPins: LocalityPin[];    // required, length 3..10
    legendText?: string;            // optional
    boundaryNote?: string;          // optional qualifier
    openMapCta?: Cta;               // optional explicit map link
  };

  serviceAreaSection: {
    title: string;                  // required
    intro: string;                  // required
    localities: string[];           // required, min 6 preferred
    disclaimer?: string;            // optional dispatch variability note
  };

  processSection?: {
    title: string;
    steps: Array<{
      label: string;                // e.g. "Step 1"
      heading: string;
      detail: string;
    }>;                             // 3 recommended
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
    mode?: "light" | "dark";    // default light
    canvasHex?: string;             // default #f4f7fb
    inkHex?: string;                // default #102035
    accentHex?: string;             // default #0d6efd
    surfaceHex?: string;            // default #ffffff
    coreZoneHex?: string;           // default #1d4ed8
    extendedZoneHex?: string;       // default #60a5fa
  };

  seo?: {
    title?: string;
    description?: string;
  };
}
```

---

## 3) Validation Rules

### 3.1 Required groups
Required:
- `brand`, `nav`, `hero`, `mapPanel`, `serviceAreaSection`
- `hero.primaryCta`, `mapPanel.mapAsset`

### 3.2 Length and cardinality
- `hero.headline` <= 18 words (hard fail if exceeded)
- `hero.subcopy` <= 30 words
- `hero.trustChips.length` must be 3..5
- `mapPanel.localityPins.length` must be 3..10
- `mapPanel.zones.length` must be 1..3

### 3.3 CTA constraints
- Primary CTA label must be action-specific (avoid `Submit`, `Learn More` as primary).
- Max 2 CTA buttons in any cluster.

### 3.4 URL safety
Reject/sanitize any `javascript:` href.

### 3.5 Accessibility constraints
- Exactly one `<h1>`.
- Map image must have descriptive `alt`.
- All controls include visible `:focus-visible` styles.
- Touch targets >= 44px.

### 3.6 Archetype anti-pattern guards
Fail lint/render if:
- hero is configured as equal 50/50 split with decorative map
- first viewport contains bento-like irregular card matrix
- first viewport is KPI-dense operations board
- first viewport starts with long narrative chapter copy

---

## 4) Deterministic Rendering Rules

1. Render header/nav.
2. Render hero intro with kicker, h1, subcopy, CTA cluster, trust chips.
3. Render dominant map panel in first viewport with zones + locality markers + optional open-map link.
4. Render service-area detail section (localities + radius notes).
5. Render optional process section.
6. Render optional FAQ.
7. Render optional final CTA.
8. Render footer.

**Desktop priority:** map panel occupies majority hero visual weight.

**Mobile priority:** CTA clarity appears before long map content; map remains visible without crowding header.

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
--s-10: 80px;
```

### 5.2 Typography
- Sans UI/body stack
- `--lh-tight: 1.1`
- `--lh-body: 1.58`
- Use `clamp()` for heading scale

### 5.3 Surfaces
- Consistent radius `14-18px`
- Subtle border + shadow separation
- Zone overlays clearly distinguishable with text labels

### 5.4 Buttons
- Primary: filled accent
- Secondary: outline/ghost
- Focus ring: 2px+ high contrast

---

## 6) Accessibility Notes

- Include skip link.
- Use semantic landmarks and heading sequence.
- If map has interactive controls, ensure keyboard access or provide equivalent non-interactive fallback link.
- Do not rely on color-only zone distinctions; add labels.

---

## 7) Conversion Guardrails

- Keep “check address” route above fold.
- Keep phone/text fallback always discoverable.
- Include explicit service boundary note to reduce false expectations.
- Trust chips should support action, not dominate layout.

---

## 8) QA Checklist

### Structure
- [ ] Required sections render in contract order
- [ ] Exactly one h1
- [ ] Map panel present and visually dominant above fold

### Distinction
- [ ] Not split hero
- [ ] Not bento mosaic
- [ ] Not editorial lead
- [ ] Not utility dashboard

### Conversion
- [ ] Primary CTA visible at 390x844
- [ ] Secondary CTA subordinate
- [ ] Coverage info explicit before deep scroll

### Accessibility
- [ ] Focus states visible
- [ ] Touch targets >= 44px
- [ ] Map alt + accessible fallback link present
- [ ] Contrast passes WCAG minimums

### Responsive
- [ ] No horizontal overflow at 320px
- [ ] Locality pins/labels not clipped at mobile widths
- [ ] Header/nav does not obscure hero CTA

### Performance
- [ ] Initial layout works without JS
- [ ] Map asset sized/compressed for fast paint
- [ ] Optional embeds lazy/deferred

---

## 9) Acceptance Tests

### Test A — Archetype Integrity
Given valid props at 1366x768,
when first viewport renders,
then map panel is dominant and user can identify service area path immediately.

### Test B — Mobile CTA Clarity
Given valid props at 390x844,
when page loads,
then primary CTA is visible before deep map details and no horizontal scroll occurs.

### Test C — Accessibility
Given keyboard-only navigation,
when tabbing nav → CTA → map link,
then focus order is logical and each element has visible focus styling.

### Test D — Data Validation
Given `href: "javascript:alert(1)"`,
when component initializes,
then unsafe href is rejected or sanitized.

### Test E — Performance Baseline
Given first load on mid-tier mobile,
when layout paints,
then hero text + map poster render without requiring map JS execution.
