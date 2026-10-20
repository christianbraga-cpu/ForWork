#!/usr/bin/env bash
# Starts the Google Search Console MCP server using the service account key stored in
# the GSC_SERVICE_ACCOUNT_JSON environment secret (raw JSON or base64). The key is written
# to a private temp file that is removed when the server exits. Never commit the key.
set -euo pipefail

if [[ -z "${GSC_SERVICE_ACCOUNT_JSON:-}" ]]; then
  echo "GSC_SERVICE_ACCOUNT_JSON is not set. See content-system/connectors/README.md" >&2
  exit 1
fi

umask 077
keyfile="$(mktemp "${TMPDIR:-/tmp}/gsc-key.XXXXXX.json")"
trap 'rm -f "$keyfile"' EXIT

if [[ "${GSC_SERVICE_ACCOUNT_JSON}" == \{* ]]; then
  printf '%s' "$GSC_SERVICE_ACCOUNT_JSON" > "$keyfile"
else
  printf '%s' "$GSC_SERVICE_ACCOUNT_JSON" | base64 -d > "$keyfile"
fi

export GOOGLE_APPLICATION_CREDENTIALS="$keyfile"
npx -y mcp-server-gsc@0.3.0
