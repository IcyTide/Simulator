from bei_ao_jue.gains import attribute_set_gain, dao_xiao_set_gain, shang_jiang_set_gain, dao_xiao_divine_gain, \
    water_weapon_gain, xiang_wang_divine_gain, divine_effect, shang_jiang_divine_gain, wind_pendant_gain
from general.gains import special_enchant_hat_gain, special_enchant_jacket_gain, special_enchant_belt_gain, \
    special_enchant_wrist_gain, special_enchant_shoes_gain

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
    "atMeleeWeaponDamageBase": "weapon_damage_base",
    "atMeleeWeaponDamageRand": "weapon_damage_rand",
    "atStrengthBase": "strength_base",
    "atPhysicsAttackPowerBase": "physical_attack_power_base",
    "atPhysicsOvercomeBase": "physical_overcome_base",
    "atAllTypeCriticalStrike": "all_critical_strike_base",
    "atPhysicsCriticalStrike": "physical_critical_strike_base",
    "atPhysicsCriticalDamagePowerBase": "physical_critical_power_base",
    "atStrainBase": "strain_base",
    "atHasteBase": "haste_base",
    "atSurplusValueBase": "surplus",
}
ATTR_TYPE_REVERSE = {v: k for k, v in ATTR_TYPE_MAP.items()}
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
ATTR_TYPE_TRANSLATE_REVERSE = {v: k for k, v in ATTR_TYPE_TRANSLATE.items()}

EQUIP_ATTR_MAP = {
    "Overcome": "破防",
    "Critical": "会心",
    "CriticalDamage": "会效",
    "Haste": "加速",
    "Surplus": "破招",
    "Strain": "无双"
}
STONE_ATTR_MAP = {
    "atStrengthBase": "力道",
    "atPhysicsAttackPowerBase": "攻击",
    "atPhysicsCriticalStrike": "会心",
    "atAllTypeCriticalStrike": "会心",
    "atPhysicsCriticalDamagePowerBase": "会效",
    "atPhysicsOvercomeBase": "破防",
    "atMeleeWeaponDamageBase": "武器伤害",
    "atStrainBase": "无双",
    "atHasteBase": "加速",
    "atSurplusValueBase": "破招",
}

ATTRIBUTE_MAP = {
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "strength": "力道",
    "base_physical_attack_power": "基础外功攻击",
    "physical_attack_power": "外功攻击",
    "base_physical_critical_strike": "外功会心等级",
    "physical_critical_strike": "外功会心",
    "physical_critical_power_base": "外功会效等级",
    "physical_critical_power": "外功会效",
    "base_physical_overcome": "基础外功破防",
    "final_physical_overcome": "最终外功破防",
    "physical_overcome": "外功破防",
    "strain_base": "无双等级",
    "strain": "无双",
    "haste_base": "加速等级",
    "haste": "加速",
    "surplus": "破招",
}
MAX_EMBED_ATTR = 3
MAX_BASE_ATTR = 6
MAX_MAGIC_ATTR = 12
MAX_ENCHANT_ATTR = 4
MAX_STONE_ATTR = 3

MAX_EMBED_LEVEL = 8
MAX_STRENGTH_LEVEL = 8
MAX_STONE_LEVEL = 6

EQUIPMENTS_DIR = "ui/assets/equipments.json"
ENCHANTS_DIR = "ui/assets/enchants.json"
STONES_DIR = "ui/assets/stones.json"
EQUIPS_CONFIG_DIR = "ui/config/equips.json"

STONE_POSITIONS = ["primary_weapon"]
WIND_PENDANT_SKILL_ID = "6800"


SPECIAL_ENCHANT_MAP = {
    "hat": {
        12800: "15436-11",
        11500: "15436-10",
        10600: "15436-9"
    },
    "jacket": {
        12800: "22151-11",
        11500: "22151-10",
        10600: "22151-9"
    },
    "belt": {
        0: "22169"
    },
    "wrist": {
        0: "22166"
    },
    "shoes": {
        0: "33247"
    },
}

GAINS_TRANSLATE = {
    "1925": "朔气4%套装",
    "4290": "刀啸风吟10%套装",
    "4291": "上将军印10%套装",
    "2401": "水特效 67 基础",
    "2498": "水特效 88 基础",
    "2540": "水特效 98 基础",
    "15436-9": "大附魔头 822 破防",
    "15436-10": "大附魔头 999 破防",
    "15436-11": "大附魔头 1098 破防",
    "22151-9": "大附魔衣 371 基础",
    "22151-10": "大附魔衣 450 基础",
    "22151-11": "大附魔衣 495 基础",
    "22169": "大附魔腰",
    "22166": "大附魔手",
    "33247": "大附魔脚",
    "6800-102": "风特效 6408 破防",
    "6800-109": "风特效 8330 破防",
    "6800-116": "风特效 9291 破防",
    "4294": "刀啸风吟5%橙武",
    "4295": "项王击鼎5%橙武",
    "2430": "橙武特效",
    "1942": "上将军印-神兵"
}
GAINS_MAP = {
    "1925": attribute_set_gain,
    "4290": dao_xiao_set_gain,
    "4291": shang_jiang_set_gain,
    "15436-9": special_enchant_hat_gain(822),
    "15436-10": special_enchant_hat_gain(999),
    "15436-11": special_enchant_hat_gain(1098),
    "22151-9": special_enchant_jacket_gain(371),
    "22151-10": special_enchant_jacket_gain(450),
    "22151-11": special_enchant_jacket_gain(495),
    "22169": special_enchant_belt_gain,
    "22166": special_enchant_wrist_gain,
    "33247": special_enchant_shoes_gain,
    "2401": water_weapon_gain(67),
    "2498": water_weapon_gain(88),
    "2540": water_weapon_gain(98),
    "6800-102": wind_pendant_gain(6408),
    "6800-109": wind_pendant_gain(8330),
    "6800-116": wind_pendant_gain(9291),
    "4294": dao_xiao_divine_gain,
    "4295": xiang_wang_divine_gain,
    "2430": divine_effect,
    "1942": shang_jiang_divine_gain
}


def EMBED_COF(level):
    if level > 6:
        return (level * 0.65 - 3.2) * 1.3
    else:
        return level * 0.195


def STRENGTH_COF(level):
    return level * (0.7 + 0.3 * level) / 200
