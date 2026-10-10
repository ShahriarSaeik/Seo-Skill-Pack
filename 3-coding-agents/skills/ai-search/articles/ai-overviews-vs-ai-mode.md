# AI Overviews vs. AI Mode: Same Conclusions, Different Sources (730K Responses Studied)

- **Updated**: 2026-10-05

## TL;DR
An industry study of 730K paired responses (a snapshot; both surfaces change often) found Google's AI Overviews and AI Mode agree on *what* to say (86% semantic similarity) while citing almost entirely *different* sources (only 13.7% citation overlap). They are two distinct retrieval systems, not short and long versions of one answer — so visibility in one does not carry to the other.

## Framework / Step-by-step
Study design you can reuse for any two AI surfaces:
1. **Capture paired responses** — same query set, one response per surface (540K pairs for citation analysis, 730K for similarity).
2. **Measure citation overlap** — share of URLs appearing in both responses.
3. **Measure word overlap** (Jaccard similarity on unique words) and **semantic similarity** (cosine similarity, 0–1).
4. **Count entities** — people, organizations, brands per response; check whether one surface's entities are a superset of the other's.
5. **Note single-generation caveat** — citations churn ~45% between generations, so real source pools overlap more than a single snapshot shows.

## Actionable checklist
- [ ] Track AI Overviews and AI Mode visibility as separate channels in reporting
- [ ] Audit which surface cites you today; expect only ~14% of citations to carry over
- [ ] Build semantic/topical authority (themes) rather than chasing exact phrases both surfaces restate anyway
- [ ] Publish comprehensive, encyclopedic-style reference content for AI Mode; video + community content for AI Overviews
- [ ] Expect wider competitor sets in AI Mode — prepare comparison and differentiation content

## Data points & benchmarks
- Citation overlap: 13.7% overall; 16.3% comparing only each surface's top 3 citations
- Word-level (Jaccard) overlap: 16%; identical first sentence: 2.51%; fully identical responses: 0.51%
- Semantic similarity: 86% average; 89.7% of pairs scored above 0.8
- AI Mode responses ~4x longer; 3.3 entities avg vs. 1.3 for AI Overviews
- 61% of the time AI Mode includes every entity the AI Overview mentioned, plus more
- No brand/entity at all: 59.4% of AI Overviews, 34.7% of AI Mode responses; 32.8% across both
- Missing citations: AI Overviews 11% vs. AI Mode 3%
- Source diets: Wikipedia 28.9% of AI Mode citations vs. 18.1% for AIOs; Quora 3.5x more and health/Facebook ~2x more in AI Mode; YouTube is the AIO favorite; AIOs cite videos and home/category pages ~2x more

## Mistakes to avoid
- Assuming an AI Overview citation guarantees AI Mode presence (or vice versa)
- Treating AI Mode as "AI Overviews but longer" — the retrieval paths and source preferences differ
- Ignoring the ~1 in 3 queries where no brand gets mentioned at all — pick entity-relevant queries to target

## Key principles
- Both surfaces use query fan-out with different models, so they converge on meaning from different evidence.
- AIO visibility is the gateway: entities that make the short answer usually get included (and diluted) in AI Mode's longer one.
- Optimize the shared semantic core once; customize the format and source strategy per surface.
