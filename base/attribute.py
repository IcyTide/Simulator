
class UselessAttribute:
    drop_defence: int = 0
    beat_back_rate: int = 0
    decritical_damage_power_base_kilonum_rate: int = 0


class ResourceAttribute:
    max_life_percent_add: int = 0

    mana_replenish_percent: int = 0

    max_sun_energy: int = 0
    max_moon_energy: int = 0


class CofAttribute:
    spunk_to_solar_and_lunar_attack_power_cof: int = 0
    spunk_to_solar_and_lunar_critical_strike_cof: int = 0


class DefenseAttribute:
    physics_shield_base: int = 0
    solar_shield_base: int = 0
    lunar_shield_base: int = 0
    neutral_shield_base: int = 0
    poison_shield_base: int = 0

    _magic_shield: int = 0

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


class AttackAttribute(CofAttribute):
    solar_attack_power_base: int = 0
    lunar_attack_power_base: int = 0


class DamageAttribute:
    skill_physics_damage: int = 0
    skill_solar_damage: int = 0
    skill_lunar_damage: int = 0
    skill_neutral_damage: int = 0
    skill_poison_damage: int = 0

    physics_damage_rand: int = 0
    solar_damage_rand: int = 0
    lunar_damage_rand: int = 0
    neutral_damage_rand: int = 0
    poison_damage_rand: int = 0


class OtherAttribute(UselessAttribute):
    dst_npc_damage_coefficient: int = 0


class Attribute(
    ResourceAttribute, DefenseAttribute, AttackAttribute, DamageAttribute, OtherAttribute
):

    @property
    def haste(self):
        return 0


if __name__ == '__main__':
    attr = Attribute()
    print(dir(attr))
