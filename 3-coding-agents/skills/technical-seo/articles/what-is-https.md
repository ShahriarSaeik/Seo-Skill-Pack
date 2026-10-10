# HTTPS for SEO: Setup, Migration Mistakes & Fixes

- **Updated**: 2026-10-05

## TL;DR
HTTPS (HTTP over TLS encryption) is a lightweight ranking signal, a trust requirement, and the prerequisite for modern speed protocols (HTTP/2, HTTP/3). Migrate with a TLS certificate + 301 redirects, then audit for the five classic mistakes: leftover HTTP pages, mixed content, unupdated internal links, unupdated canonical/OG tags, and broken redirect chains.

## Framework / Step-by-step
**Certificates:**
1. Get a TLS certificate from a trusted Certificate Authority and install it on the server.
2. Validation tiers: DV (domain validation — free, fine for blogs), OV (organization validated), EV (extended validation — browsers no longer show special EV indicators, so it rarely adds value). All tiers encrypt equally; the choice is about organizational assurance, not ranking.
3. Wildcard certificates cover unlimited subdomains; SAN certificates can also cover separate domains.
4. Use TLS 1.3 with 1.2 fallback; disable TLS 1.0/1.1 (deprecated, dropped by browsers).

**Migration (HTTP → HTTPS):**
1. Install certificate; 301-redirect all HTTP URLs to HTTPS.
2. Update internal links, canonical tags, and Open Graph tags to HTTPS URLs.
3. Fix mixed content (HTTP resources on HTTPS pages) — a CSP of `upgrade-insecure-requests` fixes most of it.
4. Implement HSTS as the final step (prevents SSL-stripping downgrades).
5. New sites: launch on HTTPS from day one.

**Post-migration audit — the 5 mistakes:**
1. HTTP pages left → crawl with all URL sources; redirect stragglers (check ad-platform URL exports for unlinked PPC landing pages).
2. HTTPS pages loading HTTP resources → update resource URLs.
3. Internal links still HTTP → rewrite (avoids pointless redirect hops).
4. Canonical/OG tags still HTTP → rewrite; HTTP canonicals are usually ignored.
5. Failed redirects (chains/loops) → split chains into single 301 hops; update internal links to the final 200 URL.

## Actionable checklist
- [ ] TLS certificate valid and unexpired; renewal automated
- [ ] TLS 1.3 enabled, 1.0/1.1 disabled
- [ ] All pages 301 HTTP→HTTPS, no leftover HTTP URLs in crawl
- [ ] No mixed content warnings
- [ ] Internal links point directly to HTTPS 200 URLs
- [ ] Canonical + OG tags use HTTPS URLs
- [ ] HSTS header implemented (last step)
- [ ] Redirect chains collapsed to single hops
- [ ] Ad campaign destination URLs updated

## Data points & benchmarks
- HTTPS has been a lightweight Google ranking signal since 2014 — a tiebreaker, not a rocket booster.
- ~89% of websites default to HTTPS (one 2026 web technology survey; approximate).
- HTTPS→HTTP referral data is stripped: HTTP sites lose referral source visibility in analytics (shows as "direct").
- HTTP/3 (QUIC-based): ~35% global adoption in one survey; requires TLS 1.3; brings 0-RTT connection setup.
- A leading non-profit certificate authority issues free DV certificates and held ~64% CA market share in one survey.

## Mistakes to avoid
- Letting certificates expire because renewal isn't automated.
- Forgetting pages that exist only in ad platforms (no sitemap/links = invisible to crawls).
- Updating links but not canonical/OG tags (or vice versa).
- Endless redirect chains from stacking migrations — both users and crawlers pay the cost.

## Key principles
- HTTPS is table stakes: browsers label HTTP sites "Not secure," and major browsers are moving to HTTPS-by-default with explicit warnings for HTTP.
- The migration itself is routine; the damage comes from the half-finished edges (links, tags, redirects).
- External backlinks don't need updating — 301s consolidate signals; spend that effort internally.
