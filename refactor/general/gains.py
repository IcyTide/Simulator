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
