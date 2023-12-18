from collections import Counter

from base.attribute import Attribute
from base.target import Target


class Status:
    def __init__(self, attribute: Attribute, target: Target,
                 skills: list, buffs: list, damages: dict, events: list, total_frame: int, verbose=False):
        if verbose:
            self.record = self.record_verbose

        self.attribute = attribute
        self.target = target

        self.gcd_group = {}
        self.casting = False

        self.intervals = {}
        self.counts = {}

        self.skills = {}
        self.cds = {}
        self.energies = Counter()

        for skill in skills:
            skill = skill(self)
            self.skills[skill.name] = skill
            self.energies[skill.name] = skill.energy

        self.buffs = {}
        self.durations = {}
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

        refresh_gcd = []
        for gcd_index, gcd in self.gcd_group.items():
            gcd = self.gcd_group[gcd_index] = gcd - gap
            if gcd <= 0:
                refresh_gcd.append(gcd_index)
        for gcd_index in refresh_gcd:
            self.gcd_group.pop(gcd_index)

        expire_buffs = []
        for buff, duration in self.durations.items():
            duration = self.durations[buff] = duration - gap
            if duration <= 0:
                expire_buffs.append(buff)
        for buff in expire_buffs:
            self.buffs[buff].clear()

        damage_skills = []
        for skill, interval in self.intervals.items():
            interval = self.intervals[skill] = interval - gap
            if interval <= 0:
                damage_skills.append(skill)
        for skill in damage_skills:
            self.skills[skill].hit()

        recharge_skills = []
        reduction_gap = gap * (1 + self.attribute.cd_reduction)
        for skill, cd in self.cds.items():
            cd = self.cds[skill] = cd - reduction_gap
            if cd <= 0:
                recharge_skills.append(skill)
        for skill in recharge_skills:
            self.skills[skill].recharge()

    def record_verbose(self, params):
        self.damages[params] += 1
        self.events.append((self.current_frame, params[1][0], params[1][1], +self.stacks))

    def record(self, params):
        self.damages[params] += 1
