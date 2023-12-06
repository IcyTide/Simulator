import random

from dataclasses import dataclass
from functools import cache

from base.status import Status


@dataclass
class PhysicalSnapshot:
    agility_base: int = 0,
    agility_gain: float = 0,
    strength_base: int = 0,
    strength_gain: float = 0,
    physical_attack_power_base: int = 0,
    physical_attack_power_gain: float = 0,
    physical_critical_strike_base: int = 0,
    physical_critical_strike_gain: float = 0,
    physical_critical_power_base: int = 0,
    physical_critical_power_gain: float = 0,
    strain_base: int = 0,
    strain_gain: float = 0,
    damage_addition: float = 0,

    critical_strike: float = 0,
    haste: float = 0


@dataclass
class MagicalSnapshot:
    spirit_base: int = 0,
    spirit_gain: float = 0,
    spunk_base: int = 0,
    spunk_gain: float = 0,
    magical_attack_power_base: int = 0,
    magical_attack_power_gain: float = 0,
    magical_critical_strike_base: int = 0,
    magical_critical_strike_gain: float = 0,
    magical_critical_power_base: int = 0,
    magical_critical_power_gain: float = 0,
    strain_base: int = 0,
    strain_gain: float = 0,
    damage_addition: float = 0,

    critical_strike: float = 0,
    haste: float = 0


