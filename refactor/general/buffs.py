from base.buff import Buff


class WaterWeapon(Buff):
    def __init__(self):
        super(WaterWeapon, self).__init__()
        self.name = "水特效"

        self.duration = 6 * 16
        self.duration_max = self.duration
        self.value = 0

        self.stack_max = 10

    def add(self):
        super(WaterWeapon, self).add()
        self.status.attribute.physical_attack_power_base += self.value

    def remove(self):
        super(WaterWeapon, self).remove()
        self.status.attribute.physical_attack_power_base -= self.value


class WindPendant(Buff):
    def __init__(self):
        super(WindPendant, self).__init__()
        self.name = "风特效"

        self.duration = 15 * 16
        self.duration_max = self.duration
        self.value = 0

    def add(self):
        super(WindPendant, self).add()
        self.status.attribute.physical_overcome_base += self.value

    def remove(self):
        super(WindPendant, self).remove()
        self.status.attribute.physical_overcome_base -= self.value

