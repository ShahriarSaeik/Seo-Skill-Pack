# What Is Cumulative Layout Shift (CLS) & How To Improve It

- **Updated**: 2026-10-05

## TL;DR
CLS measures visual stability: how much visible content moves during load (scored over the worst 5-second window; shifts within 500 ms of user input are excluded). Good = ≤0.1 at the 75th percentile. Most shifts come from dimensionless images/embeds/ads, late-loading fonts, JS-injected content, and layout-triggering animations — all cheap to fix with space reservation and transform animations.

## Framework / Step-by-step
**The formula:** layout shift score = (% of viewport affected) × (distance moved by unstable elements).

**The 4 fixes:**
1. **Reserve space for images, videos, iframes, ads** — set width/height (or CSS aspect-ratio) on every media element; use width/height with srcset for responsive images; reserve maximum space for dynamic ad slots so the placeholder never grows.
2. **Optimize fonts** — font swaps cause invisible/unstyled text flashes (FOIT/FOUT). Best: system fonts. Otherwise: preload + `font-display: optional` — the font either loads in a brief window or the default font renders this visit (custom font appears on subsequent loads from cache).
3. **Animate without layout changes** — never animate `top`, `left`, `box-shadow`, `box-sizing`, etc.; use `transform` animations instead.
4. **Qualify for back/forward cache (bfcache)** — instant reloads with zero shifts. Requirements: never use the `unload` event, minimize `Cache-Control: no-store`, refresh stale data after bfcache restore, avoid `window.opener` ops, close open connections on navigation, and test cacheability.

**Measurement:** field data (real users, 28-day window) is the ranking input; lab tests diagnose causes ("Avoid large layout shifts" diagnostics identify culprits). Search Console groups failing URLs by template.

## Actionable checklist
- [ ] Add width/height or aspect-ratio to every image, video, iframe, and embed
- [ ] Reserve max-size slots for ads and dynamically injected embeds
- [ ] Choose font strategy: system font, or preload + font-display: optional
- [ ] Convert layout-triggering animations to transform-based ones
- [ ] Audit JS that injects content above existing content; reserve its space
- [ ] Verify bfcache eligibility (no unload handlers, careful no-store, close connections)
- [ ] Fix templates via Search Console URL groups, not page-by-page

## Data points & benchmarks
- CLS thresholds: good ≤0.1 / needs improvement 0.1-0.25 / poor >0.25.
- 72.8% of sites achieved good CLS in April 2023 (older figure) — the most improved Core Web Vital at the time.
- CLS is similar across desktop and mobile, but worse on slower connections.
- Page-level CLS is worse than origin-level — teams fix high-traffic pages and leave the long tail failing.

## Mistakes to avoid
- Shipping images/embeds without dimensions (the #1 shift cause).
- Using font-display: swap on late-loading fonts — a likely visible jump.
- Animating layout properties instead of transforms.
- Assuming origin-level "good" means every page passes — audit at page/template level.
- Breaking bfcache with unload listeners or blanket no-store headers.

## Key principles
- CLS is about user trust: misclicks from shifting layouts (especially onto ads) destroy UX.
- Space reservation solves most shifts — dimensions are the cheapest fix in all of CWV.
- Exclude user-initiated shifts from worry; only uninstructed movement counts.
