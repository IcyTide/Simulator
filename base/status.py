from base.attribute import Attribute

from base.target import Target


class Status:
    def __init__(self, attribute: Attribute, target: Target,
                 skills: list, buffs: list, damages: dict, total_frame: int):
        self.attribute = attribute
        self.target = target

        self.gcd_group = {}
        self.casting = 0

        self.skills = {}

        self.cds = {}
        self.energies = {}
        self.counts = {}
        self.intervals = {}

        for skill in skills:
            skill.status = self

            self.skills[skill.name] = skill
            self.energies[skill.name] = skill.energy

        self.buffs = {}
        self.durations = {}
        self.stacks = {}

        for buff in buffs:
            buff.status = self

            self.buffs[buff.name] = buff
            self.stacks[buff.name] = 0

        self.total_frame = total_frame
        self.current_frame = 0
        self.damages = damages

    def timer(self, gap=1):
        self.current_frame += gap
        self.casting = max(0, self.casting - gap)

        refresh_gcd = []
        for gcd_index, gcd in self.gcd_group.items():
            self.gcd_group[gcd_index] = max(0, gcd - gap)
            if not self.gcd_group[gcd_index]:
                refresh_gcd.append(gcd_index)
        for gcd_index in refresh_gcd:
            self.gcd_group.pop(gcd_index)

        damage_skills = []
        for skill, interval in self.intervals.items():
            self.intervals[skill] = max(0, interval - gap)
            if not self.intervals[skill]:
                damage_skills.append(skill)
        for skill in damage_skills:
            self.skills[skill].hit()

        recharge_skills = []
        reduction_gap = gap * (1 + self.attribute.cd_reduction)
        for skill, cd in self.cds.items():
            self.cds[skill] = max(0, cd - reduction_gap)
            if not self.cds[skill]:
                recharge_skills.append(skill)
        for skill in recharge_skills:
            self.skills[skill].recharge()

        expire_buffs = []
        for buff, duration in self.durations.items():
            self.durations[buff] = max(0, duration - gap)
            if not self.durations[buff]:
                expire_buffs.append(buff)
        for buff in expire_buffs:
            self.buffs[buff].clear()

    def record(self, params):
        if params not in self.damages:
            self.damages[params] = 0
        self.damages[params] += 1
