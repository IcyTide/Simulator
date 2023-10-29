POSITION_MAP = {
    "帽子": "hat",
    "上衣": "jacket",
    "腰带": "belt",
    "护腕": "wrist",
    "下装": "bottoms",
    "鞋子": "shoes",
    "项链": "necklace",
    "腰坠": "pendant",
    "戒指1": "ring",
    "戒指2": "ring",
    "远程武器": "tertiary_weapon",
    "近战武器": "primary_weapon"
}
ATTR_TYPE_MAP = {
    "atMeleeWeaponDamageBase": "weapon_damage_base",
    "atMeleeWeaponDamageRand": "weapon_damage_rand",
    "atStrengthBase": "strength_base",
    "atPhysicsAttackPowerBase": "physical_attack_power_gain",
    "atPhysicsOvercomeBase": "physical_overcome_base",
    "atPhysicsCriticalStrike": "physical_critical_strike_base",
    "atPhysicsCriticalDamagePowerBase": "physical_critical_damage_base",
    "atHasteBase": "haste_base",
    "atSurplusValueBase": "surplus_base",
    "atStrainBase": "strain_base"
}
ATTR_MAP = {
    "Overcome": "破防",
    "Critical": "会心",
    "CriticalDamage": "会效",
    "Haste": "加速",
    "Surplus": "破招",
    "Strain": "无双"
}
MAX_EMBED_NUMBER = 3
MAX_EMBED_LEVEL = 8


def EMBED_COF(level):
    if level > 6:
        return (level * 0.65 - 3.2) * 1.3
    else:
        level * 0.195


def STRENGTH_COF(level):
    return level * (0.7 + 0.3 * level) / 200

