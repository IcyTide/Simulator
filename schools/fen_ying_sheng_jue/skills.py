from base.constant import MAGICAL_ATTACK_POWER_COF, WEAPON_DAMAGE_COF, MAGICAL_DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import *

"""
    Base Skills
"""


class 大漠刀法(Melee):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大漠刀法"

        self.gcd_index = self.name
        self.gcd_base = 24

        self.skill_damage_addition = 205 / 1024


class 破(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破"

        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (0.42 * 0.75 * 0.72 - 1))


class 赤日轮(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "赤日轮"

        self.gcd_base = 16

        self.damage_base = [135, int(135 * 1.1), int(135 * 1.2)]
        self.damage_rand = [20, int(20 * 1.1), int(20 * 1.2)]
        self.attack_power_cof = [
            MAGICAL_ATTACK_POWER_COF(77 * 1.2 * 1.1 * 1.1 * 1.1 * 1.05),
            MAGICAL_ATTACK_POWER_COF(77 * 1.2 * 1.1 * 1.1 * 1.1 * 1.05),
            MAGICAL_ATTACK_POWER_COF(96 * 1.2 * 1.1 * 1.1 * 1.1 * 1.05)
        ]

        self.gain = 20

    def pre_cast(self):
        super().pre_cast()
        if self.status.stacks["赤日轮"] == 2:
            self.level = 3
        elif self.status.stacks["赤日轮"] == 1:
            self.level = 2
        else:
            self.level = 1

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["月灵"] != 100:
            self.status.buffs["日灵"].increase(self.gain)
        self.status.skills["赤日轮-外功"].cast()
        if self.status.stacks["赤日轮"] == 2:
            self.status.buffs["赤日轮"].clear()
        else:
            self.status.buffs["赤日轮"].trigger()


class 赤日轮_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "赤日轮-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 烈日斩(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "烈日斩"

        self.gcd_base = 16
        self.cd_base = 6 * 16

        self.damage_base = int(490 * 0.95 / 3)
        self.damage_rand = int(485 * 0.1 / 3)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(141 * 1.1 * 1.1 * 1.05 * 1.05)

        self.gain = 40

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["月灵"] != 100:
            self.status.buffs["日灵"].increase(self.gain)
        self.status.skills["烈日斩-外功"].cast()
        self.status.buffs["烈日"].trigger()
        if self.status.stacks["银月斩-持续"]:
            self.status.skills["破"].cast()


class 烈日斩_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "烈日斩-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 生死劫(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "生死劫"

        self.gcd_base = 16

        self.is_cast = False
        self.is_hit = False

    @property
    def condition(self):
        return self.status.stacks["日灵"] == 100 or self.status.stacks["月灵"] == 100

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["日灵"] == 100:
            self.status.skills["生死劫·日"].cast()
        elif self.status.stacks["月灵"] == 100:
            self.status.skills["生死劫·月"].cast()


class 生死劫_日(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "生死劫·日"

        self.damage_base = 70
        self.damage_rand = 10
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.05)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["日灵"].clear()
        self.status.skills["生死劫·日-外功"].cast()
        if self.status.stacks["光明相"]:
            self.status.buffs["光明相"].consume()
            self.status.buffs["月灵"].increase(100)


class 生死劫_日_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "生死劫·日-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 生死劫_月(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "生死劫·月"

        self.damage_base = 70
        self.damage_rand = 10
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["月灵"].clear()
        self.status.skills["生死劫·月-外功"].cast()
        if self.status.stacks["光明相"]:
            self.status.buffs["光明相"].consume()
            self.status.buffs["日灵"].increase(100)


class 生死劫_月_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "生死劫·月-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 净世破魔击(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "净世破魔击"

        self.gcd_base = 16

        self.is_cast = False
        self.is_hit = False

    @property
    def condition(self):
        return self.status.stacks["日灵"] == 100 or self.status.stacks["月灵"] == 100

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["日灵"] == 100:
            self.status.skills["净世破魔击·日"].cast()
        elif self.status.stacks["月灵"] == 100:
            self.status.skills["净世破魔击·月"].cast()


class 净世破魔击_日(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "净世破魔击·日"

        self.damage_base = int(520 * 0.95 * 0.4)
        self.damage_rand = int(520 * 0.1 * 0.4)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(180 * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 * 1.1)

    def post_cast(self):
        self.status.buffs["日灵"].clear()
        self.status.skills["净世破魔击·日-外功"].cast()
        super().post_cast()
        if self.status.stacks["光明相"]:
            self.status.buffs["光明相"].consume()
            self.status.buffs["月灵"].increase(100)


class 净世破魔击_日_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "净世破魔击·日-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)


class 净世破魔击_月(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "净世破魔击·月"

        self.is_cast = False
        self.hit_with_cast = True

        self.tick_base = 3

        self.damage_base = int(262 * 2 * 0.98 / 7)
        self.damage_rand = int(262 * 2 * 0.04 / 7)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(60 * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 * 1.1)

    def post_hit(self):
        self.status.skills["净世破魔击·月-外功"].cast()
        super().post_hit()

    def post_cast(self):
        self.status.buffs["月灵"].clear()
        super().post_cast()
        if self.status.stacks["光明相"]:
            self.status.buffs["光明相"].consume()
            self.status.buffs["日灵"].increase(100)


class 净世破魔击_月_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "净世破魔击·月-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 幽月轮(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "幽月轮"

        self.gcd_base = 16

        self.damage_base = int(381 * 0.95 / 5)
        self.damage_rand = int(381 * 0.1 / 5)
        self.attack_power_cof = [
            MAGICAL_ATTACK_POWER_COF(70 * 1.2 * 1.1 * 1.1 * 1.1 * 1.05),
            MAGICAL_ATTACK_POWER_COF(70 * 1.2 * 1.1 * 1.1 * 1.1 * 1.05),
            MAGICAL_ATTACK_POWER_COF(80 * 1.2 * 1.1 * 1.1 * 1.1 * 1.05)
        ]

        self.gain = 20

    def pre_cast(self):
        super().pre_cast()
        if self.status.stacks["幽月轮"] == 2:
            self.level = 3
        elif self.status.stacks["幽月轮"] == 1:
            self.level = 2
        else:
            self.level = 1

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["日灵"] != 100:
            self.status.buffs["月灵"].increase(self.gain)
        if self.status.stacks["幽月轮"] == 2:
            self.status.buffs["幽月轮"].clear()
        else:
            self.status.buffs["幽月轮"].trigger()
        self.status.skills["幽月轮-外功"].cast()


class 幽月轮_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "幽月轮-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 银月斩(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "银月斩"

        self.gcd_base = 16
        self.cd_base = 6 * 16

        self.damage_base = int(413 * 0.95 / 4)
        self.damage_rand = int(413 * 0.1 / 4)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(128 * 1.1 * 1.1 * 1.1 * 1.05 * 1.05)

        self.gain = 40

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["日灵"] != 100:
            self.status.buffs["月灵"].increase(self.gain)
        if self.status.stacks["烈日"]:
            self.status.skills["破"].cast()
        self.status.skills["银月斩-持续"].cast()
        self.status.skills["银月斩-外功"].cast()


class 银月斩_持续(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "银月斩-持续"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 32
        self.tick_base = 6

        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(128 * 1.1 * 1.1 * 1.2 * 1.1 * 1.05, self.interval_base)


class 银月斩_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "银月斩-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 驱夜断愁(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "驱夜断愁"

        self.gcd_base = 16
        self.cd_base = 4 * 16

        self.damage_base = int(500 * 0.95 / 5 * 1.3)
        self.damage_rand = int(473 * 0.1 / 5 * 1.3)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(260 * 1.1 * 1.05 * 1.05)

        self.gain = 60

    @property
    def condition(self):
        return self.status.stacks["日月同辉"] or self.status.stacks["暗尘"]

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["日灵"] != 100 and self.status.stacks["月灵"] != 100:
            self.status.buffs["日灵"].increase(self.gain)
            self.status.buffs["月灵"].increase(self.gain)
        self.status.skills["驱夜断愁-外功"].cast()


class 驱夜断愁_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "驱夜断愁-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)


class 暗尘弥散(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "暗尘弥散"

        self.cd_base = 45 * 16

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = self.name

    def post_cast(self):
        super().post_cast()
        self.status.buffs["暗尘"].trigger()


class 光明相(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "光明相"

        self.cd_base = 95 * 16

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = self.name

    def post_cast(self):
        super().post_cast()
        self.status.buffs["光明相"].trigger()


"""
    Talent Skills
"""


class 诛邪镇魔(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "诛邪镇魔"

        self.gcd_base = 16

    @property
    def condition(self):
        return self.status.stacks["诛邪镇魔"]

    def post_cast(self):
        super().post_cast()
        for skill in self.status.buffs["诛邪镇魔"].skill_list:
            self.status.skills[skill].cast()
        self.status.buffs["诛邪镇魔"].clear()
        self.status.buffs["光明相"].consume()


class 诛邪镇魔_日(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "诛邪镇魔-日"

        self.damage_base = 209
        self.damage_rand = 240
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(225 * 1.05 * 1.1 * 1.1)


class 诛邪镇魔_月(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "诛邪镇魔-月"

        self.damage_base = 209
        self.damage_rand = 240
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(225 * 1.05 * 1.1 * 1.1)


class 洞若观火_日(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "洞若观火-日"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = int(286 * 0.95)
        self.damage_rand = int(286 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(36 * 1.1 * 1.15 * 1.1)


class 洞若观火_月(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "洞若观火-月"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = int(286 * 0.95)
        self.damage_rand = int(286 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(36 * 1.1 * 1.15 * 1.1)


class 灼烧(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "灼烧"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 32
        self.tick_base = 5

        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(230 * 1.2, self.interval_base)


class 靡业报劫(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "靡业报劫"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 70
        self.damage_rand = 10
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(160)

    def post_cast(self):
        super().post_cast()


class 靡业报劫_日(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "靡业报劫·日"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 32
        self.tick_base = 7

        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(1508, self.interval_base)

    def post_cast(self):
        super().post_cast()
        if self.level == 1:
            self.status.skills["靡业报劫·终"].cast()


class 靡业报劫_月(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "靡业报劫·月"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 32
        self.tick_base = 7

        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(1508, self.interval_base)

    def post_cast(self):
        super().post_cast()
        if self.level == 1:
            self.status.skills["靡业报劫·终"].cast()


class 靡业报劫_终(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "靡业报劫·终"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 70
        self.damage_rand = 10
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(160 * 2)


class 净体不畏_日(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "净体不畏·日"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 100
        self.damage_rand = 20
        self.attack_power_cof = [
            MAGICAL_ATTACK_POWER_COF(50 * 1.1 * 1.2 * 1.8),
            MAGICAL_ATTACK_POWER_COF(50 * 1.1 * 1.2 * 1.8 * 0.5 * 1.5),
            MAGICAL_ATTACK_POWER_COF(50 * 1.1 * 1.2 * 1.8 * 1.5),
            MAGICAL_ATTACK_POWER_COF(50 * 1.1 * 1.2 * 1.8 * 1.5 * 0.1),
        ]


class 净体不畏_月(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "净体不畏·月"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 100
        self.damage_rand = 20
        self.attack_power_cof = [
            MAGICAL_ATTACK_POWER_COF(50 * 1.1 * 1.2 * 1.8),
            MAGICAL_ATTACK_POWER_COF(50 * 1.1 * 1.2 * 1.8 * 0.5 * 1.5),
            MAGICAL_ATTACK_POWER_COF(50 * 1.1 * 1.2 * 1.8 * 1.5),
            MAGICAL_ATTACK_POWER_COF(50 * 1.1 * 1.2 * 1.8 * 1.5 * 0.1),
        ]


class 降灵尊(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降灵尊"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 70
        self.damage_rand = 10
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(50 * 1.1 * 1.2 * 1.8 * 1.5 * 1.42 * 1.5 * 0.8)


class 悬象著明(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "悬象著明"

        self.activate = False

        self.gcd_base = 16
        self.cd_base = 40 * 16

        self.is_cast = False
        self.is_hit = False

    @property
    def condition(self):
        return self.status.stacks["日灵"] == 100 or self.status.stacks["月灵"] == 100

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["日灵"] == 100:
            self.status.skills["悬象著明·日"].cast()
        elif self.status.stacks["月灵"] == 100:
            self.status.skills["悬象著明·月"].cast()


class 悬象著明_日(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "悬象著明·日"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 70
        self.damage_rand = 10
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.05)

    def post_cast(self):
        self.status.buffs["日灵"].clear()
        self.status.skills["悬象著明·日-外功"].cast()
        super().post_cast()
        self.status.buffs["悬象著明·日"].trigger()
        if self.status.stacks["光明相"]:
            self.status.buffs["光明相"].consume()
            self.status.buffs["月灵"].increase(100)


class 悬象著明_日_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "悬象著明·日-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 悬象著明_月(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "悬象著明·月"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 70
        self.damage_rand = 10
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.05)

    def post_cast(self):
        self.status.buffs["月灵"].clear()
        self.status.skills["悬象著明·月-外功"].cast()
        super().post_cast()
        self.status.buffs["悬象著明·月"].trigger()
        if self.status.stacks["光明相"]:
            self.status.buffs["光明相"].consume()
            self.status.buffs["日灵"].increase(100)


class 悬象著明_月_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "悬象著明·月-外功"

        self.is_cast = False
        self.is_hit = False

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 赤日轮_悬象(FixedInterval, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "赤日轮·悬象"

        self.interval_list = [8]

        self.damage_base = int(37 * 1.2)
        self.damage_rand = int(5 * 1.2)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(32 * 1.2 * 1.1 * 1.1 * 1.1 * 1.05)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["悬象著明·日"].consume()


class 烈日斩_悬象(FixedInterval, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "烈日斩·悬象"

        self.interval_list = [8]

        self.damage_base = int(125 * 0.95 / 3)
        self.damage_rand = int(67 * 0.1 / 3)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.1 * 1.1 * 1.05 * 1.05)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["悬象著明·日"].consume()

    def post_cast(self):
        super().post_cast()
        self.status.buffs["烈日"].trigger()
        if self.status.stacks["银月斩-持续"]:
            self.status.skills["破"].cast()


class 生死劫_日_悬象(FixedInterval, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "生死劫·日·悬象"

        self.interval_list = [8]

        self.damage_base = 70
        self.damage_rand = 10
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.05)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["悬象著明·日"].consume()


class 生死劫_月_悬象(FixedInterval, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "生死劫·月·悬象"

        self.interval_list = [8]

        self.damage_base = 70
        self.damage_rand = 10
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.05)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["悬象著明·月"].consume()


class 净世破魔击_日_悬象(FixedInterval, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "净世破魔击·日·悬象"

        self.interval_list = [8]

        self.damage_base = int(520 * 0.95 * 0.2)
        self.damage_rand = int(520 * 0.1 * 0.2)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(180 * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 * 0.7)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["悬象著明·日"].consume()

    def post_cast(self):
        super().post_cast()
        self.status.skills["净世破魔击·日-外功"].cast()


class 净世破魔击_月_悬象(FixedInterval, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "净世破魔击·月·悬象"

        self.is_cast = False
        self.hit_with_cast = True

        self.tick_base = 3

        self.interval_list = [8]

        self.damage_base = int(262 * 2 * 0.98 / 7)
        self.damage_rand = int(262 * 2 * 0.04 / 7)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(60 * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 * 0.7)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["悬象著明·月"].consume()

    def post_hit(self):
        super().post_hit()
        self.status.skills["净世破魔击·月-外功"].cast()


class 幽月轮_悬象(FixedInterval, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "幽月轮·悬象"

        self.interval_list = [8]

        self.damage_base = int(100 * 0.95 / 5)
        self.damage_rand = int(25 * 0.1 / 5)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(40 * 1.2 * 1.1 * 1.1 * 1.1 * 1.05)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["悬象著明·月"].consume()


class 银月斩_悬象(FixedInterval, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "银月斩·悬象"

        self.interval_list = [8]

        self.damage_base = int(73 * 0.95 / 4)
        self.damage_rand = int(73 * 0.1 / 4)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(40 * 1.1 * 1.1 * 1.1 * 1.05)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["悬象著明·月"].consume()

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["烈日"]:
            self.status.skills["破"].cast()
        self.status.skills["银月斩-持续"].cast()


class 驱夜断愁_神兵(TriggerSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "驱夜断愁·神兵"

        self.is_cast = False
        self.is_hit = False

        self.probability = 307 / 1024

        self.damage_base = 20
        self.damage_rand = 2
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(50)


SKILLS_MAP = {
    "通用": [大漠刀法, 破, 驱夜断愁_神兵],
    "日月净世": [
        赤日轮, 赤日轮_外功, 烈日斩, 烈日斩_外功, 幽月轮, 幽月轮_外功, 银月斩, 银月斩_持续, 银月斩_外功,
        生死劫, 生死劫_日, 生死劫_日_外功, 生死劫_月, 生死劫_月_外功,
        净世破魔击, 净世破魔击_日, 净世破魔击_日_外功, 净世破魔击_月, 净世破魔击_月_外功
    ],
    "御暗烬灭令": [驱夜断愁, 驱夜断愁_外功, 暗尘弥散],
    "幻魔妙相": [光明相],
    "奇穴": [
        诛邪镇魔, 诛邪镇魔_日, 诛邪镇魔_月, 洞若观火_日, 洞若观火_月, 靡业报劫, 靡业报劫_日, 靡业报劫_月, 靡业报劫_终,
        净体不畏_日, 净体不畏_月, 降灵尊, 悬象著明, 悬象著明_日, 悬象著明_日_外功, 悬象著明_月, 悬象著明_月_外功,
        赤日轮_悬象, 烈日斩_悬象, 幽月轮_悬象, 银月斩_悬象, 生死劫_日_悬象, 生死劫_月_悬象, 净世破魔击_日_悬象,
        净世破魔击_月_悬象
    ]
}
SKILLS = sum(SKILLS_MAP.values(), [])
