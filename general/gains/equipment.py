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
    cd = 180

    def inner(status: Status):
        status.attribute.physical_overcome_base += value * duration / cd
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
        if not self.status.stacks["大附魔腰·冷却"]:
            self.status.skills["大附魔腰"].cast()

    for skill in status.skills.values():
        if skill.is_hit:
            skill.post_hit_effect.append(enchant_belt_post_hit)


def special_enchant_wrist_gain(status: Status):
    def enchant_wrist_post_hit(self: Skill):
        if not self.status.stacks["大附魔手·冷却"]:
            self.status.skills["昆吾·弦刃"].cast()

    for skill in status.skills.values():
        if skill.is_hit:
            skill.post_hit_effect.append(enchant_wrist_post_hit)


def special_enchant_shoes_gain(status: Status):
    def enchant_wrist_critical_hit(self: Skill):
        if not self.status.stacks["大附魔脚·冷却"]:
            self.status.skills["刃凌"].cast()

    for skill in status.skills.values():
        if skill.is_hit:
            skill.critical_hit_effect.append(enchant_wrist_critical_hit)


EQUIP_GAINS_NUMBER = {
    "15436-9": 822,
    "15436-10": 999,
    "15436-11": 1098,
    "22151-9": 371,
    "22151-10": 450,
    "22151-11": 495,
    "2401": 67,
    "2498": 88,
    "2540": 98,
    "6800-102": 6408,
    "6800-109": 8330,
    "6800-116": 9291
}
EQUIP_GAINS_NAME = {
    "15436-9": f"大附魔帽 {EQUIP_GAINS_NUMBER['15436-9']} 破防",
    "15436-10": f"大附魔帽 {EQUIP_GAINS_NUMBER['15436-10']} 破防",
    "15436-11": f"大附魔帽 {EQUIP_GAINS_NUMBER['15436-11']} 破防",
    "22151-9": f"大附魔衣 {EQUIP_GAINS_NUMBER['22151-9']} 外攻",
    "22151-10": f"大附魔衣 {EQUIP_GAINS_NUMBER['22151-10']} 外攻",
    "22151-11": f"大附魔衣 {EQUIP_GAINS_NUMBER['22151-11']} 外攻",
    "22169": "大附魔腰",
    "22166": "大附魔腕",
    "33247": "大附魔鞋",
    "2401": f"水特效 {EQUIP_GAINS_NUMBER['2401']} 外攻",
    "2498": f"水特效 {EQUIP_GAINS_NUMBER['2498']} 外攻",
    "2540": f"水特效 {EQUIP_GAINS_NUMBER['2540']} 外攻",
    "6800-102": f"风特效 {EQUIP_GAINS_NUMBER['6800-102']} 破防",
    "6800-109": f"风特效 {EQUIP_GAINS_NUMBER['6800-109']} 破防",
    "6800-116": f"风特效 {EQUIP_GAINS_NUMBER['6800-116']} 破防",
}
EQUIP_GAINS = {
    "15436-9": special_enchant_hat_gain(EQUIP_GAINS_NUMBER['15436-9']),
    "15436-10": special_enchant_hat_gain(EQUIP_GAINS_NUMBER['15436-10']),
    "15436-11": special_enchant_hat_gain(EQUIP_GAINS_NUMBER['15436-11']),
    "22151-9": special_enchant_jacket_gain(EQUIP_GAINS_NUMBER['22151-9']),
    "22151-10": special_enchant_jacket_gain(EQUIP_GAINS_NUMBER['22151-10']),
    "22151-11": special_enchant_jacket_gain(EQUIP_GAINS_NUMBER['22151-11']),
    "22169": special_enchant_belt_gain,
    "22166": special_enchant_wrist_gain,
    "33247": special_enchant_shoes_gain,
    "2401": water_weapon_gain(EQUIP_GAINS_NUMBER['2401']),
    "2498": water_weapon_gain(EQUIP_GAINS_NUMBER['2498']),
    "2540": water_weapon_gain(EQUIP_GAINS_NUMBER['2540']),
    "6800-102": wind_pendant_gain(EQUIP_GAINS_NUMBER['6800-102']),
    "6800-109": wind_pendant_gain(EQUIP_GAINS_NUMBER['6800-109']),
    "6800-116": wind_pendant_gain(EQUIP_GAINS_NUMBER['6800-116']),
}
