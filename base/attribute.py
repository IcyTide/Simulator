class UselessAttribute:
    drop_defence: int = 0
    beat_back_rate: int = 0
    decritical_damage_power_base_kilonum_rate: int = 0


class ResourceAttribute:
    max_life_percent_add: int = 0


class DefenseAttribute:
    physics_shield_base: int = 0

    solar_shield_base: int = 0
    lunar_shield_base: int = 0
    neutral_shield_base: int = 0
    poison_shield_base: int = 0

    _magic_shield: int = 0

    resist_critical_strike_rate: int = 0

    @property
    def magic_shield(self):
        return self._magic_shield

    @magic_shield.setter
    def magic_shield(self, value):
        residual = value - self._magic_shield
        self.solar_shield_base += residual
        self.lunar_shield_base += residual
        self.neutral_shield_base += residual
        self.poison_shield_base += residual
        self._magic_shield = value



class DamageCoefficientAttribute:
    physics_damage_coefficient: int = 0
    solar_damage_coefficient: int = 0
    lunar_damage_coefficient: int = 0
    neutral_damage_coefficient: int = 0
    poison_damage_coefficient: int = 0

    _coming_damage_coefficient: int = 0

    @property
    def coming_damage_coefficient(self):
        return self._coming_damage_coefficient

    @coming_damage_coefficient.setter
    def coming_damage_coefficient(self, value):
        residual = value - self._coming_damage_coefficient
        self.physics_damage_coefficient += residual
        self.solar_damage_coefficient += residual
        self.lunar_damage_coefficient += residual
        self.neutral_damage_coefficient += residual
        self.poison_damage_coefficient += residual
        self._coming_damage_coefficient = value


class MajorAttribute:
    strength_base: int = 0
    agility_base: int = 0

    strength_to_physics_attack_power_cof: int = 0
    strength_to_physics_overcome_cof: int = 0


class AttackAttribute(MajorAttribute):
    physics_attack_power_base: int = 0


class CriticalAttribute(MajorAttribute):
    physics_critical_strike_base_rate: int = 0
    physics_critical_damage_power_base_kilo_num_rate: int = 0


class MinorAttribute:
    haste_base: int = 0

    @property
    def haste(self):
        return 0


class DamageAttribute:
    skill_physics_damage: int = 0

    physics_damage_rand: int = 0

    _all_damage_add_percent: int = 0
    all_physics_damage_add_percent: int = 0
    all_magic_damage_add_percent: int = 0

    @property
    def all_damage_add_percent(self):
        return self._all_damage_add_percent

    @all_damage_add_percent.setter
    def all_damage_add_percent(self, value):
        residual = value - self._all_damage_add_percent
        self.all_physics_damage_add_percent += residual
        self.all_magic_damage_add_percent += residual
        self._all_damage_add_percent = value


class OtherAttribute(MinorAttribute):
    all_shield_ignore_percent: int = 0
    dst_npc_damage_coefficient: int = 0


class Attribute(
    UselessAttribute, ResourceAttribute,
    DefenseAttribute, DamageCoefficientAttribute,
    AttackAttribute, CriticalAttribute,
    DamageAttribute, OtherAttribute
):
    pass


if __name__ == '__main__':
    attr = Attribute()
    print(dir(attr))
