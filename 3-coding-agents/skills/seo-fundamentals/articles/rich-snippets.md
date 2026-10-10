# Rich Snippets (Rich Results): How to Earn Enhanced Listings

- **Updated**: 2026-10-05

## TL;DR
Rich snippets (now officially "rich results") are search listings enhanced by schema markup — star ratings, prices, stock status, event dates. They're not a ranking factor, but they increase visual prominence and click-through. Implementation = add valid structured data, validate it, then monitor it continuously.

## Framework / Step-by-step
1. **Check what's already marked up** — your CMS or plugin may already emit schema; audit a sample page's structured data before writing any code.
2. **Choose the right type** — match schema to actual page content (Product for ecommerce, Review for reviewable items, Recipe, Event, etc.).
3. **Generate JSON-LD markup** — JSON-LD is the recommended format; a CMS plugin, a markup generator, or a developer can produce it.
4. **Validate before deploying** — run the code (not just the URL) through a rich results testing tool before it goes live.
5. **Deploy in `<head>` or `<body>`** — either placement is acceptable.
6. **Validate again on the live URL** — confirm "valid items" detection after deployment.
7. **Monitor with scheduled crawls** — include structured data checks in routine site audits; prioritize fixes by page-level organic traffic.

## Actionable checklist
- [ ] Audit key page types for existing structured data (don't double-tag)
- [ ] Only mark up content that is actually visible to users on the page
- [ ] Use JSON-LD format
- [ ] Validate code pre-launch AND the live URL post-launch
- [ ] Review rich result status in Search Console for errors
- [ ] Re-validate after site redesigns, theme changes, or plugin updates (markup breaks easily)
- [ ] Fix invalid markup on high-traffic pages first

## Data points & benchmarks
- Review snippets (yellow stars) can appear for: books, courses, events, local businesses, movies, products, recipes, and software apps (check Google's current documentation for supported types).
- Since August 2023, FAQ rich results are shown only for well-known government and health sites, and HowTo rich results have been removed — don't invest in those types expecting display.
- Valid markup makes a page *eligible*, but there is no guarantee Google will show the rich result.

## Mistakes to avoid
- Marking up content that isn't visible on the page (violates structured data policies and risks manual action).
- Assuming rich snippets are a ranking factor — they aren't; the payoff is CTR, not position.
- Skipping ongoing monitoring: old or broken schema silently kills eligibility.
- Duplicating schema via both plugin and manual code.

## Key principles
- Rich results are an eligibility game: valid markup is necessary, Google's discretion is final.
- Vocabulary check: rich snippets = rich results (enhancements from your markup); SERP features (local pack, knowledge panels, videos) are Google-side additions you can't directly trigger.
- Enhanced listings earn attention, not rankings — prioritize on revenue-critical pages (products, key content) first.
