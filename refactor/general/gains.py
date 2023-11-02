from base.status import Status

""" permanent gain """


def han_ru_lei(status: Status):
    status.attribute.physical_attack_power_gain += 0.1


def po_feng(status: Status):
    status.attribute.target.physical_shield_base -= 32


def xiu_qi(status: Status):
    status.attribute.strength_base += 32


def enchant():
    pass


def food():
    pass


def potions():
    pass


""" periodic gain """


def special_enchant_hat_gain(value):
    def inner(status: Status):
        status.attribute.physical_overcome_base += value
        status.attribute.magical_overcome_base += value

    return inner


def special_enchant_jacket_gain(value1, value2):
    def inner(status: Status):
        status.attribute.magical_attack_power_base += value1
        status.attribute.physical_attack_power_base += value2

    return inner


def special_enchant_belt_gain(status: Status):
    pass


def special_enchant_wrist_gain(status: Status):
    pass


def special_enchant_shoes_gain(status: Status):
    pass
