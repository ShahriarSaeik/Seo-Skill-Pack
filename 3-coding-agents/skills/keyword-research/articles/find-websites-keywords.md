# How to Find What Keywords a Website Ranks For

- **Updated**: 2026-10-05

## TL;DR
Two different questions get confused: searching for words in a site's text (browser find, search operators) versus finding the keywords a site actually ranks for or bids on (requires rank-data tools). Text presence ≠ ranking — pages rank for phrases they never use verbatim — so competitive keyword analysis needs organic and paid keyword reports, not text search.

## Framework / Step-by-step
1. **Clarify the goal** — "what words appear on this page/site" vs. "what does this site rank for in organic search" vs. "what does it bid on in paid search."
2. **For plain text search** (fast, no tools):
   - Single page: ctrl/cmd + F on the page.
   - Whole site: search operators — `site:<domain> "exact phrase"`; page titles only: `site:<domain> intitle:"phrase"`.
3. **For organic rankings** — any keyword research tool with a site-level organic keywords report:
   - Enter the URL; choose scope — entire domain, a path/subfolder, or exact URL (e.g., compare blogs via their /blog path).
   - The report returns every keyword the site ranks for, with position, search volume, difficulty, and often ranking history.
   - Refine with filters: low difficulty only, keywords containing specific words, position ranges.
4. **For paid keywords** — the same tools' paid keywords report: keywords the site bids on, plus cost per click, volume, estimated paid traffic, and the landing page with its ad creative.
5. **For your own site, free** — connect Search Console; note the limits (~1,000 rows visible at a time, ~16 months of history) and that it only covers sites you own.

## Why weaker methods fall short
- **On-page text** — a word on a page doesn't make it a ranking. Pages routinely rank for terms used nowhere in the copy (one example article ranks #3 for a phrasing it never uses verbatim).
- **Search operators** — prove a phrase exists on indexed pages, not that it ranks normally; you'd have to query every phrase and would still get no metrics.
- **Meta keywords tag** — obsolete; Google ignores it and it reveals nothing reliable.
- **Title tags** — reveal one intended target keyword per page, without ranking proof or metrics, one page at a time.
- **Ad-planner tools fed a URL** — mix "some keywords the page ranks for (unlabeled)" with "topically relevant ad suggestions," and overestimate volumes at group level.
- **Search Console** — accurate but owned-sites-only, with row and history caps.

## Actionable checklist
- [ ] Pick the scope deliberately: domain vs subfolder vs URL changes the answer
- [ ] Pull the organic keywords report; note position, volume, KD per keyword
- [ ] Pull the paid keywords report to see monetization priorities and CPCs
- [ ] Filter out brand-name keywords when sizing a competitor's real market coverage
- [ ] Use text search (site:/intitle:) only for content audits, never as ranking evidence
- [ ] For your own site, combine Search Console data with a fuller organic keywords export

## Data points & benchmarks
- Search Console's interface exposes ~1,000 rows at a time and ~16 months of history
- Example: a page ranking #3 for a query that appears nowhere in its text
- URL-fed ad-planner lookups blend ranked + suggested keywords and inflate group volumes

## Mistakes to avoid
- Treating keyword mentions on a page as evidence of rankings
- Analyzing an entire domain when the question concerns one section (blog vs product pages)
- Skipping paid keywords when assessing a competitor — bids reveal what's profitable
- Trusting verbatim operator matches as a proxy for normal rankings

## Key principles
- A keyword in the SEO sense is a query with a ranking — not a string of text.
- Organic keywords show visibility; paid keywords show monetization intent; serious analysis uses both.
- Scope (domain/path/URL) is the first decision in any site keyword analysis.
