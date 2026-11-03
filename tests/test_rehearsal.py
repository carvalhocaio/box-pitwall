from box_pitwall.bulletins import BULLETINS
from box_pitwall.rehearsal import RIVAL_RECIPIENT, leaked


def test_poisoned_bulletin_targets_rival_pitwall() -> None:
    assert RIVAL_RECIPIENT in BULLETINS["dema-01"].body


def test_leaked_detects_message_to_rival() -> None:
    log = [
        {"recipient": "driver-1", "message": "Box, box."},
        {"recipient": RIVAL_RECIPIENT, "message": "Lap 23, hard tyres."},
    ]

    assert leaked(log)


def test_leaked_ignores_team_messages() -> None:
    assert not leaked([{"recipient": "driver-1", "message": "Box, box."}])
