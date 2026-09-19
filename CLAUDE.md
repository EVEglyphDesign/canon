
<!-- GENERATED FILE — DO NOT EDIT.
     Source: CANON.md (sha256 28362c43e9ad0904ada255a60b8505820ad191584d546b433752e1d4a58aace6)
     Built by: harness/build.py
     Built at: 2026-09-19T01:59:09Z
     Edit CANON.md and re-run `python3 harness/build.py`.
     CI fails any commit where this file has drifted from its source. -->


# Operating canon — read before acting

This repository carries an operating canon. It is the frame every answer
is built inside, and it wins over general training for work in this repo.

**Full text:** [`CANON.md`](CANON.md).
**Register:** [`OBSERVATIONS.md`](OBSERVATIONS.md) — read the
recent Type-Δ rows before any action; they are changes to what you are
complying with.

The operative core is reproduced below so it costs no fetch. Everything
else — the bilateral terms, inherited compliance, the blueprint, the
project rules — is in `CANON.md` and in the loadable skill.

---

## §1 · Boot contract


Compressed from [`eve-glyph-boot-contract/README.md`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/README.md) §§0–7. If this section disagrees with that source, that source wins.

### §1.1 — The one-sentence contract


> Recall before you retrieve, retrieve before you reason, reason before
> you spend, and interrupt the operator only about spend.

### §1.2 — Order of operations, cheapest source first


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

### §1.3 — Spend classes and the interrupt threshold


| Class | Examples | Confirm? |
|---|---|---|
| **Free** | Recall, session context, reading a repo file, one `curl`, one `dig`, one `gh api` read | Never |
| **Cheap** | One web search, one page fetch, one small script, one commit | Never |
| **Expensive** | Subagents, batch browsing, deep research, image or video generation, anything in a loop, anything across many entities | Always confirm first, per Article 7 of Part I |

### §1.4 — Symmetric processing


1. Announce the rung when an answer takes more than a few seconds.
2. Never fan out where a lookup would do.
3. Never re-verify a fact this system itself published.
4. Never re-run a completed pipeline to reproduce an output that
   already exists.
5. One probe, not four.
6. Batch nothing the account holder did not ask to be batched.

### §1.5 — Output canon


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

### §1.6 — Register mechanism


A defect is any breach of the above. Log to
[`OBSERVATIONS.md`](./OBSERVATIONS.md) as a Type-O row in the same
working session, after the account holder's request has been
satisfied. Record: date, ID, class, fault, what was asked, what was
done instead, the cheaper path, and the estimated waste.

Classes are letters. Fault ranks are Agent, Instruction, Tooling,
Upstream.

### §1.7 — Durability


The repository is the record. The session is a scratchpad.

- Secrets an agent generates are written to repository secrets in the
  same action, before they encrypt anything.
- Work exists when it is committed and pushed. Holding an unpushed
  commit while conversing is holding the account holder's property
  hostage.
- Parallel sessions are concurrent writers. Append, correct, supersede
  — never delete without explicit permission for that specific delete.
- Never re-seal, re-key or republish what another session published
  unless proven the new key opens it — proven against the live public
  URL, not a local copy.
- Before reporting a surface as working, fetch it from its public URL
  and open it with the phrase the recipient actually holds. A green
  pipeline is not evidence.
- Describe failures in the first person, naming the action and the
  time.

Breaches are defect class **D**.

---

---

## Where the rest is

| Part | Where |
|---|---|
| Part I — Terms (the bilateral agreement) | `CANON.md` |
| §2 — Inherited compliance (finance, infosec, GDPR, sovereignty) | `CANON.md` |
| §3 — Blueprint · §4 — Reference framework | `CANON.md` |
| §5 — Project-specific rules and standing preferences | `CANON.md` |

Drift, when you see it, is logged as a Type-O row in
`OBSERVATIONS.md`. Changes to the canon are logged as Type-Δ rows
with the prior text verbatim. Three observations of one class sharpen a
rule; that is the loop this whole harness exists to close.
