from base.buff import Buff, GainBuff, SnapshotBuff, DotBuff, CountBuff, CDBuff, TriggerBuff, PlacementBuff, Energy
from general.buffs import 内功双会套装


class 佛吼(内功双会套装):
    def __init__(self, status):
        super().__init__(status)
        self.name = "佛吼"


class 贪破(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "贪破"

        self.stack_max = 10

        self.gain_group = ["破"]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].surplus_cof_gain -= 0.03 * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].surplus_cof_gain += 0.03 * stack


class 贪破_计数(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "贪破-计数"

        self.stack_max = 4

    def add(self, stack):
        super().add(stack)
        if self.status.stacks[self.name] == self.stack_max:
            self.status.buffs["贪破"].clear()
            self.clear()


class 禅那(Energy):
    def __init__(self, status):
        super().__init__(status)
        self.name = "禅那"

        self.stack_max = 3


class 普渡(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "普渡"

        self.duration = 288
        self.stack_max = 2

        self.gain_group = [
            "普渡四方", "普渡四方-外功", "韦陀献杵", "韦陀献杵-外功", "横扫六合", "横扫六合-外功", "捕风式", "拿云式",
            "守缺式"
        ]

        self.values = [20 / 1024, 41 / 1024, 61 / 1024]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition += self.values[stack - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition -= self.values[stack - 1]


class 横扫六合_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "横扫六合-持续"


class 罗汉金身(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "罗汉金身"

        self.duration = 20 * 16

        self.value = 308 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_overcome_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_overcome_gain -= self.value


class 袈裟(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "袈裟"


class 伏魔(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "伏魔"

        self.value = 102 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.damage_addition -= self.value


class 擒龙(SnapshotBuff, PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "擒龙"

        self.value = 204 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value


class 拿云(TriggerBuff, Energy):
    def __init__(self, status):
        super().__init__(status)
        self.name = "拿云"

        self.probability = 307 / 1024

        self.stack_max = 3


class 秉心(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "秉心"

        self.stack_max = 3
        self.count_list = []

    def add(self, stack):
        super().add(stack)
        if self.status.stacks[self.name] == self.stack_max:
            self.status.buffs["拿云"].trigger()
            self.clear()

    def clear(self):
        super().clear()
        self.count_list = []


class 身意(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "身意"

        self.duration = 32

        self.values = [0.05, 52 / 1024]

    def add(self, stack):
        super().add(stack)
        self.status.attribute.magical_critical_strike_gain += self.values[0]

    def remove(self, stack):
        super().remove(stack)
        self.status.attribute.magical_critical_strike_gain -= self.values[0]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_critical_strike_gain += self.values[0]
        self.status.attribute.magical_critical_power_gain += self.values[1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_critical_strike_gain -= self.values[0]
        self.status.attribute.magical_critical_power_gain -= self.values[1]


class 千斤坠_无取(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "千斤坠·无取"

        self.duration = 144

    def add(self, stack):
        super().add(stack)
        self.status.skills["千斤坠"].activate = False
        self.status.skills["千斤坠·无取"].activate = True

    def remove(self, stack):
        super().remove(stack)
        self.status.skills["千斤坠"].activate = True
        self.status.skills["千斤坠·无取"].activate = False


class 千斤坠_无舍(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "千斤坠·无舍"

        self.duration = 144

    def add(self, stack):
        super().add(stack)
        self.status.skills["千斤坠"].activate = False
        self.status.skills["千斤坠·无舍"].activate = True

    def remove(self, stack):
        super().remove(stack)
        self.status.skills["千斤坠"].activate = True
        self.status.skills["千斤坠·无舍"].activate = False


class 纷纭_禅那(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "纷纭-禅那"


class 缩地(TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "缩地"

        self.duration = 960

        self.probability = 0.5


class 金刚怒目(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "金刚怒目"

        self.value = 308 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value


class 三生(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "三生"

        self.values = [82 / 1024, 164 / 1024, 246 / 1024]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.values[level - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.values[level - 1]


class 众嗔(GainBuff):
    def __init__(self, status):
        super().__init__(status)

        self.name = "众嗔"

        self.gain_group = ["韦陀献杵", "韦陀献杵-外功", "守缺式", "拿云式"]

        self.value = 205 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition -= self.value


class 缴械(Buff):
    def __init__(self, status):
        super().__init__(status)

        self.name = "缴械"

        self.skills = ["六合棍", "普渡四方", "韦陀献杵", "横扫六合", "罗汉金身", "擒龙诀"]

    def add(self, stack):
        super().add(stack)
        for skill in self.skills:
            self.status.skills[skill].activate = False

    def remove(self, stack):
        super().remove(stack)
        for skill in self.skills:
            self.status.skills[skill].activate = True


class 佛果_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)

        self.name = "佛果-冷却"

        self.duration = 16


class 金刚日轮(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)

        self.name = "金刚日轮"

        self.duration = 18 * 16

        self.values = [0.06, 62 / 1024]

    def add(self, stack):
        super().add(stack)
        self.status.attribute.magical_critical_strike_gain += self.values[0]

    def remove(self, stack):
        super().remove(stack)
        self.status.attribute.magical_critical_strike_gain -= self.values[0]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_critical_strike_gain += self.values[0]
        self.status.attribute.magical_critical_power_gain += self.values[1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_critical_strike_gain -= self.values[0]
        self.status.attribute.magical_critical_power_gain -= self.values[1]


class 金刚日轮_计数(CountBuff):
    def __init__(self, status):
        super().__init__(status)

        self.name = "金刚日轮-计数"

        self.stack_max = 2
        self.count_list = []

    def add(self, stack):
        super().add(stack)
        if self.status.stacks[self.name] == self.stack_max:
            self.status.skills["金刚日轮"].cast()
            self.clear()

    def clear(self):
        super().clear()
        self.count_list = []


class 六合棍意(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)

        self.name = "六合棍意"


class 桑莲妙境(TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "桑莲妙境"

        self.probability = 25 / 1024

    def add(self, stack):
        super().add(stack)
        self.status.skills["守缺式"].reset()
        self.status.buffs["桑莲妙境-冷却"].trigger()


class 桑莲妙境_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "桑莲妙境-冷却"

        self.duration = 30 * 16


BUFFS = [佛吼, 贪破, 贪破_计数, 禅那, 普渡, 横扫六合_持续, 罗汉金身, 袈裟, 伏魔, 擒龙,
         拿云, 秉心, 身意, 千斤坠_无取, 千斤坠_无舍, 纷纭_禅那, 缩地, 金刚怒目, 三生, 众嗔, 缴械, 佛果_冷却, 金刚日轮,
         金刚日轮_计数, 六合棍意]
