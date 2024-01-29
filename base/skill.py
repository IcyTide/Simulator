import random
from collections import namedtuple

from dataclasses import dataclass
from functools import partial
from itertools import chain

from base.constant import PHYSICAL_ATTACK_POWER_COF, WEAPON_DAMAGE_COF
from base.status import Status
from utils.damage import *


Gains = namedtuple("Gains", ["buff", "level", "stack"])
Damage = namedtuple("Damage", ["skill", "critical", "level", "times", "gains"])


@cache
def apply_haste(haste, value):
    return int(value / (1 + haste))


@dataclass
class Snapshot:
    level: int = 1
    critical_strike: float = 0
    gains: dict = None


@dataclass
class Skill:
    status: Status
    name: str = None
    activate: bool = True

    is_cast: bool = True
    is_hit: bool = True
    hit_with_cast: bool = False

    gcd_index: any = 0
    gcd_base: int = 24

    tick_base: int = 1
    interval_base: int = 0

    cd_base: int = 0
    energy: int = 1

    level: int = 1
    snapshot: [Snapshot] = None
    haste: float = 0
    dice: random.Random = None

    def __post_init__(self):
        self.pre_cast_effect = []
        self.post_cast_effect = []
        self.pre_hit_effect = []
        self.critical_hit_effect = []
        self.post_hit_effect = []

        self.dice = random.Random(82)

        self.attribute = self.status.attribute
        self.target = self.status.target
        self.snapshot = self

    @property
    def critical_strike(self):
        raise NotImplementedError

    """ base property """

    @property
    def gcd(self):
        return apply_haste(self.haste, self.gcd_base)

    @property
    def cd(self):
        return self.cd_base

    @property
    def tick(self):
        return self.tick_base

    @property
    def interval(self):
        return apply_haste(self.haste, self.interval_base)

    @property
    def duration(self):
        return self.interval * self.tick

    @property
    def roll(self):
        return self.dice.random()

    """ action functions """

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
        if self.status.casting:
            return False
        return self.condition

    def reset(self):
        self.status.energies[self.name] = self.energy
        self.status.cds.pop(self.name)

    def recharge(self):
        self.reset()

    def set_gcd(self):
        if self.gcd_base:
            self.status.gcd_group[self.gcd_index] = self.gcd

    def set_cd(self):
        if self.cd_base:
            self.status.cds[self.name] = self.cd
            self.status.energies[self.name] -= 1

    def pre_cast(self):
        self.status.ticks[self.name] = 0
        self.haste = self.status.attribute.haste
        self.status.intervals[self.name] = self.interval

        for effect in self.pre_cast_effect:
            effect(self)

    def cast(self, level=1):
        if not level:
            return
        self.level = level

        self.pre_cast()
        if not self.interval:
            for _ in range(self.tick):
                self.hit()

    def post_cast(self):
        self.status.ticks.pop(self.name)
        self.status.intervals.pop(self.name)

        for effect in self.post_cast_effect:
            effect(self)

    def pre_hit(self):
        for effect in self.pre_hit_effect:
            effect(self)

    def hit(self):
        self.pre_hit()
        self.post_hit()

    def post_hit(self):
        self.status.ticks[self.name] += 1

        for effect in self.post_hit_effect:
            effect(self)

        if self.status.ticks[self.name] == self.tick:
            self.post_cast()
        else:
            self.status.intervals[self.name] = self.interval

    def record(self, critical, level, times=1):
        gains = tuple(
            Gains(buff, level, stack) for buff, (level, stack) in self.status.gains[""] + self.status.gains[self.name]
        )
        self.status.record(Damage(self.name, critical, level, times, gains))

    @staticmethod
    def to_overdraw(skill):
        skill.set_cd = partial(OverdrawSkill.set_cd, skill)
        skill.recharge = partial(OverdrawSkill.recharge, skill)

    @staticmethod
    def to_charging(skill):
        skill.set_cd = partial(ChargingSkill.set_cd, skill)
        skill.recharge = partial(ChargingSkill.recharge, skill)


