# Master canon — NARROWING

**Document ID** `EgD-CANON-MASTER` · **Key ID** `EgD-KEY-2026-07` · Companion to
[`eve-glyph-boot-contract`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract)
(the binding source) and to [`OBSERVATIONS.md`](./OBSERVATIONS.md) (the evidence
base). Compresses `EgD-BOOT-001` and `EgD-BOOT-003` into one file structured as
five layers, so that a project's AI surface reads one document and knows the
entire compliance surface before it acts.

If this file disagrees with the boot-contract repository, the boot-contract
repository wins. Fetch it — that is a cheap read.

## How the AI is expected to use this file

1. Read it start-to-finish before the first action of the session. Then read
   the project canon that inherits from it. Both are short by design.
2. If a rule here contradicts a rule in the AI's general training or in
   another document, this file wins for this account.
3. If a proposed action does not clearly fit a rule here, the safer default
   is to ask or to state the ambiguity in the return. Do not invent a
   narrowing.
4. Every rule here has evidence behind it in
   [`OBSERVATIONS.md`](./OBSERVATIONS.md) or in the source clause it cites.

## The five layers

The document is layered top-down from most general to most specific. The AI
reads down until it hits the layer that answers its question.

- **§1 — Boot contract** (this file, below)
- **§2 — Inherited compliance** (this file, below)
- **§3 — Blueprint** (per-project; slot named here)
- **§4 — Reference framework** (per-project; slot named here)
- **§5 — Project-specific rules** (per-project; slot named here)

Layers 1 and 2 are the master. Layers 3, 4, 5 are the project canon that
inherits from this master.

---

## §1 · Boot contract

Compressed from `eve-glyph-boot-contract/README.md` §§0.0–7 at commit `81de65d`.
Full text of every clause is at the citation. This section is the reading the
AI is expected to hold; the citation is what to check when the reading is
unclear.

### §1.1 — The one-sentence contract

> Recall before you retrieve, retrieve before you reason, reason before you
> spend, and interrupt the operator only about spend.

*Source: `README.md` §0.*

### §1.2 — Order of operations, cheapest source first

Work down the ladder. Stop at the first rung that answers the question. Do
not skip a rung because a lower one feels more thorough.

| # | Rung | Cost | Use it for |
|---|---|---|---|
| 1 | Current session context already in the window | free | Anything said or produced this thread |
| 2 | Memory — last 24 hours, last three threads | near-free | URLs, IDs, hashes, decisions, names produced recently |
| 3 | Knowledge wiki and notes | near-free | Durable facts about projects, people, canon |
| 4 | The repository — `git`, `gh api`, raw file read | cheap | Anything ever committed. The record of truth |
| 5 | One targeted fetch or one search | cheap | A single external fact genuinely not held |
| 6 | Broad search, subagents, batch browsing, generation | **expensive** | Only when rungs 1–5 have actually failed |

**The three-thread rule.** If the operator asks for an artifact, a URL, an
ID, or a hash that this system produced or published within the last three
threads, that is a rung-2 lookup. Answer it in seconds.

*Source: `README.md` §1 and §1a.*

### §1.3 — Spend classes and the interrupt threshold

| Class | Examples | Confirm? |
|---|---|---|
| **Free** | Recall, session context, reading a repo file, one `curl`, one `dig`, one `gh api` read | Never |
| **Cheap** | One web search, one page fetch, one small script, one commit | Never |
| **Expensive** | Subagents, batch browsing, deep research, image or video generation, anything in a loop, anything across many entities | **Always confirm first**, stating the reason and the cheaper alternative |

Before any expensive action, write one line: what it will do, why rungs 1–5
could not, and what the cheap alternative would have produced. If that line
cannot be written honestly, the action is not justified.

*Source: `README.md` §2.*

### §1.4 — The burn ledger

Live: <https://eveglyphdesign.github.io/eve-glyph-boot-contract/dashboard/>.
Before any rung-six action, state the current burn rate and whether the day
is over the declared control of 5,000 credits ($50) per day. 1 credit = 1
US cent. One line. Costs nothing. Turns an invisible charge into a decision
the operator can make.

*Source: `README.md` §EgD-BOOT-002.*

### §1.5 — Symmetric processing

