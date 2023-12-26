from base.skill import Skill
from base.status import Status
from general.recipes import DamageRecipe, CriticalRecipe, CDReductionRecipe, IntervalReductionRecipe, EmptyRecipe


class 剑气回复:
    def __init__(self, skills, value):
        self.skills = skills
        self.value = value

    def post_cast_effect(self, skill: Skill):
        skill.status.buffs["剑气"].increase(self.value)

    def __call__(self, status: Status):
        for skill in self.skills:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect)


class 云栖松剑气回复:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["云栖松剑气回复"].cast()

    def __call__(self, status: Status):
        status.skills["云栖松"].post_cast_effect.append(self.post_cast_effect)


RECIPES = {
    "听雷": [
        "听雷(5%伤害)", "听雷(4%伤害)", "听雷(3%伤害)", "听雷(3%会心)",
        "听雷(2%会心)"
    ],
    "啸日": [
        "啸日(10剑气)", "啸日(0.5持续)", "啸日(0.5持续)", "啸日(0.5持续)"
    ],
    "夕照雷峰": [
        "夕照雷峰(4%伤害)", "夕照雷峰(3%伤害)", "夕照雷峰(3%会心)", "夕照雷峰(2%伤害)",
        "夕照雷峰(-0.125读条)", "夕照雷峰(-0.125读条)"
    ],
    "云飞玉皇": [
        "云飞玉皇(4%伤害)", "云飞玉皇(3%伤害)", "云飞玉皇(-0.25读条)", "云飞玉皇(-0.25读条)",
        "云飞玉皇(3%会心)", "云飞玉皇(2%伤害)"
    ],
    "风来吴山": [
        "风来吴山(4%伤害)", "风来吴山(3%伤害)", "风来吴山(3%会心)", "风来吴山(2%伤害)",
        "风来吴山(2%会心)"
    ],
    "九溪弥烟": [
        "九溪弥烟(5%伤害)", "九溪弥烟(4%伤害)", "九溪弥烟(3%伤害)", "九溪弥烟(3%会心)"
    ],
    "黄龙吐翠": [
        "黄龙吐翠(5%伤害)", "黄龙吐翠(4%伤害)", "黄龙吐翠(6剑气)", "黄龙吐翠(4剑气)",
        "黄龙吐翠(3%伤害)", "黄龙吐翠(4%会心)", "黄龙吐翠(3%会心)", "黄龙吐翠(2%会心)"
    ],
    "云栖松": [
        "云栖松(5剑气)", "云栖松(-10冷却)", "云栖松(-10冷却)", "云栖松(气血恢复)"
    ]
}
RECIPE_GAINS = {
    "听雷(5%伤害)": DamageRecipe(["听雷"], 51 / 1024),
    "听雷(4%伤害)": DamageRecipe(["听雷"], 41 / 1024),
    "听雷(3%伤害)": DamageRecipe(["听雷"], 31 / 1024),
    "听雷(3%会心)": CriticalRecipe(["听雷"], 0.03),
    "听雷(2%会心)": CriticalRecipe(["听雷"], 0.02),

    "啸日(10剑气)": 剑气回复(["啸日"], 10),
    "啸日(0.5持续)": EmptyRecipe(),

    "夕照雷峰(4%伤害)": DamageRecipe(["夕照雷峰"], 41 / 1024),
    "夕照雷峰(3%伤害)": DamageRecipe(["夕照雷峰"], 31 / 1024),
    "夕照雷峰(3%会心)": CriticalRecipe(["夕照雷峰"], 0.03),
    "夕照雷峰(2%伤害)": DamageRecipe(["夕照雷峰"], 21 / 1024),
    "夕照雷峰(-0.125读条)": IntervalReductionRecipe(["夕照雷峰"], 2),

    "云飞玉皇(4%伤害)": DamageRecipe(["云飞玉皇"], 41 / 1024),
    "云飞玉皇(3%伤害)": DamageRecipe(["云飞玉皇"], 31 / 1024),
    "云飞玉皇(3%会心)": CriticalRecipe(["云飞玉皇"], 0.03),
    "云飞玉皇(2%伤害)": DamageRecipe(["云飞玉皇"], 21 / 1024),
    "云飞玉皇(-0.25读条)": IntervalReductionRecipe(["云飞玉皇"], 4),

    "风来吴山(4%伤害)": DamageRecipe(["风来吴山-持续", "风来吴山-引导"], 41 / 1024),
    "风来吴山(3%伤害)": DamageRecipe(["风来吴山-持续", "风来吴山-引导"], 31 / 1024),
    "风来吴山(3%会心)": CriticalRecipe(["风来吴山-持续", "风来吴山-引导"], 0.03),
    "风来吴山(2%伤害)": DamageRecipe(["风来吴山-持续", "风来吴山-引导"], 21 / 1024),

    "九溪弥烟(5%伤害)": DamageRecipe(["九溪弥烟"], 51 / 1024),
    "九溪弥烟(4%伤害)": DamageRecipe(["九溪弥烟"], 41 / 1024),
    "九溪弥烟(3%伤害)": DamageRecipe(["九溪弥烟"], 31 / 1024),
    "九溪弥烟(3%会心)": CriticalRecipe(["九溪弥烟"], 0.03),

    "黄龙吐翠(5%伤害)": DamageRecipe(["黄龙吐翠"], 51 / 1024),
    "黄龙吐翠(4%伤害)": DamageRecipe(["黄龙吐翠"], 41 / 1024),
    "黄龙吐翠(6剑气)": 剑气回复(["黄龙吐翠"], 6),
    "黄龙吐翠(4剑气)": 剑气回复(["黄龙吐翠"], 4),
    "黄龙吐翠(3%伤害)": DamageRecipe(["黄龙吐翠"], 31 / 1024),
    "黄龙吐翠(4%会心)": CriticalRecipe(["黄龙吐翠"], 0.04),
    "黄龙吐翠(3%会心)": CriticalRecipe(["黄龙吐翠"], 0.03),
    "黄龙吐翠(2%会心)": CriticalRecipe(["黄龙吐翠"], 0.02),

    "云栖松(5剑气)": 云栖松剑气回复(),
    "云栖松(-10冷却)": CDReductionRecipe(["云栖松"], 10 * 16),
    "云栖松(气血恢复)": EmptyRecipe()
}
