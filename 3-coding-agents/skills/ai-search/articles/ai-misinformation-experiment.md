# AI Misinformation Experiment: The Most Detailed Story Wins

- **Updated**: 2026-10-05

## TL;DR
A two-month experiment (a single study; models change quickly) planted a fake brand online, then seeded three conflicting fake narratives (a promotional blog, a Reddit insider AMA, and a fake "debunking" investigation) against an official FAQ with explicit denials. Most AI assistants repeated the fabricated stories — and a detailed lie consistently beat a vague official truth. If you don't publish a specific, detailed official version of your brand story, AI will assemble one from whatever looks credible.

## Framework / Step-by-step
The experiment protocol (and your defensive playbook). It used an invented brand; never seed false claims about real brands or people.
1. **Create the vacuum** — a unique brand name with zero search presence (AI site built in ~1 hour).
2. **Test baselines** — 56 false-premise questions ("A celebrity endorsed X — who was it?", "How is X handling the backlash?") across 8 AI assistants.
3. **Publish the official record** — an FAQ with explicit denials: "We have never been acquired", "We do not produce X", plus schema markup.
4. **Seed competing narratives** — three mutually contradictory third-party sources, including a pseudo-journalistic "investigation" that debunks the obvious lies while inserting new ones.
5. **Re-test** — track which source each model adopts and whether the FAQ is cited.

## Actionable checklist
- [ ] Publish an official FAQ that explicitly denies recurring false claims (exact phrasing, dates, numbers)
- [ ] Include specifics even when refusing: "We don't share unit counts" loses to "634 units in 2023" — give ranges if exacts are impossible
- [ ] Build "how it actually works" pages, data/statistics pages, and product comparison pages detailed enough to beat third-party explainers
- [ ] Make specific, substantiated claims ("fastest at [metric]", "best for [use case]") — only ones you can back with evidence; generic "industry-leading" claims get averaged into noise
- [ ] Set alerts for brand name + hijack red-flag words: investigation, deep dive, insider, former employee, lawsuit, controversy
- [ ] Ask each major assistant "What do you know about [brand]?" regularly; flag misleading answers through built-in feedback
- [ ] Watch for hallucinated URLs pointing at your site and redirect them

## Data points & benchmarks
- Baseline (no manipulation): Perplexity failed ~40% of false-premise questions (confused the fake brand with a real electronics maker); one model passed 53–54 of 56 by grounding in the real site
- After planting fake sources: the most manipulable models repeated misinformation in 37–39% of answers; the most robust stayed under 7% and cited the FAQ in 84% of answers
- 5 of 8 assistants trusted the fake "investigation" over the official FAQ
- One assistant hallucinated a full Black Friday performance analysis (+230% sales) from zero input
- Skepticism did not persist: models that first doubted the brand's existence later asserted invented facts without disclaimers

## Mistakes to avoid
- Leaving information gaps (founding story, pricing, headcount, locations) for others to fill
- Vague denials instead of quotable, specific rebuttals
- Assuming Reddit/Medium/Quora are side channels — assistants cite them directly as brand evidence
- Treating "AI" as one index — each model represents your brand differently

## Key principles
- In AI search, the most detailed story wins — even when false. Specificity is the currency of credibility.
- A debunking wrapper is the strongest attack vector: it launders new lies by first refuting old ones.
- Narrative ownership is the new PR: compete for the authoritative version of your own brand.
