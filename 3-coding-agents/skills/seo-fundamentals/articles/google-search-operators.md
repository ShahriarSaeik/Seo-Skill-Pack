# Search Operators: The Complete Command List and SEO Workflows

- **Updated**: 2026-10-05

## TL;DR
Advanced search operators are commands and characters (`site:`, `intitle:`, `-`, `OR`, quotes) that turn a search engine into a precision research tool. For SEO they power a dozen workflows: auditing indexing, competitor research, link prospecting, finding unlinked mentions, and tracking competitor publishing pace. Most operators are only useful in combination.

## Framework / Step-by-step
**Master the reliable core:**
- `""` exact phrase | `OR` / `|` either term | `-` exclude term | `*` wildcard | `()` grouping
- `site:` restrict to a domain or path | `intitle:` / `allintitle:` | `inurl:` / `allinurl:` | `intext:` / `allintext:`
- `filetype:` / `ext:` | `before:` / `after:` (dates) | `source:` (news) | `define:`, `map:`, `movie:`, `stocks:`, `weather:`, unit conversion `in`

**Know what's unreliable** (results hit-and-miss): number ranges `#..#`, `inanchor:`/`allinanchor:`, `AROUND(X)`, `loc:`, `location:`, `daterange:`.

**Know what's dead** (officially dropped or no longer reliable): `~` synonyms, `+` exact, `link:`, `info:`, `related:`, `cache:` (cached links removed in 2024), `phonebook:`, blog-search operators, hashtag search. Don't build workflows on these.

## Actionable checklist
- [ ] Audit indexing: `site:yourdomain.com filetype:pdf` — deindex gated lead-magnet PDFs via noindex headers
- [ ] Competitor recon: `[competitor] alternatives` / `[competitor] vs`; `site:competitor.com/section/` + `intitle:("what is"|"what are")` to profile their content strategy
- [ ] Guest-post targets: `[topic] intitle:"write for us" inurl:write-for-us` — better: find a serial guest author via `[topic] inurl:author/[firstname-lastname]` (editorial placements only; paid or sponsored posts need rel="sponsored"/nofollow)
- [ ] Resource-page links: `[topic] intitle:resources inurl:resources` (pitch only pages that link out)
- [ ] Internal-link opportunities: `site:yourdomain.com "target phrase"` — link unlinked mentions
- [ ] "Best-of" outreach: `best [category] -[yourbrand]` — pitch listicles that omit you
- [ ] Competitor reviews: `allintitle:review (competitor1 OR competitor2)` + `after:` for active sites
- [ ] Q&A targeting: `site:quora.com inurl:([topic 1] | topic 2)` for answerable threads (answer genuinely and disclose any affiliation; undisclosed promotion gets removed)
- [ ] Publishing pace: `site:competitor.com after:2026-01-01 before:2026-02-01` (includes republished pages — treat as estimates)

## Data points & benchmarks
- Roughly 40+ documented operators over the years; most core ones work reliably, several are unreliable, and many are deprecated.
- `link:` and `info:` died in 2017, and `cache:` was removed in 2024 — any tutorial citing them is stale.
- Practical cap: operator searches surface *pages*, not performance — pair with traffic estimates to confirm a pattern (e.g., a competitor's 86 definition-style pages turned out to be 20K+/month traffic pieces — worth copying).

## Mistakes to avoid
- Using operators solo — `site:` + `intitle:` + `inurl:` combined is where the precision lives.
- Building processes on deprecated or unreliable operators.
- Pitching every "write for us" result — everyone else does; author-footprint searches surface less-spammed targets.
- Reading `after:` results as first-publish dates — updated pages pollute the count.

## Key principles
- Operators find footprints; strategy is choosing which footprint matters (gated files, author bios, resource URLs, brand omissions).
- Every operator query you save is a reusable prospecting template — keep a library.
- Operators show existence, not value — always validate candidates with traffic/authority data before investing outreach effort.
