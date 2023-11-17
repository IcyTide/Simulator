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

POSITIONS = ['帽子', '上衣', '腰带', '护腕', '下装', '鞋子', '项链', '腰坠', '戒指1', '戒指2', '远程武器', '近战武器']
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

EQUIP_GAINS_NUMBER = {
    "15436-9": 822,
    "15436-10": 999,
    "15436-11": 1098,
    "22151-9": 371,
    "22151-10": 450,
    "22151-11": 495,
    "2401": 67,
    "2498": 88,
    "2540": 98,
    "6800-102": 6408,
    "6800-109": 8330,
    "6800-116": 9291
}
EQUIP_GAINS_NAME = {
    "15436-9": f"大附魔帽 {EQUIP_GAINS_NUMBER['15436-9']} 破防",
    "15436-10": f"大附魔帽 {EQUIP_GAINS_NUMBER['15436-10']} 破防",
    "15436-11": f"大附魔帽 {EQUIP_GAINS_NUMBER['15436-11']} 破防",
    "22151-9": f"大附魔衣 {EQUIP_GAINS_NUMBER['22151-9']} 外攻",
    "22151-10": f"大附魔衣 {EQUIP_GAINS_NUMBER['22151-10']} 外攻",
    "22151-11": f"大附魔衣 {EQUIP_GAINS_NUMBER['22151-11']} 外攻",
    "22169": "大附魔腰",
    "22166": "大附魔腕",
    "33247": "大附魔鞋",
    "2401": f"水特效 {EQUIP_GAINS_NUMBER['2401']} 外攻",
    "2498": f"水特效 {EQUIP_GAINS_NUMBER['2498']} 外攻",
    "2540": f"水特效 {EQUIP_GAINS_NUMBER['2540']} 外攻",
    "6800-102": f"风特效 {EQUIP_GAINS_NUMBER['6800-102']} 破防",
    "6800-109": f"风特效 {EQUIP_GAINS_NUMBER['6800-109']} 破防",
    "6800-116": f"风特效 {EQUIP_GAINS_NUMBER['6800-116']} 破防",

    "1925": "朔气4%套装",
    "4290": "刀啸风吟10%套装",
    "4291": "上将军印10%套装",
    "4294": "刀啸风吟5%橙武",
    "4295": "项王击鼎5%橙武",
    "2430": "橙武特效",
    "1942": "上将军印-神兵"
}
EQUIP_GAINS = {
    "15436-9": special_enchant_hat_gain(EQUIP_GAINS_NUMBER['15436-9']),
    "15436-10": special_enchant_hat_gain(EQUIP_GAINS_NUMBER['15436-10']),
    "15436-11": special_enchant_hat_gain(EQUIP_GAINS_NUMBER['15436-11']),
    "22151-9": special_enchant_jacket_gain(EQUIP_GAINS_NUMBER['22151-9']),
    "22151-10": special_enchant_jacket_gain(EQUIP_GAINS_NUMBER['22151-10']),
    "22151-11": special_enchant_jacket_gain(EQUIP_GAINS_NUMBER['22151-11']),
    "22169": special_enchant_belt_gain,
    "22166": special_enchant_wrist_gain,
    "33247": special_enchant_shoes_gain,
    "2401": water_weapon_gain(EQUIP_GAINS_NUMBER['2401']),
    "2498": water_weapon_gain(EQUIP_GAINS_NUMBER['2498']),
    "2540": water_weapon_gain(EQUIP_GAINS_NUMBER['2540']),
    "6800-102": wind_pendant_gain(EQUIP_GAINS_NUMBER['6800-102']),
    "6800-109": wind_pendant_gain(EQUIP_GAINS_NUMBER['6800-109']),
    "6800-116": wind_pendant_gain(EQUIP_GAINS_NUMBER['6800-116']),

    "1925": bei_ao_jue.gains.attribute_set_gain,
    "4290": bei_ao_jue.gains.dao_xiao_set_gain,
    "4291": bei_ao_jue.gains.shang_jiang_set_gain,
    "4294": bei_ao_jue.gains.dao_xiao_divine_gain,
    "4295": bei_ao_jue.gains.xiang_wang_divine_gain,
    "2430": bei_ao_jue.gains.divine_effect,
    "1942": bei_ao_jue.gains.shang_jiang_divine_gain
}
CONSUMABLES_NUMBER = {
    "major_food_max": 347,
    "major_food_min": 173,

    "physical_food_max": 696,
    "physical_food_min": 348,
    "minor_food_max": 1545,
    "minor_food_min": 773,

    "major_potion_max": 446,
    "major_potion_min": 223,

    "physical_potion_max": 895,
    "physical_potion_min": 448,
    "minor_potion_max": 1987,
    "minor_potion_min": 993,

    "weapon_enchant_max": 597,
    "weapon_enchant_min": 298,

    "tong_ze_spread": 234,
    "streamed_fish_spread": 517,
    "major_spread": 396,
    "physical_spread": 398,
    "minor_spread": 883,
    "boiled_fish_max": 400,
    "boiled_fish_min": 100,
}

