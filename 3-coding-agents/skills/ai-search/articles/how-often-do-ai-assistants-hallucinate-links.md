# How Often AI Assistants Hallucinate Links (16M-URL Study)

- **Updated**: 2026-10-05

## TL;DR
An industry study of 16M AI-cited URLs found assistants send visitors to 404 pages 2.87x more often than traditional search (0.43% vs 0.15% baseline). ChatGPT is the biggest offender: 1.01% of clicked URLs and 2.38% of all cited URLs are dead — often plausible-looking URLs that never existed. Fix: mine analytics for AI-referred 404s and 301-redirect them to real equivalents.

## Framework / Step-by-step
1. **Filter analytics for AI-referred traffic** — apply a regex to session source (match the major assistant domains/bots); or use an analytics tool with a built-in AI-channel filter.
2. **Check HTTP status of referred URLs** — script a status checker (or run a crawler) against the exported URL list.
3. **Filter to 404s with meaningful visits** — e.g., >10 visitors/month; manually confirm they're hallucinated (plausible pattern, never a real page) vs genuine dead pages.
4. **301-redirect hallucinated URLs to real equivalents** — the URL slug usually reveals intent (a hallucinated /blog/keywords/ page → your real keyword-research guide).
5. **Fallback: upgrade the 404 page** — if redirect sprawl isn't worth it, put popular content and key conversion paths on the 404 template for stranded AI visitors.
6. **Keep perspective** — AI referral traffic is still small; this is a cheap hygiene fix, not a growth lever.

## Actionable checklist
- [ ] Pull 90 days of AI-referred URLs from analytics
- [ ] Resolve HTTP statuses; list 404 URLs receiving >10 visits/month
- [ ] Verify each is truly hallucinated (not a deleted real page)
- [ ] 301 hallucinated URLs to closest real pages
- [ ] Enrich the 404 template with top content + newsletter/signup links
- [ ] Never move/delete URL patterns assistants commonly cite without redirects
- [ ] Re-check quarterly; new hallucinations accumulate

## Data points & benchmarks
- Clicked-URL 404 rates by assistant: ChatGPT 1.01% (84K of 8.3M URLs), Claude 0.58%, Copilot 0.34%, Perplexity 0.31%, Gemini 0.21%, Mistral 0.12%
- Average assistant 404 rate 0.43% vs Google-referrer baseline 0.15% → 2.87x
- Cited-URL 404 rates (including unclicked): ChatGPT 2.38%, Perplexity 0.87%, Gemini 0.86%, Copilot 0.54%; Google top-20 baseline 0.84%
- Perplexity/Gemini ≈ the search-index baseline (they retrieve live from a search index) — ChatGPT's gap is true hallucination + stale internal knowledge
- Common hallucination shape: URLs that fit a site's pattern but never existed (e.g., /blog/newsletter/, /blog/internal-links/)
- Contributing factor: AI-generated content containing hallucinated URLs gets crawled and re-cited (74% of newly created webpages contained some AI-generated content in an April 2025 study)
- Scale context: in the study's sample, assistants ≈ 0.25% of average site traffic vs ~39% from Google — impact is real but small (check your own share)

## Mistakes to avoid
- Assuming every AI-referred 404 is a "bug" — some are your own un-redirected URL changes
- Building dozens of redirects for URLs with negligible visits
- Leaving the default 404 template up for AI visitors who were promised real content
- Ignoring hallucinated URLs entirely — they represent lost, high-intent visitors
- Forgetting that assistants cite from stale memory: pages deleted years ago still get cited

## Key principles
- Hallucinated URLs follow your site's naming patterns — predictable, findable, redirectable
- Assistants relying on live search indexes hallucinate less than those leaning on parametric memory
- Every un-redirected URL move creates future hallucination surface
- Low-effort hygiene beats elaborate prevention
