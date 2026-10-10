# SEO for Static Sites: 8 Problems to Watch For

- **Updated**: 2026-10-05

## TL;DR
Static site generators (and AI-"vibe-coded" sites) remove the CMS safety net: canonicals, sitemaps, redirects, metadata, schema, and 404 handling all become your job. Going static doesn't remove SEO work — it moves it from plugins/defaults to your build process. Audit for eight recurring failure modes.

## Framework / Step-by-step
The 8 problems and their fixes:
1. **Trailing slash & canonical conflicts** — framework and host may disagree on /page vs /page/, splitting signals. Fix: pick one format, align framework, host, canonicals, and internal links; crawl for conflicts.
2. **Robots.txt / sitemap / noindex conflicts** — code-generated sitemaps don't know which pages are noindex, so drafts and thank-you pages leak into search. Fix: one rule (e.g., a noindex flag) that both the sitemap and RSS feed respect; verify robots.txt exists and points to the right sitemap.
3. **Image optimization gaps** — images added outside the framework's pipeline bypass resizing/compression (some frameworks copy files raw by default). Fix: always use the framework's image component (ideally outputting WebP/AVIF with fallbacks); check for oversized files and missing alt text before publish.
4. **Template-driven metadata & schema errors** — one bad default in a shared template replicates to every page using it (e.g., auto-appended brand name overflows titles; wrong schema type). Fix: define metadata/schema requirements per page type before building; test multiple pages after any template change; validate markup.
5. **Incorrect HTTP status codes** — missing pages can return 200 OK with a "404-looking" page (soft 404s) when SPA fallback files are served for unknown routes. Fix: configure real 404s; request known-bad URLs and check the actual status code.
6. **Internal linking inconsistencies** — different templates/components emit mixed URL formats (with/without slash, relative vs absolute, case). Fix: standardize www, slash, absolute/relative, HTTPS, lowercase, extensions, hyphens, parameters, index pages; centralize in one link helper.
7. **Technical performance** — static generation ≠ fast; excess JavaScript, sitewide CSS, heavy third-party scripts, poor font/image loading still hurt. Fix: code splitting, critical CSS, right rendering strategy per page, defer non-essential scripts, CDN caching; test the built site, not assumptions.
8. **Migration pitfalls** — moving CMS → static silently drops redirects, sitemap rules, metadata logic, schema, and link behavior. Fix: treat it as a full migration — map every old URL, 301 all changes, diff old/new canonicals + metadata + schema + sitemaps, crawl both versions.

## Actionable checklist
- [ ] Verify /page and /page/ resolve to one canonical version site-wide
- [ ] Exclude noindex pages from sitemap AND RSS/feed logic; recheck when adding page types
- [ ] Confirm robots.txt exists, references the correct sitemap, and doesn't block wanted sections
- [ ] Route every image through the framework's optimization pipeline; audit for oversized files and blank alt text
- [ ] Test metadata/schema templates across several pages, not one example
- [ ] Request fake URLs and confirm they return real 404 status codes (not 200)
- [ ] Standardize one URL format in a shared link component (slash, case, scheme, www, hyphens)
- [ ] Audit JS/CSS weight, third-party scripts, and font loading on the live build
- [ ] Before any CMS→static migration: full URL map, 301s, canonical/metadata/schema diff, old+new crawls

## Data points & benchmarks
- A comprehensive site crawl (100+ technical checks) is a sensible scope for a static-site audit.
- In one blog's framework migration, a single misconfigured internal-linking rule nofollowed ALL internal links — one config error can sitewide-neutralize internal linking.
- One international blog migration (subfolder → subfolder) confirmed: URL changes without 301s lose links and ranking signals.

## Mistakes to avoid
- Assuming the static build is fast without testing — static HTML can still ship heavy JS/CSS.
- Trusting a preview that "looks fine" — oversized images, 200-status 404s, and template errors all survive previews.
- Letting AI-generated components pick their own URL formats and metadata conventions.
- Treating a CMS→static move as a redesign instead of a full SEO migration.

## Key principles
- Going static doesn't remove SEO work; it relocates it from CMS defaults to your build pipeline.
- One template decision scales everywhere — both an efficiency and a blast radius.
- No framework is "best for SEO"; evaluate on URL control, canonical/metadata generation, noindex + sitemap exclusion control, image tooling, schema validation, and redirect/404 effort.
- Small, infrequently updated sites suit static setups; complex publishing workflows may still need a CMS.
