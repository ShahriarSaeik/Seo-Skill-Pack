# 7 Confirmed Google Ranking Factors

- **Updated**: 2026-10-05

## TL;DR
Most claimed ranking factors are unconfirmed speculation. Seven that Google has publicly confirmed (a core list, not exhaustive) are: backlinks, relevance, freshness, HTTPS, mobile-friendliness, page speed (Core Web Vitals), and intrusive interstitials. Optimize these before spending time on anything speculative.

## Framework / Step-by-step
The seven confirmed factors, roughly in order of practical impact (a judgment call, not a Google ranking):

1. **Backlinks** — confirmed 2016 as one of the strongest ranking factors. Quality matters: build links from prominent websites on the topic, not just any site.
2. **Relevance (search intent)** — Google's systems infer what searchers want; you must too. Study top-ranking pages: content type (blog post vs. product page), format, angle. Use a content-gap analysis of top pages' common keyword rankings to reveal required subtopics (e.g., pages ranking for "air fryer" also cover best brands).
3. **Freshness** — query-dependent: strong for "netflix new shows," irrelevant for "how to solve a rubik's cube." If your keyword rewards freshness, update regularly or publish new content.
4. **HTTPS** — a lightweight ranking factor since 2014. Install a TLS certificate if you're serving the "Not Secure" warning.
5. **Mobile-friendliness** — a mobile ranking signal since 2015 (historical); since mobile-first indexing, Google primarily uses the mobile version of your content for indexing and ranking, so mobile and desktop content must match. Test with Lighthouse / PageSpeed Insights and Chrome DevTools device mode (Search Console's Mobile Usability report and the Mobile-Friendly Test were retired in Dec 2023).
6. **Page speed** — factor since 2010 (desktop) / 2018 (mobile). Google measures page experience through Core Web Vitals: LCP (loading), INP (responsiveness; replaced FID in March 2024), CLS (visual stability). Goal is "fast enough," not fastest — very slow experiences are the most at risk.
7. **Intrusive interstitials** — a negative ranking factor since 2017, now part of Page Experience signals. Use banners instead of full-page overlays; don't obscure content; don't redirect to separate consent/input pages.

## Actionable checklist
- [ ] Audit backlink profile; prioritize links from topical, prominent sites
- [ ] Verify every target keyword's page matches SERP intent (type/format/angle)
- [ ] Check SERP dates: update pages where freshness is rewarded
- [ ] Serve all pages over HTTPS
- [ ] Pass mobile checks (Lighthouse, DevTools device mode, mobile/desktop content parity)
- [ ] Hit "good" Core Web Vitals thresholds (LCP/INP/CLS)
- [ ] Replace intrusive popups with non-obstructive banners

## Data points & benchmarks
- Backlinks as top factor: confirmed by Google in 2016.
- HTTPS factor live since 2014; mobile-friendliness since 2015; interstitial penalty since 2017; page speed since 2010 (desktop), 2018 (mobile).
- FID was replaced by INP as the interactivity metric in March 2024.

## Mistakes to avoid
- Chasing unconfirmed "ranking factors" (most SEO factor lists are speculation).
- Obsessing over millisecond speed improvements — "good" Core Web Vitals is the goal, not perfect scores.
- Using full-screen interstitials (including consent redirects).
- Treating freshness as universally important — it's query-dependent.

## Key principles
- Build links from sites that are prominent on the subject — topical relevance beats raw authority.
- Content-gap analysis of top-ranking pages reveals which subtopics relevance requires.
- Six of the seven confirmed factors are table stakes; backlinks and relevance are where rankings are won.
