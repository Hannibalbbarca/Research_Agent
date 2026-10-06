# Document Retrieval and Parsing — Discussion Notebook

Our dedicated notebook for the first component of the AI Equity Research Agent.

## Current focus

For the next five to six days, we will focus on this component: finding the required company documents, fetching them, and parsing them into a form the main research system can read and use.

We are currently in discussion mode. The user writes the application code; Codex helps with design, methods, SDKs, libraries, debugging guidance, and code review. Codex maintains these notes on GitHub.

## Where our notes belong

The three original files keep their existing roles: [IDEAS.md](IDEAS.md) for overall ideas and decisions, [TOOLS.md](TOOLS.md) for the tool inventory, and [PROGRESS.md](PROGRESS.md) for overall challenges and achievements. Update them only when necessary as the project advances.

All detailed explanations and discussions of this document retrieval and parsing component belong in **this file**: architecture, methods, library comparisons, findings, experiments, difficulties, and code review reasoning. Avoid duplicating those details across the three main files.

## What we have agreed

- Build the project piece by piece, starting with document retrieval and parsing.
- The retrieval component should find requested documents on the internet for a company and a specified financial year.
- Parsing will use ordinary Python code written by the user.
- The complete pipeline should be usable independently and later connect to the main research agent.
- Use this file for detailed discussions and findings about this component.

The exact agent framework, libraries, supported document types, and output format have not been chosen. Calling this a pipeline, agent, or sub-agent does not settle its architecture.

## Example we are working toward

A user requests a company's report for a particular financial year. The component locates the requested document, downloads it, and returns parsed content that the research system can use.

The spoken example was transcribed as "Wadilal." The exact company, year, and report type have not been confirmed. Annual-report PDFs were suggested as a possible starting point, but the user has not yet confirmed that scope.

## Proposed flow — still open for discussion

1. **Understand the request:** Identify the company, document type, and financial year.
2. **Find candidates:** Locate possible documents, preferably from official or authoritative sources.
3. **Fetch and inspect:** Download the file and check whether it matches the request. Initial extraction may be needed to inspect its contents.
4. **Parse:** Use Python to extract the agreed content from the matching document.
5. **Return a usable result:** Provide parsed content, document metadata, source references, and any warnings or failures.

This is a proposal to discuss, not an implemented or tested design.

## Questions we still need to answer

- Which document types should the first version support?
- How should we identify the correct company and financial-year period?
- What should the retrieval agent decide, and what should ordinary code handle?
- Does parsing need text, tables, or both? Do scanned documents belong in the first version?
- What output should the main research agent receive, and how should it call this component?
- What should happen when a document is missing, ambiguous, inaccessible, or only partly readable?

## Tools and approach decisions

**Selected:** Python for document parsing.

**Not selected:** Retrieval SDK, agent framework, search provider, download library, parsing library, OCR approach, storage, and integration interface.

As we compare tools, record their purpose, alternatives, tradeoffs, and why we choose them. Keep the overall [tool record](TOOLS.md) updated when a choice is made.

## Findings and experiments

No document retrieval or parsing experiments have been run yet. Future entries should identify the document or source examined, the method tried, the observed result, and its limitations.

## Challenges to investigate

These are anticipated difficulties, not failures we have already observed:

- Confusing similar company names or fetching the wrong financial year.
- Links that lead to a webpage rather than the requested document.
- Scanned pages, complex financial tables, and incomplete extraction.
- Keeping source and page references attached to parsed content.
- Reporting partial results clearly rather than presenting them as complete.

## Code review notes

No application code has been submitted for review yet. When the user writes a component, record the version reviewed, findings, reasoning, and follow-up outcomes here.

## Discussion log

### 6 October 2026 — Dedicated focus and notebook agreed

**User's direction:** Focus on the document retrieval and parsing component for the next five to six days, and create a separate Markdown file for its discussions and discoveries.

**Decision:** This file is the detailed notebook for that work. [IDEAS.md](IDEAS.md) remains the overall project notebook; [PROGRESS.md](PROGRESS.md) records project-wide challenges and achievements.

**Current state:** Discussion only. The user is still explaining the requirements.

**Follow-up clarification:** Keep the three original files in their existing roles, making necessary updates as work progresses. Maintain the detailed explanation of this component in this dedicated notebook only.

## How we will add future entries

Record the topic, the user's requirements, ideas considered, agreed decisions, findings and evidence, difficulties, and remaining questions. Include code review outcomes when relevant. Keep proposals, choices, and verified results clearly distinguished.
