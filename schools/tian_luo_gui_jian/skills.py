import random

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


class 神机回复(LoopSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "神机回复"

        self.interval_base = 16

        self.gain = 10

    def post_hit(self):
        super().post_hit()
        self.status.buffs["神机"].increase(self.gain)


class 破(MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破"

        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (0.654075 - 1))

    def post_cast(self):
        super().post_cast()
        self.status.buffs["贪破"].trigger()


class 孔雀翎(CastingSkill, MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "孔雀翎"

        self.cd_base = 18 * 16

        self.damage_base = int(366 * 0.95)
        self.damage_rand = int(366 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(130)

    @property
    def condition(self):
        return self.status.stacks["神机"] >= 20

    def post_cast(self):
        super().post_cast()
        self.status.buffs["神机"].decrease(20)


class 暴雨梨花针(ChannelSkill, ChargingSkill, MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "暴雨梨花针"

        self.is_cast = False
        self.hit_with_cast = True

        self.energy = 2
        self.cd_base = 8 * 16
        self.tick_base = 5
        self.interval_base = 8

        self.damage_base = 523
        self.damage_rand = int(523 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(30 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1 * 1.25 * 1.1)

    @property
    def condition(self):
        return self.status.stacks["神机"] >= 30

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["神机"].decrease(30)


class 蚀肌弹(CastingSkill, MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蚀肌弹"

        self.interval_base = 28

        self.damage_base = 180
        self.damage_rand = 20
        self._attack_power_cof = MAGICAL_ATTACK_POWER_COF(108 * 1.2 * 1.1 * 1.05 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1)

    @property
    def attack_power_cof(self):
        return self._attack_power_cof + MAGICAL_ATTACK_POWER_COF(self.interval_base)

    @property
    def condition(self):
        return self.status.stacks["神机"] >= 25

    def post_cast(self):
        super().post_cast()
        self.status.buffs["神机"].decrease(25)
        self.status.skills["蚀肌弹-外功"].cast()


class 蚀肌弹_外功(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蚀肌弹-外功"

        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 天女散花(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天女散花"

    @property
    def condition(self):
        return self.status.stacks["神机"] >= 25

    def post_cast(self):
        super().post_cast()
        self.status.buffs["神机"].decrease(25)
        self.status.skills["天女散花-伤害"].cast()


class 天女散花_伤害(PlacementSkill, MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天女散花-伤害"

        self.interval_list = [8]

        self.damage_base = int(131 * 0.95)
        self.damage_rand = int(131 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(115)

    def post_cast(self):
        super().post_cast()
        self.status.skills["化血"].cast()


class 化血(DotSkill, MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "化血"

        self.is_cast = False
        self.is_hit = False

        self.tick_base = 8
        self.interval_base = 48

        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(140 * 1.3 * 1.05 * 1.1, self.interval_base)


class 天绝地灭(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭"

        self.is_cast = False
        self.is_hit = False

        self.cd_base = 20 * 16

    @property
    def condition(self):
        return self.status.stacks["神机"] >= 30

    def post_cast(self):
        super().post_cast()
        self.status.buffs["神机"].decrease(30)
        if not self.status.stacks["天绝地灭-持续-一"]:
            self.status.skills["天绝地灭-持续-一"].cast()
        elif not self.status.stacks["天绝地灭-持续-二"]:
            self.status.skills["天绝地灭-持续-二"].cast()
        elif not self.status.stacks["天绝地灭-持续-三"]:
            self.status.skills["天绝地灭-持续-三"].cast()
        else:
            raise Exception("Not Enough Space")


class 天绝地灭_伤害(MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-伤害"

        self.damage_base = int(131 * 0.8)
        self.damage_rand = int(131 * 0.4)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.1)


class 天绝地灭_持续_一(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-持续-一"

        self.interval_base = 48
        self.tick_base = 5

    @property
    def tick(self):
        return self.tick_base + self.status.stacks["聚精凝神"]

    @property
    def interval(self):
        return max(40, super().interval)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs[self.name].trigger()

    def post_hit(self):
        super().post_hit()
        if not self.status.stacks["天绝地灭-冷却"]:
            self.status.buffs["天绝地灭-冷却"].trigger()
            for skill in self.status.buffs["天绝地灭-计数"].skill_list:
                self.status.skills["天绝地灭-伤害"].cast()
                self.status.skills[skill].hit()


class 天绝地灭_持续_二(天绝地灭_持续_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-持续-二"


class 天绝地灭_持续_三(天绝地灭_持续_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-持续-三"


class 千机变(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "千机变"

        self.is_cast = False
        self.is_hit = False

    @property
    def condition(self):
        return self.status.stacks["神机"] >= 30

    def post_cast(self):
        super().post_cast()
        self.status.buffs["神机"].decrease(30)
        self.status.buffs["千机变"].trigger()


class 连弩(LoopSkill, MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "连弩"

        self.interval_base = 24

        self.damage_base = [37, 50]
        self.damage_rand = [5, 10]
        self.attack_power_cof = [
            MAGICAL_ATTACK_POWER_COF(94 * 1.1 * 0.9 * 1.05),
            MAGICAL_ATTACK_POWER_COF(144 * 1.1 * 1.15 * 0.9 * 1.05)
        ]

    def pre_hit(self):
        super().pre_hit()
        if self.status.stacks["鬼斧弹药"]:
            self.level = 2
        else:
            self.level = 1

    def post_hit(self):
        super().post_hit()
        self.status.buffs["鬼斧弹药"].consume()


class 鬼斧神工(ChannelSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "鬼斧神工"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 48
        self.cd_base = 90 * 16

    @property
    def condition(self):
        return self.status.stacks["神机"] >= 20

    def post_cast(self):
        super().post_cast()
        self.status.buffs["神机"].decrease(20)
        self.status.buffs["扬威"].trigger()
        for _ in range(15):
            self.status.buffs["鬼斧弹药"].trigger()


class 暗藏杀机(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "暗藏杀机"

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = self.name
        self.cd_base = 4 * 16

    def post_cast(self):
        super().post_cast()
        if not self.status.stacks["暗藏杀机-一"]:
            self.status.buffs["暗藏杀机-一"].trigger()
        elif not self.status.stacks["暗藏杀机-二"]:
            self.status.buffs["暗藏杀机-二"].trigger()
        elif not self.status.stacks["暗藏杀机-三"]:
            self.status.buffs["暗藏杀机-三"].trigger()
        else:
            self.status.buffs["暗藏杀机-一"].trigger()


class 图穷匕见(CastingSkill, MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "图穷匕见"

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = self.name
        self.cd_base = 4 * 16

        self.damage_rand = int(527 * 0.4)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(115 * 1.09 * 1.1 * 1.1 * 1.3)

    @property
    def tick(self):
        return self.status.stacks["暗藏杀机-计数"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["暗藏杀机-一"].clear()
        self.status.buffs["暗藏杀机-二"].clear()
        self.status.buffs["暗藏杀机-三"].clear()


class 心无旁骛(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "心无旁骛"

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = self.name
        self.cd_base = 90 * 16

    def post_cast(self):
        super().post_cast()
        self.status.buffs["神机"].increase(100)
        self.status.buffs["心无旁骛"].trigger()


"""
    Talent Skills
"""


class 血影留痕_天绝地灭(MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "血影留痕-天绝地灭"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = int(23 * 0.8)
        self.damage_rand = int(23 * 0.4)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.1 * 1.2)


class 血影留痕_图穷匕见(血影留痕_天绝地灭):
    def __init__(self, status):
        super().__init__(status)
        self.name = "血影留痕-图穷匕见"


class 天风汲雨(MixedDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天风汲雨"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = int(131 * 0.8)
        self.damage_rand = int(131 * 0.4)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.1 * 1.55 * 2)


class 化血迷心(TriggerSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "化血迷心"

        self.is_cast = False
        self.is_hit = False

        self.probability = 717 / 1024

    def post_cast(self):
        super().post_cast()
        self.status.skills["化血"].consume(1)


class 诡鉴冥微(CastingSkill, ChargingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "诡鉴冥微"

        self.activate = False

        self.is_cast = False
        self.is_hit = False

        self.energy = 2
        self.gcd_index = self.name
        self.cd_base = 25 * 16

    def post_cast(self):
        super().post_cast()
        self.status.skills["天绝地灭"].reset()
        if not self.status.stacks["诡鉴冥微-一"]:
            self.status.buffs["诡鉴冥微-一"].trigger()
        elif not self.status.stacks["诡鉴冥微-二"]:
            self.status.buffs["诡鉴冥微-二"].trigger()
        else:
            self.status.buffs["诡鉴冥微-一"].trigger()


class 天绝地灭_诡鉴_一(天绝地灭_持续_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-诡鉴-一"


class 天绝地灭_诡鉴_二(天绝地灭_持续_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-诡鉴-二"


SKILLS_MAP = {
    "通用": [六合棍, 神机回复, 破],
    "乾坤一掷": [孔雀翎, 暴雨梨花针],
    "九宫飞星": [
        蚀肌弹, 蚀肌弹_外功, 天女散花, 天女散花_伤害, 化血, 天绝地灭, 天绝地灭_伤害, 天绝地灭_持续_一, 天绝地灭_持续_二, 天绝地灭_持续_三,
        千机变, 连弩, 鬼斧神工, 暗藏杀机, 图穷匕见
    ],
    "天魔无相": [心无旁骛],
    "奇穴": [血影留痕_天绝地灭, 血影留痕_图穷匕见, 天风汲雨, 化血迷心, 诡鉴冥微, 天绝地灭_诡鉴_一, 天绝地灭_诡鉴_二]
}
SKILLS = sum(SKILLS_MAP.values(), [])
