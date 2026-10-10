# Googlebot: How Google's Crawler Works

- **Updated**: 2026-10-05

## TL;DR
Googlebot is Google's evergreen crawler fleet: smartphone and desktop variants plus specialized crawlers for news, images, and video. It runs on thousands of machines (self-throttling to avoid overwhelming sites), mostly crawls from one US location, reads only the first part of each file (documented limits: 15 MB default for Google's crawlers, 2 MB for HTML per a 2026 doc update — check current docs), and indexes the mobile-rendered version of pages. Verify "Googlebot" visits by IP — many tools and malicious bots spoof its user-agent.

## Framework / Step-by-step
**The crawl → index pipeline:**
1. URL collection — from discovered links, sitemaps, RSS feeds, and submitted URLs.
2. Prioritization + fetch — pages are scheduled, downloaded, stored.
3. Processing — extract links, plus resources needed to render (JS, CSS, API calls); those get crawled and cached too.
4. Rendering — pages rendered like a browser would, using cached resources.
5. Re-processing — detect changes and new links; the MOBILE version of the rendered page is what gets stored in the index.
6. New links return to the crawl queue (loop).

**Controlling crawling:**
- robots.txt (what may be crawled)
- nofollow attributes/tags (hint only)
- the Search Console crawl-rate limiter was removed in January 2024 (Googlebot adapts to server health automatically).

**Controlling indexing:**
- Delete the content, or put it behind authentication (crawlers don't log in)
- noindex meta tag / X-Robots-Tag
- Search Console removals tool (temporarily hides; still crawled)
- robots.txt controls crawling, not indexing — a blocked page can still be indexed from links (blocking Googlebot-Image does keep images out of image search).

## Actionable checklist
- [ ] Log-file crawler IPs verified against Google's published IP ranges (spoofed bots are common)
- [ ] Search Console Crawl Stats reviewed: which crawler types hit which files, when
- [ ] HTML kept well under 2 MB and other files under 15 MB (check current Google docs); robots.txt under 500 KiB
- [ ] HTTP/2 enabled; compression (gzip/brotli) working
- [ ] Caching validators (ETag / Last-Modified) honored so unchanged pages return 304s
- [ ] No geo-blocking that would exclude the crawler's US-originated requests (verify with care — some locale-adaptive crawling exists)
- [ ] Mobile rendering treated as the source of truth for what's indexed

## Data points & benchmarks
- Googlebot accounted for ~24% of all "good bot" HTTP requests on the web in one CDN's radar data (older snapshot) — the single most active crawler; one SEO-industry crawler followed at ~14%, Bing's at under 5%.
- Documented size limits: 15 MB default per file for Google's crawlers, 2 MB for HTML in Googlebot for Search (per a 2026 doc update); 500 KiB max for robots.txt.
- Crawler user-agents include: Googlebot Smartphone, Googlebot Desktop, Googlebot-Image, Googlebot-Video, news crawlers, store crawlers, the inspection tool, and utility crawlers — each with distinct strings.

## Mistakes to avoid
- Trusting user-agent strings alone — verify by IP or DNS before granting access or diagnosing "Googlebot" traffic.
- Assuming robots.txt controls indexing — it controls crawling; use noindex (on a crawlable page) to keep a page out of the index.
- Ignoring that the indexed content is the mobile-rendered DOM — desktop-only differences go unnoticed.

## Key principles
- Googlebot is polite by design: it adapts crawl rate to server health — slow responses teach it to crawl less.
- Rendering + caching is central: resources are cached, XHR requests are live, mobile rendered content is what ranks.
- Crawl controls (robots.txt) and index controls (noindex, auth, deletion) are separate systems — choose deliberately.
