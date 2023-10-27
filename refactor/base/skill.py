import random
from dataclasses import dataclass

from base.status import Status


@dataclass
class Snapshot:
    attack_power: float = 0
    critical_strike: float = 0
    critical_damage: int = 0
    strain: float = 0
    haste: float = 0

    damage_addition: float = 0


@dataclass
class Skill:
    name: str = None
    status: Status = None
    activate: bool = True

    is_cast: bool = True
    cast_while_casting: bool = False
    is_instant: bool = False
    is_snapshot: bool = False

    snapshot: Snapshot = None
    gcd_index: int = 0

    probability: float = 0
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

    base_damage_gain: float = 0
    rand_damage_gain: float = 0
    attack_power_cof_gain: float = 0
    weapon_damage_cof_gain: float = 0
    surplus_cof_gain: float = 0

    damage_addition_gain: float = 0
    shield_ignore_base: float = 0
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
    def attack_power_cof(self):
        return self.attack_power_cof_base + self.attack_power_cof_base * self.attack_power_cof_gain

    @property
    def weapon_damage_cof(self):
        return self.weapon_damage_cof_base + self.weapon_damage_cof_base * self.weapon_damage_cof_gain

    @property
    def surplus_cof(self):
        return self.surplus_cof_base + self.surplus_cof_base * self.surplus_cof_gain

    @property
    def attack_power(self):
        if self.snapshot:
            return self.snapshot.attack_power
        else:
            return self.status.attribute.attack_power

    @property
    def critical_strike(self):
        if self.snapshot:
            return self.snapshot.critical_strike
        else:
            return self.status.attribute.critical_strike + self.critical_strike_gain

    @property
    def critical_damage(self):
        if self.snapshot:
            return self.snapshot.critical_damage
        else:
            return self.status.attribute.critical_damage + self.critical_damage_gain

    @property
    def strain(self):
        if self.snapshot:
            return self.snapshot.strain
        else:
            return self.status.attribute.strain

    @property
    def haste(self):
        if self.snapshot:
            return self.snapshot.haste
        else:
            return self.status.attribute.haste

    @property
    def damage_addition(self):
        if self.snapshot:
            return self.snapshot.damage_addition
        else:
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
        return self.interval_base // (1 + self.haste)

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
        return self.gcd_base // (1 + self.haste)

    @property
    def cd(self):
        return self.cd_base

    def set_gcd(self):
        self.status.gcd_group[self.gcd_index] = self.gcd

    @property
    def roll(self):
        return random.random()

    """ action functions """

    def ready(self):
        self.status.energies[self.name] = self.energy

    def pre_cast(self):
        if self.is_cast:
            self.set_gcd()
            self.status.casting = self.intervals[0]
        if self.cd:
            if self.name in self.status.cds:
                self.status.cds[self.name] += self.cd
            else:
                self.status.cds[self.name] = self.cd

            self.status.energies[self.name] -= 1

        if self.is_snapshot:
            self.snapshot = Snapshot(attack_power=self.status.attribute.attack_power,
                                     critical_strike=self.critical_strike,
                                     critical_damage=self.critical_damage,
                                     strain=self.status.attribute.strain,
                                     haste=self.status.attribute.haste,
                                     damage_addition=self.damage_addition)

        self.status.counts[self.name] = 1

        if self.name not in self.status.intervals:
            self.status.intervals[self.name] = self.intervals[0]

        for effect in self.pre_cast_effect:
            effect(self)

    def cast(self):
        if not self.probability or self.roll < self.probability:
            self.pre_cast()

            if not self.base_damage:
                self.post_cast()

            if self.is_instant:
                self.status.counts[self.name] += 1
                self.status.intervals[self.name] = 0

            while self.name in self.status.intervals and self.status.intervals[self.name] == 0:
                self.damage()

    def post_cast(self):
        for effect in self.post_cast_effect:
            effect(self)

        self.status.counts[self.name] = 0
        if self.name in self.status.intervals:
            self.status.intervals.pop(self.name)
        # if self.is_cast:
        #     self.status.casting = 0

    def pre_damage(self):
        for effect in self.pre_damage_effect:
            effect(self)

    def damage(self):
        self.pre_damage()
        self.record()
        self.post_damage()

    def record(self):
        damage = self.cal_damage()

        self.status.record(self.name, "damage", damage)
        self.status.total_damage += damage

    def post_damage(self):
        for effect in self.post_damage_effect:
            effect(self)

        if self.status.counts[self.name] == self.count:
            self.post_cast()
        else:
            self.status.intervals[self.name] = self.intervals[self.status.counts[self.name]]
            if self.is_cast:
                self.status.casting = self.status.intervals[self.name]
            self.status.counts[self.name] += 1

    def cal_damage(self):
        damage = self.base_damage + self.rand_damage / 2
        damage = damage + self.attack_power_cof * self.attack_power
        damage = damage + self.weapon_damage_cof * self.status.attribute.weapon_damage
        damage = damage + self.surplus_cof * self.status.attribute.surplus

        damage = damage * (1 + self.damage_addition)

        damage = damage * (1 + self.strain)

        # if self.roll < self.critical_strike:
        #     damage += damage * self.critical_damage

        damage = damage * (1 + self.critical_strike * self.critical_damage)

        damage = damage * (1 + self.status.attribute.overcome)

        defense = self.status.attribute.target.defense(
            self.shield_ignore_base + self.status.attribute.shield_ignore_base,
            self.shield_ignore_gain + self.status.attribute.shield_ignore_gain
        )

        damage = damage * (1 - defense)
        damage = damage * (1 + self.status.attribute.pve_addition)
        damage = damage * (1 + self.status.attribute.target.vulnerable)
        damage = damage * (1 - self.status.attribute.level_reduction)
        return damage
