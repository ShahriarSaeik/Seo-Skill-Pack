# How to Do a Basic Website Audit to Improve SEO and UX (in 10 Steps)

- **Updated**: 2026-10-05

## TL;DR
A beginner-friendly audit covering technical, UX, and content basics in 10 checks: design, navigation, mobile-friendliness, robots.txt/sitemap, HTTPS, speed, content quality, broken pages/links, meta titles/descriptions, and keyword targeting. Crawl the site first, then prioritize fixes by traffic/conversion value — most fixes are self-explanatory or a one-ticket handoff to a developer.

## Framework / Step-by-step
1. **Check design** — no intrusive pop-ups (pogo-sticking + mobile interstitial penalties), legible text (font size, sans-serif, white space, contrast), clear CTAs ("Start trial" not "Join the adventure"). Redesign roughly every 4-5 years (rule of thumb).
2. **Check navigation** — menu exists, links all important pages, uncluttered, contact easy. Sketch the site flow; test with fresh eyes (users, family, or a cheap freelance video audit — people soften criticism).
3. **Check mobile-friendliness** — ~49%+ browse on mobile, ~60% of searches are mobile (older data). Test key pages with Lighthouse or Chrome DevTools device mode (Google's Mobile-Friendly Test was retired in Dec 2023); hire a developer if they fail.
4. **Check robots.txt & sitemap** — both optional for tiny sites but cheap insurance; find robots.txt at /robots.txt and the sitemap URL inside it (or root folder). Generate both via CMS plugin if missing.
5. **Check HTTPS** — lock icon required: ranking factor since 2014, mandatory for payments/data. Free certificates exist (industry-backed nonprofit CAs). Also fix internal HTTP links, mixed content, and HTTP canonicals.
6. **Check speed** — 53% of mobile visitors abandoned sites over 3s in one older study; a 100ms slowdown reportedly cost one retailer ~1% of sales. Test the homepage in a speed tool, then crawl for slow pages and prioritize by organic traffic.
7. **Check content quality** — well-written, error-free, skimmable (one H1, cascading H2/H3/H4), not duplicated, readable at ~7th-grade level (average reading level; comprehension degrades above it). Small sites: review manually; large sites: review top-traffic and thin (low-word-count) pages first; fix duplicate-without-canonical issues.
8. **Check broken pages & links** — internal 4XXs (fix or redirect, especially those with backlinks) and external 4XXs (dead third-party links make the site look abandoned).
9. **Check titles & descriptions** — audit for missing, duplicate, overlong, or multiple tags. Keywords where natural, but the job is enticing the click; find low-CTR/high-impression pages in the performance report as rewrite candidates.
10. **Check keyword targeting** — right keyword = traffic potential + low difficulty + intent match. Check what page TYPE ranks for the query (product/category vs blog/guide) — never try to rank a page where it doesn't belong (e.g., a "best X" listicle for a buying-mode query like "X").

## Actionable checklist
- [ ] Crawl the site with a site auditor (schedule recurring crawls); enable external link status checks
- [ ] Load the site incognito; remove aggressive pop-ups; verify CTAs make sense out of context
- [ ] Run Lighthouse/DevTools mobile checks on homepage + distinct sections
- [ ] Confirm robots.txt + sitemap exist and are submitted
- [ ] Verify HTTPS everywhere: internal links, mixed content, canonicals
- [ ] Speed-test the homepage; crawl for slow pages; fix by traffic priority
- [ ] Review top pages for spelling, structure (H1-H4), reading level, thin content
- [ ] Fix internal 4XXs (redirect those with backlinks) and dead external links
- [ ] Rewrite missing/duplicate/overlong titles & descriptions; attack low-CTR high-impression pages
- [ ] Match each important page's keyword to the intent of the live SERP

## Data points & benchmarks
- 53% of mobile visits abandoned pages slower than 3s; 100ms of latency ≈ 1% sales loss for one major retailer (both older figures).
- ~49% of browsing and ~60% of searches happen on mobile (older data — likely higher now).
- Target reading level: ≤7th grade (US average; comprehension drops beyond it).
- Design refresh cadence: roughly every 4-5 years (rule of thumb, not a standard).
- HTTPS: confirmed lightweight ranking factor since 2014.

## Mistakes to avoid
- Judging your own site — you're the worst test user; get outside eyes.
- Fixing issues in arbitrary order — prioritize by organic traffic and conversion value.
- Keyword-stuffing titles; their primary job is winning the click.
- Targeting high-volume head terms whose SERP intent doesn't match your page type.
- Skipping the audit because "it's fine" — sites rot silently; schedule recurring crawls.

## Key principles
- Audit = technical + UX + content, not just SEO; UX failures (pop-ups, walls of text, broken links) become SEO failures via user behavior.
- Crawl first: automation finds what eyes skip.
- Don't rank pages where they don't belong — SERP composition defines the content type.