CONSUMABLES = {
    f"三鲜粥({CONSUMABLES_NUMBER['major_food_max']}力道)":
        strength_food(CONSUMABLES_NUMBER["major_food_max"]),
    f"三鲜汤({CONSUMABLES_NUMBER['major_food_min']}力道)":
        strength_food(CONSUMABLES_NUMBER["major_food_min"]),

    f"太后饼({CONSUMABLES_NUMBER['physical_food_max']}外攻)":
        physical_attack_power_food(CONSUMABLES_NUMBER["physical_food_max"]),
    f"煎饼果子({CONSUMABLES_NUMBER['physical_food_min']}外攻)":
        physical_attack_power_food(CONSUMABLES_NUMBER["physical_food_min"]),
    f"白肉血肠({CONSUMABLES_NUMBER['minor_food_max']}破招)":
        surplus_food(CONSUMABLES_NUMBER["minor_food_max"]),
    f"红烧扣肉({CONSUMABLES_NUMBER['minor_food_max']}加速)":
        haste_food(CONSUMABLES_NUMBER["minor_food_max"]),
    f"红烧排骨({CONSUMABLES_NUMBER['minor_food_max']}破防)":
        all_overcome_food(CONSUMABLES_NUMBER["minor_food_max"]),
    f"酸菜鱼({CONSUMABLES_NUMBER['minor_food_max']}会心)":
        all_critical_strike_food(CONSUMABLES_NUMBER["minor_food_max"]),
    f"毛血旺({CONSUMABLES_NUMBER['minor_food_min']}破招)":
        surplus_food(CONSUMABLES_NUMBER["minor_food_min"]),
    f"栗子烧肉({CONSUMABLES_NUMBER['minor_food_min']}加速)":
        haste_food(CONSUMABLES_NUMBER["minor_food_min"]),
    f"水煮肉片({CONSUMABLES_NUMBER['minor_food_min']}破防)":
        all_overcome_food(CONSUMABLES_NUMBER["minor_food_min"]),
    f"鱼香肉丝({CONSUMABLES_NUMBER['minor_food_min']}会心)":
        all_critical_strike_food(CONSUMABLES_NUMBER["minor_food_min"]),

    f"上品大力丸({CONSUMABLES_NUMBER['major_potion_max']}力道)":
        strength_potion(CONSUMABLES_NUMBER["major_potion_max"]),
    f"中品大力丸({CONSUMABLES_NUMBER['major_potion_min']}力道)":
        strength_potion(CONSUMABLES_NUMBER["major_potion_min"]),

    f"上品亢龙散({CONSUMABLES_NUMBER['physical_potion_max']}外攻)":
        physical_attack_power_potion(CONSUMABLES_NUMBER["physical_potion_max"]),
    f"中品亢龙散({CONSUMABLES_NUMBER['physical_potion_min']}外攻)":
        physical_attack_power_potion(CONSUMABLES_NUMBER["physical_potion_min"]),
    f"上品凝神散({CONSUMABLES_NUMBER['minor_potion_max']}破招)":
        surplus_potion(CONSUMABLES_NUMBER["minor_potion_max"]),
    f"上品活气散({CONSUMABLES_NUMBER['minor_potion_max']}加速)":
        haste_potion(CONSUMABLES_NUMBER["minor_potion_max"]),
    f"上品破秽散({CONSUMABLES_NUMBER['minor_potion_max']}破防)":
        all_overcome_potion(CONSUMABLES_NUMBER["minor_potion_max"]),
    f"上品玉璃散({CONSUMABLES_NUMBER['minor_potion_max']}会心)":
        all_critical_strike_potion(CONSUMABLES_NUMBER["minor_potion_max"]),
    f"中品凝神散({CONSUMABLES_NUMBER['minor_potion_min']}破招)":
        surplus_potion(CONSUMABLES_NUMBER["minor_potion_min"]),
    f"中品活气散({CONSUMABLES_NUMBER['minor_potion_min']}加速)":
        haste_potion(CONSUMABLES_NUMBER["minor_potion_min"]),
    f"中品破秽散({CONSUMABLES_NUMBER['minor_potion_min']}破防)":
        all_overcome_potion(CONSUMABLES_NUMBER["minor_potion_min"]),
    f"中品玉璃散({CONSUMABLES_NUMBER['minor_potion_min']}会心)":
        all_critical_strike_potion(CONSUMABLES_NUMBER["minor_potion_min"]),

    f"瀑沙熔锭({CONSUMABLES_NUMBER['weapon_enchant_max']}外攻)":
        physical_attack_power_enchant(CONSUMABLES_NUMBER["weapon_enchant_max"]),
    f"瀑沙磨石({CONSUMABLES_NUMBER['weapon_enchant_min']}外攻)":
        physical_attack_power_enchant(CONSUMABLES_NUMBER["weapon_enchant_min"]),

    "同泽宴":
        tong_ze_spread(CONSUMABLES_NUMBER["tong_ze_spread"]),
    "蒸鱼菜盘":
        streamed_fish_spread(CONSUMABLES_NUMBER["streamed_fish_spread"]),
    f"水晶芙蓉宴({CONSUMABLES_NUMBER['major_spread']}力道)":
        strength_spread(CONSUMABLES_NUMBER["major_spread"]),
    f"玉笛谁家听落梅({CONSUMABLES_NUMBER['physical_spread']}外攻{CONSUMABLES_NUMBER['minor_spread']}会心/破招)":
        physical_spread(CONSUMABLES_NUMBER["physical_spread"], CONSUMABLES_NUMBER["minor_spread"]),
    f"炼狱水煮鱼({CONSUMABLES_NUMBER['boiled_fish_min']}破招/无双)":
        boiled_fish_spread(CONSUMABLES_NUMBER["boiled_fish_min"]),
    f"百炼水煮鱼({CONSUMABLES_NUMBER['boiled_fish_min']}破招/无双)":
        boiled_fish_spread(CONSUMABLES_NUMBER["boiled_fish_max"])
}
MAJOR_FOODS = {
    "力道": [
        f"三鲜粥({CONSUMABLES_NUMBER['major_food_max']}力道)",
        f"三鲜汤({CONSUMABLES_NUMBER['major_food_min']}力道)"
    ]
}
MINOR_FOODS = {
    "外功": [
        f"太后饼({CONSUMABLES_NUMBER['physical_food_max']}外攻)",
        f"煎饼果子({CONSUMABLES_NUMBER['physical_food_min']}外攻)",
        f"白肉血肠({CONSUMABLES_NUMBER['minor_food_max']}破招)",
        f"红烧扣肉({CONSUMABLES_NUMBER['minor_food_max']}加速)",
        f"红烧排骨({CONSUMABLES_NUMBER['minor_food_max']}破防)",
        f"酸菜鱼({CONSUMABLES_NUMBER['minor_food_max']}会心)",
        f"毛血旺({CONSUMABLES_NUMBER['minor_food_min']}破招)",
        f"栗子烧肉({CONSUMABLES_NUMBER['minor_food_min']}加速)",
        f"水煮肉片({CONSUMABLES_NUMBER['minor_food_min']}破防)",
        f"鱼香肉丝({CONSUMABLES_NUMBER['minor_food_min']}会心)"
    ]
}
MAJOR_POTIONS = {
    "力道": [
        f"上品大力丸({CONSUMABLES_NUMBER['major_potion_max']}力道)",
        f"中品大力丸({CONSUMABLES_NUMBER['major_potion_min']}力道)"
    ],
}
MINOR_POTIONS = {
    "外功": [
        f"上品亢龙散({CONSUMABLES_NUMBER['physical_potion_max']}外攻)",
        f"中品亢龙散({CONSUMABLES_NUMBER['physical_potion_min']}外攻)",
        f"上品凝神散({CONSUMABLES_NUMBER['minor_potion_max']}破招)",
        f"上品活气散({CONSUMABLES_NUMBER['minor_potion_max']}加速)",
        f"上品破秽散({CONSUMABLES_NUMBER['minor_potion_max']}破防)",
        f"上品玉璃散({CONSUMABLES_NUMBER['minor_potion_max']}会心)",
        f"中品凝神散({CONSUMABLES_NUMBER['minor_potion_min']}破招)",
        f"中品活气散({CONSUMABLES_NUMBER['minor_potion_min']}加速)",
        f"中品破秽散({CONSUMABLES_NUMBER['minor_potion_min']}破防)",
        f"中品玉璃散({CONSUMABLES_NUMBER['minor_potion_min']}会心)"
    ]
}
WEAPON_ENCHANTS = {
    "外功": [
        f"瀑沙熔锭({CONSUMABLES_NUMBER['weapon_enchant_max']}外攻)",
        f"瀑沙磨石({CONSUMABLES_NUMBER['weapon_enchant_min']}外攻)"
    ]
}
WINES = {

}
SNACKS = {

}
SPREADS = {
    "力道": [
        f"水晶芙蓉宴({CONSUMABLES_NUMBER['major_spread']}力道)",
        f"玉笛谁家听落梅({CONSUMABLES_NUMBER['physical_spread']}外攻{CONSUMABLES_NUMBER['minor_spread']}会心/破招)"
    ],
}

