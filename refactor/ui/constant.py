POSITION_TRANSLATE = {
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
    "atStrengthBase": "strength_base",
    "atSurplusValueBase": "surplus_base",
    "atStrainBase": "strain_base",
    "atHasteBase": "haste_base",
    "atPhysicsAttackPowerBase": "physical_attack_power_base",
    "atPhysicsOvercomeBase": "physical_overcome_base",
    "atPhysicsCriticalStrike": "physical_critical_strike_base",
    "atPhysicsCriticalDamagePowerBase": "physical_critical_damage_base",
    "atMeleeWeaponDamageBase": "weapon_damage_base",
    "atMeleeWeaponDamageRand": "weapon_damage_rand"
}
ATTR_TYPE_REVERSE = {v: k for k, v in ATTR_TYPE_MAP.items()}
ATTR_TYPE_TRANSLATE = {
    "strength_base": "力道",
    "surplus_base": "破招",
    "strain_base": "无双",
    "haste_base": "加速",
    "physical_attack_power_base": "外功攻击",
    "physical_critical_strike_base": "外功会心",
    "physical_critical_damage_base": "外功会效",
    "physical_overcome_base": "外功破防",
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害"
}
ATTR_TYPE_TRANSLATE_REVERSE = {v: k for k, v in ATTR_TYPE_TRANSLATE.items()}

ATTR_MAP = {
    "Overcome": "破防",
    "Critical": "会心",
    "CriticalDamage": "会效",
    "Haste": "加速",
    "Surplus": "破招",
    "Strain": "无双"
}

ATTRIBUTE_MAP = {
    "strength": "力道",
    "surplus": "破招",
    "base_strain": "无双等级",
    "strain": "无双",
    "base_haste": "加速等级",
    "haste": "加速",
    "base_physical_attack_power": "基础外功攻击",
    "physical_attack_power": "外功攻击",
    "base_physical_critical_strike": "外功会心等级",
    "physical_critical_strike": "外功会心",
    "base_physical_critical_damage": "外功会效等级",
    "physical_critical_damage": "外功会效",
    "base_physical_overcome": "外功破防等级",
    "physical_overcome": "外功破防",
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害"
}
MAX_EMBED_ATTR = 3
MAX_BASE_ATTR = 6
MAX_MAGIC_ATTR = 12
MAX_ENCHANT_ATTR = 4
MAX_STONE_ATTR = 3

MAX_EMBED_LEVEL = 8
MAX_STRENGTH_LEVEL = 8
MAX_STONE_LEVEL = 6

EQUIPMENTS_DIR = "assets/equipments"
ENCHANTS_DIR = "assets/enchants"
STONES_DIR = "assets/stones.json"

SPECIAL_ENCHANT_POSITIONS = ["hat", "jacket", "belt", "wrist", "shoes"]
STONE_POSITIONS = ["primary_weapon"]

BASE_ATTR = {

}


def EMBED_COF(level):
    if level > 6:
        return (level * 0.65 - 3.2) * 1.3
    else:
        return level * 0.195


def STRENGTH_COF(level):
    return level * (0.7 + 0.3 * level) / 200
