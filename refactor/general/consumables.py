from base.status import Status

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


def surplus_food(value):
    return {"surplus": value}


def haste_food(value):
    return {"haste_base": value}


def all_overcome_food(value):
    return {"physical_overcome_base": value}


def all_critical_strike_food(value):
    return {"all_critical_strike_base": value}


def physical_attack_power_food(value):
    return {"physical_attack_power_base": value}


""" Major Potion """


def strength_potion(value):
    return {"strength_base": value}


""" Minor Potion """


def surplus_potion(value):
    return {"surplus": value}


def haste_potion(value):
    return {"haste_base": value}


def all_overcome_potion(value):
    return {"physical_overcome_base": value}


def all_critical_strike_potion(value):
    return {"all_critical_strike_base": value}


def physical_attack_power_potion(value):
    return {"physical_attack_power_base": value}


""" Wine """


def strength_wine(value):
    def inner(status: Status):
        status.attribute.strength_base += value

    return inner


""" Snack """
