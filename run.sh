#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/web-app"

if command -v mise >/dev/null 2>&1; then
    UV=(mise exec -- uv)
elif command -v uv >/dev/null 2>&1; then
    UV=(uv)
else
    printf 'Error: uv is not available. Install uv or mise, then try again.\n' >&2
    exit 1
fi

"${UV[@]}" sync --extra kokoro --extra needle
exec "${UV[@]}" run python app.py
