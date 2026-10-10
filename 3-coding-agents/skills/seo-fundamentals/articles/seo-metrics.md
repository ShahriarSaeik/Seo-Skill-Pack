# SEO Metrics: The 10 Worth Tracking (and 4 to Ignore)

- **Updated**: 2026-10-05

## TL;DR
Most SEO dashboards mix signal with noise. Ten metrics reliably indicate whether SEO is working: organic traffic, keyword rankings, search visibility (share of voice), traffic value, organic conversions, referring domains, indexed pages, page indexing errors, Core Web Vitals, and a technical health score. Four popular metrics — bounce rate, exit rate, pages per session, and average session duration — are vanity numbers that don't drive decisions.

## Framework / Step-by-step
Track in three layers:
1. **Outcome metrics** — organic traffic (filter out branded queries if you're an established brand), organic conversions (revenue-tied; e-commerce: purchases/AOV; SaaS: trials/signups by tier), and traffic value (what your organic clicks would cost as paid ads — rising value means you're winning "money keywords").
2. **Competitive/relative metrics** — keyword rankings for your most business-relevant terms, and search visibility (share of all clicks on a tracked keyword set that land on you). Visibility is the SEO version of share of voice, and share of voice correlates with market share — a better KPI than raw traffic growth.
3. **Leading/technical metrics** — referring domains over time (quality-checked; the strongest traffic-correlated link metric), indexed pages (should grow steadily; sudden drops = technical trouble), page indexing errors (fix before they spread), Core Web Vitals (LCP loading, INP responsiveness, CLS layout stability — a minor ranking factor), and an overall technical health score from a site crawler.

## Actionable checklist
- [ ] Pull organic traffic from Search Console with a brand-query exclusion filter
- [ ] Track rankings only for keywords that matter commercially
- [ ] Compute search visibility over a representative keyword set; benchmark against competitors
- [ ] Report traffic value alongside traffic volume
- [ ] Set up conversion tracking per business model and compare like-for-like periods (mind seasonality)
- [ ] Audit new referring domains monthly for quality, not just count
- [ ] Watch the indexed-pages trend; investigate any sudden change
- [ ] Clear page indexing errors (Search Console Page indexing report); validate fixes
- [ ] Check Core Web Vitals in Search Console; fix failing metrics
- [ ] Review crawl health score and error diffs between crawls
- [ ] Remove bounce rate, exit rate, pages/session, and avg. session duration from SEO KPI reports

## Data points & benchmarks
- Referring domains show a clear positive correlation with organic search traffic across large-scale studies — growth trend matters more than the absolute number.
- Core Web Vitals have been a minor ranking factor since June 2021 — bad scores can hurt, but they won't outrank relevance.
- Time-based engagement metrics are skewed: in Universal Analytics (retired in 2023) a bounced session recorded 0 seconds, systematically understating engagement. GA4 uses engagement rate and engaged time instead, but they're still context, not SEO KPIs.
- Last-click attribution under-credits SEO: it assigns conversions to the final traffic source, hiding SEO's assist role — compare attribution models in your analytics.

## Mistakes to avoid
- Treating raw organic traffic as success without excluding branded visits or tying to conversions.
- Reporting engagement metrics (bounce rate, pages/session, time on page) as SEO KPIs — they're skewed, benchmarkless, or easy to misread.
- Celebrating referring-domain counts without quality review.
- Ignoring indexed-page counts until pages vanish — sudden drops are the earliest technical warning sign.

## Key principles
- Prefer relative metrics (search visibility/share of voice) over absolute ones for KPIs — they normalize for market shifts.
- Every metric in the report must have a "why" and a decision attached; if a number can't change an action, delete it.
- Technical metrics are leading indicators; traffic and conversions lag — read them together.
