# Schema Markup & AI Citations: A 1,885-Page Causality Test

- **Updated**: 2026-10-05

## TL;DR
AI-cited pages are ~3x more likely to carry JSON-LD schema than non-cited pages (53% vs ~18%) — but a controlled experiment on 1,885 pages that ADDED schema (vs 4,000 matched controls) found no citation uplift on any AI platform. The gap is correlation: sites that add schema also do everything else well. Don't buy "add schema for AI citations" as a tactic for pages already being cited.

## Framework / Step-by-step
1. **Audit why you're adding schema** — valid reasons: rich results, voice assistants, knowledge-graph/entity work. Invalid (per this data): boosting AI citations on already-cited pages.
2. **If you still want to test it, run a matched experiment:**
   - Pick 5-10 test pages with existing AI citations (baseline needed)
   - Pick 5-10 control pages with similar citation levels; change nothing on them
   - Record 30-day baseline citations per platform (an AI visibility tracker with URL filters)
   - Add JSON-LD to test pages only; change nothing else
   - Compare group deltas after 30+ days: treated must beat controls to count (controls absorb platform-wide trends)
3. **Redirect effort to what correlates causally** — retrieval relevance (titles, content, rankings) and brand mentions, not markup.
4. **One open case** — pages with ZERO AI citations weren't studied; schema might still help unseen pages get crawled/parsed initially. Keep basic entity/organization markup, skip mass rollout.

## Actionable checklist
- [ ] Drop "schema → AI citations" claims from roadmaps and client decks
- [ ] Keep schema where it earns rich results or supports entity disambiguation (note: FAQ rich results now appear only for well-known government/health sites, and HowTo rich results were removed in 2023)
- [ ] Ensure key facts appear in VISIBLE HTML text, not only in structured data (AI retrieval reads visible content)
- [ ] Run the 5-10/5-10 matched test before any sitewide schema project pitched as AEO
- [ ] Watch for follow-ups: schema-type-specific effects, JS-injected schema, 60-90 day windows

## Data points & benchmarks
- Prevalence: 53% of AI-cited pages have schema vs ~3x lower rate on non-cited pages (6M-URL analysis)
- Treatment effect (matched difference-in-differences): AI Overviews −4.6% (statistically significant but tiny: ~12 daily citations on a base of hundreds; unexplained), AI Mode +2.4% (indistinguishable from zero), ChatGPT +2.2% (indistinguishable from zero)
- Raw AI Mode before/after growth was +43% — but controls grew almost as much; platform boom, not schema
- Design: 1,885 pages adding JSON-LD (Aug 2025-Mar 2026), ~4,000 controls (3 per treated URL, matched on pre-period citations), 30-day windows, 4 independent statistical tests agreeing
- All treated pages already had 100+ AI citations pre-treatment (already inside the consideration set)
- Independent retrieval test (one test): five major AI systems (ChatGPT, Claude, Perplexity, Gemini, AI Mode) all ignored JSON-LD/microdata/RDFa during live fetches, extracting only visible HTML

## Mistakes to avoid
- Citing the "53% of cited pages have schema" stat as proof schema causes citations
- Making schema the centerpiece of an AEO pitch
- Changing schema + content + links simultaneously, then crediting schema for any movement
- Comparing before/after numbers without controls (platform trends swamp any real effect)
- Putting critical facts only in structured data that AI retrieval demonstrably skips

## Key principles
- Correlation artifacts: technically-maintained sites over-index on every good signal at once
- Isolate single-variable changes with matched controls or don't measure at all
- AI systems consume visible content at retrieval time; hidden metadata is mostly for traditional search features
- "Already cited" and "never cited" are different problems — interventions may work on one, not the other
