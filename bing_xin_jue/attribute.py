from base.constant import *

from base.attribute import Attribute


class BingXinJue(Attribute):
    SPIRIT_TO_ATTACK_POWER = 1946 / INT_SCALE
    SPIRIT_TO_CRITICAL_STRIKE = 287 / INT_SCALE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.physical_attack_power_base += 4222

        self.grad_attrs = {
            "spirit_base": MAJOR_DELTA,
            "spunk_base": MAJOR_DELTA,
            "surplus": MINOR_DELTA,
            "strain_base": MINOR_DELTA,
            "magical_attack_power_base": MAGICAL_DELTA,
            "magical_critical_strike_base": MINOR_DELTA,
            "magical_critical_power_base": MINOR_DELTA,
            "magical_overcome_base": MINOR_DELTA,
            "weapon_damage_base": WEAPON_DELTA
        }
        self.delta_attr = "magical_critical_strike_base"
        self.delta_grad_attrs = {
            "spirit_base": SPIRIT_TO_CRITICAL_STRIKE,   # must bring same quantity of delta_attr
            "magical_critical_strike_base": 1
        }

    @property
    def magical_attack_power(self):
        return self._magical_attack_power

    @magical_attack_power.setter
    def magical_attack_power(self, magical_attack_power):
        self._magical_attack_power = int(magical_attack_power + self._spirit * self.SPIRIT_TO_ATTACK_POWER)

    @property
    def base_magical_critical_strike(self):
        return self._base_magical_critical_strike

    @base_magical_critical_strike.setter
    def base_magical_critical_strike(self, base_magical_critical_strike):
        base_magical_critical_strike = int(base_magical_critical_strike + self._spirit * self.SPIRIT_TO_CRITICAL_STRIKE)
        self._base_magical_critical_strike = base_magical_critical_strike
        self.magical_critical_strike_percent = base_magical_critical_strike / CRITICAL_STRIKE_SCALE
