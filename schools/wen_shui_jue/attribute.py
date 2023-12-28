from base.constant import *

from base.attribute import Attribute


class WenShuiJue(Attribute):
    AGILITY_TO_TO_ATTACK_POWER = 1638 / INT_SCALE
    AGILITY_TO_OVERCOME = 256 / INT_SCALE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.physical_attack_power_base += 3449
        self.physical_critical_strike_base += 2544

        self.pve_addition += 133 / INT_SCALE

        self.grad_attrs = {
            "agility_base": MAJOR_DELTA,
            "strength_base": MAJOR_DELTA,
            "surplus": MINOR_DELTA,
            "strain_base": MINOR_DELTA,
            "physical_attack_power_base": PHYSICAL_DELTA,
            "physical_critical_strike_base": MINOR_DELTA,
            "physical_critical_power_base": MINOR_DELTA,
            "physical_overcome_base": MINOR_DELTA,
            "weapon_damage_base": WEAPON_DELTA
        }
        self.delta_attr = "physical_critical_strike_base"
        self.delta_grad_attrs = {
            "agility_base": AGILITY_TO_CRITICAL_STRIKE,  # must bring same quantity of delta_attr
            "physical_critical_strike_base": 1
        }

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, agility):
        agility = int(agility)
        self._agility = agility
        self.extra_physical_attack_power = agility * self.AGILITY_TO_TO_ATTACK_POWER
        self.extra_physical_overcome = int(agility * self.AGILITY_TO_OVERCOME)
        self.base_physical_critical_strike = (self._physical_critical_strike_base + self._extra_physical_critical_strike
                                              + agility * AGILITY_TO_CRITICAL_STRIKE)
