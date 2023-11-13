from functools import cache


@cache
def defense(shield_base, shield_gain, shield_ignore_base, shield_ignore_gain,
            skill_shield_ignore_base, skill_shield_ignore_gain, shield_constant):
    shield = shield_base
    shield -= int(shield_base * (shield_ignore_base + skill_shield_ignore_base))
    shield += shield * shield_gain
    shield -= int(shield * (shield_ignore_gain + skill_shield_ignore_gain))
    return max(0, shield / (shield + shield_constant))


@cache
def base_result(damage_base, damage_rand, damage_gain):
    damage = damage_base + damage_rand / 2
    damage += damage * damage_gain
    return int(damage)


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
def init_result(damage_base, damage_rand, attack_power_cof, weapon_damage_cof, surplus_cof,
                damage_gain, attack_power_cof_gain, weapon_damage_cof_gain, surplus_cof_gain,
                attack_power, weapon_damage, surplus):
    return (base_result(damage_base, damage_rand, damage_gain) +
            attack_power_result(attack_power_cof, attack_power_cof_gain, attack_power) +
            weapon_damage_result(weapon_damage_cof, weapon_damage_cof_gain, weapon_damage) +
            surplus_result(surplus_cof, surplus_cof_gain, surplus))


@cache
def damage_addition_result(damage, damage_addition, skill_damage_addition):
    return int(damage * (1 + damage_addition + skill_damage_addition))


@cache
def overcome_result(damage, overcome, defense_reduction):
    return int(damage * (1 + overcome) * (1 - defense_reduction))


@cache
def critical_result(damage, critical_power, skill_critical_power):
    return int(damage * (critical_power + skill_critical_power))


@cache
def level_reduction_result(damage, level_reduction):
    return int(damage * (1 - level_reduction))


@cache
def strain_result(damage, strain):
    return int(damage * (1 + strain))


@cache
def pve_addition_result(damage, pve_addition, skill_pve_addition):
    return int(damage * (1 + pve_addition + skill_pve_addition))


@cache
def vulnerable_result(damage, vulnerable):
    return int(damage * (1 + vulnerable))


@cache
def hit_damage(damage_base, damage_rand, attack_power_cof, weapon_damage_cof, surplus_cof,
               damage_gain, attack_power_cof_gain, weapon_damage_cof_gain, surplus_cof_gain,
               attack_power, weapon_damage, surplus,
               damage_addition, skill_damage_addition, overcome, defense_reduction,
               critical_power, skill_critical_power,
               strain, level_reduction, pve_addition, skill_pve_addition, vulnerable):
    damage = init_result(damage_base, damage_rand, attack_power_cof, weapon_damage_cof, surplus_cof,
                         damage_gain, attack_power_cof_gain, weapon_damage_cof_gain, surplus_cof_gain,
                         attack_power, weapon_damage, surplus, )

    damage = damage_addition_result(damage, damage_addition, skill_damage_addition)
    damage = overcome_result(damage, overcome, defense_reduction)
    damage = critical_result(damage, critical_power, skill_critical_power)
    damage = level_reduction_result(damage, level_reduction)
    damage = strain_result(damage, strain)
    damage = pve_addition_result(damage, pve_addition, skill_pve_addition)
    damage = vulnerable_result(damage, vulnerable)

    return damage



