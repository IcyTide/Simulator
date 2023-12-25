from base.buff import GainBuff, TriggerBuff, CDBuff


class 外功双会套装(GainBuff, TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.probability = 102 / 1024

        self.duration = 6 * 16

        self.values = [0.04, 41 / 1024]

    def add(self):
        super().add()
        self.status.attribute.physical_critical_strike_gain += self.values[0]

    def remove(self):
        super().remove()
        self.status.attribute.physical_critical_strike_gain -= self.values[0]

    def gain(self, level, stack):
        self.level = level
        self.status.attribute.physical_critical_strike_gain += self.values[0] * stack
        self.status.attribute.physical_critical_power_gain += self.values[1] * stack

    def revoke(self, level, stack):
        self.level = level
        self.status.attribute.physical_critical_strike_gain -= self.values[0] * stack
        self.status.attribute.physical_critical_power_gain -= self.values[1] * stack


class 内功双会套装(GainBuff, TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.probability = 102 / 1024

        self.duration = 6 * 16

        self.values = [0.04, 41 / 1024]

    def add(self):
        super().add()
        self.status.attribute.magical_critical_strike_gain += self.values[0]

    def remove(self):
        super().remove()
        self.status.attribute.magical_critical_strike_gain -= self.values[0]

    def gain(self, level, stack):
        self.level = level
        self.status.attribute.magical_critical_strike_gain += self.values[0] * stack
        self.status.attribute.magical_critical_power_gain += self.values[1] * stack

    def revoke(self, level, stack):
        self.level = level
        self.status.attribute.magical_critical_strike_gain += self.values[0] * stack
        self.status.attribute.magical_critical_power_gain += self.values[1] * stack


class 大附魔腰(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔腰"

        self.duration = 8 * 16
        self.value = [10 / 1024, 51 / 1024]

    def gain(self, level, stack):
        self.status.attribute.damage_addition += self.value[level - 1]

    def revoke(self, level, stack):
        self.status.attribute.damage_addition -= self.value[level - 1]


class 大附魔腰_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔腰-冷却"

        self.duration = 30 * 16


class 大附魔手_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔手-冷却"

        self.duration = 10 * 16


class 大附魔脚_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔脚-冷却"

        self.duration = 10 * 16


BUFFS = [大附魔腰, 大附魔腰_冷却, 大附魔手_冷却, 大附魔脚_冷却]
