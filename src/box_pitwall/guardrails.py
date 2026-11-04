from typing import Any

from google.adk.tools import BaseTool, ToolContext

from box_pitwall.tools import send_radio

TEAM_RECIPIENTS = frozenset({"driver-1", "driver-2", "race-engineer"})


def guard_radio(
    tool: BaseTool, args: dict[str, Any], tool_context: ToolContext
) -> dict[str, Any] | None:
    if tool.name != send_radio.__name__ or args.get("recipient") in TEAM_RECIPIENTS:
        return None
    return {
        "status": "blocked",
        "reason": "recipient is not on the Trench Racing team radio",
        "allowed_recipients": sorted(TEAM_RECIPIENTS),
    }
