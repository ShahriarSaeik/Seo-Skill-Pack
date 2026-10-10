# 10 SEO Issues That Really Matter & How to Fix Them

- **Updated**: 2026-10-05

## TL;DR
Based on an older industry study of 1M+ domains: the most common issues (missing meta descriptions on 72.9% of sites) aren't the ones that matter. Fix these 10 instead: indexability problems, broken pages, weak internal linking, mobile issues, HTTPS issues, Core Web Vitals, deep site structure, missing schema, duplicate content, and oversized HTML (2 MB Googlebot limit).

## Framework / Step-by-step
The 10 issues that actually matter, in order:
1. **Indexability issues** — Page must be (a) crawlable, (b) not noindexed, (c) canonical. Watch: canonical points to 4xx, canonical points to redirect.
2. **Broken pages** — 4xx/5xx pages waste link equity, crawl budget, and UX. Use referring-domain counts to prioritize: restore page or 301 redirect.
3. **Few or no internal links** — Orphan pages get no PageRank. Add relevant internal links (an internal link opportunities report helps).
4. **Mobile experience issues** — Mobile-first indexing + Page Experience signals. Fix viewport tags, tap targets, plugin dependencies; check with Lighthouse/DevTools (Search Console's Mobile Usability report was retired in Dec 2023).
5. **HTTPS issues** — HTTPS is a (small) ranking signal. 301/308 redirect all HTTP→HTTPS; fix mixed content.
6. **Performance & stability (Core Web Vitals)** — Goal is "good" score, not fastest: LCP, INP (replaced FID in March 2024), CLS.
7. **Unoptimized site structure** — Rule of thumb: pages >6 clicks from homepage get diluted link equity. Flatten structure or add links from higher pages.
8. **Lack of relevant schema markup** — Not a ranking factor, but enables rich results (recipes, jobs, videos, events).
9. **Duplicate content** — Google picks one version, maybe not yours. Consolidate to one canonical version (HTTPS).
10. **Oversized HTML pages (>2 MB)** — Googlebot only reads the first 2 MB of uncompressed HTML; everything after is ignored.

## Actionable checklist
- [ ] Site crawler indexability check: fix canonicals pointing to 4xx/redirects; remove unwanted noindex
- [ ] Crawl for broken pages (4xx/5xx): fix (restore or 301); prioritize those with referring domains
- [ ] Find and fix orphan pages (link or delete)
- [ ] Use an internal link opportunities report to add contextual links
- [ ] Check mobile issues in Lighthouse/DevTools device mode (viewport, tap targets, legible font size ≥12px)
- [ ] All HTTP pages 301/308 → HTTPS; check mixed content
- [ ] Add `Content-Security-Policy: upgrade-insecure-requests` header to auto-upgrade HTTP resources
- [ ] Search Console Core Web Vitals report: get all three metrics to "good"
- [ ] Crawl depth report: important pages ≤6 clicks from home
- [ ] Generate schema (generator or AI assistant, reviewed manually) + validate it (Rich Results Test / Schema Markup Validator)
- [ ] Check site resolves at only ONE of http/https × www/non-www (others 301 to canonical host)
- [ ] Check HTML page size against Googlebot's documented crawl limit (2 MB; see the data points)

## Data points & benchmarks
- Missing meta descriptions found on 72.9% of studied sites — common but doesn't impact rankings.
- Canonical pointing to a broken page: only 2.6% of sites — rare but severe.
- Googlebot crawls only the first 2 MB of uncompressed HTML (confirmed Feb 2026 doc update).
- Pages >6 clicks from homepage = too deep; link equity diminishes with each hop.
- INP replaced FID as CWV interaction metric in March 2024.
- Mobile legible-font guideline: at least 12 px (Lighthouse).
- HTTPS: small ranking signal since 2014.

## Mistakes to avoid
- Chasing common-but-harmless issues (missing meta descriptions) while ignoring rare-but-severe ones (broken canonicals).
- Deleting broken pages with backlinks — that link equity is wasted; redirect instead.
- Assuming schema improves rankings — it only unlocks rich result eligibility.
- Letting pages bloat past 2 MB with inline base64 images, embedded SVGs/JSON, inline CSS/JS — browsers render fine but Googlebot silently stops reading.
- Putting business-irrelevant pages in main navigation just for SEO (one site deliberately kept its glossary out of main nav).

## Key principles
- "The ones you see the most aren't necessarily the ones you should be losing sleep over."
- For a page to rank it must be crawlable, not noindexed, and canonical — three hard requirements.
- Page experience is a tiebreaker between pages of similar content quality, not a trump card.
- Duplicate content: "we won't show all of these pages" (John Mueller) — Google picks, possibly wrongly, unless you consolidate.
