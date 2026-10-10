---
name: seo-router
description: Start here for any SEO or AI-search task. Routes the request to the right specialist SEO skill (fundamentals, keyword research, on-page, technical, link building, content marketing, local, enterprise, AI search), adapts the answer to beginner, intermediate or advanced users, and runs multi-step workflows such as a full SEO plan for a new site, a site audit, a traffic-drop diagnosis, a blog post from keyword to publish, or an AI visibility plan. Use whenever the user mentions SEO, Google rankings, organic traffic, keywords, backlinks, AI Overviews or ChatGPT visibility, or wants more search traffic, even if they don't name a specific skill.
metadata:
  version: "2.0"
  levels: beginner, intermediate, advanced
  agent-compatibility: any agent that reads markdown (Claude, ChatGPT, Gemini, Copilot, Cursor, Codex, and others)
---

# SEO Router: start here

This skill is the entry point to an SEO playbook library of 11 skills and 514 playbooks. It decides **which skill to open**, **how deep to go** for this user, and **what order to run things in** when a task spans several areas.

## Step 0: Use the user's language
If the user writes in Bangla or Banglish (Bangla in English letters), reply in Bangla at the user's level: simple, everyday Bangla for beginners; clear professional Bangla for intermediate and expert users. Keep SEO terms in English, and explain each term in Bangla the first time it appears (for example: "impressions (Google-এ আপনার সাইট কতবার দেখানো হয়েছে)"). The same rule applies to any other language.

**Non-English markets (for example Bangladesh):** research keywords in the local script, in English, and in transliteration (শাড়ি / saree / sharee), because people search all three ways. Check which form gets more results with autocomplete. Local platforms such as Facebook pages and marketplaces complement SEO but don't replace the website.

**Beginners:** playbooks often include developer-level items (faceted navigation, canonicals, logs). For a beginner, pick only the 3–5 steps they can do themselves this week, and mention that a developer can handle the technical items later.

## Step 1: Gauge the user's level
Infer the level from the user's wording. Ask one question only if the level is unclear and it would change the answer.

| Signal | Level | How to respond |
|---|---|---|
| "What is SEO?", "how do I get on Google", no jargon, small site or first site | **Beginner** | Plain language and analogies. Define every term using [GLOSSARY.md](GLOSSARY.md). Give 3–5 prioritized steps that can be done this week with free tools. No more than 2 statistics. |
| Uses terms like KD, intent, canonical or GBP correctly; has Search Console; wants a process | **Intermediate** | A step-by-step framework with a checklist and benchmarks. Name the type of tool for each step. |
| Talks about crawl budget, log files, fan-out, forecasting, stakeholders, or thousands of URLs | **Advanced** | Full framework, edge cases, data points with caveats, prioritization by impact and effort, and how to measure results. Skip the basics. |

## Step 2: Route to a specialist skill
| The user wants to… | Open skill |
|---|---|
| Understand SEO, get a strategy, run an SEO audit, analyze competitors, understand algorithm updates or penalties, or get an industry playbook (SaaS, ecommerce, B2B, healthcare, finance) | `seo-fundamentals` |
| Find keywords or topics, judge difficulty or volume, map or cluster keywords | `keyword-research` |
| Optimize one page: titles, metas, headings, URLs, images, FAQ, CTR | `on-page-seo` |
| Grow an **online shop** (ecommerce: category and product pages) | `seo-fundamentals` (`ecommerce-seo`) + `keyword-research` + `on-page-seo` |
| Add **schema / structured data (JSON-LD)** to a page | `seo-fundamentals` (`schema-markup`, ready JSON-LD examples) |
| SEO for a **SaaS** or a brand-new product site (incl. first backlinks) | `seo-fundamentals` (`saas-seo`) + `link-building` (`how-to-get-backlinks`) |
| **No traffic at all** after 2+ months | `technical-seo` (`why-is-my-website-not-showing-up-on-google`) first: confirm indexing with `site:` and Search Console, then `keyword-research` |
| Fix indexing, crawling, speed, redirects, canonicals, JavaScript, migrations (large moves: `large-site-migration-playbook`), international sites | `technical-seo` |
| Get backlinks, do outreach or digital PR, audit or clean up links | `link-building` |
| Plan, write, refresh, promote or measure content; build a topical map | `content-marketing` |
| Rank in Google Maps or the local pack, set up GBP, citations, reviews, location pages | `local-seo` |
| Run SEO for a large site, team or agency: forecasting, reporting, OKRs, buy-in, mergers | `enterprise-seo` |
| Get cited or mentioned by ChatGPT, Perplexity, Gemini or AI Overviews, or track AI traffic | `ai-search` |
| **Traffic or rankings dropped** (any level, any wording, e.g. "ট্রাফিক কমে গেছে", "traffic drop", "rankings fell") | `traffic-drop-doctor` first (it asks for Search Console data, or works without it); if it isn't installed, workflow C below |

Article names in backticks below (like `seo-audit`) are files in that skill's `articles/` folder. Each specialist skill has its own *Learning path* (Beginner, Intermediate, Advanced) and a *Quick playbooks* table. Open that skill's `SKILL.md`, choose the 1–3 relevant articles, and apply them.

