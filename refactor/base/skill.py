from copy import deepcopy
from dataclasses import dataclass

from base import Timeline
from base.constant import *
from base.status import Status, Attribute


@dataclass
class Addition:
    attack_power_cof_base: int = 0
    attack_power_cof_gain: int = 0
    damage: int = 0
    pve: int = 0
    shield_ignore: int = 0
    critical_strike: int = 0
    critical_damage: int = 0


@dataclass
class Skill:
    uid: int
    name: str

    timeline: Timeline
    status: Status

    skills: dict = None
    buffs: dict = None
    attribute: Attribute = None
    addition: Addition = None

    activate: bool = True

    is_cast: bool = True
    cast_while_casting: bool = False
    is_instant: bool = False
    is_snapshot: bool = False

    gcd_index: int = 0

    count: int = 1

    interval_base: int = 0
    gcd_base: int = 24
    cd_base: int = gcd_base
    energy: int = 1

    current_interval: int = 0
    current_count: int = 0
    current_cd: int = 0
    current_energy: int = energy

    base_damage: int = 0
    weapon_damage_cof: int = 0
    attack_power_cof_base: int = 0

    attack_power_cof_base_addition: int = 0
    attack_power_cof_gain_addition: int = 0
    damage_base_addition: int = 0
    pve_base_addition: int = 0
    shield_ignore_addition: int = 0
    critical_strike_addition: int = 0
    critical_damage_addition: int = 0

    def __post_init__(self):
        self.attribute = self.status.attribute
        self.status.additions[self.uid] = Addition(self.attack_power_cof_base_addition,
                                                   self.attack_power_cof_gain_addition,
                                                   self.damage_base_addition, self.pve_base_addition,
                                                   self.shield_ignore_addition,
                                                   self.critical_strike_addition, self.critical_damage_addition)
        self.addition = self.status.additions[self.uid]
    
    """ attributes """
    @property
    def attack_power_cof(self):
        return self.attack_power_cof_base * self.addition.attack_power_cof_gain + \
            self.addition.attack_power_cof_base

    @property
    def damage_addition(self):
        return self.attribute.damage_addition + self.addition.damage // INT_SCALE

    @property
    def pve_addition(self):
        return self.attribute.pve_addition + self.addition.pve // INT_SCALE
    
    @property
    def physical_critical_strike(self):
        return self.attribute.physical_critical_strike + self.addition.critical_strike / PERCENT_SCALE
    
    @property
    def physical_critical_damage(self):
        return self.attribute.physical_critical_damage + self.addition.critical_damage / INT_SCALE

    @property
    def magical_critical_strike(self):
        return self.attribute.magical_critical_strike + self.addition.critical_strike / PERCENT_SCALE

    @property
    def magical_critical_damage(self):
        return self.attribute.magical_critical_damage + self.addition.critical_damage / INT_SCALE
    
    @property
    def critical_strike(self):
        return self.attribute.critical_strike + self.addition.critical_strike / PERCENT_SCALE
    
    @property
    def critical_damage(self):
        return self.attribute.critical_damage + self.addition.critical_damage / INT_SCALE

    @property
    def physical_shield(self):
        return self.status.physical_shield * (1 - self.addition.shield_ignore) // INT_SCALE

    @property
    def magical_shield(self):
        return self.status.magical_shield * (1 - self.addition.shield_ignore) // INT_SCALE
    
    """ skill detail"""
    @property
    def interval(self):
        return self.interval_base // (1 + self.attribute.haste)

    @property
    def gcd(self):
        return self.gcd_base // (1 + self.attribute.haste)

    @property
    def cd(self):
        return self.cd_base

    @property
    def duration(self):
        return self.interval * self.count

    @property
    def current_duration(self):
        return self.current_interval + self.interval * (self.count - 1)

    @property
    def condition(self):
        return True

    @property
    def ready(self):
        if self.status.gcd[self.gcd_index]:
            return False
        if not self.current_energy:
            return False
        if self.status.casting and not self.cast_while_casting:
            return False
        return self.activate and self.condition

    """ update function"""

    def set_interval(self, interval):
        self.current_interval = max(interval, 0)
        if self.count and not self.current_interval:
            self.damage()

    def add_interval(self, interval):
        self.set_interval(self.interval + interval)

    def set_count(self, count):
        self.current_count = count

    def add_count(self, count):
        self.set_count(self.current_count + count)

    def set_cd(self, cd):
        self.current_cd = max(cd, 0)
        if not self.current_cd:
            self.set_energy(self.energy)

    def add_cd(self, cd):
        self.set_cd(self.cd + cd)

    def set_energy(self, energy):
        self.current_energy = max(energy, self.energy)

    def add_energy(self, energy):
        self.set_energy(self.current_energy + energy)

    """ timeline functions """

    def insert(self):
        gaps = (e for e in (self.current_cd, self.current_interval) if e > 0)
        if gaps:
            self.timeline.set(min(gaps), self)

    def update(self, gap):
        self.add_interval(-gap)
        self.add_cd(-gap)
        self.insert()

    """ action functions """

    def pre_cast(self):
        self.status.set_gcd(self.gcd_index, self.gcd)
        self.status.set_casting(self.is_cast * self.duration)

        self.add_cd(self.cd)
        self.add_energy(-1)

        if self.is_snapshot:
            self.attribute = deepcopy(self.status.attribute)
            self.addition = deepcopy(self.status.additions[self.uid])

        self.set_count(self.count)
        self.set_interval(self.interval)

    def cast(self):
        self.pre_cast()

        if self.is_instant:
            self.damage()

        self.status.insert()
        self.insert()

    def post_cast(self):
        self.set_count(0)
        self.set_interval(0)

        self.status.set_casting(0)

    def pre_damage(self):
        pass

    def damage(self):
        self.pre_damage()
        # TODO: damage
        self.post_damage()

        if not self.current_count:
            self.post_cast()

    def post_damage(self):
        self.add_count(-1)
        self.set_interval(self.interval)

    """ calculation function"""
    
    @property
    def weapon_damage(self):
        damage = self.weapon_damage_cof * self.status.weapon_damage
        critical_damage = damage * self.physical_critical_damage
        expected_damage = damage * (1 - self.physical_critical_strike) + critical_damage * self.physical_critical_strike
        expected_damage = expected_damage * self.attribute.physical_overcome
        return expected_damage // INT_SCALE
    
    @property
    def attack_damage(self):
        damage = self.attack_power_cof * self.attribute.attack_power
        critical_damage = damage * self.critical_damage
        expected_damage = damage * (1 - self.critical_strike) + critical_damage * self.critical_strike
        expected_damage = expected_damage * self.attribute.overcome
        return expected_damage // INT_SCALE
    
    def total_damage(self):
        damage = self.weapon_damage + self.attack_damage
        damage = damage * self.attribute.strain * self.damage_addition * self.pve_addition
        return damage
    
    def record(self):
        damage = self.base_damage + self.attack_power_cof * self.attribute.attack_power
        return

