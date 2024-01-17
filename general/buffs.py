from base.buff import SnapshotBuff, TriggerBuff, CDBuff


class 外功双会套装(SnapshotBuff, TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.probability = 102 / 1024

        self.duration = 6 * 16

        self.values = [0.04, 41 / 1024]

    def add(self, stack):
        super().add(stack)
        self.status.attribute.physical_critical_strike_gain += self.values[0]

    def remove(self, stack):
        super().remove(stack)
        self.status.attribute.physical_critical_strike_gain -= self.values[0]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_strike_gain += self.values[0]
        self.status.attribute.physical_critical_power_gain += self.values[1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_strike_gain -= self.values[0]
        self.status.attribute.physical_critical_power_gain -= self.values[1]


class 内功双会套装(SnapshotBuff, TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.probability = 102 / 1024

        self.duration = 6 * 16

        self.values = [0.04, 41 / 1024]

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


class 大附魔腰(SnapshotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔腰"

        self.duration = 8 * 16
        self.value = [10 / 1024, 51 / 1024]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.damage_addition += self.value[level - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.damage_addition -= self.value[level - 1]


class 大附魔腰_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔腰-冷却"

        self.duration = 30 * 16


class 大附魔腕_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔腕-冷却"

        self.duration = 10 * 16


class 大附魔脚_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔脚-冷却"

        self.duration = 10 * 16


BUFFS = [大附魔腰, 大附魔腰_冷却, 大附魔腕_冷却, 大附魔脚_冷却]
