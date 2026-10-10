# Diagnosis Guide: Cause Signatures, Confirmation Checks, Manual Method

## Contents
- The 6 analyses
- Cause signature table
- How to confirm each cause
- Order of elimination
- Manual spreadsheet method (no code)
- Common traps

## The 6 analyses
1. **Totals and decomposition.** Compare clicks, impressions, CTR and position for before vs after. Then split the click change:
   - impressions effect = (Impr_after − Impr_before) × CTR_before
   - CTR effect = (CTR_after − CTR_before) × Impr_after

   The bigger effect tells you whether this is mainly a visibility problem or a click-through problem.
2. **Timeline.** Find the drop date (the biggest 14-day before/after change in daily clicks). Note its shape: a sudden step-down means an event; a gradual slope means decay, competition or demand. Compare the same weeks last year (seasonality). Check whether it has partly recovered.
3. **Query patterns.** Label each losing query:
   - **ranking_loss**: position worsened by 3 or more (or by 1.5 or more inside the top 10)
   - **ctr_loss**: position within ±1.5, CTR down 25% or more, impressions not collapsing
   - **demand_loss**: impressions down 30% or more at a stable position
   - **disappeared**: impressions fell to 0

   Then sum the lost clicks per label.
4. **Sections.** Group pages by their first URL folder. A cause that hits one template or section is almost always technical or content-specific to that section.
5. **Segments.** Brand vs non-brand, informational vs other queries (CTR at a stable position), device, and country.
6. **Event match.** Check the drop date against Google updates and the site's own changes (±7 days, allowing for indexing lag).

## Cause signature table
| Cause | Timeline | Impressions | CTR | Position | Scope | Tell-tale sign |
|---|---|---|---|---|---|---|
| Tracking or data glitch | Cliff to ~0 | ~0 | n/a | n/a | All | Zero days; analytics disagrees with Search Console |
| Sitewide deindexing (noindex, robots.txt, auth wall) | Cliff over days | ↓↓ | ~ | Stable for remaining URLs | All | "Excluded by noindex" or "Blocked by robots.txt" surge in the Pages report |
| Section indexing or technical problem | Step | ↓↓ in one section | ~ | **Stable** | One folder or template | Pages at zero impressions; deploy date nearby |
| Migration or redirect error | Step after launch | ↓ | ~ | ↓ | Old URLs | Old URLs 404 or redirect-chain; new URLs not indexed yet |
| Core or algorithm update | Step on update dates | ↓ | ↓ (follows position) | **↓ on many pages** | Sitewide or a content type | Exact date match; competitors gained |
| Spam update or manual action | Step | ↓↓ | n/a | ↓↓ | Sitewide or a section | Manual action notice; link-scheme or scaled content history |
| AI Overviews or SERP features | Gradual or step as features roll out | ~ or ↑ | **↓↓** | **Stable** | Informational queries | CTR loss at stable position, informational > other |
| Competitors or content decay | Gradual | ↓ | ↓ | Gradual ↓ | Specific pages | Fresher or better pages now outrank you |
| Seasonality or demand | Cyclical | ↓ | ~ | Stable | All or a topic | Same pattern in the same weeks last year |
| Brand demand | Gradual | ↓ brand | ~ | Stable | Brand queries | Branded impressions fall |
| Intent shift | Step | ↓ for specific queries | ↓ | ↓ | A few big queries | The SERP now shows a different content type |

(↓ = down, ↓↓ = sharply down, ~ = roughly unchanged)

## How to confirm each cause
- **Tracking:** compare with analytics. Check the Search Console property type (domain vs URL-prefix) and the verification status.
- **Indexing:** URL-inspect 3–5 affected URLs ("URL is not on Google"?). Check the Pages report reasons, view the page source for `noindex`, check robots.txt and canonical tags, and look at the HTTP status.
- **Migration:** crawl the old URL list and expect 301 → 200. Look for chains, loops and 404s.
- **Algorithm update:** look up the official rollout dates on the Google Search Status Dashboard. Compare the drop date at daily granularity. Search the top losing queries and see who gained.
- **Manual action:** Search Console → Security & Manual Actions.
- **AI Overviews or SERP features:** search the top CTR-loss queries in an incognito window from the right country and note any AI Overview, video, PAA, shopping, forum or other features. A rank tracker with SERP-feature history is faster.
- **Competitors:** for each of the top 10 losing queries, record who now ranks above you, and compare freshness, depth, format and links.
- **Seasonality:** compare year over year in Search Console, and check the topic's Google Trends curve.
- **Brand:** branded impressions trend vs brand activity (PR, ads, reputation).

## Order of elimination
Check the cheapest things first:
1. Tracking
2. Manual actions
3. Indexing and technical
4. Your own changes
5. Algorithm updates
6. SERP or CTR changes
7. Competitors and content
8. Seasonality and demand
9. Brand

## Manual spreadsheet method
Use this if you can't run the script. It needs the Compare export opened in any spreadsheet.
1. **Pages sheet.** Add these columns:
   - `ΔClicks = after − before`
   - `ΔPos = after − before` (positive means worse)
   - `ΔImpr% = after/before − 1`
   - `Section`: the first folder of the URL, e.g. `=REGEXEXTRACT(A2,"https?://[^/]+(/[^/]+/)")`
2. **Pivot by Section.** Sum the clicks and impressions for each period, and average the position weighted by impressions. Sort by ΔClicks. Look for:
   - a section with impressions down 60% or more and a stable position (indexing)
   - position up 2 or more (ranking loss)
3. **Queries sheet.** Add `CTR_b = clicks/impr` and `CTR_a`, then label each row with a formula:
   - `=IF(ΔClicks>=0,"ok",IF(impr_after=0,"disappeared",IF(ΔPos>=3,"ranking",IF(AND(ABS(ΔPos)<1.5,CTR_a<0.75*CTR_b),"ctr",IF(ΔImpr%<=-0.3,"demand","mixed")))))`
   - Pivot the sum of ΔClicks by label to get the share of loss per pattern.
4. **Brand split:** filter the queries that contain the brand name and compare the totals.
5. **Informational CTR:** filter queries starting with how, what, why or similar (or containing "?") that have a stable position, and compare their CTR change with the other queries.
6. **Timeline:** chart `Dates.csv` with a 7-day average. Mark update dates and deploys, and compare the same weeks last year.
7. **Migration pairing** (if URLs changed): put old and new URLs side by side and match them by slug (the last path part). For each old URL, check that it 301s to its pair. Old URLs with no pair and lost clicks are where the fix pays off.
8. **Seasonality adjustment:** seasonal share ≈ last year's % change ÷ this year's % change over the same 28-day windows. Remove that before splitting the rest between the other causes.

## Common traps
- Using queries for totals: anonymized queries are missing, so use pages or the overall chart.
- Average position rising (getting worse) because you *gained* new low-ranking impressions. Check impressions before you call it a ranking loss.
- Comparing weeks that contain different holidays, or different numbers of weekend days.
- Blaming an update that started 3 weeks before the drop.
- Reading a drop in a single page's clicks as sitewide.
- Ignoring that two causes can overlap. Quantify each one.
- Reading a migration as an indexing failure: a section that drops to zero is often just moving to new URLs. Check whether another section gained at the same time.
- Using an export that's weeks old. Always check the last date in the data.
