from base.skill import Skill

"""
    Base Skills
"""


class ShuangFengDaoFa(Skill):
    def __init__(self):
        super(ShuangFengDaoFa, self).__init__()
        self.name = "霜风刀法"

        self.gcd_index = -1

        self.base_damage_base = 1

        self.attack_power_cof_base = 16 * 10
        self.weapon_damage_cof_base = 1024


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
        self.status.buffs["秀明尘身"].refresh()
        self.status.buffs["松烟竹雾"].expire()
        self.status.buffs["雪絮金屏"].expire()


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
        self.status.buffs["秀明尘身"].expire()
        self.status.buffs["松烟竹雾"].refresh()
        self.status.buffs["雪絮金屏"].expire()


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
        self.status.buffs["秀明尘身"].expire()
        self.status.buffs["松烟竹雾"].expire()
        self.status.buffs["雪絮金屏"].refresh()


class LeiZouFengQie(Skill):
    def __init__(self):
        super(LeiZouFengQie, self).__init__()
        self.name = "雷走风切"

        self.gcd_index = 1
        self.cd_base = 18 * 16

        self.base_damage_base = 175
        self.rand_damage_base = 15
        self.attack_power_cof_base = 224 * 0.8 * 0.7

    @property
    def condition(self):
        return self.status.stacks["秀明尘身"] or self.status.stacks["松烟竹雾"]


class ShangJiangJunYin(Skill):
    def __init__(self):
        super(ShangJiangJunYin, self).__init__()
        self.name = "上将军印"

        self.cd_base = 18 * 16
        self.interval_list = [4, 6, 6, 6, 6]

        self.base_damage_base = 300
        self.rand_damage_base = 15
        self.attack_power_cof_base = 160 * 0.9 * 1.1 * 1.05
        self.weapon_damage_cof_base = 1024

    @property
    def condition(self):
        return self.status.stacks["秀明尘身"]


class PoFuChenZhou(Skill):
    def __init__(self):
        super(PoFuChenZhou, self).__init__()
        self.name = "破釜沉舟"

        self.cd_base = 9 * 16
        self.energy = 2

        self.base_damage_base = 350
        self.rand_damage_base = 20
        self.attack_power_cof_base = 400 * 0.9 * 0.95 * 1.1 * 1.15
        self.weapon_damage_cof_base = 2048
        self.surplus_cof_base = 1024 * 1024 * (0.875 - 1)

    @property
    def condition(self):
        return self.status.stacks["秀明尘身"]


class NaoXuMiDot(Skill):
    def __init__(self):
        super(NaoXuMiDot, self).__init__()
        self.name = "闹须弥-持续"

        self.is_cast = False
        self.is_dot = True
        self.is_snapshot = True

        self.count_base = 8
        self.interval_base = 48

        self.attack_power_cof_base = 280

    def post_cast(self):
        super(NaoXuMiDot, self).post_cast()
        self.set_buff()


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
        self.status.skills["闹须弥-持续"].cast()


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
        self.status.skills["惊燕式"].cast()


class JingYanShi(Skill):
    def __init__(self):
        super(JingYanShi, self).__init__()
        self.name = "惊燕式"

        self.cd_base = 10 * 16
        self.interval_list = [3, 7]

        self.base_damage_base = 80
        self.rand_damage_base = 10
        self.attack_power_cof_base = 64 * 1.3 * 1.2
        self.weapon_damage_cof_base = 1024
        self.surplus_cof_base = 1024 * 1024 * (0.275 - 1)

    def pre_cast(self):
        super(JingYanShi, self).pre_cast()
        self.status.cds["擒龙六斩"] = self.cd

    def post_damage(self):
        super(JingYanShi, self).post_damage()
        self.attack_power_cof_gain += 0.25

    def post_cast(self):
        super(JingYanShi, self).post_cast()
        self.attack_power_cof_gain = 1
        self.status.skills["逐鹰式"].activate = True


class ZhuYingShi(Skill):
    def __init__(self):
        super(ZhuYingShi, self).__init__()
        self.name = "逐鹰式"

        self.cd_base = 10 * 16
        self.interval_list = [4, 6]

        self.base_damage_base = 80
        self.rand_damage_base = 10
        self.attack_power_cof_base = 64 * 1.3 * 1.2
        self.weapon_damage_cof_base = 1024
        self.surplus_cof_base = 1024 * 1024 * (0.275 - 1)

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def pre_cast(self):
        super(ZhuYingShi, self).pre_cast()
        self.status.cds["擒龙六斩"] += self.cd

    def post_damage(self):
        super(ZhuYingShi, self).post_damage()
        self.attack_power_cof_gain += 0.5

    def post_cast(self):
        super(ZhuYingShi, self).post_cast()
        self.attack_power_cof_gain = 1


