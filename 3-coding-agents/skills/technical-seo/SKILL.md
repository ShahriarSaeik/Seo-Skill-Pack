---
name: technical-seo
description: "Technical SEO playbooks, from basics to advanced: crawling and indexing, robots.txt, sitemaps, canonical tags, redirects, duplicate content, Search Console index-coverage errors, Core Web Vitals and page speed, mobile-first indexing, JavaScript and React SEO, hreflang and international sites, faceted navigation, crawl budget, log file analysis, site migrations, and technical audits. Use whenever pages aren't indexed or showing on Google, a site is slow, a migration or redesign is planned, or someone wants a technical SEO audit or a fix for a Search Console error."
metadata:
  version: "2.0"
  levels: beginner, intermediate, advanced
  agent-compatibility: any agent that reads markdown (Claude, ChatGPT, Gemini, Copilot, Cursor, Codex, and others)
---

# Technical SEO Playbooks

Vendor-neutral playbooks distilled from 57 in-depth SEO articles. Every playbook has the same shape: TL;DR → framework → checklist → data points → mistakes → principles.

## When to use
- Site audits, crawlability/indexation problems
- Sitemaps, redirects, canonicals, structured data, page speed
- International SEO, hreflang, duplicate content, faceted navigation, crawl budget

## Learning path: pick your level

