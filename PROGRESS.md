# Challenges and Progress

Our record of difficulties, lessons, successes, and achievements. This file reflects what actually happened, rather than plans presented as completed work.

## Current position

- GitHub access works, and the initial commit is checked out locally.
- The repository began with only a README.
- We are discussing an AI Equity Research Agent and keeping a shared notebook.
- Initial domain: company equity research. Other research domains are a possible later expansion.
- Collaboration is defined: the user writes all application code; Codex provides ongoing technical guidance and code review and maintains these notes.
- The component now aims to gather publicly accessible information as well as retrieve documents. Its detailed notebook remains [DOCUMENT_AGENT.md](DOCUMENT_AGENT.md).
- The user confirmed Azure connectivity locally and shared a Python search/tool-calling prototype for review. Application code stays local until the user confirms it works; no application files are present in this repository.
- Browser Use 0.13.11 with Azure GPT-4.1 mini has been tried locally. The user confirmed browser startup and model connectivity; a pasted terminal trace shows navigation and downloads, but neither included Infosys run established retrieval of the requested FY2024–25 report.
- Candidate relevance, missing-year clarification, HTTP 403 download failures, navigation recovery, and document identity remain reliability issues. Parser integration, caching, and dependable broader evidence retrieval remain unverified.
- As of 16 October, the user reports a local program that captures company and research-objective variables. This new implementation has not been inspected here. The next requested stage is official-website discovery and relevant-information acquisition, discussed in [RESEARCH_ARCHITECTURE.md](RESEARCH_ARCHITECTURE.md). No application code has been changed or pushed by Codex. A six-to-seven-day focused prototype was previously discussed as a scoped estimate, not a completed capability or guarantee.

## Challenges and difficulties

### 12 October 2026 — Browser-agent trace review

The first Infosys attempt downloaded an unrelated quarterly document, mishandled back navigation in a new tab, visited an unsuccessful reports URL, and finished with `success: False`. Its final inference that the requested report was unavailable was stronger than the evidence supported. It logged normal browser cleanup.

The second attempt downloaded an annual report identified by extracted text as FY2025–26, rather than FY2024–25. It also encountered a model output truncated at 4096 output tokens and two scroll timeouts. It ended with Ctrl+C at step 10, not a successful final answer. Browser Use 0.13.11's Windows signal handler calls `os._exit(0)`, which can bypass the application's normal `finally` cleanup. The total runtime cannot be attributed precisely because comprehensive timestamps were absent.

**Lesson:** Separate an executed browser action, the model's interpretation, and independently checked task completion. A wrong-year download is not successful retrieval of the requested report. No CAPTCHA appears in the supplied trace.

**Status:** Diagnosed from the user's terminal output and the published library source; fixes have not been implemented or tested. The user asked to understand the setup before changing code.

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

### 16 October 2026 — Company and research objective captured locally

The user reports having implemented a local program that stores the company and research objective in variables. This is a user-reported input-stage milestone, not independent validation or evidence of successful website research. The next stage is to discover the official website and gather source-backed relevant information.

### 14 October 2026 — Architecture discussion record established

Created [RESEARCH_ARCHITECTURE.md](RESEARCH_ARCHITECTURE.md) to preserve the new discussion, distinguish proposals from decisions, and track unresolved assumptions. The first proposed stage covers company identification and official-website reading. This is documentation progress, not an implemented research workflow.

### 8–11 October 2026 — Local connection and documentation recovery

The user confirmed that the Azure OpenAI connection works locally and provided code for review. This establishes model connectivity, not successful document acquisition.

Cloud workspace startup failures delayed documentation updates. Access returned on 11 October, allowing a documentation-only catch-up covering local experiments, known failures, broader information-agent scope, and the engineering lessons. All detailed reasoning is in [DOCUMENT_AGENT.md](DOCUMENT_AGENT.md).

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

### Documentation milestone — dedicated component notebook

Created [DOCUMENT_AGENT.md](DOCUMENT_AGENT.md) for discussions, discoveries, approach choices, experiments, challenges, and code review notes about document retrieval and parsing. This records the focus of the work; the component itself has not been implemented.


- An empty repository offers no application workflow to install or test.
- A successful Git check confirms repository access; it does not validate an application.
- Keep tentative ideas separate from agreed decisions and verified results.

## Format for future entries

For a challenge, record the date, what happened, its impact, what we tried, the outcome, and whether it remains open.

For an achievement, record what changed, why it matters, and the evidence that supports calling it complete.
