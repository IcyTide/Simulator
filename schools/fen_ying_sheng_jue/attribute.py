from base.constant import *

from base.attribute import Attribute


class FenYingShengJue(Attribute):
    SPUNK_TO_ATTACK_POWER = 1946 / INT_SCALE
    SPUNK_TO_CRITICAL_STRIKE = 297 / INT_SCALE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.magical_attack_power_base += 4346
        self.pve_addition += 143 / 1024

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
            "spirit_base": SPIRIT_TO_CRITICAL_STRIKE,
            "spunk_base": self.SPUNK_TO_CRITICAL_STRIKE,
            "magical_critical_strike_base": 1
        }

    @property
    def spunk(self):
        return self._spunk

    @spunk.setter
    def spunk(self, spunk):
        spunk = int(spunk)
        self._spunk = spunk
        self._extra_magical_attack_power = int(spunk * self.SPUNK_TO_ATTACK_POWER)
        self.base_magical_attack_power = self._magical_attack_power_base + spunk * SPUNK_TO_ATTACK_POWER
        self.extra_magical_critical_strike = spunk * self.SPUNK_TO_CRITICAL_STRIKE
        self.base_magical_overcome = self._magical_overcome_base + spunk * SPUNK_TO_OVERCOME
