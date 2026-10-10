# Changelog

## v3.1 (2026-10-05): full audit and verification release
- **Full-library fact-check and fix pass.** Nine parallel expert-review passes covered all 512 original playbooks, and about 490 files were corrected, including:
  - retired Search Console tools (Mobile Usability report, robots.txt Tester, Coverage → Page indexing)
  - INP instead of FID; FAQ and HowTo rich-result limits; Google Business Profile changes
  - robots.txt facts and WebP/AVIF image formats
  - misstated or undated statistics
  - warnings on risky tactics (paid or value-exchange links, expired domains, doorway or scaled content, undisclosed promotion)
  - removal of leftover vendor UI, vendor voice and garbled text
- **New and expanded playbooks.**
  - New: Google Business Profile troubleshooting; local SEO in Bangladesh.
  - Expanded: ready JSON-LD templates (Product in BDT, LocalBusiness, Organization); a 90-day content plan with an ecommerce and skincare variant; a compressed 4-week migration plan; ROI and payback in the forecasting model; a free keyword recipe for beginners.
- **Router.**
  - Traffic drops always go to `traffic-drop-doctor` first.
  - New routing rows for schema, SaaS and "no traffic at all".
  - The language rule now matches the user's level (simple Bangla for beginners, professional Bangla for experts).
  - New YMYL guardrail.
- **Traffic Drop Doctor.** Google update dates are now current through September 2026 (Google Search Status Dashboard), and the script warns when the events file is out of date.
- **Docs.** Added a full strategy guide (Bangla and English) with a system map, `CREDITS.md`, `LICENSE.md` and `AUDIT-REPORT.md`. Internal research and pricing documents were removed from the public pack.

## v3.0 (2026-10-05): newbie setup and Bangla docs
- Per-platform folders: Claude, ChatGPT/Gemini and coding agents, plus install scripts.
- A complete Bangla guide with 75 prompts, available offline as HTML.
- Bangla-reply rule added in every skill.
- Traffic Drop Doctor merged into the pack (11 skills in total).

## v2.0 (historical; the folder layout changed in v3) (2026-10-04)

### Validation
- All 10 skills pass the official Agent Skills spec validator (`quick_validate.py`): frontmatter, kebab-case name, description ≤1024 characters, no angle brackets.
- All 10 pass `tools/validate_skills.py --strict` with 0 errors and 0 warnings. Its checks:
  - name matches folder
  - SKILL.md under 500 lines
  - every relative link resolves
  - no orphan articles
  - ARTICLES.md in sync with the articles folder
  - every article has TL;DR, checklist, mistakes and principles sections
  - no raw URLs (example domains allowed)
  - no vendor brand or staff names
- Functional testing: simulated beginner and advanced users ran against every skill through independent test agents, followed by a regression pass.

### New
- **`seo-router` skill**: entry point with level detection, a routing table and 7 multi-skill workflows (new site, audit, traffic drop, blog post, AI visibility, local, enterprise).
- **Learning path** (Beginner / Intermediate / Advanced) in every skill.
- **Agent-neutral "How to use this skill" section** in every skill.
- **GLOSSARY.md** (bundled in every skill), containing:
  - plain-English terms
  - a tool-category → free-alternative table
  - a "report names" translation table
- **6 new advanced playbooks**:
  - keyword clustering at scale
  - large-site migration with log validation
  - manual AI visibility audit
  - SEO forecasting model
  - multi-location/franchise operations
  - title audit at scale
- **AGENTS.md** for Cursor, Copilot, Codex, Gemini CLI and other AGENTS.md-aware tools.
- **knowledge-pack/**: one merged file per skill plus paste-in instructions for ChatGPT, Gemini Gems, Claude Projects and NotebookLM.
- **Trigger-optimized descriptions** for all skills.

### Fixed
- Removed about 220 remaining vendor and tool names, vendor-staff attributions, and first-person vendor voice ("our blog", "my research"). These are now neutral phrasing, as the library policy requires.
- Fixed anonymization artifacts ("8 an SEO data API", "your an SEO data API", "my research grew", and stray non-English text).
- Factual updates:
  - FAQ rich results are limited to government and health sites (since August 2023).
  - HowTo rich results were removed.
  - GBP chat was discontinued (2024), and GBP Q&A is marked legacy.
  - Service-area business address rule now matches Google's guidelines.
  - Googlebot verification uses reverse DNS or published IP ranges, not an IP prefix.
  - Migration disavow and geo-targeting advice corrected.
  - Title width aligned to ~600px.
- Removed internal maintenance notes from SKILL.md files ("pending", "skill complete").
- MCP-only wording changed to "CSV export, API, or connector".
