import os

from general.gains import equipment

from schools import wen_shui_jue, bei_ao_jue, bing_xin_jue, yi_jin_jing, ao_xue_zhan_yi, gu_feng_jue, fen_ying_sheng_jue

""" Directory """
# ASSETS_DIR = os.path.join(os.getcwd(), "qt/assets")
ASSETS_DIR = "qt/assets"
EQUIPMENTS_DIR = os.path.join(ASSETS_DIR, "equipments")
ENCHANTS_DIR = os.path.join(ASSETS_DIR, "enchants")
STONES_DIR = os.path.join(ASSETS_DIR, "stones.json")

""" Equipments """
POSITION_MAP = {
    '帽子': 'hat',
    '上衣': 'jacket',
    '腰带': 'belt',
    '护腕': 'wrist',
    '下装': 'bottoms',
    '鞋子': 'shoes',
    '项链': 'necklace',
    '腰坠': 'pendant',
    '戒指1': 'ring',
    '戒指2': 'ring',
    '远程武器': 'tertiary_weapon',
    '近战武器': 'primary_weapon',
    '额外武器': 'secondary_weapon'
}
STONES_POSITIONS = ["primary_weapon", 'secondary_weapon']
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
    "primary_weapon": 3,
    "secondary_weapon": 3
}
SPECIAL_ENCHANT_POSITIONS = ["hat", "jacket", "belt", "wrist", "shoes"]
""" Attrs """
ATTR_TYPE_MAP = {
    "atMeleeWeaponDamageBase": "weapon_damage_base",
    "atMeleeWeaponDamageRand": "weapon_damage_rand",
    "atBasePotentialAdd": "all_major_base",
    "atAgilityBase": "agility_base",
    "atStrengthBase": "strength_base",
    "atSpiritBase": "spirit_base",
    "atSpunkBase": "spunk_base",
    "atPhysicsAttackPowerBase": "physical_attack_power_base",
    "atMagicAttackPowerBase": "magical_attack_power_base",
    "atLunarAttackPowerBase": "magical_attack_power_base",
    "atSolarAttackPowerBase": "magical_attack_power_base",
    "atSolarAndLunarAttackPowerBase": "magical_attack_power_base",
    "atPhysicsOvercomeBase": "physical_overcome_base",
    "atMagicOvercome": "magical_overcome_base",
    "atLunarOvercomeBase": "magical_overcome_base",
    "atSolarOvercomeBase": "magical_overcome_base",
    "atSolarAndLunarOvercomeBase": "magical_overcome_base",
    "atAllTypeCriticalStrike": "all_critical_strike_base",
    "atPhysicsCriticalStrike": "physical_critical_strike_base",
    "atMagicCriticalStrike": "magical_critical_strike_base",
    "atLunarCriticalStrike": "magical_critical_strike_base",
    "atSolarCriticalStrike": "magical_critical_strike_base",
    "atSolarAndLunarCriticalStrike": "magical_critical_strike_base",
    "atAllTypeCriticalDamagePowerBase": "all_critical_power_base",
    "atPhysicsCriticalDamagePowerBase": "physical_critical_power_base",
    "atMagicCriticalDamagePowerBase": "magical_critical_power_base",
    "atLunarCriticalDamagePowerBase": "magical_critical_power_base",
    "atSolarCriticalDamagePowerBase": "magical_critical_power_base",
    "atSolarAndLunarCriticalDamagePowerBase": "magical_critical_power_base",
    "atSurplusValueBase": "surplus",
    "atStrainBase": "strain_base",
    "atHasteBase": "haste_base",
}
ATTR_TYPE_TRANSLATE = {
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "all_major_base": "全属性",
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
    "atAgilityBase", "atStrengthBase", "atSpiritBase", "atSpunkBase",
    "atPhysicsAttackPowerBase", "atPhysicsCriticalStrike",
    "atPhysicsCriticalDamagePowerBase", "atPhysicsOvercomeBase",
    "atMagicAttackPowerBase", "atMagicCriticalStrike",
    "atMagicCriticalDamagePowerBase", "atMagicOvercome"
]

