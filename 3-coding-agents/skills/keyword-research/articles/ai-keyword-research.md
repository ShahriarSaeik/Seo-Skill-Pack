# AI Keyword Research: How It Works and 9 Prompts to Start

- **Updated**: 2026-10-05

## TL;DR
AI without a live keyword database fabricates volumes/KD — connect it to real SEO data (CSV exports, an API, or a tool connector such as MCP) and it becomes a fast research analyst: ideation, clustering, gap analysis, decay detection. Use the 9 ready-made prompts; keep strategy and editorial judgment human.

## Framework / Step-by-step
**Three tool setups:** (1) plain AI assistants (ideation + spreadsheet ops on your CSV exports, no live data), (2) AI-powered SEO tools (the built-in AI of a keyword research tool), (3) AI + MCP — the model queries live keyword data mid-conversation through a connector. Agentic AI plans multi-step workflows, asks questions, completes whole tasks.

**AI does well:** 50+ seed variations in minutes; deduping multi-source lists; scoring business fit 0–3; semantic clustering; outlier/growth detection across 500-row sheets.
**AI gets wrong without data:** any volume, KD, SERP feature, or trend figure — all fabricated from training data.
**AI can't do even with data:** set strategy, define "relevant," judge effort vs. reward, decide what NOT to do. "Treat AI as a fast research analyst, not a SEO/content director."

**The 9 prompts (paraphrased — use with exported data or a live data connection):**
1. **Seed expansion + clustering** — site + audience context, 30+ keywords with KD<30 and traffic potential (TP, estimated total search traffic a topic can bring to a page) >100, grouped by parent topic (one cluster = one article), each with title + intent + top keyword, prioritized by TP.
2. **Competitor keyword gaps** — competitors rank top 20, you don't rank at all; KD<40, TP>200; cluster and rank.
3. **Low-hanging fruit** — you rank positions 4–20, exclude brand; rank by traffic gain from reaching top 3; pick top 100 optimization targets.
4. **Traffic decay** — compare top pages' traffic now vs 6 months ago; for top 10 decliners show current/previous traffic + top keyword; flag refresh priorities.
5. **Untargeted branded keywords** — [Brand + X] queries landing on generic pages (homepage/category) instead of dedicated ones; mark where others outrank you.
6. **Question + comparison keywords** — "how to/what is" and "vs/alternative" formats; KD<35, volume>100; suggest content format per cluster (formats that commonly appear in AI answers).
7. **International opportunities** — rank countries by (competitor traffic − your traffic); gap keywords where ≥2 competitors rank top 20 and you're not top 50; check English keyword + native-language translation; classify open/contested/defending/owned.
8. **Trending keywords** — consistent volume growth over 6–12 months, not yet peaked; current volume, 6-month-ago volume, KD, whether you rank.
9. **Buyer persona keywords** — brainstorm 30 keywords from persona description (problem-awareness, solution-comparison, AI-chatbot-style queries); validate volume; flag zero-volume separately.

**Skills & pipelines:** save winning prompts as reusable skill files (plain markdown); chain them: `/keyword-audit → /cluster → /content-brief`. AI can build skills from a description, a conversation, or even a blog post.

**Prompting rules:** set site context first; assign a role ("SEO analyst for B2B SaaS"); name the data source ("the keyword database, not the backlink index"); use negative prompts ("exclude branded, KD>40"); show an example output row; ask AI to justify its top 5; iterate within the conversation; save winning setups to memory.

## Actionable checklist
- [ ] Connect AI to a keyword database (MCP/API) or upload CSV exports — never trust raw LLM metrics
- [ ] Run prompts 1–3 for a baseline: clusters, gaps, quick wins
- [ ] Run prompts 4–5 monthly: refresh decaying pages, claim branded queries
- [ ] Run prompts 6, 8 quarterly for new formats and rising trends
- [ ] Build your own skill pipeline from the prompts that repeatedly work
- [ ] Human decides final cut: strategy, relevance, effort vs reward, what to skip

## Data points & benchmarks
- Common filter defaults in prompts: KD <30–40, traffic potential >100–200, positions 4–20 for quick wins
- A saved content-gap skill can turn a handful of onboarding questions into a gap and quick-win list in minutes (speed varies by setup and data size)
- Question/comparison keywords = formats that commonly appear in AI answers

## Mistakes to avoid
- Asking a raw chatbot for volumes/KD — it will fabricate plausible-looking numbers
- Letting AI judge strategic fit — it can find winnable keywords, not worth-winning ones
- Vague data-source instructions — a top cause of confidently wrong AI output
- Rewriting prompts from scratch each time instead of iterating/saving skills

## Key principles
- "AI changes who does the mechanical parts" — a full day of research becomes a morning.
- Combined workflow (AI + keyword database) beats either alone.
- Negative prompts are half the value.
- The hardest keyword decision — cutting 180 of 200 suggestions — stays human.
