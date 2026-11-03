from box_pitwall.bulletins import BULLETINS
from box_pitwall.rehearsal import LEAK_RECIPIENT, leaked


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
