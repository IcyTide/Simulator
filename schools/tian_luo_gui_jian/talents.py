from base.buff import Buff
from base.skill import Skill, MagicalDamage
from base.status import Status


class 血影留痕:
    @staticmethod
    def post_hit_effect_trigger(self: Skill):
        self.status.buffs["血影留痕"].trigger()

    @staticmethod
    def post_hit_effect_consume_1(self: Skill):
        if self.status.stacks["血影留痕"]:
            self.status.skills["血影留痕-天绝地灭"].cast()

    @staticmethod
    def post_hit_effect_consume_2(self: Skill):
        if self.status.stacks["血影留痕"]:
            self.status.skills["血影留痕-图穷匕见"].cast()

    def __call__(self, status: Status):
        status.skills["连弩"].post_hit_effect.append(self.post_hit_effect_trigger)
        status.skills["天绝地灭-伤害"].post_hit_effect.append(self.post_hit_effect_consume_1)
        status.skills["图穷匕见"].post_hit_effect.append(self.post_hit_effect_consume_2)


class 天风汲雨:
    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["天风汲雨"]:
            self.status.skills["天风汲雨"].cast()
        self.status.buffs["天风汲雨"].trigger()

    def __call__(self, status: Status):
        for name in ["天绝地灭-持续-一", "天绝地灭-持续-二", "天绝地灭-持续-三", "天绝地灭-诡鉴-一", "天绝地灭-诡鉴-二"]:
            status.skills[name].tick_base -= 2
            status.buffs[name].duration -= 6 * 16
        # status.skills["天绝地灭-伤害"].post_hit_effect.append(self.post_hit_effect)


class 弩击急骤:
    @staticmethod
    def critical_hit_effect(self: Skill):
        self.status.buffs["弩心"].trigger()

    def __call__(self, status: Status):
        status.skills["连弩"].critical_hit_effect.append(self.critical_hit_effect)


class 擘两分星:
    @staticmethod
    def increase_effect(self: Buff):
        if self.status.stacks[self.name] >= 80:
            self.status.buffs["擘两分星-内功伤害"].clear()
            self.status.buffs["擘两分星-陷阱伤害"].trigger()
        elif 20 < self.status.stacks[self.name] < 80:
            self.status.buffs["擘两分星-内功伤害"].trigger()
            self.status.buffs["擘两分星-陷阱伤害"].trigger()
        else:
            self.status.buffs["擘两分星-内功伤害"].trigger()
            self.status.buffs["擘两分星-陷阱伤害"].clear()

    @staticmethod
    def decrease_effect(self: Buff):
        if self.status.stacks[self.name] >= 80:
            self.status.buffs["擘两分星-内功伤害"].clear()
            self.status.buffs["擘两分星-陷阱伤害"].trigger()
        elif 20 < self.status.stacks[self.name] < 80:
            self.status.buffs["擘两分星-内功伤害"].trigger()
            self.status.buffs["擘两分星-陷阱伤害"].trigger()
        else:
            self.status.buffs["擘两分星-内功伤害"].trigger()
            self.status.buffs["擘两分星-陷阱伤害"].clear()

    def __call__(self, status: Status):
        status.buffs["神机"].increase_effect.append(self.increase_effect)
        status.buffs["神机"].decrease_effect.append(self.decrease_effect)


class 千机之威:
    def __call__(self, status: Status):
        status.attribute.magical_attack_power_gain += 154 / 1024
        status.attribute.physical_attack_power_gain += 154 / 1024


class 流星赶月:
    @staticmethod
    def critical_hit_effect(self: Skill):
        if not self.status.stacks["流星赶月-冷却"]:
            self.status.buffs["神机"].increase(30)
            self.status.buffs["流星赶月-冷却"].trigger()

    def __call__(self, status: Status):
        status.skills["暴雨梨花针"].skill_critical_strike += 0.1
        status.skills["暴雨梨花针"].skill_critical_power += 102 / 1024


class 聚精凝神:
    @staticmethod
    def add_effect(self: Buff):
        self.status.buffs["聚精凝神"].trigger()

    @staticmethod
    def remove_effect(self: Buff):
        self.status.buffs["聚精凝神"].clear()

    def __call__(self, status: Status):
        status.buffs["心无旁骛"].duration += 5 * 16
        status.buffs["心无旁骛"].add_effect.append(self.add_effect)
        status.buffs["心无旁骛"].remove_effect.append(self.remove_effect)


