from base.buff import Buff


class CriticalSet(Buff):
    def __init__(self):
        super().__init__()
        self.probability = 0.1

        self.duration = 6 * 16

    def add(self):
        super().add()
        self.status.attribute.physical_critical_strike_gain += 0.04
        self.status.attribute.physical_critical_power_gain += 41 / 1024

    def remove(self):
        super().remove()
        self.status.attribute.physical_critical_strike_gain -= 0.04
        self.status.attribute.physical_critical_power_gain -= 41 / 1024


class BaiDuanCD(Buff):
    def __init__(self):
        super().__init__()
        self.name = "锻造过度"
        self.duration = 60 * 16


class BaiDuanDamageCD(Buff):
    def __init__(self):
        super().__init__()
        self.name = "炽炎·冷却"
        self.duration = 4


class WaterWeapon(Buff):
    def __init__(self):
        super().__init__()
        self.name = "水特效"

        self.duration = 6 * 16

        self.value = 0

        self.stack_max = 10

    def add(self):
        super().add()
        self.status.attribute.physical_attack_power_base += self.value

    def remove(self):
        super().remove()
        self.status.attribute.physical_attack_power_base -= self.value


class WindPendant(Buff):
    def __init__(self):
        super().__init__()
        self.name = "风特效"

        self.duration = 15 * 16

        self.value = 0

    def add(self):
        super().add()
        self.status.attribute.physical_overcome_base += self.value

    def remove(self):
        super().remove()
        self.status.attribute.physical_overcome_base -= self.value


class BeltEnchant1(Buff):
    def __init__(self):
        super().__init__()
        self.name = "大附魔腰·1%"

        self.duration = 8 * 16

    def add(self):
        super().add()
        self.status.attribute.damage_addition += 0.01

    def remove(self):
        super().remove()
        self.status.attribute.damage_addition -= 0.01


class BeltEnchant5(Buff):
    def __init__(self):
        super().__init__()
        self.name = "大附魔腰·5%"

        self.duration = 8 * 16

    def add(self):
        super().add()
        self.status.attribute.damage_addition += 0.05

    def remove(self):
        super().remove()
        self.status.attribute.damage_addition -= 0.05


class BeltEnchantCD(Buff):
    def __init__(self):
        super().__init__()
        self.name = "大附魔腰·冷却"

        self.duration = 30 * 16


class WristEnchantCD(Buff):
    def __init__(self):
        super().__init__()
        self.name = "大附魔手·冷却"

        self.duration = 10 * 16


class ShoesEnchantCD(Buff):
    def __init__(self):
        super().__init__()
        self.name = "大附魔脚·冷却"

        self.duration = 10 * 16