TEAM_GAINS_NUMBER = {
    "袖气": 244,
    "左旋右转": 54,

    "撼如雷": 51 / 1024,
    "破风": 1150,
    "劲风": 1397,
    "乘龙箭": 102 / 1024,
    "号令三军": 470,
    "激雷": 205 / 1024,

    "立地成佛": 30 * 5 / 1024,
    "舍身弘法": 470,

    "秋肃": 61 / 1024,
    "皎素": 51 / 1024,

    "碎星辰": 10 / 1024,
    "破苍穹": 10 / 1024,

    "剑锋百锻": 1,

    "善友": 0.06,
    "仙王蛊鼎": 123 / 1024,

    "戒火": 51 / 1024,
    "烈日": 51 / 1024,
    "朝圣言": 470,
    "圣浴明心": 705,

    "酒中仙": 0.1,

    "虚弱": 51 / 1024,
    "寒啸千军": 204 / 1024,
    "振奋": 60,

    "庄周梦": 60,

    "疏狂": 307 / 1024,

    "配伍": 10 * 5 / 1024,
}
TEAM_GAINS_NAME = {
    "袖气": f"{TEAM_GAINS_NUMBER['袖气']}全属性",
    "左旋右转": f"左旋右转({TEAM_GAINS_NUMBER['左旋右转']}破招)",

    "撼如雷": f"{round(TEAM_GAINS_NUMBER['撼如雷'] * 100)}%外攻",
    "破风": f"破风(-{TEAM_GAINS_NUMBER['破风']}外防)",
    "劲风": f"劲风(-{TEAM_GAINS_NUMBER['劲风']}外防)",
    "乘龙箭": f"{-round(TEAM_GAINS_NUMBER['乘龙箭'] * 100)}%外防",
    "号令三军": f"号令三军({TEAM_GAINS_NUMBER['号令三军']}无双)",
    "激雷": f"激雷({round(TEAM_GAINS_NUMBER['激雷'] * 100)}%外攻/外破)",

    "立地成佛": f"立地成佛(-{round(TEAM_GAINS_NUMBER['立地成佛'] * 100)}%内防)",
    "舍身弘法": f"舍身弘法({TEAM_GAINS_NUMBER['舍身弘法']}无双)",

    "秋肃": f"{round(TEAM_GAINS_NUMBER['秋肃'] * 100)}%全易伤",
    "皎素": f"{round(TEAM_GAINS_NUMBER['皎素'] * 100)}%全会效",

    "碎星辰": f"{round(TEAM_GAINS_NUMBER['碎星辰'] * 100)}%外功会效",
    "破苍穹": f"{round(TEAM_GAINS_NUMBER['破苍穹'] * 100)}%内功会效",

    "剑锋百锻": f"{round(TEAM_GAINS_NUMBER['剑锋百锻'] * 100)}%武伤",

    "善友": f"{round(TEAM_GAINS_NUMBER['善友'] * 100)}%调息加速",
    "仙王蛊鼎": f"仙王蛊鼎({round(TEAM_GAINS_NUMBER['仙王蛊鼎'] * 100)}伤害加成)",

    "戒火": f"{round(TEAM_GAINS_NUMBER['戒火'] * 100)}%全易伤",
    "烈日": f"{round(TEAM_GAINS_NUMBER['烈日'] * 100)}%阴性/阳性易伤",
    "朝圣言": f"朝圣言({TEAM_GAINS_NUMBER['朝圣言']}无双)",
    "圣浴明心": f"圣浴明心({TEAM_GAINS_NUMBER['圣浴明心']}无双)",

    "酒中仙": f"{round(TEAM_GAINS_NUMBER['酒中仙'] * 100)}%外会",

    "虚弱": f"{-round(TEAM_GAINS_NUMBER['虚弱'] * 100)}%外防",
    "寒啸千军": f"寒啸千军({round(TEAM_GAINS_NUMBER['寒啸千军'] * 100)}破防)",
    "振奋": f"振奋({TEAM_GAINS_NUMBER['振奋']}破防)",

    "庄周梦": f"庄周梦({TEAM_GAINS_NUMBER['庄周梦']}无双)",

    "疏狂": f"疏狂({round(TEAM_GAINS_NUMBER['疏狂'] * 100)}攻击)",

    "飘黄": f"飘黄(额外伤害)",
    "配伍": f"配伍({round(TEAM_GAINS_NUMBER['配伍'] * 100)}全属性)",
}
TEAM_GAINS = {
    "袖气": xiu_qi(TEAM_GAINS_NUMBER["袖气"]),
    "左旋右转": zuo_xuan_you_zhuan(TEAM_GAINS_NUMBER["左旋右转"]),

    "撼如雷": han_ru_lei(TEAM_GAINS_NUMBER["撼如雷"]),
    "破风": po_feng(TEAM_GAINS_NUMBER["破风"], TEAM_GAINS_NUMBER["劲风"]),
    "乘龙箭": cheng_long_jian(TEAM_GAINS_NUMBER["乘龙箭"]),
    "号令三军": hao_ling_san_jun(TEAM_GAINS_NUMBER["号令三军"]),
    "激雷": ji_lei(TEAM_GAINS_NUMBER["激雷"]),

    "立地成佛": li_di_cheng_fo(TEAM_GAINS_NUMBER["立地成佛"]),
    "舍身弘法": she_shen_hong_fa(TEAM_GAINS_NUMBER["舍身弘法"]),

    "秋肃": qiu_su(TEAM_GAINS_NUMBER["秋肃"]),
    "皎素": jiao_su(TEAM_GAINS_NUMBER["皎素"]),

    "碎星辰": sui_xing_chen(TEAM_GAINS_NUMBER["碎星辰"]),
    "破苍穹": po_cang_qiong(TEAM_GAINS_NUMBER["破苍穹"]),

    "剑锋百锻": jian_feng_bai_duan(TEAM_GAINS_NUMBER["破苍穹"]),

    "善友": shan_you(TEAM_GAINS_NUMBER["善友"]),
    "仙王蛊鼎": xian_wang_gu_ding(TEAM_GAINS_NUMBER["仙王蛊鼎"]),

    "戒火": jie_huo(TEAM_GAINS_NUMBER["戒火"]),
    "烈日": lie_ri(TEAM_GAINS_NUMBER["烈日"]),
    "朝圣言": chao_sheng_yan(TEAM_GAINS_NUMBER["朝圣言"], TEAM_GAINS_NUMBER["圣浴明心"]),

    "酒中仙": jiu_zhong_xian(TEAM_GAINS_NUMBER["酒中仙"]),

    "虚弱": xu_ruo(TEAM_GAINS_NUMBER["虚弱"]),
    "寒啸千军": han_xiao_qian_jun(TEAM_GAINS_NUMBER["寒啸千军"]),
    "振奋": zhen_fen(TEAM_GAINS_NUMBER["振奋"]),

    "庄周梦": zhuang_zhou_meng(TEAM_GAINS_NUMBER["庄周梦"]),

    "疏狂": shu_kuang(TEAM_GAINS_NUMBER["疏狂"]),

    "飘黄": piao_huang,
    "配伍": pei_wu(TEAM_GAINS_NUMBER["配伍"]),
}
