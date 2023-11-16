import bei_ao_jue.gains
from bei_ao_jue.attribute import BeiAoJue
from general.gains.equipment import *
from general.gains.team import *
from general.consumables import *

CLASSES = ["少林", "万花", "天策", "纯阳", "七秀", ]
SUPPORT_CLASS = {
    "北傲诀": {
        "school": "霸刀",
        "major": "力道",
        "kind": "外功",
        "attribute": BeiAoJue,
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

POSITIONS = ['帽子', '上衣', '腰带', '护腕', '下装', '鞋子', '项链', '腰坠', '戒指2', '远程武器', '近战武器']
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
    "atAllTypeCriticalStrike": "全会心",
    "atPhysicsCriticalDamagePowerBase": "会效",
    "atPhysicsOvercomeBase": "破防",
    "atMeleeWeaponDamageBase": "武器伤害",
    "atStrainBase": "无双",
    "atHasteBase": "加速",
    "atSurplusValueBase": "破招",
}

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


EQUIPMENTS_DIR = "ui/assets/equipments.json"
ENCHANTS_DIR = "ui/assets/enchants.json"
STONES_DIR = "ui/assets/stones.json"
EQUIPS_CONFIG_DIR = "ui/config/equips.json"

STONE_POSITIONS = ["近战武器"]
WIND_PENDANT_SKILL_ID = "6800"

SPECIAL_ENCHANT_MAP = {
    "帽子": {
        12800: "15436-11",
        11500: "15436-10",
        10600: "15436-9"
    },
    "上衣": {
        12800: "22151-11",
        11500: "22151-10",
        10600: "22151-9"
    },
    "腰带": {
        0: "22169"
    },
    "护腕": {
        0: "22166"
    },
    "鞋子": {
        0: "33247"
    },
}

EQUIP_GAINS_TRANSLATE = {
    "15436-9": "大附魔帽 822 破防",
    "15436-10": "大附魔帽 999 破防",
    "15436-11": "大附魔帽 1098 破防",
    "22151-9": "大附魔衣 371 外攻",
    "22151-10": "大附魔衣 450 外攻",
    "22151-11": "大附魔衣 495 外攻",
    "22169": "大附魔腰",
    "22166": "大附魔腕",
    "33247": "大附魔鞋",
    "2401": "水特效 67 外攻",
    "2498": "水特效 88 外攻",
    "2540": "水特效 98 外攻",
    "6800-102": "风特效 6408 破防",
    "6800-109": "风特效 8330 破防",
    "6800-116": "风特效 9291 破防",

    "1925": "朔气4%套装",
    "4290": "刀啸风吟10%套装",
    "4291": "上将军印10%套装",
    "4294": "刀啸风吟5%橙武",
    "4295": "项王击鼎5%橙武",
    "2430": "橙武特效",
    "1942": "上将军印-神兵"
}
EQUIP_GAINS = {
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

    "1925": bei_ao_jue.gains.attribute_set_gain,
    "4290": bei_ao_jue.gains.dao_xiao_set_gain,
    "4291": bei_ao_jue.gains.shang_jiang_set_gain,
    "4294": bei_ao_jue.gains.dao_xiao_divine_gain,
    "4295": bei_ao_jue.gains.xiang_wang_divine_gain,
    "2430": bei_ao_jue.gains.divine_effect,
    "1942": bei_ao_jue.gains.shang_jiang_divine_gain
}
CONSUMABLES = {
    "三鲜粥(347力道)": strength_food(347),
    "三鲜汤(173力道)": strength_food(173),

    "上品大力丸(446力道)": strength_potion(446),
    "中品大力丸(223力道)": strength_potion(223),

    "太后饼(696外攻)": physical_attack_power_food(696),
    "煎饼果子(348外攻)": physical_attack_power_food(348),
    "白肉血肠(1545破招)": surplus_food(1545),
    "红烧扣肉(1545加速)": haste_food(1545),
    "红烧排骨(1545破防)": all_overcome_food(1545),
    "酸菜鱼(1545会心)": all_critical_strike_food(1545),
    "毛血旺(773破招)": surplus_food(773),
    "栗子烧肉(773加速)": haste_food(773),
    "水煮肉片(773破防)": all_overcome_food(773),
    "鱼香肉丝(773会心)": all_critical_strike_food(773),

    "上品亢龙散(895外攻)": physical_attack_power_potion(895),
    "中品亢龙散(448外攻)": physical_attack_power_potion(448),
    "上品凝神散(1987破招)": surplus_potion(1987),
    "上品活气散(1987加速)": haste_potion(1987),
    "上品破秽散(1987破防)": all_overcome_potion(1987),
    "上品玉璃散(1987会心)": all_critical_strike_potion(1987),
    "中品凝神散(993破招)": surplus_potion(993),
    "中品活气散(993加速)": haste_potion(993),
    "中品破秽散(993破防)": all_overcome_potion(993),
    "中品玉璃散(993会心)": all_critical_strike_potion(993),

    "瀑沙熔锭(597外攻)": physical_attack_power_enchant(597),
    "瀑沙磨石(298外攻)": physical_attack_power_enchant(298),

    "水晶芙蓉宴(力道)": strength_spread(396),
    "玉笛谁家听落梅": physical_spread(398, 883),
    "同泽宴": tong_ze_spread(234),
    "蒸鱼菜盘": streamed_fish_spread(517),
    "炼狱水煮鱼": boiled_fish_spread(100),
    "百炼水煮鱼": boiled_fish_spread(400)
}
MAJOR_FOODS = {
    "力道": ["三鲜粥(347力道)", "三鲜汤(173力道)"]
}
MINOR_FOODS = {
    "外功": [
        "太后饼(696外攻)", "煎饼果子(348外攻)",
        "白肉血肠(1545破招)", "红烧扣肉(1545加速)", "红烧排骨(1545破防)", "酸菜鱼(1545会心)",
        "毛血旺(773破招)", "栗子烧肉(773加速)", "水煮肉片(773破防)", "鱼香肉丝(773会心)"
    ]
}
MAJOR_POTIONS = {
    "力道": ["上品大力丸(446力道)", "中品大力丸(223力道)"],
}
MINOR_POTIONS = {
    "外功": [
        "上品亢龙散(895外攻)", "中品亢龙散(448外攻)",
        "上品凝神散(1987破招)", "上品活气散(1987加速)", "上品破秽散(1987破防)", "上品玉璃散(1987会心)",
        "中品凝神散(993破招)", "中品活气散(993加速)", "中品破秽散(993破防)", "中品玉璃散(993会心)"
    ]
}
WEAPON_ENCHANTS = {
    "外功": ["瀑沙熔锭(597外攻)", "瀑沙磨石(298外攻)"]
}
WINES = {

}
SNACKS = {

}
SPREADS = {
    "力道": ["水晶芙蓉宴(力道)", "玉笛谁家听落梅"],
}

TEAM_GAINS = {
    "袖气": xiu_qi(244),
    "左旋右转": zuo_xuan_you_zhuan(54),

    "撼如雷": han_ru_lei,
    "破风": po_feng(1150),
    "劲风": po_feng(1397),
    "乘龙箭": cheng_long_jian,
    "号令三军": hao_ling_san_jun(470),
    "激雷": ji_lei,

    "立地成佛": li_di_cheng_fo,
    "舍身弘法": she_shen_hong_fa(470),

    "秋肃": qiu_su,
    "落子无悔": luo_zi_wu_hui,

    "碎星辰": sui_xing_chen,
    "破苍穹": po_cang_qiong,

    "剑锋百锻": jian_feng_bai_duan,

    "善友": shan_you,
    "仙王蛊鼎": xian_wang_gu_ding,

    "戒火": jie_huo,
    "烈日": lie_ri,
    "朝圣言": chao_sheng_yan(470),
    "圣浴明心": chao_sheng_yan(705),

    "酒中仙": jiu_zhong_xian,

    "虚弱": xu_ruo,
    "振奋": zhen_fen(60),
    "寒啸千军": han_xiao_qian_jun,

    "庄周梦": zhuang_zhou_meng(60),

    "疏狂": shu_kuang,

    "飘黄": piao_huang,
    "配伍": pei_wu,
}
