# Automating Data-Driven Content Refreshes with an AI Agent

- **Updated**: 2026-10-05

## TL;DR
Data-driven posts are only worth reading if the numbers are current, but manually refreshing 14–20 of them monthly was a full-afternoon slog — so updates slipped to quarterly or never. One content team built an AI agent that pulls, cleans, and formats every dataset monthly and files CMS drafts for review. It reportedly saves 20+ hours/month, and updates now happen on time.

## Framework / Step-by-step
1. **Find the automation candidate.** For each recurring task ask: does it run on a schedule, and can you write down the rules for "done right"? If both are yes, automate it. "Pull the same numbers and reformat them" passes; "write the article" fails — keep that.
2. **Automate the plumbing, not the thinking.** Fetching, cleaning, formatting, pasting into the CMS, date edits — hand all of it off. Judgment stays human.
3. **Make the cleaning visible.** Don't accept a finished list; have the agent show what it removed and why, next to what it kept.
4. **Add a model-powered cleaning layer with human review.** Raw "top questions" lists contain movie titles, non-questions, brand queries, bot-like queries. An LLM pass filters at scale (e.g., screening 5,000 candidates for real person names), but a person checks every refresh.
5. **Never let it publish.** The agent creates drafts and emails a summary; a human reviews and hits publish. An agent that does 90% and leaves the last 10% is the goal — 100% automation that occasionally publishes nonsense is a fire to put out.
6. **Lock what the model shouldn't touch.** Pin headline stats, verified figures, and the opening line so the agent can't quietly reword a number into falsehood.

## Actionable checklist
- [ ] List recurring content chores; mark the ones that are scheduled + rule-based
- [ ] Map each dataset to its source, update method, and cleaning rules
- [ ] Require a "kept vs. removed + why" view for every refresh
- [ ] Keep verify-and-publish as a manual human step
- [ ] Protect key figures from model rewording
- [ ] When it works, share it internally — useful automations spread on their own (in the original team, several writers adopted versions of it)

## Data points & benchmarks
- 14 datasets refreshed monthly by the agent; ≥20 hours saved per month
- Cadence improved from quarterly (or never) to monthly — and more data posts became feasible to publish
- In the team's own data, search traffic rose after data-post updates (correlation; freshness helps most where the query expects current numbers)
- Screening example: the "most searched people" table requires judging up to 5,000 candidates per refresh
- An analyst forecast (2025) expects 40%+ of agentic AI projects to be scrapped by 2027 — this kind survives because it's boring and well-defined

## Mistakes to avoid
- Assuming "top questions" = sort by volume: raw lists are full of movie titles ("how to train your dragon"), non-questions ("would you rather questions"), and brand queries
- Measuring brand-search growth for brands whose names are common words without baseline subtraction — estimate pre-existing search volume, subtract it, count only brand-driven growth
- Trusting one-month spikes as growth; confirm the company itself ranks for its name (a software brand can drown under an unrelated brand with the same name)
- Building in silence — sharing the win internally multiplied its impact

## Key principles
- Data content earns compounding traffic only if kept fresh; decay is the default
- The best first automation is tedious, rule-based, and scheduled — not creative
- Agents enforce the rules; humans decide what the rules should be
- Everyone becomes a manager of agents: be the editor who confirms it works and pushes live
