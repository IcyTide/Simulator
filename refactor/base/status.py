from dataclasses import dataclass, field

from base import Timeline
from base.constant import *
from base.attribute import Attribute


class Source:
    pass


@dataclass
class Target:
    physical_shield: int = 0
    magical_shield: int = 0
    physical_vulnerable: int = 0
    magical_vulnerable: int = 0


@dataclass
class Status:
    timeline: Timeline

    attribute: Attribute
    snapshots: dict

    source: Source
    target: Target

    gcd: list
    casting: int = 0

    weapon_damage_rand: int = 0
    weapon_damage_base: int = 0
    weapon_damage_gain: int = 0

    physical_shield_ignore: int = 0
    magical_shield_ignore: int = 0

    @property
    def base_weapon_damage(self):
        return self.weapon_damage_base + self.weapon_damage_rand / 2

    @property
    def weapon_damage(self):
        return self.weapon_damage_base + \
               self.weapon_damage_base * self.weapon_damage_gain // INT_SCALE + \
               self.weapon_damage_rand / 2

    @property
    def physical_shield(self):
        return self.target.physical_shield * (1 - self.physical_shield_ignore)

    @property
    def magical_shield(self):
        return self.target.physical_shield * (1 - self.magical_shield_ignore)

    """ timeline functions"""
    def insert(self):
        gaps = (e for e in (self.casting, *self.gcd) if e > 0)
        if gaps:
            self.timeline.set(min(gaps), self)

    def set_casting(self, casting):
        self.casting = max(casting, 0)

    def add_casting(self, casting):
        self.set_casting(self.casting + casting)

    def set_gcd(self, index, gcd):
        self.gcd[index] = max(gcd, 0)

    def add_gcd(self, index, gcd):
        self.set_gcd(index, self.gcd[index] + gcd)

    def update(self, gap):
        self.add_casting(-gap)
        self.gcd = [self.add_gcd(index, -gap) for index, gcd in enumerate(self.gcd)]
        self.insert()
