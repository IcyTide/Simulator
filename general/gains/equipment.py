from base.skill import Skill
from base.status import Status

""" Equipment Gains """


class 外功水特效:
    def __init__(self, value):
        self.stacks = 10
        self.value = value

    def __call__(self, status: Status):
        status.attribute.physical_attack_power_base += self.value * self.stacks


class 内功水特效:
    def __init__(self, value):
        self.stacks = 10
        self.value = value

    def __call__(self, status: Status):
        status.attribute.magical_attack_power_base += self.value * self.stacks


class 外功风特效:
    def __init__(self, value):
        self.duration = 15
        self.cd = 180
        self.value = value

    def __call__(self, status: Status):
        status.attribute.physical_overcome_base += self.value * self.duration / self.cd


class 内功风特效:
    def __init__(self, value):
        self.duration = 15
        self.cd = 180
        self.value = value

    def __call__(self, status: Status):
        status.attribute.magical_overcome_base += self.value * self.duration / self.cd


class 大附魔帽:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.attribute.physical_overcome_base += self.value
        status.attribute.magical_overcome_base += self.value


class 大附魔衣:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __call__(self, status: Status):
        status.attribute.physical_attack_power_base += self.value1
        status.attribute.magical_attack_power_base += self.value2


class 大附魔腰:
    @staticmethod
    def enchant_belt_post_hit(self: Skill):
        if not self.status.stacks["大附魔腰-冷却"]:
            self.status.skills["大附魔腰"].cast()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.enchant_belt_post_hit)


class 大附魔腕:
    @staticmethod
    def enchant_wrist_post_hit(self: Skill):
        if not self.status.stacks["大附魔腕-冷却"]:
            self.status.skills["昆吾·弦刃"].cast()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.enchant_wrist_post_hit)


class 大附魔鞋:
    @staticmethod
    def enchant_shoes_critical_hit(self: Skill):
        if not self.status.stacks["大附魔脚-冷却"]:
            self.status.skills["刃凌"].cast()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_hit:
                skill.critical_hit_effect.append(self.enchant_shoes_critical_hit)


EQUIP_GAINS_NUMBER = {
    "15436-9": 822,
    "15436-10": 999,
    "15436-11": 1098,
    "22151-9": (371, 442),
    "22151-10": (450, 538),
    "22151-11": (495, 591),
    "2400": 81,
    "2401": 67,
    "2497": 105,
    "2498": 88,
    "2539": 117,
    "2540": 98,
    "6800-101": 6408,
    "6800-102": 6408,
    "6800-108": 8330,
    "6800-109": 8330,
    "6800-115": 9291,
    "6800-116": 9291
}
EQUIP_GAINS_NAME = {
    "15436-9": f"大附魔帽 {EQUIP_GAINS_NUMBER['15436-9']} 破防",
    "15436-10": f"大附魔帽 {EQUIP_GAINS_NUMBER['15436-10']} 破防",
    "15436-11": f"大附魔帽 {EQUIP_GAINS_NUMBER['15436-11']} 破防",
    "22151-9": f"大附魔衣 {EQUIP_GAINS_NUMBER['22151-9'][0]}/{EQUIP_GAINS_NUMBER['22151-9'][1]} 外/内攻",
    "22151-10": f"大附魔衣 {EQUIP_GAINS_NUMBER['22151-9'][0]}/{EQUIP_GAINS_NUMBER['22151-9'][1]} 外/内攻",
    "22151-11": f"大附魔衣 {EQUIP_GAINS_NUMBER['22151-9'][0]}/{EQUIP_GAINS_NUMBER['22151-9'][1]} 外/内攻",
    "22169": "大附魔腰",
    "22166": "大附魔腕",
    "33247": "大附魔鞋",
    "2400": f"水特效 {EQUIP_GAINS_NUMBER['2400']} 内攻",
    "2401": f"水特效 {EQUIP_GAINS_NUMBER['2401']} 外攻",
    "2497": f"水特效 {EQUIP_GAINS_NUMBER['2497']} 内攻",
    "2498": f"水特效 {EQUIP_GAINS_NUMBER['2498']} 外攻",
    "2539": f"水特效 {EQUIP_GAINS_NUMBER['2539']} 内攻",
    "2540": f"水特效 {EQUIP_GAINS_NUMBER['2540']} 外攻",
    "6800-101": f"风特效 {EQUIP_GAINS_NUMBER['6800-101']} 内破",
    "6800-102": f"风特效 {EQUIP_GAINS_NUMBER['6800-102']} 外破",
    "6800-108": f"风特效 {EQUIP_GAINS_NUMBER['6800-108']} 内破",
    "6800-109": f"风特效 {EQUIP_GAINS_NUMBER['6800-109']} 外破",
    "6800-115": f"风特效 {EQUIP_GAINS_NUMBER['6800-115']} 内破",
    "6800-116": f"风特效 {EQUIP_GAINS_NUMBER['6800-116']} 外破",
}
EQUIP_GAINS = {
    "15436-9": 大附魔帽(EQUIP_GAINS_NUMBER['15436-9']),
    "15436-10": 大附魔帽(EQUIP_GAINS_NUMBER['15436-10']),
    "15436-11": 大附魔帽(EQUIP_GAINS_NUMBER['15436-11']),
    "22151-9": 大附魔衣(*EQUIP_GAINS_NUMBER['22151-9']),
    "22151-10": 大附魔衣(*EQUIP_GAINS_NUMBER['22151-10']),
    "22151-11": 大附魔衣(*EQUIP_GAINS_NUMBER['22151-11']),
    "22169": 大附魔腰(),
    "22166": 大附魔腕(),
    "33247": 大附魔鞋(),
    "2400": 内功水特效(EQUIP_GAINS_NUMBER['2400']),
    "2401": 外功水特效(EQUIP_GAINS_NUMBER['2401']),
    "2497": 内功水特效(EQUIP_GAINS_NUMBER['2497']),
    "2498": 外功水特效(EQUIP_GAINS_NUMBER['2498']),
    "2539": 内功水特效(EQUIP_GAINS_NUMBER['2539']),
    "2540": 外功水特效(EQUIP_GAINS_NUMBER['2540']),
    "6800-101": 内功风特效(EQUIP_GAINS_NUMBER['6800-101']),
    "6800-102": 外功风特效(EQUIP_GAINS_NUMBER['6800-102']),
    "6800-108": 内功风特效(EQUIP_GAINS_NUMBER['6800-108']),
    "6800-109": 外功风特效(EQUIP_GAINS_NUMBER['6800-109']),
    "6800-115": 内功风特效(EQUIP_GAINS_NUMBER['6800-115']),
    "6800-116": 外功风特效(EQUIP_GAINS_NUMBER['6800-116']),
}
