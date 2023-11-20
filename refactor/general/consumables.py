""" Weapon Enchant """


def physical_attack_power_enchant(value):
    return {"physical_attack_power_base": value}


""" Spread """


def strength_spread(value):
    return {"strength_base": value}


def physical_spread(value1, value2):
    return {"physical_attack_power_base": value1,
            "all_critical_strike_base": value2,
            "surplus": value2}


def tong_ze_spread(value):
    return {"surplus": value, "strain_base": value}


def boiled_fish_spread(value):
    return {"surplus": value, "strain_base": value}


def streamed_fish_spread(value):
    return {"strain_base": value}


""" Major Food """


def strength_food(value):
    return {"strength_base": value}


""" Minor Food """


def physical_attack_power_food(value):
    return {"physical_attack_power_base": value}


def surplus_food(value):
    return {"surplus": value}


def haste_food(value):
    return {"haste_base": value}


def all_overcome_food(value):
    return {"physical_overcome_base": value}


def all_critical_strike_food(value):
    return {"all_critical_strike_base": value}


""" Major Potion """


def strength_potion(value):
    return {"strength_base": value}


""" Minor Potion """


def physical_attack_power_potion(value):
    return {"physical_attack_power_base": value}


def surplus_potion(value):
    return {"surplus": value}


def haste_potion(value):
    return {"haste_base": value}


def all_overcome_potion(value):
    return {"physical_overcome_base": value}


def all_critical_strike_potion(value):
    return {"all_critical_strike_base": value}


""" Wine """


def strength_wine(value):
    return {"strength_base": value}


def haste_wine(value):
    return {"haste_base": value}


""" Snack """


def physical_attack_power_snack(value):
    return {"physical_attack_power_base": value}


def strain_snack(value):
    return {"strain_base": value}


def critical_snack(value):
    return {"all_critical_strike_base": value}


def overcome_snack(value):
    return {"physical_overcome_base": value}


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

    "minor_snack_max": 1934,
    "minor_snack_min": 858,
    "physical_snack": 866,

    "major_wine": 256,
    "haste_wine": 1144,

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

    f"创意料理({CONSUMABLES_NUMBER['physical_snack']})外攻":
        physical_attack_power_snack(CONSUMABLES_NUMBER["physical_snack"]),
    f"创意料理({CONSUMABLES_NUMBER['minor_snack_max']})无双":
        strain_snack(CONSUMABLES_NUMBER["minor_snack_max"]),
    f"创意料理({CONSUMABLES_NUMBER['minor_snack_max']})会心":
        critical_snack(CONSUMABLES_NUMBER["minor_snack_max"]),
    f"创意料理({CONSUMABLES_NUMBER['minor_snack_max']})破防":
        overcome_snack(CONSUMABLES_NUMBER["minor_snack_max"]),

    f"汾酒·旬又三({CONSUMABLES_NUMBER['major_wine']}力道)":
        strength_wine(CONSUMABLES_NUMBER["major_wine"]),

    f"女儿红·旬又三({CONSUMABLES_NUMBER['haste_wine']}加速)":
        haste_wine(CONSUMABLES_NUMBER["haste_wine"]),

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
    f"百炼水煮鱼({CONSUMABLES_NUMBER['boiled_fish_max']}破招/无双)":
        boiled_fish_spread(CONSUMABLES_NUMBER["boiled_fish_max"])
}
FOODS = {
    "力道": [
        f"三鲜粥({CONSUMABLES_NUMBER['major_food_max']}力道)",
        f"三鲜汤({CONSUMABLES_NUMBER['major_food_min']}力道)"
    ],
    "通用": [
        f"白肉血肠({CONSUMABLES_NUMBER['minor_food_max']}破招)",
        f"红烧扣肉({CONSUMABLES_NUMBER['minor_food_max']}加速)",
        f"红烧排骨({CONSUMABLES_NUMBER['minor_food_max']}破防)",
        f"酸菜鱼({CONSUMABLES_NUMBER['minor_food_max']}会心)",
        f"毛血旺({CONSUMABLES_NUMBER['minor_food_min']}破招)",
        f"栗子烧肉({CONSUMABLES_NUMBER['minor_food_min']}加速)",
        f"水煮肉片({CONSUMABLES_NUMBER['minor_food_min']}破防)",
        f"鱼香肉丝({CONSUMABLES_NUMBER['minor_food_min']}会心)"
    ],
    "外功": [
        f"太后饼({CONSUMABLES_NUMBER['physical_food_max']}外攻)",
        f"煎饼果子({CONSUMABLES_NUMBER['physical_food_min']}外攻)"
    ]
}
POTIONS = {
    "力道": [
        f"上品大力丸({CONSUMABLES_NUMBER['major_potion_max']}力道)",
        f"中品大力丸({CONSUMABLES_NUMBER['major_potion_min']}力道)"
    ],
    "通用": [
        f"上品凝神散({CONSUMABLES_NUMBER['minor_potion_max']}破招)",
        f"上品活气散({CONSUMABLES_NUMBER['minor_potion_max']}加速)",
        f"上品破秽散({CONSUMABLES_NUMBER['minor_potion_max']}破防)",
        f"上品玉璃散({CONSUMABLES_NUMBER['minor_potion_max']}会心)",
        f"中品凝神散({CONSUMABLES_NUMBER['minor_potion_min']}破招)",
        f"中品活气散({CONSUMABLES_NUMBER['minor_potion_min']}加速)",
        f"中品破秽散({CONSUMABLES_NUMBER['minor_potion_min']}破防)",
        f"中品玉璃散({CONSUMABLES_NUMBER['minor_potion_min']}会心)"
    ],
    "外功": [
        f"上品亢龙散({CONSUMABLES_NUMBER['physical_potion_max']}外攻)",
        f"中品亢龙散({CONSUMABLES_NUMBER['physical_potion_min']}外攻)"
    ]
}
WEAPON_ENCHANTS = {
    "外功": [
        f"瀑沙熔锭({CONSUMABLES_NUMBER['weapon_enchant_max']}外攻)",
        f"瀑沙磨石({CONSUMABLES_NUMBER['weapon_enchant_min']}外攻)"
    ]
}
SNACKS = {
    "通用": [
        f"创意料理({CONSUMABLES_NUMBER['minor_snack_max']})无双",
        f"创意料理({CONSUMABLES_NUMBER['minor_snack_max']})会心",
        f"创意料理({CONSUMABLES_NUMBER['minor_snack_max']})破防",
    ],
    "外功": [
        f"创意料理({CONSUMABLES_NUMBER['physical_snack']})外攻"
    ]
}
WINES = {
    "通用": [f"女儿红·旬又三({CONSUMABLES_NUMBER['haste_wine']}加速)"],
    "力道": [f"汾酒·旬又三({CONSUMABLES_NUMBER['major_wine']}力道)"]

}
SPREADS = {
    "力道": [
        f"水晶芙蓉宴({CONSUMABLES_NUMBER['major_spread']}力道)"
    ],
    "外功": [
        f"玉笛谁家听落梅({CONSUMABLES_NUMBER['physical_spread']}外攻{CONSUMABLES_NUMBER['minor_spread']}会心/破招)"
    ]
}
