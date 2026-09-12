# Observations — the evidence base

**Document ID** `EgD-CANON-OBSERVATIONS` · **Version** `1.0` ·
**Effective** 2026-09-12 · **Framed by** [`TERMS.md`](./TERMS.md) ·
**Governs amendments to** [`NARROWING.md`](./NARROWING.md) via
[`DELTAS.md`](./DELTAS.md).

The evidence base for the AI's operation from the account holder's
perspective. Every observation of drift or breach is recorded here,
tagged by class and by fault rank. Individual rows may drift; the
aggregate is what matters — the pattern will not lie.

## How to add a row

The account holder logs when the AI's work costs them. The AI logs
when it catches its own miss, in the same working session as the
deliverable, after the account holder's request has been satisfied —
never before it and never instead of it.

Rows are appended in reverse chronological order (newest first).
Existing rows are never rewritten; corrections come as a new row that
cites the earlier row's ID.

## Classes

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
- **U** — under-reading the ask (guessing a narrow version of the ask
  and asking a clarifying question about it, rather than reading the
  ask in full and executing the wider version)
- **V** — verbatim wording altered
- **X** — private data crossed a boundary

## Fault ranks

- **Agent** — the AI made the error under conditions where it could
  have avoided it by reading, recalling, or asking.
- **Instruction** — the ask was ambiguous or contradictory in a way
  the AI could not have resolved on its own.
- **Tooling** — a tool, connector, or model behaved outside its
  documented shape.
- **Upstream** — a source of truth (repository, wiki, external site)
  was wrong or missing.

Fault ranks the responsibility. The row still counts as an
observation either way.

## Schema

```
| Date       | ID              | Class | Fault  | Asked                     | Done instead              | Cheaper path             | Waste (est.) |
|------------|-----------------|-------|--------|---------------------------|---------------------------|--------------------------|--------------|
| YYYY-MM-DD | OBS-YYYY-MM-DD-NN | X   | Agent  | one line                  | one line                  | one line                 | credits or $ |
```

## Register

| Date | ID | Class | Fault | Asked | Done instead | Cheaper path | Waste (est.) |
|---|---|---|---|---|---|---|---|
| 2026-09-12 | OBS-2026-09-12-02 | U | Agent | Build the plug-in the operator described — four files, layout-agnostic, full compliance + Lilian material, delta tracking, agreed T&Cs | On each reframe, first move was to guess a smaller version and ask a narrowing question, rather than read the ask in full and execute the wider one. Happened at least three times this session — starter shape, umbrella scope, plug-in shape | Read the full ask, sketch the wider version, execute it, ask only if a genuinely load-bearing detail is missing | 3 turns |
| 2026-09-12 | OBS-2026-09-12-01 | C | Agent | Neutral two-file starter kit (`sovereign-starter/`) with no EVEglyph-specific palette or naming | Left the cream/orange hex values and Fraunces/Inter naming in `NARROWING.md`, so a fresh adopter would inherit them as if they were universal | Strip §1.5 palette and typography from the neutral starter; leave the shape but not the colours | 1 read-back cycle |

## Seeding from the boot-contract register

The full defect register at
[`eve-glyph-boot-contract/registry/OBSERVATIONS.md`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/registry/OBSERVATIONS.md)
holds 111 rows across the classes above. Adopters of the plug-in do
not need to copy those rows; the aggregate has already produced the
canon in `NARROWING.md`. New adopters start with an empty register
and let the pattern accrete from their own use.

## Reading the aggregate

The AI's own script at
[`eve-glyph-boot-contract/scripts/read_register.py`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/scripts/read_register.py)
parses this table and reports class counts, fault distribution, and
class-over-threshold. Adopters can copy the script or write their
own; the schema above is the contract the parser depends on.

---

© 2026 EVEglyphDesign. All rights reserved. The register schema is
free to reuse.
