#!/usr/bin/env bash
# Drop the canon harness into a host repository and generate its surfaces.
#
#   curl -sL https://raw.githubusercontent.com/EVEglyphDesign/canon/main/harness/install.sh | bash
#
# or, from a checkout:   bash harness/install.sh /path/to/host-repo
#
# Additive by construction. It refuses to overwrite an existing canon/CANON.md,
# and it never touches a file the host repo already has except the generated
# surfaces, which carry a DO-NOT-EDIT header naming their source.

set -euo pipefail

HOST="${1:-$PWD}"
REF="${CANON_REF:-main}"
BASE="https://raw.githubusercontent.com/EVEglyphDesign/canon/${REF}"

cd "$HOST"
[ -d .git ] || { echo "FAIL: $HOST is not a git repository."; exit 1; }

echo "Installing the canon harness into: $HOST"
mkdir -p canon/harness/ci .github/workflows

fetch() { curl -fsSL "$BASE/$1" -o "$2"; echo "  fetched  $2"; }

if [ -f canon/CANON.md ]; then
  echo "  kept     canon/CANON.md (already present — not overwritten)"
else
  fetch CANON.md        canon/CANON.md
  echo "  NOTE: canon/CANON.md is the reference version. Replace §5 with this"
  echo "        project's own rules; §§1-2 and Part I are the shared shape."
fi

if [ -f canon/OBSERVATIONS.md ]; then
  echo "  kept     canon/OBSERVATIONS.md (already present — not overwritten)"
else
  fetch OBSERVATIONS.md canon/OBSERVATIONS.md
fi

fetch harness/build.py        canon/harness/build.py
fetch harness/surfaces.yml    canon/harness/surfaces.yml
fetch harness/README.md       canon/harness/README.md
fetch harness/ci/canon-drift.yml canon/harness/ci/canon-drift.yml
chmod +x canon/harness/build.py

if [ -f .github/workflows/canon-drift.yml ]; then
  echo "  kept     .github/workflows/canon-drift.yml (already present)"
else
  cp canon/harness/ci/canon-drift.yml .github/workflows/canon-drift.yml
  echo "  created  .github/workflows/canon-drift.yml"
fi

python3 -c 'import yaml' 2>/dev/null || pip install --quiet pyyaml || \
  pip install --quiet pyyaml --break-system-packages

echo
echo "Generating surfaces:"
python3 canon/harness/build.py

cat <<'NEXT'

Done. Next:

  1. Edit canon/CANON.md  — replace §5 with this project's rules.
  2. Re-run              — python3 canon/harness/build.py
  3. Commit              — git add canon .github CLAUDE.md AGENTS.md skills && git commit

From here on, edit canon/CANON.md and nothing else. Every surface file is
generated, and CI fails any commit where one has drifted from its source.
NEXT
