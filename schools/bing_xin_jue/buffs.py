from base.buff import Buff, GainBuff, DotBuff, CountBuff, CDBuff, TriggerBuff, PlacementBuff, Energy
from general.buffs import 内功双会套装


class 嗔怒(内功双会套装):
    def __init__(self, status):
        super().__init__(status)
        self.name = "嗔怒"


class 剑舞(GainBuff, Energy):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑舞"

        self.stack_add = 2
        self.stack_max = 10

        self.value = 31 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value * stack


class 满堂(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "满堂"

        self.stack_add = 5
        self.stack_max = 5

        self.duration = 15 * 16

        self.values = [0.08, 21 / 1024]

    def add(self):
        super().add()
        self.status.attribute.magical_critical_strike_gain += self.values[0]

    def remove(self):
        super().remove()
        self.status.attribute.magical_critical_strike_gain -= self.values[0]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_critical_strike_gain += self.values[0]
        self.status.attribute.magical_critical_power_gain += self.values[1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_critical_strike_gain -= self.values[0]
        self.status.attribute.magical_critical_power_gain -= self.values[1]


class 急曲_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "急曲-持续"

        self.stack_max = 3


class 繁音急节(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "繁音急节"

        self.duration = 20 * 16

        self.value = 461 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value


class 枕上(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "枕上"

        self.duration = 16 * 15

        self.stack_max = 5

        self.value = 10 / 1024

    def add(self):
        super().add()
        self.status.attribute.haste_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.haste_gain -= self.value


class 广陵月(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "广陵月"

        self.duration = 16 * 6

    def add(self):
        super().add()
        self.status.skills["剑破虚空"].cost = False

    def remove(self):
        super().remove()
        self.status.skills["剑破虚空"].cost = True
        self.status.buffs["广陵月-会效"].clear()


class 广陵月_会效(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "广陵月-会效"

        self.duration = 16 * 6

        self.stack_max = 10

        self.value = 20 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_critical_power_gain += self.value * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_critical_power_gain -= self.value * stack


class 流玉(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流玉"

        self.duration = 16 * 5

        self.value = 512 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.skills["玳弦急曲"].skill_damage_addition += self.value
        self.status.skills["玳弦急曲-新妆"].skill_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.skills["玳弦急曲"].skill_damage_addition -= self.value
        self.status.skills["玳弦急曲-新妆"].skill_damage_addition -= self.value


class 流玉_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流玉-持续"


class 钗燕_计数(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "钗燕-计数"

        self.stack_max = 3
        self.duration = 6 * 16

        self.count_list = []

    def add(self):
        super().add()
        if self.status.stacks[self.name] == 3:
            self.status.skills["钗燕"].cast()
            self.status.skills["急曲-持续"].cast()
            self.clear()

    def clear(self):
        super().clear()
        self.count_list = []


class 盈袖(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "盈袖"

        self.duration = 20 * 16

        self.value = 204 / 1024

    def add(self):
        super().add()
        self.status.attribute.extra_haste += self.value

    def remove(self):
        super().remove()
        self.status.attribute.extra_haste -= self.value


class 化冰(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "化冰"

        self.duration = 180 * 16

        self.value = 184 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.pve_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.level = level
        self.status.attribute.pve_addition -= self.value


class 化冰_计数(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "化冰-计数"

        self.duration = 24

        self.stack_max = 3

    def add(self):
        super().add()
        if self.status.stacks[self.name] == 3:
            self.status.skills["化冰"].cast()
            self.clear()


class 夜天(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "夜天"

        self.duration = 2 * 16

        self.value = 102 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.damage_addition -= self.value


class 琼霄_持续(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "琼霄-持续"


class 琼霄_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "琼霄-冷却"

        self.duration = 20 * 16


class 凝华(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "凝华"

        self.stack_add = 3
        self.stack_max = 9

        self.duration = 20 * 16


class 霜降(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "霜降"

        self.values = [154 / 1024, 307 / 1024, 461 / 1024]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.skills["玳弦急曲"].skill_damage_addition += self.values[level - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.skills["玳弦急曲"].skill_damage_addition -= self.values[level - 1]


class 飞霜绛露(TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "飞霜绛露"

        self.probability = 25 / 1024

    def add(self):
        super().add()
        self.status.skills["剑气长江"].reset()
        self.status.buffs["飞霜绛露-冷却"].trigger()


class 飞霜绛露_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "飞霜绛露-冷却"

        self.duration = 30 * 16

class 气吞长江_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "气吞长江-持续"

        self.is_dot = True

        self.stack_max = 3


BUFFS = [嗔怒, 剑舞, 满堂, 急曲_持续, 繁音急节, 枕上, 广陵月, 广陵月_会效, 流玉, 流玉_持续,
         钗燕_计数, 盈袖, 化冰, 化冰_计数, 夜天, 琼霄_持续, 琼霄_冷却, 凝华, 霜降,
         飞霜绛露, 飞霜绛露_冷却, 气吞长江_持续]
