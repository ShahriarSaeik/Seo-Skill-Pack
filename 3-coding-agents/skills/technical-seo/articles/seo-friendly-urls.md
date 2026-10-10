# SEO-Friendly URLs: How to Build Them

- **Updated**: 2026-10-05

## TL;DR
The slug (the part after the domain) is the piece you control on every new page: reduce your title to the core keyword, lowercase it, hyphenate it. For the rest of the URL: HTTPS, brandable domain, .com-style TLD, subfolders for hierarchy, no dates, no parameters, no keyword stuffing. Rarely worth changing existing URLs.

## Framework / Step-by-step
**Building the slug (new pages):**
1. Start with the page title.
2. Remove special characters (commas, colons, semicolons, quotes — unsafe or hard to auto-link).
3. Remove numbers (they go stale when the content changes; titles are easy to update, URLs are not).
4. Remove superfluous words — but keep enough to describe the content.
5. Boil it down to the keyword people actually search (check what similar ranking pages target).
6. Optionally add 1-2 keyword modifiers for context (e.g., "seo").
7. Optionally make it readable (conjunctions, plurals).
8. Lowercase everything (case-sensitivity risks duplicate URLs on some servers).
9. Replace spaces with hyphens (not underscores; hyphens are the official recommendation).

**Rest-of-URL best practices:**
- HTTPS everywhere.
- Subdomains only when truly needed — many practitioners report traffic gains moving subdomain content into subfolders, despite official statements of equivalence.
- Memorable, brandable domain over keyword-rich domain.
- Generic TLD (.com preferred); some TLDs carry spam associations that hurt link building. ccTLDs for single-country targeting.
- Subfolders create hierarchy and context (`store/earbuds/apple/airpods` beats `buy-apple-airpods-earbuds`).
- Use as many subfolders as needed — depth itself isn't a ranking problem, but buried pages usually are; audit clicks-from-homepage instead.
- Avoid keyword repetition across path segments.
- Avoid dates in URLs (updates make them contradictory); set permalinks before publishing on a new site.
- Avoid URL parameters on indexable pages; canonicalize parameter duplicates.

## Actionable checklist
- [ ] Slugs: lowercase, hyphenated, keyword-first, no numbers/special chars
- [ ] Permalink structure set before publishing (no dates) on new sites
- [ ] Subfolders used for logical hierarchy
- [ ] No unnecessary subdomains
- [ ] Parameter-driven duplicates canonicalized
- [ ] Site crawl checked for deep pages (click depth, not folder count)
- [ ] Existing URLs left alone unless there's a strong reason

## Data points & benchmarks
- Hyphens are the officially recommended word separator; Google doesn't treat underscores as word separators.
- URLs get truncated in search results when long — keep slugs short.
- Spaces in URLs become %20 — never allow them.

## Mistakes to avoid
- Renaming slugs on a whim — redirects are easy to forget and usually not worth it.
- Keyword-stuffed slugs and repeated keywords across subfolders.
- Trusting subfolder count as a depth metric — measure internal link depth instead.
- Assuming a keyword-rich domain ranks itself — it hasn't worked that way for a long time.

## Key principles
- Describe the page in a few words, hyphenate — that's 90% of slug optimization.
- URLs are permanent; titles are mutable. Never bake mutable details (numbers, dates) into URLs.
- Subfolders are the default; subdomains are the exception.
