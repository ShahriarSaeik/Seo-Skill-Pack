# What Is llms.txt, and Should You Care?

- **Updated**: 2026-10-05

## TL;DR
llms.txt is a proposed standard: a Markdown file at your site root that maps LLMs to your highest-value content (docs, policies, product catalogs). It sounds like robots.txt for AI, but, as of this writing, no major AI provider has committed to reading it — and one study of 137K domains found 97% of published llms.txt files received zero requests. Low effort, near-zero proven benefit; prioritize actual AI visibility work instead.

## Framework / Step-by-step
1. **What it is** — a Markdown file (H2 sections linking to key resources) meant to curate the "good stuff" for language models: API docs, quickstarts, terms, returns, product catalogs, sizing guides.
2. **What it is NOT** — an enforced protocol. AI crawlers honor robots.txt (that file genuinely controls AI bot access); none of the major providers has officially adopted llms.txt for crawling or retrieval. Google's guidance says no special AI-specific files are needed to appear in its AI features, and its search representatives have compared llms.txt to the old keywords meta tag: a site's self-description nobody asked to read.
3. **If you still want one** (cheap optionality):
   - Start from a Markdown file; group resources by type under H2s
   - Link to structured, Markdown-friendly content
   - Host at the site root (/llms.txt)
   - Keep it updated; skip speculative metadata (token budgets etc.) — no evidence any crawler respects it
4. **Where actual AI visibility comes from** — check server logs/bot analytics to see which AI crawlers actually hit your site; track AI referral traffic and brand mentions in AI answers; invest in content freshness, citations, and third-party mentions instead.

## Actionable checklist
- [ ] Verify robots.txt correctly allows/blocks the AI crawlers you care about (this is enforced; llms.txt is not)
- [ ] Check server logs or bot analytics for actual AI-bot requests before investing further
- [ ] If publishing llms.txt: keep it to genuinely valuable structured docs, keep it current
- [ ] Don't put anything in it you wouldn't hand a competitor — a curated content map eases scraping
- [ ] Track real AI visibility metrics: mentions, citations, AI referral traffic — not file presence

## Data points & benchmarks
- One study of 137,000 domains: 28% publish an llms.txt — adoption driven purely by speculation.
- Of ~38,000 domains with a valid llms.txt, 97% received zero requests for it in a measured month — no bots, no humans.
- Adoption is concentrated among tech-savvy sites (analytics users); general-web adoption is lower.
- Even the vendors whose own docs publish llms.txt files don't state their crawlers use the standard.

## Mistakes to avoid
- Treating llms.txt as a ranking or citation lever — no provider parses it.
- Spending budget on generators and audits for an unread file.
- Exposing a tidy map of your best content to scrapers without weighing the risk.
- Neglecting robots.txt AI-crawler rules (which DO work) in favor of a decorative file.

## Key principles
- A standard without adopters is a suggestion; llms.txt is currently a solution in search of a problem.
- AI models largely reuse existing crawl infrastructure (robots.txt, sitemaps, plain good content).
- People latch onto files like this because they lack control over AI visibility — real control comes from measurable mentions, citations, and crawler access data.
- Cheap to add, harmless to keep, but never a substitute for AI visibility tracking.
