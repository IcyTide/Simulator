import random
from dataclasses import dataclass
from functools import cache

from base.damage import hit_damage, defense
from base.status import Status


@dataclass
class Snapshot:
    attack_power: int = 0

    critical_strike: float = 0
    critical_power: float = 0

    strain: float = 0
    haste: float = 0
    damage_addition: float = 0

    skill_critical_strike: float = 0
    skill_critical_power: float = 0
    skill_damage_addition: float = 0


@dataclass
class Skill:
    name: str = None
    status: Status = None
    activate: bool = True

    is_cast: bool = True
    cast_while_casting: bool = False
    is_hit: bool = True
    is_instant: bool = False
    is_snapshot: bool = False

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
    critical_hit_effect: list = None
    pre_hit_effect: list = None
    post_hit_effect: list = None

    damage_base: int = 0
    damage_rand: int = 0
    attack_power_cof: float = 0
    weapon_damage_cof: float = 0
    surplus_cof: float = 0

    damage_gain: float = 0
    attack_power_cof_gain: float = 0
    weapon_damage_cof_gain: float = 0
    surplus_cof_gain: float = 0

    skill_damage_addition: float = 0
    skill_pve_addition: float = 0
    skill_shield_ignore_base: float = 0
    skill_shield_ignore_gain: float = 0
    skill_critical_strike: float = 0
    skill_critical_power: float = 0
    skill_cd_reduction: float = 0

    snapshot: [Snapshot, "Skill"] = None

    def __post_init__(self):
        self.pre_cast_effect = []
        self.post_cast_effect = []
        self.pre_hit_effect = []
        self.critical_hit_effect = []
        self.post_hit_effect = []

        self.snapshot = self

    """ attributes """

    @property
    def attack_power(self):
        raise NotImplementedError

    @property
    def critical_strike(self):
        raise NotImplementedError

    @property
    def critical_power(self):
        raise NotImplementedError

    @property
    def strain(self):
        return self.status.attribute.strain

    @property
    def haste(self):
        return self.status.attribute.haste

    @property
    def damage_addition(self):
        return self.status.attribute.damage_addition

    """ skill detail"""

    @property
    def condition(self):
        return True

    @property
    def available(self):
        if not self.activate:
            return False
        if self.status.gcd_group.get(self.gcd_index):
            return False
        if not self.status.energies[self.name]:
            return False
        if self.status.casting and not self.cast_while_casting:
            return False
        return self.condition

    @property
    def interval(self):
        if self.interval_list:
            return self.interval_list[self.status.counts[self.name]]
        else:
            return self.apply_scale(self.interval_base, self.snapshot.haste)

    @property
    def count(self):
        if self.interval_list:
            return len(self.interval_list)
        else:
            return self.count_base

    @property
    def duration(self):
        if self.interval_list:
            return sum(self.interval_list)
        else:
            return self.interval * self.count

    @property
    def gcd(self):
        return self.apply_scale(self.gcd_base, self.haste)

    @property
    def cd(self):
        return self.cd_base

    @property
    def roll(self):
        return random.random()

    @staticmethod
    @cache
    def apply_scale(value, scale):
        return int(value / (1 + scale))

    """ action functions """

    def recharge(self):
        self.status.energies[self.name] = self.energy

        if self.name in self.status.cds:
            self.status.cds.pop(self.name)

    def pre_cast(self):
        self.status.counts[self.name] = 0

        if self.name not in self.status.intervals:
            self.status.intervals[self.name] = self.interval
        if self.is_cast:
            self.status.casting = self.duration
            if self.gcd:
                self.status.gcd_group[self.gcd_index] = self.gcd
        if self.cd:
            self.status.cds[self.name] = self.cd + self.status.cds.get(self.name, 0)
            self.status.energies[self.name] -= 1
        if self.is_snapshot:
            self.snapshot = Snapshot(
                attack_power=self.attack_power,
                critical_strike=self.critical_strike,
                critical_power=self.critical_power,
                strain=self.strain,
                haste=self.haste,
                damage_addition=self.damage_addition,
                skill_critical_strike=self.skill_critical_strike,
                skill_critical_power=self.skill_critical_power,
                skill_damage_addition=self.skill_damage_addition
            )

        for effect in self.pre_cast_effect:
            effect(self)

    def cast(self):
        if self.probability and self.roll >= self.probability:
            return

        self.pre_cast()

        if not self.damage_base:
            self.post_cast()
            return

        while self.status.intervals.get(self.name) == 0:
            self.hit()

    def post_cast(self):
        for effect in self.post_cast_effect:
            effect(self)

        if self.is_cast:
            self.status.casting = 0

        self.status.counts.pop(self.name)

        if self.name in self.status.intervals:
            self.status.intervals.pop(self.name)

    def pre_hit(self):
        for effect in self.pre_hit_effect:
            effect(self)

    def critical_hit(self):
        for effect in self.critical_hit_effect:
            effect()

    def hit(self):
        self.pre_hit()

        critical = self.roll < self.snapshot.critical_strike + self.snapshot.skill_critical_strike
        self.record(critical)

        if critical:
            self.critical_hit()
        self.post_hit()

    def record(self, critical):
        if critical:
            self.status.record(self.name, "critical", self.critical_damage)
        else:
            self.status.record(self.name, "hit", self.hit_damage)

    def post_hit(self):
        for effect in self.post_hit_effect:
            effect(self)

        self.status.counts[self.name] += 1

        if self.status.counts[self.name] == self.count:
            self.post_cast()
        else:
            self.status.intervals[self.name] = self.interval

    @property
    def hit_damage(self):
        raise NotImplementedError

    @property
    def critical_damage(self):
        raise NotImplementedError


