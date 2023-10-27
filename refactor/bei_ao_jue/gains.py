from base.skill import Skill
from base.status import Status


def skill_set_gain(status: Status):
    status.skills["上将军印"].damage_addition_gain += 0.1
    status.skills["见尘"].damage_addition_gain += 0.1
    status.skills["刀啸风吟"].damage_addition_gain += 0.1


def attribute_set_gain(status: Status):
    related_skills = ["霜风刀法", "雷走风切", "上将军印", "破釜沉舟", "坚壁清野", "刀啸风吟", "惊燕式", "逐鹰式"]

    def attribute_set_post_cast(self: Skill):
        self.status.buffs["朔气"].trigger()

    for skill in related_skills:
        status.skills[skill].post_cast_effect.append(attribute_set_post_cast)


def divine_gain(status: Status):
    pass


def sub_divine_gain(status: Status):
    pass


def water_weapon_gain(status: Status):
    related_skills = ["霜风刀法", "雷走风切", "上将军印", "破釜沉舟", "坚壁清野", "刀啸风吟", "惊燕式", "逐鹰式"]

    def water_weapon_post_damage(self: Skill):
        self.status.buffs["水特效"].trigger()

    for skill in related_skills:
        status.skills[skill].post_damage_effect.append(water_weapon_post_damage)


gains = [
    skill_set_gain, attribute_set_gain, water_weapon_gain
]
