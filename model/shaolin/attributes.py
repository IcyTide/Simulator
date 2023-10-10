from abstract import Attribute
from constants import CRITICAL_STRIKE_SCALE


class ShaolinAttribute(Attribute):
    def __init__(self, **args):
        super().__init__(**args)
        self.k_counter = 0.3

    @property
    def magical_attack_power(self):
        return super().magical_attack_power + self.spunk * 1.85

    @property
    def magical_critical_strike(self):
        return super().magical_critical_strike + self.spunk * 0.38 / CRITICAL_STRIKE_SCALE

    @property
    def attack_power(self):
        return self.magical_attack_power

    @property
    def critical_strike(self):
        return self.magical_critical_strike

    @property
    def critical_effect(self):
        return self.magical_critical_effect

    @property
    def overcome(self):
        return self.magical_overcome


test = ShaolinAttribute(base_spunk=8498, base_magical_attack_power=26116,
                        weapon_damage=(3282 + 5470) / 2,
                        base_magical_critical_strike=10586, base_magical_critical_effect=0,
                        base_magical_overcome=41697, base_strain=20304, counter=21231, target_level=124)


my_4 = ShaolinAttribute(base_spunk=8351,
                        base_magical_attack_power=25011,
                        weapon_damage=(3282 + 5470) / 2,
                        base_magical_critical_strike=13061,
                        base_magical_critical_effect=0,
                        base_magical_overcome=34808,
                        base_strain=18156,
                        counter=19306,
                        target_level=124)

my_rare = ShaolinAttribute(base_spunk=5278,
                           base_magical_attack_power=33336,
                           weapon_damage=(3282 + 5470) / 2,
                           base_magical_critical_strike=7791,
                           base_magical_critical_effect=282,
                           base_magical_overcome=32987,
                           base_strain=14873,
                           counter=38051,
                           target_level=124)
