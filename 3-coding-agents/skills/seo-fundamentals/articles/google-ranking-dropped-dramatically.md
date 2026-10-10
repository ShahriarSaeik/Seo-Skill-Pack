# Google Ranking Dropped Dramatically? (Here's What to Check)

- **Updated**: 2026-10-05

## TL;DR
Before changing anything after a rankings drop, run a 9-point diagnosis in order: algorithm updates, your traffic timeline, keyword-level losses, technical changes, competitors, links, content quality, SERP shifts, and manual actions. Match exact dates — only then act.

## Framework / Step-by-step
1. **Check for Google algorithm updates** — Google's search status page; faster: some SEO tools overlay algorithm-update markers on your traffic timeline.
2. **Check your organic traffic timeline** — weekly granularity over at least a year for perspective. Does the drop EXACTLY align with an update? (Example: March 2023 core update roughly aligned but not exactly → keep investigating.)
3. **Check top traffic-driving keywords** — Compare keyword performance year-over-year; sort by change. Drill into historical SERP data with custom dates. Case study: "yamaha motorcycles" dropped because Google swapped the /motorcycle page for the homepage — that page 404'd on March 14 and vanished from SERPs by March 16.
4. **Check recent technical changes** — Crawl your site with an SEO audit tool for a health score and per-issue fixes. Crawl before/after migrations to diff issues. Specific culprits:
   - **4XX pages** — dead pages lose traffic directly (the Yamaha site's top pages were all 404s on the drop date).
   - **Canonicals** — missing/misimplemented canonical tags; spot-check pages or run a full crawl.
   - **Redirects** — use 301s; avoid chains and loops.
   - **Robots.txt** — accidental crawl blocks (diff old vs. new robots.txt; check the robots.txt report in Search Console → Settings and test key URLs with URL Inspection; common during migrations).
5. **Check competitors' rankings** — Compare their keyword gains against your losses over the same dates. Sometimes they're just better at SEO.
6. **Check your links** — Review broken backlinks (one example site had 3,442 groups of follow links to fix; lost 3 high-authority links from prominent sites). Then audit for bad links (paid, PBN, low-quality directories, comment/forum spam, hacked sites) → disavow cautiously ("a very heavy gun... you can shoot yourself in the foot" — Google).
7. **Check your content** — If hit during a content-focused update, run a content audit. Use Google's self-assessment questions: original info/research/analysis? substantial and comprehensive? insightful beyond the obvious? not just rewriting sources? descriptive non-clickbait headings? bookmark/share-worthy? magazine/encyclopedia-worthy? substantial value vs. other SERP pages?
8. **Check the SERPs** — Intent shifts happen. Historical example: "corona" — beer sites displaced by COVID news + Top stories within months (Jan → Mar 2020), later reverted. Use historical SERP comparisons to spot reshuffles you can't control.
9. **Check for a manual action** — Total traffic loss → check the manual actions report in your Search Console. "No issues detected" = fine; else address the stated action type (pure spam, unnatural links, thin content, cloaking, etc.).

## Actionable checklist
- [ ] Overlay algorithm-update dates on your traffic chart; demand exact date alignment
- [ ] Run YoY keyword compare; trace the worst losers through historical SERP data
- [ ] Crawl the site; fix 4XXs, canonicals, redirect chains, robots.txt blocks
- [ ] Diff pre/post-migration crawls if you migrated
- [ ] Compare competitor rankings side-by-side over the same window
- [ ] Fix broken backlinks; audit for paid/PBN/spam links before disavowing
- [ ] Audit content against Google's self-assessment questions
- [ ] Compare historical SERPs for intent shifts
- [ ] Verify no manual action in your Search Console

## Data points & benchmarks
- Diagnosis case: page 404'd March 14 → gone from SERPs March 16 → site's biggest keyword collapsed (drops follow technical failures within days).
- Example broken-backlink backlog: 3,442 groups of dofollow broken links on one site.
- "Corona" SERP flip: beer → COVID results in ~3 months; intent later reverted.
- Google's helpful-content self-assessment questions focus on originality, comprehensiveness, insight, and comparative value.

## Mistakes to avoid
- Making changes before diagnosing — date-mismatched "update hits" usually have another cause.
- Assuming an update hit you when a competitor simply outranked you, or the SERP intent shifted.
- Ignoring broken backlinks and lost high-authority links.
- Careless disavowing — treat it as a heavy gun.
- Skipping the manual-actions check when traffic goes to zero.

## Key principles
- "Investigating, analyzing, and finding data you can rely on" beats panic changes.
- Exact date alignment is the core diagnostic technique (update vs. technical failure vs. competitor gain).
- SERPs are dynamic — intent shifts and reversions can mask or mimic penalties.
