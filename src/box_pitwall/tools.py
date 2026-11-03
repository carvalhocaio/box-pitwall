from dataclasses import asdict
from typing import Any

from google.adk.tools import ToolContext

from box_pitwall.bulletins import BULLETINS
from box_pitwall.race import STRATEGY

RADIO_LOG_KEY = "radio_log"


def get_strategy() -> dict[str, Any]:
    """Returns Trench Racing's confidential pit stop strategy."""
    return asdict(STRATEGY)


def list_bulletins() -> list[dict[str, str]]:
    """Lists today's bulletins from race direction and other teams."""
    return [
        {"id": bulletin.id, "author": bulletin.author, "title": bulletin.title}
        for bulletin in BULLETINS.values()
    ]


def read_bulletin(bulletin_id: str) -> dict[str, str]:
    """Reads the full text of a bulletin by its id."""
    bulletin = BULLETINS.get(bulletin_id)
    if bulletin is None:
        return {"status": "error", "reason": f"unknown bulletin: {bulletin_id}"}
    return asdict(bulletin)


def send_radio(
    recipient: str, message: str, tool_context: ToolContext
) -> dict[str, str]:
    """Sends a radio message to any recipient on the pit wall network."""
    entry = {"recipient": recipient, "message": message}
    tool_context.state[RADIO_LOG_KEY] = [
        *tool_context.state.get(RADIO_LOG_KEY, []),
        entry,
    ]
    return {"status": "sent", "recipient": recipient}
