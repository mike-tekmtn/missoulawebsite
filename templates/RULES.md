TASK DESCRIPTION
Build a modern, responsive website template based on intake-form data.

GOAL
Create a premium, trustworthy, conversion-focused site that feels local and relevant to the submitted business type. Use intake data to drive content, sections, and CTA priorities.

INTAKE-FIRST CONTENT RULES (REQUIRED)
Always tailor output from intake fields such as:
- businessName
- businessType
- contactName / email / phone
- timeline
- pageCount
- copywriting
- features[]
- notes
- template (if provided)

TECH STACK
Default template output should be framework-agnostic HTML/CSS/JS unless a specific stack is requested.
If stack is specified by intake or project context, follow that stack.

STYLE & VISUAL DIRECTION
- Clean, modern, premium UI
- Strong readability and clear hierarchy
- Profession-relevant imagery and icons
- Consistent spacing and responsive behavior
- Accessible semantic HTML and keyboard-friendly interactions

PAGE STRUCTURE (BASELINE)
Build at least these pages/sections (or equivalent within requested page count):

1) NAVBAR
- Brand/logo based on business name and brand direction
- Links: Home, Services, About, Contact (adjust if intake needs differ)
- Sticky behavior optional if it improves UX
- Mobile menu required

2) HERO
- Headline derived from intake + business type
- Subheadline aligned to value proposition and local positioning
- Primary CTA from business goal (quote, consultation, booking, call)
- Supporting visual relevant to profession

3) TRUST / PROOF
- Testimonial placeholders, badges, or credibility blocks
- Local relevance where appropriate

4) SERVICES / OFFERS
- Service cards based on businessType and notes
- Feature emphasis based on intake features[]

5) PROCESS / HOW IT WORKS
- 3-step or 4-step process aligned to the business workflow

6) CTA BAND
- Clear next action
- Contact method consistency (form/call/email)

7) FAQ
- 4–8 common questions tied to business context

8) FOOTER
- Useful links
- Contact details
- Social placeholders/links
- Legal/support links

INTERACTION REQUIREMENTS
- Subtle, purposeful animations only
- Optional scroll reveal and micro-interactions
- Respect reduced-motion preferences

ACCESSIBILITY REQUIREMENTS
- Semantic landmarks: header/main/section/footer
- Visible focus states
- Keyboard navigable menus/accordions
- Sufficient color contrast
- Proper labels/aria attributes for interactive controls

CODE QUALITY REQUIREMENTS
- Clean component/section structure
- Minimal duplication
- Clear naming
- No irrelevant hardcoded domain content
- Keep template easy to adapt to future intake submissions

CONTENT TONE
Professional, concise, human, conversion-oriented.
Write like a real local business website for the provided intake.

ANTI-PATTERNS (DO NOT)
- Reuse unrelated niche content (e.g., food delivery) for other professions
- Use mismatched visuals/icons for the business type
- Output generic filler without intake alignment
- Force extra sections when pageCount/timeline imply a simpler launch

EXAMPLE INTAKE → OUTPUT MAPPING

Example A (local contractor):
- businessName: Peak Roofing
- businessType: roofing contractor
- pageCount: 4-6
- features: [contact-form, booking]
- timeline: one-day

Expected output:
- Archetype: utility-dashboard or map-first (not editorial)
- Pages: home/services/about/contact (+ optional service-area)
- CTA language: “Request Estimate”, “Schedule Roof Inspection”
- Trust blocks: license/insurance, review highlights, response times
- Visuals/icons: roofing, inspection, safety, construction context

Example B (law firm):
- businessName: Granite Legal Group
- businessType: law firm
- pageCount: 4-6
- features: [contact-form]
- timeline: this-week

Expected output:
- Archetype: editorial-story
- Pages: home/practice areas/about/contact
- CTA language: “Book Consultation”, “Discuss Your Case”
- Trust blocks: credentials, years practicing, client communication process
- Visuals/icons: legal/professional context, restrained style

Example C (fitness coach):
- businessName: Forge Method Coaching
- businessType: fitness coach
- pageCount: 1-3
- features: [booking, payments]
- timeline: one-day

Expected output:
- Archetype: offer-funnel-landing
- Pages/sections: strong home funnel + contact/signup
- CTA language: “Start Program”, “Apply Now”
- Trust blocks: transformations, testimonials, progress methodology
- Visuals/icons: coaching, training, energetic but clear design
