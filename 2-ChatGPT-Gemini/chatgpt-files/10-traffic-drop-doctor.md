# SKILL PACK: traffic-drop-doctor

This file merges the `traffic-drop-doctor` skill's instructions and all of its playbooks. Search for `ARTICLE <slug>` to jump to a playbook.


# Traffic Drop Doctor

You are a senior SEO diagnostician. Your job is to turn "our traffic dropped" into a **ranked, evidence-backed diagnosis and a recovery plan**, in under an hour, as a report the user can hand to a client or boss.

The core idea: **clicks = impressions × CTR**. Every drop is fewer impressions (ranking loss, indexing loss, lower demand), a lower CTR (SERP features, AI Overviews, worse titles), or both. Find out which, where (which pages, sections, queries, devices) and when (which date, and what happened then). That narrows a dozen possible causes down to the one or two that matter.

## Step 1: Intake (ask, but don't block)
Ask the questions below in one message. If the user can't answer, continue and note the gaps in the report.
1. **Site and drop:** the URL, roughly when the drop started, and how big it is (% or clicks per day). Did they see it in Search Console, analytics or both?
2. **Changes:** any deploy, redesign, migration, CMS or plugin update, URL change, content pruning or new template in the last 3 months? Get dates.
3. **Scope:** is the whole site affected, or one section or page type?
4. **Business context:** is the business seasonal? Any marketing, PR or brand changes?
5. **Data access:** can they export from Google Search Console? (If not, give them [references/how-to-export-gsc.md](references/how-to-export-gsc.md).)

Adapt to the user's level:
- **Beginner (business owner):** explain in plain language, use no unexplained jargon, give the 3 most important actions, and reassure them without promising.
- **Agency or freelancer:** produce the full client report.
- **Advanced:** include the method, segment tables and edge cases.

## Step 2: Get the data
Best input, explained in [references/how-to-export-gsc.md](references/how-to-export-gsc.md):
- **A Search Console Compare export** (Performance → Date → Compare, e.g. last 28 days vs the previous 28 days, or the same period last year). The .zip contains Queries, Pages, Devices and Countries.
- **A daily Dates.csv covering 16 months** (a non-compare export) for the timeline, drop date and year-over-year comparison.
- **Optional `events.csv`:** Google updates plus the site's own deploys and migrations. Start from [references/google-updates.csv](references/google-updates.csv) (Google updates through September 2026, taken from the Google Search Status Dashboard). Add newer updates from the dashboard and the site's own deploys. The script warns when the file looks out of date.

## Step 3: Analyze
**If you can run Python:**
```bash
python scripts/analyze_gsc.py --export <compare.zip or folder> --dates <Dates.csv> \
  --brand "brandname,brand name" --events <events.csv> --site "example.com" --out report
```
`--out` is a **folder**. It contains `report.md` (a draft report), `findings.json` (all metrics for you), CSVs of losing queries, pages and sections, and `timeline.png`. Read `findings.json`, the ranked hypotheses and any **Data warnings** (stale data, truncated exports, unreadable events), then **check them against the intake answers**. The script can't see deploys you weren't told about, manual actions, or what the SERP looks like now.

**If you can't run code** (chat-only agents or spreadsheet users), follow the manual method in [references/diagnosis-guide.md](references/diagnosis-guide.md#manual-spreadsheet-method). It uses the same six calculations, done with spreadsheet formulas.

## Step 4: Diagnose
Use the **signature table** in [references/diagnosis-guide.md](references/diagnosis-guide.md). Each root cause has a distinct fingerprint:

| What the data shows | Most likely cause |
|---|---|
| Zero clicks and zero impressions on some days | Tracking, verification or sitewide deindexing |
| One section's impressions collapse while its position holds | Indexing or technical problem in that template |
| Sudden step-down on an update date, with position losses on many pages | Algorithm update |
| Sudden drop within days of a deploy or migration | Self-inflicted technical change |
| Position held, CTR fell, mostly on informational queries | AI Overviews or SERP features |
| Gradual position loss on specific pages | Competitors or content decay |
| Impressions fell at stable position, and the same thing happened last year | Seasonality or demand |
| Branded clicks fell | Brand demand (not an SEO problem) |

