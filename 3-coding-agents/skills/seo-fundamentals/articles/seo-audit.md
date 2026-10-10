# How to Do an SEO Audit in 13 Easy Steps (With Checklist)

- **Updated**: 2026-10-05

## TL;DR
An SEO audit systematically finds the issues holding back rankings and the opportunities worth pursuing. Work through 13 checks — from crawl health and traffic-drop diagnosis to on-page basics, declining content, content gaps, internal links, and SERP features — then fix technical issues, on-page issues, and content opportunities in that order.

## Framework / Step-by-step
1. **Run a site crawl** — use a site audit tool (crawling software) to detect 100+ issue types; don't try to fix everything, follow the priorities below.
2. **Diagnose organic traffic drops** — compare traffic charts against known algorithm update dates (search status dashboards). Check the manual actions report in Search Console if traffic dropped sharply.
3. **Check for duplicate site versions** — only one of `https://domain.com` / `https://www.domain.com` should be live; all variants must 301-redirect to the master version, or link equity gets diluted.
4. **Diagnose indexability** — look for pages accidentally blocked by noindex meta robots tags; remove the tag on pages you want indexed.
5. **Ensure mobile-friendliness** — Google indexes the mobile version of your pages (mobile-first indexing). The Search Console Mobile Usability report and Mobile-Friendly Test were retired in 2023, so test key templates with Lighthouse/PageSpeed Insights and Chrome DevTools device mode, and confirm mobile and desktop content match.
6. **Benchmark Core Web Vitals** — LCP (loading), INP (interactivity, replaced FID in March 2024), CLS (visual stability). Use the Search Console Core Web Vitals report.
7. **Reclaim authority from broken pages** — find 404 pages with backlinks (a backlink tool's pages report filtered by 404 status), then either redirect or rebuild the page.
8. **Fix sitemap issues** — the sitemap should list only canonical, indexable, live pages; no redirects or dead pages.
9. **Enforce on-page basics** — every indexable page needs a title tag, meta description, and H1. Prioritize fixes by the page's organic traffic.
10. **Find declining content** — in Search Console, compare the last 6 months vs. the previous period and sort pages by click difference; refresh and republish the biggest decliners.
11. **Find content gaps** — keywords competitors rank for that you don't (a competitor content-gap report); shortlist relevant ones.
12. **Audit internal links** — fix broken internal links, reconnect orphan pages, and add contextual internal links from pages that mention keywords your target page ranks for.
13. **Optimize for AI Overviews and featured snippets** — filter your keyword rankings for SERP features you don't own; featured snippets and AI Overview citations often go to the same well-structured pages, so clear, answer-first content helps with both.

## Actionable checklist
- [ ] Crawl the site with an SEO audit tool
- [ ] Overlay traffic drops with algorithm update dates; check manual actions
- [ ] Verify all domain variants redirect to one master (HTTPS) version
- [ ] Remove stray noindex tags from pages that should rank
- [ ] Fix mobile issues found in Lighthouse/PageSpeed Insights; confirm mobile/desktop content parity
- [ ] Record LCP / INP / CLS baselines; fix worst pages first
- [ ] 301 or restore 404 pages that have referring domains
- [ ] Clean the sitemap (canonical, live pages only)
- [ ] Fix missing/empty titles, meta descriptions, H1s — highest-traffic pages first
- [ ] Refresh top declining pages from the last 6 months
- [ ] Build a content-gap keyword shortlist from competitors
- [ ] Fix broken internal links; re-link orphan pages; add contextual links
- [ ] Chase featured snippets/AI Overview citations on keywords where you already rank top 10

## Data points & benchmarks
- Roughly 99% of keywords that trigger an AI Overview are informational (industry study of 300K keywords).
- 12.3% of queries have a featured snippet; snippets capture 8.6% of clicks; 30.9% of snippets come from position one (2017 study of 2 million featured snippets, before AI Overviews).
- One study found SERPs with AI Overviews showed far more featured snippets than SERPs without — a correlation, not proof that one causes the other.
- One audited site had 724 pages missing title tags — a common, easily fixed click-killer.

## Mistakes to avoid
- Trying to fix all 100+ crawl issues at once instead of prioritizing.
- Ignoring traffic-drop timing — fixes differ for algorithm hits vs. manual actions vs. seasonality.
- Leaving multiple accessible site versions (dilutes link equity).
- Letting sitemaps contain redirects, dead, or non-canonical pages.
- Assuming noindexed pages are intentional — always verify.

## Key principles
- An audit outputs three buckets: technical fixes, on-page fixes, content opportunities.
- Broken pages with backlinks are wasted authority — always reclaim them.
- Featured snippets and AI Overviews are correlated (both reward clear, direct answers), but winning one doesn't guarantee the other.
- Internal links directly feed PageRank distribution; orphan pages are invisible to it.
