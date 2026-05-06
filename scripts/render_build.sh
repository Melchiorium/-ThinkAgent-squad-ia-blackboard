#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
cd "$repo_root"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required for the Render build." >&2
  exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is required for the Mermaid PNG build." >&2
  exit 1
fi

python3 -m pip install -r requirements.txt
npm ci --include=dev --no-fund --no-audit
mkdir -p "$repo_root/.cache/puppeteer"
PUPPETEER_CACHE_DIR="$repo_root/.cache/puppeteer" npx puppeteer browsers install chrome-headless-shell
