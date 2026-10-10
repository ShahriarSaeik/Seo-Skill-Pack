# Nofollow vs. Follow Links: Index Creep & Link Control

- **Updated**: 2026-10-05

## TL;DR
Nofollow (rel="nofollow") tells search engines not to vouch for a link or pass PageRank/anchor text through it — used originally against comment spam, now also for paid/affiliate links and untrusted content. Internal links should essentially never be nofollowed; paid and user-generated links always. A natural profile mixes both: roughly 60-90% followed links is normal.

## Framework / Step-by-step
**What it is:** `<a href="…" rel="nofollow">` — identical UX to followed links, visible only in HTML. A robots meta tag of `nofollow` applies to every link on the page.

**History that explains today's rules:**
1. 2005 — introduced to kill comment spam (no ranking credit for links in comments/trackbacks).
2. 2009 — Google ended "PageRank sculpting": PageRank now divides across ALL outbound links, nofollowed or not, so nofollowing internal links no longer channels more equity elsewhere. (Remaining legitimate use: crawl prioritization on links like "login"/"register".)
3. Paid-link enforcement — paid/sponsored links have long had to be qualified; since 2019 the modern practice is rel="sponsored" for paid, rel="ugc" for user-generated content, and nofollow as the general case (all three are treated as hints, not directives).

**Why nofollow links still matter indirectly:**
1. Profile diversity — an all-followed profile looks manipulated.
2. Traffic — nofollowed placements (Q&A sites, forums, communities) get content seen, which earns followed links downstream.
3. Penalty protection — properly disclosing paid links keeps you safe from manual actions (and competitor reports).

**5-step audit:**
1. Followed backlinks with keyword-rich anchors → investigate for paid/manipulated links (remove, nofollow request, or disavow).
2. Followed backlinks from sponsored posts → request nofollow.
3. Keyword-rich followed outbound links on YOUR site (guest posts, UGC) → nofollow or remove; big publishers have gone site-wide nofollow for the same reason.
4. Sponsored posts on your site with followed links → add nofollow (search `site:yourdomain "sponsored post"`).
5. Nofollowed internal links → remove nofollow except for truly unimportant pages (login, register).

## Actionable checklist
- [ ] All paid, sponsored, and affiliate links nofollowed (or rel=sponsored)
- [ ] Guest post bio links use branded anchors or nofollow
- [ ] Comment/UGC links nofollowed (CMS default — verify)
- [ ] Widget/sitewide outbound links nofollowed
- [ ] No unexplained nofollowed internal links between valuable pages
- [ ] Followed vs nofollowed ratio checked (roughly 60-90% followed is normal)
- [ ] Anchor-text distribution scanned for keyword-rich followed anchors (sort by commercial intent to surface spammy ones)

## Data points & benchmarks
- ~85% of referring domains to one large SEO blog are followed; 60-90% followed is the typical healthy band.
- In an older study of ~44,600 SERPs, total backlinks correlated with rankings slightly more strongly than followed backlinks alone — weak evidence that some nofollowed links may count.
- PageRank division: with 10 links, 5 nofollowed, each followed link still passes only 1/10 (not 1/5) — sculpting is dead.

## Mistakes to avoid
- Nofollowing internal links to "concentrate" PageRank — it just discards equity and can orphan pages.
- 100% followed backlink profiles — a manipulation tell.
- Buying followed links and relying on Google not noticing — competitors can report you.
- Disavowing exact-match anchors without investigating context — natural exact-match links exist.

## Key principles
- Nofollow = "I don't vouch for this link." Use it for anything paid, untrusted, or user-generated.
- Treat nofollow as a hint: search engines may still crawl or count the link.
- When link building, prioritize followed placements — but never dismiss high-traffic nofollowed ones (referral traffic converts into followed links).
