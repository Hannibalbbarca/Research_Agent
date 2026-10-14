# Tools We Use

A record of the tools we actually use, why we use them, and what remains undecided.

## Currently in use

| Tool | What we use it for |
| --- | --- |
| Codex | Discussing ideas, advising on methods, SDKs and libraries, reviewing user-written code, and maintaining our notes. |
| Git | Tracking file history and synchronizing changes with GitHub. |
| GitHub | Hosting the Research_Agent repository and making our notes available later. |
| Markdown | Writing readable notes with headings, lists, and links. |
| Codex cloud environment | Providing the workspace where we inspect and edit repository files. |

## Used or selected for the local prototype

| Tool | Purpose | Evidence/status |
| --- | --- | --- |
| Python | Information-agent tools and future parser integration. | User-written local prototype shared for review. |
| Azure OpenAI | Model inference and tool-call decisions. | User confirmed the local connection works. |
| Azure GPT-4.1 mini | Model used in the local Browser Use experiment. | User confirmed connectivity; terminal trace shows browser-agent operation, but dependable report retrieval has not been established. |
| Browser Use 0.13.11 | Candidate browser-agent framework for local navigation and document discovery. | Tried locally; first report run failed and the second found the wrong year before interruption. Not selected as the final research architecture. |
| Playwright / Chromium | Install and run a local browser for the experiment. | User confirmed browser startup. No separate custom Playwright agent was built. |
| OpenAI Python SDK | Connect to the Azure `/openai/v1/` endpoint. | Used in the pasted local code; no dated API-version argument. |
| python-dotenv | Load local settings from `.env`. | Used in the pasted code; credentials stay local. |
| ddgs | Initial web-source discovery. | Used in local search experiments; candidate relevance is insufficient for dependable document acquisition. |
| HTTPX | HTTP requests and download examples. | Downloads attempted by the user; many HTTP 403 responses reported. Reliable acquisition is not yet established. |

These are local-prototype records, not evidence of an installed or tested application in this cloud checkout. Detailed reasoning and results belong in [DOCUMENT_AGENT.md](DOCUMENT_AGENT.md).

## Used during environment setup

- **Cloud environment onboarding skill:** Guided checkout inspection and setup checks.
- **Bash and command-line file tools:** Inspected the workspace and repository files.

These helped prepare the workspace. They are not decisions about the application's technology stack.

## Selected for future implementation

| Tool | Intended purpose | Status |
| --- | --- | --- |
| Document parser | Parse complex downloaded documents. | Being investigated by the user's friend; implementation and interface not provided here. |

Beautiful Soup, managed search/page-reading services, Pydantic, and storage/index options have been discussed but not confirmed as part of the reliable implementation. Playwright was used to install Chromium for the local browser experiment; this is separate from building a custom agent on Playwright.

## Not selected yet

Azure OpenAI is the current prototype model provider. Browser Use is a tested prototype candidate, not a finalized production framework. We have not selected a production search/reading service, parser library, database/index, application interface, or deployment platform. Codex as an application runtime was considered and is currently set aside.

As of 14 October, the broader architecture is being discussed from first principles in [RESEARCH_ARCHITECTURE.md](RESEARCH_ARCHITECTURE.md). The new discussion does not commit us to the earlier prototype's tools.

We will choose tools after discussing the problem and requirements. A suggested tool should stay marked as a candidate until we agree to use it.

The user will write the application code personally. Codex will explain recommendations and tradeoffs, help with usage questions, and review the resulting code as development progresses.

## What to record when we add a tool

- Its name and purpose.
- Whether it is a candidate, selected, or actively used.
- Why it fits our needs and which alternatives we considered.
- Costs, limitations, and required access.
- What we have actually tested.

Never put API keys, passwords, or other secret values in these notes.
