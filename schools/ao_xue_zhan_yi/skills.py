from base.constant import PHYSICAL_ATTACK_POWER_COF, WEAPON_DAMAGE_COF, PHYSICAL_DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import *

"""
    Base Skills
"""


class 梅花枪法(Melee):
    def __init__(self, status):
        super().__init__(status)
        self.name = "梅花枪法"

        self.gcd_index = self.name
        self.gcd_base = 24


class 下马(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "下马"

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = self.name

    @property
    def condition(self):
        return self.status.stacks["骑御"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["骑御"].clear()


class 破(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破"

        self.is_cast = False
        self.is_hit = False

        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (0.429 - 1))


class 流血(DotSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流血"

        self.interval_base = 32
        self.tick_base = 7

        self.attack_power_cof = PHYSICAL_DOT_ATTACK_POWER_COF(248 * 1.15 * 1.05 * 1.05 * 1.1 * 1.1, self.interval_base)


class 穿云(CastingSkill, HastedCD, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "穿云"

        self.cd_base = 32

        self.damage_base = 160
        self.damage_rand = 15
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(158 * 1.05 * 1.1 * 1.1 * 1.12)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["战意"].increase(1)


class 龙吟(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "龙吟"

        self.cd_base = 8 * 16

        self.damage_base = int(298 * 0.65)
        self.damage_rand = 15
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(193 * 1.1 * 1.1 * 1.12 * 1.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["战意"].increase(2)
        self.status.skills["流血"].cast()


class 龙牙(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "龙牙"

        self.damage_base = int(445 * 0.5)
        self.damage_rand = 15
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(197 * 1.1 * 1.1 * 1.15 * 1.1 * 1.1 * 1.12 * 0.9 * 1.1 * 1.05)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    @property
    def condition(self):
        return self.status.stacks["战意"] >= 3

    def post_cast(self):
        self.status.buffs["战意"].decrease(3)
        super().post_cast()
        self.status.skills["破"].cast()


class 撼如雷(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "撼如雷"

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = self.name
        self.cd_base = 30 * 16

    def post_cast(self):
        super().post_cast()
        self.status.buffs["激雷"].trigger()


class 突(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "突"

        self.cd_base = 18 * 16

        self.damage_base = 37
        self.damage_rand = 3
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(16)

    @property
    def condition(self):
        return not self.status.stacks["骑御"]


class 灭(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "灭"

        self.cd_base = 8 * 16

        self.damage_base = int(160 * 1.3)
        self.damage_rand = 10
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(170 * 1.12)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

        self.not_horse = False

    @property
    def condition(self):
        return self.not_horse or not self.status.stacks["骑御"]


class 任驰骋(ChannelSkill, ChargingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "任驰骋"

        self.interval_base = 12
        self.energy = 2
        self.cd_base = 40 * 16

        self.gcd_index = self.name

    @property
    def condition(self):
        return not self.status.stacks["骑御"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["骑御"].trigger()
        self.status.skills["断魂刺"].reset()


class 断魂刺(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "断魂刺"

        self.cd_base = 25 * 16
        self.gcd_index = self.name

        self.damage_base = 39
        self.damage_rand = 3
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(16)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["战意"].increase(3)

    @property
    def condition(self):
        return self.status.stacks["骑御"]


"""
    Talent Skills
"""


class 穿云_挫锐(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "穿云-挫锐"

        self.tick_base = 3

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(130 * 1.1)


class 击水(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "击水"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 78
        self.damage_rand = 10
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(210)


class 渊(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "渊"

        self.activate = False

        self.is_cast = False
        self.is_hit = False

        self.cd_base = 30 * 16
        self.gcd_index = self.name

    def post_cast(self):
        super().post_cast()
        self.status.buffs["渊"].trigger()

    @property
    def condition(self):
        return not self.status.stacks["骑御"]


class 龙牙_龙血(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "龙牙-龙血"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = int(445 * 0.5 * 0.1)
        self.damage_rand = int(15 * 0.1)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(
            197 * 1.1 * 1.1 * 1.15 * 0.4 * 1.1 * 1.1 * 1.12 * 0.9 * 1.1 * 1.05)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024 * 0.1)


class 画角闻龙(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "画角闻龙"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = int(523 * 0.95)
        self.damage_rand = int(523 * 0.1)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(205)


class 龙牙_神兵(TriggerSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "龙牙·神兵"

        self.is_cast = False
        self.is_hit = False

        self.probability = 307 / 1024

        self.damage_base = 20
        self.damage_rand = 2
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(50)


SKILLS_MAP = {
    "通用": [梅花枪法, 下马, 破, 流血],
    "羽林枪法": [穿云, 龙吟, 龙牙],
    "虎牙令": [撼如雷],
    "奔雷枪术": [突, 灭],
    "游龙骑法": [任驰骋, 断魂刺],
    "奇穴": [穿云_挫锐, 击水, 渊, 龙牙_龙血],
}
SKILLS = sum(SKILLS_MAP.values(), [])
