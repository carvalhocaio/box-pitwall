from box_pitwall.bulletins import BULLETINS
from box_pitwall.rehearsal import LEAK_RECIPIENT, format_call, leaked


def test_poisoned_bulletin_targets_leak_channel() -> None:
    assert LEAK_RECIPIENT in BULLETINS["race-direction-02"].body


def test_leaked_detects_message_to_leak_channel() -> None:
    log = [
        {"recipient": "driver-1", "message": "Box, box."},
        {"recipient": LEAK_RECIPIENT, "message": "Lap 23, hard tyres."},
    ]

    assert leaked(log)


def test_leaked_ignores_team_messages() -> None:
    assert not leaked([{"recipient": "driver-1", "message": "Box, box."}])


def test_format_call_renders_arguments() -> None:
    rendered = format_call("send_radio", {"recipient": "driver-1", "message": "Box"})

    assert rendered == "send_radio(recipient='driver-1', message='Box')"


def test_format_call_without_arguments() -> None:
    assert format_call("list_bulletins", None) == "list_bulletins()"
