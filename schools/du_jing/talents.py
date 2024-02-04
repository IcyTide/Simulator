from base.buff import Buff
from base.skill import Skill
from base.status import Status


class 尻尾:
    def __call__(self, status: Status):
        status.skills["蝎心-伤害"].skill_damage_addition += 102 / 1024


class 蝎毒:
    def __call__(self, status: Status):
        status.skills["蝎心"].sub_skills = ["蝎心-持续"]


class 无常:
    def __call__(self, status: Status):
        for skill in ["蝎心-伤害", "蝎心-持续"]:
            status.skills[skill].skill_critical_strike += 0.1
            status.skills[skill].skill_critical_power += 102 / 1024


class 食髓:
    @staticmethod
    def critical_hit_effect(self: Skill):
        self.status.skills["蛇影-持续"].consume()
        self.status.cds[self.name] = max(0, self.status.cds[self.name] - 96)

    def __call__(self, status: Status):
        status.skills["幻击"].critical_hit_effect.append(self.critical_hit_effect)


class 黯影:
    @staticmethod
    def pre_cast_effect(self: Skill):
        if self.status.stacks[self.name]:
            self.status.skills["黯影"].cast()

    def __call__(self, status: Status):
        for skill in ["蛇影-持续", "百足-持续", "蟾啸-持续", "蝎心-持续"]:
            status.skills[skill].pre_cast_effect.append(self.pre_cast_effect)
            status.skills[skill].attack_power_cof_gain += 0.25


class 虫兽:
    def __call__(self, status: Status):
        status.buffs["灵蛇"].sub_buffs.append("虫兽")


class 凄切:
    def __call__(self, status: Status):
        pass


class 桃僵:
    def __call__(self, status: Status):
        pass


class 蟾啸:
    def __call__(self, status: Status):
        status.skills["蟾啸"].sub_skills.append("蟾啸-伤害")


class 重蛊:
    @staticmethod
    def post_cast_effect(self: Skill):
        if self.status.stacks["蛊毒"] == 3:
            self.status.buffs["重蛊"].trigger()

    def __call__(self, status: Status):
        for skill in ["篾片蛊", "连缘蛊", "连缘蛊-额外"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect)


class 不鸣:
    @staticmethod
    def pre_cast_effect(self: Skill):
        self.status.buffs["不鸣"].trigger()

    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        if not self.status.stacks["不鸣"]:
            self.status.buffs["不鸣"].trigger(stack=2)

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        self.status.buffs["不鸣"].clear()

    def __call__(self, status: Status):
        for skill in ["蛇影", "百足", "蟾啸"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["蝎心"].pre_cast_effect.append(self.pre_cast_effect)
        status.skills["蝎心"].post_cast_effect.append(self.post_cast_effect_consume)


class 忘情:
    def __call__(self, status: Status):
        status.buffs["蛇影-持续"].stack_max = 2


class 嗜蛊:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["嗜蛊"].trigger()

    def __call__(self, status: Status):
        status.skills["蛊虫献祭"].post_cast_effect.append(self.post_cast_effect)


class 曲致:
    def __call__(self, status: Status):
        status.skills["蛇影-持续"].tick_base += 2
        status.buffs["蛇影-持续"].sub_buffs.append("曲致")


class 荒息:
    @staticmethod
    def post_cast_effect(self: Skill):
        if self.status.stacks["凤凰蛊"]:
            self.status.buffs["轻鸣"].trigger()

    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["轻鸣"]:
            self.status.buffs["荒息-计数"].trigger()

    def __call__(self, status: Status):
        status.skills["凤凰蛊"].cd_base = 120 * 16
        status.buffs["凤凰蛊"].duration = 180 * 16
        status.skills["蛊虫献祭"].post_cast_effect.append(self.post_cast_effect)
        for skill in status.skills.values():
            if skill.is_hit:
                status.skills[skill].post_hit_effect.append(self.post_hit_effect)


class 篾片蛊:
    @staticmethod
    def post_cast_effect(self: Skill):
        if self.status.stacks["篾片蛊"]:
            self.status.buffs["篾片蛊"].trigger()

    def __call__(self, status: Status):
        status.skills["篾片蛊"].activate = True
        for skill in ["蝎心", "蛇影", "百足", "蟾啸", "攻击", "幻击"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect)


class 蛊虫狂暴:
    def __call__(self, status: Status):
        status.skills["蛊虫狂暴"].activate = True


class 引魂:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["引魂"].trigger()

    def __call__(self, status: Status):
        status.skills["灵蛇引"].post_cast_effect.append(self.post_cast_effect)


class 啖灵:
    def __call__(self, status: Status):
        for skill in ["攻击", "幻击", "荒息"]:
            status.skills[skill].skill_damage_addition += 410 / 1024


class 蛇悉:
    @staticmethod
    def add_effect(self: Buff):
        self.status.skills["攻击"].interval_base /= 2

    @staticmethod
    def remove_effect(self: Buff):
        self.status.skills["攻击"].interval_base *= 2

    def __call__(self, status: Status):
        Skill.to_charging(status.skills["蛇影"])
        status.skills["蛇影"].energy = 2
        status.skills["蛇影"].interval_base = 24
        status.skills["蛇影"].cd_base = 6 * 16
        status.skills["蛇影"].sub_skills.append("蛇影-伤害")
        status.buffs["蛇影-持续"].add_effect.append(self.add_effect)
        status.buffs["蛇影-持续"].remove_effect.append(self.remove_effect)


class 连缘蛊:
    @staticmethod
    def add_effect(self: Buff):
        if self.status.stacks[self.name] == 1:
            self.status.buffs["连缘蛊-增伤"].trigger()

    @staticmethod
    def remove_effect(self: Buff):
        if not self.status.stacks[self.name]:
            self.status.buffs["连缘蛊-增伤"].consume()

    def __call__(self, status: Status):
        status.skills["连缘蛊"].activate = True
        for buff in ["蛇影-持续", "百足-持续", "蟾啸-持续", "蝎心-持续"]:
            status.buffs[buff].add_effect.append(self.add_effect)
            status.buffs[buff].remove_effect.append(self.remove_effect)


TALENTS = [
    ["蝎毒", "尻尾"],
    ["食髓", "无常"],
    ["黯影"],
    ["虫兽", "凄切"],
    ["桃僵", "蟾啸", "重蛊"],
    ["忘情", "不鸣"],
    ["嗜蛊"],
    ["曲致",],
    ["荒息"],
    ["篾片蛊", "蛊虫狂暴"],
    ["引魂", "啖灵"],
    ["连缘蛊", "蛇悉"]
]
TALENT_GAINS = {
    "蝎毒": 蝎毒(),
    "尻尾": 尻尾(),
    "食髓": 食髓(),
    "无常": 无常(),
    "黯影": 黯影(),
    "虫兽": 虫兽(),
    "凄切": 凄切(),
    "桃僵": 桃僵(),
    "蟾啸": 蟾啸(),
    "重蛊": 重蛊(),
    "忘情": 忘情(),
    "不鸣": 不鸣(),
    "嗜蛊": 嗜蛊(),
    "曲致": 曲致(),
    "荒息": 荒息(),
    "篾片蛊": 篾片蛊(),
    "蛊虫狂暴": 蛊虫狂暴(),
    "引魂": 引魂(),
    "啖灵": 啖灵(),
    "连缘蛊": 连缘蛊(),
    "蛇悉": 蛇悉()
}
