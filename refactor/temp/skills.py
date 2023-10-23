from base.skill import Skill


"""
    Base Skills
"""


class XiuMingChenShen(Skill):
    def __init__(self):
        self.name = "秀明尘身"
        self.gcd_index = -1
        self.cd_base = 3

    @property
    def condition(self):
        return not self.status.stacks[self]

    def post_cast(self):
        super(XiuMingChenShen, self).post_cast()
        self.status.buffs["秀明尘身"].refresh()
        self.status.buffs["松烟竹雾"].expire()
        self.status.buffs["雪絮金屏"].expire()


class SongYanZhuWu(Skill):
    def __init__(self):
        super(SongYanZhuWu, self).__init__()
        self.name = "松烟竹雾"
        self.gcd_index = -2
        self.cd_base = 3

    @property
    def condition(self):
        return not self.status.stacks[self]

    def post_cast(self):
        super(SongYanZhuWu, self).post_cast()
        self.status.buffs["秀明尘身"].expire()
        self.status.buffs["松烟竹雾"].refresh()
        self.status.buffs["雪絮金屏"].expire()


class XueXuJinPing(Skill):
    def __init__(self):
        super(XueXuJinPing, self).__init__()
        self.name = "雪絮金屏"
        self.gcd_index = -3
        self.cd_base = 3

    @property
    def condition(self):
        return not self.status.stacks[self]

    def post_cast(self):
        super(XueXuJinPing, self).post_cast()
        self.status.buffs["秀明尘身"].expire()
        self.status.buffs["松烟竹雾"].expire()
        self.status.buffs["雪絮金屏"].refresh()


class ShangJiangJunYin(Skill):
    def __init__(self):
        self.name = "上将军印"
        self.cd_base = 18
        self.gcd_base = 8

        self.interval_list = [1, 2, 3, 4, 5]

        self.base_damage = 0
        self.attack_power_cof_base = 0
        self.weapon_damage_cof = 1

    @property
    def condition(self):
        return not self.status.stacks[self.status.buffs["秀明尘身"]]


class PoFuChenZhou(Skill):
    def __init__(self):
        super(PoFuChenZhou, self).__init__()
        self.name = "破釜沉舟"

        self.cd_base = 9

        self.base_damage = 0
        self.attack_power_cof_base = 0
        self.weapon_damage_cof = 2
        self.surplus_cof = 0

    @property
    def condition(self):
        return not self.status.stacks[self.status.buffs["秀明尘身"]]


class NaoXuMiDot(Skill):
    def __init__(self):
        self.name = "闹须弥-持续"

        self.is_cast = False
        self.is_snapshot = True

        self.count_base = 8
        self.interval_base = 48

        self.base_damage = 0
        self.attack_power_cof_base = 0

    def post_cast(self):
        super(NaoXuMiDot, self).post_cast()
        self.set_dot()


class NaoXuMi(Skill):
    def __init__(self):
        self.name = "闹须弥"

        self.cd_base = 25

        self.base_damage = 0
        self.attack_power_cof_base = 0
        self.weapon_damage_cof = 2

    @property
    def condition(self):
        return not self.status.stacks[self.status.buffs["松烟竹雾"]]

    def post_cast(self):
        super(NaoXuMi, self).post_cast()
        self.status.skills["闹须弥-持续"].cast()


class QinLongLiuZhan(Skill):
    def __init__(self):
        self.name = "擒龙六斩"

        self.is_cast = False

    @property
    def condition(self):
        return not self.status.stacks[self.status.buffs["松烟竹雾"]]

    def post_cast(self):
        super(QinLongLiuZhan, self).post_cast()
        self.status.skills["惊燕式"].cast()


class JingYanShi1(Skill):
    def __init__(self):
        super(JingYanShi1, self).__init__()
        self.name = "惊燕式-1"

        self.is_cast = False

        self.base_damage = 0
        self.attack_power_cof_base = 0
        self.weapon_damage_cof = 0


class JingYanShi2(Skill):
    def __init__(self):
        super(JingYanShi2, self).__init__()
        self.name = "惊燕式-2"

        self.is_cast = False

        self.base_damage = 0
        self.attack_power_cof_base = 0
        self.weapon_damage_cof = 0


