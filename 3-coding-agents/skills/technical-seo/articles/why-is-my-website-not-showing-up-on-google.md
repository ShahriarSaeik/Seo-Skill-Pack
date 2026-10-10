# 8 Fixes For When Your Website Isn't Showing Up In Google

- **Updated**: 2026-10-05

## TL;DR
When a site is invisible in search, work an 8-step diagnostic ladder: indexed at all? → sitemap submitted? → noindex blocking? → robots.txt blocking? → orphans (no internal links)? → enough backlinks vs competitors? → matching search intent? → penalty? The first five are mechanical checks; the last three are strategic gaps.

## Framework / Step-by-step
1. **Check indexing** — `site:yourwebsite.com` gives a rough view of what's indexed; the Page indexing report and URL Inspection tool confirm per-page status and offer "Request indexing" for misses (a hint, not a guarantee).
2. **Submit your sitemap** — sitemaps flag important pages even when internal links are missing. Find the URL in robots.txt; submit in Search Console. No sitemap? Create one.
3. **Check for noindex** — `<meta name="robots" content="noindex">` blocks indexing regardless of sitemap. Common trap: CMS "discourage search engines" checkbox adds it sitewide. Crawl for "noindex page in sitemap" warnings — near-certain problem.
4. **Check robots.txt crawl blocks** — Search Console's "Submitted URL blocked by robots.txt" error means either unblock pages you want indexed or remove unwanted pages from the sitemap. If unsure, hire an expert — one bad rule hides the whole site.
5. **Check internal links / orphans** — pages with no internal links (orphans) are findable only via sitemap/backlinks and are rarely deemed important: if visitors can't reach a page, why index it? Crawl with sitemap + backlinks as URL sources to surface orphans; link, merge, or delete them.
6. **Check backlinks** — indexed ≠ visible; few-link pages rarely rank for searched terms (clear links↔traffic correlation in one large dataset). Compare your linking sites (and third-party authority estimates, which are not Google metrics) vs competitors; benchmark needed links by counting linking domains of the top 3 results for your target keyword. Quality beats count: one example page has 421 linking domains but only ~50 strong ones — that's the real competitive bar.
7. **Check search intent** — if top results for your keyword are all listicles and you're shipping a product page, you won't rank. Match the dominant format/type of page-one results.
8. **Check for penalties** — manual actions appear in Search Console (Security & Manual Actions); algorithmic hits show as traffic cliffs aligned with known update dates on a traffic-over-time graph. Either → get expert help.

## Actionable checklist
- [ ] Run site: search; inspect and request indexing for key URLs
- [ ] Submit XML sitemap (URL usually in robots.txt)
- [ ] Verify no noindex tags — especially CMS visibility settings
- [ ] Clear robots.txt blocks flagged in the Page indexing report (check the robots.txt report in Search Console → Settings)
- [ ] Crawl for orphan pages; add internal links to anything important
- [ ] Compare linking domains vs the top 3 ranking pages for your keyword
- [ ] Align page format with the dominant content type on page one
- [ ] Check manual actions and traffic-vs-update alignment

## Data points & benchmarks
- Brand-new sites commonly take days to several weeks to be indexed, and longer to rank for non-brand searches; check indexing before assuming a problem.
- Example competitive bar: a ranking listicle with 421 linking domains had only ~50 high-quality ones when filtered for link quality — quality filters reset the real target.
- Clear positive correlation between backlinks and organic traffic across one large dataset.
- CMS "search engine visibility" checkbox = the most common accidental sitewide noindex.

## Mistakes to avoid
- Submitting a sitemap full of noindexed or robots-blocked URLs.
- Assuming indexing = visibility; without competitive links, nothing ranks for searched terms.
- Ignoring intent and trying to outrank listicles with product pages.
- DIY surgery on a misunderstood robots.txt — one directive can hide everything.

## Key principles
- Visibility = crawlable + indexable + internally linked + competitive authority + intent match.
- Orphan pages signal unimportance to both users and engines.
- Benchmark link needs against quality-filtered competitor links, not raw counts.
