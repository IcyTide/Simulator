from base.status import Status


def damage_recipe(skills, value):
    def inner(status: Status):
        for skill in skills:
            status.skills[skill].skill_damage_addition += value

    return inner


def critical_recipe(skills, value):
    def inner(status: Status):
        for skill in skills:
            status.skills[skill].skill_critical_strike += value

    return inner
