# Title Tag Audit at Scale (1k–100k Pages)

- **Updated**: 2026-10-05

## TL;DR
Don't rewrite every title. Crawl all titles, join them with Search Console data, and fix *technical* issues sitewide through templates: missing, duplicate, truncated or multiple titles. Then hand-rewrite only "opportunity" pages, those with high impressions, average position about 3–15 and below-expected CTR. Ship changes in batches with a holdout group so you can prove impact. Watch Google's rewrite rate as a quality signal.

## Framework / Step-by-step
1. **Collect.** Crawl the site and export URL, title, title pixel width, H1, indexability and template type. Export 3 months of Search Console page+query data (clicks, impressions, CTR, position).
2. **Join and classify.** Join on URL, then classify each page:
   - **Technical:** missing, duplicate, over ~600px, multiple `<title>` tags, or title ≠ topic.
   - **Opportunity:** impressions in the top 30% of the site, position 3–15, CTR below your site's CTR curve at that position by more than 20–30%.
   - **Rewrite risk:** Google shows a different title (compare the live SERP title on a sample).
   - **Leave alone:** low impressions, or CTR at or above the curve.
3. **Fix technical issues by template.** Product: `{Product} – {Key attribute} | {Brand}`. Category: `{Category} ({Count}+ options) | {Brand}`. Location: `{Service} in {City} | {Brand}`. Fix it once in the template and it applies to thousands of URLs.
4. **Hand-rewrite opportunities.**
   - Confirm the main query and its intent.
   - Front-load the keyword and keep it under about 600px.
   - Add a click reason (benefit, number, freshness, proof).
   - Align the title with the H1 topic.
   - Avoid clickbait the page can't back up.
5. **Batch with a holdout.** Change about 70–80% of an opportunity cohort and hold back 20–30% as a control. Compare the CTR change at constant position over 3–4 weeks. Roll out the winning patterns to templates.
6. **Monitor rewrites.** If Google keeps replacing a title, it usually means the title is too long, stuffed or mismatched with the content. Adjust toward the text Google chose.
7. **Repeat quarterly.** Intent drifts, so re-run the classification and refresh titles where CTR decays.

## Actionable checklist
- [ ] Crawl export joined with Search Console page data
- [ ] Technical issues fixed in templates, not page by page
- [ ] Opportunity list: high impressions, position 3–15, CTR well below the curve
- [ ] Your own CTR curve built from non-brand Search Console data
- [ ] Rewrites keep the keyword, add a click reason, stay under ~600px
- [ ] Batch changes with a 20–30% holdout cohort
- [ ] Compare CTR at constant position over 3–4 weeks
- [ ] Log every change (date, old, new) to attribute results

## Data points & benchmarks
- Google rewrites a meaningful share of title tags (one older study found about 33%), most often when titles are too long, stuffed, or don't match page content.
- Common issues across 1M+ sites in one older crawler dataset: title mismatched with the SERP title (68.5% of sites), too long (63.2%), too short (32.8%), missing (5.6%), multiple tags (3.0%).
- Titles are a small ranking factor but a big CTR lever. The gains show up in CTR at constant position.

## Mistakes to avoid
- Rewriting thousands of titles at once with no control group, so you can't prove impact
- Optimizing pages with no impressions
- Measuring raw clicks during a seasonal swing instead of CTR at constant position
- Stuffing secondary keywords into templated titles
- Ignoring Google's rewrites, which show what it thinks the page is about

## Key principles
- Fix systems (templates) before pages.
- Spend manual effort only where impressions already exist.
- Test, measure, then scale the winning pattern.
