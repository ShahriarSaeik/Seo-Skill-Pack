# Mobile-First Indexing Goes Mobile-Only

- **Updated**: 2026-10-05

## TL;DR
Mobile-first indexing means the mobile version of your content is what gets indexed and ranked — and since July 2024, content entirely inaccessible on mobile is no longer indexable at all. The rollout is complete (2016-2023), there's one index, and there's no opting out. Keep important content, links, and technical signals fully present on mobile.

## Framework / Step-by-step
**Timeline:** mobile-friendliness as ranking factor (Apr 2015) → mobile-first indexing announced (Nov 2016) → rollout (Mar 2018) → >50% of sites (Dec 2018) → default for new sites (Jul 2019) → >70% (Mar 2020) → last stragglers moved (May 2023; a few desktop-only relics remain) → **mobile-only: content not accessible on mobile becomes unindexable (Jul 2024)**.

Verify your status: Search Console Settings → About (shows the indexing crawler); the URL Inspection tool shows "Crawled as: [bot] smartphone". Desktop crawling still happens occasionally (to relate desktop/mobile versions) — its presence is normal.

**Best practices:**
1. **Build mobile-friendly** — responsive design, mobile speed, mobile SERP optimization, no intrusive interstitials, device-split performance/rank tracking.
2. **Keep important content** — mobile doesn't need to be identical, but anything omitted "because it's long" can hurt. Content hidden behind UX patterns (tabs, accordions, expandables) is no longer discounted — ecommerce does this well (progressive product details, Q&A, reviews).
3. **Navigation & links** — external links consolidate fine with correct canonicals; ensure internal links (breadcrumbs, full menus) survive on mobile — missing links change how PageRank flows.
4. **Technical checks** — crawl once with a desktop user agent, again with mobile, and diff the results: on-page tags (titles, descriptions, canonicals, robots, hreflang, structured data, image alt), robots.txt differences (especially m-dot subdomains), CSS/JS/image crawlability, mobile Core Web Vitals, interstitials, viewport/text size/tap targets (check in Lighthouse or Chrome DevTools device mode; Search Console's Mobile Usability report and the Mobile-Friendly Test were retired in Dec 2023).

**Known failure modes (from engine guidance):** missing structured data or titles on mobile, noindex on mobile URLs, missing/blocked/low-quality images or alt text, mobile URL as error page or with anchor fragments, mobile page blocked by robots.txt, duplicate mobile targets, desktop redirecting to mobile homepage, video/host-load issues.

## Actionable checklist
- [ ] Confirm mobile-first indexing status and "Crawled as" agent in Search Console
- [ ] Crawl with mobile UA; diff vs desktop crawl for missing tags, links, and content
- [ ] Keep all important content and internal links (incl. breadcrumbs) on mobile
- [ ] Use tabs/accordions freely for UX — hidden content is fine when user-triggered
- [ ] Compare m-dot robots.txt vs main; allow CSS/JS/images everywhere
- [ ] Check mobile CWV (field data in Search Console/PageSpeed Insights) and run Lighthouse/DevTools mobile checks (viewport, tap targets, text size)
- [ ] Remove full-screen interstitials (except legal gates)
- [ ] Verify nothing on the site is desktop-only accessible

## Data points & benchmarks
- Rollout took ~7 years (2016 → May 2023 complete).
- Jul 2024 cliff: content invisible on mobile = not indexable.
- One index; no opt-out; desktop-UA crawls still occur for version relationship checks.

## Mistakes to avoid
- Trimming mobile content, internal links, or structured data "for space."
- Different robots.txt rules on m-dot subdomains.
- Blocking CSS/JS from crawling — rendering needs them.
- Assuming hidden/tabbed content is discounted — that rule died with mobile-first indexing.

## Key principles
- If it's not on mobile, it's not in the index — mobile parity is a hard requirement now.
- Hidden-behind-interaction content is fine; absent content is not.
- Crawl-and-diff (desktop vs mobile) is the core audit technique.
