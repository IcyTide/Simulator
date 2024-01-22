from base.buff import Buff, GainBuff, SnapshotBuff, DotBuff, CDBuff, PlacementBuff, TriggerBuff, Energy, ExtendBuff
from general.buffs import 外功双会套装


class 军啸(外功双会套装):
    def __init__(self, status):
        super().__init__(status)
        self.name = "军啸"


class 锐意(Energy):
    def __init__(self, status):
        super().__init__(status)
        self.name = "锐意"

        self.stack_max = 100


class 身形(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "身形"

        self.stack_max = 3
        self.duration = 160


class 识破(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "识破"

        self.duration = 30 * 16


class 破绽(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破绽"

        self.stack_max = 4
        self.duration = 30 * 16

    def add(self):
        super().add()
        self.status.skills["避实击虚"].probability = self.status.stacks[self.name] * 0.25

    def remove(self):
        super().remove()
        self.status.skills["避实击虚"].probability = self.status.stacks[self.name] * 0.25


class 流血(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流血"

        self.stack_max = 4


class 单手持刀(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "单手持刀"

    def add(self):
        super().add()
        self.status.buffs["双手持刀"].clear()


class 双手持刀(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "双手持刀"

    def add(self):
        super().add()
        self.status.buffs["单手持刀"].clear()


class 行云式_二(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "行云式·二"

        self.duration = 160


class 行云式_三(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "行云式·三"

        self.duration = 160


class 沧浪三叠_二(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "沧浪三叠·二"

        self.duration = 160


class 沧浪三叠_三(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "沧浪三叠·三"

        self.duration = 160


class 灭影追风(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "灭影追风"

        self.duration = 6 * 16

        self.value = 102 / 1024

    def add(self):
        super().add()
        self.status.buffs["灭影追风-快照"].trigger()

    def remove(self):
        super().remove()
        self.status.buffs["灭影追风-快照"].clear()

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_overcome_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_overcome_gain -= self.value


class 灭影追风_快照(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "灭影追风-快照"

        self.values = [0.1, 100 / 1024]

    def add(self):
        super().add()
        self.status.attribute.physical_critical_strike_gain += self.values[0]

    def remove(self):
        super().remove()
        self.status.attribute.physical_critical_strike_gain -= self.values[0]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_strike_gain += self.values[0]
        self.status.attribute.physical_critical_power_gain += self.values[1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_strike_gain -= self.values[0]
        self.status.attribute.physical_critical_power_gain -= self.values[1]


class 戗风(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "戗风"

        self.duration = 8 * 16
        self.value = 154 / 1024
        
        self.gain_group = ["沧浪三叠·一", "沧浪三叠·二", "沧浪三叠·三", "横云断浪", "孤锋破浪"]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition -= self.value


class 雨积(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "雨积"

        self.duration = 160
        self.value = 154 / 1024

        self.gain_group = ["行云式·一", "行云式·二", "行云式·三", "停云式"]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition -= self.value


class 镇机(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "镇机"

        self.values = [
            154 / 1024,
            307 / 1024,
            461 / 1024,
            614 / 1024,
            768 / 1024,
            922 / 1024
        ]

        self.gain_group = ["断云式"]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition += self.values[self.level - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_group:
            self.status.skills[skill].skill_damage_addition -= self.values[self.level - 1]


class 界破(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "界破"


class 长溯(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "长溯"

        self.duration = 30 * 16
        self.stack_max = 3

    def add(self):
        super().add()
        self.status.skills["孤锋破浪"].tick_base = 1 + self.status.stacks[self.name]

    def remove(self):
        super().remove()
        self.status.skills["孤锋破浪"].tick_base = 1 + self.status.stacks[self.name]


class 涤瑕(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "涤瑕"

        self.values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.skills["流血"].attack_power_cof_gain += self.values[self.level - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.skills["流血"].attack_power_cof_gain -= self.values[self.level - 1]


class 流岚(GainBuff, ExtendBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流岚"

        self.duration = 0
        self.duration_add = 20 * 16
        self.duration_max = 60 * 16
        self.value = 410 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.all_shield_ignore += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.all_shield_ignore -= self.value


class 潋风(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "潋风"

        self.duration = 6 * 16


class 截辕_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "截辕-持续"


BUFFS = [
    军啸, 锐意, 身形, 识破, 破绽, 流血, 单手持刀, 双手持刀, 行云式_二, 行云式_三, 沧浪三叠_二, 沧浪三叠_三, 灭影追风, 灭影追风_快照,
    戗风, 雨积, 镇机, 界破, 长溯, 涤瑕, 流岚, 潋风, 截辕_持续
]
