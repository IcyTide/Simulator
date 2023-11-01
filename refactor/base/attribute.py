from dataclasses import dataclass

from .constant import *

"""
    TODO: add update func to replace property
"""


@dataclass
class Target:
    level: int = 124
    physical_shield_base: int = 27550
    magical_shield_base: int = 27550

    physical_shield_gain: int = 0
    magical_shield_gain: int = 0

    physical_vulnerable: int = 0
    magical_vulnerable: int = 0

    @property
    def shield_base(self):
        return self.physical_shield_base

    @property
    def shield_gain(self):
        return self.physical_shield_gain

    def shield(self, shield_ignore_base, shield_ignore_gain):
        shield = self.shield_base - self.shield_base * shield_ignore_base + self.shield_gain
        return shield - shield * shield_ignore_gain

    def defense(self, shield_ignore_base, shield_ignore_gain):
        shield = self.shield(shield_ignore_base, shield_ignore_gain)
        return shield / (shield + SHIELD_SCALE * (LEVEL_SCALE * self.level - LEVEL_CONSTANT))

    @property
    def vulnerable(self):
        return self.physical_vulnerable


@dataclass
class Attribute:
    target: Target = None

    level: int = 120
    all_major_base: int = 0
    all_major_gain: int = 0
    agility_base: int = 0
    agility_gain: float = 0
    strength_base: int = 0
    strength_gain: float = 0
    spirit_base: int = 0
    spirit_gain: float = 0
    spunk_base: int = 0
    spunk_gain: float = 0

    surplus_base: int = 0

    strain_base: int = 0
    strain_gain: float = 0
    haste_base: int = 0
    haste_gain: float = 0

    physical_attack_power_base: int = 0
    physical_attack_power_gain: float = 0
    magical_attack_power_base: int = 0
    magical_attack_power_gain: float = 0

    all_critical_strike_base: int = 0
    all_critical_strike_gain: float = 0
    physical_critical_strike_base: int = 0
    physical_critical_strike_gain: float = 0
    magical_critical_strike_base: int = 0
    magical_critical_strike_gain: float = 0

    all_critical_damage_gain: float = 0
    physical_critical_damage_base: int = 0
    physical_critical_damage_gain: float = 0
    magical_critical_damage_base: int = 0
    magical_critical_damage_gain: float = 0

    physical_overcome_base: int = 0
    physical_overcome_gain: float = 0
    magical_overcome_base: int = 0
    magical_overcome_gain: float = 0

    weapon_damage_rand: int = 0
    weapon_damage_base: int = 0
    weapon_damage_gain: float = 0

    physical_shield_ignore_base: float = 0
    magical_shield_ignore_base: float = 0
    physical_shield_ignore_gain: float = 0
    magical_shield_ignore_gain: float = 0

    damage_addition: float = 0
    pve_addition: float = 0

    """ major attributes """

    def __post_init__(self):
        if not self.target:
            self.target = Target()
        self.grad_scale = {
            "agility_base": MAJOR_BASE,
            "spunk_base": MAJOR_BASE,
            "strength_base": MAJOR_BASE,
            "spirit_base": MAJOR_BASE,
            "surplus_base": MINOR_BASE,
            "strain_base": MINOR_BASE,
            # "haste_base": MINOR_BASE,
            "physical_attack_power_base": ATTACK_POWER_BASE,
            "magical_attack_power_base": ATTACK_POWER_BASE,
            "physical_critical_strike_base": MINOR_BASE,
            "magical_critical_strike_base": MINOR_BASE,
            "physical_critical_damage_base": MINOR_BASE,
            "magical_critical_damage_base": MINOR_BASE,
            "physical_overcome_base": MINOR_BASE,
            "magical_overcome_base": MINOR_BASE,
            "weapon_damage_base": WEAPON_DAMAGE_BASE
        }
        self.grad_attrs = []

    @property
    def base_agility(self):
        return self.agility_base + self.all_major_base

    @property
    def agility(self):
        return self.base_agility + self.base_agility * (self.agility_gain + self.all_major_gain)

    @property
    def base_spunk(self):
        return self.spunk_base + self.all_major_base

    @property
    def spunk(self):
        return self.base_spunk + self.base_spunk * (self.spunk_gain + self.all_major_gain)

    @property
    def base_strength(self):
        return self.strength_base + self.all_major_base

    @property
    def strength(self):
        return self.base_strength + self.base_strength * (self.strength_gain + self.all_major_gain)

    @property
    def base_spirit(self):
        return self.spirit + self.all_major_base

    @property
    def spirit(self):
        return self.base_spirit + self.base_spirit * (self.spirit_gain + self.all_major_gain)

    @property
    def major(self):
        raise NotImplementedError

    """ minor attributes """

    @property
    def surplus(self):
        return self.surplus_base

    @property
    def base_strain(self):
        return self.strain_base

    @property
    def final_strain(self):
        return self.strain_base / STRAIN_SCALE

    @property
    def strain(self):
        return self.final_strain + self.strain_gain

    @property
    def base_haste(self):
        return self.haste_base

    @property
    def final_haste(self):
        return self.haste_base / HASTE_SCALE

    @property
    def haste(self):
        return self.final_haste + self.haste_gain

    @property
    def base_physical_attack_power(self):
        return self.physical_attack_power_base + self.strength * STRENGTH_TO_ATTACK_POWER

    @property
    def final_physical_attack_power(self):
        return self.base_physical_attack_power + self.base_physical_attack_power * self.physical_attack_power_gain

    physical_attack_power = final_physical_attack_power

    @property
    def base_magical_attack_power(self):
        return self.magical_attack_power_base + self.spunk_base * SPUNK_TO_ATTACK_POWER

    @property
    def final_magical_attack_power(self):
        return self.base_magical_attack_power + self.base_magical_attack_power * self.magical_attack_power_gain

    magical_attack_power = final_magical_attack_power

    @property
    def attack_power(self):
        raise NotImplementedError

    @property
    def base_physical_critical_strike(self):
        return self.physical_critical_strike_base + self.all_critical_strike_base + \
               self.agility * AGILITY_TO_CRITICAL_STRIKE

    @property
    def final_physical_critical_strike(self):
        return self.base_physical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def physical_critical_strike(self):
        return self.final_physical_critical_strike + self.physical_critical_strike_gain + self.all_critical_strike_gain

    @property
    def base_magical_critical_strike(self):
        return self.magical_critical_strike_base + self.all_critical_strike_base + \
               self.spirit * SPIRIT_TO_CRITICAL_STRIKE

    @property
    def final_magical_critical_strike(self):
        return self.base_magical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def magical_critical_strike(self):
        return self.final_magical_critical_strike + self.magical_critical_strike_gain + self.all_critical_strike_gain

    @property
    def critical_strike(self):
        raise NotImplementedError

    @property
    def base_physical_critical_damage(self):
        return self.physical_critical_damage_base

    @property
    def final_physical_critical_damage(self):
        return self.physical_critical_damage_base / CRITICAL_DAMAGE_SCALE

    @property
    def physical_critical_damage(self):
        return CRITICAL_DAMAGE_BASE + self.final_physical_critical_damage + self.physical_critical_damage_gain + \
               self.all_critical_damage_gain

    @property
    def base_magical_critical_damage(self):
        return self.magical_critical_damage_base

    @property
    def final_magical_critical_damage(self):
        return self.magical_critical_damage_base / CRITICAL_DAMAGE_SCALE

    @property
    def magical_critical_damage(self):
        return CRITICAL_DAMAGE_BASE + self.final_magical_critical_damage + self.magical_critical_damage_gain + \
               self.all_critical_damage_gain

    @property
    def critical_damage(self):
        raise NotImplementedError

    @property
    def base_physical_overcome(self):
        return self.physical_overcome_base + self.strength_base * STRENGTH_TO_OVERCOME

    @property
    def final_physical_overcome(self):
        return self.base_physical_overcome + self.base_physical_overcome * self.physical_overcome_gain

    @property
    def physical_overcome(self):
        return self.final_physical_overcome / OVERCOME_SCALE

    @property
    def base_magical_overcome(self):
        return self.magical_overcome_base + self.spunk_base * SPUNK_TO_OVERCOME

    @property
    def final_magical_overcome(self):
        return self.base_magical_overcome + self.base_magical_overcome * self.magical_overcome_gain

    @property
    def magical_overcome(self):
        return self.final_magical_overcome / OVERCOME_SCALE

    @property
    def overcome(self):
        raise NotImplementedError

    """ others """

    @property
    def base_weapon_damage(self):
        return self.weapon_damage_base + self.weapon_damage_rand / 2

    @property
    def weapon_damage(self):
        return self.weapon_damage_base + self.weapon_damage_base * self.weapon_damage_gain + \
               self.weapon_damage_rand / 2

    @property
    def shield_ignore_base(self):
        raise NotImplementedError

    @property
    def shield_ignore_gain(self):
        raise NotImplementedError

    @property
    def level_reduction(self):
        return LEVEL_REDUCTION * (self.target.level - self.level)
