from base.constant import PHYSICAL_ATTACK_POWER_COF, MAGICAL_ATTACK_POWER_COF
from base.skill import Skill, PhysicalSkill, MagicalSkill


class 大附魔腰(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔腰"

        self.is_cast = False
        self.is_hit = False

        self.probability = 0.2

    def post_cast(self):
        super().post_cast()
        if self.roll < 0.3:
            self.status.buffs["大附魔腰"].trigger(1)
        else:
            self.status.buffs["大附魔腰"].trigger(2)
        self.status.buffs["大附魔腰-冷却"].trigger()


class 外功_昆吾_弦刃(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "昆吾·弦刃"

        self.is_cast = False
        self.is_hit = False

        self.probability = 0.1

        self.damage_base = 40
        self.damage_rand = 17
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(75)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["大附魔手-冷却"].trigger()


class 内功_昆吾_弦刃(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "昆吾·弦刃"

        self.is_cast = False
        self.is_hit = False

        self.probability = 0.1

        self.damage_base = 40
        self.damage_rand = 17
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(75)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["大附魔手-冷却"].trigger()


class 外功_刃凌(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "刃凌"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 40
        self.damage_base = 17
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(60)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["大附魔脚-冷却"].trigger()


class 内功_刃凌(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "刃凌"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 40
        self.damage_base = 17
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(90)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["大附魔脚-冷却"].trigger()


SKILLS = {
    "外功": [大附魔腰, 外功_昆吾_弦刃, 外功_刃凌],
    "内功": [大附魔腰, 内功_昆吾_弦刃, 内功_刃凌]
}
