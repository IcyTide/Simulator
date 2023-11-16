from base.constant import FRAME_PER_SECOND
from base.skill import Skill
from base.status import Status

""" Equipment Gains """


def water_weapon_gain(value):
    stacks = 10

    def inner(status: Status):
        status.attribute.physical_attack_power_base += value * stacks
        # status.buffs["水特效"].value = value
        #
        # def water_weapon_post_hit(self: Skill):
        #     self.status.buffs["水特效"].trigger()
        #
        # for skill in status.skills.values():
        #     if skill.is_hit:
        #         skill.post_hit_effect.append(water_weapon_post_hit)

    return inner


def wind_pendant_gain(value):
    duration = 15

    def inner(status: Status):
        status.attribute.physical_overcome_base += value * duration * FRAME_PER_SECOND / status.total_frame
        # status.buffs["风特效"].value = value

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
        if skill.is_hit:
            skill.post_hit_effect.append(enchant_belt_post_hit)


def special_enchant_wrist_gain(status: Status):
    def enchant_wrist_post_hit(self: Skill):
        if not self.status.stacks["大附魔手"]:
            self.status.skills["昆吾·弦刃"].cast()

    for skill in status.skills.values():
        if skill.is_hit:
            skill.post_hit_effect.append(enchant_wrist_post_hit)


def special_enchant_shoes_gain(status: Status):
    def enchant_wrist_critical_hit(self: Skill):
        if not self.status.stacks["大附魔脚"]:
            self.status.skills["刃凌"].cast()

    for skill in status.skills.values():
        if skill.is_hit:
            skill.critical_hit_effect.append(enchant_wrist_critical_hit)
