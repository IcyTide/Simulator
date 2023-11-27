from dataclasses import dataclass

from base.constant import AGILITY_TO_CRITICAL_STRIKE, STRENGTH_TO_ATTACK_POWER, STRENGTH_TO_OVERCOME, \
    STRAIN_SCALE, HASTE_SCALE, CRITICAL_STRIKE_SCALE, CRITICAL_POWER_BASE, CRITICAL_POWER_SCALE, OVERCOME_SCALE


@dataclass
class Attribute:
    level: int = 120
    _all_major_base: int = 0
    _all_major_gain: float = 0
    _agility_base: int = 0
    _agility_gain: float = 0
    _agility: int = 0
    _strength_base: int = 0
    _strength_gain: float = 0
    _strength: int = 0

    surplus: int = 0

    _strain_base: int = 0
    _strain_percent: float = 0
    _strain_gain: float = 0
    _strain: float = 0
    _haste_base: int = 0
    _haste_percent: float = 0
    _haste_gain: float = 0
    _haste: float = 0

    _physical_attack_power_base: int = 0
    _base_physical_attack_power: int = 0
    _physical_attack_power_gain: float = 0
    _physical_attack_power: int = 0

    _all_critical_strike_base: int = 0
    _all_critical_strike_gain: float = 0

    _physical_critical_strike_base: int = 0
    _base_physical_critical_strike: int = 0
    _physical_critical_strike_percent: float = 0
    _physical_critical_strike_gain: float = 0
    _physical_critical_strike: float = 0

    _all_critical_power_gain: float = 0

    _physical_critical_power_base: int = 0
    _physical_critical_power_percent: float = 0
    _physical_critical_power_gain: float = 0
    _physical_critical_power: float = 0

    _physical_overcome_base: int = 0
    _base_physical_overcome: int = 0
    _final_physical_overcome: int = 0
    _physical_overcome_gain: float = 0
    _physical_overcome: float = 0

    weapon_damage_rand: int = 0
    _weapon_damage_base: int = 0
    _weapon_damage_gain: float = 0
    _weapon_damage: int = 0

    _all_shield_ignore: float = 0
    _physical_shield_ignore: float = 0

    damage_addition: float = 0
    pve_addition: float = 0
    cd_reduction: float = 0

    def __post_init__(self):
        self.grad_attrs = {}
        self.delta_attr = ""
        self.delta_value = 0
        self.delta_grad_attrs = {}

        self.all_major_base += 41

    """ Major Attr Function"""

    @property
    def all_major_base(self):
        return self._all_major_base

    @all_major_base.setter
    def all_major_base(self, all_major_base):
        residual = all_major_base - self._all_major_base
        self.agility_base += residual
        self.strength_base += residual
        self._all_major_base = all_major_base

    @property
    def all_major_gain(self):
        return self._all_major_gain

    @all_major_gain.setter
    def all_major_gain(self, all_major_gain):
        residual = all_major_gain - self._all_major_gain
        self.agility_gain += residual
        self.strength_gain += residual
        self._all_major_gain = all_major_gain

    @property
    def agility_base(self):
        return self._agility_base

    @agility_base.setter
    def agility_base(self, agility_base):
        self._agility_base = agility_base
        self.agility = agility_base * (1 + self._agility_gain)

    @property
    def agility_gain(self):
        return self._agility_gain

    @agility_gain.setter
    def agility_gain(self, agility_gain):
        self._agility_gain = agility_gain
        self.agility = self._agility_base * (1 + agility_gain)

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, agility):
        agility = int(agility)
        self._agility = agility
        self.base_physical_critical_strike = self._physical_critical_strike_base + agility * AGILITY_TO_CRITICAL_STRIKE

    @property
    def strength_base(self):
        return self._strength_base

    @strength_base.setter
    def strength_base(self, strength_base):
        self._strength_base = strength_base
        self.strength = strength_base * (1 + self._strength_gain)

    @property
    def strength_gain(self):
        return self._strength_gain

    @strength_gain.setter
    def strength_gain(self, strength_gain):
        self._strength_gain = strength_gain
        self.strength = self._strength_base * (1 + strength_gain)

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        strength = int(strength)
        self._strength = strength
        self.base_physical_attack_power = self._physical_attack_power_base + strength * STRENGTH_TO_ATTACK_POWER
        self.base_physical_overcome = self._physical_overcome_base + strength * STRENGTH_TO_OVERCOME

    """ Minor Function """

    @property
    def strain_base(self):
        return self._strain_base

    @strain_base.setter
    def strain_base(self, strain_base):
        self._strain_base = strain_base
        self.strain_percent = strain_base / STRAIN_SCALE

    @property
    def strain_percent(self):
        return self._strain_percent

    @strain_percent.setter
    def strain_percent(self, strain_percent):
        self._strain_percent = strain_percent
        self.strain = strain_percent + self._strain_gain

    @property
    def strain_gain(self):
        return self._strain_gain

    @strain_gain.setter
    def strain_gain(self, strain_gain):
        self._strain_gain = strain_gain
        self.strain = self._strain_percent + strain_gain

    @property
    def strain(self):
        return self._strain

    @strain.setter
    def strain(self, strain):
        self._strain = strain

    @property
    def haste_base(self):
        return self._haste_base

    @haste_base.setter
    def haste_base(self, haste_base):
        self._haste_base = haste_base
        self.haste_percent = haste_base / HASTE_SCALE

    @property
    def haste_percent(self):
        return self._haste_percent

    @haste_percent.setter
    def haste_percent(self, haste_percent):
        self._haste_percent = haste_percent
        self.haste = haste_percent + self._haste_gain

    @property
    def haste_gain(self):
        return self._haste_gain

    @haste_gain.setter
    def haste_gain(self, haste_gain):
        self._haste_gain = haste_gain
        self.haste = self._haste_percent + haste_gain

    @property
    def haste(self):
        return self._haste

    @haste.setter
    def haste(self, haste):
        self._haste = haste

    """ Attack Power Function """

    @property
    def physical_attack_power_base(self):
        return self._physical_attack_power_base

    @physical_attack_power_base.setter
    def physical_attack_power_base(self, physical_attack_power_base):
        self._physical_attack_power_base = physical_attack_power_base
        self.base_physical_attack_power = physical_attack_power_base + self._strength * STRENGTH_TO_ATTACK_POWER

    @property
    def base_physical_attack_power(self):
        return self._base_physical_attack_power

    @base_physical_attack_power.setter
    def base_physical_attack_power(self, base_physical_attack_power):
        base_physical_attack_power = int(base_physical_attack_power)
        self._base_physical_attack_power = base_physical_attack_power
        self.physical_attack_power = base_physical_attack_power * (1 + self._physical_attack_power_gain)

    @property
    def physical_attack_power_gain(self):
        return self._physical_attack_power_gain

    @physical_attack_power_gain.setter
    def physical_attack_power_gain(self, physical_attack_power_gain):
        self._physical_attack_power_gain = physical_attack_power_gain
        self.physical_attack_power = self._base_physical_attack_power * (1 + physical_attack_power_gain)

    @property
    def physical_attack_power(self):
        return self._physical_attack_power

    @physical_attack_power.setter
    def physical_attack_power(self, physical_attack_power):
        self._physical_attack_power = int(physical_attack_power)

    """ Critical Strike Function"""

    @property
    def all_critical_strike_base(self):
        return self._all_critical_strike_base

    @all_critical_strike_base.setter
    def all_critical_strike_base(self, all_critical_strike_base):
        residual = all_critical_strike_base - self._all_critical_strike_base
        self.physical_critical_strike_base += residual
        self._all_critical_strike_base = all_critical_strike_base

    @property
    def all_critical_strike_gain(self):
        return self._all_critical_strike_gain

    @all_critical_strike_gain.setter
    def all_critical_strike_gain(self, all_critical_strike_gain):
        residual = all_critical_strike_gain - self._all_critical_strike_gain
        self.physical_critical_strike_gain += residual
        self._all_critical_strike_gain = all_critical_strike_gain

    @property
    def physical_critical_strike_base(self):
        return self._physical_critical_strike_base

    @physical_critical_strike_base.setter
    def physical_critical_strike_base(self, physical_critical_strike_base):
        self._physical_critical_strike_base = physical_critical_strike_base
        self.base_physical_critical_strike = physical_critical_strike_base + self._agility * AGILITY_TO_CRITICAL_STRIKE

    @property
    def base_physical_critical_strike(self):
        return self._base_physical_critical_strike

    @base_physical_critical_strike.setter
    def base_physical_critical_strike(self, base_physical_critical_strike):
        base_physical_critical_strike = int(base_physical_critical_strike)
        self._base_physical_critical_strike = base_physical_critical_strike
        self.physical_critical_strike_percent = base_physical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def physical_critical_strike_percent(self):
        return self._physical_critical_strike_percent

    @physical_critical_strike_percent.setter
    def physical_critical_strike_percent(self, physical_critical_strike_percent):
        self._physical_critical_strike_percent = physical_critical_strike_percent
        self.physical_critical_strike = physical_critical_strike_percent + self._physical_critical_strike_gain

    @property
    def physical_critical_strike_gain(self):
        return self._physical_critical_strike_gain

    @physical_critical_strike_gain.setter
    def physical_critical_strike_gain(self, physical_critical_strike_gain):
        self._physical_critical_strike_gain = physical_critical_strike_gain
        self.physical_critical_strike = self._physical_critical_strike_percent + physical_critical_strike_gain

    @property
    def physical_critical_strike(self):
        return self._physical_critical_strike

    @physical_critical_strike.setter
    def physical_critical_strike(self, physical_critical_strike):
        self._physical_critical_strike = physical_critical_strike

    """ Critical Power Function"""

    @property
    def all_critical_power_gain(self):
        return self._all_critical_power_gain

    @all_critical_power_gain.setter
    def all_critical_power_gain(self, all_critical_power_gain):
        residual = all_critical_power_gain - self._all_critical_power_gain
        self.physical_critical_power_gain += residual
        self._all_critical_power_gain = all_critical_power_gain

    @property
    def physical_critical_power_base(self):
        return self._physical_critical_power_base

    @physical_critical_power_base.setter
    def physical_critical_power_base(self, physical_critical_power_base):
        self._physical_critical_power_base = physical_critical_power_base
        self.physical_critical_power_percent = CRITICAL_POWER_BASE + physical_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def physical_critical_power_percent(self):
        return self._physical_critical_power_percent

    @physical_critical_power_percent.setter
    def physical_critical_power_percent(self, physical_critical_power_percent):
        self._physical_critical_power_percent = physical_critical_power_percent
        self.physical_critical_power = physical_critical_power_percent + self._physical_critical_power_gain

    @property
    def physical_critical_power_gain(self):
        return self._physical_critical_power_gain

    @physical_critical_power_gain.setter
    def physical_critical_power_gain(self, physical_critical_power_gain):
        self._physical_critical_power_gain = physical_critical_power_gain
        self.physical_critical_power = self._physical_critical_power_percent + physical_critical_power_gain

    @property
    def physical_critical_power(self):
        return self._physical_critical_power

    @physical_critical_power.setter
    def physical_critical_power(self, physical_critical_power):
        self._physical_critical_power = physical_critical_power

    """ Overcome Function"""

    @property
    def physical_overcome_base(self):
        return self._physical_overcome_base

    @physical_overcome_base.setter
    def physical_overcome_base(self, physical_overcome_base):
        self._physical_overcome_base = physical_overcome_base
        self.base_physical_overcome = physical_overcome_base + self._strength * STRENGTH_TO_OVERCOME

    @property
    def base_physical_overcome(self):
        return self._base_physical_overcome

    @base_physical_overcome.setter
    def base_physical_overcome(self, base_physical_overcome):
        base_physical_overcome = int(base_physical_overcome)
        self._base_physical_overcome = base_physical_overcome
        self.final_physical_overcome = base_physical_overcome * (1 + self._physical_overcome_gain)

    @property
    def physical_overcome_gain(self):
        return self._physical_overcome_gain

    @physical_overcome_gain.setter
    def physical_overcome_gain(self, physical_overcome_gain):
        self._physical_overcome_gain = physical_overcome_gain
        self.final_physical_overcome = self._base_physical_overcome * (1 + physical_overcome_gain)

    @property
    def final_physical_overcome(self):
        return self._final_physical_overcome

    @final_physical_overcome.setter
    def final_physical_overcome(self, final_physical_overcome):
        final_physical_overcome = int(final_physical_overcome)
        self._final_physical_overcome = final_physical_overcome
        self.physical_overcome = final_physical_overcome / OVERCOME_SCALE

    @property
    def physical_overcome(self):
        return self._physical_overcome

    @physical_overcome.setter
    def physical_overcome(self, physical_overcome):
        self._physical_overcome = physical_overcome

    """ Weapon Damage Function """

    @property
    def weapon_damage_base(self):
        return self._weapon_damage_base

    @weapon_damage_base.setter
    def weapon_damage_base(self, weapon_damage_base):
        self._weapon_damage_base = weapon_damage_base
        self.weapon_damage = weapon_damage_base * (1 + self._weapon_damage_gain) + self.weapon_damage_rand / 2

    @property
    def weapon_damage_gain(self):
        return self._weapon_damage_gain

    @weapon_damage_gain.setter
    def weapon_damage_gain(self, weapon_damage_gain):
        self._weapon_damage_gain = weapon_damage_gain
        self.weapon_damage = self._weapon_damage_base * (1 + weapon_damage_gain) + self.weapon_damage_rand / 2

    @property
    def weapon_damage(self):
        return self._weapon_damage

    @weapon_damage.setter
    def weapon_damage(self, weapon_damage):
        self._weapon_damage = int(weapon_damage)

    """ Others """

    @property
    def all_shield_ignore(self):
        return self._all_shield_ignore

    @all_shield_ignore.setter
    def all_shield_ignore(self, all_shield_ignore):
        residual = all_shield_ignore - self._all_shield_ignore
        self.physical_shield_ignore += residual
        self._all_shield_ignore = all_shield_ignore

    @property
    def physical_shield_ignore(self):
        return self._physical_shield_ignore

    @physical_shield_ignore.setter
    def physical_shield_ignore(self, physical_shield_ignore):
        self._physical_shield_ignore = physical_shield_ignore
