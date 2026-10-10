# Robots Meta Tag & X-Robots-Tag: Indexation Control

- **Updated**: 2026-10-05

## TL;DR
The robots meta tag (HTML) and X-Robots-Tag (HTTP header) control how search engines index pages and snippets — robots.txt cannot do this. Use noindex for pages that shouldn't rank (thin, staging, admin, PPC landers), X-Robots-Tag for non-HTML files and bulk rules, and never combine noindex with a robots.txt block.

## Framework / Step-by-step
**The two mechanisms:**
1. Robots meta tag — `<meta name="robots" content="noindex, nofollow">` in `<head>`; `name` targets a specific crawler (`robots` = all).
2. X-Robots-Tag — HTTP response header with the same values; the only option for PDFs/images, and the scalable option (regex matching via server config).

**Content values (Google-supported):**
- `noindex` / `nofollow` / `all` (default; never needed) / `none` (avoid — not universally supported)
- `noarchive`, `notranslate`, `noimageindex`
- `unavailable_after: <RFC850 date>` — timed noindex for promos/contests
- Snippet controls: `nosnippet`, `max-snippet:[n]`, `max-image-preview:[none|standard|large]`, `max-video-preview:[n]`; plus `data-nosnippet` HTML attribute on div/span/section
- `indexifembedded` — pairs with noindex for iframe-embedded content

Conflicting directives resolve to the MOST restrictive one.

**When to use which:**
- Meta tag: HTML pages, per-page control, engines that ignore headers.
- X-Robots-Tag: PDFs/images, whole-subdirectory or parameterized bulk noindexing, server/CDN-level control.

## Actionable checklist
- [ ] noindex on: thin pages, staging, admin/thank-you, internal search results, PPC landers, unreleased promos
- [ ] No page is BOTH noindexed and blocked in robots.txt
- [ ] Noindexed pages kept in sitemap (with refreshed lastmod) UNTIL deindexed, then removed
- [ ] Staging noindex/disallow removed before production pushes (add to dev checklist)
- [ ] "Secret" URLs noindexed, not listed in robots.txt (robots.txt is public — leaks URLs)
- [ ] X-Robots-Tag used for PDFs/images that shouldn't be indexed
- [ ] HTTP headers spot-checked after server config changes
- [ ] max-image-preview:large set on pages with 1200px+ images (feed/Discover eligibility)

## Data points & benchmarks
- A `noindex` line in robots.txt was never officially supported; Google informally honored it until September 1, 2019 and now ignores it.
- Snippet preview directives arrived in October 2019 (copyright-driven): `max-snippet:-1, max-image-preview:large, max-video-preview:-1` = no snippet restrictions.
- Large image previews need source images ≥1200px wide.

## Mistakes to avoid
- Blocking noindexed pages in robots.txt — search engines can't see the noindex, so URLs can stay indexed; you also lose the recrawl signal.
- Removing a page from the sitemap the same day you noindex it — sitemap + fresh lastmod accelerates recrawling.
- `none` directive — other search engines don't support it.
- Bulk-editing server config without backups — one syntax error can take down the site.
- Relying on meta robots for engines that only read headers (or vice versa) — know your target engines.

## Key principles
- robots.txt = can we crawl it; meta robots/X-Robots-Tag = can you index/show it. Two separate systems.
- Deindexing is a process: noindex → keep crawlable → keep in sitemap → confirm removal → clean up sitemap.
- Indexation directives are page-level; combine with sitemaps and robots.txt for sitewide strategy.
