from base.constant import PHYSICAL_ATTACK_POWER_COF, WEAPON_DAMAGE_COF, PHYSICAL_DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import PhysicalSkill, Skill

"""
    Base Skills
"""


class ShuangFengDaoFa(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "霜风刀法"

        self.gcd_index = self.name

        self.damage_base = 1

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(16)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class XiuMingChenShen(Skill):
    def __init__(self):
        super().__init__()
        self.name = "秀明尘身"

        self.is_hit = False

        self.gcd_base = 0
        self.gcd_index = self.name
        self.cd_base = 3 * 16

    @property
    def condition(self):
        return not self.status.stacks[self.name]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["秀明尘身"].trigger()
        self.status.buffs["松烟竹雾"].clear()
        self.status.buffs["雪絮金屏"].clear()


class SongYanZhuWu(Skill):
    def __init__(self):
        super().__init__()
        self.name = "松烟竹雾"

        self.is_hit = False

        self.gcd_base = 0
        self.gcd_index = self.name
        self.cd_base = 3 * 16

    @property
    def condition(self):
        return not self.status.stacks[self.name]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["秀明尘身"].clear()
        self.status.buffs["松烟竹雾"].trigger()
        self.status.buffs["雪絮金屏"].clear()


class XueXuJinPing(Skill):
    def __init__(self):
        super().__init__()
        self.name = "雪絮金屏"

        self.is_hit = False

        self.gcd_base = 0
        self.gcd_index = self.name
        self.cd_base = 3 * 16

    @property
    def condition(self):
        return not self.status.stacks[self.name]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["秀明尘身"].clear()
        self.status.buffs["松烟竹雾"].clear()
        self.status.buffs["雪絮金屏"].trigger()


class LeiZouFengQie(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "雷走风切"

        self.gcd_index = self.name
        self.cd_base = 16 * 16

        self.damage_base = 175
        self.damage_rand = 15
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(224 * 0.8 * 0.7)

    @property
    def condition(self):
        return not self.status.stacks["雪絮金屏"]


class ShangJiangJunYin(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "上将军印"

        self.cd_base = 18 * 16
        self.interval_list = [4, 6, 6, 6, 6]

        self.damage_base = 300
        self.damage_rand = 15
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(160 * 0.9 * 1.1 * 1.05)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    @property
    def condition(self):
        return self.status.stacks["秀明尘身"]


class PoFuChenZhou(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "破釜沉舟"

        self.is_overdraw = True

        self.cd_base = 9 * 16
        self.energy = 2

        self.damage_base = 350
        self.damage_rand = 20
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(400 * 0.9 * 0.95 * 1.1 * 1.15)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)

    @property
    def condition(self):
        return self.status.stacks["秀明尘身"]

    def post_cast(self):
        super().post_cast()
        self.status.skills["破釜沉舟·破招"].cast()
        if self.status.stacks["沉夜重雪"]:
            self.recharge()
            self.status.skills["背水沉舟·持续"].cast()


class PoFuChenZhouSurplus(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "破釜沉舟·破招"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 1
        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (0.875 - 1))


class NaoXuMiDot(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "闹须弥·持续"

        self.is_cast = False
        self.is_hit = False

        self.is_snapshot = True

        self.count_base = 8
        self.interval_base = 48

        self.damage_base = 1
        self.attack_power_cof = PHYSICAL_DOT_ATTACK_POWER_COF(280, self.interval_base)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["闹须弥·持续"].trigger()


class NaoXuMi(Skill):
    def __init__(self):
        super().__init__()
        self.name = "闹须弥"

        self.is_hit = False

        self.cd_base = 25 * 16

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def pre_cast(self):
        super().pre_cast()
        self.status.skills["闹须弥·持续"].cast()


class QinLongLiuZhan(Skill):
    related_skills = ["逐鹰式"]

    def __init__(self):
        super().__init__()
        self.name = "擒龙六斩"

        self.cd_base = 10 * 16

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def recharge(self):
        super().recharge()
        for skill in self.related_skills:
            self.status.skills[skill].activate = False

    def post_cast(self):
        super().post_cast()
        self.status.skills["惊燕式"].cast()


class QinLongLiuZhanSurplus(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "擒龙六斩·破招"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 1
        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (0.275 - 1))


class JingYanShi(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "惊燕式"

        self.interval_list = [3, 7]

        self.damage_base = 80
        self.damage_rand = 10
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(64 * 1.3 * 1.2)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    def post_hit(self):
        self.attack_power_cof_gain += 0.25
        super().post_hit()

    def post_cast(self):
        super().post_cast()
        self.attack_power_cof_gain -= 0.25 * self.count
        self.status.skills["擒龙六斩·破招"].cast()
        self.status.skills["逐鹰式"].activate = True


class ZhuYingShi(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "逐鹰式"

        self.activate = False

        self.interval_list = [4, 6]

        self.damage_base = 80
        self.damage_rand = 10
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(64 * 1.3 * 1.2)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    @property
    def condition(self):
        return self.status.skills['擒龙六斩'].available

    def pre_cast(self):
        super().pre_cast()
        self.status.cds["擒龙六斩"] += self.status.skills["擒龙六斩"].cd
        self.status.energies["擒龙六斩"] -= 1

    def post_hit(self):
        self.attack_power_cof_gain += 0.5
        super().post_hit()

    def post_cast(self):
        self.activate = False
        self.attack_power_cof_gain -= 0.5 * self.count
        super().post_cast()
        self.status.skills["擒龙六斩·破招"].cast()


class JianBiQingYeDot(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "坚壁清野·持续"

        self.is_cast = False

        self.interval_list = [16] * 10

        self.damage_base = 250
        self.damage_rand = 20
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(160 * 1.1)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["坚壁清野·持续"].trigger()


class JianBiQingYe(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "坚壁清野"

        self.cd_base = 30 * 16

        self.damage_base = 430
        self.damage_rand = 20
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(288 * 1.2 * 0.7 * 1.1)

    @property
    def condition(self):
        return self.status.stacks["雪絮金屏"]

    def post_cast(self):
        super().post_cast()
        self.status.skills["坚壁清野·持续"].cast()


class DaoXiaoFengYinSurplus(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "刀啸风吟·破招"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 1
        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (0.1375 - 1))


class DaoXiaoFengYin(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "刀啸风吟"

        self.interval_base = 24

        self.damage_base = 250
        self.damage_rand = 20

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(256 * 1.2 * 1.05 * 1.1 * 1.1 * 1.05)

    @property
    def condition(self):
        return self.status.stacks["雪絮金屏"]

    def post_cast(self):
        super().post_cast()
        self.status.skills["刀啸风吟·破招"].cast()


"""
    Talent Skills
"""


class JianChen(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "见尘"

        self.is_cast = False
        self.is_hit = False

        self.interval_list = [5, 6, 6, 6, 6]

        self.damage_base = int(100 * 1.45 * 0.5)
        self.damage_rand = int(10 * 1.45 * 0.5)

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(60 * 1.45 * 1.1 * 0.7)
        # self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024 * 1.45 * 0.25)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["见尘"].trigger()


class ChuGe(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "楚歌"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 55
        self.damage_rand = 5
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(1200 * 0.8)


# class LinJiang(Skill):
#     def __init__(self):
#         super().__init__()
#         self.name = "临江"
#
#         self.is_cast = False
#
#         self.damage_base = 150
#         self.damage_rand = 50 * 0.1
#         self.attack_power_cof = 40 * 1.1 * 0.8 * 1.1


class JueQi(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "绝期"

        self.is_cast = False
        self.is_hit = False

        self.probability = 306 / 1024

        self.damage_base = 250
        self.damage_rand = 20
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(120)

    def post_cast(self):
        super().post_cast()
        self.status.skills["闹须弥·持续"].cast()


class XiangQiDot(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "降麒式·持续"

        self.is_cast = False

        self.interval_list = [16] * 15

        self.damage_base = 50
        self.damage_rand = 5

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(60 * 2)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["降麒式·持续"].trigger()


class XiangQiShi(Skill):
    def __init__(self):
        super().__init__()
        self.name = "降麒式"

        self.activate = False

        self.gcd_base = 0

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["降麒式"].trigger()
        self.status.skills["降麒式·持续"].cast()


class ShangJiangJunYinDivine(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "上将军印·神兵"

        self.is_cast = False
        self.is_hit = False

        self.probability = 102 / 1024

        self.damage_base = 20
        self.damage_rand = 2
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(25)


class BeiShuiChenZhouDot(PhysicalSkill):
    def __init__(self):
        super().__init__()
        self.name = "背水沉舟·持续"

        self.is_cast = False
        self.is_hit = False

        self.is_dot = True
        self.is_snapshot = True

        self.interval_base = 3 * 16
        self.count_base = 6

        self.damage_base = 1
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(380)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["背水沉舟·持续"].trigger()


SKILLS = [ShuangFengDaoFa, XiuMingChenShen, SongYanZhuWu, XueXuJinPing, LeiZouFengQie,
          ShangJiangJunYin, PoFuChenZhou, PoFuChenZhouSurplus,
          NaoXuMiDot, NaoXuMi, QinLongLiuZhan, QinLongLiuZhanSurplus, JingYanShi, ZhuYingShi,
          JianBiQingYeDot, JianBiQingYe, DaoXiaoFengYin, DaoXiaoFengYinSurplus,
          JianChen, ChuGe, JueQi, XiangQiDot, XiangQiShi]
