from base.buff import Buff
from general.buffs import CriticalSet


class ShuoQi(CriticalSet):
    def __init__(self):
        super().__init__()
        self.name = "朔气"


class XiuMingChenShen(Buff):
    def __init__(self):
        super().__init__()
        self.name = "秀明尘身"


class SongYanZhuWu(Buff):
    related_skills = ["逐鹰式"]

    def __init__(self):
        super().__init__()
        self.name = "松烟竹雾"

    def remove(self):
        super().remove()
        for skill in self.related_skills:
            self.status.skills[skill].activate = False


class XueXuJinPing(Buff):
    def __init__(self):
        super().__init__()
        self.name = "雪絮金屏"


class NaoXuMiDot(Buff):
    def __init__(self):
        super().__init__()
        self.name = "闹须弥·持续"

        self.is_dot = True


class JianBiQingYeDot(Buff):
    def __init__(self):
        super().__init__()
        self.name = "坚壁清野·持续"

        self.is_dot = True


class ChuGe(Buff):
    def __init__(self):
        super().__init__()
        self.name = "楚歌"

        self.duration = 6 * 16

        self.stack_max = 3

    def remove(self):
        super().remove()
        self.status.buffs["楚歌·计数"].clear()


class ChuGeCount(Buff):
    def __init__(self):
        super().__init__()
        self.name = "楚歌·计数"

        self.duration = 6 * 16

        self.stack_max = 5

    @property
    def condition(self):
        return self.status.stacks["楚歌"]

    def add(self):
        super().add()
        if self.status.stacks[self.name] == self.stack_max:
            for _ in range(self.status.stacks["楚歌"]):
                self.status.skills["楚歌"].cast()
            self.status.buffs["楚歌"].clear()


class JianChen(Buff):
    def __init__(self):
        super().__init__()
        self.name = "见尘"

        self.is_dot = True


class HanFeng(Buff):
    related_skills = ["刀啸风吟", "坚壁清野"]

    def __init__(self):
        super().__init__()
        self.name = "含风"

        self.duration = 24 * 16

        self.stack_max = 2

    def add(self):
        super().add()
        self.status.attribute.physical_critical_strike_gain += 0.05
        self.status.attribute.physical_critical_power_gain += 0.05
        for skill in self.related_skills:
            self.status.skills[skill].skill_damage_addition += 0.05

    def remove(self):
        super().remove()
        self.status.attribute.physical_critical_strike_gain -= 0.05
        self.status.attribute.physical_critical_power_gain -= 0.05
        for skill in self.related_skills:
            self.status.skills[skill].skill_damage_addition -= 0.05


class XiangQiCount(Buff):
    def __init__(self):
        super().__init__()
        self.name = "降麒式·计数"

        self.stack_max = 6

    def add(self):
        super().add()
        if self.status.stacks[self.name] == 6:
            self.clear()
            self.status.buffs["降麒式·就绪"].trigger()


class XiangQiReady(Buff):
    def __init__(self):
        super().__init__()
        self.name = "降麒式·就绪"

        self.duration = 15 * 16

    def add(self):
        super().add()
        self.status.skills["降麒式"].activate = True

    def remove(self):
        super().remove()
        self.status.skills["降麒式"].activate = False


class XiangQiDot(Buff):
    def __init__(self):
        super().__init__()
        self.name = "降麒式·持续"

        self.is_dot = True


class XiangQiShi(Buff):
    def __init__(self):
        super().__init__()
        self.name = "降麒式"

        self.duration = 15 * 16

    def add(self):
        super().add()
        self.status.buffs["降麒式·计数"].clear()
        self.status.buffs["降麒式·就绪"].clear()
        self.status.attribute.damage_addition += 0.2

    def remove(self):
        self.status.attribute.damage_addition -= 0.2


BUFFS = [
    ShuoQi,
    XiuMingChenShen, SongYanZhuWu, XueXuJinPing, NaoXuMiDot, JianBiQingYeDot, ChuGe, ChuGeCount,
    JianChen, HanFeng, XiangQiCount, XiangQiReady, XiangQiDot, XiangQiShi]