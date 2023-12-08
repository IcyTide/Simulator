from base.buff import Buff


class 外功双会套装(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.probability = 102 / 1024

        self.duration = 6 * 16

        self.value1 = 0.04
        self.value2 = 41 / 1024

    def add(self):
        super().add()
        self.status.attribute.physical_critical_strike_gain += self.value1
        self.status.attribute.physical_critical_power_gain += self.value2

    def remove(self):
        super().remove()
        self.status.attribute.physical_critical_strike_gain -= self.value1
        self.status.attribute.physical_critical_power_gain -= self.value2


class 内功双会套装(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.probability = 102 / 1024

        self.duration = 6 * 16

        self.value1 = 0.04
        self.value2 = 41 / 1024

    def add(self):
        super().add()
        self.status.attribute.magical_critical_strike_gain += self.value1
        self.status.attribute.magical_critical_power_gain += self.value2

    def remove(self):
        super().remove()
        self.status.attribute.magical_critical_strike_gain -= self.value1
        self.status.attribute.magical_critical_power_gain -= self.value2


class 大附魔腰(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔腰"

        self.duration = 8 * 16
        self.level_params = {
            "value": [10 / 1024, 51 / 1024]
        }
        self.value = 10 / 1024

    def add(self):
        super().add()
        self.status.attribute.damage_addition += self.value

    def remove(self):
        super().remove()
        self.status.attribute.damage_addition -= self.value


class 大附魔腰_冷却(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔腰-冷却"

        self.duration = 30 * 16


class 大附魔手_冷却(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔手-冷却"

        self.duration = 10 * 16


class 大附魔脚_冷却(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "大附魔脚-冷却"

        self.duration = 10 * 16


BUFFS = [大附魔腰, 大附魔腰_冷却, 大附魔手_冷却, 大附魔脚_冷却]
