# Observations — the evidence base and the change ledger

**Document ID** `EgD-CANON-OBSERVATIONS` · **Version** `1.2` ·
**Effective** 2026-09-12 · **Framed by** [`CANON.md`](./CANON.md) ·
**Governs changes to** [`CANON.md`](./CANON.md).

This is the shareable file of the plug-in. It travels between
contexts; the rules in `CANON.md` stay with the account.

The evidence base for the AI's operation *and* the change ledger for
the rulebook. One register, two shapes of row. Individual rows may
drift; the aggregate is what matters — the pattern will not lie.

## Why one register instead of two

Every rule change begins as an observation. Either the account holder
observed drift and wrote a rule to close it; or the account holder
observed that a standing rule no longer fits and rewrote it; or an
external source (regulation update, framework revision) added a
constraint the register needed to record. In every case the register
is the trigger.

A separate delta ledger split the same event across two files and
asked the reader to reconcile them. This file collapses that back:
one row, one event, one place to look.

`git log` still records that a file changed. This register records
what the change *means* for the agreement.

## Two shapes of row

**Type O — observation of drift.** The AI's work put something on the
account holder's plate that it should not have, or the AI caught its
own miss. One row, class, fault, cheaper path, waste. The account
holder logs when the AI's work costs them; the AI logs when it
catches its own miss, in the same working session as the deliverable,
after the account holder's request has been satisfied.

**Type Δ — observation of change.** A clause in `CANON.md` changed. One row, section anchor, prior text verbatim,
new text verbatim, reason. The reason is either an O-row ID from
above (three of the same shape stacking up produced the rule), an
operator instruction quoted from the session, or an external source
named at its URL.

Rows are appended in reverse chronological order (newest first).
Existing rows are never rewritten; corrections come as a new row
that cites the earlier row's ID.

## Classes (for Type O rows)

Letters. Extend the list when a genuinely new class arises; keep
existing letters stable.

- **A** — artwork or copyright fidelity breach
- **B** — bilingual or translation gap
- **C** — canon breach (output rules, palette, naming, typography)
- **D** — durability (unpushed commit, transient key, lost secret)
- **E** — evidence gap (claim exceeds source)
- **F** — framework misapplication
- **H** — handoff shape (multiple files where one was asked, wrong container)
- **I** — interrupt over a free action
- **L** — link or format (plain URL, unclickable, wrong surface)
- **P** — provenance (missing anchor, unnamed source)
- **R** — retrieval waste (fan-out where lookup would do; cold start)
- **S** — unconfirmed spend (expensive action without gate)
- **T** — tooling misuse
- **U** — under-reading the ask
- **V** — verbatim wording altered
- **X** — private data crossed a boundary

## Fault ranks (for Type O rows)

- **Agent** — the AI made the error under conditions where it could
  have avoided it by reading, recalling, or asking.
- **Instruction** — the ask was ambiguous or contradictory in a way
  the AI could not have resolved on its own.
- **Tooling** — a tool, connector, or model behaved outside its
  documented shape.
- **Upstream** — a source of truth was wrong or missing.

Fault ranks the responsibility. The row still counts as an
observation either way.

## Type O schema (drift)

```
| Date       | ID                | Class | Fault  | Asked                     | Done instead              | Cheaper path             | Waste (est.) |
|------------|-------------------|-------|--------|---------------------------|---------------------------|--------------------------|--------------|
| YYYY-MM-DD | OBS-YYYY-MM-DD-NN | X     | Agent  | one line                  | one line                  | one line                 | credits or $ |
```

## Type Δ schema (change)

Type-Δ rows do not fit a table cleanly (verbatim text before and
after is often long), so they take a block form under the register
table:

```
### Δ-YYYY-MM-DD-NN — <one-line summary>

- **File:** TERMS.md | NARROWING.md
- **Section:** §X.Y — <section title>
- **When:** YYYY-MM-DDTHH:MM:SS±HH:MM
- **Reason:** OBS-YYYY-MM-DD-NN | operator instruction | <external URL>

#### Was

> Prior text, verbatim.

#### Is

> New text, verbatim.

#### Notes

Optional. Any context the diff alone will not carry.
```

## Register — Type O (drift)

Newest first.

| Date | ID | Class | Fault | Asked | Done instead | Cheaper path | Waste (est.) |
|---|---|---|---|---|---|---|---|
| 2026-09-12 | OBS-2026-09-12-04 | U | Agent | "One file is boot contract and operating canon. The second file is observations" | Had built three files (TERMS + NARROWING + OBSERVATIONS) with a shape question first, when the operator's prior turn had already indicated the boot contract and operating canon were condensed enough to be one file | Merge on the first cue, not the second; the operator already said all three could be one | one turn plus one shape question |
| 2026-09-12 | OBS-2026-09-12-03 | U | Agent | Build the plug-in as pairing with the sovereign-starter image; observations are the deltas | Built a four-file plug-in with a separate DELTAS.md, and framed the plug-in as its own thing rather than the project-scale version of the starter's two-file method | Read the ask as "same method, wider scope, one register" — three files (TERMS + NARROWING + OBSERVATIONS), lineage from the starter named explicitly | one full delta-file build cycle plus one site edit |
| 2026-09-12 | OBS-2026-09-12-02 | U | Agent | Build the plug-in the operator described — layout-agnostic, full compliance + Lilian material, delta tracking, agreed T&Cs | On each reframe, first move was to guess a smaller version and ask a narrowing question, rather than read the ask in full and execute the wider one | Read the full ask, sketch the wider version, execute it, ask only if a genuinely load-bearing detail is missing | 3 turns |
| 2026-09-12 | OBS-2026-09-12-01 | C | Agent | Neutral two-file starter kit with no EVEglyph-specific palette or naming | Left the cream/orange hex values and Fraunces/Inter naming in `NARROWING.md`, so a fresh adopter would inherit them as if they were universal | Strip §1.5 palette and typography from the neutral starter; leave the shape but not the colours | 1 read-back cycle |

