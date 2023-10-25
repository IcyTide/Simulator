import random
from dataclasses import dataclass

from base.constant import DAMAGE_SCALE, PHYSICAL_DAMAGE_SCALE, INT_SCALE, SURPLUS_SCALE, DOT_DAMAGE_SCALE
from base.status import Status


@dataclass
class Skill:
    name: str = None
    status: Status = None
    activate: bool = True

    is_cast: bool = True
    cast_while_casting: bool = False
    is_instant: bool = False
    is_snapshot: bool = False
    is_dot: bool = False

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

    base_damage_base: float = 0
    rand_damage_base: float = 0

    attack_power_cof_base: float = 0
    weapon_damage_cof_base: float = 0
    surplus_cof_base: float = 0

    base_damage_gain: float = 1
    rand_damage_gain: float = 1
    attack_power_cof_gain: float = 1
    weapon_damage_cof_gain: float = 1

    damage_addition_gain: float = 1
    pve_addition_gain: float = 1
    shield_ignore_gain: float = 0
    critical_strike_gain: float = 0
    critical_damage_gain: float = 0

    def __post_init__(self):
        self.pre_cast_effect = []
        self.post_cast_effect = []
        self.pre_damage_effect = []
        self.post_damage_effect = []

    """ attributes """
    @property
    def base_damage(self):
        return self.base_damage_base + self.base_damage_base * self.base_damage_gain

    @property
    def rand_damage(self):
        return self.rand_damage_base + self.rand_damage_base * self.rand_damage_gain

    @property
    def base_attack_power_cof(self):
        return self.attack_power_cof_base + self.attack_power_cof_base * self.attack_power_cof_gain

    @property
    def attack_power_cof(self):
        if self.is_dot:
            return self.base_attack_power_cof * self.interval / DOT_DAMAGE_SCALE / PHYSICAL_DAMAGE_SCALE
        else:
            return self.base_attack_power_cof / DAMAGE_SCALE / PHYSICAL_DAMAGE_SCALE

    @property
    def base_weapon_damage_cof(self):
        return self.weapon_damage_cof_base + self.weapon_damage_cof_base * self.weapon_damage_cof_gain

    @property
    def weapon_damage_cof(self):
        return self.base_weapon_damage_cof // INT_SCALE

    @property
    def base_surplus_cof(self):
        return self.surplus_cof + 1 if self.surplus_cof < 0 else self.surplus_cof

    @property
    def surplus_cof(self):
        return (self.base_surplus_cof // INT_SCALE + INT_SCALE) // INT_SCALE * SURPLUS_SCALE

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
        if self.status.gcd_group[self.gcd_index]:
            return False
        if not self.status.energies[self.name]:
            return False
        if self.status.casting and not self.cast_while_casting:
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
        if self.is_cast:
            return self.gcd_base // (1 + self.status.attribute.haste)
        else:
            return 0

    @property
    def cd(self):
        return self.cd_base

    @property
    def snapshot(self):
        return {k: v for k, v in self.status.stacks.items() if v}

    def set_gcd(self):
        self.status.gcd_group[self.gcd_index] = self.gcd

    def set_buff(self):
        buff = self.status.buffs[self.name]
        if self.is_snapshot:
            buff.snapshot = self.snapshot

        if self.name in self.status.intervals:
            buff.refresh(duration=sum([self.status.intervals[self.name]] + self.intervals[1:]))
        else:
            buff.refresh()

    @property
    def roll(self):
        return random.random()

    """ action functions """
    def recharge(self):
        self.status.energies[self.name] = self.energy

    def pre_cast(self):
        if self.gcd:
            self.set_gcd()
        if self.cd:
            if self.name in self.status.cds:
                self.status.cds[self.name] += self.cd
            else:
                self.status.cds[self.name] = self.cd

            self.status.energies[self.name] -= 1
        # self.status.set_casting(self.is_cast * self.duration)

        self.status.counts[self.name] = self.count
        self.status.intervals[self.name] = self.intervals[0]

        if self.is_cast:
            self.status.casting = self.status.intervals[self.name]
        for effect in self.pre_cast_effect:
            effect(self)

    def cast(self):
        self.pre_cast()

        if not self.base_damage:
            self.post_cast()

        if self.is_instant:
            self.status.counts[self.name] += 1
            self.status.intervals[self.name] = 0

        while self.name in self.status.intervals and not self.status.intervals[self.name]:
            self.damage()

    def post_cast(self):
        self.status.counts[self.name] = 0
        self.status.intervals.pop(self.name)

        # self.status.set_casting(0)

        for effect in self.post_cast_effect:
            effect(self)

    def pre_damage(self):
        for effect in self.pre_damage_effect:
            effect(self)

    def damage(self):
        self.pre_damage()
        self.record()
        self.post_damage()

        if not self.status.counts[self.name]:
            self.post_cast()

    def record(self):
        if self.is_snapshot:
            self.status.record(self.name, "damage", self.status.buffs[self.name].snapshot)
        else:
            self.status.record(self.name, "damage", self.snapshot)
        if self.surplus_cof_base:
            self.status.record(self.name + "-破招", "damage", self.snapshot)

    def post_damage(self):
        self.status.counts[self.name] -= 1
        self.status.intervals[self.name] = self.intervals[self.status.counts[self.name]]

        if self.is_cast:
            self.status.casting = self.status.intervals[self.name]

        for effect in self.post_damage_effect:
            effect(self)
