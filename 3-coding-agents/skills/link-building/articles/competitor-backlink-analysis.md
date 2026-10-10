# How to Perform a Competitor Link Analysis in 3 Steps

- **Updated**: 2026-10-05

## TL;DR
A competitor link analysis reveals which sites commonly link to sites like yours — those shared links are likely what helps competitors rank. Basic version: identify competitors → link-intersect report → spot patterns. Scaled version (~2-4 hours): merge referring-domain exports across dozens of competitors (niche or local) and count overlaps to surface opportunity categories nobody in your market uses.

## Framework / Step-by-step
**Basic (3 steps):**
1. **Identify competitors** — use the organic-competitors view in a backlink or SEO tool (or a keyword tool's domain-share view if you don't have a site yet); you can also just list who ranks in the SERPs you want
2. **Find common links** — run a link-intersect (common backlinks) comparison: enter your site + competitors → referring domains linking to multiple competitors but not you; open the actual links to see context
3. **Identify strategies** — work through missing common links, and/or categorize patterns (niche sites, local listings, etc.)
Bonus: check competitors' **top pages by links** for tools/studies/quotes driving links that a link-intersect view misses.

**Scaled niche process:**
1. List competitor domains (own list or a competing-domains view)
2. Export referring domains for each (a backlink analysis tool, or its API at larger scale)
3. Merge CSVs (Windows: `copy *.csv combined.csv`; Mac: `cat *.csv > combined.csv`)
4. Excel: Insert Table → Count column `=COUNTIF(B:B,[@[Referring Domain]])` → paste as values → Remove Duplicates → sort by Count desc
5. Categorize top referring sites (organizations, trade shows, suppliers, niche directories) → study how they link (what the linking pages say and where the link sits)

**Scaled LOCAL process (differentiators):**
- Build keyword list "[service] + [top 50 cities]" → a keyword research tool → export WITH SERPs → keep organic niche sites (filter out high-authority domains, roughly 50+ on the tool's scale, to drop directories/aggregators) → export each site's referring domains → same merge/count flow
- Or reverse: "[city] + [popular local niches]" → analyze same-city site overlaps
- Categorize local patterns (Raleigh example): colleges (jobs/scholarships/discounts/alumni), city directories, local news, suppliers/partners (testimonials), churches, business groups, events/meetups, sponsorships/charities, podcasts, local awards, coupons, job postings; wedding vendors interlink; realtors link to "things to do". Caution: links obtained in exchange for a scholarship, discount, sponsorship, or free product are paid placements — tag them rel="sponsored"/nofollow.

## Actionable checklist
- [ ] Identify 3-10 organic competitors
- [ ] Run a link-intersect comparison; export missing-link domains
- [ ] Check top pages by links per competitor for asset-driven links
- [ ] (Scaled) merge referring-domain CSVs, COUNTIF, dedupe, sort
- [ ] Tag categories; note HOW each category links
- [ ] For local: run the city x service and city x niche matrices
- [ ] Turn each category into an outreach play; reuse across clients

## Data points & benchmarks
- Scaled process time estimate: **2-4 hours**
- Local cleanup filter: excluding high-authority domains (roughly 50+) removes most directories/aggregators
- Common local link categories observed: 14 patterns (colleges → job postings)

## Mistakes to avoid
- Only looking at link OVERLAP — unique per-competitor assets (tools, studies) get missed
- Analyzing only direct competitors in weak local markets — stronger markets elsewhere reveal untapped opportunity categories
- Keeping directory/aggregator "best-of" sites in local analysis — filter them out
- Forgetting that findings are reusable — agencies should systematize across same-area clients

## Key principles
- Links many competitors share are likely the links helping them rank — prioritize those.
- Local sites link to local sites: mine same-city overlaps, not just same-niche.
- The categorization step turns raw data into strategy — patterns become campaigns.