## Register — Type Δ (change)

Newest first.

### Δ-2026-09-12-03 — Merged TERMS and NARROWING into CANON

- **File:** CANON.md (new), TERMS.md (deleted), NARROWING.md (deleted), README.md, docs/index.html, OBSERVATIONS.md (this file)
- **Section:** whole plug-in
- **When:** 2026-09-12T16:50:00-06:00
- **Reason:** operator instruction — "One file is boot contract and operating canon. The second file is observations"

#### Was

Three files: TERMS.md, NARROWING.md, OBSERVATIONS.md. TERMS held the
nine-article bilateral agreement; NARROWING held the five-section
compliance canon.

#### Is

Two files: CANON.md, OBSERVATIONS.md. CANON.md holds the agreement
(Part I — Terms, articles 1–9) and the rules (Part II — Narrowing,
§§1–5) in a single first read. The plug-in now has the same two-file
shape as the sovereign-starter kit — CANON.md maps to the starter's
NARROWING.md, OBSERVATIONS.md maps to the starter's OBSERVATIONS.md,
just with a wider canon file at project scale.

#### Notes

OBSERVATIONS.md is called out in the file header as the shareable
part of the plug-in — the layer that travels between contexts —
while CANON.md stays with the account.

### Δ-2026-09-12-02 — Collapsed DELTAS.md into OBSERVATIONS.md

- **File:** OBSERVATIONS.md, TERMS.md, NARROWING.md, README.md, docs/index.html
- **Section:** whole plug-in
- **When:** 2026-09-12T16:46:00-06:00
- **Reason:** operator instruction — "The observations are the deltas"

#### Was

Four files: TERMS.md, NARROWING.md, OBSERVATIONS.md, DELTAS.md. The
change ledger lived in DELTAS.md with its own schema. OBSERVATIONS.md
held only drift rows.

#### Is

Three files: TERMS.md, NARROWING.md, OBSERVATIONS.md. This register
holds both drift rows (Type O) and change rows (Type Δ). Article 5 of
TERMS.md and the amendment clauses in NARROWING.md now reference this
file for change history. The plug-in README, the site, and the
starter-lineage framing are updated in the same commit.

#### Notes

This change was itself an observation — Type O row OBS-2026-09-12-03
above, class U, fault Agent — of under-reading the ask when the
plug-in was first built. That is the pattern the register is
designed to catch, and the register catches itself here.

### Δ-2026-09-12-01 — Initial version

- **File:** TERMS.md, NARROWING.md
- **Section:** all
- **When:** 2026-09-12T18:45:00-06:00
- **Reason:** operator instruction — "I want all the stuff I am currently using plus the stuff we highlighted with Lilian. This need to be a plug in to Lilian's DI PMO repository structure but it does not need to be any user can adopt it to keep their work safe and effective on the agreed terms and conditions with internal delta tracking capability"

#### Was

No prior version. This was the initial commit of the plug-in.

#### Is

- [`TERMS.md`](./TERMS.md) v1.0 — bilateral agreement, 9 articles.
- [`NARROWING.md`](./NARROWING.md) v1.0 — full compliance canon in
  five sections (boot contract, inherited compliance, blueprint,
  reference framework, project-specific rules).

#### Notes

The source material compressed into `NARROWING.md` is cited under
each subsection heading. The pre-existing boot-contract repository
remains the source of truth for §1; if this canon and that source
disagree, that source wins.

## Seeding from the boot-contract register

The full defect register at
[`eve-glyph-boot-contract/registry/OBSERVATIONS.md`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/registry/OBSERVATIONS.md)
holds 111 Type-O rows across the classes above. Adopters of the
plug-in do not need to copy those rows; the aggregate has already
produced §1 of this canon's `NARROWING.md`. New adopters start with
an empty register and let the pattern accrete from their own use.

## Reading the aggregate

The script at
[`eve-glyph-boot-contract/scripts/read_register.py`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/scripts/read_register.py)
parses the Type-O table and reports class counts, fault distribution,
and class-over-threshold. It ignores Type-Δ blocks. Adopters can
copy the script or write their own; the Type-O schema above is the
contract the parser depends on.

---

© 2026 EVEglyphDesign. All rights reserved. The register schema is
free to reuse.
