from base.buff import Buff
from base.skill import Skill
from base.status import Status


def long_xi(status: Status):
    related_skills = ["惊燕式", "逐鹰式"]
    for skill in related_skills:
        status.skills[skill].interval_list = None
        status.skills[skill].count_base = 2
        status.skills[skill].interval_base = 0

    status.skills["擒龙六斩"].energy = 6


def gui_han(status: Status):
    status.skills["上将军印"].cd_base -= 120 + 5 * 8

    # def gui_han_post_damage(self: Skill):
    #     if self.status.counts[self] > self.count - 5:
    #         self.status.cds[self] -= 8
    #
    # status.skills["上将军印"].post_damage_effect.append(gui_han_post_damage)


def yang_guan(status: Status):
    status.skills["上将军印"].skill_damage_addition += 0.15
    status.skills["见尘"].skill_damage_addition += 0.15

    status.skills["上将军印"].skill_shield_ignore_base += 0.2


def shuang_tian(status: Status):
    def shuang_tian_post_hit(self: Skill):
        self.base_damage_gain += 0.15
        self.rand_damage_gain += 0.15
        self.attack_power_cof_gain += 0.15

        if self.status.counts[self.name] < 4:
            self.weapon_damage_cof_gain += 0.15

    def shuang_tian_post_cast(self: Skill):
        count = self.status.counts[self.name]
        self.base_damage_gain -= 0.15 * count
        self.rand_damage_gain -= 0.15 * count
        self.attack_power_cof_gain -= 0.15 * count

        self.weapon_damage_cof_gain -= 0.15 * min(4, count)

    status.skills["上将军印"].post_hit_effect.append(shuang_tian_post_hit)
    status.skills["上将军印"].post_cast_effect.append(shuang_tian_post_cast)


def jian_chen(status: Status):
    def jian_chen_pre_cast(self: Skill):
        self.status.skills["见尘"].cast()

    status.skills["上将军印"].pre_cast_effect.append(jian_chen_pre_cast)


def han_feng(status: Status):
    def han_feng_post_hit(self: Skill):
        self.status.buffs["含风"].refresh()

    status.skills["刀啸风吟"].post_hit_effect.append(han_feng_post_hit)


def fen_jiang(status: Status):
    status.skills["上将军印"].interval_list = [4, 4, 5, 5, 5, 5, 4]
    status.skills["见尘"].interval_list = [5, 4, 5, 5, 5, 5, 4]


def xing_huo(status: Status):
    status.attribute.strength_gain += 0.1


def chu_ge(status: Status):
    status.skills["破釜沉舟"].cd_base -= 3 * 16
    status.skills["破釜沉舟"].skill_critical_strike += 0.1
    status.skills["破釜沉舟"].skill_critical_power += 0.2

    def chu_ge_pre_cast(self: Skill):
        self.status.buffs["楚歌"].trigger()

    status.skills["破釜沉舟"].pre_cast_effect.append(chu_ge_pre_cast)

    def chu_ge_post_hit(self: Skill):
        self.status.buffs["楚歌·计数"].trigger()

    related_skills = ["霜风刀法", "雷走风切", "上将军印", "破釜沉舟", "坚壁清野·持续",
                      "坚壁清野", "刀啸风吟", "惊燕式", "逐鹰式", "降麒式·持续"]
    for skill in related_skills:
        status.skills[skill].post_hit_effect.append(chu_ge_post_hit)


def jue_qi(status: Status):
    status.skills["闹须弥·持续"].attack_power_cof_gain += 0.7

    def jue_qi_post_hit(self: Skill):
        if self.status.stacks["闹须弥·持续"]:
            self.status.skills["绝期"].cast()

    related_skills = ["霜风刀法", "雷走风切", "上将军印", "破釜沉舟", "坚壁清野·持续",
                      "坚壁清野", "刀啸风吟", "惊燕式", "逐鹰式", "降麒式·持续"]
    for skill in related_skills:
        status.skills[skill].post_hit_effect.append(jue_qi_post_hit)


def zhong_yan(status: Status):
    related_skills = ["秀明尘身", "松烟竹雾", "雪絮金屏", "雷走风切",
                      "上将军印", "破釜沉舟", "坚壁清野", "闹须弥", "擒龙六斩", "惊燕式", "逐鹰式"]

    def zhong_yan_add_effect(self: Buff):
        for skill in related_skills:
            if skill in self.status.cds:
                self.status.cds[skill] /= 1.3
            self.status.skills[skill].cd_base /= 1.3

    def zhong_yan_remove_effect(self: Buff):
        for skill in related_skills:
            if skill in self.status.cds:
                self.status.cds[skill] *= 1.3
            self.status.skills[skill].cd_base *= 1.3

    status.buffs["秀明尘身"].add_effect.append(zhong_yan_add_effect)
    status.buffs["秀明尘身"].remove_effect.append(zhong_yan_remove_effect)


def xiang_qi_shi(status: Status):
    related_skills = ["惊燕式", "逐鹰式"]

    def qin_long_post_cast(self: Skill):
        self.status.cds["擒龙六斩"] -= 2 * 16

    for skill in related_skills:
        status.skills[skill].post_cast_effect.append(qin_long_post_cast)

    def xiang_qi_shi_post_cast(self: Skill):
        self.status.buffs["降麒式·计数"].trigger()

    for skill in related_skills:
        status.skills[skill].post_cast_effect.append(xiang_qi_shi_post_cast)


talents = [long_xi, gui_han, yang_guan, shuang_tian, han_feng, jian_chen, fen_jiang, xing_huo, chu_ge, jue_qi,
           zhong_yan, xiang_qi_shi]
