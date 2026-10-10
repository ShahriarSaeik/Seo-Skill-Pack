# 301 vs. 302 Redirects for SEO: Which Should You Use?

- **Updated**: 2026-10-05

## TL;DR
301 = permanent move: the new URL gets indexed and link signals consolidate FORWARD. 302 = temporary move: the old URL stays indexed and signals consolidate BACKWARD. Use the type that matches reality — but if you slip, search engines often figure out your intent eventually (a long-standing 302 gets treated as a 301, sometimes immediately for established destinations).

## Framework / Step-by-step
**Use 301 when permanently:** changing a URL, migrating domains, moving HTTP→HTTPS, fixing www/non-www duplicates, merging pages, restructuring URLs.

**Use 302 when temporarily:** geo/language steering, A/B testing a page, gathering feedback on a new page without risking the old one's rankings, seasonal/promo redirects to a sales page.

**How search engines respond:**
- 301 → index the new URL; backlinks to the old URL effectively count for the new one. Exception: irrelevant redirects (e.g., blog post → homepage) are treated as soft 404s and pass nothing.
- 302 → keep the old URL indexed, signals consolidate backward. Exception: if the engine believes you meant permanent, it flips to 301 behavior — timing varies from days to months, or immediately when the destination is established.

**Auditing accidental 302s:**
1. Check individual URLs: URL Inspection tool — "not on Google" = treated as permanent; still indexed = temporary.
2. At scale: find 302 redirects that still earn organic traffic (a telltale sign they're treated as temporary); swap those to 301s. Verify canonicals match after recrawl.

**Implementation:** server config (one line per URL; regex rules for whole-site moves) or CMS redirect managers. For whole-domain moves, registrar/DNS-level forwarding beats keeping old hosting alive just to serve .htaccess (confirm it sends 301s, not 302s).

## Actionable checklist
- [ ] Map every redirect to permanent or temporary intent before choosing a status code
- [ ] Permanent moves: 301 (domain, HTTPS, www, merges, restructures)
- [ ] Temporary moves: 302 (tests, promos, geo-steering)
- [ ] Audit for accidental 302s on permanent moves — prioritize ones with organic traffic
- [ ] Verify relevance of redirect targets (irrelevant = soft 404 = no signal transfer)
- [ ] Confirm consolidation in a backlink tool (old referring domains credited to new URL)
- [ ] For domain moves, use registrar/DNS forwarding instead of paying for old hosting

## Data points & benchmarks
- 302→301 reinterpretation timing: usually weeks to months; can be immediate for redirects to established sites (one reported 302 site-to-site redirect flipped the indexed domain right away).
- Redirects are a canonicalization signal, not a directive — rare inversions happen both ways.
- Organic traffic landing on a 302-redirected URL = engine still treats it as temporary.

## Mistakes to avoid
- Using 302 for domain migrations or HTTPS moves (almost always permanent).
- Redirecting dissimilar pages and expecting link equity to transfer (soft 404 treatment).
- Fixing "accidental" 302s the engine has already reinterpreted — changing the code then changes nothing.
- Keeping old hosting alive solely to serve redirect rules — use DNS forwarding.

## Key principles
- Match the status code to the move's permanence — that's the whole rule.
- Signals follow the indexed URL: forward for 301, backward for 302.
- Relevance gates equity transfer; the engine must believe the destination is the same content.
