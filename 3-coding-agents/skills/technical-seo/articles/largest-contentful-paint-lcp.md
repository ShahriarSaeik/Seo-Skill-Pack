# What Is Largest Contentful Paint (LCP) & How To Improve It

- **Updated**: 2026-10-05

## TL;DR
LCP measures how long the largest visible viewport element (usually the hero image or H1 text block) takes to render. Good = ≤2.5s at the 75th percentile of real-user loads. It's the Core Web Vital sites struggle with most — mobile and slow connections make the threshold nearly impossible without deliberate optimization. The playbook: identify the LCP element, then prioritize, shrink, move closer, and cache the resources it needs.

## Framework / Step-by-step
**What counts as the LCP element:** `<img>`, SVG image, video poster frame, CSS `url()` background image, or block-level text. Elements outside the viewport don't count.

**Improvement steps:**
1. **Find your LCP element** — page speed reports list it under Diagnostics; filter issues by LCP.
2. **Prioritize the critical rendering path** — load LCP-element resources and above-the-fold assets first; defer everything else.
   - Images early: delete if unneeded; compress; `fetchpriority="high"`, Early Hints, and/or preload (with imagesrcset for responsive images).
   - Images late: `loading="lazy"` — never on above-the-fold images.
   - CSS early: minify, remove unused, inline critical CSS into the HTML.
   - CSS late: preload non-critical stylesheets and apply via `onload`.
   - Fonts: preload (good) → `font-display: optional` + preload (better) → system font (best — nothing to load).
   - JS early: inline or preload only what above-the-fold content needs; prerender/SSR on frameworks.
   - JS late: `async` for early/dependent scripts (analytics), `defer` for the rest.
3. **Make files smaller** — tree-shake unused code; compress everything (server/CDN-level).
4. **Serve files closer** — use a CDN (server copies near users).
5. **Host resources on the same server** — avoids extra connection handshakes; otherwise use `preconnect`/`dns-prefetch` (dns-prefetch has broader support).
6. **Cache aggressively** — long cache lifetimes, purged on change; cache at the CDN too.
7. **Emerging extras** — speculative prerendering, signed exchanges, HTTP/3.

**Measurement:** field data (real users, 28-day rolling) is what counts; lab data diagnoses. Search Console buckets failing URLs into template groups — fix once per template.

## Actionable checklist
- [ ] Identify the LCP element per failing template
- [ ] Add `fetchpriority="high"` / preload to the hero image; compress and size it correctly
- [ ] Lazy-load below-the-fold images only
- [ ] Inline critical CSS; defer the rest via preload + onload
- [ ] Pick a font strategy (system > optional display > preload)
- [ ] Compress all assets; tree-shake unused JS/CSS
- [ ] Put the site + critical assets behind a CDN
- [ ] Add preconnect/dns-prefetch for required third-party origins
- [ ] Set long cache headers with change-triggered purges
- [ ] Verify with lab tests; field data lags 28 days

## Data points & benchmarks
- LCP thresholds: good ≤2.5s / needs improvement 2.5-4s / poor >4s (75th percentile).
- 57.1% of sites achieved good LCP site-wide in April 2023 (older figure) — the hardest vital to pass.
- Mobile LCP is markedly worse than desktop; the threshold is nearly unreachable on slow connections without optimization.
- Many sites pass just by adding Early Hints/preloads for the main image, stylesheets, and fonts.

## Mistakes to avoid
- Lazy-loading above-the-fold (especially the LCP) image.
- Fixing many reported issues but seeing no LCP gain — dependencies and conflicting priorities can mask wins; retest iteratively.
- Inlining ALL CSS/JS (only the critical subset).
- Ignoring connection overhead from scattered third-party asset hosts.

## Key principles
- LCP = perceived load speed; the biggest element is almost always the lever.
- Optimize the critical rendering path: earliest possible discovery + fastest delivery of one element.
- Fix templates, not individual URLs.
