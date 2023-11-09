from functools import cached_property

from base.constant import *

from base.attribute import Attribute, Target


class BeiAoJue(Attribute):
    STRENGTH_TO_ATTACK_POWER = 1587 / INT_SCALE
    STRENGTH_TO_OVERCOME = 369 / INT_SCALE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.physical_attack_power_base += 3725
        self.pve_addition += 0.09
        self.grad_attrs = ['strength_base', 'surplus', 'strain_base', 'physical_attack_power_base',
                           'physical_critical_power_base', 'physical_overcome_base', 'weapon_damage_base']

    @property
    def physical_attack_power(self):
        return self._physical_attack_power

    @physical_attack_power.setter
    def physical_attack_power(self, physical_attack_power):
        self._physical_attack_power = physical_attack_power + self._strength * self.STRENGTH_TO_ATTACK_POWER

    @property
    def final_physical_overcome(self):
        return self._final_physical_overcome

    @final_physical_overcome.setter
    def final_physical_overcome(self, final_physical_overcome):
        self._final_physical_overcome = final_physical_overcome + self._strength * self.STRENGTH_TO_OVERCOME
        self.physical_overcome = self._final_physical_overcome / OVERCOME_SCALE


def get_attribute():
    attribute = BeiAoJue()
    attrs = {'weapon_damage_base': 3245, 'weapon_damage_rand': 2163, 'strength_base': 10635,
             'physical_attack_power_base': 19809, 'physical_critical_strike_base': 20036,
             'all_critical_strike_base': 1363,
             'physical_critical_power_base': 2340, 'physical_overcome_base': 28752, 'strain_base': 35426,
             'haste_base': 883,
             'surplus': 7785}
    for k, v in attrs.items():
        setattr(attribute, k, getattr(attribute, k) + v)
    return attribute
