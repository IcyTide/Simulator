from base.buff import Buff
from base.skill import Skill
from base.status import Status


class 龙息:
    def __call__(self, status: Status):
        related_skills = ["惊燕式", "逐鹰式"]
        for skill in related_skills:
            status.skills[skill].interval_list = [0, 0]

        Skill.to_overdraw(status.skills["擒龙六斩"])
        status.skills["擒龙六斩"].energy = 6
        status.energies["擒龙六斩"] = 6


class 归酣:
    def __call__(self, status: Status):
        status.skills["上将军印"].cd_base -= 120 + 5 * 8


class 阳关:
    def __call__(self, status: Status):
        status.skills["上将军印"].skill_damage_addition += 154 / 1024
        status.skills["见尘"].skill_damage_addition += 154 / 1024

        status.skills["上将军印"].skill_shield_gain -= 205 / 1024


class 霜天:
    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.buffs["霜天"].cast()
        # if self.status.counts[self.name] < 4:
        #     self.weapon_damage_cof_gain += 0.15

    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["霜天"].post_cast()
        # self.weapon_damage_cof_gain -= 0.15 * min(4, count)

    def __call__(self, status: Status):
        status.skills["上将军印"].post_hit_effect.append(self.post_hit_effect)
        status.skills["上将军印"].post_cast_effect.append(self.post_cast_effect)


class 见尘:
    @staticmethod
    def pre_cast_effect(self: Skill):
        if self.status.stacks["闹须弥-持续"]:
            self.status.skills["见尘"].cast()

    def __call__(self, status: Status):
        status.skills["上将军印"].pre_cast_effect.append(self.pre_cast_effect)


class 含风:
    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.buffs["含风"].cast()

    def __call__(self, status: Status):
        status.skills["刀啸风吟"].post_hit_effect.append(self.post_hit_effect)


class 分疆:
    def __call__(self, status: Status):
        status.skills["上将军印"].interval_list = [4, 4, 5, 5, 5, 5, 4]
        status.skills["见尘"].interval_list = [5, 4, 5, 5, 5, 5, 4]


class 星火:
    def __call__(self, status: Status):
        status.attribute.strength_gain += 102 / 1024


class 楚歌:
    @staticmethod
    def pre_cast_effect(self: Skill):
        self.status.buffs["楚歌"].cast()

    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["楚歌"]:
            self.status.buffs["楚歌-计数"].cast()

    def __call__(self, status: Status):
        status.skills["破釜沉舟"].cd_base -= 3 * 16
        status.skills["破釜沉舟"].skill_critical_strike += 0.1
        status.skills["破釜沉舟"].skill_critical_power += 205 / 1024
        status.skills["破釜沉舟"].pre_cast_effect.append(self.pre_cast_effect)
        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.post_hit_effect)


class 绝期:
    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["闹须弥-持续"]:
            self.status.skills["绝期"].cast()

    def __call__(self, status: Status):
        status.skills["闹须弥-持续"].attack_power_cof_gain += 0.7

        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.post_hit_effect)


class 重烟:
    @staticmethod
    def add_effect(self: Buff):
        self.status.attribute.cd_reduction += 307 / 1024

    @staticmethod
    def remove_effect(self: Buff):
        self.status.attribute.cd_reduction -= 307 / 1024

    def __call__(self, status: Status):
        status.buffs["秀明尘身"].add_effect.append(self.add_effect)
        status.buffs["秀明尘身"].remove_effect.append(self.remove_effect)


class 降麒式:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.cds["擒龙六斩"] -= 2 * 16
        self.status.buffs["降麒式-计数"].cast()

    def __call__(self, status: Status):
        related_skills = ["惊燕式", "逐鹰式"]

        for skill in related_skills:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect)


TALENTS = [
    ["龙息"],
    ["归酣"],
    ["阳关"],
    ["霜天"],
    ["含风"],
    ["见尘"],
    ["分疆"],
    ["星火"],
    ["楚歌"],
    ["绝期"],
    ["重烟"],
    ["降麒式"]
]
TALENT_GAINS = {
    "龙息": 龙息(),
    "归酣": 归酣(),
    "阳关": 阳关(),
    "霜天": 霜天(),
    "含风": 含风(),
    "见尘": 见尘(),
    "分疆": 分疆(),
    "星火": 星火(),
    "楚歌": 楚歌(),
    "绝期": 绝期(),
    "重烟": 重烟(),
    "降麒式": 降麒式(),
}
