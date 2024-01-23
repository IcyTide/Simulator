from base.buff import Buff, GainBuff, SnapshotBuff, DotBuff, CountBuff, CDBuff, PlacementBuff, TriggerBuff
from general.buffs import 外功双会套装


class 朔气(外功双会套装):
    def __init__(self, status):
        super().__init__(status)
        self.name = "朔气"


class 秀明尘身(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "秀明尘身"


class 松烟竹雾(Buff):
    related_skills = ["逐鹰式"]

    def __init__(self, status):
        super().__init__(status)
        self.name = "松烟竹雾"

    def remove(self):
        super().remove()
        for skill in self.related_skills:
            self.status.skills[skill].activate = False


class 雪絮金屏(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "雪絮金屏"


class 闹须弥_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "闹须弥-持续"


class 坚壁清野_持续(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "坚壁清野-持续"


class 冥鼓(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "冥鼓"

        self.value = 410 / 1024

        self.gain_group = ["破"]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_shield_gain -= self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_shield_gain += self.value


class 霜天(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "霜天"

        self.duration = 16

        self.stack_max = 7
        self.value = 0.15

        self.gain_group = ["上将军印"]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.skills["上将军印"].damage_gain += self.value * stack
        self.status.skills["上将军印"].attack_power_cof_gain += self.value * stack
        self.status.skills["上将军印"].weapon_damage_cof_gain += self.value * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.skills["上将军印"].damage_gain -= self.value * stack
        self.status.skills["上将军印"].attack_power_cof_gain -= self.value * stack
        self.status.skills["上将军印"].weapon_damage_cof_gain -= self.value * stack


class 楚歌(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "楚歌"

        self.duration = 6 * 16

        self.stack_max = 3

    def remove(self):
        super().remove()
        self.status.buffs["楚歌-计数"].clear()


class 楚歌_计数(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "楚歌-计数"

        self.duration = 6 * 16

        self.stack_max = 5

    def add(self):
        super().add()
        if self.status.stacks[self.name] == self.stack_max:
            for _ in range(self.status.stacks["楚歌"]):
                self.status.skills["楚歌"].cast()
            self.status.buffs["楚歌"].clear()


class 见尘(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "见尘"


class 含风(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "含风"

        self.duration = 24 * 16

        self.stack_max = 2
        self.values = [0.05, 51 / 1024, 51 / 1024]

    def add(self):
        super().add()
        self.status.attribute.physical_critical_strike_gain += self.values[0]

    def remove(self):
        super().remove()
        self.status.attribute.physical_critical_strike_gain -= self.values[0]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_strike_gain += self.values[0] * stack
        self.status.attribute.physical_critical_power_gain += self.values[1] * stack
        self.status.skills["刀啸风吟"].skill_damage_addition += self.values[2] * stack
        self.status.skills["坚壁清野"].skill_damage_addition += self.values[2] * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_strike_gain -= self.values[0] * stack
        self.status.attribute.physical_critical_power_gain -= self.values[1] * stack
        self.status.skills["刀啸风吟"].skill_damage_addition -= self.values[2] * stack
        self.status.skills["坚壁清野"].skill_damage_addition -= self.values[2] * stack


class 降麒式_计数(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降麒式-计数"

        self.stack_max = 6

    def add(self):
        super().add()
        if self.status.stacks[self.name] == 6:
            self.clear()
            self.status.buffs["降麒式-就绪"].trigger()


class 降麒式_就绪(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降麒式-就绪"

        self.duration = 15 * 16

    def add(self):
        super().add()
        self.status.skills["降麒式"].activate = True

    def remove(self):
        super().remove()
        self.status.skills["降麒式"].activate = False


class 降麒式_持续(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降麒式-持续"


class 降麒式(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降麒式"

        self.duration = 15 * 16

        self.value = 205 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.damage_addition -= self.value


class 沉夜重雪(TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "沉夜重雪"

        self.probability = 31 / 1024

    def add(self):
        super().add()
        self.status.skills["破釜沉舟"].reset()
        self.status.skills["刀啸风吟"].direct = True
        self.status.buffs["沉夜重雪-冷却"].trigger()

    def remove(self):
        super().remove()
        self.status.skills["刀啸风吟"].direct = False


class 沉夜重雪_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "沉夜重雪-冷却"

        self.duration = 30 * 16


class 背水沉舟_持续(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "背水沉舟-持续"

        self.is_dot = True

        self.stack_max = 3


BUFFS = [
    朔气, 秀明尘身, 松烟竹雾, 雪絮金屏, 闹须弥_持续, 坚壁清野_持续,
    冥鼓, 霜天, 楚歌, 楚歌_计数, 见尘, 含风, 降麒式_计数, 降麒式_就绪, 降麒式_持续, 降麒式,
    沉夜重雪, 沉夜重雪_冷却, 背水沉舟_持续
]
