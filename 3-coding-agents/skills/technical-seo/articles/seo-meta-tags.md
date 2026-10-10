# Meta Tags for SEO: The Six That Matter

- **Updated**: 2026-10-05

## TL;DR
Six meta tags earn their place in the `<head>`: title, description, robots, viewport, charset, and meta refresh (which you should avoid using). Titles and robots carry real SEO weight; descriptions affect clicks, not rankings; viewport signals mobile-friendliness; charset prevents broken text; meta keywords is dead and should be removed.

## Framework / Step-by-step
**1. Meta title** — the primary snippet headline.
- Unique per page, descriptive, click-worthy (not clickbait), matches search intent, includes target keyword where natural, under ~60 characters.
- Four failure modes: too long/short, missing, multiple `<title>` tags on one page, duplicated across pages.

**2. Meta description** — the snippet pitch.
- Unique, accurate summary, under ~160 characters, keyword where natural.
- Not a ranking factor — but influences click-through. Expect rewrites.

**3. Meta robots** — controls indexing and link-following (not crawling): `index, noindex, follow, nofollow` in any combination; `none` = `noindex, nofollow`; absent tag = `index, follow`.
- Only set it when you actually want to restrict a page. Nofollow is treated as a hint.

**4. Meta viewport** — required for mobile-friendly rendering: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.

**5. Meta charset** — declare `<meta charset="UTF-8">` (HTML5 syntax) so browsers don't guess and garble text.

**6. Meta refresh redirect** — avoid; use a 301 server redirect instead.

## Actionable checklist
- [ ] Every page has exactly one unique title (<60 chars) and description (<160 chars)
- [ ] Site crawl checks for missing/duplicate/multiple titles and descriptions
- [ ] Meta robots set only where restriction is intended — audit for rogue noindex/nofollow
- [ ] No noindexed pages also blocked in robots.txt (noindex becomes invisible)
- [ ] No noindexed pages listed in the sitemap (except temporarily while waiting for them to drop from the index)
- [ ] Viewport tag present on all pages (usually theme-level); verify in Lighthouse/Chrome DevTools device mode (Search Console's Mobile Usability report was retired in Dec 2023)
- [ ] UTF-8 charset declared site-wide
- [ ] Meta refresh redirects replaced with 301s (add a canonical if one must remain)
- [ ] Meta keywords tags removed sitewide (usually one line in the CMS template)

## Data points & benchmarks
- Title tags: keep under ~60 characters; meta descriptions: ~160 characters.
- Google has ignored the meta keywords tag since 2009; one major alternative search engine has stated it uses keyword stuffing as a spam signal.
- Google rewrites meta descriptions for the majority of queries — write for the user, not the snippet.

## Mistakes to avoid
- Stuffing meta keywords — pointless at best, a spam signal at worst.
- Using meta refresh redirects — inconsistent browser support, confusing for users, slower than server redirects.
- Assuming Google always shows your title/description — it often substitutes its own.
- Setting `noindex` then blocking the page in robots.txt — the directive can't be seen, and the URL may still appear in results.

## Key principles
- Titles are the highest-leverage meta tag: they influence both rankings (as content/relevance signals) and clicks.
- Meta descriptions = click optimization, not ranking optimization.
- The viewport tag is a prerequisite for a usable mobile layout; mobile-friendliness was a ranking signal from 2015 (historical), and mobile-first indexing is now universal.
