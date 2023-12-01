from base.constant import PHYSICAL_ATTACK_POWER_COF, MAGICAL_ATTACK_POWER_COF, WEAPON_DAMAGE_COF, \
    MAGICAL_DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import PhysicalSkill, MagicalSkill, Skill

"""
    Base Skills
"""


class LianHuanShuangDao(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "连环双刀"

        self.gcd_index = self.name

        self.damage_base = 1

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(16)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class MingDongSiFang(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "名动四方"

        self.is_cast = False
        self.is_hit = False

        self.cd_base = 16

    @property
    def condition(self):
        return self.status.stacks["剑舞"] < 10

    def post_cast(self):
        super().post_cast()
        if self.status.current_frame == 0:
            for _ in range(10):
                self.status.buffs["剑舞"].trigger()
        self.status.buffs["剑舞"].trigger()


class JiQuDot(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "急曲·持续"

        self.is_cast = False
        self.is_hit = False

        self.is_snapshot = True
        self.is_stack = True

        self.count_base = 6
        self.interval_base = 48

        self.damage_base = 1
        self.attack_power_cof = MAGICAL_DOT_ATTACK_POWER_COF(114 * 1.1 * 0.9 * 1.1, self.interval_base)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["急曲·持续"].trigger()


class JiangHaiNingGuang(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "江海凝光"

        self.damage_base = int(215 * 0.95 / 2.5)
        self.damage_rand = int(215 * 0.1 / 2.5)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(64 * 1.3 * 1.1)


class DaiXianJiQu(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "玳弦急曲"

        self.count_base = 3
        self.interval_base = 16
        self.damage_base = 252
        self.damage_rand = int(202 * 0.1)

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(85 * 0.9 * 1.25 * 1.05)

        self.ji_qu = True

    def post_cast(self):
        super().post_cast()
        if self.ji_qu:
            self.status.skills["急曲·持续"].cast()
        self.status.skills["玳弦急曲·破招"].cast()


class DaiXianJiQuSurplus(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "玳弦急曲·破招"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 1
        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (1.2 * 0.33 * 0.33 - 1))


class JianPoXuKong(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑破虚空"

        self.cd_base = 10 * 16

        self.damage_base = int(230 * 0.98 / 2 + 10)
        self.damage_rand = int(230 * 0.04 / 2 + 10)

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(220 * 1.1 * 1.1 * 1.1)

        self.jian_wu = True

    def post_cast(self):
        super().post_cast()
        if self.jian_wu:
            self.status.buffs["剑舞"].consume(4)
        self.status.skills["急曲·持续"].cast()
        self.status.skills["剑破虚空·破招"].cast()


class JianPoXuKongSurplus(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑破虚空·破招"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 1
        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (0.55 * 0.7 - 1))


class JianQiChangJiang(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑气长江"

        self.cd_base = 6 * 16

        self.damage_base = int(442 * 2 * 0.98 * 0.2)
        self.damage_rand = int(262 * 2 * 0.04 * 0.5)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(152 * 1.1 * 1.2 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1)


class JianYingLiuHen(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑影留痕"

        self.is_hit = False

        self.gcd_base = 0
        self.cd_base = 10 * 16


class FanYinJiJie(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "繁音急节"

        self.is_hit = False

        self.gcd_base = 0
        self.cd_base = 60 * 16

    def post_cast(self):
        super().post_cast()
        self.status.buffs["繁音急节"].trigger()


class XinGuXian(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "心鼓弦"

        self.is_hit = False

        self.cd_base = 1200 * 16


class PoLuoMen(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "婆罗门"

        self.is_hit = False

        self.cd_base = 20 * 16


"""
    Talent Skills
"""


class DaiXianJiQuXinZhuang(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "玳弦急曲·新妆"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = int(252 * 0.15)
        self.damage_rand = int(202 * 0.1 * 0.15)

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(85 * 0.45 * 0.9 * 1.25 * 1.05)


class GuangLingYue(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "广陵月"

        self.activate = False

        self.gcd_base = 0
        self.cd_base = 20 * 16

    def post_cast(self):
        super().post_cast()
        self.status.buffs["广陵月"].trigger()


class GuangLingYueDamage(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "广陵月·伤害"

        self.is_cast = False

        self.damage_base = 20
        self.damage_rand = 17
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(16 * 1.1)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["广陵月·会效"].trigger()


class LiuYuDot(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流玉·持续"

        self.is_cast = False
        self.is_hit = False

        self.is_snapshot = True

        self.count_base = 4
        self.interval_base = 16

        self.damage_base = int(384 * 0.95)
        self.damage_rand = int(384 * 0.1)
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(250)

        self.skill_shield_gain -= 819 / 1024

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["流玉·持续"].trigger()

    def post_cast(self):
        super().post_cast()
        self.status.skills["流玉·破招"].cast()


class LiuYuSurplus(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流玉·破招"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 1
        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (1.2 - 1))


class ChaiYai(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "钗燕"

        self.is_cast = False

        self.damage_base = 133
        self.damage_rand = 10

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(100 * 1.3)

    def post_cast(self):
        super().post_cast()
        self.status.skills["急曲·持续"].cast()
        self.status.skills["钗燕·明"].cast()


class ChaiYaiMing(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "钗燕·明"

        self.is_cast = False

        self.damage_base = 70
        self.damage_rand = 5

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(300 * 1.6 * 1.8 * 0.7 * 0.95)


class YingXiu(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "盈袖"

        self.is_cast = False

        self.damage_base = 70
        self.damage_rand = 5
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF((400 + 250) * 0.25 * 0.5)


class HuaBing(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "化冰"

        self.is_cast = False

        self.damage_base = 20
        self.damage_rand = int(27 * 0.1)

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(300 * 1.05 * 1.2)


class QiongXiaoDot(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "琼霄·持续"

        self.is_cast = False

        self.interval_list = [16] * 20

        self.damage_base = int(32 * 0.95)
        self.damage_rand = int(32 * 0.1)

        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(36 * 1.1 * 1.1 * 1.2)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["剑神无我"].trigger()

    def post_hit(self):
        super().post_hit()
        if self.status.counts[self.name] == 1:
            self.status.skills["急曲·持续"].cast()
        if not self.status.stacks["琼霄·冷却"] and self.status.stacks["急曲·持续"] == 3:
            self.status.stacks["琼霄·急曲"].cast()


class QiongXiao(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "琼霄·急曲"

        self.is_cast = False

        self.damage_base = 70
        self.damage_rand = 5
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(36 * 1.1 * 1.1 * 1.2)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["琼霄·冷却"].trigger()


class NingHua(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "凝华"

        self.is_cast = False

        self.damage_base = 115
        self.damage_rand = 5
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(30 * 0.7)

    def post_cast(self):
        super().post_cast()
        self.status.skills["凝华·明"].cast()


class NingHuaMing(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "凝华·明"

        self.is_cast = False

        self.damage_base = 115
        self.damage_rand = 5
        self.attack_power_cof = MAGICAL_ATTACK_POWER_COF(370 * 0.5 * 1.7 * 0.7)


class JianPoXuKongDivine(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑破虚空·神兵"

        self.is_cast = False
        self.is_hit = False

        self.probability = 307 / 1024

        self.damage_base = 20
        self.damage_rand = 2
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(65)


class QiTunChangJiangDot(MagicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "气吞长江·持续"

        self.is_cast = False
        self.is_hit = False

        self.is_stack = True
        self.is_snapshot = True

        self.interval_base = 3 * 16
        self.count_base = 10

        self.damage_base = 1
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(400 * 1.4)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["气吞长江·持续"].trigger()


SKILLS = [LianHuanShuangDao, MingDongSiFang, JiQuDot, JiangHaiNingGuang, DaiXianJiQu,
          DaiXianJiQuSurplus, JianPoXuKong, JianPoXuKongSurplus, JianQiChangJiang, JianYingLiuHen, FanYinJiJie,
          XinGuXian, PoLuoMen, DaiXianJiQuXinZhuang, GuangLingYue, GuangLingYueDamage, LiuYuDot, LiuYuSurplus,
          ChaiYai, ChaiYaiMing, YingXiu, HuaBing, QiongXiaoDot, QiongXiao, NingHua, NingHuaMing, JianPoXuKongDivine,
          QiTunChangJiangDot]
