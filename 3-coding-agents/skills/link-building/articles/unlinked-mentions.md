# A Simple Guide to Turning (Unlinked) Brand Mentions into Links

- **Updated**: 2026-10-05

## TL;DR
Unlinked brand mentions are the easiest link wins: the author already knows you, so you have a legitimate reason to ask for a link. Find mentions of your brand, products, spokespeople — even misspelled domains and stolen images — verify which pages don't link, then politely ask. ~29-30% of pages that mention a brand turn out not to link to it.

## Framework / Step-by-step
1. **Build a brand-term list** — brand name, product names, tool names, key spokespeople. Anything brand-related is fair game.
2. **Find mentions** — six methods:
   - a) a content research tool: search brand + `-site:yourdomain.com`; filter English, authority 30+, traffic 50+/mo; export
   - b) Google: `intext:brand -yourdomain.com -twitter.com -facebook.com...` (Google returns limited results per query, roughly 500 at most; use date filters to slice)
   - c) Reverse-engineer your social profile: a backlink analysis tool on your profile URL → backlinks → check which referring pages don't link to your site (~54% didn't in one test)
   - d) Domain misspellings: typo generator → a bulk URL analysis tool (whole-domain scope) → sort by RDs → check backlinks of typo domains for anchors with correct spelling but wrong URL
   - e) Stolen images: Google reverse image search or another reverse image search service on infographics, GIFs, logos → scrape URLs
   - f) mention alerts for ongoing monitoring — use OR operator for misspellings/products; weekly digest
3. **Filter to truly unlinked pages** — run URL lists through a site crawler's custom search with regex `<a [^>]*\bhref\s*=\s*"([^"]*yourdomain.com[^"]*)` (keep pages that do NOT contain a match); or a bulk link-checker tool.
4. **Prioritize** — a bulk URL analysis tool → sort by page-level authority (PageRank is page-level; a strong page on a domain that already links elsewhere is still worth pursuing).
5. **Outreach** — short, kind request; explain why the link adds value for their readers; offer bonus value (flag typos/broken links). Example email: pointed out the unlinked mention + suggested a title improvement → link added.

## Actionable checklist
- [ ] List all brand terms: company, products, tools, spokespeople (and common misspellings)
- [ ] Run a content research tool search with `-site:` exclusion + authority/traffic filters
- [ ] Crawl exported URLs with a desktop site crawler regex to isolate unlinked pages
- [ ] Sort opportunities by page-level authority (and traffic), not just domain authority
- [ ] Check misspelled-domain backlinks (typo generator + a bulk URL analysis tool)
- [ ] Reverse-image-search your best infographics/graphics for uncredited embeds
- [ ] Set mention alerts (weekly) for brand + misspellings via OR operator
- [ ] Email promptly — authors are more likely to edit fresh posts
- [ ] Skip mentions where a link adds no reader value

## Data points & benchmarks
- In one study of 558 brand-mentioning pages: **164 unlinked (~29%)**
- Of 530 pages scraped from Google: ~**30%** unlinked
- Of 262 pages linking to one brand's social profile: **~54%** didn't link to the brand's site
- Large-brand test (1 week): 393 pages with authority 30+ and 50+ monthly visits mentioning a major sportswear brand → **329 (84%) unlinked** (big brands are mentioned far more often than they are linked)
- Filters used: authority ≥30, organic traffic ≥50/mo, English

## Mistakes to avoid
- Being pushy when the mention doesn't warrant a link (or the site already links to you everywhere)
- Asking for links that add no reader value (negative-press mentions, irrelevant context)
- Chasing only new referring domains — page-level links matter too
- Assuming 100% success — even big brands fail on some perfectly good pitches
- Copying the sample email verbatim — write your own, personalize per site

## Key principles
- An unlinked mention means you're "already halfway" — familiarity exists; the ask is small.
- Act fast on new mentions (alerts) — recency increases edit likelihood.
- Give extra value in the ask (report errors, suggest improvements) to justify the edit.