@dataclass
class Skill:
    status: Status
    name: str = None
    activate: bool = True

    is_cast: bool = True
    is_hit: bool = True
    is_stack: bool = False
    is_instant: bool = False
    is_overdraw: bool = False
    is_snapshot: bool = False

    cast_while_casting: bool = False
    cd_with_haste: bool = False

    gcd_index: any = 0

    probability: float = 1
    count_base: int = 1
    interval_base: int = 0
    interval_list: list = None
    gcd_base: int = 24
    cd_base: int = 0
    energy: int = 1

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
    skill_shield_gain: float = 0
    skill_shield_ignore: float = 0
    skill_critical_strike: float = 0
    skill_critical_power: float = 0

    level_params: dict = None
    snapshot = None

    def __post_init__(self):
        self.pre_cast_effect = []
        self.post_cast_effect = []
        self.critical_hit_effect = []
        self.post_hit_effect = []

        self.snapshot = self
        self.attribute = self.status.attribute
        self.target = self.status.target

    """ attributes """

    @property
    def strain_base(self):
        return self.attribute.strain_base

    @property
    def strain_gain(self):
        return self.attribute.strain_gain

    @property
    def damage_addition(self):
        return self.attribute.damage_addition + self.skill_damage_addition

    @property
    def pve_addition(self):
        return self.attribute.pve_addition + self.skill_pve_addition

    @property
    def critical_strike(self):
        raise NotImplementedError

    @property
    def haste(self):
        return self.attribute.haste

    """ skill detail """

    @property
    def condition(self):
        return True

    @property
    def available(self):
        if not self.activate:
            return False
        if self.status.gcd_group.get(self.gcd_index):
            return False
        if self.status.energies[self.name] == 0:
            return False
        if self.status.casting and not self.cast_while_casting:
            return False
        return self.condition

    @staticmethod
    @cache
    def apply_haste(value, scale):
        return int(value / (1 + scale))

    @property
    def stack(self):
        if self.is_stack:
            return self.status.stacks[self.name]
        return 1

    @property
    def count(self):
        if self.interval_list:
            return len(self.interval_list)
        return self.count_base + int(self.is_instant)

    @property
    def interval(self):
        if self.interval_list:
            return self.interval_list[self.status.counts[self.name]]
        return self.apply_haste(self.interval_base, self.snapshot.haste)

    @property
    def duration(self):
        if self.interval_list:
            return sum(self.interval_list)
        return self.interval * self.count

    @property
    def gcd(self):
        return self.apply_haste(self.gcd_base, self.haste)

    @property
    def cd(self):
        if self.cd_with_haste:
            return self.apply_haste(self.cd_base, self.haste)
        return self.cd_base

    @property
    def roll(self):
        return random.random()

    """ action functions """

    def recharge(self):
        if self.is_overdraw:
            self.status.energies[self.name] = self.energy
            self.status.cds.pop(self.name)
        else:
            self.status.energies[self.name] += 1
            if self.status.energies[self.name] < self.energy:
                self.set_cd()
            else:
                self.status.cds.pop(self.name)

    def set_cd(self):
        cd = self.status.cds.get(self.name, 0)
        if self.is_overdraw:
            self.status.cds[self.name] = self.cd + cd
        else:
            self.status.cds[self.name] = cd if cd else self.cd

    def consume(self):
        critical = self.roll < self.snapshot.critical_strike
        count = self.count - self.status.counts[self.name]
        self.record(critical, count)

        self.status.buffs[self.name].clear()
        self.post_cast()

    def pre_cast(self):
        if self.is_cast:
            self.status.casting = self.duration
            if self.gcd_base:
                self.status.gcd_group[self.gcd_index] = self.gcd
        if self.cd_base:
            self.set_cd()
            self.status.energies[self.name] -= 1
        if self.is_instant:
            self.status.intervals[self.name] = 0
        if self.is_snapshot:
            self.save_snapshot()

        self.status.counts[self.name] = 0

        for effect in self.pre_cast_effect:
            effect(self)

    def cast(self, level=None):
        if self.roll >= self.probability:
            return

        if level:
            for attr, values in self.level_params.items():
                setattr(self, attr, values[level - 1])

        self.pre_cast()

        if not self.damage_base:
            self.post_cast()
            return

        if self.name not in self.status.intervals:
            self.status.intervals[self.name] = self.interval

        while self.status.intervals.get(self.name) == 0:
            self.hit()

    def critical_hit(self):
        for effect in self.critical_hit_effect:
            effect(self)

    def hit(self):
        critical = self.roll < self.snapshot.critical_strike
        self.record(critical)

        if critical:
            self.critical_hit()

        self.post_hit()

    def record(self, critical, count=1):
        self.status.record(self.record_damage(critical, count))

    def post_hit(self):
        for effect in self.post_hit_effect:
            effect(self)

        self.status.counts[self.name] += 1

        if self.status.counts[self.name] == self.count:
            self.post_cast()
        else:
            self.status.intervals[self.name] = self.interval

    def post_cast(self):
        for effect in self.post_cast_effect:
            effect(self)

        if self.is_cast:
            self.status.casting = 0

        self.status.counts.pop(self.name)

        if self.name in self.status.intervals:
            self.status.intervals.pop(self.name)

    def record_damage(self, critical, count):
        raise NotImplementedError

    def save_snapshot(self):
        raise NotImplementedError