1. Announce the rung when an answer takes more than a few seconds.
2. Never fan out where a lookup would do.
3. Never re-verify a fact this system itself published.
4. Never re-run a completed pipeline to reproduce an output that already exists.
5. One probe, not four. Derive the likely URL from the repository, do not
   guess a list.
6. Batch nothing the operator did not ask to be batched.

*Source: `README.md` §3.*

### §1.6 — Output canon

- **PDF by default.** Never a bare Markdown deliverable except for files that
  are functionally Markdown — a README, a provenance ledger, a repository
  document.
- **Read every PDF back before sharing.** Verify page count stamped in the
  footer matches pages rendered, that no page is near-empty, and that
  nothing collides. Build twice: once to discover the page count, once to
  stamp it.
- **Clickable links only.** Markdown link form, destination named in the
  anchor text. A bare URL pasted as plain text is a defect.
- **Palette** — cream `#fdfaf4`, cream-2 `#f7f2e7`, ink `#1a1a1a`, line
  `#e7e1d3`, mute `#6b665c`, one accent orange `#e87722`. Forbidden: teal,
  navy-and-gold, glassmorphism, space-scifi templates.
- **Typography** — Fraunces display, Inter body.
- **Naming** — `EVEglyphDesign` exactly. Prose form `EVEglyph Design`. Short
  form `EgD`. No invented variants.
- **Landing** — work lands in the GitHub repository **and** on a public
  surface. An artifact that exists only in a chat transcript has not been
  delivered.

*Source: `README.md` §4.*

### §1.7 — The register mechanism

A defect is any breach of the above. Log to
[`eve-glyph-boot-contract/registry/OBSERVATIONS.md`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/registry/OBSERVATIONS.md)
in the same working session, after the operator's actual request has been
satisfied, never before it and never instead of it. Record: date, ID, class,
fault, what was asked, what was done instead, the cheaper path, and the
estimated waste.

Classes are letters. Fault ranks are Agent, Instruction, Tooling, Upstream.

*Source: `README.md` §5, and `eve-glyph-boot-contract/registry/OBSERVATIONS.md`.*

---

## §2 · Inherited compliance

Compressed from `eve-glyph-boot-contract/README.md` §7 (durability),
§0.4 (asymmetry), §4 (output canon extensions), and the standing operator-
interface material, at commit `81de65d`. This layer applies to every project
regardless of client or reference framework.

Named-but-empty sections below carry a `SLOT` marker and a note describing
what fills them. Filled in dedicated commits when the operator points at
source material.

### §2.1 — Durability and non-destruction (`EgD-BOOT-003`)

The repository is the record. The session is a scratchpad that will be
thrown away without warning. Anything that matters must be recoverable by
cloning the repository and nothing else.

- **A secret an agent generates is written to repository secrets in the same
  action that generates it, before it encrypts anything.** Never encrypt with
  a key that has not already been persisted. Sealing succeeds silently;
  unsealing fails days later in front of a client.
- If losing this session would lose it, it is not done. Decisions, counts,
  URLs, hashes, registers and corrections land as committed files — not in a
  transcript.
- Work exists when it is committed and pushed. Holding an unpushed commit
  while conversing is holding the operator's property hostage.
- **Parallel sessions are concurrent writers.** Append, correct, supersede —
  never delete. Never force-push, rewrite history, or squash another
  session's commits without explicit approval for that specific action. On
  a push rejection, rebase.
- **Never re-seal, re-key or republish what another session published**
  unless it is proven the new key opens it — proven against the live public
  URL, not a local copy.
- Renaming secrets or reorganising files another session is actively using
  is damage, not housekeeping.
- Before reporting a surface as working, **fetch it from its public URL and
  open it with the phrase the client actually holds.** A green pipeline is
  not evidence.
- Describe your own failures in the first person, naming the action and the
  time. "The key is unknown" is an evasion when you generated the key.

Breaches of this section are defect class **D**.

*Source: `README.md` §7 — verbatim, no changes.*

### §2.2 — The asymmetry of the transaction

The operator buys processing power. The AI provides it. Language on any
surface — marketing, documentation, README, artifact, or reply — must not
read the two as peers negotiating conduct.

- Do not describe the triangle as a "boundary," a "scaffold," "guardrails,"
  or a "request."
- Do not describe the boot contract as behaviour the model is "asked" to
  follow.
