# How to Do an SEO Log File Analysis

- **Updated**: 2026-10-05

## TL;DR
Server access logs are the most trustworthy record of what Googlebot actually crawls. Analyze them (verified for fake bots) to find crawl-budget waste on non-200/non-indexable URLs, discover orphan pages, monitor priority URLs, and check bot/cache trends. Small sites can usually get by with Search Console Crawl Stats instead.

## Framework / Step-by-step
1. **Get access logs** (not error logs) from developers — be specific. Expect hurdles: data split across origin/load balancer/CDN servers, terabyte file sizes, PII (user IPs) compliance, short storage retention.
2. **Store logs** — a log-shipping integration from your CDN/server + a data warehouse = long-term storage you own; configure to strip PII.
3. **Verify Googlebot** — fake Googlebots are common. Options: reverse DNS lookup per Google's guide, firewall bad-bot rule sets, or match against Google's published Googlebot IP ranges (never a rough "66." prefix filter), or your CDN/WAF's managed fake-bot rule.
4. **Extract data** — SQL query in your data warehouse pulling date, URL, IP, user agent, status code, cache status, content type; filter `user_agent LIKE '%Googlebot%' OR user_agent LIKE '%bingbot%'`. Export CSV → spreadsheet.
5. **Enrich with data from a site audit crawler** — add organic traffic, status codes, crawl depth, indexability, internal links from a page-level crawl export.
6. **Run the analyses** (see checklist).

## Actionable checklist
- [ ] Status codes overview: what share of bot hits are non-200? (crawl budget waste)
- [ ] URLs overview: filter non-200 URLs with many internal inlinks → fix via an internal link opportunities report
- [ ] Crawl budget wastage: frequently crawled 200 HTML pages that are non-indexable (canonicalized/noindexed) → investigate why (internal links, sitemap inclusion, external links) → remove the links or fix the signals (don't robots.txt-block URLs whose noindex or canonical Google needs to read)
- [ ] Priority URL monitoring: track daily hits for a short list of key URLs; verify redirects are picked up quickly
- [ ] Orphan URLs: 200 HTML URLs with hits but zero internal links → add internal links, and include them in a custom URL-list crawl to audit them
- [ ] Directories overview: is Googlebot over-crawling low-traffic directories vs high-value ones?
- [ ] CDN cache status: a high cache-hit ratio helps CWV/TTFB; investigate miss/dynamic causes
- [ ] Bots overview: which bots crawl most; track changes post-migration

## Data points & benchmarks
- Search Console Crawl Stats: shows samples, max 3 months history, not all URLs — enough for small sites.
- Log files benefit large/frequently-changing sites most (mirrors Google's crawl-budget guidance).
- Many Googlebot IPv4 addresses start with "66.", but that is NOT reliable — verify with reverse DNS or Google's published Googlebot IP ranges.
- Google crawls popular URLs more; infrequent crawling of static URLs is normal, not a problem.
- `<lastmod>` in XML sitemaps: Google's public statements have varied over the years; current docs say it is used only when consistently accurate.
- Many CDN/WAF plans offer fake-bot blocking.
- High-traffic site access logs can reach terabytes+.

## Mistakes to avoid
- Requesting "log files" without specifying access logs (developers will ask which).
- Analyzing unverified Googlebot data — fake bots inflate numbers.
- Assuming non-200 hits are always a problem — Google crawls old 301s for years; worry when internal links point to non-200s.
- Assuming infrequent crawl = problem — normal for rarely-changing URLs.
- Cache misses: parameterized URLs often bypass the CDN cache by default.
- Relying on `<lastmod>` alone given Google's inconsistent signals.

## Key principles
- Log files = ground truth of crawler behavior; everything else is inference.
- Crawl budget optimization = maximize hits on indexable, valuable, changed URLs.
- Cross-analyzing logs + crawl data + analytics beats any single source.
- Ownership of log data (your own warehouse) sidesteps PII and access friction long-term.
