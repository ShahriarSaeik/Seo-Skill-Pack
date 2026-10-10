# Large-Site Migration Playbook (10k–1M URLs, with Log Validation)

- **Updated**: 2026-10-05

## TL;DR
Big migrations fail from missing URLs, not bad redirects. Build a complete URL inventory from crawls, logs, sitemaps, backlinks, analytics and Search Console. Map it by template with rules, then by hand for high-value URLs. Test on staging, launch in a low-traffic window, then validate with crawls *and* server logs for 4–8 weeks. Expect a temporary dip. A dip that hasn't recovered after about 8–12 weeks means something is broken.

## Framework / Step-by-step
**Phase 1: Inventory (weeks −8 to −6)**
1. Union of URL sources: a full crawl, the last 6–12 months of server logs (every URL Googlebot requested), XML sitemaps, Search Console page exports, analytics landing pages, and backlink-tool target URLs (pages with referring domains).
2. Deduplicate and normalize (protocol, trailing slash, case, parameters). Tag each URL with template type, traffic, conversions, referring domains and index status.
3. Choose your **priority tier**: the top ~5–10% of URLs by traffic, revenue or links get manual mapping and QA. Everything else is rule-based.

**Phase 2: Redirect map (weeks −6 to −3)**
4. Write rules per template (for example `/blog/{slug}` → `/resources/{slug}`), then generate the map programmatically.
5. Manually map the priority tier one-to-one to the closest-equivalent new URL. Never send everything to the homepage.
6. Retired content: redirect to the closest relevant page. If none exists, return 404/410 deliberately; don't create soft 404s.
7. Collapse chains: old→new must be a single hop, and old internal redirects must be updated to their final targets.

**Phase 3: Staging QA (weeks −3 to −1)**
8. Crawl staging (blocked from indexing with authentication, *not* robots.txt alone). Check status codes, canonicals, hreflang, meta robots, structured data, internal links (to final URLs), pagination and rendered content parity for JavaScript pages.
9. Run the full old-URL list through the staging redirect rules. Target ≥99% returning 301→200, zero loops, zero chains.
10. Benchmark performance (Core Web Vitals) on key templates.

**Phase 4: Launch (day 0)**
11. Deploy redirects together with the new site. Remove staging auth and noindex. Check robots.txt.
12. Submit new XML sitemaps. Temporarily keep an *old-URL* sitemap as well, so Google recrawls the redirects faster.
13. For domain changes: verify both properties in Search Console and use the Change of Address tool. Re-upload an existing disavow file only if you had one.
14. Update canonical tags, hreflang, internal links, paid and email links, and high-value external links you control.

**Phase 5: Validation (weeks 0–8)**
15. **Crawl the old-URL list daily for the first week, then weekly.** Every URL should return 301 to a 200 page.
16. **Watch the logs:**
   - Verify Googlebot by reverse DNS or published IP ranges.
   - Track Googlebot hits per day on old vs new URLs. Old-URL hits should decline as new-URL hits rise.
   - Track the status-code mix (watch spikes in 404, 5xx or 302).
   - Note directories Googlebot hasn't touched since launch.
17. Search Console: watch Pages (indexed/not indexed), crawl stats, and the performance of old vs new URLs. Note the launch date in your reporting and analytics annotations.
18. Rank and traffic tracking on the priority tier. Investigate any page that lost more than 30% after about 4 weeks.

**Short on time? A compressed 4-week plan** (higher risk, so cut scope rather than QA):
- Week −4: inventory (crawl + logs + Search Console + backlink targets) and rule-based redirect map; hand-map the top ~5% of URLs.
- Week −3: build redirects on staging; test the full old-URL list (≥99% single-hop 301 → 200).
- Week −2: content/template parity check, internal links to final URLs, new sitemaps (split into a sitemap index, max 50,000 URLs or 50 MB per file).
- Week −1: go/no-go review. **No-go if** redirect pass rate < 99%, priority URLs not 1:1 mapped, or staging still has noindex/robots blocks. Prepare a rollback (keep old routing deployable).
- Weeks 0–4: daily old-URL crawl in week 1, log monitoring, Page indexing report; investigate any priority page down > 30%.
- Same-domain folder moves (e.g., `/blog/` → `/resources/`) don't use the Change of Address tool; redirects, internal links, canonicals and sitemaps do the work.

## Actionable checklist
- [ ] URL inventory from at least 5 sources, deduplicated and tagged
- [ ] Priority tier mapped by hand; the rest mapped by tested rules
- [ ] ≥99% of old URLs → single-hop 301 → 200 on staging
- [ ] Staging protected by authentication, not just robots.txt or noindex
- [ ] Internal links point to final URLs (no internal redirects)
- [ ] Old-URL sitemap submitted alongside new sitemaps at launch
- [ ] Change of Address tool used (domain moves)
- [ ] Log dashboard: Googlebot hits by status code and old/new URL, daily
- [ ] Keep redirects in place for at least 1 year (ideally permanently)
- [ ] Post-launch review at weeks 1, 2, 4 and 8

## Data points & benchmarks
- Google recommends keeping redirects for at least one year. Removing them early loses accumulated signals and breaks backlinks.
- Typical healthy migrations show a temporary fluctuation that recovers within weeks. Large structural or domain changes can take longer to settle.
- Pages with referring domains are the costliest to lose. Several practitioners value each recovered referring domain at hundreds of dollars in equivalent link-building cost.

## Mistakes to avoid
- Building the map from a crawl alone. Crawls miss orphaned URLs that logs and backlinks reveal.
- Redirecting everything to the homepage or a category page (treated as soft 404s)
- Launching with staging noindex or a robots.txt disallow still in place
- Changing URLs, templates, content and domain at once with no rollback plan. Stage changes where possible.
- Stopping monitoring after week 1

## Key principles
- Inventory is the migration. A URL you didn't list is a URL you'll lose.
- Logs show what Google actually did; crawls show what you built. You need both.
- Treat high-value URLs as individual projects and the long tail as a rules problem.
