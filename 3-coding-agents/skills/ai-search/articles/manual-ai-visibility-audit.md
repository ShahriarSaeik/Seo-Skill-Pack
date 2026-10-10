# Manual AI Visibility Audit (No Paid Tracker Needed)

- **Updated**: 2026-10-05

## TL;DR
AI answers vary from run to run, so a single test proves nothing. Build a fixed prompt set (30–60 prompts across the buyer journey), run each prompt several times per assistant, and log brand mentions, citations, position, sentiment and accuracy for you and 3 competitors. Turn the results into share of voice and a gap list, then fix the gaps with on-site content (Build), corrections (Fix) and third-party mentions (Influence). Re-run monthly with the same prompts.

## Framework / Step-by-step
1. **Build the prompt set (30–60 prompts).**
   - Sources: customer questions from sales and support, Search Console queries phrased as questions, PAA, forums and Reddit threads.
   - Spread across stages:
     - Awareness: "how do I…", "what is…"
     - Consideration: "best X for Y", "X vs Y", "alternatives to X"
     - Decision: "is X worth it", "X pricing", "X reviews"
   - Include about 20% branded prompts ("what is [brand]", "[brand] vs [competitor]") to test accuracy.
2. **Choose assistants.** Cover the 3–5 your audience uses (for example ChatGPT, Google AI Overviews and AI Mode, Perplexity, Gemini, Copilot). Note the model or mode and whether web search was on.
3. **Run with controls.** Use a logged-out or fresh session and the same location and language. Run each prompt **3–5 times** per assistant, because brand lists rarely repeat exactly.
4. **Log every run** in a spreadsheet:
   - Columns: prompt, stage, assistant, run #, brands mentioned (in order), your position, cited URLs/domains, sentiment (+/0/−), factual errors, date.
5. **Score.**
   - **Mention rate:** runs that mention you ÷ total runs.
   - **Share of voice:** your mentions ÷ all tracked-brand mentions.
   - **Citation rate:** runs citing your domain ÷ runs.
   - **Average position** when mentioned.
   - **Accuracy issues:** count and severity.
   Compute each one per stage and per assistant.
6. **Find gaps.**
   - (a) Prompts where competitors appear and you don't.
   - (b) Domains AI cites for your topics (review sites, listicles, forums, Wikipedia, YouTube) where you're absent.
   - (c) Inaccurate or outdated claims about your brand.
   - (d) Fan-out sub-questions with no page on your site. Ask the assistant what it searched, or infer from its citations.
7. **Plan with Fix / Build / Influence.**
   - **Fix:** correct facts on your site, pricing and feature pages, schema and profiles.
   - **Build:** answer-first pages for missing prompts and comparisons.
   - **Influence:** get onto cited third-party pages through PR, reviews, community participation and listicle outreach (disclose affiliations; never pay for undisclosed placements).
8. **Re-run monthly** with the identical prompt set and report trends, not single snapshots.

## Actionable checklist
- [ ] 30–60 prompts across awareness, consideration and decision, ~20% branded
- [ ] 3–5 runs per prompt per assistant, with fresh sessions and fixed location
- [ ] Log mentions, order, citations, sentiment and errors for you plus 3 competitors
- [ ] Compute mention rate, share of voice, citation rate and position per stage
- [ ] List the top 20 cited third-party domains in your topic
- [ ] Turn gaps into a Fix / Build / Influence backlog with owners
- [ ] Check AI referral traffic in analytics (assistant domains as referrers) to tie visibility to visits
- [ ] Keep the prompt set frozen; add new prompts as a separate cohort

## Data points & benchmarks
- One experiment asking an assistant the same brand-recommendation question 100 times found less than a 1-in-100 chance of getting an identical list twice. That's why multiple runs are mandatory.
- Brand web mentions correlate more strongly with AI visibility than backlinks in large-scale studies (one study of 75K brands).
- AI-cited content skews fresher than classic search results, so dated pages are a common gap.

## Mistakes to avoid
- Judging visibility from one run, or from your own logged-in, personalized session
- Tracking only branded prompts (these inflate your score)
- Changing the prompt set every month, which makes trends meaningless
- Building only on-site content when the gap is third-party citations
- Ignoring wrong facts. Inaccurate answers cost more than missing ones.

## Key principles
- AI visibility is probabilistic; measure rates, not ranks.
- You get cited where the AI already looks, so map its sources first.
- Same prompts, same method, every month. Consistency beats tooling.
