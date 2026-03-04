# Missoula Website — Brand Kit

## 1) Brand Core

**Brand name (working):** Missoula Website  
**Positioning:** A modern, local-first web presence that feels as grounded and welcoming as Missoula itself—outdoor energy, creative culture, and practical clarity.  
**Brand promise:** We make local businesses look credible fast, without sounding generic.

**Personality traits:**
- Grounded
- Friendly
- Capable
- Creative
- Clean

---

## 2) Logo Direction

## Concept Direction: **"River + Ridge"**
Missoula is defined by valleys, water, and mountain contours. The logo should abstract these without becoming clip-art.

### Primary mark
- A custom monogram or symbol combining:
  - one flowing curve (river/current)
  - one angular contour (ridge/peak)
- Should work as:
  - full lockup (symbol + wordmark)
  - symbol-only favicon/social avatar

### Wordmark style
- Lowercase or mixed-case sans-serif wordmark for approachability.
- Tight tracking not required; prioritize readability at small sizes.

### Prohibitions
- No literal mountain stock icon
- No script fonts in the logo
- No over-detailed linework that disappears at 24px

### Minimum sizes
- Full lockup min width: **140px**
- Symbol-only min size: **20px**

---

## 3) Color System (Design Tokens)

These tokens are intended for CSS variables and design tooling.

```css
:root {
  --color-sky-600: #2563EB;   /* Primary brand blue */
  --color-pine-700: #14532D;  /* Deep natural accent */
  --color-river-500: #06B6D4; /* Secondary interactive accent */
  --color-sun-400: #FBBF24;   /* Warm highlight */

  --color-slate-900: #0F172A; /* Primary text */
  --color-slate-700: #334155; /* Body text */
  --color-slate-200: #E2E8F0; /* Borders/subtle UI */
  --color-mist-50: #F8FAFC;   /* Surface */
  --color-white: #FFFFFF;

  --color-success: #16A34A;
  --color-warning: #D97706;
  --color-error: #DC2626;
}
```

### Usage ratio
- 60% neutrals (mist/slate/white)
- 25% primary blue
- 10% pine + river accents
- 5% sun highlight (sparingly)

### Accessibility
- Body text should meet WCAG AA minimum (4.5:1).
- Use `--color-slate-900` on light surfaces as default.
- Yellow/sun color should not be used for body text on white.

---

## 4) Typography

## Primary pairing (recommended)
- **Headlines:** `Sora` (600–700)
- **Body/UI:** `Inter` (400–600)

## Alternative pairing
- **Headlines:** `Manrope`
- **Body/UI:** `Source Sans 3`

### Type scale (web)
- H1: 48/56
- H2: 36/44
- H3: 28/36
- H4: 22/30
- Body L: 18/30
- Body: 16/26
- Small: 14/22

### Rules
- Avoid more than 2 families per page.
- Keep line lengths around 60–80 characters for readability.
- Headline case: sentence case preferred over all caps.

---

## 5) Icon Style

- Style: **rounded-outline with selective duotone fills**
- Stroke: 1.75px equivalent at 24px grid
- Corner radius: soft, geometric
- Visual language: maps, location pin, compass cues, device/browser, checkmarks
- Avoid skeuomorphic or 3D icon packs

### Icon color rules
- Default: `--color-slate-700`
- Active/highlight: `--color-sky-600`
- Success states: `--color-success`

---

## 6) Imagery & Photography Direction

### Subject focus
- Real Missoula-feeling scenes: downtown storefronts, trailside community moments, riverside light, local makers
- Authentic business owners and customers, not staged corporate stock smiles

### Visual treatment
- Natural light preferred
- Slightly cool-neutral grade with warm skin tones
- Moderate contrast, avoid heavy HDR
- Include environmental context (mountains/trees/streets) where possible

### Composition
- 70% candid/documentary
- 30% composed brand storytelling
- Reserve negative space in hero imagery for text overlays

### Don’ts
- No generic skyline stock from unrelated cities
- No overly saturated travel-poster editing
- No clichéd handshake-only business shots

---

## 7) Voice & Tone

## Voice pillars
1. **Local-smart**: Knows the market without sounding exclusive.
2. **Clear-first**: Simple language, no jargon stacking.
3. **Confident-helpful**: Direct recommendations, no hype.

## Tone by context
- **Homepage:** welcoming + credible
- **Service pages:** practical + results-oriented
- **Contact/CTA:** low-friction + encouraging

### Copy examples
- Instead of: “Leverage synergistic digital ecosystems.”
- Use: “Get a site that looks sharp, loads fast, and helps people call you.”

- Instead of: “Best-in-class solutions for every vertical.”
- Use: “Built for Missoula businesses that need clarity, not complexity.”

---

## 8) CTA Language

### Primary CTA patterns
- **“Get My Free Homepage Mockup”**
- **“See Your Site Redesign”**
- **“Book a 15-Minute Website Review”**

### Secondary CTA patterns
- “View Sample Layouts”
- “Compare Before & After”
- “Ask a Quick Question”

### CTA style rules
- Lead with action verbs.
- Prefer first-person for high-intent buttons (“Get My…”, “Show Me…”).
- Keep to 3–6 words whenever possible.

---

## 9) Component-Level Usage Examples

### Hero section
- Headline in Sora 700, slate-900
- Subhead in Inter 400, slate-700
- Primary button: sky-600 background + white text
- Secondary button: white background + sky-600 border/text
- Background: mist-50 with optional topographic line texture at low opacity

### Card modules
- White card on mist background
- 1px border slate-200
- Icon at top in sky-600 or slate-700
- CTA text link in sky-600 with subtle hover underline

### Testimonials
- Use portrait or local environment thumbnail
- Quote text in slate-900
- Business name in pine-700 to introduce subtle local accent

---

## 10) Brand Consistency Checklist

Before publishing any page, verify:
- [ ] Uses approved color tokens only
- [ ] Headline and body fonts match kit
- [ ] Icons match rounded-outline style
- [ ] Photography feels local/authentic
- [ ] CTA language is specific and action-led
- [ ] No generic/template-sounding copy remains
