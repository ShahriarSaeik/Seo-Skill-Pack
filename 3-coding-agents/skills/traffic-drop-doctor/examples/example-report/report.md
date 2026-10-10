# Traffic Drop Diagnosis — trailpeak.example (demo)

_Periods compared: **Previous 28 days** (before) vs **Last 28 days** (after). Source: Google Search Console. Generated 2026-10-05._

## Executive summary

- Organic clicks went from **57,274 → 26,758 (-53.3%)**. Impressions changed -24.8%, CTR moved 7.37% → 4.57%, and average position moved 3.6 → 5.3.
- Of the 30,516 lost clicks, about **14,188 come from lower impressions** (visibility or demand) and **16,328 come from lower CTR** (clicks per view).
- The drop started around **2026-09-11** and looks like a **sudden step-down** (-51.1% over 14 days).
- Same 28 days last year: -6.4%, so this is **not** a normal seasonal dip.
- Recovery so far: no recovery yet (0% of the lost daily traffic is back).
- Events near the drop date: Demo core update (fictional) (2026-09-03–2026-09-18); Deploy v4.2: new deals template (2026-09-06).
- Most likely causes: **Indexing or technical problem in /deals/** (High); **Google algorithm update** (High); **Your own site change (deploy, migration, redesign, content change)** (High).

## Likely causes, ranked

_Shares of the drop can overlap (seasonality, for example, affects every section), so don't add them up._

1. **Indexing or technical problem in /deals/** (confidence: High)  
   Evidence: In /deals/: impressions fell 89.7% while average position held (4.3 → 4.3). Pages that rank where they did but almost never appear usually dropped out of the index partway through the period. This section explains 20% of the click loss. URL-inspect a few pages; check noindex, robots.txt, canonicals, 404s/redirects and recent deploys for this template.
2. **Google algorithm update** (confidence: High)  
   Evidence: Drop on 2026-09-11 matches Demo core update (fictional) (2026-09-03–2026-09-18); 48.5% of lost clicks come from ranking losses, concentrated in /reviews/. Don't change anything until the rollout has finished, then audit the affected pages against Google's helpful-content questions.
3. **Your own site change (deploy, migration, redesign, content change)** (confidence: High)  
   Evidence: Drop on 2026-09-11 is near 'Deploy v4.2: new deals template' (2026-09-06); the indexing problem in /deals/ fits this timing. Diff before/after crawls; check redirects, canonicals, noindex, removed pages and internal links.
4. **SERP change: AI Overviews or new SERP features taking clicks (rankings held)** (confidence: Medium)  
   Evidence: 31.2% of lost clicks come from queries whose position held but CTR fell; 54% of the total drop is a CTR effect. Informational queries lost 41.6% CTR at stable positions vs 8.3% for others: a typical AI Overview pattern. Affected sections: /guides/. Confirm by checking whether the losing queries now show an AI Overview or other features.
5. **Manual action or security issue** (confidence: Check)  
   Evidence: Can't be detected from performance data. Open Search Console → Security & Manual Actions. It takes 30 seconds, so always check.

## Recommended action plan

| # | Action | Addresses | Impact | Effort |
|---|---|---|---|---|
| 1 | Fix the section: remove noindex/robots blocks, restore or 301 removed URLs, correct canonicals, request reindexing | Indexing or technical problem in /deals/ | High | Low–Med |
| 2 | Let the rollout finish (check its end date on the Google Search Status Dashboard), then audit top losing pages against helpful-content questions; improve depth, originality, E-E-A-T | Google algorithm update | High | Med–High |
| 3 | Crawl every old URL; add single-hop 301s to the closest new page for unmatched URLs; fix chains; update internal links, canonicals and sitemaps; keep redirects 1+ year | Your own site change (deploy, migration, redesign, content change) | High | Low–Med |
| 4 | Rewrite titles/metas for the affected queries; add answer-first sections, schema and original data; shift effort to queries AI can't fully answer; track AI citations | SERP change: AI Overviews or new SERP features taking clicks (rankings held) | Med | Med |
| 5 | Check Security & Manual Actions; if present, fix and file a reconsideration request | Manual action or security issue | High | Varies |

## Where the lost clicks went (query patterns)

| Pattern | Share of lost clicks |
|---|---|
| Ranking loss (position dropped) | 48.5% |
| CTR loss (position held, fewer clicks) | 31.2% |
| Impressions loss at stable position (less demand, or pages dropping out of the index) | 19.6% |
| Mixed / unclear | 0.6% |

## Brand vs non-brand

| Segment | Clicks before | Clicks after | Clicks Δ% | Impr. Δ% | CTR before | CTR after | Pos. before | Pos. after |
|---|---|---|---|---|---|---|---|---|
| brand | 3,783 | 3,627 | -4.1 | -5.5 | 40.2 | 40.8 | 1.1 | 1.1 |
| non_brand | 42,037 | 17,781 | -57.7 | -25.1 | 6.86 | 3.87 | 4.3 | 6 |

## CTR at stable positions (AI Overview check)

| Query type | Queries | CTR before % | CTR after % | CTR Δ% |
|---|---|---|---|---|
| informational | 72 | 6.15 | 3.59 | -41.6 |
| other | 59 | 9.82 | 9.01 | -8.3 |

## Site sections

| Section | Pages | Pages → 0 impr. | Clicks before | Clicks after | Clicks Δ% | Impr. Δ% | Pos. before | Pos. after |
|---|---|---|---|---|---|---|---|---|
| /reviews/ | 18 | 0 | 24,815 | 10,016 | -59.6 | -29.1 | 3.7 | 7.7 |
| /guides/ | 18 | 0 | 21,051 | 11,523 | -45.3 | -6.2 | 3.5 | 3.7 |
| /deals/ | 12 | 0 | 6,678 | 684 | -89.8 | -89.7 | 4.3 | 4.3 |
| / | 1 | 0 | 4,344 | 4,176 | -3.9 | -5.4 | 1.1 | 1.1 |
| /(top-level pages) | 1 | 0 | 386 | 359 | -7 | -6.1 | 1.3 | 1.3 |

## Top losing queries

| Query | Clicks Δ | Pos. before | Pos. after | CTR before % | CTR after % | Pattern |
|---|---|---|---|---|---|---|
| top rated cooler | -348 | 3.9 | 8 | 7.07 | 4.07 | ranking_loss |
| best gps watch | -339 | 4.6 | 8.7 | 6.35 | 3.58 | ranking_loss |
| best headlamp 2026 | -307 | 4.6 | 8.6 | 8.15 | 4.55 | ranking_loss |
| top rated trekking poles | -295 | 4.7 | 8.8 | 6.67 | 3.84 | ranking_loss |
| best gps watch 2026 | -291 | 3.7 | 7.8 | 6.36 | 3.57 | ranking_loss |
| best cooler | -271 | 3.6 | 7.7 | 7.06 | 4.07 | ranking_loss |
| trail runners sale | -261 | 3.7 | 3.6 | 9.39 | 9.24 | demand_loss |
| trekking poles reviews | -257 | 4.4 | 8.5 | 6.67 | 3.83 | ranking_loss |
| tent deals | -253 | 5.5 | 5.5 | 9 | 9.28 | demand_loss |
| best hammock | -252 | 3.6 | 7.6 | 8.39 | 4.76 | ranking_loss |
| trail runners reviews | -250 | 4.7 | 8.7 | 9.16 | 5.2 | ranking_loss |
| best camping stove 2026 | -247 | 3.9 | 7.9 | 7.79 | 4.46 | ranking_loss |
| best trail runners | -247 | 5 | 9 | 9.15 | 5.2 | ranking_loss |
| top rated headlamp | -239 | 5.6 | 9.7 | 8.14 | 4.56 | ranking_loss |
| best hammock 2026 | -231 | 4.2 | 8.2 | 8.4 | 4.76 | ranking_loss |

## Top losing pages

| Page | Clicks Δ | Pos. before | Pos. after | Impr. before | Impr. after | Pattern |
|---|---|---|---|---|---|---|
| https://trailpeak.example/reviews/best-cooler/ | -1,215 | 3.5 | 7.6 | 28,657 | 19,900 | ranking_loss |
| https://trailpeak.example/reviews/best-gps-watch/ | -1,203 | 3.5 | 7.6 | 31,915 | 23,091 | ranking_loss |
| https://trailpeak.example/reviews/best-trekking-poles/ | -1,153 | 3.9 | 7.9 | 29,250 | 20,771 | ranking_loss |
| https://trailpeak.example/reviews/best-trail-runners/ | -1,049 | 3.8 | 7.9 | 19,274 | 13,742 | ranking_loss |
| https://trailpeak.example/reviews/best-base-layer/ | -1,049 | 4.1 | 8.2 | 27,894 | 19,137 | ranking_loss |
| https://trailpeak.example/reviews/best-hammock/ | -990 | 3.6 | 7.6 | 19,728 | 14,017 | ranking_loss |
| https://trailpeak.example/reviews/best-headlamp/ | -986 | 4.5 | 8.6 | 19,955 | 14,022 | ranking_loss |
| https://trailpeak.example/reviews/best-camping-stove/ | -971 | 3.3 | 7.3 | 20,942 | 14,852 | ranking_loss |
| https://trailpeak.example/reviews/best-tent/ | -822 | 2.7 | 6.8 | 21,873 | 15,959 | ranking_loss |
| https://trailpeak.example/guides/how-to-choose-hammock/ | -816 | 3.8 | 4 | 32,298 | 29,522 | ctr_loss |
| https://trailpeak.example/guides/how-to-choose-base-layer/ | -772 | 3.3 | 3.4 | 22,245 | 20,660 | ctr_loss |
| https://trailpeak.example/reviews/best-down-jacket/ | -748 | 4.1 | 8.1 | 15,957 | 11,190 | ranking_loss |
| https://trailpeak.example/deals/trail-runners-deals/ | -723 | 3.5 | 3.4 | 8,553 | 870 | demand_loss |
| https://trailpeak.example/guides/how-to-choose-headlamp/ | -708 | 2.7 | 3 | 23,644 | 22,609 | ctr_loss |
| https://trailpeak.example/reviews/best-bear-canister/ | -693 | 3.5 | 7.5 | 19,201 | 13,698 | ranking_loss |

## Devices

| Segment | Clicks before | Clicks after | Clicks Δ% | Pos. before | Pos. after |
|---|---|---|---|---|---|
| MOBILE | 36,655 | 17,125 | -53.3 | 4 | 5.4 |
| DESKTOP | 18,900 | 8,830 | -53.3 | 3.6 | 4.6 |
| TABLET | 1,718 | 803 | -53.3 | 4.2 | 5.1 |

## Countries

| Segment | Clicks before | Clicks after | Clicks Δ% | Pos. before | Pos. after |
|---|---|---|---|---|---|
| United States | 40,665 | 18,998 | -53.3 | 3.8 | 4.9 |
| Canada | 6,873 | 3,211 | -53.3 | 3.8 | 4.9 |
| United Kingdom | 5,155 | 2,408 | -53.3 | 3.8 | 4.9 |
| Australia | 4,582 | 2,141 | -53.3 | 3.8 | 4.9 |

## Timeline

![Daily organic clicks](timeline.png)

## Not visible in this data (check manually)

- Manual actions and security issues (Search Console)
- Crawl diff before vs after the drop (site audit crawler)
- Whether losing queries now show AI Overviews or new SERP features (search them, or use a rank tracker with SERP features)
- Competitors that gained the positions you lost
- Backlinks lost around the drop date

---
_Method: clicks are split into an impressions effect and a CTR effect. Each losing query and page is labeled by pattern, then scored against root-cause rules. This diagnosis is evidence-based but probabilistic, so confirm the top causes with the manual checks above before acting._