class DamageSkill(Skill):
    _damage_base: [int, list] = 0
    _damage_rand: [int, list] = 0
    _attack_power_cof: [float, list] = 0.0
    _weapon_damage_cof: [float, list] = 0.0
    _surplus_cof: [float, list] = 0.0

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

    @property
    def damage_base(self):
        if isinstance(self._damage_base, int):
            return self._damage_base
        else:
            return self._damage_base[self.level - 1]

    @damage_base.setter
    def damage_base(self, damage_base):
        self._damage_base = damage_base

    @property
    def damage_rand(self):
        if isinstance(self._damage_rand, int):
            return self._damage_rand
        else:
            return self._damage_rand[self.level - 1]

    @damage_rand.setter
    def damage_rand(self, damage_rand):
        self._damage_rand = damage_rand

    @property
    def attack_power_cof(self):
        if isinstance(self._attack_power_cof, float):
            return self._attack_power_cof
        else:
            return self._attack_power_cof[self.level - 1]

    @attack_power_cof.setter
    def attack_power_cof(self, attack_power_cof):
        self._attack_power_cof = attack_power_cof

    @property
    def weapon_damage_cof(self):
        if isinstance(self._weapon_damage_cof, float):
            return self._weapon_damage_cof
        else:
            return self._weapon_damage_cof[self.level - 1]

    @weapon_damage_cof.setter
    def weapon_damage_cof(self, weapon_damage_cof):
        self._weapon_damage_cof = weapon_damage_cof

    @property
    def surplus_cof(self):
        if isinstance(self._surplus_cof, float):
            return self._surplus_cof
        else:
            return self._surplus_cof[self.level - 1]

    @surplus_cof.setter
    def surplus_cof(self, surplus_cof):
        self._surplus_cof = surplus_cof

    def critical_hit(self):
        for effect in self.critical_hit_effect:
            effect(self)

    def hit(self):
        self.pre_hit()
        critical = self.roll < self.snapshot.critical_strike

        self.record(critical, self.snapshot.level)

        if critical:
            self.critical_hit()

        self.post_hit()


class TriggerSkill(Skill):
    probability: float = 1

    def cast(self, level=1):
        if self.roll < self.probability:
            super().cast()


""""""


class CastingSkill(Skill):
    direct: bool = False

    def pre_cast(self):
        super().pre_cast()
        self.set_gcd()
        self.status.casting = True
        if self.direct:
            self.hit()

    def post_cast(self):
        self.set_cd()
        self.status.casting = False
        super().post_cast()


class ChannelSkill(Skill):
    _instant: bool = False

    @property
    def instant(self):
        return self._instant

    @instant.setter
    def instant(self, instant):
        if instant:
            self.tick_base += 1
        else:
            self.tick_base -= 1

    def pre_cast(self):
        super().pre_cast()
        self.status.casting = True
        self.set_gcd()
        self.set_cd()
        if self.instant:
            self.hit()

    def post_cast(self):
        self.status.casting = False
        super().post_cast()


class PeriodicalSkill(Skill):
    def pre_cast(self):
        for effect in self.pre_cast_effect:
            effect(self)

        self.status.ticks[self.name] = 0
        self.haste = self.status.attribute.haste
        if not self.status.intervals[self.name]:
            self.status.intervals[self.name] = self.interval

        self.status.buffs[self.name].trigger()

    def post_cast(self):
        super().post_cast()
        self.status.buffs[self.name].clear()


class LoopSkill(Skill):
    @property
    def available(self):
        return True

    @property
    def interval(self):
        return self.interval_base

    @property
    def tick(self):
        return -1


""""""


class FixedInterval(Skill):
    _interval_list: list = None
    _duration: int = 0

    @property
    def interval_list(self):
        return self._interval_list

    @interval_list.setter
    def interval_list(self, interval_list):
        self._interval_list = interval_list
        self._duration = sum(interval_list)

    @property
    def interval(self):
        return self._interval_list[self.status.ticks[self.name]]

    @property
    def tick(self):
        return len(self._interval_list)

    @property
    def duration(self):
        return self._duration


""""""


class HastedCD(Skill):
    @property
    def cd(self):
        return apply_haste(self.haste, self.cd_base)


""""""


class OverdrawSkill(Skill):
    def set_cd(self):
        self.status.energies[self.name] -= 1
        self.status.cds[self.name] += self.cd


class ChargingSkill(Skill):
    def recharge(self):
        if self.status.energies[self.name] < self.energy:
            self.status.energies[self.name] += 1

        if self.status.energies[self.name] == self.energy:
            self.status.cds.pop(self.name)
        else:
            self.status.cds[self.name] = self.cd

    def set_cd(self):
        self.status.energies[self.name] -= 1
        if not self.status.cds[self.name]:
            self.status.cds[self.name] = self.cd


