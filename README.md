<div align="center">

# SEO Skills Pack v3.1

**A multilingual, AI-ready SEO playbook library for coding agents and AI assistants.**

[Bangla quick start](START-HERE-BANGLA.md) · [Installation guides](docs-bn/) · [Strategy](STRATEGY.md) · [Audit report](AUDIT-REPORT.md) · [License](LICENSE.md)

</div>

---

> **Attribution:** This repository redistributes the **SEO Skills Pack by Rashed Hasan Akash** under the terms in [`LICENSE.md`](LICENSE.md). It is not an original work of this repository's maintainer. Please preserve the author's credit. The license allows free use, sharing and adaptation, but prohibits resale of the pack or a lightly modified copy.

## What is included?

The pack contains **11 AI skills and 514 SEO playbooks**, along with Bangla-first setup guides and a Search Console traffic-drop analysis script. It is designed for beginner, intermediate and advanced workflows, and supports vendor-neutral guidance across traditional SEO and AI search visibility (AEO/GEO).

### The 11 skills

| Skill | What it helps with |
|---|---|
| `seo-router` | Routes requests to the right skill and coordinates multi-step workflows |
| `seo-fundamentals` | SEO strategy, site audits, search intent and core concepts |
| `keyword-research` | Keyword discovery, intent, clustering and mapping |
| `on-page-seo` | Titles, meta descriptions, headings, internal links and page-level improvements |
| `technical-seo` | Crawling, indexing, redirects, canonicals, structured data and performance |
| `link-building` | Backlink audits, outreach and digital PR workflows |
| `content-marketing` | Content planning, briefs, writing, refreshing and measurement |
| `local-seo` | Local visibility, business profiles, reviews and location pages |
| `enterprise-seo` | SEO at scale, forecasting, reporting and operational workflows |
| `ai-search` | AI answer visibility, AEO/GEO, citations and AI referral measurement |
| `traffic-drop-doctor` | Evidence-led diagnosis of organic traffic declines using Search Console exports |

## Choose your setup

| Platform or workflow | Folder | Quick start |
|---|---|---|
| Claude Skills | [`1-Claude/`](1-Claude/) | Upload the `.skill` files; start with `seo-router.skill`. |
| ChatGPT, Gemini or project-based assistants | [`2-ChatGPT-Gemini/`](2-ChatGPT-Gemini/) | Use the instructions file and upload the matching knowledge files. |
| Claude Code, Cursor, Copilot, Codex, Gemini CLI and other coding agents | [`3-coding-agents/`](3-coding-agents/) | Copy `AGENTS.md`, `GLOSSARY.md` and `skills/` into your project, then follow the platform guide. |

New to the pack? Start with the [Bangla guide](START-HERE-BANGLA.md). The detailed installation instructions are in [`docs-bn/`](docs-bn/).

## Traffic Drop Doctor

The `traffic-drop-doctor` skill includes a Python analyzer for Google Search Console exports. It helps separate impressions changes from CTR changes, identify losing pages and queries, and produce a structured diagnostic report. The included demo data is fictional.

See [`STRATEGY.md`](STRATEGY.md) and [`docs-bn/07-traffic-drop-doctor.md`](docs-bn/07-traffic-drop-doctor.md) for examples and usage notes. Validate findings against the site's own data before making decisions.

## Installation safety note

Review scripts before executing them. The Claude Code installer replaces any existing target skill directory with the same skill name (`rm -rf` on macOS/Linux and `Remove-Item -Recurse -Force` on Windows) before copying the packaged version. Back up custom changes in `~/.claude/skills/` or a project's `.claude/skills/` folder first. Prefer a project-specific installation when testing.

## Quality notes and limitations

- The included upstream audit report describes the author's release checks; it is not an independent audit performed by this repository maintainer.
- SEO guidance, platform interface labels and third-party statistics can become outdated. Verify important claims against current primary sources.
- No skill can guarantee rankings, traffic or business results.
- Preserve the original credits and license when sharing or adapting this pack.

## Credits and license

Original pack author: **Rashed Hasan Akash**. See [`CREDITS.md`](CREDITS.md) for the project's attribution notes and [`LICENSE.md`](LICENSE.md) for the permitted use and restrictions.
