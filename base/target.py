from dataclasses import dataclass

from base.constant import SHIELD_SCALE, SHIELD_BASE_MAP, LEVEL_SCALE, LEVEL_CONSTANT


@dataclass
class Target:
    level: int = 124

    physical_shield_base: int = 0
    magical_shield_base: int = 0

    physical_shield_gain: float = 0
    magical_shield_gain: float = 0

    _all_vulnerable: float = 0
    physical_vulnerable: float = 0
    magical_vulnerable: float = 0

    shield_constant: float = 0

    def __post_init__(self):
        if not self.physical_shield_base:
            self.physical_shield_base = SHIELD_BASE_MAP[self.level]
            self.magical_shield_base = SHIELD_BASE_MAP[self.level]
        if not self.shield_constant:
            self.shield_constant = SHIELD_SCALE * (LEVEL_SCALE * self.level - LEVEL_CONSTANT)

    @property
    def all_vulnerable(self):
        return self._all_vulnerable

    @all_vulnerable.setter
    def all_vulnerable(self, all_vulnerable):
        residual = all_vulnerable - self._all_vulnerable
        self.physical_vulnerable += residual
        self.magical_vulnerable += residual
        self._all_vulnerable = all_vulnerable
