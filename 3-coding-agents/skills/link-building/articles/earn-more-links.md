# How to Earn More Links: Add Context to Content Analysis

- **Updated**: 2026-10-05

## TL;DR
"Most-linked content" lists are dominated by mediocre posts on big sites (native audience, fast rankings, huge social, paid distribution) while great posts on small sites under-appear. Fix: score each post as the PERCENTAGE of its site's total referring domains it earned — the "overachievers" reveal the topics that win on merit, and almost nobody else analyzes this way.

## Framework / Step-by-step
The analogy: ranking players by total wins puts bit-part role players on great teams above all-time greats; switching to winning percentage fixes the list. Content analysis has the identical flaw when ranked by raw link counts.

**Method A — find overachieving content by topic:**
1. Search a topic in a content research database (one query returned ~77,000 pages; the top 10 were all very high-authority sites (roughly 77-90+ on the tool's scale) — several generic few-hundred-word posts)
2. Tailor the dataset with multi-metric floors: recent (last ~2 years), your language, shares ≥ 10, domain authority ≥ 15, referring domains ≥ 5, organic traffic ≥ 30 (→ ~900 pages). Multiple simultaneous floors filter spam — faking ONE metric is easy; faking several is hard
3. Pull domain-level metrics for every URL (a bulk URL-profiling tool or API)
4. Compute context: referring domains to URL ÷ referring domains to entire site = the post's share of the site's links
5. Sort by share. The overachiever list's average domain authority drops (one case: 90 → 56), and topic conclusions change: the raw list suggested "how to save for retirement"; the overachiever list revealed "average net worth" as the differentiated play

**Method B — find overachieving content by competitor (when topic is unknown):**
1. Identify competitors broadly (anyone competing for your audience's attention): use a competing-domains view or the domains ranking for your head keywords
2. Export each competitor's top content (prefix mode if content lives on a subdomain)
3. Merge exports, tag rows by company, compute each post's share: `=post RD / SUMIF(all rows for that site)` (works for social shares too)
4. Sort by share — small-site winners surface: for one custom-apparel store, the raw list pointed to a big brand's mega-listicles; the overachiever list revealed corporate outings/team-building content as the real link-earning niche
- Works even comparing only large sites against each other (recipe publishers example: overachievers per brand)

## Actionable checklist
- [ ] Pull your topic's page list; apply the six floors (recency, language, shares, domain authority, RD, traffic)
- [ ] Export; VLOOKUP domain-level RD from a bulk URL-profiling tool
- [ ] Add the URL-RD-to-site-RD share column; sort by it
- [ ] Analyze overachievers' common words/phrases for topic strategy
- [ ] Repeat per competitor when the topic isn't obvious (SUMIF version)
- [ ] Set your own "win" floor (5 RDs? 10?) to filter noise before crowning overachievers

## Data points & benchmarks
- One raw topic export: 77,000 pages, top 10 all very high authority (77-90+ on the tool's scale), several near-contentless
- After flooring: ~900 relevant pages (~1% of raw)
- Raw-list average authority score 90 vs overachiever-list average 56 (same topic)
- A 900-word generic post on a major publisher earned 51 RDs; a 5,000-word comprehensive post on a mid-size site earned 21 — the latter is the learning opportunity
- Big-site "top posts" often account for ~0.03% of their site's total links — they aren't game-changers even for their own sites

## Mistakes to avoid
- Skyscraping the raw "most linked" list — you're copying domain power, not content lessons
- Single-metric filtering — one faked metric slips through; several together don't
- Comparing absolute link counts across sites of wildly different sizes
- Ignoring overachievers on small sites because their absolute numbers look small
- Defining competitors too narrowly (media sites and adjacent businesses count)

## Key principles
- Links measure content + distribution; divide out distribution to isolate content quality
- A post earning 20 links on an unknown, unsupported site outperforms one earning 50 on a giant
- Multi-metric entry bars are cheap spam insurance
- Overachiever analysis yields a dataset most competitors never look at — a durable insight edge
- Reusable across topics, competitors, and even social-share analysis
