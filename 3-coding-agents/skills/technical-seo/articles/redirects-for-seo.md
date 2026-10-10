# 11 Types Of Redirects & Their SEO Impact

- **Updated**: 2026-10-05

## TL;DR
Redirects forward users/bots from old URLs to new ones and are a canonicalization signal. Prefer server-side 301/308 for permanent moves (signals consolidate forward) and 302/307 for temporary ones (signals usually stay on the original URL). Avoid loops, overly broad rules, and expired SSL certificates on old domains.

## Framework / Step-by-step
**Redirect taxonomy:**
- Permanent: 301, 308, meta refresh (=0s), HTTP refresh (=0s), JavaScript, crypto redirect
- Temporary: 302, 303, 307, meta refresh (>0s), HTTP refresh (>0s)
- Preferred permanent order: 308/301 > meta refresh 0/HTTP refresh 0 > JavaScript > crypto
- Preferred temporary order: 307/302/303 > meta refresh/HTTP refresh
- Implementation locations: server-level (Apache .htaccess, Nginx, IIS, CMS plugins), DNS-level, CDN-level (edge rules/workers), HTML, HTTP headers

**Key behavioral rules:**
1. Permanent redirects = strong canonicalization hint → link signals consolidate to the NEW URL (a page with 10 backlinks redirects → new page benefits as if links pointed at it directly).
2. Irrelevant redirects (e.g., blog post → homepage) get treated as soft 404s; signals do NOT consolidate.
3. Temporary redirects = weak hint → signals usually stay on the ORIGINAL URL, but Google may swap to treating them as permanent after days/weeks/months (faster when target is an established page).
4. Verify treatment: Search Console URL Inspection on the old URL ("not on Google" = treated as permanent); or Search Console Links report to see where link signals consolidated.

## Actionable checklist
- [ ] HTTP→HTTPS redirect returns 301/308 (check with a free SEO toolbar; note HSTS sites show browser-cached 307 — check the server response in incognito)
- [ ] Implement HSTS + consider HSTS preload submission
- [ ] Redirect old URLs with backlinks: in a backlink tool, list your most-linked pages that return 404 → sort by referring domains → 301 to relevant current pages
- [ ] Keep redirect chains under 5 hops (Googlebot follows max 10; 5 per session)
- [ ] Fix redirect loops (remove the looping redirect; point to true final destination; update internal links)
- [ ] Match redirects 1:1 — avoid broad folder-level catch-alls (test with domain.com/random-garbage → should 404, not redirect)
- [ ] Renew/multi-domain SSL certs on old migrated domains (bots pass but users get errors)
- [ ] Keep redirects live at least 1 year (Google guidance), and indefinitely while the old URL still earns links or traffic
- [ ] During migration, redirect indexed files (images, PDFs) too — skip JS/CSS/fonts
- [ ] Update internal links to point directly at final URLs, not through redirects

## Data points & benchmarks
- Googlebot follows up to 10 redirect hops (5 per session); one practitioner's practical cutoff: fix chains >5 hops.
- Keep redirects at least 1 year for permanent signal transfer (per Google guidance).
- ~two-thirds of links on the web disappeared over a 9-year period (an older link-rot study) — old unredirected URLs lose real value.
- Google treats irrelevant redirects as soft 404s.
- Temporary redirects can be reinterpreted as permanent in days to months; international 302 homepage setups can stay "temporary" for years.
- 308 = 301 but preserves HTTP method (GET/POST); 307 = 302 with method preserved; 303 is form-resubmission prevention, treated like 302/307.

## Mistakes to avoid
- Using client-side (JS/meta refresh) redirects when server-side is possible — rendering can fail.
- Redirecting everything to the homepage — treated as soft 404, link signals lost.
- Overly broad redirect rules — can accidentally claim hacked/spam pages' links as yours.
- Letting old-domain SSL certs expire after migration — users hit errors, no redirect.
- Obsessing over 1 extra hop — chains <5 hops are fine.
- Trusting status codes blindly — a 200 OK page can still be redirecting.
- Removing redirects before 1 year or before checking whether users still hit old URLs.

## Key principles
- "Redirects are important for SEO" — they combine signals between pages and drive canonicalization.
- Permanent = consolidate forward; temporary = usually consolidate backward.
- Redirects are like postal mail forwarding for the web.
- Match redirects 1:1 and keep them as long as possible, ideally forever.
