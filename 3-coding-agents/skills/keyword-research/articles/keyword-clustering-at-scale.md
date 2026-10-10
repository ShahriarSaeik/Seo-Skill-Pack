# Keyword Clustering and Mapping at Scale (10k+ Keywords, Tool-Agnostic)

- **Updated**: 2026-10-05

## TL;DR
At scale, cluster by **SERP overlap**: two keywords belong on one page if Google ranks mostly the same URLs for both. Clean the list, pull the top 10 URLs per keyword, group keywords whose results share 3–4 or more URLs, name each cluster after its highest-volume keyword, and map each cluster to exactly one URL (existing or new). Then QA a sample by hand and check for cannibalization before anything ships.

## Framework / Step-by-step
1. **Clean the list.** Lowercase it, trim whitespace and remove exact duplicates. Merge plural/singular and word-order variants where the SERP is the same. Drop irrelevant terms with a negative-keyword list (competitor brands you can't target, "free", "jobs" and similar). Usually 20–40% of a raw export disappears here.
2. **Pre-bucket by modifier.** Split by intent cues before any SERP work: informational (how, what, why, guide), commercial (best, vs, review, alternatives), transactional (buy, price, near me) and branded. This cuts the comparison workload and stops cross-intent merges.
3. **Collect SERPs.** For each keyword, store the top 10 organic URLs from the same country and device. Use a keyword tool's SERP export, a SERP API or a clustering tool. Budget roughly one SERP lookup per keyword. Reuse results that are under about 30 days old.
4. **Cluster by overlap.**
   - Compare URL sets pairwise inside each bucket.
   - **Threshold:** 3 shared URLs gives loose clusters (good for broad guides); 4–5 gives tight clusters (good for product and category pages). Start at 4.
   - **Method:** pick the highest-volume unclustered keyword as the *hub*, add every keyword sharing at least the threshold of URLs with it, and repeat. "Hard" clustering (each keyword's set must overlap every other member) is stricter and better for ecommerce.
5. **Label and size.** Name each cluster after its top keyword (or the parent topic). Sum volume or traffic potential, and record the dominant content type, format and angle from the SERP.
6. **Map to URLs.** For each cluster, check whether an existing page ranks for, or is about, the hub keyword. If yes, map the cluster there and add missing subtopics. If no, create one new URL. **Rule: one cluster per URL, and one URL per cluster.**
7. **Cannibalization check.** Using Search Console, flag any query where 2+ of your URLs get impressions, and compare that against the map. Resolve by merging (301), differentiating intent, or re-pointing internal links.
8. **QA sample.** Manually review about 5% of clusters (at least 30), focusing on the largest and the most valuable. Look for mixed intent, a hub that is too broad, and orphan singletons. Adjust the threshold and re-run if more than 10% look wrong.
9. **Ship as a living map.** Store it in a spreadsheet or database with these columns: keyword, cluster, hub, volume/TP, intent, mapped URL, status (exists/new/merge), owner, priority. Re-run quarterly or after major updates, because SERPs drift.

## Actionable checklist
- [ ] Deduplicate and apply negatives before any paid SERP pulls
- [ ] Pre-bucket by intent modifier
- [ ] Use the same location, device and date window for every SERP
- [ ] Start with an overlap threshold of 4/10, then tune it
- [ ] Assign exactly one URL per cluster; log merges and redirects
- [ ] Check Search Console for queries where 2+ of your URLs get impressions
- [ ] Hand-QA 5% of clusters before briefing writers
- [ ] Prioritize clusters by (traffic potential × business potential) ÷ difficulty
- [ ] Re-cluster quarterly

## Data points & benchmarks
- In an older study, the average top-ranking page ranked for about 1,000 keywords, so a 20k list often collapses into a few hundred to a few thousand clusters.
- One clustering-tool test processed 4,703 keywords in about 51 minutes. Budget time and API credits accordingly.
- Singleton clusters (one keyword) are normal for long-tail lists. Merge them into the closest hub if intent matches; otherwise treat them as FAQ or subsection candidates rather than new pages.

## Mistakes to avoid
- Clustering by shared words (lexical) instead of shared SERPs. "Apple watch bands" and "apple watch price" share words but need different pages.
- Mixing countries or devices in one SERP pull
- Creating a page per keyword (thin, cannibalizing content)
- Skipping the existing-URL check, which creates duplicates of pages that already rank
- Treating the map as finished; intent shifts after core updates

## Key principles
- The SERP is the ground truth for "same intent".
- Cluster first, then write: content briefs come from clusters, not keywords.
- Precision beats recall on money pages (tighter threshold); recall beats precision on guides (looser threshold).
- A cluster map is only useful if it's enforced through internal links and briefs.
