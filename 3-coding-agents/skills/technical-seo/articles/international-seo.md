# 10 International SEO Best Practices + Checklist

- **Updated**: 2026-10-05

## TL;DR
International SEO in 10 steps: pick target markets via competitor traffic data, plan languages per country, choose subfolders (or ccTLDs — never URL parameters), install a CDN, do per-market keyword research, keep one language per page, keep internal links language-consistent, implement hreflang correctly, never auto-redirect by IP/cookies, and build country-specific backlinks.

## Framework / Step-by-step
1. **Define international markets upfront** — Check competitors' organic traffic share by country (a competitive traffic analysis tool) to spot demand you're missing.
2. **Consider all languages per market** — Canada needs EN+FR; language-first targeting is valid when resources are tight; country-specific content is optimal (currency, terminology, culture).
3. **Choose URL structure:**
   - ccTLDs (example.de): clear geo signal, localized hosting; costly, splits authority, maintenance heavy
   - Subfolders (example.com/de/): easiest, one domain, consolidated authority, easiest reporting — one practitioner's pick
   - Subdomains (de.example.com): customizable, localized hosting; crawled separately, similar cons to ccTLD
   - Parameterized URLs (?lang=de): avoid at all costs — not recommended by Google
4. **Install a CDN** — distributed servers keep load times low for all markets.
5. **Keyword research per market** — terminology differs by country ("ibis bird" US vs "bin chicken" AU, 12K/mo); use native speakers or a keyword tool that supports each market's language and dialect.
6. **One language per page** — separate URL per language; localize images, currency, time zones, phone numbers, addresses. No dynamic translation on a single URL.
7. **Internal links stay in-language** — cross-language links send conflicting signals and confuse users; a market with too few pages to link to isn't ready to launch.
8. **Implement hreflang properly** — Google uses the strongest same-language version for ranking position, then serves the most relevant regional variant.
9. **Never redirect by IP/cookies** — most Google crawls come from US IPs; you'd hide non-US content from Google. Prompt via banner/nav instead. Never give Googlebot a different experience (cloaking).
10. **Build backlinks per target country** — US authority doesn't transfer to Mexico; audit backlink geography (a backlink tool's breakdown by country and ccTLD).

## Actionable checklist
- [ ] Analyze competitor traffic-by-country to validate market potential
- [ ] Decide language-only vs country-specific rollout
- [ ] Set up subfolders (recommended) or ccTLDs; never parameters
- [ ] CDN live for all markets
- [ ] Localized keyword research done per market (not just translated)
- [ ] One language per URL; localized currency/imagery/metadata
- [ ] Internal links point only to same-language content
- [ ] Header/footer navigation populated for each market before launch
- [ ] Hreflang validated (site crawler's hreflang checks)
- [ ] No IP/cookie redirects; language switcher + suggestion banner instead
- [ ] Country-level backlink building plan; monitor backlink geography vs competitors

## Data points & benchmarks
- "Bin chicken" (AU): ~12,000 searches/mo vs near-zero for "ibis bird" in Australia (older figure).
- "Home insurance": UK = 67K monthly searches, highest of any country (older figure).
- Google crawls mostly from US IPs and rarely varies crawl location.
- Canada: English + French both official — need fr-CA and en-CA versions.

## Mistakes to avoid
- Parameterized URLs for internationalization (not recommended by Google).
- Auto-translating content on one URL instead of dedicated pages.
- Internal links crossing languages.
- IP/cookie-based redirects — including Googlebot-specific bypasses (cloaking).
- Launching a market with only a handful of pages.
- Assuming home-market backlink authority carries over to new countries.

## Key principles
- Localize everything: keywords, content, currency, imagery — translation alone isn't international SEO.
- Subfolders consolidate authority; ccTLDs split it but add user trust.
- Google serves the best language match using hreflang + the strongest version's ranking position.
- Treat every market as its own SEO campaign, including link building.
