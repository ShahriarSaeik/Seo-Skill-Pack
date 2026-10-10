# Hreflang: The Easy Guide for Beginners

- **Updated**: 2026-10-05

## TL;DR
Hreflang tells Google which language/region version of a page to show which users. It's bidirectional (every page in a cluster must reference all others + itself), best implemented in XML sitemaps for large sites, and 67% of implementations in one older study had errors. Hreflang is a signal, not a directive.

## Framework / Step-by-step
**Syntax:** `<link rel="alternate" hreflang="lang-country" href="URL" />` — ISO 639-1 language (+ optional ISO 3166-1 country, e.g., `en-gb`).

**3 golden rules:**
1. **Bidirectional** — if page A references B, B must reference A (forms an "hreflang cluster"; like a Facebook relationship status).
2. **Self-referencing tags** — each page lists itself plus all variants (optional per Mueller, but best practice).
3. **x-default tag** — fallback page when no language matches (recommended, not mandatory).

**Matching logic:** Google looks for language+country match → language-only match → x-default.

**3 implementation methods:**
1. HTML `<head>` tags — easy but must edit every variant when adding languages.
2. HTTP headers — for PDFs/non-HTML.
3. XML sitemap (xhtml:link markup) — often the most efficient: one file, no page edits, no page-weight overhead. Best for large sites; semi-automate with a spreadsheet template.

## Actionable checklist
- [ ] Every page in a cluster lists ALL variants + itself (+ x-default)
- [ ] Valid ISO codes only (en-gb not en-UK; dash not underscore)
- [ ] One URL per language per cluster (no duplicates like en-us AND en-uk pointing to identical content without localization)
- [ ] Hreflang points to canonical URLs only (never non-canonical)
- [ ] Hreflang targets return 200 (not broken/redirected)
- [ ] Don't block hreflang pages in robots.txt; don't noindex them
- [ ] Keep HTML lang attribute consistent with hreflang
- [ ] Schedule recurring site crawls with an hreflang check (return-tag errors, non-canonical or broken targets); Search Console's International Targeting report was retired
- [ ] Verify country traffic per language version in analytics or an SEO tool (e.g., /de/ should get DE/AT/CH traffic)
- [ ] Don't auto-redirect by IP/browser language — use a banner suggestion instead (redirects can block crawler access and risk cloaking)

## Data points & benchmarks
- 67% of hreflang implementations across 374,756 domains had issues (older industry study).
- Hreflang is one of ~40 Google canonicalization signals; cluster pages can share ranking signals (strongest page's rank position applies, SERP swaps to the user's best-match variant).
- Google + Yandex use hreflang; Bing has said it treats it as a weak signal (relies on content-language attribute, links, visitors); Baidu ignores it.
- No limit to number of hreflang tags per page.
- Google can often tolerate minor errors (underscore vs dash, en-UK vs en-GB, missing self-reference, relative URLs) — but don't rely on it; fix them.
- Canada language split: 56.9% English, 21.3% French (older census figures; example of multi-language same-country targeting).

## Mistakes to avoid
- One-way hreflang references (missing return tags) — cluster breaks.
- Same URL referenced for multiple languages.
- Hreflang + contradictory canonical tags.
- Auto-redirecting users by IP — cloaking risk and breaks indexing; use a small banner instead (too-large banner = interstitial penalty risk).
- Hreflang tags forced into `<body>` by broken `<head>` parsing (iframes, unclosed tags, JS injection) — ignored there.
- Assuming hreflang guarantees the right page shows — it's a signal, not a directive; localize same-language variants (pricing, spelling) to help.

## Key principles
- "One of the most complex aspects of SEO" — John Mueller.
- Hreflang = correct language version for users + duplicate-content mitigation + shared ranking signals within clusters.
- One practitioner prefers a single page per language with dynamic country personalization instead of en-us/en-uk duplicates.
- Automate implementation (sitemap + spreadsheet), audit continuously — errors are inevitable at scale.
