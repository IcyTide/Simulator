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
    name: str = None
    status: Status = None
    activate: bool = True

    is_cast: bool = True
    cast_while_casting: bool = False
    is_hit: bool = True
    is_dot: bool = True
    is_instant: bool = False
    is_overdraw: bool = False
    is_snapshot: bool = False

    gcd_index: any = 0

    probability: float = 1
    count_base: int = 1
    interval_base: int = 0
    interval_list: list = None
    gcd_base: int = 24
    cd_base: int = 0
    energy: int = 1

    pre_cast_effect: list = None
    post_cast_effect: list = None
    critical_hit_effect: list = None
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
    skill_shield_gain: float = 0
    skill_shield_ignore: float = 0
    skill_critical_strike: float = 0
    skill_critical_power: float = 0

    snapshot: [PhysicalSnapshot, "Skill"] = None

    def __post_init__(self):
        self.pre_cast_effect = []
        self.post_cast_effect = []
        self.critical_hit_effect = []
        self.post_hit_effect = []

        self.snapshot = self

    """ attributes """

    @property
    def strain_base(self):
        return self.status.attribute.strain_base

    @property
    def strain_gain(self):
        return self.status.attribute.strain_gain

    @property
    def damage_addition(self):
        return self.status.attribute.damage_addition + self.skill_damage_addition

    @property
    def pve_addition(self):
        return self.status.attribute.pve_addition + self.skill_pve_addition

    @property
    def critical_strike(self):
        raise NotImplementedError

    @property
    def haste(self):
        return self.status.attribute.haste

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
        if self.is_dot:
            return self.status.buffs[self.name]
        else:
            return 1

    @property
    def interval(self):
        if self.interval_list:
            return self.interval_list[self.status.counts[self.name]]
        else:
            return self.apply_haste(self.interval_base, self.snapshot.haste)

    @property
    def count(self):
        if self.interval_list:
            return len(self.interval_list)
        else:
            return self.count_base + int(self.is_instant)

    @property
    def duration(self):
        if self.interval_list:
            return sum(self.interval_list)
        else:
            return self.interval * self.count

    @property
    def gcd(self):
        return self.apply_haste(self.gcd_base, self.haste)

    @property
    def cd(self):
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

    def cast(self):
        if self.roll >= self.probability:
            return

        self.pre_cast()

        if not self.damage_base:
            self.post_cast()
            return

        if self.name not in self.status.intervals:
            self.status.intervals[self.name] = self.interval

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

    def critical_hit(self):
        for effect in self.critical_hit_effect:
            effect(self)

    def hit(self):
        critical = self.roll < self.snapshot.critical_strike
        self.record(critical)

        if critical:
            self.critical_hit()

        self.post_hit()

    def record(self, critical):
        self.status.record(self.record_damage(critical))

    def post_hit(self):
        for effect in self.post_hit_effect:
            effect(self)

        self.status.counts[self.name] += 1

        if self.status.counts[self.name] == self.count:
            self.post_cast()
        else:
            self.status.intervals[self.name] = self.interval

    def record_damage(self, critical):
        raise NotImplementedError

    def save_snapshot(self):
        raise NotImplementedError


class PhysicalSkill(Skill):
    @property
    def agility_base(self):
        return self.status.attribute.agility_base

    @property
    def agility_gain(self):
        return self.status.attribute.agility_gain

    @property
    def strength_base(self):
        return self.status.attribute.strength_base

    @property
    def strength_gain(self):
        return self.status.attribute.strength_gain

    @property
    def physical_attack_power_base(self):
        return self.status.attribute.physical_attack_power_base

    @property
    def physical_attack_power_gain(self):
        return self.status.attribute.physical_attack_power_gain

    @property
    def physical_critical_strike_base(self):
        return self.status.attribute.physical_critical_strike_base

    @property
    def physical_critical_strike_gain(self):
        return self.status.attribute.physical_critical_strike_gain + self.skill_critical_strike

    @property
    def physical_critical_power_base(self):
        return self.status.attribute.physical_critical_power_base

    @property
    def physical_critical_power_gain(self):
        return self.status.attribute.physical_critical_power_gain + self.skill_critical_power

    @property
    def critical_strike(self):
        return self.status.attribute.physical_critical_strike + self.skill_critical_strike

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

    def record_damage(self, critical: bool):
        snapshot = self.snapshot
        attribute = self.status.attribute
        target = self.status.target
        return (
            (
                ('agility_base', snapshot.agility_base),
                ('agility_gain', snapshot.agility_gain),
                ('strength_base', snapshot.strength_base),
                ('strength_gain', snapshot.strength_gain),
                ('surplus', attribute.surplus),
                ('strain_base', snapshot.strain_base),
                ('strain_gain', snapshot.strain_gain),
                ('physical_attack_power_base', snapshot.physical_attack_power_base),
                ('physical_attack_power_gain', snapshot.physical_attack_power_gain),
                ('physical_critical_strike_base', snapshot.physical_critical_strike_base),
                ('physical_critical_strike_gain', snapshot.physical_critical_strike_gain),
                ('physical_critical_power_base', snapshot.physical_critical_power_base),
                ('physical_critical_power_gain', snapshot.physical_critical_power_gain),
                ('physical_overcome_base', attribute.physical_overcome_base),
                ('physical_overcome_gain', attribute.physical_overcome_gain),
                ('weapon_damage_base', attribute.weapon_damage_base),
                ('weapon_damage_rand', attribute.weapon_damage_rand),
                ('weapon_damage_gain', attribute.weapon_damage_gain)
            ),
            (
                ('level', attribute.level),
                ('damage_addition', self.damage_addition),
                ('pve_addition', self.pve_addition),
                ('shield_ignore', attribute.physical_shield_ignore + self.skill_shield_ignore),

                ('target_level', target.level),
                ('shield_base', target.physical_shield_base),
                ('shield_gain', target.physical_shield_gain + self.skill_shield_gain),
                ('vulnerable', target.physical_vulnerable),
                ('shield_constant', target.shield_constant),

                ('skill', self.name),
                ('critical', critical),
                ('stack', self.stack),
                ('damage_base', self.damage_base),
                ('damage_rand', self.damage_rand),
                ('damage_gain', self.damage_gain),
                ('attack_power_cof', self.attack_power_cof),
                ('weapon_damage_cof', self.weapon_damage_cof),
                ('surplus_cof', self.surplus_cof),
                ('attack_power_cof_gain', self.attack_power_cof_gain),
                ('weapon_damage_cof_gain', self.weapon_damage_cof_gain),
                ('surplus_cof_gain', self.surplus_cof_gain)
            )
        )


