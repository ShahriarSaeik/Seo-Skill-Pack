# Where AI Search Traffic Actually Goes: Homepage, Product Pages, Free Tools (80%)

- **Updated**: 2026-10-05

## TL;DR
In one SEO company's site analytics (a single site, so treat it as an example): over 80% of AI-referral traffic landed on just three page types — free tools (36.5%), product pages (23.1%), and the homepage (20.4%) — while informational content earned a smaller share (though more than it earns from organic). Product and homepage over-performance signals brand recommendation, not content optimization; international pages drastically under-perform (3.1% of AI traffic vs 22.2% of organic); and 3.6% of AI traffic went to hallucinated URLs that don't exist.

## Framework / Step-by-step
The analysis (replicable on any site with an LLM channel segment):
1. **Segment AI referral traffic** in analytics (grouped assistant channel); note caveats — referrers are sometimes stripped and AI-answer traffic hides inside "organic search."
2. **Classify landing pages by type** — tools, product pages, homepage, informational, programmatic, international.
3. **Compare share-of-traffic by page type: AI vs organic** to find over/under-performers.
4. **Check landing URLs for hallucinations** — fetch status codes; 3.6% of that site's AI traffic hit pages that don't exist.

## Actionable checklist
- [ ] Build/maintain free tools and utility pages — they're the #1 AI traffic destination (job-to-be-done beats summaries)
- [ ] Keep product pages and homepage polished: AI recommends brands, and that traffic lands there
- [ ] Don't write off top-of-funnel content: informational pages earn a larger traffic share from AI than from organic
- [ ] Audit AI landing URLs for 404s/hallucinated paths; redirect any with meaningful visits (threshold ~10/month) to relevant pages
- [ ] Re-examine international ROI: AI assistants barely send non-English traffic — don't expect parity yet
- [ ] Keep overall expectations calibrated: AI traffic is still a fraction of a percent of total visits

## Data points & benchmarks
- AI referral split: free tools 36.45% | product pages 23.12% | homepage 20.41% (80% combined)
- Informational content over-performs its organic share; programmatic pages under-perform
- International pages: 22.2% of organic clicks vs 3.1% of AI clicks (~7x under-representation)
- 3.6% of AI traffic went to hallucinated URLs (mostly one chatbot)
- Context for that site: AI = 0.5% of total traffic (30-day window), 0.3% year to date

## Mistakes to avoid
- Rebuilding strategy around AI traffic distribution while it's <1% of total
- Ignoring hallucinated-URL traffic — those are users hitting 404s you can recover with redirects
- Assuming AI performance problems on international pages are your fault — non-English representation in AI systems may simply lag
- Treating product-page over-performance as an optimization cue — it's brand recommendation, earned off-site

## Key principles
- AI sends users to where action happens (tools, products), not where information lives.
- Brand strength routes AI traffic; content quality earns citations.
- Fight harder for smaller traffic — the cost/benefit of content is shifting.
