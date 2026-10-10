# What We Actually Know About Optimizing for LLM Search

- **Updated**: 2026-10-05

## TL;DR
LLM search optimization is largely SEO + brand marketing with new mechanics. Seven evidence-based tactics: third-party brand mentions (quality > volume), LLM-friendly structure (BLUF, logical HTML, no forced chunking), long-tail content clusters, optimizing for commands (75% of AI prompts are tasks, not questions), freshness, AI crawler access, and per-platform diversification (each LLM cites different sources — 86% don't overlap).

## Framework / Step-by-step
1. **Third-party presence** — branded web mentions are among the strongest AIO correlations (0.664). Focus quality: one brand got consistent AI mentions from just a handful of top-tier press placements. Mentions on highly-linked pages correlate ρ~0.70 (AIOs), high-traffic pages ρ~0.55. Build via PR/content partnerships (find targets via a cited-domains view or manual prompts), reviews/community, consistent brand messaging ("share of memory" — track co-mentions). Prioritize topics that can't be discussed without mentioning your product.
2. **Structure for LLMs** — Analysis of Chrome's page-embedding code suggests only the first ~30 passages are considered (unconfirmed): front-load key content, split mega-articles into focused pieces. Tree-walking algorithm follows semantic HTML structure. 200-word passage chunks: structure matters, but DON'T force "chunking" or status-update style; overlap_passages is built in — write naturally with logically grouped paragraphs.
3. **Long-tail clusters** — average ChatGPT prompt = 42 words; fan-out multiplies sub-queries. Mine prompts from competitor-gap analysis; Search Console query filters containing `/overview` or `/search` may reveal AI Mode long-tails (an unverified theory). Build topic clusters with question coverage, not single-keyword pages.
4. **Optimize for commands** — 75% of AI prompts are commands. Action mapping: find tasks by filtering competitor and keyword data for action verbs ("make", "track", "create", "generate") and "how to/can" queries; build jobs-to-be-done content (templates, calculators).
5. **Freshness** — AI-cited content is 25.7% fresher; 13.1% preference for recently updated. One SaaS brand reported 1,135 new AI Overview mentions after updating one post (anecdotal; may not be causal).
6. **Crawler access** — ~5.9% of sites blocked GPTBot in one snapshot; check robots.txt + firewall; verify via server logs or your CDN's bot analytics.
7. **Diversify per platform** — Google: own ecosystem (YouTube) + Reddit/Quora. ChatGPT: publishers/news (Reuters, AP). Perplexity: diverse, global, niche sites. Per-platform playbooks: e.g., one site got cited in AIOs via third-party listicles on a single publisher, ChatGPT via listicles on a major tech publication, Perplexity via competitor "vs" content — tailor outreach/content per engine.

## Actionable checklist
- [ ] Check citation gaps per platform; build platform-specific mention strategies
- [ ] Front-load key content within first 30 passages; split unwieldy long-form
- [ ] Fix heading hierarchy (proper H1→H2→H3 order)
- [ ] Mine competitor-gap prompts + Search Console /overview /search filters for long-tail ideas
- [ ] Map customer actions; create task-support content
- [ ] Update priority pages substantively; measure AIO mention change
- [ ] Verify AI bots aren't blocked (robots.txt, WAF, CDN)
- [ ] Track co-mentions (brand + topic) share over time

## Data points & benchmarks
- Branded web mentions → AIO visibility correlation: 0.664; branded anchors 0.527; site pages 0.17 (75K brands)
- Mentions on highly-linked pages: ρ~0.70 (AIOs), ~0.4 (Perplexity), ~0.1 (ChatGPT)
- Average ChatGPT prompt: 42 words; 75% are commands (one analysis of 1,800 real conversations)
- AI-cited content 25.7% fresher than organic; +13.1% preference for recently updated
- Only 7 of top-50 most-cited domains appear across AIOs, ChatGPT, AND Perplexity — 86% unique per assistant
- ~5.9% of websites disallow GPTBot
- Chrome embedding (from code analysis, unconfirmed): first 30 passages only; 200-word DocumentChunker passages; overlap_passages parameter handles chunk-boundary context

## Mistakes to avoid
- Chasing mentions for volume — quality placements on authoritative/linked/trafficked pages compound; volume alone doesn't
- Forced "chunk optimization" or status-update-style writing — AI handles overlap natively
- Wasting early passages on intros/boilerplate (30-passage ceiling)
- One-size-fits-all strategy — winning in Google AIOs ≠ winning in ChatGPT/Perplexity
- Accidentally blocking AI crawlers

## Key principles
- "SEO is very much not dead — in fact it's doing a lot of the heavy lifting": AI assistants lean heavily on search indexes for retrieval
- LLM search = goal shifts from ranking pages to being discoverable + extractable in answers
- Share of memory: consistent messaging repeated across web → more mind-space in customers AND LLMs
- Relevance is key: off-site content must align with your product and story