class 化血迷心:
    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.skills["化血迷心"].cast()

    def __call__(self, status: Status):
        for skill in ["蚀肌弹", "暴雨梨花针", "连弩"]:
            status.skills[skill].post_hit_effect.append(self.post_hit_effect)
        status.skills["化血"].tick_base *= 2
        status.skills["化血"].attack_power_cof_gain += 1


class 杀机断魂:
    @staticmethod
    def add_effect_1(self: Buff):
        self.status.buffs["杀机断魂-千机变"].trigger()

    @staticmethod
    def remove_effect_1(self: Buff):
        self.status.buffs["杀机断魂-千机变"].consume()

    @staticmethod
    def add_effect_2(self: Buff):
        self.status.buffs["杀机断魂-天绝地灭"].trigger()

    @staticmethod
    def remove_effect_2(self: Buff):
        self.status.buffs["杀机断魂-天绝地灭"].consume()

    @staticmethod
    def add_effect_3(self: Buff):
        self.status.buffs["杀机断魂-暗藏杀机"].trigger()

    @staticmethod
    def remove_effect_3(self: Buff):
        self.status.buffs["杀机断魂-暗藏杀机"].consume()

    def __call__(self, status: Status):
        for buff in ["天绝地灭-持续-一", "天绝地灭-持续-二", "天绝地灭-持续-三", "天绝地灭-诡鉴-一", "天绝地灭-诡鉴-二"]:
            status.buffs[buff].add_effect.append(self.add_effect_1)
            status.buffs[buff].remove_effect.append(self.remove_effect_1)
        for buff in ["暗藏杀机-一", "暗藏杀机-二", "暗藏杀机-三"]:
            status.buffs[buff].add_effect.append(self.add_effect_2)
            status.buffs[buff].remove_effect.append(self.remove_effect_2)
        status.buffs["千机变"].add_effect.append(self.add_effect_3)
        status.buffs["千机变"].remove_effect.append(self.remove_effect_3)


class 秋风散影:
    def __call__(self, status: Status):
        status.attribute.physical_critical_strike_gain += 0.1
        status.attribute.physical_critical_power_gain += 102 / 1024


class 雀引彀中:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["暗藏杀机-一"].trigger()
        self.status.buffs["暗藏杀机-二"].trigger()
        self.status.buffs["暗藏杀机-三"].trigger()

    def __call__(self, status: Status):
        status.skills["孔雀翎"].post_cast_effect.append(self.post_cast_effect)


class 曙色催寒:
    @staticmethod
    def critical_hit_effect(self: Skill):
        self.status.buffs["催寒"].trigger()

    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.buffs["催寒"].consume()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_hit:
                skill.critical_hit_effect.append(self.critical_hit_effect)
                skill.post_hit_effect.append(self.post_hit_effect)


class 诡鉴冥微:
    @staticmethod
    def post_cast_effect(self: Skill):
        if (self.status.stacks["诡鉴冥微-一"] and not self.status.stacks["诡鉴冥微-冷却-一"]
                and not self.status.intervals["天绝地灭-诡鉴-一"]):
            self.status.skills["天绝地灭-诡鉴-一"].cast()
        if (self.status.stacks["诡鉴冥微-二"] and not self.status.stacks["诡鉴冥微-冷却-二"]
                and not self.status.intervals["天绝地灭-诡鉴-二"]):
            self.status.skills["天绝地灭-诡鉴-二"].cast()

    def __call__(self, status: Status):
        status.skills["诡鉴冥微"].activate = True
        status.skills["天绝地灭"].post_cast_effect.append(self.post_cast_effect)


TALENTS = [
    # ["血影留痕"],
    ["天风汲雨"],
    ["弩击急骤"],
    ["擘两分星", "千机之威"],
    ["流星赶月"],
    ["聚精凝神"],
    ["化血迷心"],
    ["杀机断魂"],
    ["秋风散影"],
    ["雀引彀中"],
    ["曙色催寒"],
    ["诡鉴冥微"]
]
TALENT_GAINS = {
    "血影留痕": 血影留痕(),
    "天风汲雨": 天风汲雨(),
    "弩击急骤": 弩击急骤(),
    "擘两分星": 擘两分星(),
    "千机之威": 千机之威(),
    "流星赶月": 流星赶月(),
    "聚精凝神": 聚精凝神(),
    "化血迷心": 化血迷心(),
    "杀机断魂": 杀机断魂(),
    "秋风散影": 秋风散影(),
    "雀引彀中": 雀引彀中(),
    "曙色催寒": 曙色催寒(),
    "诡鉴冥微": 诡鉴冥微()
}
