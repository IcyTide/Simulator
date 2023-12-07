from base.buff import Buff
from base.skill import Skill
from base.status import Status


class 伤春:
    def __call__(self, status: Status):
        status.skills["剑破虚空"].skill_damage_addition += 102 / 1024


class 青梅嗅:
    def __call__(self, status: Status):
        status.skills["玳弦急曲"].skill_critical_strike += 0.1
        status.skills["玳弦急曲"].skill_critical_power += 102 / 1024


class 千里冰封:
    def __call__(self, status: Status):
        status.skills["剑破虚空"].skill_critical_strike += 0.1
        status.skills["剑破虚空"].skill_critical_power += 102 / 1024


class 惊寒:
    def __call__(self, status: Status):
        status.skills["剑气长江"].skill_damage_addition += 154 / 1024
        status.skills["江海凝光"].skill_damage_addition += 154 / 1024


class 新妆:
    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.skills["玳弦急曲-新妆"].cast()

    def __call__(self, status: Status):
        status.skills["玳弦急曲"].ji_qu = False
        status.skills["玳弦急曲"].interval_base = 13
        status.skills["玳弦急曲"].post_hit_effect.append(self.post_hit_effect)


class 青梅:
    def __call__(self, status: Status):
        status.skills["急曲-持续"].attack_power_cof_gain += 0.15


class 枕上:
    @staticmethod
    def critical_hit_effect(self: Skill):
        self.status.buffs["枕上"].trigger()

    def __call__(self, status: Status):
        related_skills = ["剑破虚空", "剑气长江", "玳弦急曲", "剑影留痕"]
        for skill in related_skills:
            status.skills[skill].critical_hit_effect.append(self.critical_hit_effect)


class 生莲:
    def __call__(self, status: Status):
        status.skills["剑破虚空"].skill_damage_addition += 358 / 1024


class 广陵月:
    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["广陵月"]:
            self.status.skills["广陵月-伤害"].cast()

    def __call__(self, status: Status):
        status.skills["广陵月"].activate = True
        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.post_hit_effect)


class 流玉:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.skills["流玉-持续"].cast()
        self.status.buffs["流玉"].trigger()

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        if self.status.stacks["流玉"]:
            self.status.buffs["流玉"].clear()

    def __call__(self, status: Status):
        status.skills["剑影留痕"].cd_base = 15 * 16
        status.skills["剑影留痕"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["玳弦急曲"].post_cast_effect.append(self.post_cast_effect_consume)


class 钗燕:
    @staticmethod
    def post_cast_effect(self: Skill):
        buff = self.status.buffs["钗燕-计数"]
        if self.name in buff.count_list:
            buff.clear()
        else:
            buff.count_list.append(self.name)
            buff.trigger()

    def __call__(self, status: Status):
        status.skills["剑影留痕"].cd_base = 15 * 16
        related_skills = ["江海凝光", "玳弦急曲", "剑破虚空", "剑气长江", "剑影留痕"]
        for skill in related_skills:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect)


class 元君:
    def __call__(self, status: Status):
        status.attribute.magical_critical_strike_gain += 0.1 * 0.5
        status.attribute.magical_critical_power_gain += 102 / 1024 * 0.5


class 霜风:
    def __call__(self, status: Status):
        status.attribute.spirit_gain += 102 / 1024


class 盈袖:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["盈袖"].trigger()

    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["盈袖"]:
            self.status.skills["盈袖"].cast()

    def __call__(self, status: Status):
        status.skills["繁音急节"].post_cast_effect.append(self.post_cast_effect)
        status.skills["玳弦急曲"].post_hit_effect.append(self.post_hit_effect)


class 化冰:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["化冰"].trigger()

    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.buffs["化冰-计数"].trigger()

    def __call__(self, status: Status):
        status.skills["心鼓弦"].cd_base = 120 * 16
        status.skills["心鼓弦"].post_cast_effect.append(self.post_cast_effect)
        status.skills["玳弦急曲"].post_hit_effect.append(self.post_hit_effect)


class 夜天:
    @staticmethod
    def critical_hit_effect(self: Skill):
        self.status.buffs["夜天"].trigger()

    def __call__(self, status: Status):
        status.skills["剑气长江"].critical_hit_effect.append(self.critical_hit_effect)


class 琼霄:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["剑神无我"].trigger()

    def __call__(self, status: Status):
        status.skills["婆罗门"].post_cast_effect.append(self.post_cast_effect)


class 凝华:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.buffs["凝华"].trigger()

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        if stack := self.status.stacks["凝华"]:
            self.status.skills["凝华"].cast(stack)
            for _ in range(3):
                self.status.skills["凝华·明"].cast(stack)
            self.status.buffs["凝华"].clear()

    def __call__(self, status: Status):
        status.skills["江海凝光"].cd_base += 4 * 16
        status.skills["江海凝光"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["剑气长江"].post_cast_effect.append(self.post_cast_effect_consume)


class 霜降:
    @staticmethod
    def add_effect(self: Buff):
        self.status.buffs["霜降"].clear()
        self.status.buffs["霜降"].trigger(self.status.stacks[self.name])

    @staticmethod
    def remove_effect(self: Buff):
        self.status.buffs["霜降"].clear()

    def __call__(self, status: Status):
        status.buffs["急曲-持续"].add_effect.append(self.add_effect)
        status.buffs["急曲-持续"].remove_effect.append(self.remove_effect)


TALENTS = [
    ["伤春", "青梅嗅"],
    ["千里冰封", "惊寒"],
    ["新妆"],
    ["青梅"],
    ["枕上"],
    ["广陵月", "生莲"],
    ["流玉"],
    ["钗燕", "元君"],
    ["盈袖", "霜风"],
    ["化冰"],
    ["夜天", "琼霄"],
    ["凝华", "霜降"]
]
TALENT_GAINS = {
    "伤春": 伤春(),
    "青梅嗅": 青梅嗅(),
    "千里冰封": 千里冰封(),
    "惊寒": 惊寒(),
    "新妆": 新妆(),
    "青梅": 青梅(),
    "枕上": 枕上(),
    "生莲": 生莲(),
    "广陵月": 广陵月(),
    "流玉": 流玉(),
    "钗燕": 钗燕(),
    "元君": 元君(),
    "霜风": 霜风(),
    "盈袖": 盈袖(),
    "化冰": 化冰(),
    "夜天": 夜天(),
    "琼霄": 琼霄(),
    "凝华": 凝华(),
    "霜降": 霜降(),
}