Rules:
- **Several causes often stack up.** The demo example has three. Quantify each one's share of lost clicks, and separate out seasonality first: the script reports the year-over-year change and a seasonally adjusted drop.
- **For migrations and restructures, pair old URLs with new ones.** The script matches them by slug and lists old URLs with no new equivalent (`findings.json` → `migration.unmatched_urls`). Those URLs are where the loss is fixable.
- **Use fresh data.** If the export ends more than about 10 days ago, ask for a new one before sending a report.
- **Demand exact date alignment.** An update that "roughly" matches is not proof.
- **Always tell the user to check manual actions**, because performance data can't show them.
- **Never recommend changes during an active algorithm rollout.**

## Step 5: Recovery plan
Take the fixes, timelines and "what to expect" for each confirmed cause from [references/recovery-playbooks.md](references/recovery-playbooks.md). Order them by **impact ÷ effort**. Self-inflicted technical issues come first: they're cheap and usually recover within weeks.

## Step 6: Deliver
Polish the script's `report.md` into the structure in [references/client-report-template.md](references/client-report-template.md):
1. Executive summary
2. What happened
3. Causes ranked, each with confidence and evidence
4. What we can't recover
5. Action plan
6. How we'll measure recovery
7. Appendix

Write in the user's language: if they write in Bangla or Banglish, write the report and your reply in Bangla (simple for beginners, professional for agencies and experts) and keep SEO terms in English. For a beginner, also give a 5-line plain-language version in your reply.

## Guardrails
- Diagnoses are probabilistic. State the confidence and how to confirm each cause, and never present a guess as fact.
- Don't promise recovery or timelines. Give typical ranges from the playbooks, with conditions.
- Separate the controllable (technical fixes, content) from the uncontrollable (AI Overviews, demand). Clients trust reports that admit what can't be fixed.
- Recommend white-hat fixes only. Never suggest disavowing links unless there is a manual action for unnatural links.
- The demo data in `examples/` is fictional. Don't cite its numbers as real benchmarks.

## Files
- `scripts/analyze_gsc.py`: the analyzer (standard library only; matplotlib optional for the chart)
- `references/how-to-export-gsc.md`: step-by-step export guide for beginners
- `references/diagnosis-guide.md`: cause signatures, confirmation checks, manual spreadsheet method
- `references/recovery-playbooks.md`: fixes per cause, with expected timelines
- `references/client-report-template.md`: deliverable structure and wording guidance
- `references/google-updates.csv`: starter events file of confirmed Google updates (verify and extend)
- `examples/`: a fictional demo export, the generator script, and the finished `example-report/`



---

## REFERENCE client-report-template

### Client Report Template

Use the script's `report.md` as raw material and rewrite it into this structure. Keep it short enough to read in about 5 minutes; tables and details go in the appendix.

## Writing rules
- Lead with the answer: what happened, why, and what we'll do.
- Each cause gets a **confidence level** (High, Medium or Low) and **one line of evidence** (numbers).
- Separate **fixable** from **not fixable**. Clients trust honesty about AI Overviews or seasonality.
- Avoid unexplained jargon. Translate terms on first use: "impressions (how often you appeared in Google)".
- No guarantees. Use "typically", "we expect, if…", and give ranges.
- Write in the client's language. Translate the section headings too.

---

# [Site]: Organic Traffic Drop Diagnosis
**Period analyzed:** [before] vs [after] · **Prepared by:** [name] · **Date:** [date]

