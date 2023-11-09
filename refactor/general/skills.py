from base.constant import ATTACK_POWER_COF
from base.skill import Skill, PhysicalSkill


class BeltEnchant(Skill):
    def __init__(self):
        super().__init__()
        self.name = "大附魔腰"

        self.is_cast = False
        self.is_hit = False

        self.probability = 0.2

    def post_cast(self):
        if self.roll < 0.3:
            self.status.buffs["大附魔腰·1%"].trigger()
        else:
            self.status.buffs["大附魔腰·5%"].trigger()
        self.status.buffs["大附魔腰·冷却"].trigger()


class WristEnchant(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "昆吾·弦刃"

        self.is_cast = False
        self.is_hit = False

        self.probability = 0.1

        self.base_damage_base = 40
        self.rand_damage_base = 17
        self.attack_power_cof_base = ATTACK_POWER_COF(75)

    def post_cast(self):
        self.status.buffs["大附魔手·冷却"].trigger()


class ShoesEnchant(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "刃凌"

        self.is_cast = False
        self.is_hit = False

        self.base_damage_base = 40
        self.rand_damage_base = 17
        self.attack_power_cof_base = ATTACK_POWER_COF(60)

    def post_cast(self):
        self.status.buffs["大附魔脚·冷却"].trigger()
