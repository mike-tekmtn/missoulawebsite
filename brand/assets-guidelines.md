# Missoula Website — Assets Guidelines

This document operationalizes the brand kit for designers, content creators, and implementers.

## 1) File & Folder Conventions

Recommended structure:

```text
missoulawebsite/
  brand/
    BRAND-KIT.md
    assets-guidelines.md
  assets/
    logos/
      missoula-logo-full.svg
      missoula-logo-mark.svg
      missoula-logo-wordmark.svg
      missoula-logo-on-dark.svg
      missoula-favicon-32.png
      missoula-favicon-16.png
    icons/
      ui/
      services/
    images/
      hero/
      local-business/
      testimonials/
      textures/
```

Naming rules:
- Use lowercase kebab-case
- Include variant intent (`-on-dark`, `-mono`, `-outline`)
- Avoid vague names like `final2.png`

---

## 2) Logo Asset Specs

### Required exports
- `SVG` (primary master format)
- `PNG` at 1x/2x for non-vector contexts
- Favicon PNG: 16x16 and 32x32

### Safe area
- Minimum clear space around logo = height of the logo mark’s tallest segment × 0.5

### Background handling
- Preferred on light: full-color mark
- On dark photos: use `-on-dark` variant with lighter wordmark
- If contrast fails, place logo on subtle neutral badge/pill

### Do not
- Stretch logo non-proportionally
- Add drop shadows/glows by default
- Recolor outside approved tokens
- Place over highly busy backgrounds without contrast treatment

---

## 3) Color Application Rules

## Functional mapping
- Primary actions: `--color-sky-600`
- Secondary accents: `--color-river-500`
- Trust/grounding accents: `--color-pine-700`
- Highlights/attention: `--color-sun-400`
- Base text: `--color-slate-900` / `--color-slate-700`

## Interaction states (recommended)
- Button hover: darken primary by ~8%
- Button active: darken primary by ~14%
- Focus ring: 2px `--color-river-500` at ~50% alpha

## Color combinations to avoid
- Sun text on white for long copy
- Pine text on sky backgrounds at small sizes
- River + sky used together at equal visual weight in dense UI

---

## 4) Typography Asset Rules

### Font loading strategy
- Prefer variable fonts where available (`Inter`, `Sora`)
- Fallback stack examples:
  - Headlines: `"Sora", "Manrope", "Segoe UI", sans-serif`
  - Body: `"Inter", "Source Sans 3", "Helvetica Neue", Arial, sans-serif`

### Performance
- Limit webfont variants to required weights (typically 400, 600, 700)
- Preload only above-the-fold headline/body faces

### Accessibility
- Minimum body size 16px on desktop and mobile
- Maintain line-height >= 1.5 for paragraph text

---

## 5) Icon Production Guidelines

### Construction
- Base grid: 24px
- Stroke: consistent (1.75px equivalent)
- End caps: rounded
- Joins: rounded

### Export
- SVG only for production pipeline
- Optional PNG fallbacks for docs/presentations

### Quality checks
- Legible at 16px
- No tiny enclosed negative spaces that collapse at small sizes
- Visual weight consistent across icon set

---

## 6) Photography & Image Prep

### Source quality
- Hero images: minimum 2200px wide
- Content section images: minimum 1200px wide
- Testimonials: square crop at 800x800 recommended

### Editing baseline
- Slight cool-neutral white balance
- Preserve realistic skin tones
- Keep saturation moderate
- Avoid excessive clarity/sharpen artifacts

### Crop guidance
- Hero crops should preserve text-safe zone
- Prioritize faces/human activity where present
- Avoid clipping key brand context (storefront signs, mountain horizon)

### Preferred formats
- `AVIF` or `WebP` for modern delivery
- JPEG fallback where needed
- Keep PNG for transparency-only use cases

---

## 7) Voice & Copy Asset Guidelines

### Reusable headline formula
`[Clear business outcome] + [local relevance] + [simple next step]`

Examples:
- “A Website That Makes Missoula Customers Call You First”
- “Modern, Local, and Ready to Launch in Days”

### Reusable CTA formula
`Action verb + ownership pronoun + concrete result`

Examples:
- “Get My Homepage Mockup”
- “Show Me the Redesign”
- “Book My Website Review”

### Microcopy style
- Keep labels plain (“Phone”, “Business Name”, “Best Time to Call”)
- Avoid corporate filler (“enterprise-grade”, “revolutionary”, “synergistic”)

---

## 8) Usage Examples (Quick Reference)

### Example A: Landing hero
- H1: Sora 700, slate-900
- Subcopy: Inter 400, slate-700
- Primary CTA button: sky-600 / white text
- Secondary link: river-500 text + arrow icon
- Image: local storefront or people-in-context, text-safe crop

### Example B: Service feature row
- Icon: rounded-outline sky-600
- Title: Sora 600
- Body: Inter 400 slate-700
- Supporting stat badge: pine-700 with white text

### Example C: Contact card
- Neutral card background (white)
- 1px slate-200 border
- CTA: “Book My 15-Minute Review”
- Optional accent rule: sun-400 top border (2px max)

---

## 9) QA Checklist for New Assets

Before assets are approved:
- [ ] File names follow kebab-case and variant naming
- [ ] Logos include full, mark-only, and dark-background variants
- [ ] Colors use approved token palette
- [ ] Typography pair matches brand kit
- [ ] Icons align to stroke/rounding standards
- [ ] Photos feel local, authentic, and not generic stock
- [ ] CTA copy is action-led and specific
- [ ] Exports include performant modern formats
