from base.constant import MAGICAL_ATTACK_POWER_COF, WEAPON_DAMAGE_COF, MAGICAL_DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import *

"""
    Base Skills
"""


class 六合棍(Melee):
    def __init__(self, status):
        super().__init__(status)
        self.name = "六合棍"

        self.gcd_index = self.name
        self.gcd_base = 24

        self.skill_damage_addition = 205 / 1024


class 破(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破"

        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (0.654075 - 1))

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破"].trigger()


class 普渡四方(CastingSkill, HastedCD, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "普渡四方"

        self.cd_base = 32

        self.damage_base = int(313 * 0.5)
        self.damage_rand = 15
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(128 * 1.1 * 1.15 * 1.1 * 1.05)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破-计数"].clear()
        self.status.buffs["禅那"].increase(1)
        self.status.buffs["普渡"].trigger()
        self.status.skills["普渡四方-外功"].cast()


class 普渡四方_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "普渡四方-外功"

        self.damage_base = int(100 * 0.95)
        self.damage_rand = int(25 * 0.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 韦陀献杵(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "韦陀献杵"

        self.damage_base = [int(451 / 3 * 0.4), int(451 * 2 / 3 * 0.4), 174][-1]
        self.damage_rand = [0, 0, 10][-1]
        self.attack_power_cof = [
            MAGICAL_ATTACK_POWER_COF(48 * 1.2 * 1.15 * 1.15 * 1.35 * 0.9 * 1.15 * 1.1 * 1.05),
            MAGICAL_ATTACK_POWER_COF(96 * 1.2 * 1.15 * 1.15 * 1.35 * 0.9 * 1.15 * 1.1 * 1.05),
            MAGICAL_ATTACK_POWER_COF(144 * 1.2 * 1.15 * 1.15 * 1.35 * 0.9 * 1.15 * 1.1 * 1.05)
        ][-1]

    def condition(self):
        return self.status.stacks["禅那"] == 3

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破-计数"].clear()
        self.status.skills["破"].cast()
        self.status.skills["韦陀献杵-外功"].cast()
        self.status.skills["禅那"].clear()


class 韦陀献杵_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "韦陀献杵-外功"

        self.damage_base = int(110 * 0.95)
        self.damage_rand = int(40 * 0.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)


class 横扫六合(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "横扫六合"

        self.damage_base = 75
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(70 * 1.2 * 1.15 * 1.15 * 1.25 * 1.1)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破-计数"].clear()
        self.status.buffs["禅那"].increase(1)
        self.status.skills["横扫六合_持续"].cast()
        self.status.skills["横扫六合-外功"].cast()


class 横扫六合_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "横扫六合-外功"

        self.damage_base = int(120 * 0.95)
        self.damage_rand = int(56 * 0.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)


class 横扫六合_持续(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "横扫六合-持续"

        self.interval_base = 32
        self.tick_base = 6

        self.damage_base = 45
        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(70 * 1.2 * 1.15 * 1.15 * 1.25 * 1.1, self.interval_base)


class 摩诃无量(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "摩诃无量"

        self.cd_base = 15 * 16

        self.damage_base = 22
        self.damage_rand = 2
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(16)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破-计数"].clear()
        self.status.buffs["禅那"].increase(2)
        self.status.skills["摩诃无量-外功"].cast()


class 摩诃无量_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "摩诃无量-外功"

        self.damage_base = int(130 * 0.95)
        self.damage_rand = int(71 * 0.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 捕风式(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "捕风式"

        self.cd_base = 6 * 16

        self.damage_base = int(181 / 3)
        self.damage_rand = int(19 / 3)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(77 * 1.15 * 1.5 * 1.05)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破-计数"].trigger()
        self.status.buffs["禅那"].increase(1)


class 捉影式(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "捉影式"

        self.cd_base = 20 * 16

        self.gcd_index = self.name

        self.interval_base = 8

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破-计数"].trigger()
        self.status.buffs["禅那"].increase(1)


class 拿云式(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "拿云式"

        self.activate = False

        self.damage_base = [int(778 * 0.95 / 3 / 3), int(778 * 0.95 / 3 * 2 / 3), int(778 * 0.95 / 3)][-1]
        self.damage_rand = [int(778 * 0.1 / 3 / 3), int(778 * 0.95 / 3 * 2 / 3), int(778 * 0.95 / 3)][-1]
        self.attack_power_cof = [
            MAGICAL_ATTACK_POWER_COF(83 * 1.15 * 1.35 * 0.9 * 1.1 * 1.05),
            MAGICAL_ATTACK_POWER_COF(173 * 1.15 * 1.35 * 0.9 * 1.1 * 1.05),
            MAGICAL_ATTACK_POWER_COF(260 * 1.15 * 1.35 * 0.9 * 1.1 * 1.05)
        ][-1]

    def condition(self):
        return self.status.stacks["禅那"] == 3 and self.status.stacks["拿云"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破-计数"].trigger()
        self.status.buffs["拿云"].consume()
        self.status.skills["破"].cast()
        self.status.skills["禅那"].clear()


class 守缺式(CastingSkill, ChargingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "守缺式"

        self.cd_base = 7 * 16
        self.energy = 3

        self.damage_base = int(142)
        self.damage_rand = int(5)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(200 * 1.2 * 1.15 * 0.95 * 1.05 * 1.1)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破-计数"].trigger()
        self.status.buffs["禅那"].increase(1)


class 罗汉金身(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "罗汉金身"

        self.cd_base = 20 * 16

    def condition(self):
        return self.status.stacks["禅那"] == 3

    def post_cast(self):
        super().post_cast()
        self.status.buffs["罗汉金身"].trigger()
        self.status.buffs["禅那"].clear()


class 二业依缘(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "二业依缘"

        self.cd_base = 18 * 16

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["伏魔"]:
            self.status.buffs["伏魔"].clear()
            self.status.buffs["袈裟"].trigger()
        else:
            self.status.buffs["袈裟"].clear()
            self.status.buffs["伏魔"].trigger()


class 千斤坠(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "千斤坠"

        self.cd_base = 25 * 16

        self.damage_base = 28
        self.damage_rand = 3
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(50)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破-计数"].clear()
        self.status.buffs["禅那"].increase(1)


class 擒龙诀(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "擒龙诀"

        self.gcd_index = self.name

        self.cd_base = 60 * 16

    def post_cast(self):
        super().post_cast()
        self.status.skills["擒龙"].cast()
        self.status.buffs["禅那"].increase(3)


class 擒龙(PlacementSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "擒龙"

        self.interval_list = [24] * 10

    def post_hit(self):
        super().post_hit()
        self.status.buffs["禅那"].increase(1)


"""
    Talent Skills
"""


class 千斤坠_无取(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "千斤坠·无取"

        self.is_cast = False

        self.gcd_index = self.name

        self.damage_base = 28
        self.damage_rand = 3
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(50 * 1.5)


class 千斤坠_无舍(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "千斤坠·无舍"

        self.is_cast = False

        self.gcd_index = self.name

        self.damage_base = 28
        self.damage_rand = 3
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(50 * 1.5)


class 降魔(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降魔"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = [6, 26]
        self.attack_power_cof = [
            MAGICAL_ATTACK_POWER_COF(36 * 1.2 * 1.15 * 1.15 * 1.35 * 0.9 * 1.15 * 1.1),
            MAGICAL_ATTACK_POWER_COF(65 * 1.15 * 1.35)
        ]


class 缩地(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "缩地"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 400
        self.damage_rand = 15
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(160)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["缩地"].clear()


class 佛果(TriggerSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "佛果"

        self.probability = 719 / 1024

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 77
        self.damage_rand = 101
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(120 * 1.12 * 1.3 * 1.05)

    def condition(self):
        return not self.status.stacks["佛果-冷却"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["佛果-冷却"].trigger()


class 金刚龙爪功(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "金刚龙爪功"

        self.is_cast = False
        self.is_hit = False

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(80 * 2.5 * 1.5)


class 金刚日轮(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "金刚日轮"

        self.damage_base = 28
        self.damage_rand = 3
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(600 * 0.8)
        self.skill_shield_gain = -666 / 1024


class 六合棍意(PlacementSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "六合棍意"

        self.interval_list = [16] * 9

        self.damage_base = 75
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(80 * 1.3  * 1.15)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["缴械"].trigger()

    def post_cast(self):
        super().post_cast()
        self.status.buffs["缴械"].clear()


class 剑破虚空_神兵(TriggerSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑破虚空·神兵"

        self.is_cast = False
        self.is_hit = False

        self.probability = 307 / 1024

        self.damage_base = 20
        self.damage_rand = 2
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(65)


class 气吞长江_持续(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "气吞长江-持续"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 3 * 16
        self.tick_base = 10

        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(400 * 1.4, self.interval_base)


SKILLS_MAP = {
    "通用": [六合棍, 破],
    "罗汉棍法": [普渡四方, 普渡四方_外功, 韦陀献杵, 韦陀献杵_外功, 横扫六合, 横扫六合_外功, 横扫六合_持续],
    "龙爪功": [捕风式, 捉影式, 拿云式, 守缺式],
    "袈裟伏魔功": [罗汉金身, 二业依缘, 千斤坠],
    "达摩武诀": [擒龙诀, 擒龙],
    "奇穴": [千斤坠_无取, 千斤坠_无舍, 降魔, 缩地, 佛果, 金刚龙爪功, 金刚日轮, 六合棍意]
}
SKILLS = sum(SKILLS_MAP.values(), [])
