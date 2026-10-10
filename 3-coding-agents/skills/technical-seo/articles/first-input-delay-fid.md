# Improving First Input Delay (FID): Faster Interactions

- **Updated**: 2026-10-05

## TL;DR
FID measured the delay between a user's first interaction (click, tap, key input) and the page's response. It was replaced by Interaction to Next Paint (INP) as a Core Web Vital on March 12, 2024 — but the fixes are identical: reduce JavaScript, load it later, break up long main-thread tasks. Most sites already pass responsiveness checks; focus only on failing templates.

## Framework / Step-by-step
**What causes delay:** JavaScript competes for the browser's single main thread (a one-burner stove). While a long task runs, the page can't respond to input; longer task = longer delay. Worse on slower devices.

**The 5 fixes:**
1. **Reduce JavaScript** — especially early-load JS piling onto the main thread; delete before optimizing.
2. **Load JS later** — use `async` (download parallel with parsing; blocks only during execution — good for analytics and scripts needed early) or `defer` (no parse blocking; executes after HTML parsing — for everything not needed immediately).
3. **Break up long tasks** — code splitting into smaller chunks so the thread frees up between tasks and input can be handled.
4. **Use web workers** — move JS off the main thread to a worker (trade-offs: no DOM access, caching considerations; needs a competent developer).
5. **Prerender or SSR** — shift rendering work from the browser to the server on JS-framework sites.

**Measurement:**
- Only real-user (field) data counts for the vital itself; good = 75% of interactions under 100 ms.
- Lab tests can't measure FID (they never click) — use Total Blocking Time (TBT) as the proxy; improving TBT improves FID/INP.
- Search Console groups failing URLs by template; fix the template once to fix the whole group.

## Actionable checklist
- [ ] Check Search Console CWV report before optimizing — most sites pass; don't fix what isn't failing
- [ ] Audit early-load JavaScript; remove what's unused
- [ ] Tag scripts: async for early/dependent (analytics), defer for the rest
- [ ] Split long tasks / large bundles via code splitting
- [ ] Move heavy computation to a web worker where feasible
- [ ] Consider SSR/prerendering for JS-heavy templates
- [ ] Track TBT in lab tests as the FID/INP proxy
- [ ] Re-check field data after the 28-day CrUX window

## Data points & benchmarks
- Historical FID thresholds (retired metric): good ≤100 ms / needs improvement 100-300 ms / poor >300 ms (75th percentile of real-user interactions).
- 95.3% of sites were already in the good FID bucket as of April 2023 (older figure).
- One Core Web Vitals study found almost no one needed to worry about FID on desktop, and very few on mobile, even on slow connections.
- FID → INP swap: March 12, 2024 (INP covers ALL interactions, not just the first).

## Mistakes to avoid
- Investing in FID fixes without checking field data first — the problem is rare.
- Optimizing only the first interaction and ignoring later ones (that's why INP replaced FID).
- Using async on scripts with unmet dependencies, or defer on scripts needed immediately.
- Hand-rolling web workers without developer support.

## Key principles
- One main thread: every millisecond of long JS is a millisecond of unresponsiveness.
- TBT (lab) and FID/INP (field) improve together — reduce main-thread blocking.
- The FID→INP transition raised the bar: all interactions now count, so long-task hygiene matters more.
