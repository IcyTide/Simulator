from base.status import Status


class DamageRecipe:
    def __init__(self, skills, value):
        self.skills = skills
        self.value = value

    def __call__(self, status: Status):
        for skill in self.skills:
            status.skills[skill].skill_damage_addition += self.value


class CriticalRecipe:
    def __init__(self, skills, value):
        self.skills = skills
        self.value = value

    def __call__(self, status: Status):
        for skill in self.skills:
            status.skills[skill].skill_critical_strike += self.value
