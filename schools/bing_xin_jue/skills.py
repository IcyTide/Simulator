from base.constant import MAGICAL_ATTACK_POWER_COF, MAGICAL_DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import Melee, LoopSkill, CastingSkill, ChannelSkill, DotSkill, PlacementSkill, TriggerSkill, \
    MagicalDamage

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


class 名动四方(LoopSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "名动四方"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 16

    def post_hit(self):
        super().post_hit()
        for _ in range(2):
            self.status.buffs["剑舞"].trigger()


class 急曲_持续(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "急曲-持续"

        self.is_cast = False
        self.is_hit = False

        self.tick_base = 6
        self.interval_base = 48

        self.damage_base = 100
        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(114 * 1.1 * 0.9 * 1.1, self.interval_base)


class 江海凝光(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "江海凝光"

        self.damage_base = int(215 * 0.95 / 2.5)
        self.damage_rand = int(215 * 0.1 / 2.5)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.3 * 1.1)

    def post_cast(self):
        super().post_cast()
        self.status.skills["急曲-持续"].consume()


class 玳弦急曲(ChannelSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "玳弦急曲"

        self.hit_with_cast = True

        self.tick_base = 3
        self.interval_base = 16
        self.damage_base = 252
        self.damage_rand = int(202 * 0.1)

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(85 * 0.9 * 1.25 * 1.05)

        self.dot = True

    def post_hit(self):
        super().post_hit()
        self.status.skills["破"].cast()

    def post_cast(self):
        super().post_cast()
        if self.dot:
            self.status.skills["急曲-持续"].cast()


class 破(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 1
        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (1.2 * 0.33 * 0.33 - 1))


class 剑破虚空(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑破虚空"

        self.cd_base = 10 * 16

        self.damage_base = int(230 * 0.98 / 2 + 10)
        self.damage_rand = int(230 * 0.04 / 2 + 10)

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(220 * 1.1 * 1.1 * 1.1)

        self.cost = True

    @property
    def condition(self):
        return self.status.stacks["剑舞"] > 4

    def post_cast(self):
        super().post_cast()
        if self.cost:
            self.status.buffs["剑舞"].consume(4)
        self.status.skills["急曲-持续"].cast()
        self.status.skills["破·虚空"].cast()


class 破_虚空(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破·虚空"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 1
        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (0.55 * 0.7 - 1))


class 剑气长江(CastingSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑气长江"

        self.cd_base = 6 * 16

        self.damage_base = int(442 * 2 * 0.98 * 0.2)
        self.damage_rand = int(262 * 2 * 0.04 * 0.5)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(152 * 1.1 * 1.2 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1)


class 剑影留痕(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑影留痕"

        self.is_hit = False

        self.gcd_index = 1
        self.gcd_base = 0
        self.cd_base = 10 * 16


class 繁音急节(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "繁音急节"

        self.is_hit = False

        self.gcd_base = 0
        self.cd_base = 60 * 16

    def post_cast(self):
        super().post_cast()
        self.status.buffs["繁音急节"].trigger()


class 心鼓弦(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "心鼓弦"

        self.is_hit = False

        self.interval_base = 24

        self.cd_base = 1200 * 16


class 婆罗门(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "婆罗门"

        self.is_hit = False


"""
    Talent Skills
"""


class 玳弦急曲_新妆(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "玳弦急曲-新妆"

        self.is_cast = False

        self.damage_base = int(252 * 0.15)
        self.damage_rand = int(202 * 0.1 * 0.15)

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(85 * 0.45 * 0.9 * 1.25 * 1.05)


class 广陵月(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "广陵月"

        self.activate = False

        self.is_cast = False
        self.is_hit = False

        self.gcd_base = 0
        self.cd_base = 20 * 16

    def post_cast(self):
        super().post_cast()
        self.status.buffs["广陵月"].trigger()


class 广陵月_伤害(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "广陵月-伤害"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 20
        self.damage_rand = 17
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(16 * 1.1)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["广陵月-会效"].trigger()


class 流玉_持续(DotSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流玉-持续"

        self.is_cast = False

        self.tick_base = 4
        self.interval_base = 16

        self.damage_base = int(384 * 0.95)
        self.damage_rand = int(384 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(250)

        self.skill_shield_gain = -819 / 1024

    def post_cast(self):
        super().post_cast()
        self.status.skills["破·流玉"].cast()


class 破_流玉(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破·流玉"

        self.is_cast = False
        self.is_hit = False

        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (1.2 - 1))


class 钗燕(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "钗燕"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 133
        self.damage_rand = 10

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(100 * 1.3)

    def post_cast(self):
        super().post_cast()
        self.status.skills["钗燕·明"].cast()


class 钗燕_明(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "钗燕·明"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 70
        self.damage_rand = 5

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(300 * 1.6 * 1.8 * 0.7 * 0.95)


class 盈袖(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "盈袖"

        self.is_cast = False

        self.damage_base = 70
        self.damage_rand = 5
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF((400 + 250) * 0.25 * 0.5)


class 化冰(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "化冰"

        self.is_cast = False

        self.damage_base = 20
        self.damage_rand = int(27 * 0.1)

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(300 * 1.05 * 1.2)


class 琼霄_持续(PlacementSkill, MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "琼霄-持续"

        self.is_cast = False
        self.is_hit = False

        self.interval_list = [16] * 20

        self.damage_base = int(32 * 0.95)
        self.damage_rand = int(32 * 0.1)

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(36 * 1.1 * 1.1 * 1.2)

    def post_hit(self):
        if self.status.ticks[self.name] == 0:
            self.status.skills["急曲-持续"].cast()
        super().post_hit()
        if not self.status.stacks["琼霄-冷却"] and self.status.stacks["急曲-持续"] == 3:
            self.status.skills["琼霄-急曲"].cast()


class 琼霄_急曲(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "琼霄-急曲"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 70
        self.damage_rand = 5
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(36 * 1.1 * 1.1 * 1.2)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["琼霄-冷却"].trigger()


class 凝华(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "凝华"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = [70 + 5 * i for i in range(10)]
        self.damage_rand = 5
        self.attack_power_cof = [MAGICAL_ATTACK_POWER_COF(30 * (i + 1) * 0.7) for i in range(10)]

    def post_cast(self):
        super().post_cast()
        for _ in range(3):
            self.status.skills["凝华·明"].cast(self.level)


class 凝华_明(MagicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "凝华·明"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = [70 + 5 * i for i in range(10)]
        self.damage_rand = 5
        self.attack_power_cof = [MAGICAL_ATTACK_POWER_COF(370 * (i + 1) * 0.5 * 1.7 * 0.7 / 3) for i in range(10)]


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
    "通用": [连环双刀, 破, 剑破虚空_神兵, 气吞长江_持续],
    "猿公剑法": [急曲_持续, 玳弦急曲, 剑破虚空, 破_虚空, 剑气长江, 剑影留痕],
    "西河剑器": [名动四方, 江海凝光],
    "剑器浑脱": [繁音急节, 心鼓弦, 婆罗门],
    "奇穴": [玳弦急曲_新妆, 广陵月, 广陵月_伤害, 流玉_持续, 破_流玉, 钗燕, 钗燕_明, 盈袖, 化冰, 琼霄_持续, 琼霄_急曲,
             凝华, 凝华_明]
}
SKILLS = sum(SKILLS_MAP.values(), [])