""""""


class PhysicalDamage(DamageSkill):
    @property
    def critical_strike(self):
        return self.attribute.physical_critical_strike + self.skill_critical_strike

    def calculate(self, level):
        self.level = level
        damage = init_result(
            self.damage_base, self.damage_rand, self.damage_gain,
            self.attack_power_cof, self.attack_power_cof_gain, self.attribute.physical_attack_power,
            self.weapon_damage_cof, self.weapon_damage_cof_gain, self.attribute.weapon_damage,
            self.surplus_cof, self.surplus_cof_gain, self.attribute.surplus
        )

        damage = damage_addition_result(damage, self.attribute.physical_damage_addition + self.skill_damage_addition)
        damage = overcome_result(damage, self.attribute.physical_overcome,
                                 self.target.physical_shield_base,
                                 self.target.physical_shield_gain + self.skill_shield_gain,
                                 self.attribute.physical_shield_ignore + self.skill_shield_ignore,
                                 self.target.shield_constant)
        # if critical:
        #     damage = critical_result(damage, attribute.physical_critical_power)
        damage = critical_result(damage,
                                 self.attribute.physical_critical_strike + self.skill_critical_strike,
                                 self.attribute.physical_critical_power + self.skill_critical_power)
        damage = level_reduction_result(damage, self.attribute.level, self.target.level)
        damage = strain_result(damage, self.attribute.strain)
        damage = pve_addition_result(damage, self.attribute.pve_addition + self.skill_pve_addition)
        damage = vulnerable_result(damage, self.target.physical_vulnerable)
        damage = damage

        return damage


class Melee(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(16)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class MagicalDamage(DamageSkill):
    @property
    def critical_strike(self):
        return self.attribute.magical_critical_strike + self.skill_critical_strike

    def calculate(self, level):
        self.level = level
        damage = init_result(
            self.damage_base, self.damage_rand, self.damage_gain,
            self.attack_power_cof, self.attack_power_cof_gain, self.attribute.magical_attack_power,
            self.weapon_damage_cof, self.weapon_damage_cof_gain, self.attribute.weapon_damage,
            self.surplus_cof, self.surplus_cof_gain, self.attribute.surplus
        )

        damage = damage_addition_result(damage, self.attribute.magical_damage_addition + self.skill_damage_addition)
        damage = overcome_result(damage, self.attribute.magical_overcome,
                                 self.target.magical_shield_base,
                                 self.target.magical_shield_gain + self.skill_shield_gain,
                                 self.attribute.magical_shield_ignore + self.skill_shield_ignore,
                                 self.target.shield_constant)
        # if critical:
        #     damage = critical_result(damage, attribute.physical_critical_power)
        damage = critical_result(damage,
                                 self.attribute.magical_critical_strike + self.skill_critical_strike,
                                 self.attribute.magical_critical_power + self.skill_critical_power)
        damage = level_reduction_result(damage, self.attribute.level, self.target.level)
        damage = strain_result(damage, self.attribute.strain)
        damage = pve_addition_result(damage, self.attribute.pve_addition + self.skill_pve_addition)
        damage = vulnerable_result(damage, self.target.magical_vulnerable)
        damage = damage

        return damage


""""""


class ActionSkill(ChannelSkill, FixedInterval):
    pass


class DotSkill(PeriodicalSkill):

    def consume(self, tick=0):
        if not tick:
            tick = self.tick

        if stack := self.status.stacks[self.name]:
            critical = self.roll < self.critical_strike
            res_tick = self.tick - self.status.ticks[self.name]
            tick = min(res_tick, tick)
            self.record(critical, self.snapshot.level, tick * stack)

            if tick == res_tick:
                self.status.buffs[self.name].clear()
                self.post_cast()

    def pre_cast(self):
        super().pre_cast()
        self.snapshot = Snapshot(
            self.level, self.critical_strike, self.status.snapshots[""] + self.status.snapshots[self.name]
        )

    def record(self, critical, level, times=1):
        gains = tuple(
            Gains(buff, level, stack)
            for buff, (level, stack) in
            dict(chain(self.status.gains[""] + self.status.gains[self.name], self.snapshot.gains)).items()
        )
        self.status.record(Damage(self.name, critical, level, times * max(1, self.status.stacks[self.name]), gains))


class PlacementSkill(PeriodicalSkill, FixedInterval):
    pass
