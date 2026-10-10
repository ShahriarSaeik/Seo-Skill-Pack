# How to Run a Content Audit: A Decision-Tree Process

- **Updated**: 2026-10-05

## TL;DR
A content audit asks systematic yes/no questions about each page (traffic, purpose, links, indexability, age, priority, cannibalization, quality, on-page, internal links, link strength, redirects, conversions) and prescribes an action per answer. Audit the top 20% of pages by traffic or backlinks first — that yields ~80% of the results.

## Framework / Step-by-step
Setup: export all indexable URLs with their traffic and backlink counts; prioritize by the 80/20 rule; merge in Search Console data for real clicks. Then run each page through this decision tree:

1. **Does the page get organic traffic?** (check Search Console / traffic estimator)
2. **Does it get traffic from other sources?** (analytics — social, email, referral)
3. **Is it mainly for organic search?**
4. **Is it useful for another purpose?** — ToS, privacy policy, landing pages for ads, conversion/navigation aids stay regardless of traffic.
5. **Does it have backlinks?** — pages with links deserve more caution and effort before any deletion/redirect decision.
6. **Is it crawlable and indexable?** — URL inspection: crawl allowed, indexing allowed, canonical correct, not redirected.
7. **Has it had time?** — under ~6 months since publish/major update may just need patience.
8. **Is ranking it a priority?** — score by business potential (how naturally you can pitch your product) × traffic potential.
9. **Could it get more traffic?** — compare the topic's traffic potential (top-ranking page's traffic) vs. your page's actual traffic; use a comparable page on the SERP, not an unbeatable official site, for the benchmark.
10. **Is another page ranking for the same terms?** — check for keyword cannibalization (multiple URLs ranking for one keyword).
11. **Is the page unique enough to keep separate?** — similar-title definition pages should merge; genuinely different pages targeting different subtopics can coexist.
12. **Is it better than the competition?** — does it cover the topic fully (content gap reveals missing subtopics) and offer something unique (data, viewpoints)?
13. **Is on-page SEO solid?** — titles, meta descriptions, URLs, images, schema.
14. **Is it internally linked where relevant?** — find keyword mentions across the site lacking links to this page.
15. **Is its link profile stronger than competitors'?** — compare referring domains and page-level authority metrics.
16. **Are there deleted pages that could be redirected to it?** — 404s with backlinks on similar topics are free authority; 301 them to the closest relevant page (redirecting to unrelated pages is treated as a soft 404).
17. **Could it convert better?** — add CTAs, sell the product more naturally in the content.

Log the recommended actions per page, then execute or delegate (each action mapped to an SOP).

## Actionable checklist
- [ ] Export URLs + traffic + backlinks; audit top 20% first
- [ ] Classify each page: keep-as-is / update / merge / redirect / improve conversions
- [ ] Fix noindex/canonical/crawl issues on deserving pages
- [ ] Give pages <6 months old more time before judging
- [ ] Resolve cannibalization by merging near-duplicates into the strongest URL
- [ ] Add missing subtopics found via content gap
- [ ] Add internal links from existing keyword mentions
- [ ] 301 deleted same-topic pages with backlinks
- [ ] Add/improve CTAs on traffic-rich, conversion-poor pages

## Data points & benchmarks
- 6 months is the minimum fair evaluation window for a new/updated page.
- Traffic potential (TP) is estimated from the current top-ranking page's traffic — but benchmark against a realistic competitor page, not an unbeatable official domain.
- Business potential scale: 3 = can pitch product heavily, 2 = can pitch naturally, 1 = awkward pitch, 0 = no fit.

## Mistakes to avoid
- Running overly basic audits that pull too little data — leads to harmful recommendations (e.g., deleting pages worth keeping).
- Auditing every page equally — 80/20 the workload.
- Deleting or redirecting content without confidence it's the right call; balance is the goal.
- Sweating word counts and meta descriptions while missing whole subtopics.

## Key principles
- Not every page needs traffic to justify existing.
- Never delete/redirect pages with backlinks without a plan — reclaim that authority.
- A successful audit focuses on the right things, not all things.
