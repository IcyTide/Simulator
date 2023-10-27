import torch

from base.attribute import Attribute, Target


class BeiAoJue(Attribute):
    def __init__(self, *args, **kwargs):
        super(BeiAoJue, self).__init__(*args, **kwargs)
        self.pve_addition = 0.09

        # self.grad_attrs = ['strength_base', 'surplus_base', 'strain_base', 'physical_attack_power_base',
        #                    'physical_critical_strike_base', 'physical_critical_damage_base',
        #                    'physical_overcome_base', 'weapon_damage_base']
        for attr in self.grad_attrs:
            setattr(self, attr, torch.tensor(getattr(self, attr), dtype=torch.float, requires_grad=True))

    @property
    def major(self):
        return self.strength

    @property
    def physical_attack_power(self):
        return super(BeiAoJue, self).final_physical_attack_power + self.major * 1.55

    @property
    def attack_power(self):
        return self.physical_attack_power

    @property
    def critical_strike(self):
        return self.physical_critical_strike

    @property
    def critical_damage(self):
        return self.physical_critical_damage

    @property
    def final_physical_overcome(self):
        return super(BeiAoJue, self).final_physical_overcome + self.major * 0.36

    @property
    def overcome(self):
        return self.physical_overcome

    @property
    def shield_ignore_base(self):
        return self.physical_shield_ignore_base

    @property
    def shield_ignore_gain(self):
        return self.physical_shield_ignore_gain


def get_attribute():
    return BeiAoJue(Target(), strength_base=10156, weapon_damage_base=3245, weapon_damage_rand=5408 - 3245,
                    surplus_base=7648, strain_base=35289, haste_base=883, physical_attack_power_base=25548,
                    physical_critical_strike_base=20877, physical_critical_damage_base=2340,
                    physical_overcome_base=35046)
