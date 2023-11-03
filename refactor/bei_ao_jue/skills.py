from base.constant import ATTACK_POWER_COF, WEAPON_DAMAGE_COF, DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import PhysicalSkill, Skill

"""
    Base Skills
"""


class ShuangFengDaoFa(PhysicalSkill):
    def __init__(self):
        super(ShuangFengDaoFa, self).__init__()
        self.name = "霜风刀法"

        self.gcd_index = -1

        self.base_damage_base = 1

        self.attack_power_cof_base = ATTACK_POWER_COF(16)
        self.weapon_damage_cof_base = WEAPON_DAMAGE_COF(1024)


class XiuMingChenShen(Skill):
    def __init__(self):
        super(XiuMingChenShen, self).__init__()
        self.name = "秀明尘身"
        self.gcd_base = 0
        self.gcd_index = -2
        self.cd_base = 3 * 16

    @property
    def condition(self):
        return not self.status.stacks[self.name]

    def post_cast(self):
        super(XiuMingChenShen, self).post_cast()
        self.status.buffs["秀明尘身"].trigger()
        self.status.buffs["松烟竹雾"].clear()
        self.status.buffs["雪絮金屏"].clear()


class SongYanZhuWu(Skill):
    def __init__(self):
        super(SongYanZhuWu, self).__init__()
        self.name = "松烟竹雾"
        self.gcd_base = 0
        self.gcd_index = -2
        self.cd_base = 3 * 16

    @property
    def condition(self):
        return not self.status.stacks[self.name]

    def post_cast(self):
        super(SongYanZhuWu, self).post_cast()
        self.status.buffs["秀明尘身"].clear()
        self.status.buffs["松烟竹雾"].trigger()
        self.status.buffs["雪絮金屏"].clear()


class XueXuJinPing(Skill):
    def __init__(self):
        super(XueXuJinPing, self).__init__()
        self.name = "雪絮金屏"
        self.gcd_base = 0
        self.gcd_index = -2
        self.cd_base = 3 * 16

    @property
    def condition(self):
        return not self.status.stacks[self.name]

    def post_cast(self):
        super(XueXuJinPing, self).post_cast()
        self.status.buffs["秀明尘身"].clear()
        self.status.buffs["松烟竹雾"].clear()
        self.status.buffs["雪絮金屏"].trigger()


class LeiZouFengQie(PhysicalSkill):
    def __init__(self):
        super(LeiZouFengQie, self).__init__()
        self.name = "雷走风切"

        self.gcd_index = 1
        self.cd_base = 16 * 16

        self.base_damage_base = 175
        self.rand_damage_base = 15
        self.attack_power_cof_base = ATTACK_POWER_COF(224 * 0.8 * 0.7)

    @property
    def condition(self):
        return self.status.stacks["秀明尘身"] or self.status.stacks["松烟竹雾"]


class ShangJiangJunYin(PhysicalSkill):
    def __init__(self):
        super(ShangJiangJunYin, self).__init__()
        self.name = "上将军印"

        self.cd_base = 18 * 16
        self.interval_list = [4, 6, 6, 6, 6]

        self.base_damage_base = 300
        self.rand_damage_base = 15
        self.attack_power_cof_base = ATTACK_POWER_COF(160*0.9*1.1*1.05)
        self.weapon_damage_cof_base = WEAPON_DAMAGE_COF(1024)

    @property
    def condition(self):
        return self.status.stacks["秀明尘身"]


class PoFuChenZhou(PhysicalSkill):
    def __init__(self):
        super(PoFuChenZhou, self).__init__()
        self.name = "破釜沉舟"

        self.cd_base = 9 * 16
        self.energy = 2

        self.base_damage_base = 350
        self.rand_damage_base = 20
        self.attack_power_cof_base = ATTACK_POWER_COF(400 * 0.9 * 0.95 * 1.1 * 1.15)
        self.weapon_damage_cof_base = WEAPON_DAMAGE_COF(2048)

    @property
    def condition(self):
        return self.status.stacks["秀明尘身"]

    def post_cast(self):
        super(PoFuChenZhou, self).post_cast()
        self.status.skills["破釜沉舟·破招"].cast()


class PoFuChenZhouSurplus(PhysicalSkill):
    def __init__(self):
        super(PoFuChenZhouSurplus, self).__init__()
        self.name = "破釜沉舟·破招"

        self.is_cast = False

        self.base_damage_base = 1
        self.surplus_cof_base = SURPLUS_COF(1024 * 1024 * (0.875 - 1))


