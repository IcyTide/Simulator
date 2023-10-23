from dataclasses import dataclass
from typing import List
from base.attribute import Attribute
from base.buff import Buff
from base.constant import MAX_GCD_GROUP
from base.skill import Skill


@dataclass
class Snapshot:
    attack_power: int = 0
    attack_power_cof: int = 0

    critical_strike: int = 0
    critical_damage: int = 0
    strain: int = 0
    damage_addition: int = 0


class Status:
    def __init__(self, attribute: Attribute, skills: List[Skill], buffs: List[Buff]):
        self.attribute = attribute
        self.counts = {}
        self.intervals = {}

        self.skills = {}
        self.gcd_group = [0 for _ in MAX_GCD_GROUP]
        self.cds = {}
        self.energies = {}
        for skill in skills:
            self.skills[skill.name] = skill
            self.gcd_group[skill.gcd_index] = 0

            self.cds[skill] = 0
            self.energies[skill] = skill.energy
            self.intervals[skill] = 0
            self.counts[skill] = 0

        self.buffs = {}
        self.durations = {}
        self.stacks = {}
        for buff in buffs:
            self.buffs[buff.name] = buff

            self.durations[buff] = 0
            self.stacks[buff] = 0

    def timer(self, gap=1):
        for skill in self.skills.values():
            self.intervals[skill] -= gap
            if not self.intervals[skill] and self.counts[skill]:
                skill.damage()

            self.cds[skill] -= gap
            if not self.cds[skill]:
                skill.recharge()

        for buff in self.buffs.values():
            self.durations[buff] -= gap
            if not self.durations[buff]:
                buff.expire()

