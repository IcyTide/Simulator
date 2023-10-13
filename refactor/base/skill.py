from copy import deepcopy
from dataclasses import dataclass

from base import Timeline
from base.status import Status


@dataclass
class Skill:
    uid: int
    name: str

    timeline: Timeline

    skills: dict
    buffs: dict
    status: Status
    snapshot: bool = False

    activate: bool = True

    casting: bool = True
    cast_while_casting: bool = False
    instant: bool = False

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
    weapon_damage: int = 0

    attack_power_base: int = 0
    attack_power_gain: int = 0

    damage_additional: int = 0
    critical_strike_additional: int = 0
    critical_damage_additional: int = 0
    shield_ignore_additional: int = 0

    @property
    def attack_power(self):
        return self.attack_power_base * self.attack_power_gain

    @property
    def duration(self):
        return self.interval * self.count

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

    @property
    def interval(self):
        return self.interval_base // (1 + self.status.attribute.haste)

    @property
    def gcd(self):
        return self.gcd_base // (1 + self.status.attribute.haste)

    @property
    def cd(self):
        return self.cd_base

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

    """ timeline function"""
    def insert(self):
        gaps = (e for e in (self.current_cd, self.current_interval) if e > 0)
        if gaps:
            self.timeline.set(min(gaps), self)

    def update(self, gap):
        self.add_interval(-gap)
        self.add_cd(-gap)
        self.insert()

    """ action function"""
    def pre_cast(self):
        self.status.set_gcd(self.gcd_index, self.gcd)
        self.status.set_casting(self.casting * self.duration)

        self.add_cd(self.cd)
        self.add_energy(-1)

        self.set_count(self.count)
        self.set_interval(self.interval)

        if self.snapshot:
            self.status.snapshots[self.uid] = deepcopy(self.status.attribute)

    def cast(self):
        self.pre_cast()

        if self.instant:
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
    def calculate(self):
        defense = self.status.physical_shield - self.status.physical_shield * self.shield_ignore_additional
        return
