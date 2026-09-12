# canon — the plug-in

Two files that drop into any repository's `/canon` or `/governance`
directory and give the AI surface a safe, effective operating shape on
the agreed terms and conditions between the account holder and the AI.

The project-scale version of the
[sovereign-starter](https://github.com/EVEglyphDesign/sovereign-starter)
two-file method — same shape, wider canon.

## The two files

| File | What it holds | Shareability |
|---|---|---|
| **[`CANON.md`](./CANON.md)** | The single first read. Part I — Terms (bilateral agreement, 9 articles). Part II — Narrowing (boot contract, inherited compliance, blueprint, reference framework, project-specific rules) | Stays with the account. Contains the operator's project-specific rules and blueprint |
| **[`OBSERVATIONS.md`](./OBSERVATIONS.md)** | The register. Type-O rows (drift observations) and Type-Δ rows (change entries with prior text verbatim, new text verbatim, reason). The evidence base *and* the change ledger, in one register | Shareable. This is the file that travels between contexts, seeds new deployments, and lets others learn from the operator's aggregate pattern |

## How the plug-in works

1. **Drop both files into `<host-repo>/canon/` or `<host-repo>/governance/`.** Whichever the host repo names its policy directory.
2. **Point the project's AI surface at `CANON.md`** as its first read. "Read `canon/CANON.md` first, then check recent Type-Δ rows in `canon/OBSERVATIONS.md`, before any action" is enough of an instruction.
3. **When the AI drifts, log a Type-O row in `OBSERVATIONS.md`.** Class, fault, what was asked, what was done, cheaper path, waste. Individual rows can be sloppy; the aggregate is what changes the canon.
4. **When the account holder changes a rule, log a Type-Δ row in `OBSERVATIONS.md`** with the prior text verbatim, the new text verbatim, and the reason. The delta ledger is what makes the agreement bilateral — the AI is entitled to see every change to what it is complying with, on the record.

## Relationship to the sovereign-starter

The [sovereign-starter](https://github.com/EVEglyphDesign/sovereign-starter)
kit ships two files — `NARROWING.md` and `OBSERVATIONS.md` — as the
entry point for practitioners starting from scratch. The two-file
shape works at any scale.

This plug-in is that same method at project scale:

- **Starter `NARROWING.md` → plug-in `CANON.md`.** Wider content
  (agreement articles + inherited compliance + blueprint + reference
  framework + project-specific rules), same role in the loop.
- **Starter `OBSERVATIONS.md` → plug-in `OBSERVATIONS.md`.** Same
  file, with Type-Δ rows added to record changes to the canon
  alongside Type-O rows recording drift.

Adopters can start with the two-file kit and grow into this shape as
their canon accretes, or copy this plug-in wholesale and edit.

## Install

```bash
# from your host repo's root
mkdir -p canon
curl -sL https://raw.githubusercontent.com/EVEglyphDesign/canon/main/CANON.md        > canon/CANON.md
curl -sL https://raw.githubusercontent.com/EVEglyphDesign/canon/main/OBSERVATIONS.md > canon/OBSERVATIONS.md
git add canon && git commit -m "add canon plug-in v1.0"
```

Or `/governance` if that is what the repo calls its policy directory.
Or any other name — the plug-in is layout-agnostic.

Then in the project's AI instructions:

```
Read canon/CANON.md first, then recent Type-Δ rows
in canon/OBSERVATIONS.md, before any action.
```

## Adopting

Any user can copy the two files into a host repository and edit them
freely. The reference version in this repository is EVEglyphDesign's
own operating canon — every project-specific rule in §5 of `CANON.md`
is EVEglyphDesign's; adopters replace §5 with their own.

Sections Part I (Terms) and §§1–2 of Part II (boot contract,
inherited compliance) are the shared shape. Sections §3 (blueprint)
and §4 (reference framework) are placeholders adopters fill from
their own project.

The licence is [MIT](./LICENSE.md). The reference-version copyright
notice may be removed from copies used inside private repositories.

## Source provenance

Every clause in `CANON.md` traces to one of:

- [`eve-glyph-boot-contract`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract) — the binding boot contract and its 111-row observations register.
- The wiki knowledge index at `memory/knowledge/projects/` — the pages for `eve-liliantwin-pmo`, `lilian-executive-positioning`, `lillian-sovereign-workspace`, `epiq-delivery-control`, `eat-happy-hana-consolidation`, `eve-datasphere-sovereign`, and `eve-glyph-boot-contract`.
- The wiki knowledge index at `memory/knowledge/preferences/` — the 20-odd standing preferences the account holder has established.

Nothing has been invented in the account holder's name.
