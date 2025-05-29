from enum import IntEnum, auto, Enum


class SKILL_EVENT_TYPE(IntEnum):
    PRE_CAST = auto()
    CAST = auto()
    HIT = auto()
