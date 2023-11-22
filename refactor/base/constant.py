INT_SCALE = 1024

FRAME_PER_SECOND = 16

LEVEL = 120
LEVEL_SCALE = 450
LEVEL_CONSTANT = 45750
LEVEL_REDUCTION = 0.05

DAMAGE_SCALE = 16
DOT_DAMAGE_SCALE = 12 * DAMAGE_SCALE * DAMAGE_SCALE
PHYSICAL_DAMAGE_SCALE = 10

MAX_GCD_GROUP = 10

CRITICAL_STRIKE_SCALE = 9.530 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
CRITICAL_POWER_SCALE = 3.335 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
OVERCOME_SCALE = 9.530 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
HASTE_SCALE = 11.695 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
STRAIN_SCALE = 9.189 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
SURPLUS_SCALE = 13.192

SHIELD_SCALE = 5.091

SHIELD_BASE_MAP = {
    124: 27550
}

MAJOR_BASE = 41
CRITICAL_POWER_BASE = 1.75

AGILITY_TO_CRITICAL_STRIKE = 655 / INT_SCALE
# STRENGTH_TO_ATTACK_POWER = 153 / INT_SCALE
STRENGTH_TO_ATTACK_POWER = 0.15
# STRENGTH_TO_OVERCOME = 307 / INT_SCALE
STRENGTH_TO_OVERCOME = 0.3
SPIRIT_TO_CRITICAL_STRIKE = 655 / INT_SCALE
SPUNK_TO_ATTACK_POWER = 184 / INT_SCALE
SPUNK_TO_OVERCOME = 307 / INT_SCALE


def ATTACK_POWER_COF(cof):
    return cof / DAMAGE_SCALE / PHYSICAL_DAMAGE_SCALE


def DOT_ATTACK_POWER_COF(cof, interval):
    return cof * interval / DOT_DAMAGE_SCALE / PHYSICAL_DAMAGE_SCALE


def WEAPON_DAMAGE_COF(cof):
    return cof / INT_SCALE


def SURPLUS_COF(cof):
    return ((cof + int(cof < 0)) / INT_SCALE + INT_SCALE) / INT_SCALE * SURPLUS_SCALE