> If your agent can't load other skills automatically, open the folder with that name, read its `SKILL.md`, and follow it.

## Step 3: Multi-skill workflows
Use these when a request spans several areas. Run the steps in order and skip any the user has already done.

### A. SEO plan for a new or small website (Beginner–Intermediate)
0. **Check for a local angle first.** Do customers visit a physical location, or does the business serve a specific area (a bakery, plumber or clinic)? If so, run `local-seo` first (Google Business Profile, reviews, citations), because it usually brings results fastest. If you can't tell, ask one question. Online-only shops skip this step.
1. `technical-seo`: confirm the site can be indexed (Search Console set up, sitemap submitted, no `noindex`, HTTPS, mobile-friendly).
2. `keyword-research`: find 20–50 low-difficulty, long-tail keywords with business potential, grouped by intent.
3. `content-marketing`: turn them into a topical map and a 90-day content calendar.
4. `on-page-seo`: apply the on-page checklist to every page you publish.
5. `link-building`: start 2 easy tactics (for example unlinked mentions and resource pages).
6. `seo-fundamentals` (`how-long-does-seo-take`, `seo-metrics`): set expectations. Most sites see first results in 3–6 months; new domains and competitive niches take 6–12+ months. Choose the metrics to track monthly.

### B. Full SEO audit (Intermediate–Advanced)
Start from `seo-fundamentals/seo-audit` and `technical-seo/technical-seo-audit`. Run checks in this order, because each layer depends on the one before it: **technical** (crawl and index) → **on-page** (intent, titles, internal links) → **content** (decay, gaps, pruning, E-E-A-T) → **links** (profile versus competitors) → **AI visibility**. Output one prioritized issue list with columns: issue, affected URLs, impact (High/Med/Low), effort, owner, fix.

### C. Traffic or ranking drop diagnosis
If the `traffic-drop-doctor` skill is installed, use it. It runs this whole workflow on the user's Search Console export and writes the report. Otherwise:
1. `seo-fundamentals`: open `analyze-sudden-traffic-drop` and `google-ranking-dropped-dramatically`. Check tracking errors, seasonality, algorithm update dates, manual actions (`google-penalties`) and SERP changes.
2. If it affects many pages: `technical-seo` (`technical-seo-audit`, `crawled-currently-not-indexed`, `website-migration`).
3. If it affects specific pages: `content-marketing` (`content-decay`, `automating-content-refresh`) and `on-page-seo` (`search-intent`, `title-tag-seo`).
4. If clicks dropped but rankings held: this is a CTR problem, not a ranking problem. Use `seo-fundamentals` (`zero-click-search`, `organic-ctr-benchmarks`) and `ai-search` (`ai-overviews-reduce-clicks-update`, `how-to-rank-in-ai-overviews`). Segment queries by whether an AI Overview or SERP feature appeared, and compare CTR at constant position.

### D. One SEO blog post, from keyword to publish
`keyword-research` (pick keyword, check intent and parent topic) → `content-marketing` (brief, outline, draft, information gain) → `on-page-seo` (title, meta, slug, headings, images, FAQ, internal links) → `ai-search` (BLUF answers, self-contained sections, schema) → `link-building` (promotion and outreach).

### E. AI visibility plan
`ai-search` (baseline with `manual-ai-visibility-audit` or `ai-visibility-audit`) → `content-marketing` and `on-page-seo` (answer-first, chunked content) → `link-building` (third-party mentions, digital PR, Reddit and forums) → `ai-search` (track AI referral traffic monthly).

### F. Local business
`local-seo` (GBP, citations, reviews, location pages) → `on-page-seo` (service pages) → `link-building` (local links) → `content-marketing` (local content).

### G. Large site or stakeholder work
`enterprise-seo` (`seo-forecasting-model`, `enterprise-seo-metrics-reporting`, `seo-okrs`) plus `technical-seo` for scale issues (crawl budget, faceted navigation, logs, migrations).

## Step 4: Deliver
Every answer should end with something the user can act on:
- **Action plan**: a table of action, why, impact, effort and when, sorted by impact.
- **Checklist**: copied and tailored from the playbook's checklist.
- **Draft**: titles, metas, outline, outreach email or schema JSON-LD.
- **Diagnosis**: likely causes ranked by probability, how to confirm each one, and the fix.

## Guardrails
- Health, beauty/skincare, finance and legal (YMYL) topics: no medical, financial or legal claims the business can't prove; recommend expert review and E-E-A-T signals.
- Don't guarantee rankings, traffic or timelines. Give ranges and the conditions behind them.
- Playbooks are tool-agnostic. Map "a keyword research tool" and similar phrases to the user's own tools, or to the free options in [GLOSSARY.md](GLOSSARY.md).
- Statistics are dated (library compiled in 2026). Attribute them as "one study found…" and verify anything critical if you can browse. Never make up numbers.
- Recommend white-hat methods. If asked about buying links, PBNs, cloaking, scaled AI spam or parasite SEO, explain the risk using the relevant playbook. Don't give step-by-step instructions for abusing search engines.
