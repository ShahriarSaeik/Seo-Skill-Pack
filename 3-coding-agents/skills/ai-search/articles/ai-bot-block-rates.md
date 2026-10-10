# AI Bot Block Rates: Which Crawlers ~140M Websites Block

- **Updated**: 2026-10-05

## TL;DR
A robots.txt study of ~140 million websites (461M robots.txt files; data runs to about Dec 2024, so rates have likely shifted since) found roughly 5.5–6% of sites block each major AI bot — with one training crawler leading at 5.89% (~8.2M sites) — and explicit, targeted blocks are rarer (~0.5%). Block rates track crawl aggressiveness (correlation 0.512), one assistant's training crawler saw the fastest block growth (+32.67% YoY), and arts & entertainment (45%) plus law & government (42%) block the most. Root cause: bots consume resources while AI platforms send just ~0.1% of referral traffic — a broken social contract.

## Framework / Step-by-step
1. **Count blocks, not sentiment** — measure robots.txt directives across sites: explicit disallows (bot named and blocked), general blocks (all bots disallowed), and allow-after-block exceptions. Firewall/IP blocks are invisible to this method (real block rates are higher).
2. **Correlate with crawl volume** — bots that make more requests get blocked more (statistically significant, r=0.512): block pressure is a function of resource cost.
3. **Segment by site category** — blocking intent differs by industry (ethics, copyright, legal, revenue fears, price-scraping prevention).
4. **Track block-rate growth over time** — new entrants double the bot population (10 → 21 major AI bots in ~16 months), so aggregate crawl cost keeps rising.
5. **As a site owner, decide your stance per bot type** — training crawlers (no traffic back) vs search/citation crawlers (can send visitors).

## Actionable checklist
- [ ] Audit robots.txt: list every AI bot you block or allow, deliberately, by name
- [ ] Distinguish training crawlers (take content, send nothing) from retrieval crawlers (can cite you and send traffic)
- [ ] If you block, use explicit per-bot disallows — inheritable "block all" rules can accidentally exclude citation crawlers
- [ ] Re-check quarterly — new AI bots launch constantly and defaults change
- [ ] Watch whether your platforms of choice start reporting impressions/clicks; reward the ones that do with crawler access
- [ ] As a publisher with cost concerns, weigh bot resource load against citation-driven traffic before blanket blocking

## Data points & benchmarks
- Most-blocked AI bots (share of ~140M sites): training crawler #1 5.89%, open corpus crawler 5.85%, one commerce giant's bot 5.78%, one short-video platform's scraper 5.74%, one assistant's training bot 5.74%, one search giant's AI-extension 5.71%
- Counting all 461M robots.txt files (incl. subdomains), the top-blocked bot's rate rises to 7.3%
- Explicit targeted blocks: leader 0.5% (~694K sites), open corpus crawler 0.49%, then a steep drop
- Fastest block-rate growth YoY: one assistant's training bot +32.67%, its sibling +25.14%, its fetch bot +20.66%, the short-video scraper +19.57%
- Crawl volume ↔ block rate: Pearson 0.512, p=0.0149 (significant at 5%)
- Most-blocking categories: arts & entertainment 45%, law & government 42% — news blocked less than expected
- AI bot count doubled from 10 (Aug 2023) to 21 (Dec 2024)
- Context (older study): AI platforms sent ~0.1% of referral traffic while search sent ~44% — the value exchange driving blocks

## Mistakes to avoid
- Blanket-blocking all bots and silently losing citation eligibility on AI surfaces
- Assuming robots.txt is the only lever or an enforcement mechanism — it is a request that compliant bots honor; firewalls and IP blocks sit outside your robots file
- Copying big publishers' blocks without their reasons (copyright litigation, scraping economics may not apply)
- Forgetting that allowed-but-ignored training crawlers still cost bandwidth with zero traffic return
- Ignoring reports of some AI bots disregarding robots.txt entirely — verify with server logs

## Key principles
- There is a social contract between crawlers and sites: traffic for content; in that study AI platforms underpaid by hundreds of times versus search
- The most active bots are the most blocked — crawl aggressively, get excluded
- The first AI platform to show site owners impressions and clicks will likely win crawler access and adoption
- If platforms keep traffic in walled gardens, expect more blocks, paid data access, or broken standards
- Blocking is an industry decision with a rationale, not pure technophobia — read the category patterns
