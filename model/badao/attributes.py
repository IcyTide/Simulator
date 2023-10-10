from model.abstract import Attribute
from model.constants import OVERCOME_SCALE


class BadaoAttribtue(Attribute):
    def __init__(self, **args):
        super().__init__(**args)
        self.k_npc = 0.14
        self.divine_rate = 0.03

    @property
    def physical_attack_power(self):
        return super().physical_attack_power + self.strength * 1.55

    @property
    def physical_overcome(self):
        return super().physical_overcome + self.strength * 0.36 / OVERCOME_SCALE

    @property
    def attack_power(self):
        return self.physical_attack_power

    @property
    def critical_strike(self):
        return self.physical_critical_strike

    @property
    def critical_effect(self):
        return self.physical_critical_effect

    @property
    def overcome(self):
        return self.physical_overcome


attribute_counter = BadaoAttribtue(base_strength=8315, base_physical_attack_power=19507,
                                   weapon_damage=(2628 + 4380) / 2,
                                   base_physical_critical_strike=11732, base_physical_critical_effect=2340,
                                   base_physical_overcome=34271, base_strain=20543, counter=19953, target_level=124)
attribute_strain = BadaoAttribtue(base_strength=8734, base_physical_attack_power=21700, weapon_damage=(2593 + 4322) / 2,
                                  base_physical_critical_strike=17423, base_physical_critical_effect=1170,
                                  base_physical_overcome=27706, base_strain=34521, counter=188, target_level=124)

attribute_tifu = BadaoAttribtue(base_strength=8456, base_physical_attack_power=22296, weapon_damage=(2593 + 4322) / 2,
                                base_physical_critical_strike=17598, base_physical_critical_effect=1588,
                                base_physical_overcome=26291, base_strain=34661, counter=0, target_level=124)
attribute_222 = BadaoAttribtue(base_strength=8496, base_physical_attack_power=22608, weapon_damage=(3004 + 5007) / 2,
                               base_physical_critical_strike=20992, base_physical_critical_effect=0,
                               base_physical_overcome=31171, base_strain=31759, counter=418, target_level=124)

# attribute_42 = BadaoAttribtue(base_strength=8988, base_physical_attack_power=22087,
#                               weapon_damage=(3004 + 5007) / 2,
#                               base_physical_critical_strike=22211, base_physical_critical_effect=2340,
#                               base_physical_overcome=29724, base_strain=23213, counter=6310, target_level=124)

attribute_42 = BadaoAttribtue(base_strength=9628, base_physical_attack_power=22405,
                              weapon_damage=(2628 + 4380) / 2,
                              base_physical_critical_strike=18885, base_physical_critical_effect=2340,
                              base_physical_overcome=31831, base_strain=23317, counter=14955, target_level=124)

attribute_4 = BadaoAttribtue(base_strength=9509, base_physical_attack_power=22869,
                             weapon_damage=(2593 + 4322) / 2,
                             base_physical_critical_strike=14313, base_physical_critical_effect=1588,
                             base_physical_overcome=34977, base_strain=26503, counter=11655, target_level=124)

attribute_chengwu = BadaoAttribtue(base_strength=8570, base_physical_attack_power=22963,
                                   weapon_damage=(3004 + 5007) / 2,
                                   base_physical_critical_strike=20112, base_physical_critical_effect=0,
                                   base_physical_overcome=30688, base_strain=24951, counter=6310, target_level=124)

divine_counter = BadaoAttribtue(base_strength=5381, base_physical_attack_power=27345,
                                weapon_damage=(3004 + 5007) / 2,
                                base_physical_critical_strike=28646, base_physical_critical_effect=6432,
                                base_physical_overcome=26376, base_strain=16231, counter=19598, target_level=124)

divine_strain = BadaoAttribtue(base_strength=7194, base_physical_attack_power=23680,
                               weapon_damage=(3004 + 5007) / 2,
                               base_physical_critical_strike=22143, base_physical_critical_effect=3786,
                               base_physical_overcome=26893, base_strain=26826, counter=12872, target_level=124)

my_counter = BadaoAttribtue(base_strength=9398, base_physical_attack_power=22327,
                            weapon_damage=(2896 + 4827) / 2,
                            base_physical_critical_strike=14983, base_physical_critical_effect=2340,
                            base_physical_overcome=33523, base_strain=25172, counter=12866, target_level=122)

my_strain = BadaoAttribtue(base_strength=9498, base_physical_attack_power=22290,
                           weapon_damage=(2896 + 4827) / 2,
                           base_physical_critical_strike=19484, base_physical_critical_effect=2340,
                           base_physical_overcome=28830, base_strain=25038, counter=13257, target_level=122)

temp = BadaoAttribtue(base_strength=7636, base_physical_attack_power=23921,
                      weapon_damage=(2896 + 4827) / 2,
                      base_physical_critical_strike=20621, base_physical_critical_effect=3176,
                      base_physical_overcome=33538, base_strain=19506, counter=23049, target_level=124)