class NaoXuMiDot(PhysicalSkill):
    def __init__(self):
        super(NaoXuMiDot, self).__init__()
        self.name = "闹须弥·持续"

        self.is_cast = False
        self.is_snapshot = True

        self.count_base = 8
        self.interval_base = 48

        self.base_damage_base = 1
        self.attack_power_cof_base = DOT_ATTACK_POWER_COF(280, self.interval_base)

    def pre_cast(self):
        super(NaoXuMiDot, self).pre_cast()
        self.status.buffs["闹须弥·持续"].trigger()


class NaoXuMi(Skill):
    def __init__(self):
        super(NaoXuMi, self).__init__()
        self.name = "闹须弥"

        self.cd_base = 25 * 16

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def pre_cast(self):
        super(NaoXuMi, self).pre_cast()
        self.status.skills["闹须弥·持续"].cast()


class QinLongLiuZhan(Skill):
    def __init__(self):
        super(QinLongLiuZhan, self).__init__()
        self.name = "擒龙六斩"

        self.gcd_base = 0

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def post_cast(self):
        super(QinLongLiuZhan, self).post_cast()
        self.status.cds["擒龙六斩"] = 0
        self.status.skills["惊燕式"].cast()


class QinLongLiuZhanSurplus(PhysicalSkill):
    def __init__(self):
        super(QinLongLiuZhanSurplus, self).__init__()
        self.name = "擒龙六斩·破招"

        self.is_cast = False

        self.base_damage_base = 1
        self.surplus_cof_base = SURPLUS_COF(1024 * 1024 * (0.275 - 1))


class JingYanShi(PhysicalSkill):
    def __init__(self):
        super(JingYanShi, self).__init__()
        self.name = "惊燕式"

        self.cd_base = 10 * 16
        self.interval_list = [3, 7]

        self.base_damage_base = 80
        self.rand_damage_base = 10
        self.attack_power_cof_base = ATTACK_POWER_COF(64 * 1.3 * 1.2)
        self.weapon_damage_cof_base = WEAPON_DAMAGE_COF(1024)

    def pre_cast(self):
        super(JingYanShi, self).pre_cast()
        self.status.cds["擒龙六斩"] += self.cd

    def post_hit(self):
        self.attack_power_cof_gain += 0.25
        super(JingYanShi, self).post_hit()

    def post_cast(self):
        self.attack_power_cof_gain -= 0.25 * self.count
        super(JingYanShi, self).post_cast()
        self.status.skills["擒龙六斩·破招"].cast()
        self.status.skills["逐鹰式"].activate = True


class ZhuYingShi(PhysicalSkill):
    def __init__(self):
        super(ZhuYingShi, self).__init__()
        self.name = "逐鹰式"

        self.activate = False

        self.cd_base = 10 * 16
        self.interval_list = [4, 6]

        self.base_damage_base = 80
        self.rand_damage_base = 10
        self.attack_power_cof_base = ATTACK_POWER_COF(64 * 1.3 * 1.2)
        self.weapon_damage_cof_base = WEAPON_DAMAGE_COF(1024)

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def pre_cast(self):
        super(ZhuYingShi, self).pre_cast()
        self.status.cds["擒龙六斩"] += self.cd

    def post_hit(self):
        self.attack_power_cof_gain += 0.5
        super(ZhuYingShi, self).post_hit()

    def post_cast(self):
        self.activate = False
        self.attack_power_cof_gain -= 0.5 * self.count
        super(ZhuYingShi, self).post_cast()
        self.status.skills["擒龙六斩·破招"].cast()


class JianBiQingYeDot(PhysicalSkill):
    def __init__(self):
        super(JianBiQingYeDot, self).__init__()
        self.name = "坚壁清野·持续"

        self.is_cast = False

        self.interval_list = [16] * 10

        self.base_damage_base = 250
        self.rand_damage_base = 20
        self.attack_power_cof_base = ATTACK_POWER_COF(160 * 1.1)

    def pre_cast(self):
        super(JianBiQingYeDot, self).pre_cast()
        self.status.buffs["坚壁清野·持续"].trigger()


class JianBiQingYe(PhysicalSkill):
    def __init__(self):
        super(JianBiQingYe, self).__init__()
        self.name = "坚壁清野"

        self.cd_base = 30 * 16

        self.base_damage_base = 430
        self.rand_damage_base = 20
        self.attack_power_cof_base = ATTACK_POWER_COF(288 * 1.2 * 0.7 * 1.1)

    @property
    def condition(self):
        return self.status.stacks["雪絮金屏"]

    def post_cast(self):
        super(JianBiQingYe, self).post_cast()
        self.status.skills["坚壁清野·持续"].cast()


