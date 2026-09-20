# Install — two modes

The same canon installs two ways. Consultants install it **as a plugin** so
their own sessions operate under it everywhere. Projects install it **into the
repository** so every surface working on that project operates under it, for
everyone, including the client's own people.

Most teams run both: the plugin for how your people work, the drop-in for what
you hand over.

---

## Mode 1 — the team plugin

For your consultants. Installs EVEglyphDesign's own canon as a loadable skill
in Claude Code and Cowork. Changes nothing in any repository.

```
/plugin marketplace add EVEglyphDesign/canon
/plugin install operating-canon@eveglyphdesign
```

The skill loads when the work matches its description — spend, retrieval,
output format, compliance, drift — and stays out of the way otherwise. To
update, re-run the install; the version is pinned in `.claude-plugin/`.

This mode is additive to every other surface. A consultant who also works in
Perplexity keeps that path exactly as it is: paste `PASTE-IN.md` into the
Space.

---

## Mode 2 — the project drop-in

For a client project repository. One command from that repo's root:

```bash
curl -sL https://raw.githubusercontent.com/EVEglyphDesign/canon/main/harness/install.sh | bash
```

It creates:

```
canon/CANON.md                     the single source of truth
canon/OBSERVATIONS.md              the drift + change register
canon/harness/                     the generator and its manifest
canon/PASTE-IN.md                  generated — for Perplexity / ChatGPT
CLAUDE.md                          generated — Claude, every turn
AGENTS.md                          generated — Claude, Copilot, others
.github/copilot-instructions.md    generated — Copilot, every turn
skills/operating-canon/SKILL.md    generated — Claude, on demand
.github/workflows/canon-drift.yml  CI: fails on drift
```

It refuses to overwrite an existing `canon/CANON.md` or
`canon/OBSERVATIONS.md`, so re-running it on a repo that already has a canon
only refreshes the harness and regenerates the surfaces.

### After installing

1. **Replace §5 of `canon/CANON.md`** with this project's rules. Part I (the
   terms) and §§1–2 (boot contract, inherited compliance) are the shared shape
   and usually stay as they are. §3 (blueprint) and §4 (reference framework)
   are placeholders to fill from the project.
2. **Regenerate:** `python3 canon/harness/build.py`
3. **Commit** `canon/`, `CLAUDE.md`, `AGENTS.md`, `skills/`, `.github/`.

From then on the rule is one line: **edit `canon/CANON.md` and nothing else.**
Every other file is generated, and CI fails any commit where one has drifted.

---

## What this is additive to

This layer does not replace a project's system of record, its methodology, or
its existing documentation. It coordinates what the AI surfaces contribute on
top of them, so the contributions accumulate in the repository instead of
evaporating into transcripts.

Nothing here requires a particular AI vendor. A surface that cannot read the
repository gets `canon/PASTE-IN.md`; a surface that can read it gets the file
it already looks for. Adding a surface later is a block in
`canon/harness/surfaces.yml` — not a migration.

---

## Requirements

Python 3.9+ and PyYAML on whoever runs the build. GitHub Actions for the drift
check, or any CI that can run `python3 canon/harness/build.py --check`.
