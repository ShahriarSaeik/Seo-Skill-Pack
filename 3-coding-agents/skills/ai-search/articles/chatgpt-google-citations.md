# ChatGPT May Scrape Google, but the Citations Don't Match (3.3K Head Terms)

- **Updated**: 2026-10-05

## TL;DR
Even though ChatGPT is reported to use Google's results (a snapshot study; behavior changes), only ~10% of its short-tail citations match Google's top 10 URLs — it applies its own selection and re-ranking layer over retrieved results. Perplexity is the opposite: ~65% URL overlap, behaving as a citation-first engine that closely follows Google. Optimize to appear on both surfaces, with cluster coverage to win the domain-level selection game.

## Framework / Step-by-step
Study protocol (3,311 classic head terms across informational/commercial/transactional/navigational intent, run through ChatGPT, Perplexity, and Google's top 100):
1. **Run each head term** through each assistant and the SERP.
2. **Measure URL-level overlap** (cited URL appears in top 10 / top 100) and **domain-level overlap** separately.
3. **Compare across query types** — short-tail vs. long-tail vs. fan-out prompts.
4. **Explain the domain-URL gap** — assistants often pick a *different page* from the *same domain* Google ranks.

## Actionable checklist
- [ ] Build cluster content: multiple pages per topic so assistants can select the best-fit page from your domain
- [ ] Track cited URLs vs. ranking URLs per assistant — a ranking domain with zero citations is a page-selection gap
- [ ] Don't assume Google rankings transfer to ChatGPT — audit its citations separately
- [ ] For Perplexity specifically, classic SEO rankings transfer well — prioritize top-10 rankings there
- [ ] Expect higher AI/Google convergence on stable intents (navigational, transactional) and divergence on informational
- [ ] Cover fan-out sub-queries even though they show the lowest SERP overlap — that's where selection is widest open

## Data points & benchmarks
- ChatGPT short-tail: 10.0% URL overlap with top 10 (20.7% top 100); domain overlap 31.8% top 10 (53.5% top 100)
- ChatGPT cites ranking *domains* ~3x more than ranking *pages*
- Perplexity short-tail: 65.1% URL overlap with top 10 (72.9% top 100); domain overlap 80.6% top 10 (91.8% top 100)
- ChatGPT URL overlap by query type: short-tail 10% > long-tail 7.05% > fan-out 6.82%
- Perplexity long-tail overlap: 28.6% — again far more Google-aligned than ChatGPT
- Likely architecture: hybrid retrieval (Google SERPs + Bing + own index + third-party APIs) followed by a proprietary re-ranking pass

## Mistakes to avoid
- Treating "rank #1 on Google" as a ChatGPT citation strategy — selection happens post-retrieval
- Ignoring domain-level strength while chasing single-URL rankings
- Assuming one assistant's citation behavior generalizes to all (ChatGPT diverges; Perplexity tracks)

## Key principles
- Scraping ≠ echoing: retrieval is step one; the re-ranking layer decides who gets cited.
- Win the domain first, then give the model multiple best-fit pages to choose from.
- Search and AI are parallel discovery systems — build for both surfaces deliberately.
