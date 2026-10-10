# "Indexed, though blocked by robots.txt" Can Be More Than A Robots.txt Block

- **Updated**: 2026-10-05

## TL;DR
This Search Console status means URLs you blocked from crawling are still indexed — because crawling and indexing are separate processes, and a robots.txt-blocked page can still be indexed from links. The block itself may live in robots.txt, or hide deeper: intermittent blocks, user-agent blocks, or IP blocks. First decide whether you even want the URL indexed; that decides the fix.

## Framework / Step-by-step
**Decision 1 — You DON'T want it indexed:**
- Add a noindex meta robots tag AND allow crawling (a crawler must see the tag to obey it).
- If the URL canonicalizes elsewhere, don't noindex — just set proper canonical signals and allow crawling so signals consolidate.

**Decision 2 — You DO want it indexed (find and remove the block), in this order:**
1. **robots.txt crawl block** — use the robots.txt report (Search Console → Settings) to find the offending Disallow (watch for `Disallow: /` sitewide blocks, common on new sites and post-migration; check CMS "search engine visibility" settings that write this line). Fix by deleting the rule (CMS setting, plugin file editor, FTP/hosting file manager).
2. **Intermittent blocks** — check robots.txt version history (the robots.txt report's fetch history, deploy history, web archives). Classic cause: a shared cache between staging and production alternately serving a blocking robots.txt — split the cache or exclude .txt files from it.
3. **User-agent blocks** — site detects and blocks specific bots (via .htaccess, server config, firewall, CDN, or hosting). Test by spoofing the user agent (browser devtools, an extension, or `curl -A "user-agent" -Lv URL`); if blocked only as the bot, hunt the rule or ask the host/CDN where it lives.
4. **IP blocks** — bot IPs denied at server/firewall level (e.g., `deny from x.x.x.x`). Hardest to self-diagnose; escalate to hosting/CDN.

## Actionable checklist
- [ ] For each flagged URL, decide: want indexed or not
- [ ] Not wanted: noindex meta + crawl allowed; canonicalized duplicates: canonicals + crawl allowed
- [ ] Wanted: check the robots.txt report (Search Console → Settings) and URL Inspection; remove the Disallow
- [ ] Check CMS visibility settings ("discourage search engines" style toggles) after launches/migrations
- [ ] Review robots.txt history for intermittent blocks; split staging/production caches
- [ ] Curl with the bot's user agent to detect UA-specific blocks
- [ ] Escalate unexplained blocks to hosting/CDN (firewall/IP rules)
- [ ] Re-validate the fix in Search Console after recrawl

## Data points & benchmarks
- Crawling ≠ indexing: blocked pages stay indexable via links — blocking crawl never guarantees deindexing.
- Whole-site `User-agent: * / Disallow: /` blocks most often appear on brand-new sites or right after migrations.
- Recurring "fixed then broken" status = intermittent block until proven otherwise.

## Mistakes to avoid
- Expecting robots.txt to deindex pages — it can't; it only hides the noindex tag.
- Pairing noindex with a robots.txt block (crawler never sees the noindex).
- Noindexing URLs that canonicalize elsewhere — conflicting instructions.
- Checking only the live robots.txt and missing historical/intermittent versions.

## Key principles
- If a page shouldn't rank: noindex + crawl allowed. If it should: remove every layer of block (file, UA, IP).
- Blocks can exist in at least four places: robots.txt, cache layers, UA rules, IP rules.
- Test as the bot, not as a human browser.
