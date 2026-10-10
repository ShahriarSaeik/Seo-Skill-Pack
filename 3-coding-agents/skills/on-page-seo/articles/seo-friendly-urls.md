# How to Create SEO-Friendly URLs (Step-by-Step)

- **Updated**: 2026-10-05

## TL;DR
URLs are a minor ranking factor but affect clicks and future-proofing. Build slugs by stripping your page title down to its core keyword (no special chars, numbers, or fluff), then apply sitewide best practices: HTTPS, subfolders, lowercase, hyphens, no dates/parameters.

## Framework / Step-by-step
**The 9-step slug process** (for new pages; rarely worth changing existing slugs):
1. Start with your page title
2. Remove special characters (commas, colons, semicolons, quotes — hard to auto-link and parse)
3. Remove numbers (URL can't be easily updated when list lengths change; titles can)
4. Remove superfluous information (e.g. bracketed text like "(Our 4-Step Process)")
5. Boil it down to the keyword — the most popular way people search for the topic (check what similar top-ranking pages get traffic for via a free SEO toolbar or any SEO tool's organic keywords report)
6. Add keyword modifiers if the exact-match slug lacks descriptiveness (e.g. "seo", "html" — but never stuff: `html-meta-title-tag-seo` is too much)
7. Make it readable (optional): add conjunctions/plurals so it reads in a sentence — `/best-crm-tools-for-small-business/` not `/best-crm-tool-small-business/`
8. Make it lowercase (avoid case-sensitivity duplicate content)
9. Replace spaces with hyphens (Google's official recommendation; browsers convert spaces to %20)

**Rest-of-URL best practices:** use HTTPS; avoid subdomains unless necessary (many observed traffic gains after subdomain → subfolder moves); pick memorable/brandable domain over keyword-rich; use a TLD users trust (.com is familiar; Google treats generic TLDs equally, but cheap ones like .biz/.info are often spam-associated); use subfolders for hierarchy (`/store/earbuds/apple/airpods` vs spammy `/buy-apple-airpods-earbuds`); avoid keyword repetition (`/mens/mens-shoes/` → `/mens/shoes/`); avoid dates; avoid URL parameters on indexable pages.

## Actionable checklist
- [ ] Slug = target keyword (+ minimal modifiers), lowercase, hyphen-separated
- [ ] No numbers, dates, special characters, or filler words in slugs
- [ ] Fix CMS permalink settings BEFORE publishing (changing later risks breakage)
- [ ] HTTPS sitewide
- [ ] Content on subfolders, not subdomains, where possible
- [ ] Subfolder hierarchy that adds meaning instead of keyword-stuffed slugs
- [ ] Canonicalize parameter-generated duplicates (ecommerce facets/sorting)
- [ ] Audit: crawl the site and filter for pages deeper than 3 clicks to find buried pages
- [ ] Audit: crawl for duplicate content caused by parameter/duplicate URLs

## Data points & benchmarks
- HTTPS has been a lightweight ranking factor since 2014
- Google officially recommends hyphens over underscores
- Google says subdomains are treated the same as subfolders — but multiple SEOs report traffic increases after migrating to subfolders, so the safe default is subfolders
- Number of subfolders is NOT a ranking factor (Google), but deep folders often signal buried architecture
- Keyword-rich domains do NOT auto-rank for those keywords (Mueller)

## Mistakes to avoid
- Changing existing URL slugs without good reason (usually more harm than good)
- Numbers in slugs that go stale when content is updated ("7 tips" that becomes 10)
- Overly specific slugs that break on content updates (one large SEO blog's `/basic-guide-anchor-text/` had to be redirected after it outgrew "basic")
- Keyword repetition across subfolders and slug
- Low-trust, spam-associated TLDs (.biz, .info, .name)
- Dates in permalinks showing contradictory info in SERPs after updates

## Key principles
- "If you were to describe your page in a few words and replace the spaces with hyphens, that would usually be good enough for SEO."
- URLs should be short, descriptive, lowercase, hyphenated — and future-proof against content changes.
- If top-ranking pages for your topic get no traffic, the topic has no search potential — no URL optimization will fix that.
- Subfolders communicate hierarchy to users AND let you include keywords without looking spammy.
