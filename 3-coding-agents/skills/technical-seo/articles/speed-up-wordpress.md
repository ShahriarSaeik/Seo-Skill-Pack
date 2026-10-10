# How to Speed Up Your CMS Website in ~20 Minutes

- **Updated**: 2026-10-05

## TL;DR
Many CMS sites (e.g., WordPress) can go from mediocre to much better speed scores in under half an hour with 11 settings-level changes: remove dead plugins/extensions, move DNS to a fast provider, enable caching, minify, conditionally combine files, defer render-blocking assets, lazy-load media, optimize web fonts, preload key resources, add a CDN, and compress images. Test everything on staging — minify/combine steps can break code.

## Framework / Step-by-step
1. **Remove unused plugins/extensions** — every idle add-on can add load; deactivate and uninstall anything nonessential (leave anything you're unsure about).
2. **Switch DNS providers** — registrar-default DNS is usually slow; point nameservers to a fast free DNS provider.
3. **Install a caching plugin** — enables server caching (pre-built static pages) + browser caching (repeat-visit files); enable mobile caching too.
4. **Minify CSS/JS** — strips whitespace/comments, shrinking files; test before deploying (JS especially can break).
5. **Combine CSS/JS files** — helps only on HTTP/1.1 (files load consecutively); pointless on HTTP/2+ (parallel loading). Check your protocol first.
6. **Eliminate render-blocking resources** — defer non-critical JS and optimize CSS delivery (inline critical CSS) so above-the-fold content paints first.
7. **Lazy-load images and videos** — images lazy-load natively in modern CMS versions; extend to videos/iframes via plugin settings.
8. **Optimize web fonts** — every font costs a CSS request + download; use fewer fonts/weights and set font-display (swap or optional) so text renders immediately.
9. **Enable preloading** — tell browsers which resources matter most (`<link rel="preload">` for critical CSS/fonts) regardless of document order.
10. **Use a CDN** — global server network serves your site from near the visitor; enable in your plugin and point it at your CDN CNAME.
11. **Compress images** — bulk-optimize with a compression plugin and convert to WebP/AVIF (with fallbacks) where supported; choose a higher-quality setting if quality drops. (Lazy-loading doesn't help above-the-fold images.)

## Actionable checklist
- [ ] Audit installed plugins/extensions; remove the unused
- [ ] Move DNS to a fast provider (swap nameservers at registrar)
- [ ] Enable server + browser caching, including mobile
- [ ] Minify CSS/JS on staging; verify nothing breaks
- [ ] Check HTTP version; combine files only if pre-HTTP/2
- [ ] Defer JS; inline critical CSS
- [ ] Lazy-load below-fold images, videos, iframes (never the LCP image)
- [ ] Set font-display (swap or optional) for web fonts
- [ ] Preload the hero/CSS/font resources
- [ ] Connect a CDN
- [ ] Bulk-compress images; re-check quality
- [ ] Measure before/after with a page-speed report and a site-wide crawl

## Data points & benchmarks
- One reported result of this stack: page size 1.89 MB → 695 KB (-63%); requests cut ~50%; full load 5.9s → 4s; site-wide average/95th-percentile load times improved ~40%; lab speed score went poor → near-perfect.
- ~20 minutes of settings changes; no code rewriting required.
- Remaining slowness after all this = custom work (clunky theme, slow hosting, heavy third-party scripts) — hire a developer.

## Mistakes to avoid
- Testing optimizations directly on production — minification and file combination can break styling/scripts.
- Judging changes in a cached browser window — clear cache and verify in incognito.
- Combining files when the server already speaks HTTP/2.
- Lazy-loading above-the-fold images.
- Assuming plugins are free of conflicts — speed plugins can clash; isolate changes.

## Key principles
- Settings-level wins (DNS, caching, compression, deferral) beat code-level heroics for most CMS sites.
- Always measure before and after — site-wide crawl metrics, not just one page's score.
- File count matters on HTTP/1.1; file size always matters.
