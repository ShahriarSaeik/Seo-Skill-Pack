# Page Speed Reports for SEOs & Developers (Field + Lab Data)

- **Updated**: 2026-10-05

## TL;DR
The standard free page-speed report combines two data types: field data (real-user experience, 28-day rolling average, 75th percentile — what rankings use) and lab data (a controlled Lighthouse-style test that pinpoints causes). Use field data to decide what to fix, lab data to diagnose and verify fixes — and never confuse the performance score with Core Web Vitals pass/fail.

## Framework / Step-by-step
**Reading the report:**
1. **Field data (real users)** — Core Web Vitals pass/fail per URL or whole origin; a metric is "good" only if 75% of experiences hit the threshold. Also shows FCP, INP, TTFB distributions.
2. **Lab data (simulated test)** — 0-100 performance score plus metrics. No FID/INP (needs real input); use Total Blocking Time (TBT) as the lab proxy.
3. **Diagnostics** — Opportunities/Diagnostics sections identify the LCP element, CLS culprits, and main-thread blockers; filter issues by target metric; treemap view exposes unused code bytes.

**Thresholds (good / needs improvement / poor):**
- LCP: ≤2.5s / 2.5-4s / >4s
- INP: ≤200ms / 200-500ms / >500ms (replaced the retired FID metric in March 2024)
- CLS: ≤0.1 / 0.1-0.25 / >0.25
- FCP: ≤1.8s / 1.8-3s / >3s; TTFB: ≤0.8s / 0.8-1.8s / >1.8s

**Workflow:**
1. Monitor at scale (bulk API pulls or crawler integrations) + Search Console CWV report, which buckets URLs by template.
2. Fix the template once — resolves every page in the bucket.
3. Use report diagnostics per failing template to target the LCP image, CLS elements, or long tasks.
4. Verify with lab tests — field data lags 28 days.

## Actionable checklist
- [ ] Analyze mobile first (usually worse than desktop)
- [ ] Check origin-level field data if URL-level data is missing (low traffic)
- [ ] Run 3-5 lab tests per page and average — scores fluctuate with network/load
- [ ] Target the reported LCP element, CLS shifters, and main-thread blockers
- [ ] Use TBT in lab tests as the INP proxy
- [ ] Don't chase every passed audit — spend time on failing metrics
- [ ] Re-test lab metrics after fixes; wait out the 28-day field window before judging CWV status
- [ ] Pull data in bulk via the API (or crawler integration) for site-wide prioritization

## Data points & benchmarks
- In older data, only 2% of tested pages scored 100; a 50 performance score was in the top 25% of tested pages.
- Score bands: 90-100 good, 50-89 needs improvement, 0-49 poor.
- Field dataset covers ~29.5M origins (April 2023) — opted-in browser users only.
- Performance score weights differ between mobile and desktop; lab tests emulate a mid-range mobile device.
- Estimated savings shown per opportunity are optimistic — fixing one issue may yield nothing if other blockers remain.

## Mistakes to avoid
- Treating a good lab score as passing Core Web Vitals — they're different measurements.
- Comparing single lab runs; always average several.
- Expecting the estimated time savings per fix to materialize exactly.
- Checking only desktop; mobile is the default index and usually the weak spot.
- Judging fixes by field data immediately — it's a 28-day rolling average.

## Key principles
- Field data decides whether you pass; lab data tells you why you fail.
- Fix templates, not URLs — bucketed reports turn one fix into thousands.
- The performance score is a weighted composite, not a ranking input; the CWV metrics are.
