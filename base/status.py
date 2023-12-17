from collections import Counter

from base.attribute import Attribute
from base.target import Target


class Monitor(dict):
    def __missing__(self, key):
        return None

    def __delitem__(self, elem):
        if elem in self:
            super().__delitem__(elem)

class Status:
    def __init__(self, attribute: Attribute, target: Target,
                 skills: list, buffs: list, damages: dict, events: list, total_frame: int, verbose=False):
        if verbose:
            self.record = self.record_verbose

        self.attribute = attribute
        self.target = target

        self.gcd_group = Counter()
        self.casting = False

        self.intervals = Counter()
        self.counts = Counter()

        self.skills = {}
        self.cds = Counter()
        self.energies = Counter()

        for skill in skills:
            skill = skill(self)
            self.skills[skill.name] = skill
            self.energies[skill.name] = skill.energy

        self.buffs = {}
        self.durations = Counter()
        self.stacks = Counter()

        for buff in buffs:
            buff = buff(self)
            self.buffs[buff.name] = buff
            self.stacks[buff.name] = 0

        self.total_frame = total_frame
        self.current_frame = 0
        self.damages = damages
        self.events = events

    def timer(self, gap=1):
        self.current_frame += gap

        for gcd_index, gcd in self.gcd_group.items():
            self.gcd_group[gcd_index] = gcd - gap

        for buff, duration in self.durations.items():
            duration = self.durations[buff] = duration - gap
            if duration <= 0:
                self.buffs[buff].clear()

        for skill, interval in self.intervals.items():
            interval = self.intervals[skill] = interval - gap
            if interval <= 0:
                self.skills[skill].hit()

        reduction_gap = gap * (1 + self.attribute.cd_reduction)
        for skill, cd in self.cds.items():
            cd = self.cds[skill] = cd - reduction_gap
            if cd <= 0:
                self.skills[skill].recharge()

    def record_verbose(self, params):
        self.damages[params] += 1
        self.events.append((self.current_frame, params[1][0], params[1][1], +self.stacks))

    def record(self, params):
        self.damages[params] += 1
