from base.skill import Skill
from base.status import Status


def dao_xiao_set_gain(status: Status):
    status.skills["刀啸风吟"].skill_damage_addition += 0.1


def shang_jiang_set_gain(status: Status):
    status.skills["上将军印"].skill_damage_addition += 0.1
    status.skills["见尘"].skill_damage_addition += 0.1


def attribute_set_gain(status: Status):
    related_skills = ["霜风刀法", "雷走风切", "上将军印", "破釜沉舟", "坚壁清野", "刀啸风吟", "惊燕式", "逐鹰式"]

    def attribute_set_post_cast(self: Skill):
        self.status.buffs["朔气"].trigger()

    for skill in related_skills:
        status.skills[skill].post_cast_effect.append(attribute_set_post_cast)


def dao_xiao_divine_gain(status: Status):
    status.skills["刀啸风吟"].skill_damage_addition += 0.05


def xiang_wang_divine_gain(status: Status):
    pass


def divine_effect(status: Status):
    pass


def shang_jiang_divine_gain(status: Status):
    pass


def water_weapon_gain(value):
    def inner(status: Status):
        related_skills = ["霜风刀法", "雷走风切", "上将军印", "破釜沉舟", "坚壁清野", "刀啸风吟", "惊燕式", "逐鹰式"]

        status.buffs["水特效"].value = value

        def water_weapon_post_hit(self: Skill):
            self.status.buffs["水特效"].trigger()

        for skill in related_skills:
            status.skills[skill].post_hit_effect.append(water_weapon_post_hit)

    return inner


def wind_pendant_gain(value):
    def inner(status: Status):
        status.buffs["风特效"].value = value

    return inner


gains = [dao_xiao_set_gain, shang_jiang_set_gain, attribute_set_gain]