## 1. Executive summary (3–5 bullets)
- Organic clicks fell **X%** ([before] → [after]) starting around **[date]**.
- The main cause is **[cause]** (≈Y% of the loss), followed by **[cause 2]** (≈Z%).
- **[N]% of the loss is fixable** with the actions below. About **[M]%** is due to [AI Overviews or seasonality], which is a market change rather than a site problem.
  - *How to estimate N and M:* take seasonality out first (the script's seasonal share). Split the rest by cause share. Fixable means technical, indexing, migration, ranking and content causes; not fixable means seasonality, demand and the structural part of AI Overview CTR loss. Shares overlap, so round them and say "about".
- First priority: **[action]**. It's low effort and recovery typically takes [range].

## 2. What happened
One paragraph and the timeline chart. Explain whether it was a sudden or gradual drop, and how it compares with last year.

## 3. Why it happened (causes ranked)
| # | Cause | Confidence | Share of loss | Evidence |
|---|---|---|---|---|
| 1 | … | High | ~40% | … |

Add a short paragraph per cause in plain language, ending with "How we confirmed it" or "How to confirm it".

## 4. What we can't recover (and how we'll adapt)
For example: "Informational searches now show AI answers. Your rankings held, but fewer people click. We will…"

## 5. Action plan
| Priority | Action | Fixes | Impact | Effort | Owner | When |
|---|---|---|---|---|---|---|

## 6. How we'll measure recovery
- KPIs: non-brand clicks; impressions in the affected section; CTR at stable position; indexed pages; positions of the top 20 queries; conversions from organic.
- Check-ins: weekly for 4 weeks, then monthly. Re-run this diagnosis after the next core update.

## 7. Appendix
Brand vs non-brand, sections, top losing queries and pages, devices and countries, method notes.



---

## REFERENCE diagnosis-guide

### Diagnosis Guide: Cause Signatures, Confirmation Checks, Manual Method

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



---

## REFERENCE how-to-export-gsc

### How to Export Search Console Data for a Traffic-Drop Diagnosis

The export takes about 5 minutes and needs no technical skills. You need access to the site's Google Search Console property (owner, full or restricted user).

## Export 1: the Compare export (required)
1. Open Search Console → choose the property → **Performance → Search results**.
2. Make sure **Total clicks**, **Total impressions**, **Average CTR** and **Average position** are all switched on. The export includes only the metrics you have selected.
3. Click the **Date** filter → **Compare** tab, and pick one of:
   - **"Compare last 28 days to previous period"** for a recent drop.
   - **A custom range:** 4 weeks after the drop vs 4 weeks before it. This is best if you know the date.
   - **Year over year** (the same 28 days last year), if the business is seasonal.
4. Click **Export → Download CSV**. You get a .zip containing `Queries.csv`, `Pages.csv`, `Countries.csv`, `Devices.csv` and others. **Keep the .zip as it is.**

## Export 2: the daily timeline (strongly recommended)
1. Change the Date filter to **Filter → Last 16 months** (not Compare).
2. **Export → Download CSV**. From this .zip you only need `Dates.csv`.

## Optional: an events file
Create a simple CSV called `events.csv` with these columns:
```
name,type,start,end
March 2025 core update,core,2025-03-13,2025-03-27
Site redesign launch,deploy,2025-04-02,2025-04-02
```
- Use type `core`, `spam` or `algorithm` for Google updates.
- Use type `deploy`, `migration`, `redesign` or `content` for your own changes.
- Start from `google-updates.csv` in this folder. Check the **Google Search Status Dashboard** for updates newer than the file, and add them.

## Good to know
- Search Console hides rare ("anonymized") queries, so query totals are lower than page totals. The analyzer uses page totals for the headline numbers.
- The data is usually about 2 days behind.
- For very large sites, the export is capped at 1,000 rows per table. Analyze one section at a time with a **Page** filter, or use the Search Console API or bulk export.
- If you can't export, screenshots of the Performance graph (16 months) and the Queries and Pages tables (Compare mode, sorted by click difference) still allow a rough diagnosis.



---

## REFERENCE recovery-playbooks

### Recovery Playbooks by Cause

Each playbook gives the fix, then **what to expect**. Typical ranges assume the fix is complete. They are not guarantees, so say that in the report.

## Contents
- Tracking or data glitch
- Sitewide or section indexing problem
- Migration or redirect error
- Core or algorithm update
- Spam update or manual action
- AI Overviews or SERP features (CTR loss)
- Competitors or content decay
- Seasonality or demand
- Brand demand
- Intent shift

## Tracking or data glitch
- **Fix:** restore the tracking tag or Search Console verification. Make sure you're looking at the right property (domain vs URL-prefix, http vs https, www).
- **Expect:** the data is corrected going forward; the past gap can't be refilled. Annotate it in your reports.

## Sitewide or section indexing problem
- **Fix:**
  - Remove the accidental `noindex` or `X-Robots-Tag`, or the robots.txt disallow.
  - Fix canonicals that point elsewhere.
  - Restore 200 status codes, or 301 removed URLs to their equivalents.
  - Resubmit the sitemap, and request indexing for the 10–20 most important URLs.
  - Add a deploy checklist (noindex and robots.txt checks) to stop it happening again.
- **Expect:** often the fastest recovery. Important pages are usually re-indexed within days to a few weeks; long-tail pages take longer.

## Migration or redirect error
- **Fix:**
  - Map every old URL to its closest new equivalent with a single-hop 301.
  - Repair chains and loops.
  - Update internal links and canonicals to the final URLs.
  - Resubmit the sitemaps, and keep redirects for at least a year.
- **Expect:** most traffic returns over weeks to a few months once the redirects are correct. Lost link equity from URLs left at 404 needs the redirects to be added.

## Core or algorithm update
- **Fix:**
  - Don't change anything mid-rollout.
  - Afterwards, audit the top losing pages against Google's helpful-content self-assessment: original information, depth, expertise and first-hand experience, satisfying the intent, and trust signals (author, sources, about page).
  - Improve or merge thin pages; remove unhelpful scaled content.
  - Compare against the pages that gained.
- **Expect:** recovery, if it comes, often shows at the *next* core update after the improvements (months). Some sites never fully recover. Be honest about that.

## Spam update or manual action
- **Fix:**
  - **Manual action:** fix exactly what the notice says (unnatural links: remove them, or disavow what you can't remove; thin or scaled content: remove or improve it), then file a reconsideration request.
  - **Algorithmic spam:** stop the tactic and clean up.
- **Expect:** a reconsideration review takes days to weeks. With an algorithmic hit, ignored links simply stop counting, so recovery comes from new legitimate signals.

## AI Overviews or SERP features (CTR loss)
- **Fix:**
  - Rewrite titles and metas for clearer value: specifics, freshness, proof.
  - Add answer-first sections that AI can cite (that earns brand visibility even without the click).
  - Add schema that still earns rich results.
  - Add original data, tools and templates, which AI summaries can't replace.
  - Shift the content mix toward commercial, comparison and experience-led queries.
  - Track AI citations and AI referral traffic.
- **Expect:** **part of this loss is structural and won't come back.** Report it as a market change. Measure success by CTR at a stable position, AI citations, and conversions per visit.

## Competitors or content decay
- **Fix:**
  - Refresh the top 10–20 losing pages: match the current intent and format of the winners, add missing subtopics, update facts and dates, and improve the media.
  - Strengthen internal links to these pages and earn a few relevant links.
  - Consolidate pages that cannibalize each other.
- **Expect:** refreshed pages often move within weeks to 3 months. Track the target queries weekly.

## Seasonality or demand
- **Fix:** no SEO fix is needed. Re-baseline on year-over-year comparisons, and prepare seasonal content 6–8 weeks before the peak. If the market shrank, expand into adjacent topics.
- **Expect:** traffic follows the demand curve.

## Brand demand
- **Fix:** escalate to marketing. Check brand campaigns, PR, reviews and reputation, and competitor bidding on your brand. Protect your branded results (sitelinks, Business Profile, review sites).
- **Expect:** depends on brand activity, not SEO.

## Intent shift
- **Fix:** look at what the SERP rewards now (format, angle, freshness). Rebuild the page to match it, or target a related query that still matches your page.
- **Expect:** weeks to months after the rebuild. Some intent shifts reverse on their own (news-driven ones, for example).
