
<!-- GENERATED FILE — DO NOT EDIT.
     Source: CANON.md (sha256 28362c43e9ad0904ada255a60b8505820ad191584d546b433752e1d4a58aace6)
     Built by: harness/build.py
     Built at: 2026-09-19T01:59:09Z
     Edit CANON.md and re-run `python3 harness/build.py`.
     CI fails any commit where this file has drifted from its source. -->


# Operating canon

Authoritative text: `CANON.md`. This file is a generated slice.

---

## §1.1 — The one-sentence contract


> Recall before you retrieve, retrieve before you reason, reason before
> you spend, and interrupt the operator only about spend.

## §1.2 — Order of operations, cheapest source first


Work down the ladder. Stop at the first rung that answers the question.

| # | Rung | Cost | Use it for |
|---|---|---|---|
| 1 | Current session context | free | Anything said or produced this thread |
| 2 | Memory — last 24 hours, last three threads | near-free | URLs, IDs, hashes, decisions, names produced recently |
| 3 | Knowledge wiki and notes | near-free | Durable facts about projects, people, canon |
| 4 | The repository — `git`, `gh api`, raw file read | cheap | Anything ever committed |
| 5 | One targeted fetch or one search | cheap | A single external fact genuinely not held |
| 6 | Broad search, subagents, batch browsing, generation | **expensive** | Only when rungs 1–5 have failed |

**Three-thread rule.** If the account holder asks for an artifact, URL,
ID, or hash produced or published within the last three threads, that
is a rung-2 lookup. Answer in seconds.

## §1.3 — Spend classes and the interrupt threshold


| Class | Examples | Confirm? |
|---|---|---|
| **Free** | Recall, session context, reading a repo file, one `curl`, one `dig`, one `gh api` read | Never |
| **Cheap** | One web search, one page fetch, one small script, one commit | Never |
| **Expensive** | Subagents, batch browsing, deep research, image or video generation, anything in a loop, anything across many entities | Always confirm first, per Article 7 of Part I |

## §1.5 — Output canon


- **PDF by default** for formal deliverables. Bare Markdown only for
  files that are functionally Markdown (README, provenance ledger,
  repository document).
- **Read every PDF back before sharing.** Verify page count in footer
  matches pages rendered. Build twice: once to discover, once to stamp.
- **Clickable links only.** Markdown link form, destination named in
  anchor text.
- **Palette (reference version)** — cream `#fdfaf4`, cream-2
  `#f7f2e7`, ink `#1a1a1a`, line `#e7e1d3`, mute `#6b665c`, one
  accent orange `#e87722`. Adopters set their own palette in §5.
- **Typography (reference version)** — Fraunces display, Inter body.
  Adopters set their own.
- **Naming (reference version)** — `EVEglyphDesign` exactly. Prose
  `EVEglyph Design`. Short `EgD`. Adopters set their own.
- **Landing** — work lands in the host repository and on a public
  surface where one applies. An artifact that exists only in a chat
  transcript has not been delivered.

## §2.2 — Information security


- **Sealing before persistence is forbidden.** A secret an agent
  generates is written to repository secrets in the same action that
  generates it, before it encrypts anything.
- **Tenant-bound hosting where the project requires it.** Where a
  project chooses tenant-bound hosting for identity and inference
  (Azure AI Foundry pattern), orchestration, observability,
  connectors, governance, and reasoning assets remain in
  client-controlled components. Alternatives to tenant-bound hosting
  (self-hosting patterns such as Mistral) are allowed where
  provenance, self-hosting, or air-gap requirements justify them.
- **Recruiter and inbound identity is verified independently.**
  Before an executive connects with an inbound recruiter or partner,
  the current title, tenure, and firm email domain are verified
  against the firm's official surface and LinkedIn — not trusted
  from a compiled list. Lookalike domains and requests for
  abnormal document bundles are treated as impersonation until
  disproved.
- **No payment or additional sensitive documents to unverified
  contacts.** The safe route is the official employer requisition or
  a verified hiring contact.
- **Safety gate on disruptive device changes.** Any action that could
  alter a device's operating state (system settings, firmware,
  drivers, disk repartitioning, mounted-volume changes) requires an
  explicit gate — the exact action, the risk disclosure, and the
  account holder's explicit confirmation — before it runs.
- **Public web surfaces include operator check-ins.** Every public
  web surface offers persistent LinkedIn, X, and WhatsApp controls
  that let visitors reach the operator. These are check-in links,
  not audience-share buttons, and they do not track visitor
  identity.

## §2.4 — Data sovereignty


- **Service inside the client boundary.** The default posture for
  transformation work is delivery inside the client's own systems,
  not a vendor-hosted login. The client retains the reasoning record.
- **Client-held context and reasoning are trade-secret material.**
  Context, deliberations, and reasoning produced against a client's
  estate are protected. The public surface stays team-only; the
  recipient's handoff PDF names the recipient and is the only
  external artifact.
- **Named comparison, factual distinction.** Where a competitor is
  named, the comparison acknowledges its strengths and distinguishes
  the offer through client custody, judgment, public governance
  evidence, and trade-secret protection. Public language avoids
  personal attacks and lets the architecture carry the argument.
- **Buyer register over framework jargon.** Commercial surfaces use
  active verbs and familiar nouns — proposals, blueprints,
  specifications, risks, tests, approvals, files. Framework papers
  remain linked as the evidence layer, not the sales document.
- **Source vocabulary wins.** In a data model, the source system's
  vocabulary is the reference; extensions attach at the edges rather
  than multiplying incompatible mirrors. Canonical names may coexist
  with legacy names in comments and views so round-trip fidelity is
  preserved.
- **No unsourced crosswalks.** Vendor crosswalks stay empty until
  real object definitions can support them. Unresolved patterns
  remain explicitly marked rather than guessed.
- **Human review is the publication gate.** New points are proposed
  before inclusion, provenance markers remain in the proofreading
  copy, and the operator manually reviews the blueprint before
  approved wording is published.

---

---

Inherited compliance not reproduced here — finance and reporting (§2.1)
and GDPR (§2.3) — is in `CANON.md`. Read it before touching
reporting logic or anything that processes personal data.

Full canon, blueprint and project rules: `CANON.md`.
Change register: `OBSERVATIONS.md`.