class JingYanShi(Skill):
    sub_skills = ["惊燕式-1", "惊燕式-2"]

    def __init__(self):
        super(JingYanShi, self).__init__()
        self.name = "惊燕式"

        self.cd_base = 10
        self.interval_base = 24

        self.surplus_cof = 0

    @property
    def condition(self):
        return not self.status.stacks[self.status.buffs["松烟竹雾"]]

    def pre_cast(self):
        super(JingYanShi, self).pre_cast()
        self.status.cds["擒龙六斩"] += self.cd

    def post_cast(self):
        super(JingYanShi, self).post_cast()
        for skill in self.sub_skills:
            self.status.skills[skill].cast()
        self.status.skills["逐鹰式"].activate = True


class ZhuYingShi1(Skill):
    def __init__(self):
        super(ZhuYingShi1, self).__init__()
        self.name = "逐鹰式-1"

        self.is_cast = False

        self.base_damage = 0
        self.attack_power_cof_base = 0
        self.weapon_damage_cof = 0


class ZhuYingShi2(Skill):
    def __init__(self):
        super(ZhuYingShi2, self).__init__()
        self.name = "逐鹰式-1"

        self.is_cast = False

        self.base_damage = 0
        self.attack_power_cof_base = 0
        self.weapon_damage_cof = 0


class ZhuYingShi(Skill):
    sub_skills = ["逐鹰式-1", "逐鹰式-2"]

    def __init__(self):
        super(ZhuYingShi, self).__init__()
        self.name = "逐鹰式"

        self.cd_base = 10
        self.interval_base = 24

        self.surplus_cof = 0

    @property
    def condition(self):
        return not self.status.stacks[self.status.buffs["松烟竹雾"]]

    def pre_cast(self):
        super(ZhuYingShi, self).pre_cast()
        self.status.cds["擒龙六斩"] += self.cd

    def post_cast(self):
        super(ZhuYingShi, self).post_cast()
        for skill in self.sub_skills:
            self.status.skills[skill].cast()


class JianBiQingYeDot(Skill):
    def __init__(self):
        super(JianBiQingYeDot, self).__init__()
        self.name = "坚壁清野-持续"

        self.is_cast = False

        self.count_base = 10
        self.interval_base = 16

        self.base_damage = 0
        self.attack_power_cof_base = 0

    def post_cast(self):
        super(JianBiQingYeDot, self).post_cast()
        self.set_dot()


class JianBiQingYe(Skill):
    def __init__(self):
        super(JianBiQingYe, self).__init__()
        self.name = "坚壁清野"

        self.cd_base = 30

        self.base_damage = 0
        self.attack_power_cof_base = 0

    @property
    def condition(self):
        return not self.status.stacks[self.status.buffs["雪絮金屏"]]

    def post_cast(self):
        super(JianBiQingYe, self).post_cast()
        self.status.skills["坚壁清野-持续"].cast()


class DaoXiaoFengYin(Skill):
    def __init__(self):
        super(DaoXiaoFengYin, self).__init__()
        self.name = "刀啸风吟"

        self.interval_base = 24

        self.base_damage = 0
        self.attack_power_cof_base = 0

    @property
    def condition(self):
        return not self.status.stacks[self.status.buffs["雪絮金屏"]]


"""
    Talent Skills
"""


class JianChen(Skill):
    def __init__(self):
        super(JianChen, self).__init__()
        self.name = "见尘"

        self.is_cast = False

        self.interval_list = [1, 2, 3, 4, 5]

        self.base_damage = 0
        self.attack_power_cof_base = 0


class ChuGe(Skill):
    def __init__(self):
        super(ChuGe, self).__init__()
        self.name = "楚歌"

        self.is_cast = False

        self.base_damage = 0
        self.attack_power_cof_base = 0
        self.pve_addition_gain = 4


class JueQi(Skill):
    def __init__(self):
        super(JueQi, self).__init__()
        self.name = "绝期"

        self.is_cast = False

        self.base_damage = 0
        self.attack_power_cof_base = 0

    def post_cast(self):
        super(JueQi, self).post_cast()
        self.status.skills["闹须弥-持续"].cast()


class XiangQiDot(Skill):
    def __init__(self):
        super(XiangQiDot, self).__init__()
        self.name = "降麒式-持续"

        self.is_cast = False

        self.count_base = 10
        self.interval_base = 16


class XiangQiShi(Skill):
    def __init__(self):
        super(XiangQiShi, self).__init__()
        self.name = "降麒式"

        self.gcd_base = 0

    def post_cast(self):
        super(XiangQiShi, self).post_cast()
        self.status.buffs["降麒式"].refresh()
