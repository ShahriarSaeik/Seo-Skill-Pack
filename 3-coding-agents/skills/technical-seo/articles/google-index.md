# How to Get Google to Index Your Website

- **Updated**: 2026-10-05

## TL;DR
Google only indexes pages it deems valuable — not everything it crawls. Get indexed by requesting indexing in Search Console, submitting a sitemap, ensuring sound internal-link structure (no orphans), and building backlinks. Still not indexed? Troubleshoot noindex tags, canonicals, crawl blocks, thin content, manual actions, and crawl budget.

## Framework / Step-by-step
**Check indexation first:** `site:yourwebsite.com` for rough count; Search Console URL Inspection tool for exact per-page status ("URL is on Google" / "URL is not on Google").

**4-step indexing playbook:**
1. **Request indexing** for homepage via Search Console URL Inspection (a hint, not a guarantee) → Google crawls outward through your structure
2. **Create + submit sitemap** — platforms auto-generate (yourdomain.com/sitemap.xml or sitemap_index.xml); WordPress: use an SEO plugin to control sitemap contents, since defaults may include low-value pages; submit in the Search Console Sitemaps report
3. **Structure site properly** — pyramid structure; every page linked from at least one page above it; audit for orphan pages (a site audit crawler)
4. **Build backlinks** — new sites: study competitors' links (link-intersect / common-backlinks analysis: relevant directories, listicles, podcasts) and earn similar ones through genuine editorial opportunities; paid or exchanged links need rel="sponsored"/nofollow

**Timeline:** new sites = days to months; new pages on established sites = hours. Factors: popularity, authority, quality, structure, technical health.

## Actionable checklist
- [ ] Search Console property set up; homepage + key pages "Request indexing"
- [ ] Sitemap submitted in Search Console; only important pages included
- [ ] No orphan pages (every indexable page has internal links)
- [ ] Backlink acquisition started (link-intersect report for quick wins)
- [ ] Troubleshooting if still unindexed:
  - [ ] No rogue noindex tags/meta (site crawler indexability check)
  - [ ] No manual actions or security issues (Search Console reports)
  - [ ] Content is genuinely valuable (thin-content heuristic: indexable pages with no rankings and little unique content; word count alone isn't a quality signal)
  - [ ] Indexable pages present in sitemap (crawler's "indexable page not in sitemap" check)
  - [ ] No robots.txt crawl blocks (robots.txt report (Search Console → Settings) + URL Inspection)
  - [ ] No rogue canonicals (Search Console "Alternate page with proper canonical tag" status / non-canonical URLs listed in the sitemap)
  - [ ] No nofollow-only internal links to the page
  - [ ] Add internal links (from an internal link opportunities report) then Request indexing again
  - [ ] Prune low-quality pages to protect crawl budget

## Data points & benchmarks
- New site indexing: a few days to several months; established site new pages: hours.
- Thin-content heuristic: no keyword rankings and little unique content (not a fixed word count).
- Google guidance: crawl budget mainly matters for very large sites (roughly 1M+ pages) or large sites with fast-changing content.
- Google never indexes all known URLs — pages must be "awesome and inspiring" (Mueller).
- Changing dates without real content improvements is manipulative and gives no benefit.
- Googlebot crawls fresh/changing pages more often than static ones.

## Mistakes to avoid
- Leaving the default WordPress sitemap unchecked (it may include unimportant pages).
- Letting pages go orphaned and expecting sitemap submission alone to work.
- Fake "freshness" (updating timestamps without improving content) — manipulative and ineffective.
- Keeping nofollow on internal links to pages you want indexed.
- Sending conflicting signals (non-canonical pages in sitemap).
- Ignoring content quality — indexing requires perceived value, not just crawlability.

## Key principles
- "Being indexed doesn't mean you'll rank — it means you're in the game, not that you're winning."
- Indexing = discoverability (links, sitemaps) + perceived value (backlinks, quality).
- Internal links do double duty: discovery + importance signals (PageRank).
- For most sites, the basics (Search Console + sitemap + sound structure) get you indexed; the rest is quality and authority.
