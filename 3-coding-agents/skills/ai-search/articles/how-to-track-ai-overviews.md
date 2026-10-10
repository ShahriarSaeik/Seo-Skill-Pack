# How to Track AI Overviews: Mentions, Citations, Click Loss, and the Traffic Google Won't Show You

- **Updated**: 2026-10-05

## TL;DR
Google hides AI Overview data (blended into google/organic or no-referrer), so track indirectly: citations via third-party tools, keyword wins via SERP-feature filters and alerts, mentions via monitoring, traffic via `#:~:text=` fragment workarounds in GA4, and click loss via before/after CTR comparisons around rollout dates. AIOs change constantly (content 70%, citations 46% of the time) but underlying meaning is stable (cosine similarity 0.95) — directional tracking works.

## Framework / Step-by-step
1. **Track citations** — an AI-citations snapshot from a backlink or SEO tool (history, per platform); an AI visibility tracker for prompts, responses, citation competitors. Find citation gaps: pages/queries where the cited domains include a competitor but not you.
2. **Track AIO keyword wins** — current: filter your ranking-keywords data by SERP feature (target cited in AI Overview). New wins: rank-tracking alerts or a date-range comparison (included now vs. not included before). Opportunities: keyword research data filtered to AIO keywords where you don't rank top 10/100, sorted by growth; an AI visibility tracker's "not mentioned + not cited" view for competitor-claimed AIOs. Add those queries to a rank tracker.
3. **Track mentions** — an AI visibility tracker: mention counts/trends, response context/sentiment, AI share of voice, cross-platform patterns (consistency across platforms = topical authority). Track YouTube/Reddit/TikTok/web mentions (feed signals). One YouTube video generated 30 brand mentions in AIOs.
4. **Track AIO traffic** — `#:~:text=` URL fragments appear on some AIO clicks (esp. long-tail). GA4 can't see fragments (client-side): use a tag manager custom JavaScript variable → event parameter → custom dimension (a published community method). Caveat: featured snippets/PAA clicks bundle into same data.
5. **Track click loss around rollouts** — in Search Console: include informational regex (`^what |^how |^why ... |guide|tutorial|definition|vs`), exclude branded + commercial terms; compare month after rollout vs. before. Validation: filtering actual AIO keywords (from an AI visibility tracker) produced nearly identical CTR drops (44% vs 42% relative).
6. **CTR drops without ranking loss ("great decoupling")** — stable position + flat or rising impressions + falling CTR = on-SERP answering. Use to: diagnose correctly (SERP behavior, not SEO failure), decide keep/drop keywords, manage client expectations, re-angle content (defend comparison queries; abandon fully-SERP-satisfiable definitional ones).
7. **DIY trackers** — an AI coding assistant + a SERP/SEO data API: weekly snapshots, AIO coverage %, citation rank, daily citations, share-of-voice chart. Limits: API costs and free-tier caps, no keyword discovery, no response/mention data.

## Actionable checklist
- [ ] Baseline: AI citations count + trend chart from a backlink/SEO tool
- [ ] Set alerts for new AIO keyword wins (weekly)
- [ ] Run date-range comparison monthly; report new AIO keywords won (one example site: 699 in a month)
- [ ] Build an AIO opportunity list (keyword research data sorted by growth, where you don't rank)
- [ ] Add competitor-claimed AIO queries (not mentioned/not cited) to a rank tracker
- [ ] Set up GTM `#:~:text=` tracking if GA4-based
- [ ] Run rollout-date CTR analysis (regex filters; e.g., May 2025 vs. April 2025)
- [ ] Document the "CTR down, ranking flat" Search Console filter setup (query regex, date comparison); re-run monthly
- [ ] Report mentions + SOV, not just citations

## Data points & benchmarks
- AIO content changes 70% of the time; citations change 46%; but cosine similarity 0.95 between consecutive responses (meaning stable)
- Example rollout analysis: CTR fell 3.76pp = 42% relative (regex-guessed AIO keywords) vs. 3.98pp = 44% (confirmed AIO keywords) — close agreement suggests the regex method is a reasonable proxy
- One widely cited study: 150K AIO keywords vs. 150K non-AIO informational — position #1 CTR fell 34.5% (0.040 → 0.026)
- ~99% of keywords that trigger an AI Overview are informational (not the same as ~99% of informational keywords triggering one)
- May 2025: AIOs expanded to 200+ countries, 40+ languages
- One example site won 699 new AIO keywords in one month
- Search Console regex examples: include `^what |^how |^why |^when |^where |^who |^which | guide|tutorial|definition|examples?|vs.?|versus| best way|difference between|meaning of`; exclude `price|pricing|cost|cheap|buy|discount|coupon|review`

## Mistakes to avoid
- Expecting exact AIO click attribution from Google — it doesn't exist; use indirect signals
- Panicking over AIO volatility — track directionally over time, not single snapshots
- "Fixing" pages when CTR drops with stable rankings — it's SERP behavior, not an SEO problem
- Defending definitional queries fully answered on-SERP; do defend comparison queries where buyers click deeper
- Over-investing in vibe-coded trackers for scale (API limits, no discovery)

## Key principles
- "Search results have morphed from directories into destinations."
- Three tracking questions: Visibility (where appearing/missing), Opportunity (what still delivers ROI), Impact (what AIOs cost you)
- Mentions are the visibility metric; citations are the authority metric; CTR delta is the cost metric
- Start tracking now — early movers gain advantage as AI search matures
