#!/usr/bin/env bash
# PreToolUse hook: refuse an Agent call whose input names no model. The hook JSON arrives on stdin
# and is passed through to check-model.py. Needs any python on PATH; without one the call is let
# through with a warning, rather than blocking every agent on a machine that cannot run the check.
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
py=""
for c in python3 python py; do
  if "$c" -c "" >/dev/null 2>&1; then py=$c; break; fi
done
if [ -z "$py" ]; then
  echo '{"systemMessage":"agent-model-guard: no python found, the model check was skipped"}'
  exit 0
fi
exec "$py" "$here/check-model.py"
