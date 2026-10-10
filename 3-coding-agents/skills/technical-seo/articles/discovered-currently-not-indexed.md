# How to Fix "Discovered - currently not indexed"

- **Updated**: 2026-10-05

## TL;DR
"Discovered - currently not indexed" = Google knows the URL but hasn't crawled it yet. Fix in 5 steps: request indexing, fix crawl-budget waste, improve content quality, add internal links, build backlinks. Google deprioritizes crawling pages it expects to be low-value.

## Framework / Step-by-step
1. **Request indexing** (Search Console URL Inspection) — for a handful of affected pages only; ~10-15 URLs/day submission limit. If it recurs, an underlying issue exists.
2. **Check crawl budget** (90% of sites don't need to worry — Gary Illyes):
   - Assets (images, scripts) served from the main hostname use up its crawl capacity → serve them from a separate CDN hostname
   - Unnecessary redirects: if a removed page has no backlinks/traffic, 404 it and remove internal links instead of redirecting
   - Duplicate content (www/non-www, HTTP/HTTPS, staging, empty boilerplate pages)
   - Internal nofollow links signal "unimportant" → replace with followed links
   - Orphan pages (sitemap-only discovery = low importance)
3. **Check content quality** — Google deprioritizes crawling based on similar pages it has already crawled. Likely-unindexed types: machine-translated, spun, unedited AI-generated, thin content. Fix: merge thin pages, improve, or noindex if not for organic search.
4. **Check internal linking** — pages with few/no internal links look unimportant. Add contextual links (an internal link opportunities report from any SEO tool helps); consider an HTML sitemap page to shorten crawl depth; use real `<a>` tags, not JS onClick() navigation.
5. **Check backlinks** — pages with few quality backlinks get deprioritized; even one valuable link speeds discovery and indexing.

## Actionable checklist
- [ ] Search Console → URL Inspection → Request indexing (≤10-15/day)
- [ ] Crawl the site: list internal redirects with no inlinks/referring domains → 404 instead
- [ ] Find pages whose only internal links are nofollow → replace with followed links
- [ ] Fix duplicate variants (www/HTTP/staging)
- [ ] Audit thin/translated/spun/AI content: merge, improve, or noindex
- [ ] Sort crawled pages by inlink count → find weakly-linked pages
- [ ] Find orphan pages (crawl vs sitemap vs logs) → add internal links
- [ ] Internal link opportunities by keyword → add contextual links
- [ ] Check important pages' backlink counts in a backlink tool → build links where weak

## Data points & benchmarks
- Search Console indexing requests: ~10–15 URLs per day (undocumented limit).
- 90% of sites don't need to worry about crawl budget (Google's Gary Illyes).
- Crawl capacity is tracked per hostname; assets on a separate hostname/CDN don't compete with your pages.
- Orphan pages are best found by comparing crawl data with sitemaps, analytics, and server logs — crawlers following links miss them by definition.

## Mistakes to avoid
- Mass-submitting indexing requests without fixing the underlying cause.
- Redirecting deleted pages that have no links or traffic (404 is fine; redirects waste budget).
- Nofollowing internal links to pages you want indexed.
- Relying on JS onClick() navigation instead of crawlable `<a href>` links.
- Expecting sitemap inclusion alone to get pages crawled.

## Key principles
- "Discovered" = known but uncrawled: a prioritization problem, not an error.
- Google predicts quality from similar pages already crawled — site-wide quality affects new pages.
- Internal links = importance signal; backlinks = value signal; both drive crawl priority.
- If content isn't meant for organic search, noindex or remove it — noindex keeps it out of the index but doesn't save crawl budget by itself.
