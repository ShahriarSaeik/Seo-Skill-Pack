# llms.txt: What a 137K-Site Server Log Study Actually Found

- **Updated**: 2026-10-05

## TL;DR
An industry study (a point-in-time snapshot) of 137K domains' server logs found llms.txt is decoration for AI search visibility: 28% of sites publish one, but 97% of files received zero requests in a month. AI retrieval bots (the ones powering answers in ChatGPT/Perplexity-style products) account for just 1.1% of the few requests that do happen. The only plausible audience today is AI coding agents reading developer documentation.

## Framework / Step-by-step
1. **Deprioritize llms.txt for AI visibility goals** — no major AI platform has committed to reading it; Google's search guidance says no special machine-readable AI files are needed to appear in its generative AI results.
2. **Check your own logs before investing** — filter bot analytics/server logs for URLs containing "llms.txt". A 97% chance of zero readership is the base rate.
3. **If you publish anyway, minimize effort** — let the CMS/website builder auto-generate it rather than hand-maintaining.
4. **Route agents to it** — agents fetch llms.txt when directed (linked from HTML, referenced in docs), never speculatively. An unlinked file will not be discovered.
5. **Treat the file like code** — version-control it, restrict edit access, alert on unauthorized changes, keep it to plain links/descriptions (nothing instruction-shaped), link only to resources you control. Prompt-injection probing of llms.txt files is already happening.
6. **Reconsider only if your audience is coding agents** — developer-docs-heavy sites are the one case where the file plausibly gets read (agentic tooling is the single biggest AI reader group, 10.5% of requests).

## Actionable checklist
- [ ] Audit whether anything actually fetches your /llms.txt before spending more time on it
- [ ] Don't create llms.txt expecting ChatGPT/Perplexity/AI Overview citations
- [ ] If publishing: link it from your HTML and documentation so directed agents can find it
- [ ] Exclude instruction-shaped content from the file (prompt-injection risk)
- [ ] Monitor 404s on /llms.txt — in the study that traffic was humans (not AI bots), so don't read it as AI interest
- [ ] Watch agent-layer developments: if agent-mediated search grows, reassess

## Data points & benchmarks
- 28% of 137K analyzed domains (~38,000 sites) publish an llms.txt — an upper bound (population skews technical/SEO-aware)
- 97% of published files received zero requests in the study month; the remaining 3% (~1.1K domains) got all traffic
- 96% of requests came from bots; only 4% humans
- Bot breakdown of requests: SEO audit tools 21.7%, unidentified scrapers 14.9%, general web crawlers 13.1%, tech-profiling 11.6%, AI agents 10.5%, AI-readiness scoring tools 5.8%, AI training crawlers 5.3%, llms.txt catalog bots 3.6%, link-preview bots 2.9%, research bots 2.7%, AI assistants 2.5%, AI retrieval bots 1.1%
- All AI bot types combined = 19.5% of requests (largest single bucket, but "fetched" ≠ "read" — every figure is a ceiling)
- Training crawlers fetch llms.txt ~5x more than AI retrieval bots; a link-preview bot (chat app unfurling) out-fetched Perplexity's crawler
- Requests to nonexistent llms.txt files (404s): 0% from AI bots, 98% human
- A browser performance audit that checks for llms.txt produced ~1 in 1,000 fetches
- Per the study, no dedicated Gemini crawler was seen: Google grounds Gemini via its regular search crawler, so llms.txt fetches by it are routine indexing, not interest

## Mistakes to avoid
- Publishing llms.txt as an "AI visibility" tactic and reporting it as progress
- Assuming a fetched file was read or acted on
- Leaving the file unlinked and expecting discovery
- Letting auto-generated platform files go unreviewed (stale/compromised files mislead every agent that trusts them)
- Ignoring the prompt-injection attack surface of a file agents are built to trust

## Key principles
- Adoption is being driven by speculation, not by any confirmed consumption by AI platforms
- Agents fetch what they are directed to; retrieval bots don't hunt for files that aren't there
- The realistic reader of llms.txt today is a coding agent, not an AI search engine
- Cheap tactics with ~97% no-op rates still carry real (security/maintenance) costs
