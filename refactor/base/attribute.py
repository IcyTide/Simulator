from dataclasses import dataclass

from base.constant import *





@dataclass
class Source:
    target: Target
    attribute: Attribute

    weapon_damage_rand: int = 0
    weapon_damage_base: int = 0
    weapon_damage_gain: int = 0

    physical_shield_ignore: int = 0
    magical_shield_ignore: int = 0


    """"""

    @property
    def physical_shield(self):
        return self.target.physical_shield - self.target.physical_shield * self.physical_shield_ignore // INT_SCALE

    @property
    def magical_shield(self):
        return self.target.magical_shield - self.target.magical_shield * self.magical_shield_ignore // INT_SCALE
