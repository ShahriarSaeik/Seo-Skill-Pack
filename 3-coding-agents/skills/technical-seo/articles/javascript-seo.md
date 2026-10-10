# JavaScript SEO: Issues & Best Practices

- **Updated**: 2026-10-05

## TL;DR
JavaScript SEO makes JS-heavy sites easy to crawl, render, and index. Most sites' JS causes no problems — issues arise when JS builds entire pages or injects/changes key elements. The safest architecture is server-side rendering, static generation, or prerendering; full client-side rendering is the riskiest and worst-supported by other search engines.

## Framework / Step-by-step
**How Google processes JS pages (two-stage indexing):**
1. Crawl — downloads HTML plus linked resources (file-size caps apply — 2 MB for HTML per a 2026 doc update, 15 MB default for other files; mobile user-agent first).
2. Processing — extracts links/resources to queue, caches every file aggressively, eliminates duplicates, applies the most restrictive directive seen.
3. Render queue — pages with noindex in the raw HTML are not rendered; news pages index from raw HTML first, rendered later.
4. Renderer — an evergreen headless Chromium. No fixed timeout; no clicking or scrolling, but the viewport is stretched (mobile 411→12,140px tall) so "below the fold" content is still seen; pixels are never painted.

**Core best practices:**
1. Unique titles/meta descriptions per page (JS frameworks are templatized — check for duplicates; SEO modules like head-tag managers exist per framework).
2. Canonicals: JS-inserted canonicals are respected only if none exists in raw HTML; never end up with two.
3. Remember: the most restrictive directive wins across raw vs rendered HTML (noindex in raw HTML never even reaches the renderer).
4. Don't block JS/CSS files in robots.txt — including on domains serving your API.
5. Verify content is DOM-loaded by default (search a quoted phrase in Google; use a browser-based SEO toolbar to compare raw vs rendered HTML; check anything behind accordions/dropdowns — Google doesn't click).
6. Links must be real `<a href>` elements — not onclick handlers, `javascript:` URLs, spans, or `<option>` tags.
7. Avoid `#` fragments for routing or parameters — use history-mode routers and clean URLs.
8. Handle error pages: JS can't return a real 404 — redirect to a real 404 URL, or noindex + error message (soft 404).
9. Infinite scroll: keep a paginated fallback; consider blocking the scroll-triggering script if pages merge in the index.
10. Use file versioning/fingerprinting (file.12345.js) so updated resources bust search-engine caches.
11. Structured data via JS-injected JSON-LD works — validate it.
12. Support HTTP connections — crawlers don't do WebSockets/WebRTC (provide fallbacks).

## Actionable checklist
- [ ] Render-critical content present in DOM without clicks
- [ ] Raw vs rendered HTML compared for titles, canonicals, robots tags
- [ ] JS/CSS crawlable in robots.txt (site + API domains)
- [ ] All internal links are `<a href>` anchors
- [ ] No hash-based routing/parameters
- [ ] Real 404 handling (or noindex fallback)
- [ ] Paginated versions exist alongside infinite scroll
- [ ] Sitemap generated via the framework/router ecosystem
- [ ] Alt attributes set on meaningful images
- [ ] URL Inspection tool used as source of truth for what the search engine sees

## Data points & benchmarks
- In an older study of title rewriting, Google rewrote titles 33.4% of the time and meta descriptions 62.78% of the time.
- In one older study, 67% of domains using hreflang had implementation errors.
- In one older study, pages reached the renderer at a median of ~5 seconds after crawling; 90th percentile was minutes — rendering delay is rarely a real problem.
- Rendering viewport (observed in one test): mobile loaded at 411x731, resized to 411x12140; desktop 1024x768 → 1024x9307.
- Googlebot's documented HTML size cutoff is 2 MB (15 MB default for other file types); keep HTML lean, especially with inlined JSON/state.
- XHR/fetch requests are NOT cached — they're fetched live during rendering and consume significant crawl budget.

## Mistakes to avoid
- Relying on full client-side rendering — other search engines (and social media crawlers reading OG tags) have limited or no JS support.
- Dynamic rendering (serving pre-rendered content per bot) — a discouraged, complexity-adding workaround.
- Checking pages with JavaScript disabled or via search-engine cache — both misrepresent what the crawler sees.
- Overwriting a raw-HTML noindex/canonical with JS and expecting the JS version to win — most restrictive signal prevails.
- The "five-second render timeout" myth — it comes from testing tools that fetch resources live and cut off early, not from the production renderer.

## Key principles
- Search engines load each page stateless, like a fresh visit — partial DOM updates during user navigation usually don't matter.
- Caching is aggressive: pages, JS, CSS are all cached and re-served at render time, which can occasionally index "impossible states" mixing old and new file versions — hence versioning.
- Don't fear JavaScript; partner with developers. The SEO's job is knowing how crawlers process it and how to troubleshoot, not writing it.
