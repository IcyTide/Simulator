from base.skill import Skill
from base.status import Status

""" Equipment Gains """


class WaterWeaponGain:
    def __init__(self, value):
        self.stacks = 10
        self.value = value

    def __call__(self, status: Status):
        status.attribute.physical_attack_power_base += self.value * self.stacks


class WindPendantGain:
    def __init__(self, value):
        self.duration = 15
        self.cd = 180
        self.value = value

    def __call__(self, status: Status):
        status.attribute.physical_overcome_base += self.value * self.duration / self.cd


class SpecialEnchantHatGain:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.attribute.physical_overcome_base += self.value


class SpecialEnchantJacketGain:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.attribute.physical_attack_power_base += self.value


class SpecialEnchantBeltGain:
    @staticmethod
    def enchant_belt_post_hit(self: Skill):
        if not self.status.stacks["大附魔腰·冷却"]:
            self.status.skills["大附魔腰"].cast()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.enchant_belt_post_hit)


class SpecialEnchantWristGain:
    @staticmethod
    def enchant_wrist_post_hit(self: Skill):
        if not self.status.stacks["大附魔手·冷却"]:
            self.status.skills["昆吾·弦刃"].cast()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.enchant_wrist_post_hit)


class SpecialEnchantShoesGain:
    @staticmethod
    def enchant_shoes_critical_hit(self: Skill):
        if not self.status.stacks["大附魔脚·冷却"]:
            self.status.skills["刃凌"].cast()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_hit:
                skill.critical_hit_effect.append(self.enchant_shoes_critical_hit)


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
    "15436-9": SpecialEnchantHatGain(EQUIP_GAINS_NUMBER['15436-9']),
    "15436-10": SpecialEnchantHatGain(EQUIP_GAINS_NUMBER['15436-10']),
    "15436-11": SpecialEnchantHatGain(EQUIP_GAINS_NUMBER['15436-11']),
    "22151-9": SpecialEnchantJacketGain(EQUIP_GAINS_NUMBER['22151-9']),
    "22151-10": SpecialEnchantJacketGain(EQUIP_GAINS_NUMBER['22151-10']),
    "22151-11": SpecialEnchantJacketGain(EQUIP_GAINS_NUMBER['22151-11']),
    "22169": SpecialEnchantBeltGain(),
    "22166": SpecialEnchantWristGain(),
    "33247": SpecialEnchantShoesGain(),
    "2401": WaterWeaponGain(EQUIP_GAINS_NUMBER['2401']),
    "2498": WaterWeaponGain(EQUIP_GAINS_NUMBER['2498']),
    "2540": WaterWeaponGain(EQUIP_GAINS_NUMBER['2540']),
    "6800-102": WindPendantGain(EQUIP_GAINS_NUMBER['6800-102']),
    "6800-109": WindPendantGain(EQUIP_GAINS_NUMBER['6800-109']),
    "6800-116": WindPendantGain(EQUIP_GAINS_NUMBER['6800-116']),
}
