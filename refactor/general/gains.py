from base.skill import Skill
from base.status import Status

""" permanent gain """


def han_ru_lei(status: Status):
    status.attribute.physical_attack_power_gain += 0.1


def po_feng(status: Status):
    status.attribute.target.physical_shield_base -= 32


def xiu_qi(status: Status):
    status.attribute.all_major_base += 32


""" Weapon Enchant """


def physical_attack_power_enchant(status: Status):
    status.attribute.physical_attack_power_base += 1


""" Major Food """


def strength_food(status: Status):
    status.attribute.strength_base += 1


""" Minor Food """


def surplus_food(status: Status):
    status.attribute.surplus += 1


def haste_food(status: Status):
    status.attribute.haste_base += 1


def physical_attack_power_food(status: Status):
    status.attribute.physical_attack_power_base += 1


def physical_critical_strike_food(status: Status):
    status.attribute.physical_critical_strike_base += 1


def physical_overcome_food(status: Status):
    status.attribute.physical_overcome_base += 1


""" Major Potion """


def strength_potion(status: Status):
    status.attribute.strength_base += 1


""" Minor Potion """


def surplus_potion(status: Status):
    status.attribute.surplus += 1


def haste_potion(status: Status):
    status.attribute.haste_base += 1


def physical_attack_power_potion(status: Status):
    status.attribute.physical_attack_power_base += 1


def physical_critical_strike_potion(status: Status):
    status.attribute.physical_critical_strike_base += 1


def physical_overcome_potion(status: Status):
    status.attribute.physical_overcome_base += 1


""" periodic gain """


def water_weapon_gain(value):
    def inner(status: Status):
        status.buffs["水特效"].value = value

        def water_weapon_post_hit(self: Skill):
            self.status.buffs["水特效"].trigger()

        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(water_weapon_post_hit)

    return inner


def wind_pendant_gain(value):
    def inner(status: Status):
        status.buffs["风特效"].value = value

    return inner


def special_enchant_hat_gain(value):
    def inner(status: Status):
        status.attribute.physical_overcome_base += value

    return inner


def special_enchant_jacket_gain(value):
    def inner(status: Status):
        status.attribute.physical_attack_power_base += value

    return inner


def special_enchant_belt_gain(status: Status):
    def enchant_belt_post_hit(self: Skill):
        if not self.status.stacks["大附魔腰"]:
            self.status.skills["大附魔腰"].cast()

    for skill in status.skills.values():
        if skill.base_damage:
            skill.post_hit_effect.append(enchant_belt_post_hit)


def special_enchant_wrist_gain(status: Status):
    def enchant_wrist_post_hit(self: Skill):
        if not self.status.stacks["大附魔手"]:
            self.status.skills["昆吾·弦刃"].cast()

    for skill in status.skills.values():
        if skill.base_damage:
            skill.post_hit_effect.append(enchant_wrist_post_hit)


def special_enchant_shoes_gain(status: Status):
    def enchant_wrist_critical_hit(self: Skill):
        if not self.status.stacks["大附魔脚"]:
            self.status.skills["刃凌"].cast()

    for skill in status.skills.values():
        if skill.base_damage:
            skill.critical_hit_effect.append(enchant_wrist_critical_hit)

