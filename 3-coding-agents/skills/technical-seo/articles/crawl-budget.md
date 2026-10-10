# When Should You Worry About Crawl Budget?

- **Updated**: 2026-10-05

## TL;DR
Crawl budget = crawl demand (how much Google wants to crawl) × crawl rate limit (how much your server can take). Most sites shouldn't worry about it. Worry when: new sites with many pages, millions of pages, frequently updated sites, or many "Discovered - currently not indexed" pages in Search Console. More crawling ≠ better rankings; uncrawled pages simply can't rank.

## Framework / Step-by-step
**When to worry:**
- New sites with lots of pages (Google doesn't yet trust/crawl much)
- Large sites (millions of URLs) or frequently updated sites
- Pages not crawled/updated as often as needed
- Many Search Console "Discovered - currently not indexed" pages (never crawled — possible crawl budget issue)

**What counts against crawl budget:** ALL URLs and requests — AMP/m-dot, hreflang variants, CSS, JS, XHR requests (not cached → heavy for JS-framework sites), images. Multiple Googlebots (desktop, mobile, image...) share one budget.

**How Google adjusts:**
- *Crawl demand* rises with page popularity (links/PageRank), change frequency, and how often Google serves the page. Staleness: unchanged pages get crawled on expanding intervals (1 day → 3 → 10 → 30 → 100...).
- *Crawl rate limit* rises if site health is good; drops with 5xx errors, 429s, or slow connect times.

**To crawl faster/smarter:**
1. Speed up server / fix 5xx and 429s (logs)
2. Add important pages to sitemaps
3. Eliminate duplicate/technical URL variants (HTTP/HTTPS, www/non-www, trailing slashes, case, index.* defaults, parameters)
4. Build more links — external AND internal (an internal-link opportunities report from any SEO tool helps)
5. Fix redirected internal links; remove 3XX URLs from sitemaps
6. Host resources on a different hostname/CDN
7. Use GET instead of POST (GET is cacheable)
8. Google Indexing API (job postings/live video only); IndexNow / Bing URL submission (any site) — all are hints, not commands
9. 304 Not Modified support (complex, rarely worth it; caching is better)

**To crawl slower:** the Search Console crawl-rate limiter was removed (January 2024); in an emergency, serve 503/429 briefly (risky — pages drop from the index after a few days).

## Actionable checklist
- [ ] Search Console Crawl Stats: check total crawl requests trend, flagged crawl statuses, host status
- [ ] Check Search Console Page Indexing for "Discovered - currently not indexed" volume
- [ ] Consolidate duplicate variants (redirect HTTP→HTTPS, www choice, trailing slash, lowercase)
- [ ] Block faceted/parameter URLs in robots.txt or switch ? to # where safe
- [ ] Sitemap: only canonical, important, 200-status URLs
- [ ] Fix internal 3xx links (site crawler → internal URLs with 3xx status)
- [ ] Add internal links to under-crawled priority pages
- [ ] Check server logs for 5xx/429s and slow connect times
- [ ] Don't bother: crawl-delay (Googlebot ignores), removing 3rd-party scripts, noindex for budget, trivial page edits

## Data points & benchmarks
- ~60% of the internet is duplicate content (older Google estimate) — mostly technical duplicates wasting crawl budget.
- Duplicate variants list: HTTP/HTTPS × www/non-www × trailing slash × case × index.* × parameters.
- Staleness backoff: crawl intervals expand ~1d → 3d → 10d → 30d → 100d for unchanged pages.
- Google slows crawling on 5xx / 429 status codes and slow connect times.
- Serving 503/429 for more than a few days risks deindexing.
- Nofollow is a hint — Google may still crawl nofollow links.

## Mistakes to avoid
- Obsessing over crawl budget on small/healthy sites.
- Making trivial edits (dates, punctuation) to trigger recrawls — Google detects insignificant changes.
- Using noindex to save crawl budget — Google must still crawl to see it.
- crawl-delay in robots.txt — Googlebot ignores it (some other crawlers respect it).
- Removing third-party scripts for crawl budget — they don't count against it.
- Long-running 503/429 to slow crawling — deindexing risk.

## Key principles
- "More crawling doesn't mean you'll rank better, but pages that aren't crawled and indexed can't rank at all."
- Crawl demand is popularity-driven: links (internal + external) are the lever you control.
- Everything (JS, CSS, XHR, variants) consumes budget — dedupe and simplify.
- Google self-adjusts to server health; keep 5xx/429 low and responses fast.
