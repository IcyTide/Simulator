from base.buff import Buff
from base.skill import Skill
from base.status import Status


class LongXi:
    def __call__(self, status: Status):
        related_skills = ["惊燕式", "逐鹰式"]
        for skill in related_skills:
            status.skills[skill].interval_list = None
            status.skills[skill].interval_base = 0

        status.skills["擒龙六斩"].energy = 6
        status.energies["擒龙六斩"] = 6


class GuiHan:
    def __call__(self, status: Status):
        status.skills["上将军印"].cd_base -= 120 + 5 * 8


class YangGuan:
    def __call__(self, status: Status):
        status.skills["上将军印"].skill_damage_addition += 0.15
        status.skills["见尘"].skill_damage_addition += 0.15

        status.skills["上将军印"].skill_shield_gain -= 0.2


class ShuangTian:
    @staticmethod
    def shuang_tian_post_hit(self: Skill):
        self.damage_gain += 0.15
        self.attack_power_cof_gain += 0.15
        self.weapon_damage_cof_gain += 0.15
        # if self.status.counts[self.name] < 4:
        #     self.weapon_damage_cof_gain += 0.15

    @staticmethod
    def shuang_tian_post_cast(self: Skill):
        count = self.status.counts[self.name]
        self.damage_gain -= 0.15 * count
        self.attack_power_cof_gain -= 0.15 * count
        self.weapon_damage_cof_gain -= 0.15 * count
        # self.weapon_damage_cof_gain -= 0.15 * min(4, count)

    def __call__(self, status: Status):
        status.skills["上将军印"].post_hit_effect.append(self.shuang_tian_post_hit)
        status.skills["上将军印"].post_cast_effect.append(self.shuang_tian_post_cast)


class JianChen:
    @staticmethod
    def jian_chen_pre_cast(self: Skill):
        if self.status.stacks["闹须弥·持续"]:
            self.status.skills["见尘"].cast()

    def __call__(self, status: Status):
        status.skills["上将军印"].pre_cast_effect.append(self.jian_chen_pre_cast)


class HanFeng:
    @staticmethod
    def han_feng_post_hit(self: Skill):
        self.status.buffs["含风"].refresh()

    def __call__(self, status: Status):
        status.skills["刀啸风吟"].post_hit_effect.append(self.han_feng_post_hit)


class FenJiang:
    def __call__(self, status: Status):
        status.skills["上将军印"].interval_list = [4, 4, 5, 5, 5, 5, 4]
        status.skills["见尘"].interval_list = [5, 4, 5, 5, 5, 5, 4]


class XingHuo:
    def __call__(self, status: Status):
        status.attribute.strength_gain += 0.1


class ChuGe:
    @staticmethod
    def chu_ge_pre_cast(self: Skill):
        self.status.buffs["楚歌"].trigger()

    @staticmethod
    def chu_ge_post_hit(self: Skill):
        self.status.buffs["楚歌·计数"].trigger()

    def __call__(self, status: Status):
        status.skills["破釜沉舟"].cd_base -= 3 * 16
        status.skills["破釜沉舟"].skill_critical_strike += 0.1
        status.skills["破釜沉舟"].skill_critical_power += 0.2
        status.skills["破釜沉舟"].pre_cast_effect.append(self.chu_ge_pre_cast)
        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.chu_ge_post_hit)


class JueQi:
    @staticmethod
    def jue_qi_post_hit(self: Skill):
        if self.status.stacks["闹须弥·持续"]:
            self.status.skills["绝期"].cast()

    def __call__(self, status: Status):
        status.skills["闹须弥·持续"].attack_power_cof_gain += 0.7

        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.jue_qi_post_hit)


class ZhongYan:
    @staticmethod
    def zhong_yan_add_effect(self: Buff):
        self.status.attribute.cd_reduction += 0.3

    @staticmethod
    def zhong_yan_remove_effect(self: Buff):
        self.status.attribute.cd_reduction -= 0.3

    def __call__(self, status: Status):
        status.buffs["秀明尘身"].add_effect.append(self.zhong_yan_add_effect)
        status.buffs["秀明尘身"].remove_effect.append(self.zhong_yan_remove_effect)


class XiangQiShi:
    @staticmethod
    def qin_long_post_cast(self: Skill):
        self.status.cds["擒龙六斩"] -= 2 * 16

    @staticmethod
    def xiang_qi_shi_post_cast(self: Skill):
        self.status.buffs["降麒式·计数"].trigger()

    def __call__(self, status: Status):
        related_skills = ["惊燕式", "逐鹰式"]

        for skill in related_skills:
            status.skills[skill].post_cast_effect.append(self.qin_long_post_cast)
            status.skills[skill].post_cast_effect.append(self.xiang_qi_shi_post_cast)


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
    "龙息": LongXi(),
    "归酣": GuiHan(),
    "阳关": YangGuan(),
    "霜天": ShuangTian(),
    "含风": HanFeng(),
    "见尘": JianChen(),
    "分疆": FenJiang(),
    "星火": XingHuo(),
    "楚歌": ChuGe(),
    "绝期": JueQi(),
    "重烟": ZhongYan(),
    "降麒式": XiangQiShi(),
}
