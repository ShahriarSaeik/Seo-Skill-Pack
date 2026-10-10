# Robots.txt and SEO: Everything You Need to Know

- **Updated**: 2026-10-05

## TL;DR
Robots.txt controls crawling (not indexing) — one misplaced character can block your whole site from Google. Use User-agent + Disallow/Allow directives, keep rules specific, and never use robots.txt to deindex: use meta robots/x-robots-tag instead (a blocked page can't be seen to read its noindex).

## Framework / Step-by-step
**File basics:**
- Located at domain.com/robots.txt (root of each subdomain; separate file per subdomain)
- Format: `Sitemap:` line + `User-agent: [bot]` blocks with `Disallow:`/`Allow:` directives
- Supported by Google: Disallow, Allow, Sitemap. NOT supported: Crawl-delay (some other crawlers, such as Bing's, honor it), Noindex (informally honored by Google until Sept 1, 2019; now ignored), Nofollow (unsupported)
- User-agent names are case-insensitive, but paths in Disallow/Allow are case-sensitive (`/Photos/` ≠ `/photos/`); `*` = all bots; crawlers follow only the most specific matching user-agent block; new user-agent declaration = clean slate
- Conflicting rules (Google/Bing): longest directive (most characters) wins; if tied, least restrictive (Allow) wins. Other engines follow first matching directive.

**Core principle:** robots.txt prevents crawling, NOT indexing. Blocked pages can still appear in search results if linked externally. To exclude from index: use meta robots `noindex` or X-Robots-Tag — and the page must be crawlable for Google to see them.

## Actionable checklist
- [ ] Check domain.com/robots.txt exists and review all directives
- [ ] Verify no `Disallow: /` left from staging
- [ ] Use trailing slashes for folder blocks: `Disallow: /de/` not `/de` (avoids blocking /designer-dresses/, /delivery/ etc.)
- [ ] One directive per line; each user-agent declared once
- [ ] Use `*` wildcards for patterns (`Disallow: /products/*?`) and `$` for URL endings (`Disallow: /*.pdf$`)
- [ ] Add `Sitemap:` directive (helps other engines discover it; redundant but harmless for Google if submitted in Search Console)
- [ ] Add `#` comments explaining rules for humans
- [ ] Regularly check the Search Console Page indexing report for URLs blocked by robots.txt
- [ ] Use the robots.txt report (Search Console → Settings) to confirm Google fetched the file and see parse errors; use URL Inspection to check whether a specific URL is blocked (the old robots.txt Tester was retired in Dec 2023)
- [ ] If deindexing: remove robots block + apply noindex tag

## Data points & benchmarks
- Max robots.txt size: 500 KiB (Google).
- Crawl-delay of 5s caps a bot at ~17,280 URLs/day — dangerous for large sites.
- Google stopped honoring unofficial robots.txt rules such as noindex on Sept 1, 2019.
- Key user-agents: Googlebot, Googlebot-Image, Bingbot, Slurp (Yahoo), Baiduspider, DuckDuckBot.

## Mistakes to avoid
- Blocking URLs in robots.txt to remove them from Google — they can stay indexed ("Indexed, though blocked by robots.txt").
- Disallowing noindexed pages — Google can't crawl to see the noindex (per Gary Illyes).
- `Disallow: /de` without trailing slash — blocks every URL starting with "/de".
- Submitting sitemap URLs that are robots-blocked (Search Console "Submitted URL blocked by robots.txt" error).
- Setting crawl-delay for Google (ignored) or too high for Bing on large sites.
- Multiple directives on one line; re-declaring the same user-agent repeatedly (confusing).

## Key principles
- "Just one character out of place can wreak havoc on your SEO."
- Robots.txt = crawling control; meta robots/x-robots-tag = indexing control.
- Bots follow the most specific applicable user-agent rules — specificity overrides `*`.
- Longest directive wins in Google/Bing conflicts; first match wins elsewhere.
- Keep it simple and commented: fewer rules = fewer catastrophic mistakes.
