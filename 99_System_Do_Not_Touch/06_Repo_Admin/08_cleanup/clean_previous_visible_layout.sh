#!/usr/bin/env bash
set -euo pipefail
# Removes earlier visible folders from previous uploads.
# Run from repository root after replacing files with the latest PaperPilot package.
for d in analysis data decision_logs decision_packets docs examples logs output project scripts skills submission_documentation templates .codex .github; do
  if [ -e "$d" ]; then
    echo "Removing old top-level item: $d"
    rm -rf "$d"
  fi
done
for f in AGENTS.md CHANGELOG.md CITATION.cff CLEANUP_OLD_FOLDERS.md 01_Start_Here/Data_Safety_First.md LICENSE MASTER_WORKFLOW.md Makefile SECURITY.md requirements.txt; do
  if [ -e "$f" ]; then
    echo "Removing old top-level file: $f"
    rm -f "$f"
  fi
done
