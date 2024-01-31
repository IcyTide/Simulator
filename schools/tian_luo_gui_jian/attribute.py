from base.constant import *

from base.attribute import Attribute


class TianLuoGuiJian(Attribute):
    SPUNK_TO_ATTACK_POWER = 1792 / INT_SCALE
    SPUNK_TO_CRITICAL_STRIKE = 584 / INT_SCALE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.magical_attack_power_base += 3725
        self.physical_critical_strike_base += 1279
        self.pve_addition += 41 / 1024

        self.grad_attrs = {
            "spunk_base": MAJOR_DELTA,
            "agility_base": MAJOR_DELTA,
            "surplus": MINOR_DELTA,
            "strain_base": MINOR_DELTA,
            "magical_attack_power_base": MAGICAL_DELTA,
            "physical_critical_strike_base": MINOR_DELTA,
            "physical_critical_power_base": MINOR_DELTA,
            "magical_overcome_base": MINOR_DELTA
        }
        self.delta_attr = "physical_critical_strike_base"
        self.delta_grad_attrs = {
            "agility_base": AGILITY_TO_CRITICAL_STRIKE,
            "spunk_base": self.SPUNK_TO_CRITICAL_STRIKE,
            "physical_critical_strike_base": 1
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
        self.extra_physical_critical_strike = spunk * self.SPUNK_TO_CRITICAL_STRIKE
        self.base_magical_overcome = self._magical_overcome_base + spunk * SPUNK_TO_OVERCOME
