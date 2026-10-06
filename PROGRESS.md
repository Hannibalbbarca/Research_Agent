# Challenges and Progress

Our record of difficulties, lessons, successes, and achievements. This file reflects what actually happened, rather than plans presented as completed work.

## Current position

- GitHub access works, and the initial commit is checked out locally.
- The repository began with only a README.
- We are discussing an AI Equity Research Agent and keeping a shared notebook.
- Initial domain: company equity research. Other research domains are a possible later expansion.
- Collaboration is defined: the user writes all application code; Codex provides ongoing technical guidance and code review and maintains these notes.
- The first planned component retrieves company documents for a specified financial year and parses them with Python, with later integration into the main agent.
- No application, dependency setup, or application tests exist yet.

## Challenges and difficulties

### 6 October 2026 — The repository initially had no commits

**What happened:** During the first setup check, the remote had no branches or commits. There were no project files to inspect or install.

**Impact:** Application setup and validation could not begin.

**Resolution:** A later check found an initial commit on `main`. It was fetched and checked out successfully.

**Status:** Resolved.

### 6 October 2026 — Defining the research workflow

**Progress:** The user has defined the project as an end-to-end AI Equity Research Agent for companies, with broader research as a possible later direction.

**Still to understand:** Intended users, markets, workflow boundaries, and final deliverables.

**Next step:** Describe the desired result for researching one company before selecting tools or implementation details.

**Status:** Open discussion topic.

### 6 October 2026 — Document pipeline design questions

**Anticipated difficulties, not observed failures:** Finding the correct legal entity and financial-year report; rejecting misleading links or wrong-year documents; dealing with scanned PDFs and financial tables; and preserving source references during extraction.

**Next step:** Confirm the first document type and desired parsing output, then compare suitable approaches and libraries.

**Status:** Design discussion. No retrieval or parsing behavior has been implemented or tested.

## Successes and achievements

### 6 October 2026 — Repository access verified

Git could read the remote and fetch the initial commit on `main`. The checkout was clean after the fetch.

### 6 October 2026 — Shared notes established

Created three linked Markdown documents:

- [IDEAS.md](IDEAS.md): discussions, reasoning, decisions, and open questions.
- [TOOLS.md](TOOLS.md): tools in use and future selection decisions.
- [PROGRESS.md](PROGRESS.md): challenges, outcomes, and lessons.

### 6 October 2026 — Collaboration clarified

The user clarified that "handwritten" means writing all application code personally. Codex will support method and tool selection, explain tradeoffs, and review code at each step. We remain in discussion mode.

### 6 October 2026 — First component scoped

The user selected document retrieval and Python parsing as the first piece of the project. It should be a reusable pipeline that can later connect to the main research agent. This is a scope decision, not a completed implementation.

## Lessons so far

- An empty repository offers no application workflow to install or test.
- A successful Git check confirms repository access; it does not validate an application.
- Keep tentative ideas separate from agreed decisions and verified results.

## Format for future entries

For a challenge, record the date, what happened, its impact, what we tried, the outcome, and whether it remains open.

For an achievement, record what changed, why it matters, and the evidence that supports calling it complete.
