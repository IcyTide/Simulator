from base.skill import Skill
from base.status import Status
from general.recipes import DamageRecipe, CriticalRecipe, CDReductionRecipe, TickIncreaseRecipe, EmptyRecipe


class 回复禅那:
    def __init__(self, skill):
        self.skill = skill

    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["禅那"].increase(1)

    def __call__(self, status: Status):
        status.skills[self.skill].post_cast_effect.append(self.post_cast_effect)


RECIPES = {
    "普渡四方": [
        "普渡四方(5%伤害)", "普渡四方(4%伤害)", "普渡四方(3%伤害)", "普渡四方(-0.25冷却)", "普渡四方(-0.25冷却)"
    ],
    "韦陀献杵": [
        "韦陀献杵(5%伤害)", "韦陀献杵(4%伤害)", "韦陀献杵(4%会心)", "韦陀献杵(回复禅那)",
        "韦陀献杵(3%会心)", "韦陀献杵(2%会心)", "韦陀献杵(3%伤害)"
    ],
    "横扫六合": [
        "横扫六合(50%伤害)", "横扫六合(+6持续)", "横扫六合(+1目标)", "横扫六合(-20%消耗)"
    ],
    "捕风式": [
        "捕风式(15%伤害)", "捕风式(10%伤害)", "捕风式(-0.5冷却)", "捕风式(-0.5冷却)",
        "捕风式(10%伤害)"
    ],
    "拿云式": [
        "拿云式(5%伤害)", "拿云式(4%伤害)", "拿云式(3%伤害)", "拿云式(回复禅那)",
    ],
    "守缺式": [
        "守缺式(5%伤害)", "守缺式(4%伤害)", "守缺式(4%会心)", "守缺式(3%伤害)",
        "守缺式(3%会心)", "守缺式(2%会心)"
    ]
}

RECIPE_GAINS = {
    "普渡四方(5%伤害)": DamageRecipe(["普渡四方", "普渡四方-外功"], 51 / 1024),
    "普渡四方(4%伤害)": DamageRecipe(["普渡四方", "普渡四方-外功"], 41 / 1024),
    "普渡四方(3%伤害)": DamageRecipe(["普渡四方", "普渡四方-外功"], 31 / 1024),
    "普渡四方(-0.25冷却)": CDReductionRecipe(["普渡四方", "普渡四方-外功"], 4),

    "韦陀献杵(5%伤害)": DamageRecipe(["韦陀献杵", "韦陀献杵-外功"], 51 / 1024),
    "韦陀献杵(4%伤害)": DamageRecipe(["韦陀献杵", "韦陀献杵-外功"], 41 / 1024),
    "韦陀献杵(4%会心)": CriticalRecipe(["韦陀献杵", "韦陀献杵-外功"], 0.04),
    "韦陀献杵(3%伤害)": DamageRecipe(["韦陀献杵", "韦陀献杵-外功"], 31 / 1024),
    "韦陀献杵(3%会心)": CriticalRecipe(["韦陀献杵", "韦陀献杵-外功"], 0.03),
    "韦陀献杵(2%会心)": CriticalRecipe(["韦陀献杵", "韦陀献杵-外功"], 0.02),
    "韦陀献杵(回复禅那)": 回复禅那("韦陀献杵"),

    "横扫六合(50%伤害)": DamageRecipe(["横扫六合", "横扫六合-外功"], 512 / 1024),
    "横扫六合(+6持续)": TickIncreaseRecipe(["横扫六合-持续"], 3),
    "横扫六合(+1目标)": EmptyRecipe(),
    "横扫六合(-20%消耗)": EmptyRecipe(),

    "捕风式(15%伤害)": DamageRecipe(["捕风式"], 150 / 1024),
    "捕风式(10%伤害)": DamageRecipe(["捕风式"], 102 / 1024),
    "捕风式(-0.5冷却)": CDReductionRecipe(["捕风式"], 8),

    "拿云式(5%伤害)": DamageRecipe(["拿云式"], 51 / 1024),
    "拿云式(4%伤害)": DamageRecipe(["拿云式"], 41 / 1024),
    "拿云式(3%伤害)": DamageRecipe(["拿云式"], 31 / 1024),
    "拿云式(回复禅那)": 回复禅那("拿云式"),

    "守缺式(5%伤害)": DamageRecipe(["守缺式"], 51 / 1024),
    "守缺式(4%伤害)": DamageRecipe(["守缺式"], 41 / 1024),
    "守缺式(4%会心)": CriticalRecipe(["守缺式"], 0.04),
    "守缺式(3%伤害)": DamageRecipe(["守缺式"], 31 / 1024),
    "守缺式(3%会心)": CriticalRecipe(["守缺式"], 0.03),
    "守缺式(2%会心)": CriticalRecipe(["守缺式"], 0.02),
}
