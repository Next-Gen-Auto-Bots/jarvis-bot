Repository purpose:
This repository hosts Jarvis-bot — a GitHub App/bot that assists with automation and developer workflows. Primary languages: Python (Telegram bot backend), TypeScript/JavaScript (Astro-based website), plus configuration files (YAML, JSON), and documentation (Markdown).

Primary goals for Copilot pull request reviews:
- Focus on correctness, security, and maintainability of code changes.
- Ensure changes include tests or justify why tests are not needed.
- Check configuration and CI workflow changes for potential risks.
- Prefer concise, actionable feedback and suggested code diffs when possible.

What to look for:
- Common bugs, off-by-one errors, null/undefined handling, and type mismatches.
- Python-specific: improper exception handling, resource leaks, security vulnerabilities in bot handlers.
- Misconfigured GitHub Actions workflows or secrets usage.
- Missing or incomplete tests for new or changed functionality.
- Unnecessary large or binary files added to the repo.
- Inconsistent code style or obvious anti-patterns.

Tech details & commands:
- Python bot code in `bot/` directory. Dependencies in requirements.txt.
  - Install: `pip install -r requirements.txt`
  - Lint: `flake8 bot/` or `pylint bot/**/*.py`
  - Test: `npm test` (currently minimal test infrastructure)
  - Security scan: `bandit -r bot/` and `pip-audit`
- Astro website component (package.json in repo root).
  - Install: `npm install`
  - Dev: `npm run dev`
  - Build: `npm run build`
  - Test: `npm test`
- Multiple CI workflows in `.github/workflows/` including CodeQL, pylint, Black Duck scans.

Files and filetypes to prioritize:
- .py for Python bot code review
- .ts, .tsx, .js for Astro website code review
- .yml/.yaml for GitHub Actions or other CI configs
- package.json, requirements.txt, tsconfig.json for dependency changes
- .env.example for configuration templates
- Do not attempt to review large binary files or assets (e.g., .png, .jpg, .zip)

Tone and output style:
- Be concise and polite. Provide short summary then bullet points with findings.
- Include suggested code snippets or minimal diffs for fixes when possible.
- If you are uncertain, state assumptions and request clarification from the author.

Examples (how to respond):
- Short summary: "Looks good overall, but tests are missing for X and there's a potential null dereference in Y."
- Suggested code: Provide minimal code snippet with explanation.

Verification steps for maintainers:
1. Merge this PR to main.
2. Create a small test PR (e.g., update README or change a trivial .py file) to confirm Copilot posts a review.
3. If Copilot still can't review, check repository Copilot settings and organization-level policies; consider enabling GitHub Copilot for this repo and adding required permissions.

Parent issue: https://github.com/Next-Gen-Auto-Bots/Jarvis-bot/issues/3
