#!/usr/bin/env bash
# Copy the stockquant package into the investing skills so they work standalone
# (e.g. when installed into a Claude profile). Run after changing stockquant/.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
skills="$here/../.claude/skills"
for s in investment-research portfolio-goal-planner; do
  dest="$skills/$s/scripts/stockquant"
  rm -rf "$dest"
  mkdir -p "$dest"
  cp "$here"/stockquant/*.py "$here"/stockquant/universe.csv "$dest"/
  echo "synced stockquant -> $dest"
done
