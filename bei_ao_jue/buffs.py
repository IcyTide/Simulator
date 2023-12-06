from base.buff import Buff
from general.buffs import PhysicalCriticalSet


class 朔气(PhysicalCriticalSet):
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


class 闹须弥_持续(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "闹须弥-持续"

        self.is_dot = True


class 坚壁清野_持续(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "坚壁清野-持续"

        self.is_dot = True


class 楚歌(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "楚歌"

        self.duration = 6 * 16

        self.stack_max = 3

    def remove(self):
        super().remove()
        self.status.buffs["楚歌-计数"].clear()


class 楚歌_计数(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "楚歌-计数"

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


class 见尘(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "见尘"

        self.is_dot = True


class 含风(Buff):
    related_skills = ["刀啸风吟", "坚壁清野"]

    def __init__(self, status):
        super().__init__(status)
        self.name = "含风"

        self.duration = 24 * 16

        self.stack_max = 2
        self.value1 = 0.05
        self.value2 = 51 / 1024

    def add(self):
        super().add()
        self.status.attribute.physical_critical_strike_gain += self.value1
        self.status.attribute.physical_critical_power_gain += self.value2
        for skill in self.related_skills:
            self.status.skills[skill].skill_damage_addition += self.value2

    def remove(self):
        super().remove()
        self.status.attribute.physical_critical_strike_gain -= self.value1
        self.status.attribute.physical_critical_power_gain -= self.value2
        for skill in self.related_skills:
            self.status.skills[skill].skill_damage_addition -= self.value2


class 降麒式_计数(Buff):
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


class 降麒式_持续(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降麒式-持续"

        self.is_dot = True


class 降麒式(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降麒式"

        self.duration = 15 * 16

        self.value = 205 / 1024

    def add(self):
        super().add()
        self.status.attribute.damage_addition += self.value

    def remove(self):
        super().remove()
        self.status.attribute.damage_addition -= self.value


class 沉夜重雪(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "沉夜重雪"

        self.probability = 31 / 1024

    @property
    def condition(self):
        return not self.status.stacks["沉夜重雪-冷却"]

    def add(self):
        super().add()
        self.status.skills["破釜沉舟"].recharge()
        self.status.skills["刀啸风吟"].interval_base = 0
        self.status.buffs["沉夜重雪-冷却"].trigger()

    def remove(self):
        super().remove()
        self.status.skills["刀啸风吟"].interval_base = 24


class 沉夜重雪_冷却(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "沉夜重雪-冷却"

        self.duration = 30 * 16
        self.duration_max = 30 * 16


class 背水沉舟_持续(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "背水沉舟-持续"

        self.is_dot = True

        self.stack_max = 3


BUFFS = [
    朔气, 秀明尘身, 松烟竹雾, 雪絮金屏, 闹须弥_持续, 坚壁清野_持续,
    楚歌, 楚歌_计数, 见尘, 含风, 降麒式_计数, 降麒式_就绪, 降麒式_持续, 降麒式
]
