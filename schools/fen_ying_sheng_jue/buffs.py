from base.buff import Buff, GainBuff, SnapshotBuff, DotBuff, CountBuff, CDBuff, TriggerBuff, PlacementBuff, Energy, \
    ExtendBuff
from general.buffs import 内功双会套装


class 明尊(内功双会套装):
    def __init__(self, status):
        super().__init__(status)
        self.name = "明尊"


class 日灵(Energy):
    def __init__(self, status):
        super().__init__(status)
        self.name = "日灵"

        self.stack_max = 100


class 月灵(Energy):
    def __init__(self, status):
        super().__init__(status)
        self.name = "月灵"

        self.stack_max = 100


class 暗尘(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "暗尘"

        self.duration = 3 * 16


class 赤日轮(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "赤日轮"

        self.duration = 32

        self.stack_max = 2


class 烈日(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "烈日"

        self.duration = 12 * 16


class 幽月轮(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "幽月轮"

        self.duration = 32

        self.stack_max = 2

        self.gain_group = ["幽月轮"]

    def add(self):
        super().add()
        self.status.skills["幽月轮"].skill_critical_strike += 0.05

    def remove(self):
        super().remove()
        self.status.skills["幽月轮"].skill_critical_strike -= 0.05

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.skills["幽月轮"].skill_critical_strike += 0.05 * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.skills["幽月轮"].skill_critical_strike -= 0.05 * stack


class 银月斩_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "银月斩-持续"


class 光明相(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "光明相"

        self.duration = 160

        self.stack_max = 3

        self.gain_group = [
            "净世破魔击·日", "净世破魔击·月", "生死劫·日", "生死劫·月", "诛邪镇魔-日", "诛邪镇魔-月",
            "靡业报劫", "靡业报劫·日", "靡业报劫·月"
        ]

    def add(self):
        super().add()
        for skill in self.gain_group:
            self.status.skills[skill].skill_critical_strike += 1

    def remove(self):
        super().remove()
        if not self.status.stacks[self.name]:
            for skill in self.gain_group:
                self.status.skills[skill].skill_critical_strike -= 1

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_critical_strike += 1

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_critical_strike -= 1


class 魂_日(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "魂·日"

        self.duration = 8 * 16


class 魂_月(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "魂·月"

        self.duration = 8 * 16


class 诛邪镇魔(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "诛邪镇魔"

        self.duration = 6 * 16

        self.skill_list = ()

    def add(self):
        super().add()
        self.status.buffs["魂·日"].clear()
        self.status.buffs["魂·月"].clear()
        if self.level == 1:
            self.skill_list = ("诛邪镇魔-日", "诛邪镇魔-日")
        elif self.level == 2:
            self.skill_list = ("诛邪镇魔-月", "诛邪镇魔-日")
        elif self.level == 3:
            self.skill_list = ("诛邪镇魔-月", "诛邪镇魔-月")
        elif self.level == 4:
            self.skill_list = ("诛邪镇魔-日", "诛邪镇魔-月")


class 明光_日(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "明光·日"

        self.duration = 960

        self.gain_group = ["净世破魔击·日", "生死劫·日", "悬象著明·日"]

        self.values = [0.15, 102 / 1024]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_critical_strike += self.values[0]
            self.status.skills[skill].skill_critical_power += self.values[1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_critical_strike -= self.values[0]
            self.status.skills[skill].skill_critical_power -= self.values[1]


class 明光_月(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "明光·月"

        self.duration = 960

        self.gain_group = ["净世破魔击·月", "生死劫·月", "悬象著明·月"]

        self.value = 246 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value


class 灼烧(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "灼烧"


class 日月同辉(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "日月同辉"

        self.duration = 560

        self.stack_max = 3


class 日月灵魂(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "日月灵魂"

        self.duration = 320

        self.stack_max = 5

    def add(self):
        super().add()
        if self.status.stacks[self.name] == self.stack_max:
            self.status.buffs["日月同辉"].trigger()
            self.clear()


class 靡业报劫_日(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "靡业报劫·日"


class 靡业报劫_月(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "靡业报劫·月"


class 超凡入圣(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "超凡入圣"

        self.duration = 160  # TODO: duration
        self.gain_group = [
            "净世破魔击·日", "净世破魔击·日-外功", "净世破魔击·月", "净世破魔击·月-外功", "诛邪镇魔-日", "诛邪镇魔-月"
        ]

        self.value = 205 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition -= self.value


class 用晦而明(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "用晦而明"

        self.value = 563 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.all_shield_ignore += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.all_shield_ignore -= self.value


class 诛戮(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "诛戮"

        self.duration = 20 * 16

        self.value = 102 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value


class 降灵尊(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降灵尊"

        self.duration = 12 * 16


class 悬象著明_日(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "悬象著明·日"

        self.duration = 320

        self.stack_add = 6
        self.stack_max = 6


class 悬象著明_月(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "悬象著明·月"

        self.duration = 320

        self.stack_add = 6
        self.stack_max = 6


class 日月齐光_日(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "日月齐光·日"

        self.duration = 192


class 日月齐光_月(SnapshotBuff, ExtendBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "日月齐光·月"

        self.duration = 192


class 日月齐光_净世破魔击(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "日月齐光·净世破魔击"

        self.duration = 384


class 日月齐光_生死劫(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "日月齐光·生死劫"

        self.duration = 384


class 日月齐光_悬象著明(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "日月齐光·悬象著明"

        self.duration = 384


class 日月齐光(SnapshotBuff, ExtendBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "日月齐光"

        self.duration = 10 * 16
        self.duration_add = 7 * 16

        self.stack_max = 3

        self.values = [51 / 1024, 154 / 1024, 307 / 1024]

    def add(self):
        super().add()
        self.status.buffs["日月齐光·日"].clear()
        self.status.buffs["日月齐光·月"].clear()

    def clear(self):
        if self.status.stacks["日灵"] != 100 and self.status.stacks["月灵"] != 100:
            self.status.buffs["日灵"].increase(40 * self.status.stacks[self.name] - 20)
            self.status.buffs["月灵"].increase(40 * self.status.stacks[self.name] - 20)
        super().clear()
        self.status.buffs["日月齐光·净世破魔击"].clear()
        self.status.buffs["日月齐光·生死劫"].clear()
        self.status.buffs["日月齐光·悬象著明"].clear()

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_damage_addition += self.values[stack - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_damage_addition -= self.values[stack - 1]


class 驱夷逐法(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "驱夷逐法"

        self.gain_group = [
            "净世破魔击·日", "净世破魔击·日-外功", "净世破魔击·月", "净世破魔击·月-外功", "诛邪镇魔-日", "诛邪镇魔-月"
        ]

        self.value = 512 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition -= self.value


BUFFS = [明尊, 日灵, 月灵, 暗尘, 赤日轮, 烈日, 幽月轮, 银月斩_持续, 光明相,
         魂_日, 魂_月, 诛邪镇魔, 明光_日, 明光_月, 灼烧, 日月同辉, 日月灵魂, 靡业报劫_日, 靡业报劫_月, 超凡入圣, 用晦而明, 诛戮, 降灵尊,
         悬象著明_日, 悬象著明_月, 日月齐光_日, 日月齐光_月, 日月齐光_净世破魔击, 日月齐光_生死劫, 日月齐光_悬象著明, 日月齐光, 驱夷逐法]
