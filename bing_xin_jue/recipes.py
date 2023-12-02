from base.skill import Skill
from base.status import Status
from general.recipes import DamageRecipe, CriticalRecipe, CDReductionRecipe


class JianQiChangJiang:
    @staticmethod
    def jian_qi_chang_jiang_post_cast(self: Skill):
        if self.roll < 0.3:
            self.recharge()
            self.status.skills["急曲·持续"].cast()

    def __call__(self, status: Status):
        status.skills["剑气长江"].post_cast_effect.append(self.jian_qi_chang_jiang_post_cast)


class FanYinJiJie:
    @staticmethod
    def fan_yin_ji_jie_post_cast(self: Skill):
        self.status.buffs["满堂"].trigger()

    @staticmethod
    def man_tang_post_hit(self: Skill):
        if self.status.stacks["满堂"]:
            self.status.buffs["满堂"].consume()

    def __call__(self, status: Status):
        status.skills["繁音急节"].post_cast_effect.append(self.fan_yin_ji_jie_post_cast)
        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.man_tang_post_hit)


RECIPES = {
    "玳弦急曲": [
        "玳弦急曲(5%伤害)", "玳弦急曲(4%伤害)", "玳弦急曲(3%伤害)"
    ],
    "剑气长江": [
        "剑气长江(6%伤害)", "剑气长江(4%伤害)", "剑气长江(3%会心)", "剑气长江(2%会心)", "剑气长江(-1冷却)",
        "剑气长江(-1冷却)", "剑气长江(30%急曲)"
    ],
    "繁音急节": [
        "繁音急节(-3冷却)", "繁音急节(-2冷却)", "繁音急节(-1冷却)", "繁音急节(满堂)"
    ],
    "江海凝光": [
        "江海凝光(15%伤害)", "江海凝光(15%伤害)", "江海凝光(3%会心)", "江海凝光(2%会心)"
    ],
}

RECIPE_GAINS = {
    "玳弦急曲(5%伤害)": DamageRecipe(["玳弦急曲", "玳弦急曲·新妆"], 51 / 1024),
    "玳弦急曲(4%伤害)": DamageRecipe(["玳弦急曲", "玳弦急曲·新妆"], 41 / 1024),
    "玳弦急曲(3%伤害)": DamageRecipe(["玳弦急曲", "玳弦急曲·新妆"], 31 / 1024),

    "剑气长江(6%伤害)": DamageRecipe(["剑气长江"], 61 / 1024),
    "剑气长江(4%伤害)": DamageRecipe(["剑气长江"], 31 / 1024),
    "剑气长江(3%会心)": CriticalRecipe(["剑气长江"], 0.03),
    "剑气长江(2%会心)": CriticalRecipe(["剑气长江"], 0.02),
    "剑气长江(-1冷却)": CDReductionRecipe(["剑气长江"], 16),
    "剑气长江(30%急曲)": JianQiChangJiang(),

    "繁音急节(-3冷却)": CDReductionRecipe(["繁音急节"], 48),
    "繁音急节(-2冷却)": CDReductionRecipe(["繁音急节"], 32),
    "繁音急节(-1冷却)": CDReductionRecipe(["繁音急节"], 16),
    "繁音急节(满堂)": FanYinJiJie(),

    "江海凝光(15%伤害)": DamageRecipe(["江海凝光"], 154 / 1024),
    "江海凝光(3%会心)": CriticalRecipe(["江海凝光"], 0.03),
    "江海凝光(2%会心)": CriticalRecipe(["江海凝光"], 0.02),
}
