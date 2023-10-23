import random
from dataclasses import dataclass

from base.status import Status, Snapshot


@dataclass
class Skill:
    name: str = None
    status: Status = None
    activate: bool = True

    is_cast: bool = True
    cast_while_casting: bool = False
    is_instant: bool = False
    is_snapshot: bool = False

    gcd_index: int = 0

    count_base: int = 1
    interval_base: int = 0
    interval_list: list = None
    gcd_base: int = 24
    cd_base: int = 0
    energy: int = 1

    pre_cast_effect: list = None
    post_cast_effect: list = None
    pre_damage_effect: list = None
    post_damage_effect: list = None

    base_damage: int = 0
    weapon_damage_cof: int = 0
    surplus_cof = 0

    attack_power_cof_base: int = 0
    attack_power_cof_gain: int = 0

    damage_addition_gain: int = 0
    pve_addition_gain: int = 0
    shield_ignore_gain: int = 0
    critical_strike_gain: int = 0
    critical_damage_gain: int = 0

    def __post_init__(self):
        self.pre_cast_effect = []
        self.post_cast_effect = []
        self.pre_damage_effect = []
        self.post_damage_effect = []
        if not self.is_cast:
            self.gcd_base = 0

    """ attributes """
    @property
    def attack_power_cof(self):
        return self.attack_power_cof_base + self.attack_power_cof_base * self.attack_power_cof_gain
    
    @property
    def critical_strike(self):
        return self.status.attribute.critical_strike + self.critical_strike_gain
    
    @property
    def critical_damage(self):
        return self.status.attribute.critical_damage + self.critical_damage_gain

    @property
    def damage_addition(self):
        return self.status.attribute.damage_addition + self.damage_addition_gain

    """ skill detail"""
    @property
    def condition(self):
        return True

    @property
    def available(self):
        if not self.activate:
            return False
        if not self.status.gcd_group[self.gcd_index]:
            return False
        if not self.status.energies[self]:
            return False
        return self.condition

    @property
    def interval(self):
        return self.interval_base // (1 + self.status.attribute.haste)

    @property
    def count(self):
        if self.interval_list:
            return len(self.interval_list)
        else:
            return self.count_base

    @property
    def intervals(self):
        if self.interval_list:
            return self.interval_list
        else:
            return [self.interval] * self.count_base

    @property
    def gcd(self):
        return self.gcd_base // (1 + self.status.attribute.haste)

    @property
    def cd(self):
        return self.cd_base

    @property
    def snapshot(self):
        return Snapshot()

    def set_gcd(self):
        self.status.gcd_group[self.gcd_index] = self.gcd

    def set_dot(self):
        dot = self.status.buffs[self.name]
        if self.is_snapshot:
            dot.snapshot = self.snapshot

        dot.refresh(duration=sum([self.status.intervals[dot]] + self.intervals[1:]))

    @property
    def roll(self):
        return random.random()

    """ action functions """
    def recharge(self):
        self.status.energies[self] = self.energy

    def pre_cast(self):
        if self.gcd:
            self.set_gcd()
        if self.cd:
            self.status.cds[self] += self.cd
            self.status.energies[self] -= 1
        # self.status.set_casting(self.is_cast * self.duration)

        if self.count:
            self.status.counts[self] = self.count

        self.status.intervals[self] = self.intervals[0]
        for effect in self.pre_cast_effect:
            effect()

    def cast(self):
        self.pre_cast()

        if not self.base_damage:
            return

        if self.is_instant:
            self.status.counts[self] += 1
            self.status.intervals[self] = 0

        if not self.status.intervals[self]:
            self.damage()

    def post_cast(self):
        self.status.counts[self] = 0
        self.status.intervals[self] = 0

        # self.status.set_casting(0)

        for effect in self.post_cast_effect:
            effect()

    def pre_damage(self):
        for effect in self.pre_damage_effect:
            effect()

    def damage(self):
        self.pre_damage()
        # TODO: damage
        self.post_damage()

        if not self.status.counts[self]:
            self.post_cast()

    def post_damage(self):
        self.status.counts[self] -= 1
        self.status.intervals[self] = self.intervals[self.status.counts[self]]

        for effect in self.post_damage_effect:
            effect()


class Melee(Skill):
    pass

