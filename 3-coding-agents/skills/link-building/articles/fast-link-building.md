# How to Start a Link Building Campaign Fast (and Systematize Everything)

- **Updated**: 2026-10-05

## TL;DR
Outreach has three tasks — find prospects, find contact info, send emails — and the bottlenecks are the first two. Skip Google prospecting; mine a content database with boolean filters, automate contact discovery (author name → bulk email finder → verifier), and load merge-field templates into an outreach tool. Result: a campaign live in ~30 minutes, systematized with docs + kanban handoffs.

## Framework / Step-by-step
1. **Find prospects (fast).** In a content research database (a large pre-built web index, so no scraping is needed), run an in-title search: `(how OR why) AND ([keyword 1] OR [keyword 2])` — e.g., how/why + muscle/gym for a supplements site. Why topic-search beats "write for us" lists: many sites publish contributor content without advertising it, topical fit is proven, and you get post URL + author name for free. Keep any guest post editorial and genuinely useful — no paid placements, no mass-produced posts, and tag anything sponsored with rel="sponsored" or nofollow.
   - Filters: your language, live pages only, authority roughly 20-95 on the tool's scale (skip junk and untouchable mega-sites), one page per domain
   - Result example: 2,685 prospects in ~2 minutes; export to a cloud spreadsheet (batch exports by authority range if the tool caps exports)
2. **Find contact info (automated).**
   - Keep only rows with author names; split first/last names with spreadsheet formulas
   - Bulk-run an email-finder tool (name + domain → email; many offer a small free tier; misses = likely guest bloggers, skip)
   - Bulk-verify found emails with a verification service (typically a few dollars per 1,000, often with free trial credits); merge valid ones back with lookups
3. **Send emails.** Import into an outreach tool; one template with merge fields. Still personalize — automation is for the boring parts: ~5 min/email = 12 emails/hour; even at an 8% conversion that's ~1 link/hour.

**Systematize:** turn the process into a system — a kanban board with one list per stage, one shared doc per step, and the "assign the next step" instruction written INTO each doc so the chain runs without a manager.
**Automate:** wire the steps together with an automation platform to remove moving parts.
**Scale:** this fast pass keeps only ~10% of prospects (names/emails not found). That's fine — it's a viability test. No legs? Kill it. Legs? Add a doc for manual name/email hunting, run more campaigns, or port the process to other tactics (broken link building etc.). For exports lacking author names, run page URLs through a URL-profiling tool to scrape authors (and optionally pull authority metrics), then merge back.

## Actionable checklist
- [ ] Write the boolean in-title query for your niche
- [ ] Apply language/live/authority range/one-page-per-domain filters; export
- [ ] Filter to author-named rows; split names with formulas
- [ ] Bulk email-finder pass; bulk verification pass; merge valid emails
- [ ] Load into outreach tool with merge-field template
- [ ] Personalize each send (5 min max) — no zero-touch blasts
- [ ] Build the kanban + docs system with self-service handoffs
- [ ] After 50-100 sends: keep-or-kill decision; if keep, add manual-prospecting doc

## Data points & benchmarks
- 2,685 prospects in ~2 minutes from a single boolean search
- Email pipeline yields roughly 10% of raw prospects fully ready to pitch
- ~5 minutes of personalization per email → 12/hour → ~1 link/hour at an 8% conversion
- Verification cost: typically a few dollars per 1,000 emails (varies by provider); first pitches possible within ~30 minutes total

## Mistakes to avoid
- Prospecting via Google when speed matters (extraction + metric checks are the real time sink)
- Targeting only "write for us" pages — many open sites never declare it
- Contacting dead pages or duplicate domains
- Using automation as an excuse to skip personalization
- Perfecting the prospect list before testing whether the campaign converts at all

## Key principles
- Bottleneck math: prospecting + contacts consume the hours; sending is trivial
- Boolean topic-mining gives you prospects AND their authors in one query
- Automate name→email→verify; humans only handle exceptions and personalization
- First campaign is a hypothesis test — optimize for speed-to-signal, not completeness
- Processes are steps; systems are steps that hand themselves off
