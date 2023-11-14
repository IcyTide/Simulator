import bei_ao_jue.gains
from bei_ao_jue.attribute import BeiAoJue
from general.gains import *

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
            "physical_overcome": "破防"
        },
        "equip_gains": {
            "1925": {
                "name": "朔气4%套装",
                "gain": bei_ao_jue.gains.attribute_set_gain
            },
            "4290": {
                "name": "刀啸风吟10%套装",
                "gain": bei_ao_jue.gains.dao_xiao_set_gain
            },
            "4291": {
                "name": "上将军印10%套装",
                "gain": bei_ao_jue.gains.shang_jiang_set_gain
            },
            "4294": {
                "name": "刀啸风吟5%橙武",
                "gain": bei_ao_jue.gains.dao_xiao_divine_gain
            },
            "4295": {
                "name": "项王击鼎5%橙武",
                "gain": bei_ao_jue.gains.xiang_wang_divine_gain
            },
            "2430": {
                "name": "橙武特效",
                "gain": bei_ao_jue.gains.divine_effect
            },
            "1942": {
                "name": "上将军印-神兵",
                "gain": bei_ao_jue.gains.shang_jiang_divine_gain
            }
        },
    }
}

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

DISPLAY_ATTRS = {
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
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

EQUIP_GAINS_TRANSLATE = {
    "15436-9": "大附魔头 822 破防",
    "15436-10": "大附魔头 999 破防",
    "15436-11": "大附魔头 1098 破防",
    "22151-9": "大附魔衣 371 外攻",
    "22151-10": "大附魔衣 450 外攻",
    "22151-11": "大附魔衣 495 外攻",
    "22169": "大附魔腰",
    "22166": "大附魔手",
    "33247": "大附魔脚",
    "2401": "水特效 67 外攻",
    "2498": "水特效 88 外攻",
    "2540": "水特效 98 外攻",
    "6800-102": "风特效 6408 破防",
    "6800-109": "风特效 8330 破防",
    "6800-116": "风特效 9291 破防",
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
}
TEAM_GAINS = {
    "通用": {
        "号令三军": hao_ling_san_jun,
        "舍身弘法": she_shen_hong_fa,
        "戒火": jie_huo,
        "朝圣言": chao_sheng_yan,
        "圣浴明心": sheng_yu_ming_xin,
        "振奋": zhen_fen,
        "寒啸千军": han_xiao_qian_jun,
        "秋肃": qiu_su,
        "秀气": xiu_qi,
        "左旋右转": zuo_xuan_you_zhuan,
        "仙王蛊鼎": xian_wang_gu_ding,
        "庄周梦": zhuang_zhou_meng,
        "飘黄": piao_huang,
        "配伍": pei_wu,

        "剑锋百锻": jian_feng_bai_duan,
        "善友": shan_you,
        "疏狂": shu_kuang,
        "撼如雷": han_ru_lei,
        "破风": po_feng,
        "劲风": jing_feng,
        "虚弱": xu_ruo,

        "碎星辰": sui_xing_chen,
        "酒中仙": jiu_zhong_xian,
        "激雷": ji_lei
    }
}
WEAPON_ENCHANTS = {
    "外功": {
        "瀑沙熔锭": physical_attack_power_enchant(597),
        "瀑沙磨石": physical_attack_power_enchant(298)
    }
}
MAJOR_FOODS = {
    "力道": {
        "三鲜粥(347力道)": strength_food(347),
        "三鲜汤(173力道)": strength_food(173)
    }
}
MINOR_FOODS = {
    "白肉血肠(1545破招)": surplus_food(1545),
    "红烧扣肉(1545加速)": haste_food(1545),
    "红烧排骨(1545破防)": all_overcome_food(1545),
    "酸菜鱼(1545会心)": all_critical_strike_food(1545),
    "毛血旺(773破招)": surplus_food(773),
    "栗子烧肉(773加速)": haste_food(773),
    "水煮肉片(773破防)": all_overcome_food(773),
    "鱼香肉丝(773会心)": all_critical_strike_food(773),
    "太后饼(696外攻)": physical_attack_power_food(696),
    "煎饼果子(348外攻)": physical_attack_power_food(348)
}
MAJOR_POTIONS = {
    "力道": {
        "上品大力丸(446力道)": strength_potion(446),
        "中品大力丸(223力道)": strength_potion(223)
    }
}
MINOR_POTIONS = {
    "上品凝神散(1987破招)": surplus_potion(1987),
    "上品活气散(1987加速)": haste_potion(1987),
    "上品破秽散(1987破防)": all_overcome_potion(1987),
    "上品玉璃散(1987会心)": all_critical_strike_potion(1987),
    "上品亢龙散(895外攻)": physical_attack_power_potion(895),
    "中品凝神散(993破招)": surplus_potion(993),
    "中品活气散(993加速)": haste_potion(993),
    "中品破秽散(993破防)": all_overcome_potion(993),
    "中品玉璃散(993会心)": all_critical_strike_potion(993),
    "中品亢龙散(448外攻)": physical_attack_power_potion(448)
}
WINES = {

}
SNACKS = {

}
SPREADS = {

}


def EMBED_COF(level):
    if level > 6:
        return (level * 0.65 - 3.2) * 1.3
    else:
        return level * 0.195


def STRENGTH_COF(level):
    return level * (0.7 + 0.3 * level) / 200
