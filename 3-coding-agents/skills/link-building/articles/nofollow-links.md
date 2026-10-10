# Nofollow vs. Follow Links: Everything You Need to Know

- **Updated**: 2026-10-05

## TL;DR
A nofollow link carries a `rel="nofollow"` tag telling search engines not to pass PageRank or anchor text — so when building links, prioritize followed ones. But nofollow links still matter: they diversify your link profile, drive referral traffic that converts into followed links, and tagging paid/sponsored links (rel="sponsored", or nofollow) protects you from penalties. Audit both directions (inbound and outbound) regularly.

## Framework / Step-by-step
**Core mechanics:**
- Followed: `<a href="https://example.com">text</a>` — passes PageRank + anchor text.
- Nofollowed: same HTML plus `rel="nofollow"` — "in general" not followed, no PageRank/anchor credit. (Since March 2020, Google treats nofollow as a *hint* it may use or ignore for ranking; `rel="sponsored"` is preferred for paid links and `rel="ugc"` for user-generated content.) Check any link with right-click → Inspect, or a browser extension that highlights nofollow links.

**History that explains today's rules:**
1. **2005** — nofollow introduced to kill comment spam (CMS platforms apply it to comment links by default).
2. **2009** — PageRank "sculpting" killed: a nofollowed link still consumes its share of PageRank, so nofollowing internal links no longer concentrates flow to money pages. Nofollowing internal links now only makes sense for crawl prioritization (e.g., login/register links).
3. **2013 onward** — paid-link enforcement: any paid or sponsored link should be tagged rel="sponsored" or nofollow. Search engines want to credit *earned* links, not bought ones.

**Five-step nofollow audit of your site:**
1. **Find followed backlinks with keyword-rich anchors** (an exact-match anchor pattern, e.g., 19 domains all linking with "payday loans", signals bought links). Remediate by type: bought links → request removal or nofollow, else disavow; guest-post bio keyword anchors → swap to branded; widget links → nofollow in the widget HTML; sitewide links → nofollow or branded anchor. Pro tip for large sites: export followed anchors, run them through a keyword tool, sort by CPC high-to-low — high-CPC anchors surface the spam.
2. **Find followed links from sponsored posts** — search your backlinks for "sponsored" with a follow filter; ask for nofollow.
3. **Find keyword-rich followed outbound links on your own site** — check outgoing anchors if you accept guest posts or user-generated content (one major publisher blanket-nofollowed all outbound links in 2017 after contributors sold links).
4. **Check your own sponsored posts** — `site:yourwebsite.com "sponsored post"`; verify the sponsor's link is nofollowed.
5. **Find nofollowed internal links** — only login/cart-type pages should carry them; remove nofollow from any content link that was accidentally tagged.

## Actionable checklist
- [ ] When link building, filter prospects to followed links first (but don't discard strong nofollow prospects)
- [ ] Check your followed/nofollow ratio; flag 100%-followed or near it
- [ ] Tag every paid, sponsored, or affiliate link you place or sell with rel="sponsored" (or nofollow), and user-generated links with rel="ugc"
- [ ] Audit inbound followed anchors for exact-match clusters; investigate before disavowing
- [ ] Fix guest-post bio anchors (yours on other sites; others' on yours)
- [ ] Remove stray nofollow tags from internal content links
- [ ] Use nofollow on internal login/register links for crawl prioritization only

## Data points & benchmarks
- An older study of 44,589 SERPs found the correlation between rankings and *followed* backlink count was slightly weaker than for *total* backlinks — possible (not conclusive) evidence that some nofollowed links from strong pages are counted
- Rough heuristic (not a Google rule): a followed-share of roughly 60-90% of referring domains is typical; near-100% followed can look manipulated
- Common nofollow sources: social networks, forums, press releases, Q&A sites, wikis, pingbacks, directories
- PageRank splitting: 10 units + 10 outbound links = 1 unit each, regardless of nofollow on some of them

## Mistakes to avoid
- Buying followed links — competitors can report you, triggering manual review and penalties
- Disavowing or removing exact-match links without investigating context first (some occur naturally)
- Trying to sculpt internal PageRank with nofollow — obsolete since 2009
- Treating nofollow placements as worthless (traffic from them produces followed links)
- Leaving sponsored content on your own site followed (no rel="sponsored"/nofollow) — the risk runs both directions

## Key principles
- Followed links pass ranking power; nofollow links pass visibility, traffic, and profile diversity.
- A natural link profile is mixed — purity in either direction is a red flag.
- Link attributes are a disclosure device: use rel="sponsored" or nofollow honestly on anything paid, and expect the same from partners.
- Nofollowed mentions are a discovery channel: see → enjoy → recommend is how followed links actually happen.
