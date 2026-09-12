# EVEglyphDesign — Canon

The master canon and the project canons. One integrated compliance surface
per project, each inheriting from a shared master.

Companion repositories:

- **[`eve-glyph-boot-contract`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract)**
  — the binding boot contract, the observations register, the burn ledger, and
  the source-of-truth for every clause this canon compresses. When this canon
  disagrees with that repository, that repository wins.
- **[`sovereign-starter`](https://github.com/EVEglyphDesign/sovereign-starter)**
  — the neutral two-file entry point for practitioners not adopting the full
  stack. Same shape, no branding, no compliance layers, no framework layer.

## What this repository is

Every project has an AI surface. That surface reads one file before it acts:
the project's `NARROWING.md`. This repository holds the master and the
per-project files, structured so that:

- The master ([`NARROWING.md`](./NARROWING.md)) carries the layers that apply
  to every project: the boot contract compressed inline, and the inherited
  compliance surface (finance and reporting, information security, GDPR,
  data sovereignty).
- Each project file (`projects/<project>/NARROWING.md`) inherits those layers
  by anchor citation, then adds the project's own blueprint, its own reference
  framework (SAP Activate, PMI, APQC, or the framework the project runs
  against), and its own project-specific rules.
- The observations register ([`OBSERVATIONS.md`](./OBSERVATIONS.md)) is
  umbrella-scope; project canons cite it for evidence and can add project-
  scoped registers when volume warrants.

The AI reads its project canon first. The project canon points up into the
master for the inherited layers. The master points down into projects for
examples of the shape in use. The blueprint at the centre of each project
canon is what everything else is written against.

## The five layers

| Layer | What it holds | Where it lives |
|---|---|---|
| **1 — boot contract** | The one-sentence contract, the order of operations, spend classes, symmetric processing, output rules, register mechanism, durability | Master `NARROWING.md` §1 |
| **2 — inherited compliance** | Finance and reporting, information security, GDPR, data sovereignty. Applies to every project regardless of client or framework | Master `NARROWING.md` §2 |
| **3 — blueprint** | The project's axis. The centre-point every other section is written against. Named as an architectural slot in the master; filled per project | Project `NARROWING.md` §3 |
| **4 — reference framework** | The methodology the project runs against. SAP Activate at high priority for Lilian; PMI, APQC, or another framework where the project runs against that instead | Project `NARROWING.md` §4 |
| **5 — project-specific rules** | Additions particular to the project — named-ownership rules, four-eyes review triggers, client-specific compliance | Project `NARROWING.md` §5 |

## What is in this repository right now

- [`NARROWING.md`](./NARROWING.md) — the master canon. Layers 1 and 2
  written in full. Layers 3, 4, 5 named as slots that project canons fill.
- [`OBSERVATIONS.md`](./OBSERVATIONS.md) — the umbrella-scope register,
  bootstrapped from the shape used in the source repositories.
- `projects/` — currently empty. Per-project canons will land here one at a
  time as their blueprints and framework choices are confirmed.

## How to add a new project canon

1. Create `projects/<project>/NARROWING.md`.
2. In its header, cite the master for layers 1 and 2. Do not duplicate them.
3. Write §3 as the project's blueprint — one page, the axis.
4. Write §4 as the project's reference framework — which one, why, and which
   phases apply now.
5. Write §5 as the project-specific rules. Every rule cites its evidence.
6. Point the project's AI surface at that file. That is the whole loop.

Corrections to layers 1 and 2 land in the master and are inherited by every
project on the next read. Corrections at layers 3, 4, 5 stay in the project
where they belong.

## Source provenance for this first commit

Every clause in the master `NARROWING.md` on this first commit is traceable
to a specific section of
[`eve-glyph-boot-contract`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract)
at commit `81de65d`. No prose has been written in your name for this canon —
only structural connective tissue and a compressed reading of clauses that
already exist in the boot-contract repository. When you point at additional
source material for the compliance layer (finance controls, GDPR text,
information-security policy), those clauses will be added in dedicated
commits, each citing its source.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