class MagicalSkill(Skill):
    @property
    def spirit_base(self):
        return self.status.attribute.spirit_base

    @property
    def spirit_gain(self):
        return self.status.attribute.spirit_gain

    @property
    def spunk_base(self):
        return self.status.attribute.spunk_base

    @property
    def spunk_gain(self):
        return self.status.attribute.spunk_gain

    @property
    def magical_attack_power_base(self):
        return self.status.attribute.magical_attack_power_base

    @property
    def magical_attack_power_gain(self):
        return self.status.attribute.magical_attack_power_gain

    @property
    def magical_critical_strike_base(self):
        return self.status.attribute.magical_critical_strike_base

    @property
    def magical_critical_strike_gain(self):
        return self.status.attribute.magical_critical_strike_gain + self.skill_critical_strike

    @property
    def magical_critical_power_base(self):
        return self.status.attribute.magical_critical_power_base

    @property
    def magical_critical_power_gain(self):
        return self.status.attribute.magical_critical_power_gain + self.skill_critical_power

    @property
    def critical_strike(self):
        return self.status.attribute.magical_critical_strike + self.skill_critical_strike

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

    def record_damage(self, critical: bool):
        snapshot = self.snapshot
        attribute = self.status.attribute
        target = self.status.target
        return (
            (
                ('spirit_base', snapshot.spirit_base),
                ('spirit_gain', snapshot.spirit_gain),
                ('spunk_base', snapshot.spunk_base),
                ('spunk_gain', snapshot.spunk_gain),
                ('surplus', attribute.surplus),
                ('strain_base', snapshot.strain_base),
                ('strain_gain', snapshot.strain_gain),
                ('magical_attack_power_base', snapshot.magical_attack_power_base),
                ('magical_attack_power_gain', snapshot.magical_attack_power_gain),
                ('magical_critical_strike_base', snapshot.magical_critical_strike_base),
                ('magical_critical_strike_gain', snapshot.magical_critical_strike_gain),
                ('magical_critical_power_base', snapshot.magical_critical_power_base),
                ('magical_critical_power_gain', snapshot.magical_critical_power_gain),
                ('magical_overcome_base', attribute.magical_overcome_base),
                ('magical_overcome_gain', attribute.magical_overcome_gain),
                ('weapon_damage_base', attribute.weapon_damage_base),
                ('weapon_damage_rand', attribute.weapon_damage_rand),
                ('weapon_damage_gain', attribute.weapon_damage_gain)
            ),
            (
                ('level', attribute.level),
                ('damage_addition', self.damage_addition),
                ('pve_addition', self.pve_addition),
                ('shield_ignore', attribute.magical_shield_ignore + self.skill_shield_ignore),

                ('target_level', target.level),
                ('shield_base', target.magical_shield_base),
                ('shield_gain', target.magical_shield_gain + self.skill_shield_gain),
                ('vulnerable', target.magical_vulnerable),
                ('shield_constant', target.shield_constant),

                ('skill', self.name),
                ('critical', critical),
                ('damage_base', self.damage_base),
                ('damage_rand', self.damage_rand),
                ('damage_gain', self.damage_gain),
                ('attack_power_cof', self.attack_power_cof),
                ('weapon_damage_cof', self.weapon_damage_cof),
                ('surplus_cof', self.surplus_cof),
                ('attack_power_cof_gain', self.attack_power_cof_gain),
                ('weapon_damage_cof_gain', self.weapon_damage_cof_gain),
                ('surplus_cof_gain', self.surplus_cof_gain)
            )
        )