""" Weapon Enchant """
from base.status import Status


def physical_attack_power_enchant(value):
    def inner(status: Status):
        status.attribute.physical_attack_power_base += value

    return inner


""" Spread """


def major_spread(status: Status):
    status.attribute.strain_base += 1


def physical_spread(status: Status):
    status.attribute.physical_attack_power_base += 1
    status.attribute.all_critical_strike_base += 1
    status.attribute.surplus += 1


def tong_ze_spread():
    pass


def boiled_fish_spread(status: Status):
    status.attribute.surplus += 1
    status.attribute.strain_base += 1


def streamed_fish_spread(status: Status):
    status.attribute.strain_gain += 1


""" Major Food """


def strength_food(value):
    def inner(status: Status):
        status.attribute.strength_base += value

    return inner


""" Minor Food """


def surplus_food(value):
    def inner(status: Status):
        status.attribute.surplus += value

    return inner


def haste_food(value):
    def inner(status: Status):
        status.attribute.haste_base += value

    return inner


def physical_attack_power_food(value):
    def inner(status: Status):
        status.attribute.physical_attack_power_base += value

    return inner


def all_overcome_food(value):
    def inner(status: Status):
        status.attribute.physical_overcome_base += value

    return inner


def all_critical_strike_food(value):
    def inner(status: Status):
        status.attribute.all_critical_strike_base += value

    return inner


""" Major Potion """


def strength_potion(value):
    def inner(status: Status):
        status.attribute.strength_base += value

    return inner


""" Minor Potion """


def surplus_potion(value):
    def inner(status: Status):
        status.attribute.surplus += value

    return inner


def haste_potion(value):
    def inner(status: Status):
        status.attribute.haste_base += value

    return inner


def physical_attack_power_potion(value):
    def inner(status: Status):
        status.attribute.physical_attack_power_base += value

    return inner


def all_overcome_potion(value):
    def inner(status: Status):
        status.attribute.physical_overcome_base += value

    return inner


def all_critical_strike_potion(value):
    def inner(status: Status):
        status.attribute.all_critical_strike_base += value

    return inner


""" Wine """


def strength_wine(value):
    def inner(status: Status):
        status.attribute.strength_base += value

    return inner


""" Snack """
