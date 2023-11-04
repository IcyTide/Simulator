from base.buff import Buff


class ShuoQi(Buff):
    def __init__(self):
        super(ShuoQi, self).__init__()
        self.name = "朔气"

        self.probability = 0.1

        self.duration = 6 * 16
        self.duration_max = self.duration

    def add(self):
        super(ShuoQi, self).add()
        self.status.attribute.physical_critical_strike_gain += 0.04
        self.status.attribute.physical_critical_power_gain += 0.04

    def remove(self):
        super(ShuoQi, self).remove()
        self.status.attribute.physical_critical_strike_gain -= 0.04
        self.status.attribute.physical_critical_power_gain -= 0.04


class XiuMingChenShen(Buff):
    def __init__(self):
        super(XiuMingChenShen, self).__init__()
        self.name = "秀明尘身"


class SongYanZhuWu(Buff):
    related_skills = ["逐鹰式"]

    def __init__(self):
        super(SongYanZhuWu, self).__init__()
        self.name = "松烟竹雾"

    def remove(self):
        super(SongYanZhuWu, self).remove()
        for skill in self.related_skills:
            self.status.skills[skill].activate = False


class XueXuJinPing(Buff):
    def __init__(self):
        super(XueXuJinPing, self).__init__()
        self.name = "雪絮金屏"


class NaoXuMiDot(Buff):
    def __init__(self):
        super(NaoXuMiDot, self).__init__()
        self.name = "闹须弥·持续"

        self.is_dot = True


class JianBiQingYeDot(Buff):
    def __init__(self):
        super(JianBiQingYeDot, self).__init__()
        self.name = "坚壁清野·持续"

        self.is_dot = True


class ChuGe(Buff):
    def __init__(self):
        super(ChuGe, self).__init__()
        self.name = "楚歌"

        self.duration = 6 * 16
        self.duration_max = self.duration

        self.stack_max = 3

    def remove(self):
        super(ChuGe, self).remove()
        self.status.buffs["楚歌·计数"].clear()


class ChuGeCount(Buff):
    def __init__(self):
        super(ChuGeCount, self).__init__()
        self.name = "楚歌·计数"

        self.duration = 6 * 16
        self.duration_max = self.duration

        self.stack_max = 5

    @property
    def condition(self):
        return self.status.stacks["楚歌"]

    def add(self):
        super(ChuGeCount, self).add()
        if self.status.stacks[self.name] == self.stack_max:
            for _ in range(self.status.stacks["楚歌"]):
                self.status.skills["楚歌"].cast()
            self.status.buffs["楚歌"].clear()


class JianChen(Buff):
    def __init__(self):
        super(JianChen, self).__init__()
        self.name = "见尘"

        self.is_dot = True


class HanFeng(Buff):
    related_skills = ["刀啸风吟", "坚壁清野"]

    def __init__(self):
        super(HanFeng, self).__init__()
        self.name = "含风"

        self.duration = 24 * 16
        self.duration_max = self.duration

        self.stack_max = 2

    def add(self):
        super(HanFeng, self).add()
        self.status.attribute.physical_critical_strike_gain += 0.05
        self.status.attribute.physical_critical_power_gain += 0.05
        for skill in self.related_skills:
            self.status.skills[skill].skill_damage_addition += 0.05

    def remove(self):
        super(HanFeng, self).remove()
        self.status.attribute.physical_critical_strike_gain -= 0.05
        self.status.attribute.physical_critical_power_gain -= 0.05
        for skill in self.related_skills:
            self.status.skills[skill].skill_damage_addition -= 0.05


class XiangQiCount(Buff):
    def __init__(self):
        super(XiangQiCount, self).__init__()
        self.name = "降麒式·计数"

        self.stack_max = 6

    def add(self):
        super(XiangQiCount, self).add()
        if self.status.stacks[self.name] == 6:
            self.clear()
            self.status.buffs["降麒式·就绪"].trigger()


class XiangQiReady(Buff):
    def __init__(self):
        super(XiangQiReady, self).__init__()
        self.name = "降麒式·就绪"

        self.duration = 15 * 16
        self.duration_max = self.duration

    def add(self):
        super(XiangQiReady, self).add()
        self.status.skills["降麒式"].activate = True

    def remove(self):
        super(XiangQiReady, self).remove()
        self.status.skills["降麒式"].activate = False


class XiangQiDot(Buff):
    def __init__(self):
        super(XiangQiDot, self).__init__()
        self.name = "降麒式·持续"

        self.is_dot = True


class XiangQiShi(Buff):
    def __init__(self):
        super(XiangQiShi, self).__init__()
        self.name = "降麒式"

        self.duration = 15 * 16
        self.duration_max = self.duration

    def add(self):
        super(XiangQiShi, self).add()
        self.status.buffs["降麒式·计数"].clear()
        self.status.buffs["降麒式·就绪"].clear()
        self.status.attribute.damage_addition += 0.2

    def remove(self):
        self.status.attribute.damage_addition -= 0.2


buffs = [ShuoQi(),
         XiuMingChenShen(), SongYanZhuWu(), XueXuJinPing(), NaoXuMiDot(), JianBiQingYeDot(), ChuGe(), ChuGeCount(),
         JianChen(), HanFeng(), XiangQiCount(), XiangQiReady(), XiangQiDot(), XiangQiShi()]
