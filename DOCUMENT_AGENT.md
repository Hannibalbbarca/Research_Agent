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
- The main research agent should be able to delegate document preparation through one request rather than managing each download and parsing step.
- Persist prepared documents and parsed results for reuse, avoiding repeated downloads and parsing when a suitable saved result already exists.
- The document component must check parsing quality and report problems before its output is treated as reliable research input.

The exact agent framework, libraries, supported document types, and output format have not been chosen. Calling this a pipeline, agent, or sub-agent does not settle its architecture.

## Example we are working toward

A user requests a company's report for a particular financial year. The component locates the requested document, downloads it, and returns parsed content that the research system can use.

The spoken example was transcribed as "Wadilal." The exact company, year, and report type have not been confirmed. Annual-report PDFs were suggested as a possible starting point, but the user has not yet confirmed that scope.

## Proposed flow — still open for discussion

1. **Understand the request:** Identify the company, document type, and financial year.
2. **Check saved results:** Reuse a matching prepared document if its version and extraction quality meet the request.
3. **Find candidates when needed:** Locate possible documents, preferably from official or authoritative sources.
4. **Fetch and inspect:** Download the file and check whether it matches the request. Initial extraction may be needed to inspect its contents.
5. **Parse:** Use Python to extract the agreed content from the matching document.
6. **Check extraction quality:** Evaluate completeness and relevant extraction checks; retry or flag failures rather than silently accepting the output.
7. **Save and return:** Retain the original document, parsed content, metadata, source references, and validation results for future reuse. Return a usable result to the caller.

This is a proposal to discuss, not an implemented or tested design.

## Persistent document preparation

**User's requirement:** Avoid making the main research agent repeatedly download and parse the same report, spending resources and context on document preparation. The document agent should own that work and verify the parsing result.

**Two proposed paths:**

- **Already prepared:** Identify the matching stored document, check its preparation status and version, and return access to the existing result.
- **Not prepared or unsuitable:** Find and download the document, parse it, evaluate the extraction, save the outcome, and return its status and usable content.

**Proposed retained information:** A stable document identifier; company identity and reporting period; source URL and retrieval time; original file and file hash; parser version; page-linked extracted content; and validation findings. Storage technology is still undecided.

**Reuse needs boundaries:** A corrected report, changed document contents, or necessary parser upgrade may justify reprocessing. The freshness policy is still open. Store unsuccessful or partial outcomes with their true status; do not mark them as verified reusable results.

**Context-saving proposal:** Persistence avoids repeated preparation, but returning the entire parsed report on every call would still consume the main agent's context. Consider returning a document identifier and compact metadata first, with access to specific pages or sections when needed. The exact retrieval interface remains undecided.

## What parsing verification should mean

Correct-document verification and extraction-quality verification are different checks. The first asks whether the file is for the requested company, period, and document type. The second asks whether the parsed representation faithfully captures the required content.

**Candidate checks, not yet selected or tested:**

- Account for every page and explicitly flag unreadable or image-only pages.
- Inspect suspiciously empty or garbled extraction and identify missing sections.
- Where financial tables are required, check row/column associations, numbers, signs, units, and period labels against the original document.
- Retain page references so important extracted values can be checked against the source.
- Return validation findings and distinguish usable results, partial results, failures, and cases needing review.

A parser completing without an exception does not prove extraction accuracy. Automated checks provide evidence within their coverage; they cannot guarantee every passage and financial figure is correct. Validation thresholds, fallback methods, and human-review criteria remain to be discussed.

## Questions we still need to answer

- Which document types should the first version support?
- How should we identify the correct company and financial-year period?
- What should the retrieval agent decide, and what should ordinary code handle?
- Does parsing need text, tables, or both? Do scanned documents belong in the first version?
- What output should the main research agent receive, and how should it call this component?
- What should happen when a document is missing, ambiguous, inaccessible, or only partly readable?
- When should a saved document be refreshed or reprocessed?
- Which extraction checks must pass before content is usable for research?
- Should the main agent receive a full parsed document, a document reference, or selected sections on demand?

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
- Reusing stored results without overlooking corrected documents or unreliable extraction.
- Reducing the main agent's context usage as well as avoiding repeated processing.

## Code review notes

No application code has been submitted for review yet. When the user writes a component, record the version reviewed, findings, reasoning, and follow-up outcomes here.

## Discussion log

### 6 October 2026 — Dedicated focus and notebook agreed

**User's direction:** Focus on the document retrieval and parsing component for the next five to six days, and create a separate Markdown file for its discussions and discoveries.

**Decision:** This file is the detailed notebook for that work. [IDEAS.md](IDEAS.md) remains the overall project notebook; [PROGRESS.md](PROGRESS.md) records project-wide challenges and achievements.

**Current state:** Discussion only. The user is still explaining the requirements.

**Follow-up clarification:** Keep the three original files in their existing roles, making necessary updates as work progresses. Maintain the detailed explanation of this component in this dedicated notebook only.

### 6 October 2026 — Persistent preparation and parsing verification

**User's reasoning:** A research agent needs many documents. Repeating document downloads and parsing wastes resources and context, so document preparation should be delegated to a dedicated reusable component.

**Requested behavior:** The main agent asks for a company's report for a specified financial year. The document component locates relevant sources, downloads the report when necessary, parses it with appropriate tools, and checks whether parsing was done correctly. Prepared results should remain available for reuse.

**Example clarification still open:** The spoken company was transcribed as "Wadilal," and the period as "2024, 2025." Confirm the legal entity and whether the request means FY 2024–25 or separate reports before treating this as a concrete test case.

**Proposals added:** Persistent storage with document and parser version tracking; separate checks for document identity and extraction quality; and on-demand access to sections to reduce context usage.

**Status:** Requirements discussion. No storage, retrieval, parsing, or validation behavior has been implemented or tested.

## How we will add future entries

Record the topic, the user's requirements, ideas considered, agreed decisions, findings and evidence, difficulties, and remaining questions. Include code review outcomes when relevant. Keep proposals, choices, and verified results clearly distinguished.
