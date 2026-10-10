# How to Detect (and Deflect) Negative SEO Attacks

- **Updated**: 2026-10-05

## TL;DR
Negative SEO = competitors using black-hat tactics (spam links, fake link-removal requests, scraping, fake parameters, fake reviews, hacking, DDoS) to sabotage your rankings. It rarely works today — link spam is devalued rather than demoted, granularly — but vigilance is cheap: monitor new/lost backlinks, indexed-page counts, security issues, and brand SERPs, and harden the site so most attacks can't land.

## Framework / Step-by-step
**Why attacks mostly fail:** since the link-spam algorithm update of 2016, Google devalues ("ignore this junk") rather than demotes sites, and does it granularly (page/section, not necessarily whole site). Its business model depends on spam not winning. Non-link attacks (hacks, reviews, DDoS) remain the real risks.

**The 7 attack types and defenses:**
1. **Spammy link building** (volume blasts or exact-match anchor manipulation) — detect via new-backlink alerts (abnormal referring-domain spikes), backlink graphs, anchor-text distribution (unnatural keyword-rich %), referring IP/subnet breakdown (hundreds of domains on one subnet = PBN). Fight: usually ignore (Google filters it); disavow only if you have a self-made link history, are in an ultra-competitive vertical, or traffic drops coincide with the attack.
2. **Fake link removal requests** — attackers email your linkers pretending to be you. Detect via lost-backlink alerts; when good links vanish without cause, ask the linking site why and request reinstatement.
3. **Content scraping** — copies can outrank originals on stronger domains. Detect by quoting a sentence in search (32-word limit), checking "Google-selected canonical" in the URL Inspection tool (an external canonical = possible scraping), or scale checkers. Fight: request attribution links, file DMCA takedowns as last resort; strong internal linking signals originality.
4. **False URL parameters** — attackers link to your URLs with fake ?params hoping to trigger duplicate indexing. Detect: sudden indexed-page spikes in the Page indexing report. Prevent: self-referencing canonicals on every page.
5. **Fake reviews** — monitor brand-review SERPs monthly (from multiple locations for local). Fight: report fakes to platforms (slow); never report genuine bad reviews — respond to them; drown fakes with a steady stream of genuine reviews.
6. **Hacking** — malware flags or "this site may be hacked" labels destroy rankings and CTR. Detect: Search Console Security Issues report. Prevent: strong passwords, updated CMS/plugins, security monitoring/cleanup services.
7. **DDoS** — flood your server (multi-terabit-per-second attacks have been recorded) or subtly slow it (hurting UX and CWV). Extended 503s can cause deindexation. Fight: CDN/DDoS protection, load balancing, origin shielding — not something you handle on origin hosting.

## Actionable checklist
- [ ] Set up new + lost backlink alerts with a sensible email cadence
- [ ] Learn your normal daily referring-domain baseline; investigate spikes
- [ ] Check the anchor-text distribution for unnatural exact-match concentration
- [ ] Deploy self-referencing canonicals site-wide (parameter attack inoculation)
- [ ] Watch indexed-page counts for unexplained spikes
- [ ] Monitor Search Console Security Issues; keep CMS/plugins patched
- [ ] Search your brand + "reviews" monthly from key locations
- [ ] Put the site behind a CDN with DDoS mitigation
- [ ] Only disavow when drops coincide with spam you didn't build

## Data points & benchmarks
- In one example, a widely used free tool attracted links from 1M+ spam pages yet still earned ~133K organic visits/month — spam devaluation works.
- In one reported example, spam links sold at ~40,000 links per dollar (60M for $1,475) — attacks are cheap, which is why they're common.
- Penguin 4.0 (2016): link spam devalued in real time, granularity finer than site-level.
- A Google representative once said they had reviewed hundreds of "negative SEO" cases and none were the actual cause of the drop (usually algorithm updates or site issues).
- Search engines process a maximum of 32 words per quoted search when hunting scrapers.

## Mistakes to avoid
- Blaming negative SEO for traffic drops before ruling out algorithm updates and your own site issues.
- Disavowing indiscriminately — wrong disavows do more harm than the spam.
- Clicking suspicious linking sites while investigating (security risk).
- Reporting genuine negative reviews instead of responding to them.
- Skipping prevention (canonicals, patching, CDN) — every defense here is cheaper than recovery.

## Key principles
- Assume incompetence before malice: most ranking drops are self-inflicted or algorithmic.
- Monitoring (links, index counts, security, brand SERPs) is the entire detection strategy.
- Prevention beats remediation for hacks and DDoS; devaluation handles most link spam for you.
