from base.constant import ATTACK_POWER_COF
from base.skill import Skill


class WristEnchant(Skill):
    def __init__(self):
        super(WristEnchant, self).__init__()
        self.name = "昆吾·弦刃"

        self.is_cast = False

        self.base_damage_base = 40
        self.rand_damage_base = 17
        self.attack_power_cof_base = ATTACK_POWER_COF(75)


class ShoesEnchant(Skill):
    def __init__(self):
        super(ShoesEnchant, self).__init__()
        self.name = "刃凌"

        self.is_cast = False

        self.base_damage_base = 40
        self.rand_damage_base = 17
        self.attack_power_cof_base = ATTACK_POWER_COF(60)
