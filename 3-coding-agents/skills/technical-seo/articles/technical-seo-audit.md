# How to Complete a Technical SEO Audit in 8 Steps

- **Updated**: 2026-10-05

## TL;DR
A repeatable 8-step technical SEO audit: crawl the site, check crawlability/indexation, audit on-page technical elements, fix image issues, analyze internal links, check external links, measure site speed, and verify mobile-friendliness. Prioritize issues by impact — indexation blockers always outrank cosmetic fixes.

## Framework / Step-by-step
1. **Crawl your website** — Set up a crawl in a site audit crawler (free options exist). Check crawl settings first: raise crawl speed and page limits for big sites; connect a PageSpeed API key if you want Core Web Vitals data. Start with the overview (health score, indexable vs non-indexable pages), then work through the issues list sorted by priority.
2. **Spot crawlability & indexation issues** — Check Search Console Page indexing report; check robots.txt for accidental disallows (robots.txt report in Search Console → Settings, plus URL Inspection); check robots meta tags; validate sitemap (all important pages in, junk out); review crawl budget via Search Console Crawl Stats (mainly for large sites).
3. **Check technical on-page elements** — Title tags (≤60 chars), meta descriptions, canonical tags, hreflang tags, structured data (JSON-LD preferred; test with the Rich Results Test and Schema Markup Validator).
4. **Identify image issues** — Broken images, oversized files (compress before upload; use WebP/AVIF with fallbacks), HTTPS→HTTP mixed content, missing alt text.
5. **Analyze internal links** — Fix 4xx internal pages (restore or 301 redirect + update links); eliminate orphan pages; silo topics for relevance.
6. **Check external links** — Pages linking to broken pages; pages with zero outgoing links (dead ends).
7. **Review site speed & performance** — Core Web Vitals (LCP, CLS, INP) via PageSpeed Insights or other lab tools; very slow sites see traffic/CTR gains from fixes; minor speed issues rarely move rankings.
8. **Ensure mobile-friendliness** — Run a second crawl with a mobile user agent; use crawl comparison to find mobile-only issues; check viewport/tap targets in Lighthouse or DevTools (the Mobile-Friendly Test and Mobile Usability report were retired in Dec 2023).

## Actionable checklist
- [ ] Run a site audit crawl; review the overview and the prioritized issues list
- [ ] Search Console Page indexing report: confirm key pages indexed, no accidental blocks
- [ ] Robots.txt: no stray `Disallow: /` left from staging
- [ ] Sitemap: only indexable, important pages included
- [ ] No unintended noindex meta tags on money pages
- [ ] Canonical tags present on duplicate/near-duplicate pages
- [ ] Hreflang valid on all language variants
- [ ] Structured data tested (Rich Results Test passes)
- [ ] Images compressed (WebP/AVIF with fallbacks), no broken images, no mixed content, alt text present
- [ ] No orphan pages; internal links point to all indexable pages
- [ ] No broken (4xx) internal pages
- [ ] Site loads fast; check PageSpeed Insights
- [ ] Second crawl with mobile user agent; compare for mobile-only issues

## Data points & benchmarks
- Title tags: keep under ~60 characters (long titles are a top reason Google rewrites them).
- Google rewrote title tags roughly a third of the time (older industry study).
- Google showed meta descriptions only ~37% of the time (older study) — still worth writing for important pages.
- Mobile shopping held ~60% of the market (2022 figure).
- Core Web Vitals used for ranking since May 2021 (LCP = load, CLS = stability, INP = responsiveness; INP replaced FID in March 2024).
- Audit cadence recommended: initial audit + quarterly, plus whenever rankings stagnate or decline.

## Mistakes to avoid
- Leaving `Disallow: /` in robots.txt after a site goes live (blocks everything).
- Accidental noindex tags on pages you want ranked.
- Including broken/unimportant pages in the sitemap (confuses crawlers, wastes crawl budget).
- Ignoring orphan pages — no internal links = no PageRank flow and poor discovery.
- Assuming small speed issues will boost rankings — only very slow sites typically gain.
- Treating all issues as equal: always triage by priority and page importance.

## Key principles
- "Technical SEO is the core foundation of any website."
- Audit before any link-building or content work — technical issues impede everything downstream.
- SEO is a points system: when you and a competitor are tied, basic housekeeping issues decide who wins.
- Internal links are "the jelly to backlinks' peanut butter" — audit both.
- An issue's importance always depends on the specific site and page: pages you want to rank take priority.