class PhysicalSkill(Skill):
    @property
    def attack_power(self):
        return self.status.attribute.physical_attack_power

    @property
    def critical_strike(self):
        return self.status.attribute.physical_critical_strike

    @property
    def critical_power(self):
        return self.status.attribute.physical_critical_power

    @property
    def hit_damage(self):
        defense_reduction = defense(
            shield_base=self.status.attribute.target.physical_shield_base,
            shield_gain=self.status.attribute.target.physical_shield_gain,
            shield_ignore_base=self.status.attribute.physical_shield_ignore_base,
            shield_ignore_gain=self.status.attribute.physical_shield_ignore_gain,
            skill_shield_ignore_base=self.skill_shield_ignore_base,
            skill_shield_ignore_gain=self.skill_shield_ignore_gain,
            shield_constant=self.status.attribute.target.shield_constant
        )
        return hit_damage(
            self.damage_base, self.damage_rand, self.attack_power_cof, self.weapon_damage_cof, self.surplus_cof,
            self.damage_gain, self.attack_power_cof_gain, self.weapon_damage_cof_gain, self.surplus_cof_gain,
            self.snapshot.attack_power, self.status.attribute.weapon_damage, self.status.attribute.surplus,
            self.snapshot.damage_addition, self.snapshot.skill_damage_addition,
            self.status.attribute.physical_overcome, defense_reduction,
            1, 0,
            self.snapshot.strain, self.status.attribute.level_reduction,
            self.status.attribute.pve_addition, self.skill_pve_addition,
            self.status.attribute.target.physical_vulnerable)

    @property
    def critical_damage(self):
        defense_reduction = defense(
            shield_base=self.status.attribute.target.physical_shield_base,
            shield_gain=self.status.attribute.target.physical_shield_gain,
            shield_ignore_base=self.status.attribute.physical_shield_ignore_base,
            shield_ignore_gain=self.status.attribute.physical_shield_ignore_gain,
            skill_shield_ignore_base=self.skill_shield_ignore_base,
            skill_shield_ignore_gain=self.skill_shield_ignore_gain,
            shield_constant=self.status.attribute.target.shield_constant
        )
        return hit_damage(
            self.damage_base, self.damage_rand, self.attack_power_cof, self.weapon_damage_cof, self.surplus_cof,
            self.damage_gain, self.attack_power_cof_gain, self.weapon_damage_cof_gain, self.surplus_cof_gain,
            self.snapshot.attack_power, self.status.attribute.weapon_damage, self.status.attribute.surplus,
            self.snapshot.damage_addition, self.snapshot.skill_damage_addition,
            self.status.attribute.physical_overcome, defense_reduction,
            self.snapshot.critical_power, self.snapshot.skill_critical_power,
            self.snapshot.strain, self.status.attribute.level_reduction,
            self.status.attribute.pve_addition, self.skill_pve_addition,
            self.status.attribute.target.physical_vulnerable)
