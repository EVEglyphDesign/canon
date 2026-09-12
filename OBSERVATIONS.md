# Observations — umbrella scope

**Document ID** `EgD-CANON-OBS` · **Key ID** `EgD-KEY-2026-07` · Companion to
[`NARROWING.md`](./NARROWING.md) (the master canon).

The register at umbrella scope. Feeds changes to the master canon (layers 1
and 2) and to any project canon (layers 3, 4, 5) whose observations belong
here rather than in a project-scoped register.

The register is not the point. The point is that the operator wants to
narrow the AI surface's operation across every project, and this file is
the evidence base for the narrowing rules in [`NARROWING.md`](./NARROWING.md).
Individual rows may drift; the aggregate is what matters. **The pattern will
not lie.**

## Provenance

Every observation logged in the source repository
[`eve-glyph-boot-contract/registry/OBSERVATIONS.md`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/registry/OBSERVATIONS.md)
counts as evidence for changes to layers 1 and 2 of the master canon in
this repository. Rather than duplicate that register here, this file cites
it and records only observations that are umbrella-scope in origin — for
example, observations against the canon-inheritance mechanism itself, or
observations that surface only when two project canons interact.

Project-scoped observations belong in `projects/<project>/OBSERVATIONS.md`
where they exist. Umbrella-scope observations belong here.

## Schema

Same schema as the source register.

| Column | What goes in it |
|---|---|
| `date` | ISO date, `YYYY-MM-DD` |
| `id` | `OBS-YYYY-MM-DD-NN`, umbrella-scope; never reused |
| `class` | Single letter — the shape of the miss |
| `fault` | Agent, Instruction, Tooling, Upstream |
| `asked` | What the operator asked for |
| `done` | What was done instead |
| `cheaper` | The path that should have been taken |
| `waste` | The cost — time, money, trust |

## Class taxonomy

Inherits from the source register at
[`eve-glyph-boot-contract/registry/OBSERVATIONS.md`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/registry/OBSERVATIONS.md).
Current classes (as of source commit `81de65d`):

- **C** (39) canon breach
- **R** (19) retrieval waste
- **D** (16) durability
- **L** (8) link and format
- **E** (6) equality drift
- **S** (5) unconfirmed spend
- **T** (4) timing
- **H** (3) handoff
- and **U**, **I**, **B**, **P**, **V**, **A**, **F** under threshold

New classes appear the first time a row uses them, in either register. Do
not delete a letter once used.

## Fault ranks

- **Agent** — the AI did it
- **Instruction** — the ask was ambiguous, contradictory, or missing key context
- **Tooling** — the platform, sandbox, or connector was the cause
- **Upstream** — a third-party service, external data, or network was the cause

## The register

<!-- Add new rows at the top. Oldest at the bottom. -->

| Date | ID | Class | Fault | Asked | Done | Cheaper | Waste |
|---|---|---|---|---|---|---|---|

*No umbrella-scope entries yet. Source-scope entries are at
[`eve-glyph-boot-contract/registry/OBSERVATIONS.md`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/registry/OBSERVATIONS.md).*

## How to add a project register

When a project accumulates enough observations that keeping them in the
umbrella register makes them hard to find:

1. Create `projects/<project>/OBSERVATIONS.md`.
2. Copy this file's schema, class taxonomy, and fault-rank sections.
3. Cite the umbrella register in the header for observations that apply
   across projects.
4. Log the project's observations there. The umbrella register keeps only
   what is cross-project.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
