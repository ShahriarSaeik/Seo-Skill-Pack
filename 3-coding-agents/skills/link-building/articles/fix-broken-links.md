# How to Find and Fix Broken Links (to Reclaim Link Equity)

- **Updated**: 2026-10-05

## TL;DR
Two separate problems: broken links ON your site (internal and outgoing) that waste equity and hurt UX, and broken backlinks TO your site (dead inbound links) whose equity "spills" on a 404. Fix outgoing links by replacing/removing; fix broken backlinks with a priority ladder ending in 301 redirects to relevant pages. One audited site had 80 referring domains pointing at a single dead URL.

## Framework / Step-by-step
**Part 1 — Broken links on your site:**
- Causes: link rot (the site you linked to deleted its page) or your own URL typos
- Find: crawl with a site audit tool or desktop crawler (a broken-external-links view works for small sites; full crawl for larger ones); check internal pages with 4XX status filters; the Page indexing report in Search Console also lists "Not found (404)" URLs Google has seen
- Fix: replace with a live equivalent (use a web archive to identify what the old target was) or remove the link outright. Tedious by design — delegate to a VA.

**Part 2 — Broken backlinks to your site:**
- Causes: you deleted/moved a page that had links, or the linking site made a URL typo (e.g., a stray bracket inside the href)
- Find: a backlink tool's top pages by links, filtered to 404 and sorted by referring domains (prioritizes the biggest leaks); a broken-backlinks view sorted by linking-page strength also works
- Fix, in priority order:
  1. **Outreach** — if the linker's typo caused it, ask them to correct the URL
  2. **Redirect to the new location** — if you moved the page (find it via `site:yourdomain.com "page title"`)
  3. **Recreate the content** at the broken URL
  4. **Redirect to the most similar relevant page** (find via `site:yourdomain.com + topic`) — the usual fix, since pages are usually deleted for a reason
  5. **Leave it as a hard 404** — acceptable last resort
- Recovering what a dead page WAS: web archive first; fallback = anchor/surrounding text of its backlinks; read a few linking articles for context
- Rules: redirects must preserve relevance (anchors describe the old page); never bulk-redirect dead pages to the homepage (search engines treat it as soft-404 behavior); 301s pass page-level equity; never serve soft 404s (200-status "not found" pages)
- Make it recurring: scheduled crawls as part of routine audits — new breakage accumulates constantly

## Actionable checklist
- [ ] Crawl the site; export all 4XX internal + external links
- [ ] Fix or remove every broken outgoing link (delegate if large)
- [ ] Export 404 pages with backlinks, sorted by referring domains
- [ ] For each: typo outreach → moved-page redirect → recreate → similar-page redirect → hard 404
- [ ] Verify no soft 404s and no homepage bulk-redirects
- [ ] Schedule automated re-crawls monthly/quarterly

## Data points & benchmarks
- One popular blog's single dead URL still held 80 referring domains — pure evaporating equity
- 301 redirects pass page-level equity (confirmed by Google representatives); keep them in place for at least a year, longer while the old URL still gets links or traffic
- Redirect relevance matters: anchor text of old links should still make sense on the redirect target

## Mistakes to avoid
- Confusing this with broken link BUILDING (exploiting competitors' dead pages — different playbook)
- Redirecting dead pages to the homepage "to be safe" — worst target, treated as soft 404
- Serving pretty 404 pages with 200 status codes (classic soft 404)
- Fixing once and never again — link rot is continuous
- Deleting/moving URLs without checking their backlink counts first

## Key principles
- Broken backlinks are free equity you already earned — reclaim before you build new
- Match the fix to the cause: their typo → outreach; your move → redirect; your deletion → recreate or re-route
- Relevance beats convenience when choosing redirect targets
- Hard 404 is honest; soft 404 confuses crawlers and users
- Treat link hygiene as scheduled maintenance, not a project
