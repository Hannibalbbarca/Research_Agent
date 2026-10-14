# Equity Research Agent — Architecture Discussion

Our notebook for the broader research-agent architecture, starting 14 October 2026. Record each substantive discussion, its reasoning, proposed alternatives, decisions, and unresolved questions. These are discussion notes, not evidence of implemented capabilities.

## How we will work

- Develop the architecture one small question at a time.
- Examine assumptions before selecting components or writing code.
- The user and Codex should question each other's ideas and reasoning.
- Use engineering explanations, define unfamiliar terms, and use concrete examples.
- Keep user proposals, Codex suggestions, and agreed decisions distinguishable.
- Preserve earlier discussions when an idea changes; record what changed and why.
- Keep implementation on hold while discussing this broader architecture. The user writes application code locally; Codex maintains the documentation.

The three summary files retain their roles: [IDEAS.md](IDEAS.md), [TOOLS.md](TOOLS.md), and [PROGRESS.md](PROGRESS.md). Detailed information-acquisition experiments remain in [DOCUMENT_AGENT.md](DOCUMENT_AGENT.md).

## Discussion 1 — How human equity research works

**Starting question:** How does a human researcher investigate a company, decide what to read next, test hypotheses, retain useful findings, and change direction?

**Initial explanation from Codex:** Equity research connects an understanding of the business, expectations about its future, uncertainty, and the price paid for ownership. A research process may move through questions, competing explanations, evidence gathering, evaluation, and a judgment that can be revisited.

A hypothesis is a provisional explanation that evidence can support or weaken. For example, fictional revenue growth might reflect volume, pricing, acquisitions, or temporary demand. These possibilities should be distinguished rather than treating a single explanation as established.

**Important boundary:** This was an illustrative explanation, not an agreed fixed research workflow. The user requested a slower discussion that examines the assumptions behind each step.

## Discussion 2 — Meta-reasoning

**User's focus:** Understand the reasoning that directs the research itself.

**Working definition:** Research reasoning evaluates a business question; meta-reasoning decides which question to investigate, what evidence to seek, how much effort to spend, whether to change direction, and when the evidence is sufficient for the intended decision.

**Considerations proposed by Codex:**

- How much resolving the question could change the investment judgment.
- What remains uncertain and the strength of existing evidence.
- Whether the proposed investigation is likely to distinguish competing explanations.
- The time, effort, and monetary cost of the investigation.

An unexpected finding can justify continuing the current investigation, changing direction, deferring a question, or opening a separate investigation. The trigger for choosing among these remains unresolved.

**Potential architecture implications, not selected components:** Maintain the objective, questions, hypotheses, source-backed evidence, contradictions, assumptions, pending investigations, and reasons for priority changes. A controller could use this state to choose the next action. Neither the implementation nor the number of agents has been decided.

## Discussion 3 — How do we know what business the company is in?

**User's challenge:** The ice-cream example assumed the analyst already knew the company's business. How was that established?

**Correction:** Codex had skipped the identity and business-understanding step. For a company-specific request, identify the actual company and inspect evidence about what it does.

Possible evidence includes the official website's business overview, the annual report's business description, and segment/revenue disclosures in financial statements.

**Distinction to preserve:** A company selling ice cream does not establish that ice cream is its primary business. Revenue or segment information helps determine economic importance. Company names, familiar brands, and search snippets provide clues, not sufficient confirmation.

## Discussion 4 — User's proposed first stage

**User request:** Record our discussions from now on.

**User's proposal:**

1. A user might ask for general research on a company or a specific investigation, such as why its share price fell three years earlier.
2. Obtain the company name from the request. If it is missing, the LLM asks the user for it.
3. Go to the company's official website.
4. Read all information there about the company to establish basic company knowledge.
5. The website may also provide annual-report links and other sources useful for later research.

**What this proposal is intended to achieve:** Give the researcher initial business context and discover further research sources before deeper analysis.

**Status:** Proposed first stage. Exhaustive website reading, its implementation, and whether it should precede every type of request have not been agreed or tested.

### Assumptions to examine next

**Identity:** A company name may refer to multiple entities, a brand, a parent, or a subsidiary. Having a name does not always identify the listed company being researched. Codex proposes resolving ambiguity before associating a website or financial information with the company; this is not yet a finalized rule.

**Official website:** How will we establish that a domain belongs to the intended legal entity? Do not treat a search rank or similar company name as verification.

**Website coverage:** What does "all information" include: business pages, product pages, investor pages, reports, subsidiaries, news archives, careers, or dynamically generated content? Reading every reachable page may introduce duplication and substantial cost. A focused initial reading and a map of further sources is a possible alternative, not a selected replacement for the user's proposal.

**Evidence quality:** An official website is a useful first-party source. Its descriptions and management claims may still need financial or independent evidence. Record sources and unresolved points rather than turning all website text into established facts.

**Historical requests:** Today's website can provide current context. An explanation of a share-price fall three years earlier may require dated filings, announcements, prices, and other contemporaneous evidence. A contemporary account alone does not establish a historical cause.

**Stopping:** What amount of verified information is sufficient for the initial company profile? How will missing or inaccessible pages be represented?

These questions are recorded for later discussion; we will take them one at a time.

## Decisions and open questions

**Confirmed:** Maintain the discussion record and examine the architecture incrementally. Set aside prior implementation choices as constraints on this design discussion.

**User proposal to explore:** Begin with company identification, official-site reading, initial business understanding, and discovery of further sources.

**Next question:** If the supplied company name matches more than one entity, how should the system establish which company the user means?

No new model, framework, crawler, storage technology, or application code was selected or implemented in this discussion.