class JianBiQingYeDot(Skill):
    def __init__(self):
        super(JianBiQingYeDot, self).__init__()
        self.name = "坚壁清野-持续"

        self.is_cast = False

        self.interval_list = [16] * 10

        self.base_damage_base = 250
        self.rand_damage_base = 20
        self.attack_power_cof_base = 160 * 1.1

    def pre_cast(self):
        super(JianBiQingYeDot, self).pre_cast()
        self.set_buff()


class JianBiQingYe(Skill):
    def __init__(self):
        super(JianBiQingYe, self).__init__()
        self.name = "坚壁清野"

        self.cd_base = 30 * 16

        self.base_damage_base = 430
        self.rand_damage_base = 20
        self.attack_power_cof_base = 0

    @property
    def condition(self):
        return self.status.stacks["雪絮金屏"]

    def post_cast(self):
        super(JianBiQingYe, self).post_cast()
        self.status.skills["坚壁清野-持续"].cast()


class DaoXiaoFengYin(Skill):
    def __init__(self):
        super(DaoXiaoFengYin, self).__init__()
        self.name = "刀啸风吟"

        self.interval_base = 24

        self.base_damage_base = 250
        self.rand_damage_base = 20

        self.attack_power_cof_base = 256 * 1.2 * 1.05 * 1.1 * 1.1 * 1.05
        self.surplus_cof_base = 1024 * 1024 * (0.1375 - 1)

    @property
    def condition(self):
        return self.status.stacks["雪絮金屏"]


"""
    Talent Skills
"""


class JianChen(Skill):
    def __init__(self):
        super(JianChen, self).__init__()
        self.name = "见尘"

        self.is_cast = False

        self.interval_list = [5, 6, 6, 6, 6]

        self.base_damage_base = 300 * 0.5
        self.rand_damage_base = 15 * 0.5

        self.attack_power_cof_base = 160 * 0.9 * 1.1 * 0.7
        self.weapon_damage_cof_base = 1024 * 0.25

    def pre_cast(self):
        super(JianChen, self).pre_cast()
        self.set_buff()


class ChuGe(Skill):
    def __init__(self):
        super(ChuGe, self).__init__()
        self.name = "楚歌"

        self.is_cast = False

        self.base_damage_base = 70
        self.rand_damage_base = 5
        self.attack_power_cof_base = 1200 * 0.8


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


class JueQi(Skill):
    def __init__(self):
        super(JueQi, self).__init__()
        self.name = "绝期"

        self.is_cast = False

        self.base_damage_base = 250
        self.rand_damage_base = 20
        self.attack_power_cof_base = 120

    def post_cast(self):
        super(JueQi, self).post_cast()
        self.status.skills["闹须弥-持续"].cast()


class XiangQiDot(Skill):
    def __init__(self):
        super(XiangQiDot, self).__init__()
        self.name = "降麒式-持续"

        self.is_cast = False

        self.interval_list = [16] * 15

        self.base_damage_base = 190
        self.rand_damage_base = 15

        self.attack_power_cof_base = 60 * 2
        self.weapon_damage_cof_base = 2048

    def pre_cast(self):
        super(XiangQiDot, self).pre_cast()
        self.set_buff()


class XiangQiShi(Skill):
    def __init__(self):
        super(XiangQiShi, self).__init__()
        self.name = "降麒式"

        self.gcd_base = 0

    def post_cast(self):
        super(XiangQiShi, self).post_cast()
        self.set_buff()
        self.status.skills["降麒式-持续"].cast()


skills = [ShuangFengDaoFa(), XiuMingChenShen(), SongYanZhuWu(), XueXuJinPing(), LeiZouFengQie(), ShangJiangJunYin(),
          PoFuChenZhou(), NaoXuMiDot(), NaoXuMi(), QinLongLiuZhan(), JingYanShi(), ZhuYingShi(), JianBiQingYeDot(),
          JianBiQingYe(), DaoXiaoFengYin(), JianChen(), ChuGe(), JueQi(), XiangQiDot(), XiangQiShi()]
