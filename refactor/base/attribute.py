from dataclasses import dataclass, field
from typing import List

from base.constant import *


@dataclass
class Attribute:
    """Self"""
    agility_base: int = 0
    agility_gain: int = 0
    strength_base: int = 0
    strength_gain: int = 0
    spirit_base: int = 0
    spirit_gain: int = 0
    spunk_base: int = 0
    spunk_gain: int = 0

    weapon_damage_rand: int = 0
    weapon_damage_base: int = 0
    weapon_damage_gain: int = 0
    surplus_base: int = 0
    surplus_gain: int = 0
    strain_base: int = 0
    strain_gain: int = 0
    haste_base: int = 0
    haste_gain: int = 0

    physical_attack_power_base: int = 0
    physical_attack_power_gain: int = 0
    magical_attack_power_base: int = 0
    magical_attack_power_gain: int = 0
    physical_critical_strike_base: int = 0
    physical_critical_strike_gain: int = 0
    magical_critical_strike_base: int = 0
    magical_critical_strike_gain: int = 0
    physical_critical_damage_base: int = 0
    physical_critical_damage_gain: int = 0
    magical_critical_damage_base: int = 0
    magical_critical_damage_gain: int = 0
    physical_overcome_base: int = 0
    physical_overcome_gain: int = 0
    magical_overcome_base: int = 0
    magical_overcome_gain: int = 0

    physical_shield_ignore_gain: int = 0
    magical_shield_ignore_gain: int = 0

    """Target"""

    def __post_init__(self):
        initialized_vars = vars(self)
        for name, value in initialized_vars.items():
            if name.endswith("_base") and isinstance(value, int):
                setattr(self, name, torch.tensor(value, dtype=torch.int))

    @property
    def major(self):
        # raise NotImplementedError
        return self.strength

    @property
    def agility(self):
        return self.agility_base + self.agility_base * self.agility_gain // INT_SCALE

    @property
    def spunk(self):
        return self.spunk_base + self.spunk_base * self.spunk_gain // INT_SCALE

    @property
    def strength(self):
        return self.strength_base + self.strength_base * self.strength_gain // INT_SCALE

    @property
    def spirit(self):
        return self.spirit_base + self.spirit_base * self.spirit_gain // INT_SCALE

    """"""

    @property
    def base_weapon_damage(self):
        return self.weapon_damage_base + self.weapon_damage_rand / 2

    @property
    def final_weapon_damage(self):
        return self.weapon_damage_base + \
               self.weapon_damage_base * self.weapon_damage_gain // INT_SCALE + \
               self.weapon_damage_rand / 2

    weapon_damage = final_weapon_damage

    @property
    def base_surplus(self):
        return self.surplus_base

    @property
    def final_surplus(self):
        return self.surplus_base + self.surplus_gain

    surplus = final_surplus

    @property
    def base_strain(self):
        return self.strain_base

    @property
    def final_strain(self):
        return self.strain_base / STRAIN_SCALE

    @property
    def strain(self):
        return self.final_strain + self.strain_gain / INT_SCALE

    @property
    def base_haste(self):
        return self.haste_base

    @property
    def final_haste(self):
        return self.haste_base / HASTE_SCALE

    @property
    def haste(self):
        return INT_SCALE / (INT_SCALE + self.final_haste * INT_SCALE + self.haste_gain)

    """"""

    @property
    def base_physical_attack_power(self):
        return self.physical_attack_power_base + self.strength * STRENGTH_TO_ATTACK_POWER // INT_SCALE

    @property
    def final_physical_attack_power(self):
        return self.base_physical_attack_power + \
               self.base_physical_attack_power * self.physical_attack_power_gain // INT_SCALE

    physical_attack_power = final_physical_attack_power

    @property
    def base_magical_attack_power(self):
        return self.magical_attack_power_base + self.spunk_base * SPUNK_TO_ATTACK_POWER // INT_SCALE

    @property
    def final_magical_attack_power(self):
        return self.base_magical_attack_power + \
               self.base_magical_attack_power * self.magical_attack_power_gain // INT_SCALE

    magical_attack_power = final_magical_attack_power

    @property
    def attack_power(self):
        # raise NotImplementedError
        return self.physical_attack_power

    @property
    def base_physical_critical_strike(self):
        return self.physical_critical_strike_base + self.agility * AGILITY_TO_CRITICAL_STRIKE // INT_SCALE

    @property
    def final_physical_critical_strike(self):
        return self.base_physical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def physical_critical_strike(self):
        return self.final_physical_critical_strike + self.physical_critical_strike_gain / PERCENT_SCALE

    @property
    def base_magical_critical_strike(self):
        return self.magical_critical_strike_base + self.spirit * SPIRIT_TO_CRITICAL_STRIKE // INT_SCALE

    @property
    def final_magical_critical_strike(self):
        return self.base_magical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def magical_critical_strike(self):
        return self.final_magical_critical_strike + self.magical_critical_strike_gain / PERCENT_SCALE

    @property
    def critical_strike(self):
        # raise NotImplementedError
        return self.physical_critical_strike

    @property
    def base_physical_critical_damage(self):
        return self.physical_critical_damage_base

    @property
    def final_physical_critical_damage(self):
        return self.physical_critical_damage_base / CRITICAL_DAMAGE_SCALE

    @property
    def physical_critical_damage(self):
        return CRITICAL_DAMAGE_BASE + self.final_physical_critical_damage + \
               self.physical_critical_damage_gain / INT_SCALE

    @property
    def base_magical_critical_damage(self):
        return self.magical_critical_damage_base

    @property
    def final_magical_critical_damage(self):
        return self.magical_critical_damage_base / CRITICAL_DAMAGE_SCALE

    @property
    def magical_critical_damage(self):
        return CRITICAL_DAMAGE_BASE + self.final_magical_critical_damage + \
               self.magical_critical_damage_gain / INT_SCALE

    @property
    def critical_damage(self):
        # raise NotImplementedError
        return self.physical_critical_damage

    @property
    def base_physical_overcome(self):
        return self.physical_overcome_base + self.strength_base * STRENGTH_TO_OVERCOME // INT_SCALE

    @property
    def final_physical_overcome(self):
        return self.base_physical_overcome + self.base_physical_overcome * self.physical_overcome_gain // INT_SCALE

    @property
    def physical_overcome(self):
        return self.final_physical_overcome / OVERCOME_SCALE

    @property
    def base_magical_overcome(self):
        return self.magical_overcome_base + self.strength_base * STRENGTH_TO_OVERCOME // INT_SCALE

    @property
    def final_magical_overcome(self):
        return self.base_magical_overcome + self.base_magical_overcome * self.magical_overcome_gain // INT_SCALE

    @property
    def magical_overcome(self):
        return self.final_magical_overcome / OVERCOME_SCALE

    @property
    def overcome(self):
        # raise NotImplementedError
        return self.physical_overcome


