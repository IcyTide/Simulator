from dataclasses import dataclass

from .constant import *

import torch


@dataclass
class Attribute:
    agility_base: int
    agility_gain: int
    strength_base: int
    strength_gain: int
    spirit_base: int
    spirit_gain: int
    spunk_base: int
    spunk_gain: int

    weapon_damage_rand: int
    weapon_damage_base: int
    weapon_damage_gain: int
    surplus_base: int
    surplus_gain: int
    strain_base: int
    strain_gain: int
    haste_base: int
    haste_gain: int

    physical_attack_power_base: int
    physical_attack_power_gain: int
    magical_attack_power_base: int
    magical_attack_power_gain: int
    physical_critical_strike_base: int
    physical_critical_strike_gain: int
    magical_critical_strike_base: int
    magical_critical_strike_gain: int
    physical_critical_damage_base: int
    physical_critical_damage_gain: int
    magical_critical_damage_base: int
    magical_critical_damage_gain: int
    physical_overcome_base: int
    physical_overcome_gain: int
    magical_overcome_base: int
    magical_overcome_gain: int
    physical_shield_ignore_base: int
    physical_shield_ignore_gain: int
    magical_shield_ignore_base: int
    magical_shield_ignore_gain: int

    k_a: int
    k_b: int
    k_c: int
    k_npc: int

    def __post_init__(self):
        initialized_vars = vars(self)
        for name, value in initialized_vars.items():
            if isinstance(value, int):
                setattr(self, name, torch.tensor(value, dtype=torch.int))

    @property
    def major(self):
        raise NotImplementedError

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

    @property
    def weapon_damage(self):
        weapon_damage = self.weapon_damage_base + self.weapon_damage_base * self.weapon_damage_gain // INT_SCALE
        return weapon_damage + self.weapon_damage_rand / 2

    @property
    def base_physical_attack_power(self):
        return self.physical_attack_power_base + self.strength * STRENGTH_TO_ATTACK_POWER // INT_SCALE

    @property
    def physical_attack_power(self):
        return self.base_physical_attack_power * self.physical_attack_power_gain // INT_SCALE

    @property
    def base_magical_attack_power(self):
        return self.magical_attack_power_base + self.spunk_base * SPUNK_TO_ATTACK_POWER // INT_SCALE

    @property
    def magical_attack_power(self):
        return self.base_magical_attack_power * self.magical_attack_power_gain // INT_SCALE

    @property
    def attack_power(self):
        raise NotImplementedError

    @property
    def base_physical_critical_strike(self):
        extra_physical_critical_strike_base = self.agility * AGILITY_TO_CRITICAL_STRIKE // INT_SCALE
        return self.physical_critical_strike_base + extra_physical_critical_strike_base

    @property
    def physical_critical_strike(self):
        return self.base_physical_critical_strike / CRITICAL_STRIKE_SCALE \
            + self.physical_critical_strike_gain / PERCENT_SCALE

    @property
    def base_magical_critical_strike(self):
        extra_magical_critical_strike_base = self.agility * SPIRIT_TO_CRITICAL_STRIKE // INT_SCALE
        return self.magical_critical_strike_base + extra_magical_critical_strike_base

    @property
    def magical_critical_strike(self):
        return self.base_magical_critical_strike / CRITICAL_STRIKE_SCALE \
            + self.magical_critical_strike_gain / PERCENT_SCALE

    @property
    def critical_strike(self):
        raise NotImplementedError

    @property
    def physical_critical_damage(self):
        return CRITICAL_DAMAGE_BASE + self.physical_critical_damage_base / CRITICAL_DAMAGE_SCALE \
            + self.physical_critical_damage_gain / INT_SCALE

    @property
    def magical_critical_damage(self):
        return CRITICAL_DAMAGE_BASE + self.magical_critical_damage_base / CRITICAL_DAMAGE_SCALE \
            + self.magical_critical_damage_gain / INT_SCALE

    @property
    def critical_damage(self):
        raise NotImplementedError

    @property
    def base_physical_overcome(self):
        extra_physical_overcome_base = self.strength_base * STRENGTH_TO_OVERCOME // INT_SCALE
        return self.physical_overcome_base + extra_physical_overcome_base
    
    @property
    def physical_overcome(self):
        physical_overcome = self.base_physical_overcome \
                            + self.base_physical_overcome * self.physical_overcome_gain // INT_SCALE
        return physical_overcome / OVERCOME_SCALE

    @property
    def base_magical_overcome(self):
        extra_magical_overcome_base = self.spunk_base * SPUNK_TO_OVERCOME // INT_SCALE
        return self.magical_overcome_base + extra_magical_overcome_base

    @property
    def magical_overcome(self):
        magical_overcome = self.base_magical_overcome \
                            + self.base_magical_overcome * self.magical_overcome_gain // INT_SCALE
        return magical_overcome / OVERCOME_SCALE

    @property
    def overcome(self):
        raise NotImplementedError
