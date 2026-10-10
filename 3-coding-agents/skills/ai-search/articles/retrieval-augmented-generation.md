# Retrieval-Augmented Generation (RAG): How AI Picks and Cites Pages

- **Updated**: 2026-10-05

## TL;DR
RAG is the pipeline that decides which pages AI assistants search, read, and cite: (1) a classifier decides whether to search at all, (2) the query fans out into sub-queries against a search index, (3) pages are chunked and matched by embedding similarity, (4) the best chunks enter the context window, get used, and are purged. Most assistants' retrieval layers run on a traditional search index — so SEO fundamentals gate AI visibility, with new failure modes (JavaScript, slow TTFB, redundancy).

## Framework / Step-by-step
1. **Understand the gate: search-worthiness** — assistants skip retrieval for "timeless or stable" queries (a reportedly leaked system prompt shows a never_search command). Restating consensus knowledge earns zero citations; unique info (data, quotes, dates, numbers) is what triggers and wins retrieval.
2. **Know each platform's retrieval source** — Gemini/AI Overviews: Google Search. Copilot: Bing. ChatGPT: Bing (official) + Google results (suspected) + a building own index. Perplexity: own crawler/index. Claude: reportedly Brave Search. One platform underperforming usually means a platform-specific indexing/signal gap, not bad content.
3. **Pass the fetch test** — serve key facts in static HTML (not JavaScript tabs/accordions); don't block AI retrieval crawlers in robots.txt or firewall; audit CDN defaults (some block AI crawlers — and even multipurpose crawlers — out of the box).
4. **Win the metadata screen** — after search, the assistant shortlists pages to open based on title, snippet/summary, and URL, judged on relevance, authority, recency, and diversity of perspective. Some domains reportedly get a licensed "VIP lane" with pre-summarized near-full-text access.
5. **Win the chunk match** — page content is chunked; chunks whose embeddings are closest to the fan-out sub-query win. Specific, entity-dense, unambiguous language maps to better coordinates.
6. **Respect the clock** — retrieval fetches appear to run on a hard timeout (~2s observed for ChatGPT; TTFB under 1s is a safe target). Watch for HTTP 499s in server logs (client gave up); multiple unrelated bots abandoning the same URL = server problem, not bot behavior.
7. **Accept the purge** — retrieved chunks are deleted after the response; retrieval visibility is rented per query. RAG is influenceable in weeks; training-data presence ("what the model knows about you") is the slow, years-long work of entity coherence.

## Actionable checklist
- [ ] Put key facts (pricing, specs, definitions) in static HTML, not JS-rendered UI
- [ ] Verify AI retrieval crawlers aren't blocked (robots.txt, firewall, CDN defaults)
- [ ] Keep TTFB under 1s on priority pages; monitor 499 status codes from AI bots
- [ ] Front-load answers: first 30% of the page should carry definitions, key claims, unique data
- [ ] Structure content as question → immediate answer blocks
- [ ] Replace generics with named entities ("a study" → "a [year] [named university] study", using the real source)
- [ ] Add genuine information gain: proprietary data, quotes, statistics, dates, numbers
- [ ] Consolidate: assistants appear to dedupe by domain — one strong page per sub-topic beats 20 thin ones
- [ ] Refresh key pages regularly; add visible "last updated" dates (recency scoring is a documented system setting)

## Data points & benchmarks
- Citation position bias: first 30% of page content generates 44.2% of citations (middle third 31.1%, bottom 24.7%)
- Q&A-structured content is cited ~2x more than non-Q&A (18% vs 8.9%)
- Entity density in AI-cited content: ~20.6% vs 5-8% in average content
- Information gain experiment (older academic study): adding quotes and statistics lifted AI visibility 30-40% vs unoptimized copy; keyword stuffing REDUCED visibility
- Most citation-predictive entity types: dates and numbers; biggest ranking predictor across 150 pages: count of unique data points
- AI-cited URLs are 25.7% fresher than organic SERP URLs; some assistants order citations newest → oldest; freshness scoring is an explicit system configuration
- Fetch limits: ~2s grounding timeout, sub-1s TTFB safe; one site saw 43.7% of pages return 499 to a major assistant's user-agent
- Domain dedup: 20 thin pages on one domain = 1 chance; citations bind to specific sentences, so be the best support for a precise claim

## Mistakes to avoid
- Burying answers mid-page or hiding critical data behind JavaScript
- Publishing generalized knowledge pages ("the value is zero" when models answer from memory)
- Assuming a Google ranking guarantees AI visibility — each assistant has its own index and biases
- Ignoring 499s/slow TTFB: pages silently dropped from the context window never get cited
- Spreading one sub-topic across many weak pages instead of one authoritative page
- Treating a citation win as permanent — chunks are purged; every query re-competes

## Key principles
- RAG = retrieval layer over search engines; indexed, retrievable, well-structured content is the entry fee
- Assistants reward specificity (entities, numbers, dates) and penalize redundancy
- "Citations bind to a sentence, not a page" — precision beats breadth
- Retrieval is winnable in weeks; parametric memory (brand knowledge) is built over years
- Speed and accessibility are citation factors: content the bot can't fetch or parse can't be cited
