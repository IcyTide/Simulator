from base.buff import GainBuff, TriggerBuff, CDBuff


class 外功双会套装(TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.probability = 102 / 1024

        self.duration = 6 * 16

        self.sub_buffs = ["外功会心套装", "外功会效套装"]


class 外功会心套装(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.value = 0.04

        self.gain_attribute = "critical_strike"
        
    def add(self):
        super().add()
        self.status.attribute.physical_critical_strike_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.physical_critical_strike_gain -= self.value

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_strike_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_strike_gain -= self.value


class 外功会效套装(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.value = 41 / 1024

        self.gain_attribute = "critical_power"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_power_gain -= self.value


class 内功双会套装(TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.probability = 102 / 1024

        self.duration = 6 * 16

        self.sub_buffs = ["内功会心套装", "内功会效套装"]


class 内功会心套装(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.value = 0.04

        self.gain_attribute = "critical_strike"

    def add(self):
        super().add()
        self.status.attribute.magical_critical_strike_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.magical_critical_strike_gain -= self.value

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_critical_strike_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_critical_strike_gain -= self.value


class 内功会效套装(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.value = 41 / 1024

        self.gain_attribute = "critical_power"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_critical_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_critical_power_gain -= self.value


class 外功风特效(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "风特效"

        self.duration = 15 * 16

        self.value = 0

        self.gain_attribute = "overcome"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_overcome_base += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_overcome_base -= self.value


class 内功风特效(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "风特效"

        self.duration = 15 * 16

        self.value = 0

        self.gain_attribute = "overcome"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_overcome_base += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_overcome_base -= self.value


class 大附魔腰(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔腰"

        self.duration = 8 * 16
        self.values = [10 / 1024, 51 / 1024]

        self.gain_attribute = "damage_addition"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.all_damage_addition += self.values[level - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.all_damage_addition -= self.values[level - 1]


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


BUFFS = {
    "外功": [外功会心套装, 外功会效套装, 外功风特效, 大附魔腰, 大附魔腰_冷却, 大附魔腕_冷却, 大附魔脚_冷却],
    "内功": [内功会心套装, 内功会效套装, 内功风特效, 大附魔腰, 大附魔腰_冷却, 大附魔腕_冷却, 大附魔脚_冷却]
}
