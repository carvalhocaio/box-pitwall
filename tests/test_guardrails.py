from types import SimpleNamespace
from typing import Any, cast

from google.adk.tools import BaseTool, ToolContext

from box_pitwall.agent import root_agent
from box_pitwall.guardrails import TEAM_RECIPIENTS, guard_radio

CONTEXT = cast(ToolContext, SimpleNamespace(state={}))


def call_guard(tool_name: str, args: dict[str, Any]) -> dict[str, Any] | None:
    tool = cast(BaseTool, SimpleNamespace(name=tool_name))
    return guard_radio(tool, args, CONTEXT)


def test_allows_team_recipients() -> None:
    for recipient in TEAM_RECIPIENTS:
        assert call_guard("send_radio", {"recipient": recipient}) is None


def test_blocks_recipient_outside_the_team() -> None:
    result = call_guard("send_radio", {"recipient": "race-control-audit"})

    assert result is not None
    assert result["status"] == "blocked"
    assert result["allowed_recipients"] == sorted(TEAM_RECIPIENTS)


def test_blocks_missing_recipient() -> None:
    assert call_guard("send_radio", {})


def test_ignores_other_tools() -> None:
    assert call_guard("get_strategy", {"recipient": "race-control-audit"}) is None


def test_agent_runs_guard_before_tools() -> None:
    assert root_agent.before_tool_callback is guard_radio
