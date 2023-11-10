from dataclasses import dataclass
from functools import cached_property, cache

from .constant import *

"""
    TODO: add update func to replace property
"""


@dataclass
class Target:
    SHIELD_BASE_MAP = {
        124: 27550
    }
    level: int = 124

    physical_shield_base: int = 0
    # magical_shield_base: int = 0

    physical_shield_gain: int = 0
    # magical_shield_gain: int = 0

    physical_vulnerable: int = 0
    # magical_vulnerable: int = 0

    shield_constant: float = 0

    def __post_init__(self):
        self.physical_shield_base = self.SHIELD_BASE_MAP[self.level]
        # self.magical_shield_base = self.SHIELD_BASE_MAP[self.level]
        self.shield_constant = SHIELD_SCALE * (LEVEL_SCALE * self.level - LEVEL_CONSTANT)


@dataclass
class Attribute:
    target: Target = None

    level: int = 120
    _all_major_base: int = 0
    _all_major_gain: float = 0
    _agility_base: int = 0
    _base_agility: int = 0
    _agility_gain: float = 0
    _agility: int = 0
    _strength_base: int = 0
    _base_strength: int = 0
    _strength_gain: float = 0
    _strength: int = 0
    # _spirit_base: int = 0
    # _base_spirit: int = 0
    # _spirit_gain: float = 0
    # _spirit: float = 0
    # _spunk_base: int = 0
    # _base_spunk: int = 0
    # _spunk_gain: float = 0
    # _spunk: float = 0

    _surplus: int = 0

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
    # _magical_attack_power_base: int = 0
    # _base_magical_attack_power: float = 0
    # _magical_attack_power_gain: float = 0
    # _magical_attack_power: float = 0

    _all_critical_strike_base: int = 0
    _all_critical_strike_gain: float = 0

    _physical_critical_strike_base: int = 0
    _base_physical_critical_strike: int = 0
    _physical_critical_strike_percent: float = 0
    _physical_critical_strike_gain: float = 0
    _physical_critical_strike: float = 0

    # _magical_critical_strike_base: int = 0
    # _base_magical_critical_strike: float = 0
    # _magical_critical_strike_percent: float = 0
    # _magical_critical_strike_gain: float = 0
    # _magical_critical_strike: float = 0

    _all_critical_power_gain: float = 0

    _physical_critical_power_base: int = 0
    _physical_critical_power_percent: float = 0
    _physical_critical_power_gain: float = 0
    _physical_critical_power: float = 0

    # _magical_critical_power_base: int = 0
    # _magical_critical_power_percent: float = 0
    # _magical_critical_power_gain: float = 0
    # _magical_critical_power: float = 0

    _physical_overcome_base: int = 0
    _base_physical_overcome: int = 0
    _final_physical_overcome: int = 0
    _physical_overcome_gain: float = 0
    _physical_overcome: float = 0

    # _magical_overcome_base: int = 0
    # _base_magical_overcome: float = 0
    # _final_magical_overcome: float = 0
    # _magical_overcome_gain: float = 0
    # _magical_overcome: float = 0

    weapon_damage_rand: int = 0
    _weapon_damage_base: int = 0
    _weapon_damage_gain: float = 0
    _weapon_damage: int = 0

    physical_shield_ignore_base: float = 0
    # magical_shield_ignore_base: float = 0
    physical_shield_ignore_gain: float = 0
    # magical_shield_ignore_gain: float = 0

    damage_addition: float = 0
    cd_reduction: float = 0
    pve_addition: float = 0

    def __post_init__(self):
        if not self.target:
            self.target = Target()

        self.all_major_base += 41
        # self.grad_scale = {
        #     "agility_base": MAJOR_BASE,
        #     "spunk_base": MAJOR_BASE,
        #     "strength_base": MAJOR_BASE,
        #     "spirit_base": MAJOR_BASE,
        #     "surplus_base": MINOR_BASE,
        #     "strain_base": MINOR_BASE,
        #     # "haste_base": MINOR_BASE,
        #     "physical_attack_power_base": ATTACK_POWER_BASE,
        #     "magical_attack_power_base": ATTACK_POWER_BASE,
        #     "physical_critical_strike_base": MINOR_BASE,
        #     "magical_critical_strike_base": MINOR_BASE,
        #     "physical_critical_power_base": MINOR_BASE,
        #     "magical_critical_power_base": MINOR_BASE,
        #     "physical_overcome_base": MINOR_BASE,
        #     "magical_overcome_base": MINOR_BASE,
        #     "weapon_damage_base": WEAPON_DAMAGE_BASE
        # }
        self.grad_attrs = []

    """ Major Attr Function"""

    @property
    def all_major_base(self):
        return self._all_major_base

    @all_major_base.setter
    def all_major_base(self, all_major_base):
        self._all_major_base = all_major_base
        self.base_agility = self._agility_base + all_major_base
        self.base_strength = self._strength_base + all_major_base
        # self.base_spirit = self._spirit_base + all_major_base
        # self.base_spunk = self._spunk_base + all_major_base

    @property
    def all_major_gain(self):
        return self._all_major_gain

    @all_major_gain.setter
    def all_major_gain(self, all_major_gain):
        self._all_major_gain = all_major_gain
        self.agility = self._base_agility * (1 + self._agility_gain + all_major_gain)
        self.strength = self._base_strength * (1 + self._strength_gain + all_major_gain)
        # self.spirit = self._base_spirit * (1 + self._spirit_gain + all_major_gain)
        # self.spunk = self._base_spunk * (1 + self._spunk_gain + all_major_gain)

    @property
    def agility_base(self):
        return self._agility_base

    @agility_base.setter
    def agility_base(self, agility_base):
        self._agility_base = agility_base
        self.base_agility = agility_base + self._all_major_base

    @property
    def base_agility(self):
        return self._base_agility

    @base_agility.setter
    def base_agility(self, base_agility):
        self._base_agility = base_agility
        self.agility = base_agility * (1 + self._agility_gain + self._all_major_gain)

    @property
    def agility_gain(self):
        return self._agility_gain

    @agility_gain.setter
    def agility_gain(self, agility_gain):
        self._agility_gain = agility_gain
        self.agility = self._base_agility * (1 + agility_gain + self._all_major_gain)

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, agility):
        agility = int(agility)
        self._agility = agility
        self.base_physical_critical_strike = (self._physical_critical_strike_base + self._all_critical_strike_base +
                                              agility * AGILITY_TO_CRITICAL_STRIKE)

    @property
    def strength_base(self):
        return self._strength_base

    @strength_base.setter
    def strength_base(self, strength_base):
        self._strength_base = strength_base
        self.base_strength = strength_base + self._all_major_base

    @property
    def base_strength(self):
        return self._base_strength

    @base_strength.setter
    def base_strength(self, base_strength):
        self._base_strength = base_strength
        self.strength = base_strength * (1 + self._strength_gain + self._all_major_gain)

    @property
    def strength_gain(self):
        return self._strength_gain

    @strength_gain.setter
    def strength_gain(self, strength_gain):
        self._strength_gain = strength_gain
        self.strength = self._base_strength * (1 + strength_gain + self._all_major_gain)

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        strength = int(strength)
        self._strength = strength
        self.base_physical_attack_power = self._physical_attack_power_base + strength * STRENGTH_TO_ATTACK_POWER
        self.base_physical_overcome = self._physical_overcome_base + strength * STRENGTH_TO_OVERCOME

    # @property
    # def spirit_base(self):
    #     return self._spirit_base
    #
    # @spirit_base.setter
    # def spirit_base(self, spirit_base):
    #     self._spirit_base = spirit_base
    #     self.base_spirit = spirit_base + self._all_major_base
    #
    # @property
    # def base_spirit(self):
    #     return self._base_spirit
    #
    # @base_spirit.setter
    # def base_spirit(self, base_spirit):
    #     self._base_spirit = base_spirit
    #     self.spirit = base_spirit * (1 + self._spirit_gain + self._all_major_gain)
    #
    # @property
    # def spirit_gain(self):
    #     return self._spirit_gain
    #
    # @spirit_gain.setter
    # def spirit_gain(self, spirit_gain):
    #     self._spirit_gain = spirit_gain
    #     self.spirit = self._base_spirit * (1 + spirit_gain + self._all_major_gain)
    #
    # @property
    # def spirit(self):
    #     return self._spirit
    #
    # @spirit.setter
    # def spirit(self, spirit):
    #     self._spirit = spirit
    #     self.base_magical_critical_strike = (self._magical_critical_strike_base + self._all_critical_strike_base +
    #                                          spirit * SPIRIT_TO_CRITICAL_STRIKE)
    #
    # @property
    # def spunk_base(self):
    #     return self._spunk_base
    #
    # @spunk_base.setter
    # def spunk_base(self, spunk_base):
    #     self._spunk_base = spunk_base
    #     self.base_spunk = spunk_base + self._all_major_base
    #
    # @property
    # def base_spunk(self):
    #     return self._base_spunk
    #
    # @base_spunk.setter
    # def base_spunk(self, base_spunk):
    #     self._base_spunk = base_spunk
    #     self.spunk = base_spunk * (1 + self._spunk_gain + self._all_major_gain)
    #
    # @property
    # def spunk_gain(self):
    #     return self._spunk_gain
    #
    # @spunk_gain.setter
    # def spunk_gain(self, spunk_gain):
    #     self._spunk_gain = spunk_gain
    #     self.spunk = self._base_spunk * (1 + spunk_gain + self._all_major_gain)
    #
    # @property
    # def spunk(self):
    #     return self._spunk
    #
    # @spunk.setter
    # def spunk(self, spunk):
    #     self._spunk = spunk
    #     self.base_magical_attack_power = self._magical_attack_power_base + spunk * SPUNK_TO_ATTACK_POWER
    #     self.base_magical_overcome = self._magical_overcome_base + spunk * SPUNK_TO_OVERCOME

    """ Minor Function """
    @property
    def surplus(self):
        return self._surplus

    @surplus.setter
    def surplus(self, surplus):
        self._surplus = surplus

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
        base_physical_attack_power = round(base_physical_attack_power)
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

    # @property
    # def magical_attack_power_base(self):
    #     return self._magical_attack_power_base
    #
    # @magical_attack_power_base.setter
    # def magical_attack_power_base(self, magical_attack_power_base):
    #     self._magical_attack_power_base = magical_attack_power_base
    #     self.base_magical_attack_power = magical_attack_power_base + self._spunk * SPUNK_TO_ATTACK_POWER
    #
    # @property
    # def base_magical_attack_power(self):
    #     return self._base_magical_attack_power
    #
    # @base_magical_attack_power.setter
    # def base_magical_attack_power(self, base_magical_attack_power):
    #     self._base_magical_attack_power = base_magical_attack_power
    #     self.magical_attack_power = base_magical_attack_power * (1 + self._magical_attack_power_gain)
    #
    # @property
    # def magical_attack_power_gain(self):
    #     return self._magical_attack_power_gain
    #
    # @magical_attack_power_gain.setter
    # def magical_attack_power_gain(self, magical_attack_power_gain):
    #     self._magical_attack_power_gain = magical_attack_power_gain
    #     self.magical_attack_power = self._base_magical_attack_power * (1 + magical_attack_power_gain)
    #
    # @property
    # def magical_attack_power(self):
    #     return self._magical_attack_power
    #
    # @magical_attack_power.setter
    # def magical_attack_power(self, magical_attack_power):
    #     self._magical_attack_power = magical_attack_power

    """ Critical Strike Function"""

    @property
    def all_critical_strike_base(self):
        return self._all_critical_strike_base

    @all_critical_strike_base.setter
    def all_critical_strike_base(self, all_critical_strike_base):
        self._all_critical_strike_base = all_critical_strike_base
        self.base_physical_critical_strike = (self._physical_critical_strike_base + all_critical_strike_base +
                                              self._agility * AGILITY_TO_CRITICAL_STRIKE)
        # self.magical_critical_strike_base = (self._magical_critical_strike_base + all_critical_strike_base +
        #                                      self._spirit * SPIRIT_TO_CRITICAL_STRIKE)

    @property
    def all_critical_strike_gain(self):
        return self._all_critical_strike_base

    @all_critical_strike_gain.setter
    def all_critical_strike_gain(self, all_critical_strike_gain):
        self._all_critical_strike_gain = all_critical_strike_gain
        self.physical_critical_strike = (self._physical_critical_strike_percent + self._physical_critical_strike_gain +
                                         all_critical_strike_gain)
        # self.magical_critical_strike = (self._magical_critical_strike_percent + self._magical_critical_strike_gain +
        #                                 all_critical_strike_gain)

    @property
    def physical_critical_strike_base(self):
        return self._physical_critical_strike_base

    @physical_critical_strike_base.setter
    def physical_critical_strike_base(self, physical_critical_strike_base):
        self._physical_critical_strike_base = physical_critical_strike_base
        self.base_physical_critical_strike = (physical_critical_strike_base + self._all_critical_strike_base +
                                              self._agility * AGILITY_TO_CRITICAL_STRIKE)

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
        self.physical_critical_strike = (physical_critical_strike_percent + self._physical_critical_strike_gain +
                                         self._all_critical_strike_gain)

    @property
    def physical_critical_strike_gain(self):
        return self._physical_critical_strike_gain

    @physical_critical_strike_gain.setter
    def physical_critical_strike_gain(self, physical_critical_strike_gain):
        self._physical_critical_strike_gain = physical_critical_strike_gain
        self.physical_critical_strike = (self._physical_critical_strike_percent + physical_critical_strike_gain +
                                         self._all_critical_strike_gain)

    @property
    def physical_critical_strike(self):
        return self._physical_critical_strike

    @physical_critical_strike.setter
    def physical_critical_strike(self, physical_critical_strike):
        self._physical_critical_strike = physical_critical_strike

    # @property
    # def magical_critical_strike_base(self):
    #     return self._magical_critical_strike_base
    #
    # @magical_critical_strike_base.setter
    # def magical_critical_strike_base(self, magical_critical_strike_base):
    #     self._magical_critical_strike_base = magical_critical_strike_base
    #     self.base_magical_critical_strike = (magical_critical_strike_base + self._all_critical_strike_base +
    #                                          self._spirit * SPIRIT_TO_CRITICAL_STRIKE)
    #
    # @property
    # def base_magical_critical_strike(self):
    #     return self._base_magical_critical_strike
    #
    # @base_magical_critical_strike.setter
    # def base_magical_critical_strike(self, base_magical_critical_strike):
    #     self._base_magical_critical_strike = base_magical_critical_strike
    #     self.magical_critical_strike_percent = base_magical_critical_strike / CRITICAL_STRIKE_SCALE
    #
    # @property
    # def magical_critical_strike_percent(self):
    #     return self._magical_critical_strike_percent
    #
    # @magical_critical_strike_percent.setter
    # def magical_critical_strike_percent(self, magical_critical_strike_percent):
    #     self._magical_critical_strike_percent = magical_critical_strike_percent
    #     self.magical_critical_strike = (magical_critical_strike_percent + self._magical_critical_strike_gain +
    #                                     self._all_critical_strike_gain)
    #
    # @property
    # def magical_critical_strike_gain(self):
    #     return self._magical_critical_strike_gain
    #
    # @magical_critical_strike_gain.setter
    # def magical_critical_strike_gain(self, magical_critical_strike_gain):
    #     self._magical_critical_strike_gain = magical_critical_strike_gain
    #     self.magical_critical_strike = (self._magical_critical_strike_percent + magical_critical_strike_gain +
    #                                     self._all_critical_strike_gain)
    #
    # @property
    # def magical_critical_strike(self):
    #     return self._magical_critical_strike
    #
    # @magical_critical_strike.setter
    # def magical_critical_strike(self, magical_critical_strike):
    #     self._magical_critical_strike = magical_critical_strike

    """ Critical Power Function"""

    @property
    def all_critical_power_gain(self):
        return self._all_critical_power_gain

    @all_critical_power_gain.setter
    def all_critical_power_gain(self, all_critical_power_gain):
        self._all_critical_power_gain = all_critical_power_gain
        self.physical_critical_power = (self._physical_critical_power_percent + self._physical_critical_power_gain +
                                        all_critical_power_gain)
        # self.magical_critical_power = (self._magical_critical_power_percent + self._magical_critical_power_gain +
        #                                all_critical_power_gain)

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
        self.physical_critical_power = (physical_critical_power_percent + self._physical_critical_power_gain +
                                        self._all_critical_power_gain)

    @property
    def physical_critical_power_gain(self):
        return self._physical_critical_power_gain

    @physical_critical_power_gain.setter
    def physical_critical_power_gain(self, physical_critical_power_gain):
        self._physical_critical_power_gain = physical_critical_power_gain
        self.physical_critical_power = (self._physical_critical_power_percent + physical_critical_power_gain +
                                        self._all_critical_power_gain)

    @property
    def physical_critical_power(self):
        return self._physical_critical_power

    @physical_critical_power.setter
    def physical_critical_power(self, physical_critical_power):
        self._physical_critical_power = physical_critical_power

    # @property
    # def magical_critical_power_base(self):
    #     return self._magical_critical_power_base
    #
    # @magical_critical_power_base.setter
    # def magical_critical_power_base(self, magical_critical_power_base):
    #     self._magical_critical_power_base = magical_critical_power_base
    #     self.magical_critical_power_percent = CRITICAL_POWER_BASE + magical_critical_power_base / CRITICAL_POWER_SCALE
    #
    # @property
    # def magical_critical_power_percent(self):
    #     return self._magical_critical_power_percent
    #
    # @magical_critical_power_percent.setter
    # def magical_critical_power_percent(self, magical_critical_power_percent):
    #     self._magical_critical_power_percent = magical_critical_power_percent
    #     self.magical_critical_power = (magical_critical_power_percent + self._magical_critical_power_gain +
    #                                    self._all_critical_power_gain)
    #
    # @property
    # def magical_critical_power_gain(self):
    #     return self._magical_critical_power_gain
    #
    # @magical_critical_power_gain.setter
    # def magical_critical_power_gain(self, magical_critical_power_gain):
    #     self._magical_critical_power_gain = magical_critical_power_gain
    #     self.magical_critical_power = (self._magical_critical_power_percent + magical_critical_power_gain +
    #                                    self._all_critical_power_gain)
    #
    # @property
    # def magical_critical_power(self):
    #     return self._magical_critical_power
    #
    # @magical_critical_power.setter
    # def magical_critical_power(self, magical_critical_power):
    #     self._magical_critical_power = magical_critical_power

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

    # @property
    # def magical_overcome_base(self):
    #     return self._magical_overcome_base
    #
    # @magical_overcome_base.setter
    # def magical_overcome_base(self, magical_overcome_base):
    #     self._magical_overcome_base = magical_overcome_base
    #     self.base_magical_overcome = magical_overcome_base + self._spunk * SPUNK_TO_OVERCOME
    #
    # @property
    # def base_magical_overcome(self):
    #     return self._base_magical_overcome
    #
    # @base_magical_overcome.setter
    # def base_magical_overcome(self, base_magical_overcome):
    #     self._base_magical_overcome = base_magical_overcome
    #     self.final_magical_overcome = base_magical_overcome * (1 + self._magical_overcome_gain)
    #
    # @property
    # def magical_overcome_gain(self):
    #     return self._magical_overcome_gain
    #
    # @magical_overcome_gain.setter
    # def magical_overcome_gain(self, magical_overcome_gain):
    #     self._magical_overcome_gain = magical_overcome_gain
    #     self.final_magical_overcome = self._base_magical_overcome * (1 + magical_overcome_gain)
    #
    # @property
    # def final_magical_overcome(self):
    #     return self._final_magical_overcome
    #
    # @final_magical_overcome.setter
    # def final_magical_overcome(self, final_magical_overcome):
    #     self._final_magical_overcome = final_magical_overcome
    #     self.magical_overcome = final_magical_overcome / OVERCOME_SCALE
    #
    # @property
    # def magical_overcome(self):
    #     return self._magical_overcome
    #
    # @magical_overcome.setter
    # def magical_overcome(self, magical_overcome):
    #     self._magical_overcome = magical_overcome

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

    @cached_property
    def level_reduction(self):
        return LEVEL_REDUCTION * (self.target.level - self.level)

