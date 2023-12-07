from base.constant import *

from base.attribute import Attribute


class BingXinJue(Attribute):
    SPIRIT_TO_ATTACK_POWER = 1946 / INT_SCALE
    SPIRIT_TO_CRITICAL_STRIKE = 287 / INT_SCALE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.magical_attack_power_base += 4222

        self.grad_attrs = {
            "spirit_base": MAJOR_DELTA,
            "spunk_base": MAJOR_DELTA,
            "surplus": MINOR_DELTA,
            "strain_base": MINOR_DELTA,
            "magical_attack_power_base": MAGICAL_DELTA,
            "magical_critical_strike_base": MINOR_DELTA,
            "magical_critical_power_base": MINOR_DELTA,
            "magical_overcome_base": MINOR_DELTA
        }
        self.delta_attr = "magical_critical_strike_base"
        self.delta_grad_attrs = {
            "spirit_base": SPIRIT_TO_CRITICAL_STRIKE + self.SPIRIT_TO_CRITICAL_STRIKE,
            "magical_critical_strike_base": 1
        }

    @property
    def spirit(self):
        return self._spirit

    @spirit.setter
    def spirit(self, spirit):
        spirit = int(spirit)
        self._spirit = spirit
        self.extra_magical_attack_power = spirit * self.SPIRIT_TO_ATTACK_POWER
        self._extra_magical_critical_strike = int(spirit * self.SPIRIT_TO_CRITICAL_STRIKE)
        self.base_magical_critical_strike = (self._magical_critical_strike_base + self._extra_magical_critical_strike
                                             + spirit * SPIRIT_TO_CRITICAL_STRIKE)
