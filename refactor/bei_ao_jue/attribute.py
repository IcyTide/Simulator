from functools import cached_property

from base.constant import *

from base.attribute import Attribute, Target


class BeiAoJue(Attribute):
    def __init__(self, *args, **kwargs):
        super(BeiAoJue, self).__init__(*args, **kwargs)
        self.all_major_base += 41
        self.physical_attack_power_base += 3725
        self.pve_addition += 0.09

        # self.grad_attrs = ['strength_base', 'surplus_base', 'strain_base', 'physical_attack_power_base',
        #                    'physical_critical_strike_base', 'physical_critical_power_base',
        #                    'physical_overcome_base', 'weapon_damage_base']

    @property
    def physical_attack_power(self):
        return self._physical_attack_power

    @physical_attack_power.setter
    def physical_attack_power(self, physical_attack_power):
        self._physical_attack_power = physical_attack_power + self._strength * 1.55

    @property
    def final_physical_overcome(self):
        return self._final_physical_overcome

    @final_physical_overcome.setter
    def final_physical_overcome(self, final_physical_overcome):
        self._final_physical_overcome = final_physical_overcome + self._strength * 0.36
        self.physical_overcome = self._final_physical_overcome / OVERCOME_SCALE


def get_attribute():
    return BeiAoJue(Target(), _strength_base=10156, _weapon_damage_base=3245, _weapon_damage_rand=5408 - 3245,
                    surplus_base=7648, _strain_base=35289, _haste_base=883, _physical_attack_power_base=25548,
                    _physical_critical_strike_base=20877, _physical_critical_power_base=2340,
                    _physical_overcome_base=35046)
