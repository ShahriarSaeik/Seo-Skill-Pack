# AI Overview Click Loss Worsened: Position-1 CTR Down 58% (Study Update)

- **Updated**: 2026-10-05

## TL;DR
A re-run of the click-loss study (300K keywords: 150K with an AI Overview present, 150K informational keywords without) using aggregated Google Search Console data found that AI Overviews correlate with a ~58% lower average CTR for the top-ranking page — up from ~34.5% in the earlier April 2025 measurement. For every 100 clicks a #1 page historically earned, ~58 are now absorbed by the answer itself.

## Framework / Step-by-step
How the impact was measured (replicable protocol):
1. **Match two keyword samples** — keywords triggering an AI Overview vs. informational keywords without one (same baseline period, pre-rollout).
2. **Pull aggregated CTR per keyword** (sum of clicks / sum of impressions, desktop, per month) from Search Console.
3. **Compare pre/post periods** — December 2023 (pre-AI Overviews) vs. December 2025.
4. **Build the counterfactual** — use the CTR decline of non-AIO informational keywords to forecast what AIO-keyword CTR would have been without AI Overviews, then compare forecast vs. actual.

## Actionable checklist
- [ ] Re-baseline traffic forecasts: assume ~half of historical position-1 click volume on AIO-triggering queries
- [ ] Segment keywords by AI Overview presence in rank tracking before diagnosing traffic drops
- [ ] Prioritize query types where clicks still escape the SERP (transactional, navigational, tools, comparison)
- [ ] Shift AIO-query KPIs from clicks to citations, mentions, and assisted conversions
- [ ] Re-run this comparison quarterly — the loss grew between the two measurements; check whether it is stabilizing

## Data points & benchmarks
- Position-1 CTR on AIO keywords: 0.073 → 0.016 (Dec 2023 → Dec 2025); informational control: 0.076 → 0.039
- Counterfactual CTR without AI Overviews: ~0.037 vs. actual ~0.0157 → **-58%**
- Prior measurement (April 2025): -34.5% — the measured loss grew by ~23 points in ~9 months
- CTR impact by position: #1 -58%, #2 -50.8%, #3 -46.4%, #4 -38.8%, #5 -32.6%, #6 -30.5%, #7 -29.7%, #8 -28.8%, #9 -29.7%, #10 -19.4%
- ~9% of AI Overviews appear below position 1 (as low as position 6) — the penalty persists there too
- Independent analyses corroborate: 47.5%–65.2% organic CTR declines; one major publisher reported 80–90% (methods differ; treat as directional)

## Mistakes to avoid
- Treating the first click-loss measurement as final — the measured loss grew as AI Overviews expanded and CTRs kept falling
- Blaming content quality for CTR declines on queries where an AI Overview answers the intent
- Extrapolating the -58% to all keywords — it applies to AIO-triggering queries specifically

## Key principles
- AI Overviews act as a structural click tax on informational rankings; plan for continued decline.
- Non-AIO informational CTR also fell (~49%) — the whole informational SERP is going zero-click.
- Optimize AIO queries for visibility and citation; optimize click-worthy intents for traffic.