| Level | Who it's for | Read in this order |
|---|---|---|
| **Beginner** | New to this topic, or you need the basics explained | [8 Fixes For When Your Website Isn't Showing Up In Google](articles/why-is-my-website-not-showing-up-on-google.md), [How Website Crawlers Work](articles/website-crawlers.md), [How to Get Google to Index Your Website](articles/google-index.md), [Robots.txt and SEO](articles/robots-txt.md), [HTTPS for SEO](articles/what-is-https.md), [What Are Core Web Vitals](articles/core-web-vitals.md), [301 Redirects Explained](articles/301-redirects.md) |
| **Intermediate** | You know the basics and need a repeatable process | [How to Complete a Technical SEO Audit in 8 Steps](articles/technical-seo-audit.md), [Canonical Tags Explained](articles/canonical-tags.md), [Duplicate Content](articles/duplicate-content.md), [What "Crawled - Currently Not Indexed" Means In Search Console](articles/crawled-currently-not-indexed.md), [How to Fix "Discovered - currently not indexed"](articles/discovered-currently-not-indexed.md), [Mobile-First Indexing Goes Mobile-Only](articles/mobile-first-indexing.md), [How to Find and Fix Orphan Pages](articles/orphan-pages.md), [Keyword Cannibalization](articles/keyword-cannibalization.md), [Hreflang](articles/hreflang-tags.md) |
| **Advanced** | You run SEO at scale or need edge cases, data and nuance | [Large-Site Migration Playbook](articles/large-site-migration-playbook.md), [How to Do an SEO Log File Analysis](articles/log-file-analysis.md), [When Should You Worry About Crawl Budget?](articles/crawl-budget.md), [JavaScript SEO](articles/javascript-seo.md), [Faceted Navigation](articles/faceted-navigation.md), [Website Migration](articles/website-migration.md), [URL Parameters](articles/url-parameters.md), [Headless SEO Explained + 6 Best Practices](articles/headless-cms-seo.md), [Enterprise Sites Are Where Technical SEO Shines](articles/enterprise-technical-seo.md), [10 International SEO Best Practices + Checklist](articles/international-seo.md) |

If you're not sure, start one level lower. The checklists still apply when you move up.

## How to use this skill (works with any AI agent)
0. **Reply in the user's language.** If they write in Bangla or Banglish (Bangla in English letters), answer in Bangla at the user's level (simple, everyday Bangla for beginners; clear professional Bangla for experts). Keep SEO terms in English, and explain each term in Bangla the first time you use it.
1. **Find the user's level.** Infer it from how they phrase the question. If it's unclear and the answer would change, ask one question. Beginners get plain language, 3–5 prioritized steps, and jargon defined from [GLOSSARY.md](GLOSSARY.md). Advanced users get the full framework, benchmarks and edge cases.
2. **Route the task.** Pick the matching row in *Quick playbooks* below. If nothing matches, search the article list or [ARTICLES.md](ARTICLES.md). For a single task, read only the 1–3 articles you need; don't load the whole folder. The learning path is for studying the topic over time, so start at its first link.
3. **Apply the playbook to the user's situation.** Each article has a TL;DR, framework, checklist, data points, mistakes and principles. Turn these into concrete actions for the user's site, niche and resources. Don't recite the article.
4. **Map tools to what the user has.** Playbooks say "a keyword research tool", "a site audit crawler" and so on. Use whatever the user has. If they have no paid tools, use the free options in the *Tool categories* table in [GLOSSARY.md](GLOSSARY.md).
5. **Treat the numbers as dated.** Benchmarks come from studies current when the library was compiled (2026). Quote them as "one study found…". If you can browse, check anything time-sensitive. Never invent statistics.
6. **Stay white-hat.** Don't promise rankings or timelines. Flag risky tactics (link buying, scaled AI spam, cloaking) and explain the risk.
7. **End with a deliverable:** a prioritized action plan or checklist (with impact and effort), a draft, or a specific diagnosis with next steps.

## Quick playbooks (start here)
| Task | Read |
|------|------|
| Run a large-site migration with log validation | [articles/large-site-migration-playbook.md](articles/large-site-migration-playbook.md) |
| Run a full technical SEO audit (8 steps) | [articles/technical-seo-audit.md](articles/technical-seo-audit.md) |
| Fix the issues that actually matter (top 10) | [articles/seo-issues.md](articles/seo-issues.md) |
| Set up or debug redirects | [articles/redirects-for-seo.md](articles/redirects-for-seo.md) |
| Write/audit robots.txt | [articles/robots-txt.md](articles/robots-txt.md) |
| Fix duplicate content / canonicals | [articles/canonical-tags.md](articles/canonical-tags.md), [articles/duplicate-content.md](articles/duplicate-content.md) |
| Go international (hreflang, URL structure) | [articles/international-seo.md](articles/international-seo.md), [articles/hreflang-tags.md](articles/hreflang-tags.md) |
| Manage crawl budget | [articles/crawl-budget.md](articles/crawl-budget.md) |
| Analyze server logs | [articles/log-file-analysis.md](articles/log-file-analysis.md) |
| Get pages indexed | [articles/google-index.md](articles/google-index.md) |
| Fix Search Console "Discovered/Crawled - not indexed" | [articles/discovered-currently-not-indexed.md](articles/discovered-currently-not-indexed.md), [articles/crawled-currently-not-indexed.md](articles/crawled-currently-not-indexed.md) |
| Improve Core Web Vitals | [articles/core-web-vitals.md](articles/core-web-vitals.md) |
| Fix faceted navigation / filters | [articles/faceted-navigation.md](articles/faceted-navigation.md) |
| Plan/survive a website migration | [articles/website-migration.md](articles/website-migration.md) |
| Fix JavaScript rendering issues | [articles/javascript-seo.md](articles/javascript-seo.md) |
| Find and fix orphan pages | [articles/orphan-pages.md](articles/orphan-pages.md) |
| Optimize meta tags | [articles/seo-meta-tags.md](articles/seo-meta-tags.md) |
| Get pagination right | [articles/rel-prev-next-pagination.md](articles/rel-prev-next-pagination.md) |
| Migrate to / debug HTTPS | [articles/what-is-https.md](articles/what-is-https.md) |
| Build SEO-friendly URLs | [articles/seo-friendly-urls.md](articles/seo-friendly-urls.md) |
| Understand crawlers & Googlebot | [articles/website-crawlers.md](articles/website-crawlers.md), [articles/googlebot.md](articles/googlebot.md) |
| Control indexing (robots meta / X-Robots-Tag) | [articles/meta-robots.md](articles/meta-robots.md) |
| Use nofollow correctly | [articles/nofollow-links.md](articles/nofollow-links.md) |
| Fix keyword cannibalization | [articles/keyword-cannibalization.md](articles/keyword-cannibalization.md) |
| Resolve trailing-slash variants | [articles/trailing-slash.md](articles/trailing-slash.md) |
| Optimize images | [articles/image-seo.md](articles/image-seo.md) |
| Remove URLs from Google | [articles/remove-urls-from-google.md](articles/remove-urls-from-google.md) |
| Get into the Knowledge Graph / AI answers | [articles/google-knowledge-graph.md](articles/google-knowledge-graph.md) |
| Do semantic / entity SEO | [articles/semantic-seo.md](articles/semantic-seo.md) |
| Run technical SEO at enterprise scale | [articles/enterprise-technical-seo.md](articles/enterprise-technical-seo.md) |
| Fix "Duplicate, Google chose different canonical" | [articles/duplicate-google-chose-different-canonical-than-user.md](articles/duplicate-google-chose-different-canonical-than-user.md) |
| SEO for a headless CMS | [articles/headless-cms-seo.md](articles/headless-cms-seo.md) |
| Read page speed reports (field vs lab) | [articles/pagespeed-insights.md](articles/pagespeed-insights.md) |
| Improve LCP / CLS / FID-INP individually | [articles/largest-contentful-paint-lcp.md](articles/largest-contentful-paint-lcp.md), [articles/cumulative-layout-shift-cls.md](articles/cumulative-layout-shift-cls.md), [articles/first-input-delay-fid.md](articles/first-input-delay-fid.md) |
| Make the site accessible (WCAG/ADA) | [articles/accessibility-seo.md](articles/accessibility-seo.md) |
| Mobile SEO & mobile-first indexing | [articles/mobile-seo.md](articles/mobile-seo.md), [articles/mobile-first-indexing.md](articles/mobile-first-indexing.md) |
| Manage URL parameters | [articles/url-parameters.md](articles/url-parameters.md) |
| Understand all canonicalization signals | [articles/canonicalization.md](articles/canonicalization.md) |
| Handle out-of-stock products | [articles/ecommerce-out-of-stock-products.md](articles/ecommerce-out-of-stock-products.md) |
| SEO for React / component SPAs | [articles/react-seo.md](articles/react-seo.md) |
| Detect & deflect negative SEO | [articles/negative-seo.md](articles/negative-seo.md) |
| Choose subdomain vs subdirectory | [articles/subdomain-vs-subfolder.md](articles/subdomain-vs-subfolder.md) |
| Fix "Indexed, though blocked by robots.txt" | [articles/indexed-though-blocked-by-robots-txt.md](articles/indexed-though-blocked-by-robots-txt.md) |
| Speed up a CMS site fast | [articles/speed-up-wordpress.md](articles/speed-up-wordpress.md) |
| Choose 301 vs 302 | [articles/301-vs-302-redirects.md](articles/301-vs-302-redirects.md) |
| Influence sitelinks | [articles/sitelinks.md](articles/sitelinks.md) |
| Diagnose "site not showing up in Google" | [articles/why-is-my-website-not-showing-up-on-google.md](articles/why-is-my-website-not-showing-up-on-google.md) |
| Run a basic SEO+UX website audit | [articles/website-audit.md](articles/website-audit.md), [articles/seo-for-static-sites.md](articles/seo-for-static-sites.md) |
| Use 301s to consolidate & boost traffic | [articles/301-redirects.md](articles/301-redirects.md) |

## All playbooks
- [Technical SEO Audit in 8 Steps](articles/technical-seo-audit.md) — crawl → indexation → on-page → images → links → speed → mobile
- [10 SEO Issues That Really Matter](articles/seo-issues.md) — indexability, broken pages, internal links, HTTPS, CWV, structure, schema, duplicates, 2 MB limit
- [11 Types of Redirects](articles/redirects-for-seo.md) — 301/308 consolidate forward; 302/307 usually don't; keep ≥1 year; chains <5 hops
- [Robots.txt Guide](articles/robots-txt.md) — crawling control only; noindex lives in meta/x-robots-tag; longest directive wins
- [Canonical Tags Explained](articles/canonical-tags.md) — absolute URLs, one canonical per page, 14 audited issues
- [Duplicate Content](articles/duplicate-content.md) — no penalty for accidents; 12 technical causes; redirect/canonicalize
- [Hreflang Guide](articles/hreflang-tags.md) — bidirectional clusters, self-references, x-default; 67% of implementations have errors
- [International SEO Best Practices](articles/international-seo.md) — subfolders preferred, CDN, per-market keywords, no IP redirects, local links
- [Crawl Budget](articles/crawl-budget.md) — demand (links) × rate limit (server health); most sites shouldn't worry
- [SEO Log File Analysis](articles/log-file-analysis.md) — verify Googlebot, find crawl waste, orphans, cache ratios
- [Get Google to Index Your Website](articles/google-index.md) — request indexing, sitemap, structure, backlinks + troubleshooting
- [Discovered - Currently Not Indexed](articles/discovered-currently-not-indexed.md) — uncrawled = prioritization: quality, internal links, crawl budget
- [Crawled - Currently Not Indexed](articles/crawled-currently-not-indexed.md) — crawled but rejected = usually a content-quality judgment
- [Core Web Vitals](articles/core-web-vitals.md) — LCP ≤2.5s, INP ≤200ms, CLS ≤0.1; tiny ranking factor, big UX factor
- [Faceted Navigation](articles/faceted-navigation.md) — canonical → robots.txt → nofollow → noindex ladder; AJAX prevention; long-tail play
- [Website Migration](articles/website-migration.md) — baseline crawl, same vs changed URLs, 301s + signal consolidation, monitor old domains
- [JavaScript SEO](articles/javascript-seo.md) — render pipeline, most-restrictive directive wins, real `<a href>` links, no 5-second render timeout
- [Website Crawlers](articles/website-crawlers.md) — 7 crawl stages; earn crawling via quality, freshness, structure
- [Orphan Pages](articles/orphan-pages.md) — cross-reference crawl vs URLs-with-hits; link/noindex/merge/delete decision tree
- [Meta Tags for SEO](articles/seo-meta-tags.md) — 6 tags that matter; titles <60, descriptions <160; delete meta keywords
- [Pagination](articles/rel-prev-next-pagination.md) — self-canonical per page; never canonical-to-page-1, noindex, nofollow, or block the series
- [HTTPS](articles/what-is-https.md) — TLS tiers, 5 classic migration mistakes, HSTS, HTTP/2+3 require HTTPS
- [SEO-Friendly URLs](articles/seo-friendly-urls.md) — keyword slug, lowercase, hyphens, subfolders, no dates/parameters
- [Googlebot](articles/googlebot.md) — mobile-rendered index, 15 MB file cap, verify by IP, ~24% of good-bot requests
- [Robots Meta & X-Robots-Tag](articles/meta-robots.md) — index/snippet control; never pair noindex with a robots.txt block
- [Nofollow vs Follow](articles/nofollow-links.md) — paid/UGC always nofollowed; 60-90% followed is natural; sculpting is dead
- [Keyword Cannibalization](articles/keyword-cannibalization.md) — real only when same intent; fix = merge + 301, never noindex/canonical/de-optimize
- [Trailing Slash](articles/trailing-slash.md) — distinct URLs past the root; pick one variant and align every signal
- [Image SEO](articles/image-seo.md) — names, alt, format, dimensions, compression, srcset, CDN, image sitemap
- [Remove URLs From Google](articles/remove-urls-from-google.md) — delete/noindex/auth/removals-tool/canonicalize; site: ≠ indexed
- [SEO for Static Sites](articles/seo-for-static-sites.md) — no CMS safety net: slash/canonical conflicts, sitemap-noindex leaks, image gaps, template errors, soft 404s, link inconsistency, perf, migration traps
- [Knowledge Graph](articles/google-knowledge-graph.md) — 54B entities/1.6T facts; powers panels + AI answers; build entity signals (Organization schema, sameAs, Wikidata, consistency everywhere)
- [Semantic SEO](articles/semantic-seo.md) — brand × content × technical; 10 expert practices; optimize HOW you appear (accuracy, sentiment, AI mentions), not just if
- [Enterprise Technical SEO](articles/enterprise-technical-seo.md) — maturity model; crawl monitoring ladder (scheduled → staging → sampling → always-on); impact/effort + cash-value tickets
- [Duplicate, Different Canonical](articles/duplicate-google-chose-different-canonical-than-user.md) — causes: duplicates, canonical chains/loops, JS app shells; usually harmless; fix by cause
- [Headless CMS SEO](articles/headless-cms-seo.md) — content models replace pages; keyword-driven attributes; programmatic schema; reference-based internal links
- [Page Speed Reports](articles/pagespeed-insights.md) — field (75th pct, 28-day) vs lab; only 2% score 100, 50 = top quartile; fix templates, verify in lab
- [FID/INP](articles/first-input-delay-fid.md) — main-thread blocking; 95.3% of sites already pass; reduce/defer/split JS, SSR
- [LCP](articles/largest-contentful-paint-lcp.md) — hardest vital (57.1% pass); fetchpriority/preload the LCP element; critical CSS; CDN + caching
- [CLS](articles/cumulative-layout-shift-cls.md) — dimensions/aspect-ratio everywhere; font-display: optional; transform animations; bfcache
- [Accessibility (ADA/WCAG)](articles/accessibility-seo.md) — target Level AA; 2,200+ US lawsuits in 2018; nav/sitemap/headings/alt/anchor overlap with SEO
- [Mobile SEO](articles/mobile-seo.md) — responsive design; full mobile/desktop parity; CWV mobile-first; hamburger nav with identical links; device-split tracking
- [URL Parameters](articles/url-parameters.md) — active vs passive; canonicalize by default; noindex selectively; robots.txt only for crawl budget
- [Canonicalization Signals](articles/canonicalization.md) — ~40 weighted signals; HTTPS>HTTP, shorter wins, redirects consolidate after ~1 year; signal consistency wins
- [Out-of-Stock Products](articles/ecommerce-out-of-stock-products.md) — returning = keep live; permanent = 301 similar/404; unknown = deprioritize on a timer
- [React SEO](articles/react-seo.md) — SSR/SSG over CSR; real status codes; History API URLs; real `<a href>` links; no on-interaction HTML injection
- [Negative SEO](articles/negative-seo.md) — 7 attack types; devaluation makes link spam mostly harmless; monitor links/index counts/security/brand SERPs
- [Subdomain vs Subdirectory](articles/subdomain-vs-subfolder.md) — a myth; integration (internal links), not path position, decides signal flow
- [Indexed, Though Blocked](articles/indexed-though-blocked-by-robots-txt.md) — crawling ≠ indexing; noindex + allow crawl, or strip robots.txt/UA/IP blocks
- [Mobile-First Indexing](articles/mobile-first-indexing.md) — rollout complete; Jul 2024 cliff (mobile-invisible = unindexable); crawl-and-diff audit
- [Speed Up a CMS](articles/speed-up-wordpress.md) — 11 settings wins ≈ 20 min: 1.89MB→695KB page, ~40% faster sitewide loads
- [301 vs 302](articles/301-vs-302-redirects.md) — permanent = signals forward, temporary = backward; engines reinterpret mismatched codes; relevance gates transfer
- [Sitelinks](articles/sitelinks.md) — algorithmic; influence via structure, internal links, headings; 12.9% of brand-query clicks
- [Not Showing Up In Google](articles/why-is-my-website-not-showing-up-on-google.md) — 8-step ladder: index → sitemap → noindex → robots → orphans → backlinks → intent → penalty
- [Basic Website Audit](articles/website-audit.md) — 10 UX+SEO checks; ≤7th-grade reading level; 53% abandon >3s mobile loads; design refresh every 4-5 years
- [301 Redirects Deep Dive](articles/301-redirects.md) — no PageRank loss since 2016; fix 9 redirect issues; cocktail merges + merger method = traffic plays

## Full category index
See [ARTICLES.md](ARTICLES.md) for the complete index of all 57 playbooks.

## Key takeaways

## Key benchmarks to remember
- LCP ≤2.5s / INP ≤200ms / CLS ≤0.1 (good thresholds; 75th percentile field data)
- Title tags ≤60 chars; site depth ≤6 clicks; HTML <2 MB (Googlebot limit)
- Redirect chains <5 hops; keep redirects ≥1 year; ~10-15 Search Console indexing requests/day
- Page must be crawlable + not noindexed + canonical to rank
- robots.txt blocks crawling, never guarantees deindexing
- 90% of sites don't need to worry about crawl budget (Google)
- Noindex must stay crawlable (never pair with robots.txt block); site: ≠ indexed
- HTTP/2 & HTTP/3 require HTTPS; images are usually the largest page-weight contributor
