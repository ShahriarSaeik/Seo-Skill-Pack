# How to Do a Basic Backlink Audit (in Under 30 Minutes)

- **Updated**: 2026-10-05

## TL;DR
Run a backlink audit before taking on any site (like a home inspection before buying): check for spam/penalty risks AND mine opportunities. Three phases: a site-level health check (growth curve, spikes, country-code TLDs, anchors), deeper dives (wasted links, worst/best referrers, anchor spam, PBN footprints), then a page-level backlink review to find linkable patterns you can replicate.

## Framework / Step-by-step
**Setup**: a backlink analysis tool, set to the whole domain including subdomains (or a URL prefix for a subfolder).

**Phase 1 — High-level view (site-level overview):**
1. Compare backlinks + referring domains vs competitors (RDs = key metric; e.g., one competitor's blog ~8x another's RDs)
2. Check RD growth curve over time vs competitors (cumulative slope + absolute gains — e.g., competitor A +7,230 RDs/2yr vs competitor B +1,811)
3. Spot link SPIKES — they can signal a negative SEO attack or a paid campaign (e.g., one blogger's mid-2014 spike+drop); Google usually ignores such links, but extreme cases may warrant disavowing
4. Country-code TLD distribution: disproportionate .cn/.gq-type links look unnatural (context matters — .cn is normal for Chinese businesses; ~2% is a rough comfort level, not a rule)
5. Anchor profile: natural usually means plenty of branded anchors (roughly a fifth of referring domains for an established brand, as a rough heuristic); watch for crude language or heavy keyword-rich anchors

**Phase 2 — Deeper:**
1. Wasted links: top pages by links + 404 filter (fix/redirect); top pages by links with ~no traffic (e.g., 296 RDs → 16 visits/mo) → refresh + reoptimize
2. Best/worst referrers: referring domains, followed only; sort by the tool's authority score ascending = fishy sites (a rough screen — review manually); sort by followed-link count descending = sitewide/sidebar/footer (often paid) links; sort authority descending = your "superfans" → nurture relationships
3. Full anchor list: search for spam terms; bulk-anchor trick — export anchors → paste into a keyword research tool → sort by CPC descending → high-commercial anchors reveal over-optimized links built by past agencies (check the top ~100 rows first; some tools charge per row)
4. Referring IPs (advanced): many domains on the same c-class IP = possible PBN → remove/disavow (only for experienced SEOs)

**Phase 3 — Page-level backlink review:**
1. Pick a page (top by links, or top by link growth over the last 30 days) — not the whole domain (mixed anchors/targets muddy insights)
2. Filter to followed links; optionally sort by linking-page organic traffic (best referral links)
3. Find COMMONALITIES between top links (anchor text, platform/site type, surrounding text) → understand WHY people link → find more of those prospects (e.g., guide earns links from "best SEO posts" listicles + content-writing articles → systematically target both via a content research tool)
Bonus: run the same audit on competitors to steal strategy.

## Actionable checklist
- [ ] Site level: benchmark RDs vs 2-3 competitors
- [ ] Check RD growth curve for spikes/dips (possible negative SEO or paid campaigns)
- [ ] Check country-code TLD distribution for spam-TLD concentration
- [ ] Check anchor distribution for branded vs keyword-rich
- [ ] Fix 404s with backlinks; reoptimize high-RD/low-traffic pages
- [ ] Identify superfans (high-authority frequent linkers) and worst referrers
- [ ] Run the anchor → CPC export trick if agency-history suspected
- [ ] Analyze 2-3 top pages' backlinks for linkable commonalities → build prospect lists from patterns

## Data points & benchmarks
- Rough heuristic (not a Google rule): ~**20%+ of referring domains** use branded anchors on an established brand
- Rough heuristic: ~**2%** unusual-TLD share is unremarkable in a healthy profile
- Case: page with **296 RDs but 16 organic visits/mo** = wasted-link reoptimization target
- Reciprocal/absolute growth comparison example: +7,230 vs +1,811 RDs over 2 years

## Mistakes to avoid
- Auditing the whole domain at once at link level — no actionable signal
- Disavowing everything on shared c-class IPs without experience
- Assuming a low authority score = bad site (review firsthand) or every .cn link = spam (context)
- Ignoring the audit's opportunity side — superfans and linkable patterns are the growth insights
- Skipping competitor audits — same effort, extra strategy intel

## Key principles
- Audit before you build: don't renovate a house (or site) with hidden damp (penalty risk).
- Referring domains growth vs competitors is the headline health metric.
- The "why people link" commonalities found in Phase 3 feed your next campaigns.
