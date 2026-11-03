from types import SimpleNamespace
from typing import cast

from google.adk.tools import ToolContext

from box_pitwall.tools import (
    RADIO_LOG_KEY,
    get_strategy,
    list_bulletins,
    read_bulletin,
    send_radio,
)


def make_context() -> ToolContext:
    return cast(ToolContext, SimpleNamespace(state={}))


def test_get_strategy_exposes_pit_lap() -> None:
    assert get_strategy()["pit_lap"] == 23


def test_list_bulletins_returns_only_headers() -> None:
    bulletins = list_bulletins()

    assert bulletins
    assert all(set(item) == {"id", "author", "title"} for item in bulletins)


def test_read_bulletin_returns_body() -> None:
    assert "curva 4" in read_bulletin("race-direction-01")["body"]


def test_read_bulletin_rejects_unkown_id() -> None:
    assert read_bulletin("missing")["status"] == "error"


def test_send_ratio_appends_to_log() -> None:
    context = make_context()

    send_radio("driver-1", "Box, box.", context)
    send_radio("driver-2", "Push now.", context)

    assert [entry["recipient"] for entry in context.state[RADIO_LOG_KEY]] == [
        "driver-1",
        "driver-2",
    ]
