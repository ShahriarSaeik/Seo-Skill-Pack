# SEO + AI Search Monitoring: 7 Core Things to Track (Free Stack)

- **Updated**: 2026-10-05

## TL;DR
Seven monitoring pillars cover classic SEO plus AI search: organic traffic, keyword rankings, referring domains, technical issues, AI citations/mentions, AI search traffic, and AI bot activity. The free stack: Google Search Console (traffic truth), a free site-audit/rank-tracking tool (longer keyword and link history, AI channel analytics, bot logs), and Bing Webmaster Tools (which offers one of the few free AI citation reports — Bing powers a major assistant's search). The highest-leverage habit: a monthly 20-question prompt battery across assistants, logged over time.

## Framework / Step-by-step
1. **Organic search traffic** — Search Console → Performance → Search results → Clicks (set date range, Web filter). Highest-accuracy source; store regular exports (or connect to a free reporting tool) to keep history past the 16-month limit.
2. **Keyword rankings** — track only target keywords for priority pages. Search Console's UI and exports are capped at 1,000 rows; a rank-tracking tool adds volume, difficulty, and longer history.
3. **Referring domains** — watch link-profile growth from your dashboard; aim to build links at or above competitor pace.
4. **Technical SEO issues** — schedule recurring site crawls; work the errors list first (fix guidance is attached to each issue).
5. **AI citations and mentions** — monthly, ask the five major assistants a fixed 20-question battery spanning brand awareness, competitive positioning, product/features, and use-case recommendations (e.g., "What is [brand]?", "Best [category] for [use case]?", "[brand] vs [competitor] — pros and cons"). Save every response; the accumulated log shows whether visibility is rising, falling, or wrong. Accuracy matters: assistants confidently state outdated pricing and discontinued features.
6. **AI search traffic** — an AI-channel breakdown by assistant platform (built into some analytics tools; otherwise a regex-based channel group on referrer domains).
7. **AI bot activity** — distinguish bot types on your CDN/server logs:
   - **Training bots** (e.g., one frontier-lab trainer, one search giant's AI extension, one open-corpus crawler): read for model building, send no traffic
   - **Search/citation bots** (assistant user-agents and search bots): fetch live at question time and can drive referrals when they cite you
   Heavy bot hits on a page = a prompt to monitor manually ("how much does [brand] cost?" for a crawled pricing page).

## Actionable checklist
- [ ] Connect Search Console, a free site-audit/rank-tracking tool, and Bing Webmaster Tools (all free) as your baseline stack
- [ ] Check organic clicks and target-keyword positions monthly
- [ ] Review referring-domain growth and new technical errors on a recurring crawl schedule
- [ ] Run the 20-question battery across all five major assistants monthly; archive responses
- [ ] Verify stated facts (pricing, features, comparisons) in AI answers and correct via updated sources
- [ ] Review the AI citation/performance report in Bing Webmaster Tools (if available to you): total citations, grounding queries, cited pages
- [ ] Check AI traffic share and per-platform trend in analytics
- [ ] Identify your most AI-crawled pages; turn them into the prompt list you manually verify

## Data points & benchmarks
- Search Console limits: 1,000 rows in the UI and exports, 16-month history, daily updates — scheduled exports or a rank tracker work around both
- Grounding queries (the phrases AI used when retrieving your content) were available at the time of writing only in Bing's AI report — check whether other engines now offer this
- AI answer accuracy drift is real: wrong pricing, discontinued features, and outdated descriptions appear confidently if unchecked
- Training-bot activity on a page = models are learning from it; search-bot activity = live answers may cite it
- Free-stack gaps that need paid tooling: multi-location rank tracking, competitor keyword/backlink research, email alerts, prompt-scale citation monitoring

## Mistakes to avoid
- Monitoring classic SEO only — assistants are a growing share of "search" for your audience
- Running AI checks once and never again — visibility drifts month to month; logs beat snapshots
- Trusting AI answers to be current — verify facts about your own brand deliberately
- Confusing training-bot crawls with citation eligibility — different bots, different outcomes
- Tracking thousands of keywords while ignoring the 20 questions buyers actually ask assistants

## Key principles
- Monitoring = catching problems before they cost traffic; that goal now spans five assistants, not one engine
- The cheapest AI visibility data is asking the assistants yourself — consistently, and archived
- Bot logs tell you what AI is reading; citation reports tell you what AI is saying; you need both
- A few free tools cover most monitoring basics; paid tools mainly add scale and alerts
