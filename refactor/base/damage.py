from functools import cache


@cache
def defense(shield_base, shield_gain, shield_ignore_base, shield_ignore_gain,
            skill_shield_ignore_base, skill_shield_ignore_gain, shield_constant):
    shield = shield_base
    shield -= shield_base * (shield_ignore_base + skill_shield_ignore_base)
    shield += shield_gain
    shield -= shield * (shield_ignore_gain + skill_shield_ignore_gain)
    return shield / (shield + shield_constant)


@cache
def hit_damage(base_damage, rand_damage, attack_power_cof, weapon_damage_cof, surplus_cof,
               base_damage_gain, rand_damage_gain, attack_power_cof_gain, weapon_damage_cof_gain, surplus_cof_gain,
               attack_power, weapon_damage, surplus, strain, overcome,
               damage_addition, pve_addition, skill_damage_addition, skill_pve_addition,
               defense_reduction, level_reduction, vulnerable):
    base_damage += base_damage * base_damage_gain
    rand_damage += rand_damage * rand_damage_gain
    attack_power_cof += attack_power_cof * attack_power_cof_gain
    weapon_damage_cof += weapon_damage_cof * weapon_damage_cof_gain
    surplus_cof += surplus_cof * surplus_cof_gain

    damage = base_damage + rand_damage / 2
    damage = damage + attack_power * attack_power_cof
    damage = damage + weapon_damage * weapon_damage_cof
    damage = damage + surplus * surplus_cof

    damage = damage * (1 + strain) * (1 + overcome)
    damage += damage * (damage_addition + skill_damage_addition)
    damage += damage * (pve_addition + skill_pve_addition)
    damage += damage * vulnerable

    damage -= damage * defense_reduction
    damage -= damage * level_reduction
    return damage


@cache
def critical_damage(damage, critical_power, skill_critical_power):
    return damage * (critical_power + skill_critical_power)
