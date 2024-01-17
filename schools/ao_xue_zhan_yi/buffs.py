from base.buff import Buff, GainBuff, SnapshotBuff, DotBuff, CDBuff, PlacementBuff, TriggerBuff, Energy
from general.buffs import 外功双会套装


class 军啸(外功双会套装):
    def __init__(self, status):
        super().__init__(status)
        self.name = "军啸"


class 战意(Energy):
    def __init__(self, status):
        super().__init__(status)
        self.name = "战意"

        self.stack_max = 5


class 骑御(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "骑御"

    def add(self, stack):
        super().add(stack)
        self.status.buffs["驰骋"].trigger()


class 流血(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流血"

        self.stack_max = 2


class 激雷(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "激雷"

        self.duration = 6 * 16

        self.value = 0.3

    def add(self, stack):
        super().add(stack)
        self.status.attribute.physical_critical_strike_gain += self.value

    def remove(self, stack):
        super().remove(stack)
        self.status.attribute.physical_critical_strike_gain -= self.value

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_strike_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_strike_gain -= self.value


class 驰骋(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "驰骋"

        self.duration = 15 * 16

        self.value = 154 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_attack_power_gain -= self.value


class 挫锐(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "挫锐"

        self.duration = 10 * 16
        self.values = [
            (status.skills["穿云-挫锐"].attack_power_cof, status.skills["穿云-挫锐"].weapon_damage_cof, 3),
            (status.skills["穿云"].attack_power_cof, status.skills["穿云"].weapon_damage_cof, 1)
        ]

    def add(self, stack):
        super().add(stack)
        self.status.skills["穿云"].attack_power_cof = self.values[0][0]
        self.status.skills["穿云"].weapon_damage_cof = self.values[0][1]
        self.status.skills["穿云"].tick_base = self.values[0][2]

    def remove(self, stack):
        super().remove(stack)
        self.status.skills["穿云"].attack_power_cof = self.values[1][0]
        self.status.skills["穿云"].weapon_damage_cof = self.values[1][1]
        self.status.skills["穿云"].tick_base = self.values[1][2]


class 大漠(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大漠"

        self.duration = 10 * 16
        self.value = 205 / 1024

        self.gain_group = ["龙牙", "龙牙-龙血"]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition -= self.value


class 龙驭(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "龙驭"

        self.stack_max = 3

        self.value = 72 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.damage_addition += self.value * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.damage_addition -= self.value * stack


class 牧云(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "牧云"

        self.stack_max = 4
        self.duration = 60 * 16

        self.values = [0.03, 60 / 1024]

    def add(self, stack):
        super().add(stack)
        self.status.attribute.physical_critical_strike_gain += self.values[0]

    def remove(self, stack):
        super().remove(stack)
        self.status.attribute.physical_critical_strike_gain -= self.values[0]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_strike_gain += self.values[0] * stack
        self.status.attribute.physical_critical_power_gain += self.values[1] * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_strike_gain -= self.values[0] * stack
        self.status.attribute.physical_critical_power_gain -= self.values[1] * stack


class 风虎(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "风虎"

        self.values = [51 / 1024, 102 / 1024, 154 / 1024, 205 / 1024, 256 / 1024]

        self.gain_group = ["穿云", "龙吟", "龙牙", "龙牙-龙血", "灭"]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition += self.values[level - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition -= self.values[level - 1]


class 战心(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "战心"

        self.gain_group = ["流血"]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].attack_power_cof_gain += 0.2

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].attack_power_cof_gain -= 0.2


class 渊(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "渊"

        self.duration = 10 * 16

        self.value = 512 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_attack_power_gain -= self.value


class 夜征(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "夜征"

        self.value = 717 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.all_shield_ignore += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.all_shield_ignore -= self.value


class 旷野孤疆(TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "旷野孤疆"

        self.probability = 82 / 1024

    @property
    def condition(self):
        return not self.status.stacks["旷野孤疆-冷却"]

    def add(self, stack):
        super().add(stack)
        self.status.skills["龙吟"].reset()
        self.status.buffs["战意"].increase(5)
        self.status.buffs["旷野孤疆-冷却"].trigger()


class 旷野孤疆_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "旷野孤疆-冷却"

        self.duration = 30 * 16


BUFFS = [
    军啸, 战意, 骑御, 流血, 激雷, 驰骋,
    挫锐, 大漠, 龙驭, 牧云, 风虎, 战心, 渊, 夜征, 旷野孤疆, 旷野孤疆_冷却
]
