# Meta Tags for SEO: A Simple Guide for Beginners

- **Updated**: 2026-10-05

## TL;DR
Only 6 meta tags matter for SEO: title, description, robots, viewport, charset, and (to avoid) meta refresh. Set each correctly, audit for the four classic mistakes (too long/short, missing, multiple, duplicate), and never use meta keywords.

## Framework / Step-by-step
The 6 important meta tags:
1. **Meta title** — SERP headline. Keep <60 chars, unique per page, keyword where natural, click-worthy not clickbait, match intent.
2. **Meta description** — SERP snippet pitch. Not a direct ranking factor but affects clicks. Keep <160 chars, unique, sentence case.
3. **Meta robots** — controls indexing and link-following (not crawling): index/noindex, follow/nofollow. Use only to restrict; not setting it = index, follow.
4. **Meta viewport** — signals mobile-friendliness. Standard tag: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
5. **Meta charset** — use UTF-8: `<meta charset="UTF-8">` (HTML5 syntax).
6. **Meta refresh redirect** — avoid; use 301 instead.

## Actionable checklist
- [ ] Unique title tag on every page, under 60 characters
- [ ] Unique meta description on every page, under 160 characters
- [ ] Meta robots tag only where you need to restrict indexing or link-following
- [ ] Never block a noindexed page in robots.txt (Google can't see the noindex)
- [ ] Standard viewport tag on all pages
- [ ] UTF-8 charset on all pages
- [ ] Replace any meta refresh redirects with server-side 301/302s (or ensure a canonical tag exists)
- [ ] Remove meta keywords tags sitewide (usually one CMS-level setting)
- [ ] Audit: a SERP snippet preview tool for single pages; a site crawler (titles, descriptions, duplicates) sitewide
- [ ] Search Console Page indexing report: check "Indexed, though blocked by robots.txt" and "Excluded by 'noindex' tag"
- [ ] Lighthouse or Chrome DevTools device mode: confirm the viewport tag is present and pages don't scroll horizontally (the Mobile Usability report was retired in 2023)

## Data points & benchmarks
- Title tag: keep under 60 characters
- Meta description: keep under 160 characters; snippets truncated to fit device width
- Google has ignored meta keywords since 2009; Bing has said stuffed keywords tags may be a spam signal
- Historical: Google introduced a mobile-friendly ranking boost in 2015; it now indexes the mobile version of pages (mobile-first indexing), so a correct viewport and mobile parity matter
- Google treats nofollow as a hint, not a directive

## Mistakes to avoid
- Rogue meta noindex on pages that should rank (zero organic traffic)
- Rogue meta nofollow blocking link discovery and PageRank flow
- Blocking noindexed pages in robots.txt so Google never sees the noindex
- Duplicate titles/descriptions across pages
- Multiple title or description tags on one page
- Using meta refresh redirects instead of 301s
- Keeping meta keywords tags (spam signal in Bing)

## Key principles
- Meta descriptions are "a pitch that convinces the user that the page is exactly what they're looking for" — they influence clicks, not rankings.
- Wrong robots attributes can have "a catastrophic impact" on search presence — understand this tag before using it.
- Not setting a meta robots tag is equivalent to index, follow — absence is usually correct.
- Every tag's worst failure mode is invisibility: missing, blocked, or duplicated tags quietly cost traffic.
