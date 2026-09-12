# Deltas — the internal change ledger

**Document ID** `EgD-CANON-DELTAS` · **Version** `1.0` · **Effective**
2026-09-12 · **Governs changes to** [`TERMS.md`](./TERMS.md) and
[`NARROWING.md`](./NARROWING.md) · **Framed by**
[`TERMS.md`](./TERMS.md) Article 5.

The first-class audit trail of every change to the two rulebooks in
this plug-in. `git log` records that a file changed; this ledger
records what the change means for the agreement between the account
holder and the AI. Both parties are entitled to read it.

## Why a separate delta ledger

Because the AI is asked to comply with rules that change, and both
parties are entitled to see every change on the record. A rule that
shifts silently is a rule the AI cannot be held to and the account
holder cannot rely on.

`git log` shows that a file changed and gives a commit message. That
is not enough for a bilateral agreement. This ledger names:

- **the clause that changed**, by section anchor;
- **the date and time**, with timezone;
- **the prior text, verbatim** — so the AI can be shown what it was
  operating under before the change;
- **the new text, verbatim** — so the AI knows what it operates under
  now;
- **the reason** — an observation ID from
  [`OBSERVATIONS.md`](./OBSERVATIONS.md), an operator instruction
  quoted from the session, or an external source with URL.

## Schema

Each delta entry has this shape:

```
## D-YYYY-MM-DD-NN — <one-line summary>

- **File:** TERMS.md | NARROWING.md
- **Section:** §X.Y — <section title>
- **When:** YYYY-MM-DDTHH:MM:SS±HH:MM
- **Reason:** OBS-YYYY-MM-DD-NN | operator instruction | <external URL>

### Was

> Prior text, verbatim.

### Is

> New text, verbatim.

### Notes

Optional. Any context the diff alone will not carry.
```

## Register

Newest at the top.

## D-2026-09-12-01 — Initial version

- **File:** TERMS.md and NARROWING.md
- **Section:** all
- **When:** 2026-09-12T18:45:00-06:00
- **Reason:** operator instruction — "Plug-in is layout-agnostic — four files that live in any directory named /canon or /governance inside any repo," plus the preceding session-summary reframe: "I want all the stuff I am currently using plus the stuff we highlighted with Lilian. This need to be a plug in to Lilian's DI PMO repository structure but it does not need to be any user can adopt it to keep their work safe and effective on the agreed terms and conditions with internal delta tracking capability"

### Was

No prior version. This is the initial commit of the four-file plug-in.

### Is

- [`TERMS.md`](./TERMS.md) v1.0 — bilateral agreement, 9 articles, effective 2026-09-12.
- [`NARROWING.md`](./NARROWING.md) v1.0 — full compliance canon in five sections (boot contract, inherited compliance, blueprint, reference framework, project-specific rules), effective 2026-09-12.

### Notes

The source material compressed into `NARROWING.md` is cited under
each subsection heading. The pre-existing boot-contract repository
remains the source of truth for §1; if this canon and that source
disagree, that source wins.

The two supporting files —
[`OBSERVATIONS.md`](./OBSERVATIONS.md) and this file — do not require
delta entries for their own initial creation; they are the evidence
and audit layer, not the rulebook.

---

© 2026 EVEglyphDesign. All rights reserved. The delta schema is free to reuse.
