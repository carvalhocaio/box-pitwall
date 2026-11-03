from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Strategy:
    pit_lap: int
    tyre: str
    plan_b: str


STRATEGY = Strategy(
    pit_lap=23,
    tyre="hard",
    plan_b="undercut on lap 19 if the safety car comes out",
)
