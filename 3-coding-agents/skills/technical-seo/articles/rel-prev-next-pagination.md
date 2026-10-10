# Pagination SEO: Getting Paginated Series Right

- **Updated**: 2026-10-05

## TL;DR
Google stopped using rel=prev/next years before announcing it in 2019 — leave existing markup in place (it still has accessibility uses, and Bing has said it may use it as a hint). The acceptable implementations are self-referencing canonicals per page, or canonicalizing to a view-all page. The four ways sites break pagination: canonicalizing to page one, noindexing, nofollowing internal links, and blocking crawling — all orphan content and cut PageRank flow.

## Framework / Step-by-step
**If you already have rel=prev/next + self-referencing canonicals:** change nothing. Treat each paginated page as a normal indexable page and keep internal links between pages in the series.

**Acceptable implementations:**
1. Each page self-canonical, crawlable, indexable, interlinked within the series.
2. Paginated pages canonicalized to a "view-all" page containing the complete content (users still get pagination; the index gets the full page).

**If you believe paginated pages are low-value:** replace the pagination crawl path with topic-grouped category pages linked from the homepage — categories can rank for their topics. Note this usually requires a redesign, and you may still need pagination within categories.

**How Google identifies a series without rel=prev/next:** consistent headings, titles (same or with page numbers), and internal links between pages in the set.

## Actionable checklist
- [ ] Each paginated page has a self-referencing canonical (or all point to view-all)
- [ ] No canonicals from page 2+ pointing to page 1
- [ ] No noindex on paginated pages (check meta robots AND X-Robots-Tag headers)
- [ ] No nofollow on internal links between paginated pages
- [ ] No robots.txt Disallow on pagination paths (e.g., /blog/page/)
- [ ] Existing rel=prev/next markup left in place
- [ ] Internal links connect the pages in each series
- [ ] Category/topic hub pages linked from the homepage where pagination is replaced

## Data points & benchmarks
- Google publicly confirmed in 2019 that it had ignored rel=prev/next for years; Bing has said it may still use it as a hint (older statement).
- Nofollow became a "hint" in 2019 — best case it's ignored, worst case it throttles crawling and signal flow.
- Long-standing guidance for paginated duplicate blocks: "do nothing" — repeated content across a series triggers no penalty.

## Mistakes to avoid
- Canonicalizing every page in a series to page one — orphans everything after page 1 and cuts PageRank (only hope is Google ignoring the tag).
- Noindexing paginated pages — they drop from the index and their links eventually stop being followed/crawled.
- Nofollowing pagination links "to save crawl budget" — same orphaning effect.
- Blocking pagination paths in robots.txt — content becomes undiscoverable.

## Key principles
- Paginated pages are normal indexable pages: crawlable, followable, self-canonical.
- Removing working markup out of panic after a search engine announcement usually does more harm than the announcement itself.
- Alternate crawl paths (categories, sitemaps) are the safety net for any pagination strategy.
