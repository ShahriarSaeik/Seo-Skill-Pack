# Recovery Playbooks by Cause

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
