# GEO, LLMO, AEO… It's All Just SEO

- **Updated**: 2026-10-05

## TL;DR
The three acronyms describe one discipline: every legitimate lever for LLM visibility is either classic SEO (rank in the indexes models ground on, publish relevant content on- and off-site) or black hat manipulation. But six genuine nuances matter at the edges: unlinked mentions count more, off-topic links count less, core pages and documents (PDFs) punch above their SEO weight, "global document context" improves chunk interpretation, developer-platform content trains models outside SEO's remit, and AI crawlers don't render JavaScript.

## Framework / Step-by-step
1. **The three levers on LLM visibility:**
   1. **Training data presence** — publish well-structured content on your core topics on your site and on third-party sites, for future training rounds. That's content strategy + off-site mentions = SEO.
   2. **RAG/grounding visibility** — assistants increasingly search the web and license classic search indexes; ranking there is literally SEO.
   3. **Adversarial manipulation** — tricking models into recommending you. That's black hat, and it decays.
2. **Expect convergence, not divergence** — search engines integrate more generative AI; LLMs lean harder on traditional indexes; as long as content is the medium, the mechanisms of influence stay the same. If you want more LLM presence, fund SEO.
3. **Apply the six real differences:**
   1. **Unlinked brand mentions matter more** — LLMs read words, not link tags; mentions across trusted sources strengthen the brand entity and its embedding near related concepts (relax the "dofollow-only" rule for outreach)
   2. **Off-topic links and rankings matter less** — irrelevant links and site-reputation-abuse content carry no entity context, so they do nothing for LLM understanding
   3. **Different content types win** — home/pricing/about pages and PDF documents get cited more than their SEO contribution suggests; bloated listing/collection pages get cited less
   4. **Unique document structures help** — sprinkle "global context" (brand, date, source) throughout long documents so every chunk is self-interpretable (raised retrieval QA accuracy from ~50–60% to ~72–75% in one engineering test); consider machine-first docs (e.g., single-file project docs)
   5. **LLMs train beyond the SEO remit** — public code repos, knowledgebases, and code samples are very likely training material; developer-facing brands should brand these surfaces
   6. **AI crawlers don't render JavaScript** — client-side-only content has been invisible to most AI crawlers (re-check current crawler behavior; this may change)

## Actionable checklist
- [ ] Stop budgeting "GEO" as a separate line item — audit whether the work is just SEO with new metrics
- [ ] Start accepting unlinked mentions in relevant, credible publications
- [ ] Stop buying off-topic links/content whose only value was authority inflation (buying links to pass ranking signals also violates Google's spam policies)
- [ ] Add self-contained context (brand, date, topic) to long-form pages and PDFs so chunks survive isolation
- [ ] Treat PDFs and forgotten document libraries as first-class citable content
- [ ] Brand public repos, docs, and knowledgebases for developer-facing products
- [ ] Server-render critical content; never hide it behind client-side JavaScript
- [ ] Track whether brand visibility in search and in LLMs moves together (it usually does)

## Data points & benchmarks
- One engineering test of "global document context" (metadata repeated through text): retrieval QA accuracy improved from ~50–60% to ~72–75%
- Traffic-by-page-type comparison: LLM referrals over-index on core site pages and documents; listing/collection pages under-index
- Brands that do well in classic search generally also do well in LLM outputs — visibilities are coupled
- One assistant's search feature is confirmed to use a major search engine's index for grounding — classic rankings feed AI answers

## Mistakes to avoid
- Selling/buying "GEO audits" that restate technical SEO and content strategy
- Chasing adversarial prompt/text injection tricks — short-term wins, long-term bans
- Dismissing all differences — the six nuances are cheap wins competitors miss
- Leaving PDFs, docs, and repos unbranded and uncontextualized
- Assuming the current no-JavaScript-rendering limitation of AI crawlers excuses JS-dependent content forever

## Key principles
- If content remains the medium, the core mechanisms of influence stay the same
- GEO is currently a byproduct of SEO — no dedicated process required
- Mentions are the new links, but links still rule search; do both
- SEOs — careers spent reconciling machine and human needs — are best placed to own AI visibility, whatever it's called
