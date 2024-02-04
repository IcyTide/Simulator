from base.constant import MAGICAL_ATTACK_POWER_COF, MAGICAL_DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import *

"""
    Base Skills
"""


class 连环双刀(Melee):
    def __init__(self, status):
        super().__init__(status)
        self.name = "连环双刀"

        self.gcd_index = self.name
        self.gcd_base = 24

        self.skill_damage_addition = 205 / 1024


class 破(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破"

        self.is_cast = False
        self.is_hit = False

        self.surplus_cof = [
            SURPLUS_COF(1024 * 1024 * (0.2 - 1)),
            SURPLUS_COF(1024 * 1024 * (0.46 - 1)),
            SURPLUS_COF(1024 * 1024 * (0.575 - 1)),
            SURPLUS_COF(1024 * 1024 * (0.92 - 1)),
            SURPLUS_COF(1024 * 1024 * (1.035 - 1)),
        ]


class 蝎心(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蝎心"

        self.interval_base = 28

        self.sub_skills = ["蝎心-伤害"]

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["破"]:
            self.status.skills["破"].cast()
            self.status.buffs["破"].clear()


class 蝎心_伤害(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蝎心-伤害"
        self.damage_base = 170
        self.damage_rand = int(489 / 3 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF((104 + 28) * 1.3 * 1.1 * 1.2 * 1.15)


class 蛇影(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛇影"

        self.cd_base = 12 * 16

        self.sub_skills = ["蛇影-持续"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["破"].trigger()


class 蛇影_持续(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛇影-持续"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 32
        self.tick_base = 6

        self.damage_base = 55
        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(286 * 1.1 * 1.15, self.interval_base)


class 百足(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "百足"

        self.cd_base = 18 * 16

        self.sub_skills = ["百足-伤害", "百足-持续"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["破"].trigger()


class 百足_伤害(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "百足-伤害"

        self.damage_base = int(250 * 0.85)
        self.damage_rand = int(230 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(216 * 1.15 * 1.1 * 1.05 * 1.1 * 1.2)


class 百足_持续(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "百足-持续"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 48
        self.tick_base = 6

        self.damage_base = 92
        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(232 * 1.1 * 1.05 * 1.1 * 1.15 * 1.2, self.interval_base)


class 蟾啸(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蟾啸"

        self.cd_base = 12 * 16

        self.sub_skills = ["蟾啸-持续"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["破"].trigger()


class 蟾啸_持续(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蟾啸-持续"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 32
        self.tick_base = 7

        self.damage_base = 50
        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(232 * 1.1 * 1.05 * 1.15 * 1.15, self.interval_base)


class 灵蛊(CastingSkill, ChargingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "灵蛊"

        self.energy = 3

        self.gcd_index = self.name
        self.cd_base = 20 * 16

        self.damage_base = int(30 * 0.95)
        self.damage_rand = int(30 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(16)


class 凤凰蛊(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "凤凰蛊"

        self.is_cast = False
        self.is_hit = False

        self.cd_base = 15 * 60 * 16

    def post_cast(self):
        super().post_cast()
        self.status.buffs["凤凰蛊"].trigger()


class 灵蛇引(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "灵蛇引"

        self.is_cast = False
        self.is_hit = False

        self.cd_base = 30 * 16
        self.gcd_index = self.name

    def post_cast(self):
        super().post_cast()
        self.status.buffs["灵蛇引"].trigger()


class 攻击(LoopSkill, PetDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "攻击"

        self.pet = "灵蛇引"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 4 * 16

        self.damage_base = int(43 * 0.95)
        self.damage_rand = int(43 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(86 * 1.5)
        self.skill_pve_addition += 154 / 1024

    @property
    def condition(self):
        return self.status.stacks["灵蛇引"]


class 幻击(CastingSkill, PetDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "幻击"

        self.pet = "灵蛇引"

        self.is_cast = False
        self.is_hit = False

        self.cd_base = 12 * 16

        self.damage_base = int(205 * 0.95)
        self.damage_rand = int(205 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(115)
        self.skill_pve_addition += 154 / 1024

    @property
    def condition(self):
        return self.status.stacks["灵蛇引"]


class 蛊虫献祭(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛊虫献祭"

        self.is_cast = False
        self.is_hit = False

        self.cd_base = 35 * 16
        self.gcd_index = self.name

    @property
    def condition(self):
        return self.status.stacks["灵蛇引"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["灵蛇献祭"].trigger()


"""
    Talent Skills
"""


class 蝎心_持续(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蝎心-持续"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 32
        self.tick_base = 6

        self.damage_base = 80
        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(270 * 1.3 * 1.1 * 1.1 * 1.15, self.interval_base)

    def pre_cast(self):
        super().pre_cast()
        if self.status.stacks["破"]:
            self.status.skills["破"].cast()
            self.status.buffs["破"].clear()


class 黯影(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "黯影"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 20
        self.damage_rand = 2
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(100)


class 蟾啸_伤害(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蟾啸-伤害"

        self.damage_base = int(300 * 0.95)
        self.damage_rand = int(300 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(136 * 1.1 * 1.05 * 1.3 * 1.2)


class 荒息(PetDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "荒息"

        self.pet = "灵蛇引"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = int(43 * 0.95)
        self.damage_rand = int(43 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(86 * 1.5 * 2 * 0.9 * 0.9)
        self.skill_pve_addition += 154 / 1024

    def post_cast(self):
        super().post_cast()
        self.status.cds["灵蛇引"] = max(0, self.status.cds["灵蛇引"] - 160)


class 篾片蛊(PlacementSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "篾片蛊"

        self.activate = False

        self.interval_list = [5 * 16]
        self.damage_base = [225, 260, 295, 330, 365, 400]
        self.damage_rand = [19, 20, 21, 22, 23, 24]
        self.attack_power_cof = [MAGICAL_ATTACK_POWER_COF((117 * (5 + (i + 1)) * 1.15 * 1.1) * 1.1) for i in range(6)]

    def pre_hit(self):
        super().pre_hit()
        self.level = self.status.stacks[self.name]


class 蛊虫狂暴(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛊虫狂暴"

        self.activate = False

        self.is_cast = False
        self.is_hit = False

        self.cd_base = 120 * 16

    def post_cast(self):
        super().post_cast()
        self.status.buffs["蛊虫狂暴"].trigger()


class 蛇影_伤害(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛇影-伤害"

        self.damage_base = int(250 * 0.85)
        self.damage_rand = int(230 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(217 * 1.3 * 1.1 * 1.7)


class 连缘蛊(ChannelSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "连缘蛊"

        self.activate = False

        self.is_cast = False
        self.hit_with_cast = True

        self.interval_base = 9
        self.tick_base = 5

        self.cd_base = 30 * 16

        self.damage_base = int(43 * 0.95)
        self.damage_rand = int(43 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(100 * 0.9 * 1.1 * 1.1)

        self.skill_pve_addition += 256 / 1024

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["连缘蛊-无视"].trigger()

    def post_hit(self):
        super().post_hit()
        self.status.skills["破"].cast(self.status.stacks["连缘蛊-增伤"] + 1)

    def post_cast(self):
        super().post_cast()
        self.status.skills["连缘蛊-额外"].cast(self.status.stacks["连缘蛊-增伤"] + 1)
        self.status.buffs["连缘蛊-无视"].clear()


class 连缘蛊_额外(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "连缘蛊-额外"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = [int(43 * 0.95), int(70 * 0.95), int(94 * 0.95), int(117 * 0.95), int(141 * 0.95)]
        self.damage_rand = [int(43 * 0.1), int(70 * 0.1), int(94 * 0.1), int(117 * 0.1), int(141 * 0.1)]
        self.attack_power_cof = [MAGICAL_ATTACK_POWER_COF(100 * (i + 1) * 1.1 * 1.1) for i in range(5)]

        self.skill_pve_addition += 256 / 1024

    def post_hit(self):
        super().post_hit()
        self.status.skills["破"].cast(self.status.stacks["连缘蛊-增伤"] + 1)


SKILLS_MAP = {
    "通用": [连环双刀, 破],
    "千劫万毒手": [蝎心, 蝎心_伤害, 蛇影, 蛇影_持续, 百足, 百足_伤害, 百足_持续, 蟾啸, 蟾啸_持续],
    "引魂蛊术": [灵蛊, 凤凰蛊],
    "驭虫奇术": [灵蛇引, 攻击, 幻击, 蛊虫献祭],
    "奇穴": [蝎心_持续, 黯影, 蟾啸_伤害, 荒息, 篾片蛊, 蛊虫狂暴, 蛇影_伤害, 连缘蛊, 连缘蛊_额外]
}
SKILLS = sum(SKILLS_MAP.values(), [])
