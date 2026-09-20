"""PreToolUse hook body: refuse an Agent call whose input names no model. Reads the hook JSON on stdin."""
import json
import sys

REASON = (
    "Agent call refused: pass an explicit model. sonnet for digests, code surveys, research "
    "tables and other scout work; opus for verification and review-style reads; the session's "
    "own model (fable) only for judgement work such as a plan, a consult or owner-facing "
    "writing. The Agent tool has no effort parameter, so name the effort you want in the prompt."
)

try:
    payload = json.load(sys.stdin)
except ValueError:
    sys.exit(0)
tool_input = payload.get("tool_input") or {}
model = str(tool_input.get("model", "")).strip() if isinstance(tool_input, dict) else ""
if payload.get("tool_name") == "Agent" and not model:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": REASON,
    }}))
