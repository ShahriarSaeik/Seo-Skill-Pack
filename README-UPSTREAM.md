# SEO Skills Pack (v3.1)

> **বাংলায় শুরু করুন:** `START-HERE-BANGLA.html` ফাইলটা ব্রাউজারে খুলুন (ডাবল-ক্লিক করুন)। নতুনদের জন্য সব কিছু সেখানে ধাপে ধাপে বলা আছে।

There are 11 AI agent skills and 514 vendor-neutral SEO playbooks, for beginners through advanced users. They work with Claude, ChatGPT, Gemini, Cursor, Copilot, Codex and any other agent that reads markdown. The agents answer in the user's language, including Bangla.

## Pick your platform
| You use | Folder | How |
|---|---|---|
| Claude (claude.ai or Desktop) | `1-Claude/` | Settings → Capabilities → turn on code execution → Skills → upload each `.skill` file (start with `seo-router`) |
| ChatGPT / Gemini / Claude Projects | `2-ChatGPT-Gemini/` | Paste `chatgpt-files/00-instructions.md` into Instructions, then upload the other files as knowledge (use `gemini-files/` for Gemini Gems) |
| Claude Code, Cursor, Copilot, Codex, Gemini CLI | `3-coding-agents/` | Copy `AGENTS.md`, `GLOSSARY.md` and `skills/` to your project root, or run `install/install-claude-code.sh` (or `.ps1`) |

## Skills
`seo-router` (start here) · `seo-fundamentals` · `keyword-research` · `on-page-seo` · `technical-seo` · `link-building` · `content-marketing` · `local-seo` · `enterprise-seo` · `ai-search` · `traffic-drop-doctor` (diagnoses traffic drops from Search Console exports and writes a client report)

## Understand the whole strategy
- `STRATEGY.md`: architecture, workflows, Traffic Drop Doctor and how to extend the library (for experienced users)
- `docs-bn/10-pura-strategy.md`: the same in Bangla, plus a 30-day beginner path and an agency workflow
- `AUDIT-REPORT.md`: how every skill was audited, tested and verified before release
- `CREDITS.md` and `LICENSE.md`: sources and terms (free to use and share, not for resale)

## Folders
- `docs-bn/`: full Bangla user guide (install, first use, 75 ready prompts, troubleshooting, glossary, full strategy)
- `docs/`: changelog
- `tools/validate_skills.py`: re-run validation after editing (`python tools/validate_skills.py 3-coding-agents/skills --strict`)

Playbooks are vendor-neutral and their statistics date from 2026. No skill guarantees rankings.
