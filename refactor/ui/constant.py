from general.gains import equipment

import bei_ao_jue

""" Directory """
EQUIPMENTS_DIR = "ui/assets/equipments.json"
ENCHANTS_DIR = "ui/assets/enchants.json"
STONES_DIR = "ui/assets/stones.json"

""" Attrs """
ATTR_TYPE_TRANSLATE = {
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "strength_base": "力道",
    "physical_attack_power_base": "外功攻击",
    "physical_critical_strike_base": "外功会心",
    "all_critical_strike_base": "全会心",
    "physical_critical_power_base": "外功会效",
    "physical_overcome_base": "外功破防",
    "strain_base": "无双",
    "haste_base": "加速",
    "surplus": "破招",
}

""" Top """
CLASSES = ["少林", "万花", "天策", "纯阳", "七秀", ]
SUPPORT_CLASS = {
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
        "simulator": {
            "prepare":  bei_ao_jue.prepare,
            "priority": bei_ao_jue.priority,
            "loop": bei_ao_jue.loop
        },
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
    **bei_ao_jue.EQUIP_GAINS_NAME
}
EQUIP_GAINS = {
    **equipment.EQUIP_GAINS,
    **bei_ao_jue.EQUIP_GAINS
}

""" Talent """
MAX_TALENTS = 12

TALENT_GAINS = {
    **bei_ao_jue.TALENT_GAINS
}

""" Recipes """
MAX_RECIPE_SKILLS = 6
MAX_RECIPES = 4

RECIPE_GAINS = {
    **bei_ao_jue.RECIPE_GAINS
}
