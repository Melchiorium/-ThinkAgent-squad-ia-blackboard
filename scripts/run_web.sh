#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
cd "$repo_root"

if [[ ! -f ".env" ]]; then
  echo "Missing .env file. Create it or copy the expected environment variables before running the web app." >&2
  exit 1
fi

set -a
source .env
set +a

: "${BLACKBOARD_PROMPT_VERSION:=V3}"
: "${WEB_HOST:=127.0.0.1}"
: "${WEB_PORT:=8000}"
: "${WEB_ACCESS_TOKEN:=demo}"

export BLACKBOARD_PROMPT_VERSION
export WEB_HOST
export WEB_PORT
export WEB_ACCESS_TOKEN

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "Missing OPENAI_API_KEY after loading .env." >&2
  exit 1
fi

if [[ "$WEB_ACCESS_TOKEN" == "demo" ]]; then
  echo "Open http://${WEB_HOST}:${WEB_PORT}/?access_token=demo"
else
  echo "Open http://${WEB_HOST}:${WEB_PORT}/ with the access token configured in .env."
fi

exec python3 app/web.py
