# What "Crawled - Currently Not Indexed" Means In Search Console

- **Updated**: 2026-10-05

## TL;DR
"Crawled - currently not indexed" = Google visited the page but chose not to index it — usually a content-quality judgment. Unlike "Discovered" (not yet crawled), here Google has seen the content and deemed it not valuable enough. Fix quality first; technical issues second.

## Framework / Step-by-step
**Diagnosis — 3 cause categories:**
1. **Content quality (most common):** thin/low-quality content, duplicate/near-duplicate content, content lacking relevance to user intent
2. **Technical issues:** noindex tags, robots.txt blocks, canonicalization errors, server errors (404/500)
3. **Other factors:** crawl budget limits (large sites), weak overall site trust/quality signals (Google is more selective on new or low-quality sites), slow page speed, poor architecture/internal linking

**Fix sequence:**
1. Improve content quality — unique, valuable, in-depth; remove duplication
2. Verify technical setup — no misplaced noindex; robots.txt not blocking; canonicals correct; no server errors
3. Optimize architecture + internal linking — logical structure; link to important pages from relevant content
4. Request re-indexing via Search Console URL Inspection after fixes
5. Be patient; monitor Search Console Page Indexing report over time

Note: pages can move INTO this status after previously being indexed (quality reassessment) — it's one of several Search Console indexing statuses.

## Actionable checklist
- [ ] Compare affected pages vs indexed pages: what's different (depth, uniqueness, length)?
- [ ] Check for near-duplicates among affected URLs
- [ ] Remove stray noindex tags / robots blocks / bad canonicals (site crawler)
- [ ] Fix 404/500 errors
- [ ] Strengthen internal links to affected pages
- [ ] Improve or consolidate thin content
- [ ] Request re-indexing after fixes
- [ ] Re-check Search Console Page Indexing report periodically

## Data points & benchmarks
- Google indexes selectively — pages must be deemed valuable enough for search results.
- Search Console status taxonomy: indexed / discovered-not-indexed / crawled-not-indexed (this one = quality signal post-crawl).
- New or low-quality sites tend to face stricter selectivity.

## Mistakes to avoid
- Treating this as a crawl problem (it's usually a quality judgment — Google already crawled it).
- Re-requesting indexing repeatedly without changing anything.
- Ignoring duplicate content among the affected pages.
- Forgetting that previously-indexed pages can regress into this status.

## Key principles
- "Crawled currently not indexed typically points to some kind of quality issue. Fix that, and the pages marked with this issue will likely be indexed."
- Discovered = crawl prioritization issue; Crawled = content value issue.
- Indexing is selective by design, especially for new or low-quality sites.
