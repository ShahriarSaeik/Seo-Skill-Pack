# Anchor Text: A Data-Driven Guide

- **Updated**: 2026-10-05

## TL;DR
Anchor text tells search engines what the linked page is about — it's been a ranking input since the original search algorithm papers. But one study of 384,614 pages (top 20 results for 19,840 keywords, isolated for page-level link authority) found only weak correlations between keyword-rich anchor percentages and rankings. Don't engineer anchor ratios; keep them natural.

## Framework / Step-by-step
1. **Know the anchor types** — exact match (the keyword), phrase match (contains the keyword), partial match (all words, wrong order), branded, naked URL, random/generic ("click here"), and image links (alt text acts as the anchor).
2. **Understand the history** — early search weighted anchors so heavily that "Google bombing" (mass-linking a page with an unrelated exact anchor) worked. The Penguin update (2012) targeted over-optimized exact-match anchors; sites tanked overnight (Penguin has been part of the core algorithm since 2016, but manipulative links can still draw a manual action). Conventional advice since: keep exact-match to ~1-5% of anchors.
3. **What the data actually shows** (two studies):
   - Exact-match anchor % vs. rank: Spearman ~0.14 (weak positive)
   - Phrase-match: ~0.11 (very weak)
   - Partial-match: ~0.11 (very weak)
   - Random anchors: ~0.02 (none)
   - Keyword in surrounding link text (per a 2004 "reference contexts" patent, engines can read text around the link): ~0.02-0.06 (none)
   - Median exact-match anchor share is zero at every ranking position — most ranking pages have no exact-match backlinks at all.
4. **Why even these weak numbers overstate it** — pages rank for hundreds of keywords (top-10 pages rank for 400-1,300 queries on average), so "the target keyword" is largely a fiction at scale; the study can't isolate the true intended keyword per page. Correlation also isn't causation: the same links that carry anchors carry authority.
5. **What to do instead** — don't manipulate anchor ratios at all. Natural profiles are diverse by default; you rarely control anchors in legitimate link building anyway (guest-post author bios are the exception — use branded anchors there).

## Actionable checklist
- [ ] Audit your backlink anchors: flag exact-match concentration on any single page
- [ ] If a page's exact-match anchor share is abnormally high vs. its natural profile, review those links for low-quality or manipulative sources and remove or disavow only those — don't try to "dilute" ratios
- [ ] Use descriptive anchors for internal links (you control those fully)
- [ ] Keep image-link alt text descriptive — it IS the anchor
- [ ] When guest posting, default to branded anchors in bios
- [ ] Never copy competitors' anchor ratios; you can't know their true target keywords

## Data points & benchmarks
- 384,614 pages studied; exact-match Spearman 0.14; phrase/partial ~0.11; random ~0.02; surrounding-text ~0.
- Penguin's first rollout (2012) affected ~3.1% of queries; exact-match-heavy sites lost rankings overnight.
- Only ~22% of a typical blog post's traffic comes from its main target keyword (one study; one example page: 17%), so single-keyword anchor engineering optimizes a rounding error.
- Top-10 pages rank for 400-1,300 other queries on average (3M-query study).

## Mistakes to avoid
- Building exact-match anchors via low-quality networks — the Penguin-era risk still applies.
- Reverse-engineering top rankers' anchor ratios and copying them (unknown true targets, survivorship bias).
- Optimizing one keyword when pages win whole topics.
- Forgetting that averages lie: medians of exact-match share are zero at every position.

## Key principles
- Anchor text provides context; it is not a lever to pull.
- A natural anchor profile is diverse — because you don't control legitimate links.
- Topics beat keywords: one exact anchor can only ever target one keyword, and pages rank for hundreds.
- If you must influence anchors anywhere, spend the effort on internal links and image alt text, where control is legitimate.