class PhysicalSkill(Skill):

    @property
    def agility_base(self):
        return self.attribute.agility_base

    @property
    def agility_gain(self):
        return self.attribute.agility_gain

    @property
    def strength_base(self):
        return self.attribute.strength_base

    @property
    def strength_gain(self):
        return self.attribute.strength_gain

    @property
    def physical_attack_power_base(self):
        return self.attribute.physical_attack_power_base

    @property
    def physical_attack_power_gain(self):
        return self.attribute.physical_attack_power_gain

    @property
    def physical_critical_strike_base(self):
        return self.attribute.physical_critical_strike_base

    @property
    def physical_critical_strike_gain(self):
        return self.attribute.physical_critical_strike_gain + self.skill_critical_strike

    @property
    def physical_critical_power_base(self):
        return self.attribute.physical_critical_power_base

    @property
    def physical_critical_power_gain(self):
        return self.attribute.physical_critical_power_gain + self.skill_critical_power

    @property
    def critical_strike(self):
        return self.attribute.physical_critical_strike + self.skill_critical_strike

    def save_snapshot(self):
        self.snapshot = PhysicalSnapshot(
            strength_base=self.strength_base,
            strength_gain=self.strength_gain,
            agility_base=self.agility_base,
            agility_gain=self.agility_gain,
            physical_attack_power_base=self.physical_attack_power_base,
            physical_attack_power_gain=self.physical_attack_power_gain,
            physical_critical_strike_base=self.physical_critical_strike_base,
            physical_critical_strike_gain=self.physical_critical_strike_gain,
            physical_critical_power_base=self.physical_critical_power_base,
            physical_critical_power_gain=self.physical_critical_power_gain,
            strain_base=self.strain_base,
            strain_gain=self.strain_gain,
            damage_addition=self.damage_addition + self.skill_damage_addition,
            critical_strike=self.critical_strike,
            haste=self.haste
        )

    def record_damage(self, critical: bool, count: int):
        return (
            (
                ('agility_base', self.snapshot.agility_base),
                ('agility_gain', self.snapshot.agility_gain),
                ('strength_base', self.snapshot.strength_base),
                ('strength_gain', self.snapshot.strength_gain),
                ('surplus', self.attribute.surplus),
                ('strain_base', self.snapshot.strain_base),
                ('strain_gain', self.snapshot.strain_gain),
                ('physical_attack_power_base', self.snapshot.physical_attack_power_base),
                ('physical_attack_power_gain', self.snapshot.physical_attack_power_gain),
                ('physical_critical_strike_base', self.snapshot.physical_critical_strike_base),
                ('physical_critical_strike_gain', self.snapshot.physical_critical_strike_gain),
                ('physical_critical_power_base', self.snapshot.physical_critical_power_base),
                ('physical_critical_power_gain', self.snapshot.physical_critical_power_gain),
                ('physical_overcome_base', self.attribute.physical_overcome_base),
                ('physical_overcome_gain', self.attribute.physical_overcome_gain),
                ('weapon_damage_base', self.attribute.weapon_damage_base),
                ('weapon_damage_rand', self.attribute.weapon_damage_rand),
                ('weapon_damage_gain', self.attribute.weapon_damage_gain)
            ),
            (
                ('skill', self.name),
                ('critical', critical),
                ('stack', self.stack * count),
                ('damage_base', self.damage_base),
                ('damage_rand', self.damage_rand),
                ('damage_gain', self.damage_gain),
                ('attack_power_cof', self.attack_power_cof),
                ('weapon_damage_cof', self.weapon_damage_cof),
                ('surplus_cof', self.surplus_cof),
                ('attack_power_cof_gain', self.attack_power_cof_gain),
                ('weapon_damage_cof_gain', self.weapon_damage_cof_gain),
                ('surplus_cof_gain', self.surplus_cof_gain),

                ('level', self.attribute.level),
                ('damage_addition', self.damage_addition),
                ('pve_addition', self.pve_addition),
                ('shield_ignore', self.attribute.physical_shield_ignore + self.skill_shield_ignore),

                ('target_level', self.target.level),
                ('shield_base', self.target.physical_shield_base),
                ('shield_gain', self.target.physical_shield_gain + self.skill_shield_gain),
                ('vulnerable', self.target.physical_vulnerable),
                ('shield_constant', self.target.shield_constant),

            )
        )


