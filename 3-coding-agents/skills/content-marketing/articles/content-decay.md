# What Is Content Decay? (And How to Fix It Before It Tanks Your Traffic)

- **Updated**: 2026-10-05

## TL;DR
Content decay is the slow, invisible decline of a page's organic traffic and rankings over months/years. Every article follows the same lifecycle (traction → growth → peak → plateau → decline); catch decay early via quarterly audits, then choose the right fix: update, consolidate, redirect, prune, or rewrite.

## Framework / Step-by-step
**Causes:** age/freshness (Google QDF; AI systems even more recency-biased), competitor improvement, search intent shift (e.g., "LLM" law degree → large language model), internal keyword cannibalization (similar articles split authority; newest quietly overtakes oldest).

**Finding decaying content:**
1. In any SEO tool's top-pages data, filter for pages with declining organic traffic over a 12-month range, keep winnable keywords (e.g., KD under ~40, lower for newer sites), and sort by largest negative traffic change
2. Check each page's change history (CMS revisions, deployment log): declined with NO preceding changes = classic decay (refresh); declined AFTER a change = you broke it (restore previous version)
3. Search Console Performance (3 months vs. prior year): both impressions+CTR down = decay; impressions flat + CTR down = SERP feature problem, not decay
4. Prioritize backlog by: business relevance, historical traffic peak, winnable KD. Low on all three → prune.

**Decision framework:**
| Situation | Action |
|---|---|
| Keyword still relevant; content outdated | Update/refresh |
| Two pages competing, one stronger | Consolidate weaker into stronger + 301 |
| Keyword off-strategy; page has backlinks | Redirect (preserve "link magnets" — move cited stats/quotes to the destination) |
| Low value, minimal traffic/links | Prune (noindex = reversible; delete = not) |
| Poorly optimized from start; topic competitive | Rewrite from scratch |

**Fixing (6 steps):** topical gap analysis (any content-optimization tool or manual SERP comparison) → update stale data/examples (one SaaS brand automated refreshes with LLM agents plus human review: 4x pace, 25% more articles, sustained traffic upticks) → align with current intent (review the live SERP: for "how to start a blog" one analysis found the mix shifting from 34% Reddit/27% guides to 60% Reddit — may require structural rewrite or genuine, disclosed forum participation) → strengthen on-page signals (title/meta, which AI assistants may also read when choosing citations; internal links from high-authority pages; site audit issues) → check AI visibility separately (manual prompt checks or an AI visibility tracker; rankings can recover while AI citations don't) → re-promote (email, social, expert contributors = engineered distribution).

**Prevention:** quarterly decay audit (flag >20% YoY drops); set keyword/rank alerts on key keywords (early competitor warning); annual scheduled reviews of top articles; build clusters not silos (check new posts against existing keywords — differentiate or merge).

## Actionable checklist
- [ ] Save a recurring "declining pages" view (declining traffic + winnable KD); review quarterly
- [ ] Diagnose each page: decay vs. self-inflicted vs. SERP-feature problem
- [ ] Apply the 5-row decision framework before touching content
- [ ] Refresh: fill topic gaps, update every stale stat, re-check intent, fix on-page, re-promote
- [ ] Verify AI citations separately after refresh
- [ ] Only update publish dates with genuine content improvements

## Data points & benchmarks
- One study found AI-cited URLs ~25.7% fresher than classic SERP results; another claimed artificially refreshed dates moved AI ranking positions, but faking dates is unreliable and risky (see Mistakes)
- Google rewrites a large share of title tags/meta descriptions (older studies; figures vary) — but overperforming originals tend to be kept
- "How to start a blog" SERP: Reddit share grew 34% → 60% in one year in one analysis
- One consultant's case: deleting 60%+ of a real estate site's articles → notable click boost for remaining pages (single case)
- One SaaS brand: 2,000+ articles; semi-automated LLM refreshes quadrupled pace at a fraction of the cost
- Quarterly audit threshold: >20% YoY traffic decline

## Mistakes to avoid
- Refreshing pages whose real problem is link authority (content fixes won't help)
- Refreshing a page you broke with a bad update — restore instead
- Consolidating without the 301 redirect (loses link equity)
- Changing dates without meaningful content changes — search engines can detect trivial edits, so it may be ignored or erode trust (misleading freshness signals risk further decay)
- Ignoring cannibalization — new posts silently killing old ones
- Treating SERP-feature CTR loss as decay

## Key principles
- "Every piece of content you've ever published is slowly dying."
- Decay now has two dimensions: Google rankings AND AI answer presence — check both separately.
- The question is whether you find decay at -20% or -80%.
- Modest annual updates are far cheaper than rescuing a page that lost 60% of traffic.