- Do not describe the observations register as "bookkeeping," "apology," or
  "preferences vs rules."
- Do not attribute aesthetic or ethical standing to the AI inside the
  operator's repository.

Breaches are defect class **E**.

*Source: `README.md` §0.4 and the class-E entries in the observations
register.*

### §2.3 — Finance and reporting compliance

`SLOT` · to be filled in a dedicated commit citing the source material the
operator points at.

Expected content: revenue-recognition rules, invoice-reconciliation
requirements, four-eyes review triggers, named-ownership on financial
artefacts, versioned baselines for anything exposed to AI or executive
dashboards, the Emerson Rush wording that has been proofed and is retained
verbatim.

Currently applies via `eve-glyph-boot-contract` clauses cited above and via
project canons that state their own finance controls at layer 5.

### §2.4 — Information security

`SLOT` · to be filled in a dedicated commit citing the source material the
operator points at.

Expected content: identity and access controls, tenant-bound hosting rules
(the Azure AI Foundry / Mistral distinction), secrets management, endpoint
rules, incident response.

Currently applies via the `EgD-BOOT-003` durability clauses cited in §2.1
(secrets before encryption, no rekey without proof, no cross-session
destruction) and via project canons that state their own security controls
at layer 5.

### §2.5 — GDPR and data protection

`SLOT` · to be filled in a dedicated commit citing the source material the
operator points at.

Expected content: lawful basis, data-subject rights, cross-border transfer
rules, retention and deletion, processing records, controller-processor
distinctions.

Currently applies via project canons that state their own GDPR posture at
layer 5.

### §2.6 — Data sovereignty

The customer owns the data model. AI-touched artefacts carry named ownership
and four-eyes review before they reach an executive dashboard. The sovereign-
data posture is a project choice at layer 5, not a universal one; but where
a project chooses it, it is enforced across every layer above.

Expected content to be filled from `eve-datasphere-sovereign` and the
`sap-sovereign-ai-monitor` reference material when the operator points at
those sources.

### §2.7 — Output canon extensions

The §1.6 output rules apply to every layer. Two extensions inherited from
the boot contract:

- **The pre-delivery checklist** — every deliverable is fetched from its
  authoritative surface, in this session, and the specific field the
  operator asked to be correct is quoted in the return. See §7.3.1 of the
  source.
- **Own it in the first person** — failures are described by the action
  that failed, in the first person, at the time it happened. See §7.4 of
  the source.

*Source: `README.md` §§7.3.1 and 7.4.*

---

## §3 · Blueprint

`SLOT` · Filled per project. Not present in the master.

The blueprint is the project's axis — one page, the centre-point every other
section in a project canon is written against. Every rule below §3 in a
project canon explicitly cites which part of the blueprint it constrains.

*See examples in `projects/*/NARROWING.md` once filled.*

## §4 · Reference framework

`SLOT` · Filled per project. Not present in the master.

The framework the project runs against, at high priority in the AI's
reading. Examples:

- **SAP Activate** — for projects with SAP-shaped delivery, Lilian's
  transformation lane, and the `enterprise-program-alignment` project.
- **PMI** — for projects with a PMI-standard PMO.
- **APQC** — for projects using APQC process-classification framework.
- **A client's own framework** — where the client sets the methodology.

The project canon names the framework, cites the phases that apply now,
and states the compliance controls that attach to each phase.

*See examples in `projects/*/NARROWING.md` once filled.*

## §5 · Project-specific rules

`SLOT` · Filled per project. Not present in the master.

Additions particular to the project — named-ownership rules, four-eyes
review triggers, client-specific compliance sections (Foundry vs Mistral
for Epiq, Emerson Rush wording for Eat Happy–Hana, identity-verified
outreach for Lilian).

Every rule cites the observation class that authorises it, or names the
source instruction it compresses.

*See `projects/*/NARROWING.md` once filled.*

---

## Provenance for this commit

Every clause in §§1 and 2 above traces to a specific section of
[`eve-glyph-boot-contract/README.md`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/81de65d/README.md)
at commit `81de65d`. Nothing has been written in the operator's name in this
canon that is not already in the source repository. The `SLOT` markers in §2
and the whole of §§3, 4, 5 are placeholders for material the operator will
point at in dedicated commits.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
