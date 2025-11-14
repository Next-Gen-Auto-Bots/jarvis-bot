Repository purpose:
This repository hosts Jarvis-bot — a GitHub App/bot that assists with automation and developer workflows. Primary languages: TypeScript (Node.js), plus configuration files (YAML, JSON), and documentation (Markdown).

Primary goals for Copilot pull request reviews:
- Focus on correctness, security, and maintainability of code changes.
- Ensure changes include tests or justify why tests are not needed.
- Check configuration and CI workflow changes for potential risks.
- Prefer concise, actionable feedback and suggested code diffs when possible.

What to look for:
- Common bugs, off-by-one errors, null/undefined handling, and type mismatches.
- Misconfigured GitHub Actions workflows or secrets usage.
- Missing or incomplete tests for new or changed functionality.
- Unnecessary large or binary files added to the repo.
- Inconsistent code style or obvious anti-patterns.

Tech details & commands:
- Repo root contains package.json. Use `npm install` and `npm test` to run tests locally.
- Lint: `npm run lint` (where applicable).
- Build: `npm run build`.

Files and filetypes to prioritize:
- .ts, .tsx, .js for code review
- .yml/.yaml for GitHub Actions or other CI configs
- package.json, tsconfig.json, Dockerfile
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
2. Create a small test PR (e.g., update README or change a trivial .ts file) to confirm Copilot posts a review.
3. If Copilot still can't review, check repository Copilot settings and organization-level policies; consider enabling GitHub Copilot for this repo and adding required permissions.

Parent issue: https://github.com/Next-Gen-Auto-Bots/Jarvis-bot/issues/3

Acceptance criteria:
- A new file .github/instructions/default.instructions.md is added in a PR targeting main.
- The PR references issue #3 and explains the purpose.
- Instructions are clear and provide commands and priorities for Copilot reviews.

Additional PR details:
- Branch name: add/copilot-instructions
- PR title: Add Copilot repository custom instructions to improve PR reviews
- Request review from: @tabrezahmed51

Please create the branch, add the file, commit, push, and open the PR targeting main.