class MagicalSkill(Skill):
    @property
    def spirit_base(self):
        return self.attribute.spirit_base

    @property
    def spirit_gain(self):
        return self.attribute.spirit_gain

    @property
    def spunk_base(self):
        return self.attribute.spunk_base

    @property
    def spunk_gain(self):
        return self.attribute.spunk_gain

    @property
    def magical_attack_power_base(self):
        return self.attribute.magical_attack_power_base

    @property
    def magical_attack_power_gain(self):
        return self.attribute.magical_attack_power_gain

    @property
    def magical_critical_strike_base(self):
        return self.attribute.magical_critical_strike_base

    @property
    def magical_critical_strike_gain(self):
        return self.attribute.magical_critical_strike_gain + self.skill_critical_strike

    @property
    def magical_critical_power_base(self):
        return self.attribute.magical_critical_power_base

    @property
    def magical_critical_power_gain(self):
        return self.attribute.magical_critical_power_gain + self.skill_critical_power

    @property
    def critical_strike(self):
        return self.attribute.magical_critical_strike + self.skill_critical_strike

    def save_snapshot(self):
        self.snapshot = MagicalSnapshot(
            spunk_base=self.spunk_base,
            spunk_gain=self.spunk_gain,
            spirit_base=self.spirit_base,
            spirit_gain=self.spirit_gain,
            magical_attack_power_base=self.magical_attack_power_base,
            magical_attack_power_gain=self.magical_attack_power_gain,
            magical_critical_strike_base=self.magical_critical_strike_base,
            magical_critical_strike_gain=self.magical_critical_strike_gain,
            magical_critical_power_base=self.magical_critical_power_base,
            magical_critical_power_gain=self.magical_critical_power_gain,
            strain_base=self.strain_base,
            strain_gain=self.strain_gain,
            damage_addition=self.damage_addition + self.skill_damage_addition,
            critical_strike=self.critical_strike,
            haste=self.haste
        )

    def record_damage(self, critical: bool, count: int):
        return (
            (
                ('spirit_base', self.snapshot.spirit_base),
                ('spirit_gain', self.snapshot.spirit_gain),
                ('spunk_base', self.snapshot.spunk_base),
                ('spunk_gain', self.snapshot.spunk_gain),
                ('surplus', self.attribute.surplus),
                ('strain_base', self.snapshot.strain_base),
                ('strain_gain', self.snapshot.strain_gain),
                ('magical_attack_power_base', self.snapshot.magical_attack_power_base),
                ('magical_attack_power_gain', self.snapshot.magical_attack_power_gain),
                ('magical_critical_strike_base', self.snapshot.magical_critical_strike_base),
                ('magical_critical_strike_gain', self.snapshot.magical_critical_strike_gain),
                ('magical_critical_power_base', self.snapshot.magical_critical_power_base),
                ('magical_critical_power_gain', self.snapshot.magical_critical_power_gain),
                ('magical_overcome_base', self.attribute.magical_overcome_base),
                ('magical_overcome_gain', self.attribute.magical_overcome_gain),
                ('weapon_damage_base', self.attribute.weapon_damage_base),
                ('weapon_damage_rand', self.attribute.weapon_damage_rand),
                ('weapon_damage_gain', self.attribute.weapon_damage_gain)
            ),
            (
                ('skill', self.name),
                ('critical', critical),
                ('stack', self.stack * count),
                ('damage_base', self.damage_base),
                ('damage_rand', self.damage_rand),
                ('damage_gain', self.damage_gain),
                ('attack_power_cof', self.attack_power_cof),
                ('weapon_damage_cof', self.weapon_damage_cof),
                ('surplus_cof', self.surplus_cof),
                ('attack_power_cof_gain', self.attack_power_cof_gain),
                ('weapon_damage_cof_gain', self.weapon_damage_cof_gain),
                ('surplus_cof_gain', self.surplus_cof_gain),

                ('level', self.attribute.level),
                ('damage_addition', self.damage_addition),
                ('pve_addition', self.pve_addition),
                ('shield_ignore', self.attribute.magical_shield_ignore + self.skill_shield_ignore),

                ('target_level', self.target.level),
                ('shield_base', self.target.magical_shield_base),
                ('shield_gain', self.target.magical_shield_gain + self.skill_shield_gain),
                ('vulnerable', self.target.magical_vulnerable),
                ('shield_constant', self.target.shield_constant),
            )
        )
