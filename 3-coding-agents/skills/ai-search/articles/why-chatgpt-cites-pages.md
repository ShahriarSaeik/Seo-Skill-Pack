# Why ChatGPT Cites One Page Over Another (1.4M-Prompt Study)

- **Updated**: 2026-10-05

## TL;DR
An industry study of 1.4M ChatGPT prompts found the model retrieves ~33 URLs per prompt but cites only ~half. Citation is gated by retrieval-channel (88% of cited URLs come from the general web-search pool), title-to-query semantic relevance (cited titles scored 0.602 vs 0.484 cosine similarity against the prompt, and 0.656 against the best-matching fan-out query), and readable URL slugs. Reddit is consumed heavily for context but almost never credited via its dedicated feed.

## Framework / Step-by-step
1. **Get into the web-search pool first** — ChatGPT's citation pipeline is dominated by general search results (88.46% citation rate in that channel vs 1.93% for the dedicated Reddit feed, 0.5% YouTube, 0.4% academic). Ranking in regular search is the entry ticket.
2. **Pass the gatekeeping layer** — the model screens candidates on retrieval metadata (title, snippet, URL) BEFORE opening page content. Optimize the title as the primary citation asset.
3. **Align titles with fan-out sub-queries** — map the sub-questions ChatGPT generates from a seed prompt; write titles that closely match the best-aligned sub-question, not just the original prompt (keep them natural and accurate to the page; don't stuff keywords).
4. **Use natural-language URL slugs** — descriptive slugs (keyword-bearing, human-readable) beat opaque URLs on citation rate.
5. **Earn establishment, not just freshness** — within a single retrieval set, older established pages beat brand-new ones; freshness becomes the tie-breaker only in news-type queries.
6. **Diagnose citation gaps** — compare your pages vs competitors' cited pages on: does it rank in search? does the title match the fan-out queries? is the slug readable?

## Actionable checklist
- [ ] Pull fan-out queries for priority prompts (from an AI visibility tracker or by inspecting the searches the assistant shows)
- [ ] Rewrite page titles to semantically mirror the top fan-out sub-questions
- [ ] Convert opaque/ID-based URL slugs to short descriptive slugs on key pages
- [ ] Check each target page ranks in the top web results for its fan-out queries
- [ ] For news content: publish fast and refresh — recency decides when relevance ties
- [ ] For evergreen content: build page age + accumulated authority; don't churn URLs
- [ ] Run competitor citation-gap analysis: prompts where rivals are cited and you're retrieved-but-not-cited

## Data points & benchmarks
- ~16.6 cited vs ~16.6 non-cited URLs per prompt; overall ~50% of retrieved URLs get cited
- Citation rate by retrieval channel: search 88.46%, news 12.01%, reddit 1.93%, youtube 0.51%, academia 0.40%
- 88% of ChatGPT citations come from the general search pool
- Reddit = 67.8% of all non-cited URLs (16M+ data points) — consumed for consensus, rarely credited
- Cosine similarity (title vs prompt): cited 0.602 vs non-cited 0.484; title vs best fan-out query: 0.656
- Natural-language slugs: 89.78% citation rate vs 81.11% for non-descriptive slugs
- Median cited page age ~500 days (~1.3 years); some cited pages 2,700+ days old; platform-wide freshness skew is increasing (median was ~958 days a year earlier)
- News queries: cited pages median ~200 days old vs ~300 for non-cited — recency is the tie-breaker when relevance is equal
- Snippet/pub-date metadata showed no reliable citation signal once retrieval-channel composition was controlled for
- Observational data: these are correlations from one study, not tested causes

## Mistakes to avoid
- Optimizing body content while ignoring the title/URL gatekeeping layer that decides whether content is opened at all
- Assuming Reddit presence alone earns citations — it shapes the answer but rarely gets the credit
- Chasing freshness on evergreen topics: a brand-new page that mismatches fan-out queries gets retrieved and dropped
- Comparing cited vs non-cited URL sets without separating retrieval channels (composition artifacts create fake "findings")
- Leaving key pages outside the top web results and expecting citations from vertical feeds

## Key principles
- ChatGPT is an aggressive editor: retrieval ≠ citation; the funnel is channel → metadata screening → page read → citation
- Titles are matched against internal fan-out sub-questions, not the user's prompt
- Relevance does the heavy lifting; freshness only breaks ties
- Established, semantically-aligned pages win; the AI "learns from the crowd, then cites another institution"
