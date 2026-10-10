# React SEO: Best Practices to Make It SEO-Friendly

- **Updated**: 2026-10-05

## TL;DR
React (and similar component libraries) default to client-side rendering (CSR) inside an app shell — content lives in the DOM, not the HTML source. Google renders JavaScript well now, but other engines and most crawlers don't, and CSR hurts first-load speed. Use SSR/SSG (e.g., via a framework like Next.js), serve correct status codes, avoid hashed URLs, keep real `<a href>` links, and don't inject essential HTML on interaction.

## Framework / Step-by-step
**How the pipeline works:** crawl (GET, save HTML/JS/CSS) → process (queue links from `<a href>`, resource URLs; stop at noindex) → render (headless Chromium executes JS, ~5s median queue) → index. Content only in the rendered DOM is at the mercy of the render step.

**The 6 best practices:**
1. **Pick the right rendering strategy** — prefer SSR (render on request) or SSG (pre-render at build; faster TTFB) over CSR: all crawlers see content, initial loads are faster, TTI improves. Frameworks let you mix (SSG for blog, SSR for account pages). Full hydration still hurts initial TTI; SSR/SSG wins for now. Also use built-in image/font/script optimization and dynamic imports.
2. **Use status codes correctly** — SPAs return 200 for everything (soft 404s) and use JS redirects instead of 3xx. If stuck on CSR: router framework + 404 component + noindex on not-found pages + visible "404" H1; JS redirects are followed but not ideal. SSR frameworks expose proper status-code helpers.
3. **Avoid hashed URLs** (#/path) — engines ignore the fragment; every hash route collapses to one URL. Use the History API for clean client-side URLs.
4. **Use `<a href>` links** — crawlers discover URLs from anchor elements; div/button navigation is invisible. Exception: deliberately hiding combinatorial faceted links from crawlers can conserve crawl budget.
5. **Don't lazy-load essential HTML** — content injected on click/hover (accordions, modals, tabs, mega/hamburger menus) is invisible until interaction. Audit those elements; ship content in HTML and toggle visibility with CSS instead.
6. **Keep the fundamentals** — canonicals, structured data, sitemaps, mobile-first, HTTPS, titles, semantic HTML all still apply.

**Audit technique:** compare raw HTML (view-source) vs rendered DOM (inspect); crawlers that store both make it easy to spot client-side-rendered titles, H1s, and content.

## Actionable checklist
- [ ] Choose SSR/SSG for indexable pages; reserve CSR for app-like areas
- [ ] Verify raw HTML contains titles, meta, canonicals, H1, primary content
- [ ] Return real 404/410 and 301/302 statuses (test with a bulk status checker)
- [ ] Replace #/ routes with History API URLs
- [ ] Inspect nav components for `<a href>` (not onClick divs)
- [ ] Check menus/modals/tabs for DOM injection on interaction; convert to CSS show/hide
- [ ] Enable framework image/font/script optimizations and code splitting
- [ ] Run CWV checks on both lab and field data — SPA initial loads are the weak point

## Data points & benchmarks
- Median crawl-to-render delay: ~5 seconds in one older study (reportedly up to a week before 2019).
- The rendering browser is evergreen Chromium — modern JS features render fine on Google; other engines (and most third-party crawlers) offer limited or no rendering.
- CSR apps can show positive field CWV for multi-page visits (client-side routing + diffing makes subsequent views fast) but fail on low pages-per-visit traffic.
- One audited major ecommerce brand had its entire mobile filter navigation injected on click — invisible to engines.

## Mistakes to avoid
- Assuming "Google renders JS" covers every crawler, tool, and AI retriever — it doesn't.
- Hash-based routing collapsing the site to one URL.
- Div/button navigation with no anchor tags — no discovery, no PageRank flow.
- Relying on full hydration for critical pages today (TTI penalty on first render).
- Soft 404s from always-200 SPA responses polluting the index.

## Key principles
- React is a tool, not an SEO verdict — configuration decides whether it helps or hurts.
- Content in the initial HTML is the only universally safe content.
- Real anchors and real status codes keep crawlers and audits accurate.
