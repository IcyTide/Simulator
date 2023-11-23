from functools import cache

from base.constant import LEVEL_REDUCTION


@cache
def level_residual(level, target_level):
    return LEVEL_REDUCTION * (target_level - level)


@cache
def defense(shield_base, shield_gain, shield_ignore, shield_constant):
    shield = shield_base
    shield += int(shield * shield_gain)
    shield -= int(shield * shield_ignore)
    return max(0, shield / (shield + shield_constant))


@cache
def base_result(damage_base, damage_rand, damage_gain):
    damage = damage_base + damage_rand / 2
    damage += damage * damage_gain
    return int(damage)


@cache
def attack_power_result(attack_power_cof, attack_power_cof_gain, attack_power):
    attack_power_cof += attack_power_cof * attack_power_cof_gain
    damage = attack_power * attack_power_cof
    return int(damage)


@cache
def weapon_damage_result(weapon_damage_cof, weapon_damage_cof_gain, weapon_damage):
    weapon_damage_cof += weapon_damage_cof * weapon_damage_cof_gain
    damage = weapon_damage * weapon_damage_cof
    return int(damage)


@cache
def surplus_result(surplus_cof, surplus_cof_gain, surplus):
    surplus_cof += surplus_cof * surplus_cof_gain
    damage = surplus * surplus_cof
    return int(damage)


@cache
def init_result(damage_base, damage_rand, damage_gain,
                attack_power_cof, attack_power_cof_gain, attack_power,
                weapon_damage_cof, weapon_damage_cof_gain, weapon_damage,
                surplus_cof, surplus_cof_gain, surplus):
    return (base_result(damage_base, damage_rand, damage_gain) +
            attack_power_result(attack_power_cof, attack_power_cof_gain, attack_power) +
            weapon_damage_result(weapon_damage_cof, weapon_damage_cof_gain, weapon_damage) +
            surplus_result(surplus_cof, surplus_cof_gain, surplus))


@cache
def damage_addition_result(damage, damage_addition):
    return int(damage * (1 + damage_addition))


@cache
def overcome_result(damage, overcome, shield_base, shield_gain, shield_ignore, shield_constant):
    defense_reduction = defense(shield_base, shield_gain, shield_ignore, shield_constant)
    return int(damage * (1 + overcome) * (1 - defense_reduction))


@cache
def critical_result(damage, critical_power):
    return int(damage * critical_power)


@cache
def level_reduction_result(damage, level, target_level):
    level_reduction = level_residual(level, target_level)
    return int(damage * (1 - level_reduction))


@cache
def strain_result(damage, strain):
    return int(damage * (1 + strain))


@cache
def pve_addition_result(damage, pve_addition):
    return int(damage * (1 + pve_addition))


@cache
def vulnerable_result(damage, vulnerable):
    return int(damage * (1 + vulnerable))


def physical_damage(attribute, params):
    damage = init_result(
        params['damage_base'], params['damage_rand'], params['damage_gain'],
        params['attack_power_cof'], params['attack_power_cof_gain'], attribute.physical_attack_power,
        params['weapon_damage_cof'], params['weapon_damage_cof_gain'], attribute.weapon_damage,
        params['surplus_cof'], params['surplus_cof_gain'], attribute.surplus
    )

    damage = damage_addition_result(damage, params['damage_addition'])
    damage = overcome_result(damage, attribute.physical_overcome,
                             params['shield_base'], params['shield_gain'], params['shield_ignore'],
                             params['shield_constant'])
    if params['critical']:
        damage = critical_result(damage, attribute.physical_critical_power)
    damage = level_reduction_result(damage, params['level'], params['target_level'])
    damage = strain_result(damage, attribute.strain)
    damage = pve_addition_result(damage, params['pve_addition'])
    damage = vulnerable_result(damage, params['vulnerable'])

    return params['skill'], params['critical'], damage