class DaoXiaoFengYinSurplus(PhysicalSkill):
    def __init__(self):
        super(DaoXiaoFengYinSurplus, self).__init__()
        self.name = "刀啸风吟·破招"

        self.is_cast = False

        self.base_damage_base = 1
        self.surplus_cof_base = SURPLUS_COF(1024 * 1024 * (0.1375 - 1))


class DaoXiaoFengYin(PhysicalSkill):
    def __init__(self):
        super(DaoXiaoFengYin, self).__init__()
        self.name = "刀啸风吟"

        self.interval_base = 24

        self.base_damage_base = 250
        self.rand_damage_base = 20

        self.attack_power_cof_base = ATTACK_POWER_COF(256 * 1.2 * 1.05 * 1.1 * 1.1 * 1.05)

    @property
    def condition(self):
        return self.status.stacks["雪絮金屏"]

    def post_cast(self):
        super(DaoXiaoFengYin, self).post_cast()
        self.status.skills["刀啸风吟·破招"].cast()


"""
    Talent Skills
"""


class JianChen(PhysicalSkill):
    def __init__(self):
        super(JianChen, self).__init__()
        self.name = "见尘"

        self.is_cast = False

        self.interval_list = [5, 6, 6, 6, 6]

        self.base_damage_base = 100 * 1.45 * 0.5
        self.rand_damage_base = 10 * 1.45 * 0.5

        self.attack_power_cof_base = ATTACK_POWER_COF(60 * 1.45 * 1.1 * 0.7)
        self.weapon_damage_cof_base = WEAPON_DAMAGE_COF(1024 * 1.45 * 0.25)

    def pre_cast(self):
        super(JianChen, self).pre_cast()
        self.status.buffs["见尘"].trigger()


class ChuGe(PhysicalSkill):
    def __init__(self):
        super(ChuGe, self).__init__()
        self.name = "楚歌"

        self.is_cast = False

        self.base_damage_base = 55
        self.rand_damage_base = 5
        self.attack_power_cof_base = ATTACK_POWER_COF(1200 * 0.8)


# class LinJiang(Skill):
#     def __init__(self):
#         super(LinJiang, self).__init__()
#         self.name = "临江"
#
#         self.is_cast = False
#
#         self.base_damage_base = 150
#         self.rand_damage_base = 50 * 0.1
#         self.attack_power_cof_base = 40 * 1.1 * 0.8 * 1.1


class JueQi(PhysicalSkill):
    def __init__(self):
        super(JueQi, self).__init__()
        self.name = "绝期"

        self.is_cast = False

        self.probability = 0.3

        self.base_damage_base = 250
        self.rand_damage_base = 20
        self.attack_power_cof_base = ATTACK_POWER_COF(120)

    def post_cast(self):
        super(JueQi, self).post_cast()
        self.status.skills["闹须弥·持续"].cast()


class XiangQiDot(PhysicalSkill):
    def __init__(self):
        super(XiangQiDot, self).__init__()
        self.name = "降麒式·持续"

        self.is_cast = False

        self.interval_list = [16] * 15

        self.base_damage_base = 50
        self.rand_damage_base = 5

        self.attack_power_cof_base = ATTACK_POWER_COF(60 * 2)
        self.weapon_damage_cof_base = WEAPON_DAMAGE_COF(1024)

    def pre_cast(self):
        super(XiangQiDot, self).pre_cast()
        self.status.buffs["降麒式·持续"].trigger()


class XiangQiShi(Skill):
    def __init__(self):
        super(XiangQiShi, self).__init__()
        self.name = "降麒式"

        self.activate = False

        self.gcd_base = 0

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def post_cast(self):
        super(XiangQiShi, self).post_cast()
        self.status.buffs["降麒式"].trigger()
        self.status.skills["降麒式·持续"].cast()


class ShangJiangJunYinDivine(PhysicalSkill):
    def __init__(self):
        super(ShangJiangJunYinDivine, self).__init__()
        self.name = "上将军印·神兵"

        self.is_cast = False

        self.probability = 0.1

        self.base_damage_base = 20
        self.rand_damage_base = 2
        self.attack_power_cof_base = ATTACK_POWER_COF(25)


skills = [ShuangFengDaoFa(), XiuMingChenShen(), SongYanZhuWu(), XueXuJinPing(), LeiZouFengQie(),
          ShangJiangJunYin(), PoFuChenZhou(), PoFuChenZhouSurplus(),
          NaoXuMiDot(), NaoXuMi(), QinLongLiuZhan(), QinLongLiuZhanSurplus(), JingYanShi(), ZhuYingShi(),
          JianBiQingYeDot(), JianBiQingYe(), DaoXiaoFengYin(), DaoXiaoFengYinSurplus(),
          JianChen(), ChuGe(), JueQi(), XiangQiDot(), XiangQiShi()]
