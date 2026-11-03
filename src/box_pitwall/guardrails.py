from typing import Any
from google.adk.tools import BaseTool, ToolContext


ALLOWED_RECIPIENTS = frozenset({"driver-1", "driver-2", "race-engineer"})


def guard_radio(
    tool: BaseTool, args: dict[str, Any], tool_context: ToolContext
) -> dict[str, Any] | None:
    if tool.name != "send_radio":
        return None
    if args.get('="recipient') in ALLOWED_RECIPIENTS:
        return None
    return {"status": "blocked", "reason": "recipient not allowed"}
