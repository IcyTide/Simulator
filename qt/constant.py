import os

from general.gains import equipment

from schools import bei_ao_jue
from schools import bing_xin_jue

""" Directory """
# ASSETS_DIR = os.path.join(os.getcwd(), "qt/assets")
ASSETS_DIR = "qt/assets"
EQUIPMENTS_DIR = os.path.join(ASSETS_DIR, "equipments")
ENCHANTS_DIR = os.path.join(ASSETS_DIR, "enchants")
STONES_DIR = os.path.join(ASSETS_DIR, "stones.json")

""" Equipments """
POSITION_MAP = {
    "hat": "hat",
    "jacket": "jacket",
    "belt": "belt",
    "wrist": "wrist",
    "bottoms": "bottoms",
    "shoes": "shoes",
    "necklace": "necklace",
    "pendant": "pendant",
    "ring_1": "ring",
    "ring_2": "ring",
    "tertiary_weapon": "tertiary_weapon",
    "primary_weapon": "primary_weapon"
}
STONES_POSITIONS = ["primary_weapon"]
EMBED_POSITIONS = {
    "hat": 2,
    "jacket": 2,
    "belt": 2,
    "wrist": 2,
    "bottoms": 2,
    "shoes": 2,
    "necklace": 1,
    "pendant": 1,
    "ring": 0,
    "tertiary_weapon": 1,
    "primary_weapon": 3
}
SPECIAL_ENCHANT_POSITIONS = ["hat", "jacket", "belt", "wrist", "shoes"]
""" Attrs """
ATTR_TYPE_MAP = {
    "atMeleeWeaponDamageBase": "weapon_damage_base",
    "atMeleeWeaponDamageRand": "weapon_damage_rand",
    "atStrengthBase": "strength_base",
    "atSpiritBase": "spirit_base",
    "atPhysicsAttackPowerBase": "physical_attack_power_base",
    "atMagicAttackPowerBase": "magical_attack_power_base",
    "atLunarAttackPowerBase": "magical_attack_power_base",
    "atPhysicsOvercomeBase": "physical_overcome_base",
    "atMagicOvercome": "magical_overcome_base",
    "atLunarOvercomeBase": "magical_overcome_base",
    "atAllTypeCriticalStrike": "all_critical_strike_base",
    "atPhysicsCriticalStrike": "physical_critical_strike_base",
    "atMagicCriticalStrike": "magical_critical_strike_base",
    "atLunarCriticalStrike": "magical_critical_strike_base",
    "atAllTypeCriticalDamagePowerBase": "all_critical_power_base",
    "atPhysicsCriticalDamagePowerBase": "physical_critical_power_base",
    "atMagicCriticalDamagePowerBase": "magical_critical_power_base",
    "atLunarCriticalDamagePowerBase": "magical_critical_power_base",
    "atSurplusValueBase": "surplus",
    "atStrainBase": "strain_base",
    "atHasteBase": "haste_base",
}
ATTR_TYPE_TRANSLATE = {
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "agility_base": "身法",
    "strength_base": "力道",
    "spirit_base": "根骨",
    "spunk_base": "元气",
    "physical_attack_power_base": "外功攻击",
    "magical_attack_power_base": "内功攻击",
    "physical_critical_strike_base": "外功会心",
    "magical_critical_strike_base": "内功会心",
    "all_critical_strike_base": "全会心",
    "physical_critical_power_base": "外功会效",
    "magical_critical_power_base": "内功会效",
    "all_critical_power_base": "全会效",
    "physical_overcome_base": "外功破防",
    "magical_overcome_base": "内功破防",
    "surplus": "破招",
    "strain_base": "无双",
    "haste_base": "加速",
}
ATTR_TYPE_TRANSLATE_REVERSE = {v: k for k, v in ATTR_TYPE_TRANSLATE.items()}

