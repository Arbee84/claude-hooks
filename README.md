# arbee84-hooks

Hooks for every Claude Code session on every device. One plugin so far:

- **agent-model-guard**: a `PreToolUse` hook on the `Agent` tool that refuses a call whose input
  names no `model`. An unset model inherits the session's model, which turns a grep-and-quote
  survey into a Fable agent. The rule it enforces: sonnet for digests, surveys and research, opus
  for verification and review-style reads, the session's own model only for judgement work.

Install on a machine, once:

    /plugin marketplace add Arbee84/claude-hooks
    /plugin install agent-model-guard@arbee84-hooks

Or in `~/.claude/settings.json`:

    {
      "extraKnownMarketplaces": { "arbee84-hooks": { "source": { "source": "github", "repo": "Arbee84/claude-hooks" } } },
      "enabledPlugins": { "agent-model-guard@arbee84-hooks": true }
    }

Needs bash (Git Bash on Windows) and any python on PATH. Without python the hook lets the call
through and shows a warning instead of blocking.
