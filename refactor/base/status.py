from dataclasses import dataclass
from typing import List

from base.attribute import Attribute

from base.constant import MAX_GCD_GROUP


@dataclass
class Snapshot:
    attack_power: int = 0
    attack_power_cof: int = 0

    critical_strike: int = 0
    critical_damage: int = 0
    strain: int = 0
    damage_addition: int = 0


class Status:
    def __init__(self, attribute: Attribute, skills: List, buffs: List, event_seq: List):
        self.attribute = attribute

        self.gcd_group = [0 for _ in range(MAX_GCD_GROUP)]
        self.casting = 0
        self.current_time = 0

        self.skills = {}
        self.cds = {}
        self.energies = {}
        self.counts = {}
        self.intervals = {}

        for skill in skills:
            self.skills[skill.name] = skill

            self.energies[skill.name] = skill.energy
            self.counts[skill.name] = 0

        self.buffs = {}
        self.durations = {}
        self.stacks = {}

        for buff in buffs:
            self.buffs[buff.name] = buff

            self.stacks[buff.name] = 0

        self.event_seq = event_seq

    def timer(self, gap=1):
        self.current_time += gap

        damage_skills = []
        for skill, interval in self.intervals.items():
            self.intervals[skill] = max(0, interval - gap)
            if not self.intervals[skill]:
                damage_skills.append(skill)
        for skill in damage_skills:
            self.intervals.pop(skill)
            self.skills[skill].damage()

        recharge_skills = []
        for skill, cd in self.cds.items():
            self.cds[skill] = max(0, cd - gap)
            if not self.cds[skill]:
                recharge_skills.append(skill)
        for skill in recharge_skills:
            self.cds.pop(skill)
            self.skills[skill].recharge()

        expire_buffs = []
        for buff, duration in self.durations.items():
            self.durations[buff] = max(0, duration - gap)
            if not self.durations[buff]:
                expire_buffs.append(buff)
        for buff in expire_buffs:
            self.durations.pop(buff)
            self.buffs[buff].expire()

        for gcd_index, gcd in enumerate(self.gcd_group):
            self.gcd_group[gcd_index] = max(0, gcd - gap)

        self.casting = max(0, self.casting - gap)

    def record(self, name, event, status):
        self.event_seq.append((self.current_time / 16, name, event, status))
