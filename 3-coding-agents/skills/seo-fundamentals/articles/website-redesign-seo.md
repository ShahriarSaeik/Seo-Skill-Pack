# How to Avoid Ruining SEO During a Website Redesign

- **Updated**: 2026-10-05

## TL;DR
Redesigns routinely destroy rankings, traffic, and link equity — one cited case deleted ~15% of organic pages during a redesign and lost almost 50% of organic traffic, and subsequent link growth never restored it. Six rules prevent nearly all redesign disasters: back up, pre-test, audit around launch, keep URLs, keep ranking pages, and minimize changes to what already works.

## Framework / Step-by-step
1. **Keep a backup of the old site** — instant rollback path (repoint the domain to the old folder); make sure nothing overwrites current databases.
2. **Test staging for mobile friendliness and Core Web Vitals** — run Lighthouse lab tests on template pages (not every page) as soon as templates are ready, on both desktop and mobile; catch unoptimized code, heavy animation, broken scaling before launch (field data only exists after launch). Keep staging out of the index with password protection rather than noindex, so a noindex tag can't carry over at launch.
3. **Run a full site audit pre- and post-launch** — diff the two crawls: new errors (noindex pages that shouldn't be, http/https duplicates, broken pages) surface in the change column. Fix new issues immediately.
4. **Keep the old URL structure** — changes (adding trailing slashes, new subfolders, subdomain moves, renamed slugs) cause broken redirects, broken backlinks, broken internal links, and orphans. If you must change, map 301s and submit an updated sitemap in Search Console (use the Change of Address tool for domain moves).
5. **Keep important organic pages** — pull your top pages by traffic and your most-linked pages from a backlink tool; those carry both rankings and backlinks. For retired products, use archive pages linked to current alternatives instead of deleting (keeps rankings and UX). Check any candidate page's traffic and links before cutting it.
6. **Minimize modifications to top-ranking pages** — protect: keywords in titles/H1/body (relevance shifts), content depth (change only to serve intent better), internal links (equity flow and context), click-distance from homepage (importance signal), schema accuracy, and page speed.

## Actionable checklist
- [ ] Full site backup + documented rollback plan before launch day
- [ ] CWV + mobile tests pass on all key templates (staging)
- [ ] Pre-launch crawl completed and archived
- [ ] URL mapping table: every changed URL has a 301 to an equivalent page
- [ ] No new noindex tags, no http/https duplication (post-launch crawl diff)
- [ ] Top-traffic and most-linked pages preserved or redirected
- [ ] New sitemap submitted at launch; Search Console monitored for indexing drops
- [ ] Homepage-to-key-page click depth unchanged or shorter

## Data points & benchmarks
- Case: ~15% of organic pages deleted in a redesign → nearly 50% organic traffic loss; growing referring domains afterward did not recover it.
- Uncontrolled URL structure changes cascade into four failure classes: broken redirects, broken backlinks, broken internal links, orphan pages.

## Mistakes to avoid
- Launching without a rollback option.
- Redesigns bundled with uncontrolled content pruning ("arbitrary deleting of older content").
- Rewriting top-ranking pages' titles/H1s/keyword framing for "brand voice."
- Changing too much at once — when rankings move you can't attribute cause or fix it.
- Assuming new links will compensate for deleted pages; they don't.

## Key principles
- A redesign changes packaging, not information architecture — unless there's a deliberate, mapped reason.
- Existing rankings and backlinks are balance-sheet assets; treat deletions like writing off capital.
- Test before launch, diff after launch: the two-crawl comparison catches what monitoring dashboards miss.
- SEO is experimentation: change less per launch so you can attribute outcomes.
