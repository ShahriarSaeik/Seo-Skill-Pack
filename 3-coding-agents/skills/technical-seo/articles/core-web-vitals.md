# What Are Core Web Vitals (CWVs) & How To Improve Them

- **Updated**: 2026-10-05

## TL;DR
Core Web Vitals = LCP (visual load), CLS (visual stability), INP (responsiveness; replaced FID March 12, 2024), measured from real Chrome users (CrUX field data) at the 75th percentile. Targets: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1. They're a ranking factor but a tiny one ("tiebreaker") — prioritize UX and conversions, not rankings.

## Framework / Step-by-step
**The 3 metrics & thresholds (Good / Needs improvement / Poor):**
- LCP: ≤2.5s / 2.5–4s / >4s — time to render the largest viewport element (usually hero image or H1; can be img, SVG image, video poster, CSS background, text block)
- INP: ≤200ms / 200–500ms / >500ms — latency across ALL click/tap/keyboard interactions
- CLS: ≤0.1 / 0.1–0.25 / >0.25 — layout shift, measured in the worst 5-second window

**Diagnosis workflow:**
1. Check Search Console Core Web Vitals report (page groups by template — fix template once, fixes all pages in group)
2. PageSpeed Insights for per-page field + lab data (Lighthouse); check LCP element under Diagnostics
3. Chrome DevTools Performance panel (screenshots → find LCP node); WebPageTest filmstrip with "Highlight Layout Shifts" for CLS
4. Lab data (repeatable conditions) for testing fixes; field data (CrUX, 28-day rolling average) is what Google uses

**Improvement playbooks:**
- LCP: prioritize resource loading, shrink files, CDN/closer servers, host resources same server, caching
- CLS: set dimensions on images/videos/iframes/ads, optimize font loading, avoid layout-triggering animations, enable bfcache
- INP: reduce JavaScript, defer JS, break up long tasks, web workers, SSR/prerendering

## Actionable checklist
- [ ] Search Console → Core Web Vitals report → identify failing URL groups
- [ ] Identify LCP element per template (PSI Diagnostics / DevTools)
- [ ] Set width/height (or aspect-ratio) on all images, embeds, iframes, ad slots
- [ ] Preload hero image + fonts; use font-display swaps carefully
- [ ] Audit JS: remove unused, defer non-critical, split long tasks
- [ ] Verify with lab data (Lighthouse) since field data lags 28 days
- [ ] Track desktop AND mobile separately (mobile signals → mobile rankings)
- [ ] Don't over-invest: most pages pass responsiveness (INP) checks; focus on failing templates

## Data points & benchmarks
- LCP good ≤2.5s; INP good ≤200ms; CLS good ≤0.1.
- Field data assessed at 75th percentile — 70% good + 5% poor still = "needs improvement."
- In one older study, only 11.4% of 42M+ pages had CWV metrics associated with them (insufficient data → group/site-level signals used).
- Mobile page experience used for ranking since May 2021; desktop since Feb 2022.
- FID → INP switch: March 12, 2024.
- CrUX = 28-day rolling average; changes take weeks to show in field data.
- Google reps call CWV "tiny ranking factors" / tiebreakers (Gary Illyes, Pubcon 2023).
- AMP no longer required for Top Stories after CWV rollout.

## Mistakes to avoid
- Expecting rankings gains from CWV fixes — impact is minimal unless extremely slow.
- Chasing the Lighthouse score instead of the actual CWV field metrics.
- Testing only lab data and ignoring CrUX field data (or vice versa).
- Forgetting CLS causes: late-loading fonts, JS-injected content, dimensionless embeds.
- Ignoring that data lags 28 days — verify fixes with lab tests.
- Trying to fix CWV without developers — it's complex; work with them.

## Key principles
- CWV is a tiebreaker among 200+ ranking signals; the business case is UX/conversions.
- Fix templates, not individual pages (Search Console groups URLs).
- Field data (CrUX, 75th percentile) is the source of truth for ranking.
- Metrics and thresholds will keep evolving (FID→INP proves it); other metrics may be added.
- Platforms (CMSs, CDNs) are automating more optimizations over time.
