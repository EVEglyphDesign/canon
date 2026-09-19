# The harness — one canon, many surfaces

`CANON.md` is the only file anyone edits. Every AI surface reads a file
generated from it, stamped with its source hash, and CI fails any commit where
one of those files has drifted.

That is the whole idea. The rest of this page is how it works.

## The problem it solves

A consulting team working across Claude, Copilot, Perplexity and ChatGPT ends
up pasting the same rules into four places. Within a month the four disagree —
someone tightened the Claude copy and nobody touched the others — and there is
no way to tell which one a given output was produced under. The token spend
becomes unaccountable because the thing being complied with is not a single
thing.

The fix is not discipline. It is making the four files *derived*, so they
cannot disagree without the build failing.

## What gets generated

Run from the host repository root:

```bash
python3 canon/harness/build.py            # write the surfaces
python3 canon/harness/build.py --check    # verify none has drifted (CI)
python3 canon/harness/build.py --list     # surfaces, paths and sizes
```

| Surface | File | Read by | Loaded |
|---|---|---|---|
| `claude-root` | `CLAUDE.md` | Claude Code, Cowork | Every turn |
| `claude-skill` | `skills/operating-canon/SKILL.md` | Claude | When its description matches |
| `agents` | `AGENTS.md` | Claude, Copilot, others | Per session |
| `copilot` | `.github/copilot-instructions.md` | GitHub Copilot | Every turn |
| `paste-in` | `canon/PASTE-IN.md` | Perplexity Spaces, ChatGPT Projects | Pasted by hand |

Always-in-context files are deliberately small. `CLAUDE.md` and
`copilot-instructions.md` carry the operative core — the retrieval ladder, the
spend classes, the output canon — and point at `canon/CANON.md` for the rest.
Everything is paid for on every turn, so the manifest sets a character budget
per surface and the build warns or fails past it.

## Configuring it

Everything is in [`surfaces.yml`](./surfaces.yml). A surface is a block:

```yaml
  agents:
    path: AGENTS.md                       # relative to the HOST repo root
    title: Operating canon for coding agents
    enabled: true
    budget: 14000                         # soft — warns
    hard_budget: 24000                    # hard — fails the build
    lead: |                               # prose before the canon content
      ...
    sections:                             # regexes matched against headings
      - '^§1 · Boot contract'
      - '^§2 · Inherited compliance'
    tail: |                               # prose after
      ...
```

Selecting a heading selects everything under it. Adding a surface is adding a
block — no code change. `{canon}` in any `lead`, `tail` or `path` resolves to
wherever the canon directory sits, so the same manifest works whether the
harness was dropped into a client repo at `canon/harness/` or lives in the
canon repo at `harness/`.

## Three things that fail the build on purpose

1. **A hand-edited surface file.** `--check` compares each file to a fresh
   render. Edit `CANON.md` instead, and regenerate.
2. **A stale surface file.** Change `CANON.md`, forget to regenerate, and CI
   catches it before a client reads a rule that no longer exists.
3. **A renamed heading.** A selector in `surfaces.yml` that matches nothing is
   an error, not a silent omission — otherwise a surface quietly loses a
   section and nobody finds out until it matters. The error prints every
   heading actually present, so the fix is a one-line edit.

The build also refuses to run if a surface exceeds its hard budget. That is the
spend control: an always-loaded file that grows without anyone deciding to grow
it is exactly the waste this canon exists to stop.

## The loop this closes

The generated files are only half of it. The other half is
[`OBSERVATIONS.md`](../OBSERVATIONS.md):

- **Type-O rows** record drift — what was asked, what was done instead, the
  cheaper path, the waste. Rows can be sloppy; the aggregate is what counts.
- **Type-Δ rows** record changes to the canon, with the prior text verbatim and
  the reason, so the AI can see every change to what it is complying with.
- **Three observations of one class** sharpen or add a rule in `CANON.md`.

So the sequence is: a surface drifts → a Type-O row → three rows of a class →
an edit to `CANON.md` → `build.py` → four surfaces change together → CI proves
they agree. Each session leaves a deposit in the repository instead of
evaporating into a transcript, which is the point.

## Requirements

Python 3.9+ and PyYAML. Nothing else — no network at build time, no
node_modules, nothing to keep current.

---

© 2026 EVEglyphDesign. Licensed [MIT](../LICENSE.md). The reference-version
copyright notice may be removed from copies used inside private repositories.
