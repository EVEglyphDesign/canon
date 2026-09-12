# canon — the plug-in

Four files that drop into any repository's `/canon` or `/governance`
directory and give the AI surface a safe, effective operating shape on
the agreed terms and conditions between the account holder and the AI.

Layout-agnostic. Any host repository. Any project management office.
Any user.

## The four files

| File | What it holds | Read priority |
|---|---|---|
| **[`TERMS.md`](./TERMS.md)** | The bilateral operating agreement. What the account holder and the AI have agreed to. The frame every other file operates inside | 1 — read first |
| **[`NARROWING.md`](./NARROWING.md)** | The canon. Every rule the AI is expected to comply with while working on this account — boot contract, finance and reporting, information security, GDPR, data sovereignty, delivery and communication rules, project-specific additions | 2 — read second, before acting |
| **[`OBSERVATIONS.md`](./OBSERVATIONS.md)** | The evidence base. Every observation of the AI's operation from the account holder's perspective, tagged by class and fault rank. Individual rows may drift; the aggregate is what matters | 3 — reference, cited by rules in `NARROWING.md` |
| **[`DELTAS.md`](./DELTAS.md)** | The internal delta ledger. Every change to `TERMS.md` and `NARROWING.md` recorded with what changed, when, why, and what the previous version said. This is what keeps the agreement live | 4 — audit trail, read when a rule is questioned |

## How the plug-in works

1. **Drop the four files into `<host-repo>/canon/` or `<host-repo>/governance/`**. Whichever the host repo names its policy directory.
2. **Point the project's AI surface at `TERMS.md` and `NARROWING.md`** as its first reads. "Read `canon/TERMS.md` first, then `canon/NARROWING.md`, before any action" is enough of an instruction.
3. **When the AI drifts, log a row in `OBSERVATIONS.md`.** Class, fault, what was asked, what was done, cheaper path, waste. Individual rows can be sloppy; the aggregate is what changes the canon.
4. **When the account holder changes a term or a rule, log the change in `DELTAS.md`.** What clause changed, from what to what, on what date, and which observation authorised the change (or "operator instruction" if it was direct). The delta ledger is what makes the agreement bilateral — the AI is entitled to see every change to what it is complying with, on the record.

## Why four files instead of two

The sovereign-starter kit ships as two files —
[`NARROWING.md`](https://github.com/EVEglyphDesign/sovereign-starter/blob/main/NARROWING.md)
and
[`OBSERVATIONS.md`](https://github.com/EVEglyphDesign/sovereign-starter/blob/main/OBSERVATIONS.md) —
for practitioners starting from scratch. The two-file shape works at
any scale.

The plug-in adds two more because a project-scale deployment needs
what a scratchpad does not:

- **`TERMS.md`** is separated from `NARROWING.md` because the agreement
  frame is stable while the rules underneath it accrete. The AI reads
  `TERMS.md` once per session; it reads `NARROWING.md` continuously.
- **`DELTAS.md`** is separated from `git log` because a project canon
  needs a first-class audit trail — human-readable, keyed to the clause
  that changed, and citing the observation that authorised the change.
  `git log` records that a file changed; `DELTAS.md` records what the
  change means for the agreement.

## Adopting the plug-in

Any user can adopt the plug-in whole, or copy the four files into a
host repository and edit them freely. The kit does not require
attribution or a link back — the licence is at
[`LICENSE.md`](./LICENSE.md).

The reference version in this repository (`EVEglyphDesign/canon`) is
maintained as one worked example — the plug-in as EVEglyphDesign
operates it today, with every clause traceable to the source repository
it compresses. New adopters can copy this version and edit, or start
from the two-file kit and grow into the four-file shape.

## Source provenance

Every clause in this repository's `NARROWING.md` traces to one of:

- [`eve-glyph-boot-contract`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract) — the binding boot contract and observations register.
- The wiki knowledge index at `memory/knowledge/projects/` — specifically the pages for `eve-liliantwin-pmo`, `lilian-executive-positioning`, `lillian-sovereign-workspace`, `epiq-delivery-control`, `eat-happy-hana-consolidation`, `eve-datasphere-sovereign`, and `eve-glyph-boot-contract`.
- The wiki knowledge index at `memory/knowledge/preferences/` — the 20-odd standing preferences the account holder has established.

Each clause carries a source anchor. Nothing has been invented in the
account holder's name.