STONE_ATTR = [
    "atMeleeWeaponDamageBase", "atSurplusValueBase", "atStrainBase", "atHasteBase",
    "atAllTypeCriticalStrike", "atAllTypeCriticalDamagePowerBase",
    "atStrengthBase", "atSpiritBase",
    "atPhysicsAttackPowerBase", "atPhysicsCriticalStrike",
    "atPhysicsCriticalDamagePowerBase", "atPhysicsOvercomeBase",
    "atMagicAttackPowerBase", "atMagicCriticalStrike",
    "atMagicCriticalDamagePowerBase", "atMagicOvercome"
]
STONE_ATTR_MAP = {
    "通用": [
        "weapon_damage_base", "surplus", "strain_base", "haste_base",
        "all_critical_strike_base", "all_critical_power_base"
    ],
    "力道": ["strength_base"],
    "根骨": ["spirit_base"],
    "外功": [
        "physical_attack_power_base", "physical_critical_strike_base",
        "physical_critical_power_base", "physical_overcome_base"
    ],
    "内功": [
        "magical_attack_power_base", "magical_critical_strike_base",
        "magical_critical_power_base", "magical_overcome_base"
    ],
}
""" Top """
SUPPORT_SCHOOL = {
    "北傲诀": {
        "school": "霸刀",
        "major": "力道",
        "kind": "外功",
        "attribute": bei_ao_jue.BeiAoJue,
        "formation": "霜岚洗锋阵",
        "talents": bei_ao_jue.TALENTS,
        "recipes": bei_ao_jue.RECIPES,
        "skills": bei_ao_jue.SKILLS,
        "buffs": bei_ao_jue.BUFFS,
        "prepare": bei_ao_jue.prepare,
        "priority": bei_ao_jue.priority,
        "loop": bei_ao_jue.loop,
        "display_attrs": {
            "strength": "力道",
            "base_physical_attack_power": "基础攻击",
            "physical_attack_power": "攻击",
            "base_physical_critical_strike": "会心等级",
            "physical_critical_strike": "会心",
            "physical_critical_power_base": "会效等级",
            "physical_critical_power": "会效",
            "base_physical_overcome": "基础破防",
            "final_physical_overcome": "最终破防",
            "physical_overcome": "破防",
            "weapon_damage_base": "基础武器伤害",
            "weapon_damage_rand": "浮动武器伤害",
            "strain_base": "无双等级",
            "strain": "无双",
            "haste_base": "加速等级",
            "haste": "加速",
            "surplus": "破招",
        }
    },
    "冰心诀": {
        "school": "七秀",
        "major": "根骨",
        "kind": "内功",
        "attribute": bing_xin_jue.BingXinJue,
        "formation": "霜岚洗锋阵",
        "talents": bing_xin_jue.TALENTS,
        "recipes": bing_xin_jue.RECIPES,
        "skills": bing_xin_jue.SKILLS,
        "buffs": bing_xin_jue.BUFFS,
        "prepare": bing_xin_jue.prepare,
        "priority": bing_xin_jue.priority,
        "loop": bing_xin_jue.loop,
        "display_attrs": {
            "spirit": "根骨",
            "base_magical_attack_power": "基础攻击",
            "magical_attack_power": "攻击",
            "base_magical_critical_strike": "会心等级",
            "magical_critical_strike": "会心",
            "magical_critical_power_base": "会效等级",
            "magical_critical_power": "会效",
            "base_magical_overcome": "基础破防",
            "final_magical_overcome": "最终破防",
            "magical_overcome": "破防",
            "weapon_damage_base": "基础武器伤害",
            "weapon_damage_rand": "浮动武器伤害",
            "strain_base": "无双等级",
            "strain": "无双",
            "haste_base": "加速等级",
            "haste": "加速",
            "surplus": "破招",
        }
    }
}

""" Equip """

MAX_EMBED_ATTR = 3
MAX_BASE_ATTR = 6
MAX_MAGIC_ATTR = 12
MAX_ENCHANT_ATTR = 4
MAX_STONE_ATTR = 3

MAX_EMBED_LEVEL = 8
MAX_STRENGTH_LEVEL = 8
MAX_STONE_LEVEL = 6


def EMBED_COF(level):
    if level > 6:
        return (level * 0.65 - 3.2) * 1.3
    else:
        return level * 0.195


def STRENGTH_COF(level):
    return level * (0.7 + 0.3 * level) / 200


STONE_POSITIONS = ["近战武器"]

EQUIP_GAINS_NAME = {
    **equipment.EQUIP_GAINS_NAME,
    **bei_ao_jue.EQUIP_GAINS_NAME,
    **bing_xin_jue.EQUIP_GAINS_NAME,
}
EQUIP_GAINS = {
    **equipment.EQUIP_GAINS,
    **bei_ao_jue.EQUIP_GAINS,
    **bing_xin_jue.EQUIP_GAINS,
}

""" Talent """
MAX_TALENTS = 12

TALENT_GAINS = {
    **bei_ao_jue.TALENT_GAINS,
    **bing_xin_jue.TALENT_GAINS,
}

""" Recipes """
MAX_RECIPE_SKILLS = 6
MAX_RECIPES = 4

RECIPE_GAINS = {
    **bei_ao_jue.RECIPE_GAINS,
    **bing_xin_jue.RECIPE_GAINS,
}
