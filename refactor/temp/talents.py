from base.buff import Buff
from base.skill import Skill
from base.status import Status


def long_xi(status: Status):
    related_skills = ["惊燕式", "逐鹰式"]
    for skill in related_skills:
        status.skills[skill].interval_base = 0

    status.skills["擒龙六斩"].energy = 6


def gui_han(status: Status):
    status.skills["上将军印"].cd_base -= 120

    def gui_han_post_damage(self: Skill):
        self.status.cds[self] -= 24

    status.skills["上将军印"].post_damage_effect.append(gui_han_post_damage)


def yang_guan(status: Status):
    status.skills["上将军印"].damage_addition_gain += 0.15
    status.skills["上将军印"].shield_ignore_gain += 0.2


def shuang_tian(status: Status):
    def shuang_tian_post_damage(self: Skill):
        self.attack_power_cof_gain += 0.15

    status.skills["上将军印"].post_damage_effect.append(shuang_tian_post_damage)


def jian_chen(status: Status):
    def jian_chen_pre_cast(self: Skill):
        self.status.buffs["见尘"].refresh()

    status.skills["上将军印"].pre_cast_effect.append(jian_chen_pre_cast)


def han_feng(status: Status):
    def han_feng_post_damage(self: Skill):
        self.status.buffs["含风"].refresh()

    status.skills["刀啸风吟"].post_damage_effect.append(han_feng_post_damage)


def fen_jiang(status: Status):
    status.skills["上将军印"].interval_list = []


def chu_ge(status: Status):
    def chu_ge_pre_cast(self: Skill):
        self.status.buffs["楚歌"].refresh()

    status.skills["破釜沉舟"].pre_cast_effect.append(chu_ge_pre_cast)

    def chu_ge_post_damage(self: Skill):
        self.status.buffs["楚歌-计数"].refresh()

    related_skills = []
    for skill in related_skills:
        status.skills[skill].post_damage_effect.append(chu_ge_post_damage)


def jue_qi(status: Status):
    status.skills["闹须弥-持续"].damage_addition += 0.7

    def jue_qi_post_damage(self: Skill):
        if self.status.stacks["闹须弥-持续"] and self.roll < 0.3:
            self.status.skills["绝期"].cast()

    related_skills = []
    for skill in related_skills:
        status.skills[skill].post_damage_effect.append(jue_qi_post_damage)


def zhong_yan(status: Status):
    related_skills = []

    def zhong_yan_add_effect(self: Buff):
        for skill in related_skills:
            if self.status.cds[skill]:
                self.status.cds[skill] = round(self.status.cds[skill] / 1.3)

    def zhong_yan_remove_effect(self: Buff):
        for skill in related_skills:
            if self.status.cds[skill]:
                self.status.cds[skill] = round(self.status.cds[skill] * 1.3)

    status.buffs["秀明尘身"].add_effect.append(zhong_yan_add_effect)
    status.buffs["秀明尘身"].remove_effect.append(zhong_yan_remove_effect)


def xiang_qi_shi(status: Status):
    related_skills = []

    def xiang_qi_shi_post_cast(self: Skill):
        self.status.cds["擒龙六斩"] -= 2

    for skill in related_skills:
        status.skills[skill].post_cast_effect.append(xiang_qi_shi_post_cast)

    def xiang_qi_shi_post_cast(self: Skill):
        self.status.buffs["降麒式-前置"].refresh()

    for skill in related_skills:
        status.skills[skill].post_cast_effect.append(xiang_qi_shi_post_cast)