""" Top """
SUPPORT_SCHOOL = {
    "问水诀": {
        "school": "藏剑",
        "major": "身法",
        "kind": "外功",
        "attribute": wen_shui_jue.WenShuiJue,
        "formation": "依山观澜阵",
        "talents": wen_shui_jue.TALENTS,
        "recipes": wen_shui_jue.RECIPES,
        "skills": wen_shui_jue.SKILLS,
        "buffs": wen_shui_jue.BUFFS,
        "initiation": wen_shui_jue.initiation,
        "prepare": wen_shui_jue.prepare,
        "priority": wen_shui_jue.priority,
        "loop": wen_shui_jue.loop,
        "display_attrs": {
            "agility": "身法",
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
        "initiation": bei_ao_jue.initiation,
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
        "formation": "九音惊弦阵",
        "talents": bing_xin_jue.TALENTS,
        "recipes": bing_xin_jue.RECIPES,
        "skills": bing_xin_jue.SKILLS,
        "buffs": bing_xin_jue.BUFFS,
        "initiation": bing_xin_jue.initiation,
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
    },
    "易筋经": {
        "school": "少林",
        "major": "元气",
        "kind": "内功",
        "attribute": yi_jin_jing.YiJinJing,
        "formation": "天鼓雷音阵",
        "talents": yi_jin_jing.TALENTS,
        "recipes": yi_jin_jing.RECIPES,
        "skills": yi_jin_jing.SKILLS,
        "buffs": yi_jin_jing.BUFFS,
        "initiation": yi_jin_jing.initiation,
        "prepare": yi_jin_jing.prepare,
        "priority": yi_jin_jing.priority,
        "loop": yi_jin_jing.loop,
        "display_attrs": {
            "spunk": "元气",
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
    },
    "傲血战意": {
        "school": "天策",
        "major": "力道",
        "kind": "外功",
        "attribute": ao_xue_zhan_yi.AoXueZhanYi,
        "formation": "卫公折冲阵",
        "talents": ao_xue_zhan_yi.TALENTS,
        "recipes": ao_xue_zhan_yi.RECIPES,
        "skills": ao_xue_zhan_yi.SKILLS,
        "buffs": ao_xue_zhan_yi.BUFFS,
        "initiation": ao_xue_zhan_yi.initiation,
        "prepare": ao_xue_zhan_yi.prepare,
        "priority": ao_xue_zhan_yi.priority,
        "loop": ao_xue_zhan_yi.loop,
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
    "孤锋诀": {
        "school": "刀宗",
        "major": "力道",
        "kind": "外功",
        "attribute": gu_feng_jue.GuFengJue,
        "formation": "横云破锋阵",
        "talents": gu_feng_jue.TALENTS,
        "recipes": gu_feng_jue.RECIPES,
        "skills": gu_feng_jue.SKILLS,
        "buffs": gu_feng_jue.BUFFS,
        "initiation": gu_feng_jue.initiation,
        "prepare": gu_feng_jue.prepare,
        "priority": gu_feng_jue.priority,
        "loop": gu_feng_jue.loop,
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
    "焚影圣诀": {
        "school": "明教",
        "major": "元气",
        "kind": "内功",
        "attribute": fen_ying_sheng_jue.FenYingShengJue,
        "formation": "炎威破魔阵",
        "talents": fen_ying_sheng_jue.TALENTS,
        "recipes": fen_ying_sheng_jue.RECIPES,
        "skills": fen_ying_sheng_jue.SKILLS,
        "buffs": fen_ying_sheng_jue.BUFFS,
        "initiation": fen_ying_sheng_jue.initiation,
        "prepare": fen_ying_sheng_jue.prepare,
        "priority": fen_ying_sheng_jue.priority,
        "loop": fen_ying_sheng_jue.loop,
        "display_attrs": {
            "spunk": "元气",
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
    },
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


EQUIP_GAINS_NAME = {
    **equipment.EQUIP_GAINS_NAME,
    **wen_shui_jue.EQUIP_GAINS_NAME,
    **bei_ao_jue.EQUIP_GAINS_NAME,
    **bing_xin_jue.EQUIP_GAINS_NAME,
    **yi_jin_jing.EQUIP_GAINS_NAME,
    **ao_xue_zhan_yi.EQUIP_GAINS_NAME,
    **gu_feng_jue.EQUIP_GAINS_NAME,
    **fen_ying_sheng_jue.EQUIP_GAINS_NAME
}
EQUIP_GAINS = {
    **equipment.EQUIP_GAINS,
    **wen_shui_jue.EQUIP_GAINS,
    **bei_ao_jue.EQUIP_GAINS,
    **bing_xin_jue.EQUIP_GAINS,
    **yi_jin_jing.EQUIP_GAINS,
    **ao_xue_zhan_yi.EQUIP_GAINS,
    **gu_feng_jue.EQUIP_GAINS,
    **fen_ying_sheng_jue.EQUIP_GAINS
}

""" Talent """
MAX_TALENTS = 12

TALENT_GAINS = {
    **wen_shui_jue.TALENT_GAINS,
    **bei_ao_jue.TALENT_GAINS,
    **bing_xin_jue.TALENT_GAINS,
    **yi_jin_jing.TALENT_GAINS,
    **ao_xue_zhan_yi.TALENT_GAINS,
    **gu_feng_jue.TALENT_GAINS,
    **fen_ying_sheng_jue.TALENT_GAINS
}

""" Recipes """
MAX_RECIPE_SKILLS = 12
MAX_RECIPES = 4

RECIPE_GAINS = {
    **wen_shui_jue.RECIPE_GAINS,
    **bei_ao_jue.RECIPE_GAINS,
    **bing_xin_jue.RECIPE_GAINS,
    **yi_jin_jing.RECIPE_GAINS,
    **ao_xue_zhan_yi.RECIPE_GAINS,
    **gu_feng_jue.RECIPE_GAINS,
    **fen_ying_sheng_jue.RECIPE_GAINS
}
