from base.skill import Skill
from base.status import Status
from general.recipes import DamageRecipe, CriticalRecipe, CDReductionRecipe, IntervalReductionRecipe, EmptyRecipe


class 暴雨梨花针气魄:
    def __init__(self, skill):
        self.skill = skill

    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.buffs["气魄"].trigger()

    def __call__(self, status: Status):
        status.skills[self.skill].post_hit_effect.append(self.post_hit_effect)


RECIPES = {
    "孔雀翎": [
        "孔雀翎(-1冷却)", "孔雀翎(-1冷却)", "孔雀翎(-1冷却)", "孔雀翎(+1距离)"
    ],
    "暴雨梨花针": [
        "暴雨梨花针(5%伤害)", "暴雨梨花针(4%伤害)", "暴雨梨花针(4%会心)", "暴雨梨花针(气魄)",
        "暴雨梨花针(3%会心)", "暴雨梨花针(3%伤害)"
    ],
    "蚀肌弹": [
        "蚀肌弹(5%伤害)", "蚀肌弹(4%伤害)", "蚀肌弹(-0.125读条)", "蚀肌弹(-0.125读条)",
        "蚀肌弹(4%会心)", "蚀肌弹(3%会心)", "蚀肌弹(3%伤害)"
    ],
    "天绝地灭": [
        "天绝地灭(5%伤害)", "天绝地灭(4%伤害)", "天绝地灭(3%伤害)"
    ],
    "暗藏杀机": [
        "暗藏杀机(5%伤害)", "暗藏杀机(4%伤害)", "暗藏杀机(3%伤害)", "暗藏杀机(2%会心)",
    ]
}

RECIPE_GAINS = {
    "孔雀翎(-1冷却)": CDReductionRecipe(["孔雀翎"], 16),
    "孔雀翎(+1距离)": EmptyRecipe(),

    "暴雨梨花针(5%伤害)": DamageRecipe(["暴雨梨花针"], 51 / 1024),
    "暴雨梨花针(4%伤害)": DamageRecipe(["暴雨梨花针"], 41 / 1024),
    "暴雨梨花针(4%会心)": CriticalRecipe(["暴雨梨花针"], 0.04),
    "暴雨梨花针(3%伤害)": DamageRecipe(["暴雨梨花针"], 31 / 1024),
    "暴雨梨花针(3%会心)": CriticalRecipe(["暴雨梨花针"], 0.03),
    "暴雨梨花针(气魄)": 暴雨梨花针气魄("暴雨梨花针"),

    "蚀肌弹(5%伤害)": DamageRecipe(["蚀肌弹"], 51 / 1024),
    "蚀肌弹(4%伤害)": DamageRecipe(["蚀肌弹"], 41 / 1024),
    "蚀肌弹(4%会心)": CriticalRecipe(["蚀肌弹"], 0.04),
    "蚀肌弹(3%伤害)": DamageRecipe(["蚀肌弹"], 31 / 1024),
    "蚀肌弹(3%会心)": CriticalRecipe(["蚀肌弹"], 0.03),
    "蚀肌弹(-0.125读条)": IntervalReductionRecipe(["蚀肌弹"], 2),

    "天绝地灭(5%伤害)": DamageRecipe(["天绝地灭-伤害"], 51 / 1024),
    "天绝地灭(4%伤害)": DamageRecipe(["天绝地灭-伤害"], 41 / 1024),
    "天绝地灭(3%伤害)": DamageRecipe(["天绝地灭-伤害"], 31 / 1024),
    "天绝地灭(+1范围)": EmptyRecipe(),

    "暗藏杀机(5%伤害)": DamageRecipe(["图穷匕见"], 51 / 1024),
    "暗藏杀机(4%伤害)": DamageRecipe(["图穷匕见"], 41 / 1024),
    "暗藏杀机(3%伤害)": DamageRecipe(["图穷匕见"], 31 / 1024),
    "暗藏杀机(2%会心)": CriticalRecipe(["图穷匕见"], 0.02),
}
