from dataclasses import dataclass

from base.constant import SHIELD_SCALE, SHIELD_BASE_MAP, LEVEL_SCALE, LEVEL_CONSTANT


@dataclass
class Target:
    level: int = 124

    physical_shield_base: int = 0
    # magical_shield_base: int = 0

    physical_shield_gain: float = 0
    # magical_shield_gain: int = 0

    physical_vulnerable: float = 0
    # magical_vulnerable: int = 0

    shield_constant: float = 0

    def __post_init__(self):
        self.physical_shield_base = SHIELD_BASE_MAP[self.level]
        # self.magical_shield_base = self.SHIELD_BASE_MAP[self.level]
        self.shield_constant = SHIELD_SCALE * (LEVEL_SCALE * self.level - LEVEL_CONSTANT)
