# Website Migration: More Than A Checklist

- **Updated**: 2026-10-05

## TL;DR
A migration is any significant change to domain, URLs, hosting, platform, or design. Success comes from preparation (baseline crawls, test pages, rollback plan), distinguishing "same URLs" vs "different URLs" scenarios, and monitoring after launch. Expect a few weeks of flux for a mid-size domain move; merges into an existing site may see no disruption at all.

## Framework / Step-by-step
**Prepare:**
1. Document what changes, who's involved, roles, deadlines — use a project tracker, not email/chat threads.
2. Keep a rollback plan to restore the original state.
3. Get Search Console + analytics access for old AND new site (combined view if possible).
4. Crawl the site as a baseline for before/after comparison.
5. Build a test-page set (top pages by traffic/links) to check for errors later.
6. Restrict staging/dev sites from being indexed; back up the site.

**If URLs stay the same** (hosting, platform, design changes):
- Compare before/after: canonicals, title tags, meta descriptions, headings, hreflang, schema, meta robots, content present in the DOM, internal links (breadcrumbs, nav, related posts), speed.
- Two big risks: leftover crawl blocks, and old redirects not copied from server config files (silently loses link equity — watch most-linked pages for 404s).

**If URLs change** (domain, protocol, structure):
- HTTP→HTTPS (easiest): install certificate, 301 redirect, add HSTS header, use a Content-Security-Policy of `upgrade-insecure-requests` to fix mixed content. Don't bother fixing the root-path redirect chain.
- Domain change: temporarily lower DNS TTL (a few hours), use the change-of-address tool in Search Console, check the old domain for manual actions.
- All: update internal links and tags (canonicals, hreflang); set up Search Console (sitemaps; re-upload an existing disavow file only if one exists); keep an old-URL sitemap short-term to monitor indexing; remove crawl blocks on old and new pages; ensure nothing is noindexed; 301-redirect pages (include images/PDFs; skip JS/CSS/font files).

## Actionable checklist
- [ ] Baseline crawl + saved test-page set before any change
- [ ] Rollback plan documented and tested
- [ ] Staging site blocked from indexing
- [ ] Crawl staging before pushing live
- [ ] Old URLs 301 (or 308) redirect to new — not 302/307
- [ ] Internal links and canonical/hreflang tags updated to new URLs
- [ ] Old-URL sitemap temporarily retained; new sitemap submitted
- [ ] Redirects and content verified on most-linked pages
- [ ] Traffic monitored across old + new properties for drops
- [ ] Old domain renewals monitored so nobody else registers them

## Data points & benchmarks
- Mid-size site migrating to a new domain: expect a few weeks of flux.
- Merging into an existing site: often no traffic disruption at all.
- Redirect only file types that get indexed (HTML, images, PDFs) — skip JS/CSS/fonts.

## Mistakes to avoid
- Running a migration without a rollback plan or baseline crawl.
- Leaving crawl blocks (robots.txt, auth) in place after launch — signals can't consolidate.
- Forgetting old redirects when changing hosts — hard-to-notice link equity loss.
- Outreach campaigns to change external links: 301s already consolidate signals; not worth the effort (update links you control).
- Letting the old site's SSL certificate expire — bots get redirected, users see an error.

## Key principles
- Almost anything that goes wrong can be fixed — catch changes early via staging crawls and post-launch comparisons.
- A drop after migration is almost always: broken redirects, crawl blocks, accidental noindex, removed/changed content, or changed internal links.
- Everything must remain crawlable on both old and new sites for signals to consolidate.
