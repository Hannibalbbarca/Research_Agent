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

**Subsequent user response:** The user expects the person requesting research to provide a clear company name. Use this as the normal-path input assumption; see Discussion 5 below.

**Official website:** How will we establish that a domain belongs to the intended legal entity? Do not treat a search rank or similar company name as verification.

**Website coverage:** What does "all information" include: business pages, product pages, investor pages, reports, subsidiaries, news archives, careers, or dynamically generated content? Reading every reachable page may introduce duplication and substantial cost. A focused initial reading and a map of further sources is a possible alternative, not a selected replacement for the user's proposal.

**Evidence quality:** An official website is a useful first-party source. Its descriptions and management claims may still need financial or independent evidence. Record sources and unresolved points rather than turning all website text into established facts.

**Historical requests:** Today's website can provide current context. An explanation of a share-price fall three years earlier may require dated filings, announcements, prices, and other contemporaneous evidence. A contemporary account alone does not establish a historical cause.

**Stopping:** What amount of verified information is sufficient for the initial company profile? How will missing or inaccessible pages be represented?

These questions are recorded for later discussion; we will take them one at a time.

## Discussion 5 — Assume a clear company name in the normal flow

**User's position:** A person requesting company research should be conscious of which company they want to investigate and provide a sufficiently clear name.

**Working interpretation:** Proceed from the supplied company name without a mandatory identity-confirmation step. Ask for the name when missing, as already proposed. Actual conflicting evidence can be handled as an exception; do not make hypothetical ambiguity dominate the initial architecture discussion. This assumption does not itself establish that a discovered website is official.

**Next topic proposed by Codex:** Define the basic company understanding we want from the official website before deciding the extent of reading. A possible initial profile covers what the company sells, who and where it sells to, how it earns revenue, and links to investor information and reports. The scope remains open for discussion.

## Discussion 6 — Model knowledge versus web research

**User's question:** When ChatGPT is asked for a short overview of Vadilal Industries, does the model already contain that information, or does it search the web?

**Explanation:** Both paths are possible. A model may generate a broad description from patterns and information learned during training. This is not a live database lookup, and the generated description may be incomplete, stale, or wrong. The presence of a company in training does not establish that any particular fact or source is retained reliably.

ChatGPT is an application that can also provide a model with tools, including web search when available. A response may use prior knowledge, retrieved sources, or both. A general company-overview request does not guarantee web research. Search behaviour depends on the product mode, available tools, instructions, and routing. Search activity and cited sources help assess retrieval; fluent or confident writing is not evidence of a search or verification of every claim.

**Application distinction:** Connecting an Azure model does not automatically supply web search. Our program must provide and execute search or browser tools and return their results to the model.

**Architecture suggestion from Codex, not a selected policy:** Model knowledge can orient an initial investigation and suggest what to inspect. Treat the business profile used as research evidence as source-backed information with references and relevant dates. A generated overview and a verified company profile are different stages.

No live search or verification of Vadilal Industries was performed for this conceptual explanation.

## Discussion 7 — 16 October 2026: company and objective captured

**User-reported progress:** A local program now captures the company and the user's research objective in variables. The implementation has not been provided or independently reviewed here.

**Requested next stage:** Locate the company's official website and fetch relevant information.

**Proposed component boundary:** Accept the company and research objective; discover and inspect candidate official domains; choose pages relevant to the initial business profile and objective; return source-backed findings, discovered document links, and unresolved gaps.

**Website discovery:** Search can locate candidate domains even when search snippets alone were inadequate for report retrieval. Inspect legal-company, contact, and investor information rather than assuming the first search result or a model-generated URL is official. If the evidence remains inconclusive, retain an unverified outcome instead of silently proceeding as confirmed. This is website verification, not a mandatory repeat confirmation of a clear company name.

**Reading proposal:** Start with the business overview and relevant product/service pages. Discover investor-relations and report/archive links for further investigation. Let the research objective determine additional pages and required dates; current business descriptions do not by themselves explain historical share-price movements. Exhaustive crawling has not been selected.

**Proposed returned information:** Company name, official-site URL and identity evidence, business description, relevant findings with source URLs and dates where available, document/source links, pages examined, and missing or inaccessible information. Keep candidate links distinct from opened or verified documents.

**Immediate suggested milestone:** Return an evidence-supported official website and one source-backed business description. Broader page acquisition follows after checking this result. Browser Use remains an available earlier prototype option; the implementation choice for this new component is not yet confirmed.

No application code was edited, installed, or pushed in this discussion. Existing variable names and interfaces should be inspected before supplying integration code.

## Discussion 8 — 16 October 2026: request-intake script review

**Material supplied:** The user pasted the request-intake script, importing `client` and `DEPLOYMENT` from `azure_config`, and `ResearchRequest` from `research_request`. The script's filename was not provided. The imported files have not yet been supplied in this review.

**Observed structure:** Maintain a conversation; parse model responses into `ResearchRequest`; ask for clarification or present an understanding; keep a proposed company/objective tuple in `pending_values`; construct `confirmed_request` from that tuple after a model-reported approval; print the approved values. There are no research/search/browser calls in this pasted script.

**Architectural interpretation:** This is the request-intake stage. Its natural handoff is the `confirmed_request` object, whose `company_name` and `research_objective` fields can feed website discovery and relevant-page reading. Do not assume that a website tool already exists in the imported files.

**Confirmation behaviour requiring attention:** The active acceptance condition checks `request.user_confirmed` and the existence of `pending_values`. It does not require `request.ready_to_confirm`, nonempty current fields, or equality between current and pending values. Copying the pending pair intentionally preserves the proposal shown to the user, but the decision that the latest reply approves that proposal still depends on the model. A misclassified correction or approval concerning a changed request could therefore commit stale values. The commented-out stricter condition is inactive; exact equality has tradeoffs when the model rephrases a genuinely approved value. Review the schema and intended approval behaviour before choosing a fix.

**Integration consideration:** The conversation loop currently runs at module level. Importing this script would execute it. If it later becomes an imported component, a function boundary and entry-point handling will need consideration; no refactor is being made now.

**Other boundary:** A structured response helps constrain representation; it does not by itself establish correct interpretation of the user's intent. The `ResearchRequest` class is needed to assess its actual validation rules. API-error and refusal handling are not fully assessed from the pasted script alone.

**Next review input:** Ask for `research_request.py` and the client setup in `azure_config.py`, without secret values or the `.env` file. Then define the next component around the actual confirmed-request interface. This was a static review; no application code was executed, edited, or pushed.

## Decisions and open questions

**Confirmed:** Maintain the discussion record and examine the architecture incrementally. Set aside prior implementation choices as constraints on this design discussion.

**User proposal to explore:** Begin with company identification, official-site reading, initial business understanding, and discovery of further sources.

**Working input assumption:** The user supplies a clear company name; the normal flow does not require asking them to confirm it again.

**Latest milestone:** The user reports local company/objective capture and has provided its intake script for static review. The imported request schema and Azure configuration remain to be reviewed.

**Next step:** Design and connect website discovery and relevant-page reading to those inputs, starting with the official-site and business-description milestone. Define initial reading scope and source evidence as part of that work.

No new model, framework, crawler, storage technology, or application code was selected or implemented in this discussion.
