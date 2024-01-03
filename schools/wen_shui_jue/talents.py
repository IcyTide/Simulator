from base.buff import Buff
from base.skill import Skill
from base.status import Status


class 淘尽:
    def __call__(self, status: Status):
        status.skills["夕照雷峰"].skill_critical_strike += 0.1
        status.skills["夕照雷峰"].skill_critical_power += 102 / 1024


class 清风:
    def __call__(self, status: Status):
        status.skills["云飞玉皇"].skill_critical_strike += 0.1
        status.skills["云飞玉皇"].skill_critical_power += 102 / 1024
        status.skills["云飞玉皇-额外"].skill_critical_strike += 0.1
        status.skills["云飞玉皇-额外"].skill_critical_power += 102 / 1024


class 岱宗:
    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.buffs["岱宗"].trigger()
        self.status.skills["云飞玉皇·岱宗"].cast()

    def __call__(self, status: Status):
        status.skills["云飞玉皇"].post_hit_effect.append(self.post_hit_effect)


class 夜雨:
    @staticmethod
    def critical_hit_effect(self: Skill):
        self.status.buffs["夜雨"].trigger()

    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.buffs["夜雨"].clear()

    def __call__(self, status: Status):
        status.skills["夕照雷峰"].critical_hit_effect.append(self.critical_hit_effect)
        status.skills["云飞玉皇"].post_hit_effect.append(self.post_hit_effect)


class 景行:
    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.skills["破"].cast(3)

    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.skills["九溪弥烟-持续"].cast()

    def __call__(self, status: Status):
        status.skills["九溪弥烟"].cd_base = 24 * 16
        status.skills["九溪弥烟"].post_hit_effect.append(self.post_hit_effect)
        status.skills["九溪弥烟"].post_cast_effect.append(self.post_cast_effect)


class 映波锁澜:
    @staticmethod
    def gain_effect(self: Buff, level, stack):
        self.status.skills["听雷"].skill_damage_addition += 102 / 1024

    @staticmethod
    def revoke_effect(self: Buff, level, stack):
        self.status.skills["听雷"].skill_damage_addition -= 102 / 1024

    @staticmethod
    def post_hit_effect_trigger(self: Skill):
        self.status.buffs["凤鸣"].trigger()

    @staticmethod
    def post_hit_effect_consume(self: Skill):
        self.status.buffs["凤鸣"].consume()

    def __call__(self, status: Status):
        status.skills["听雷"].post_hit_effect.append(self.post_hit_effect_trigger)
        status.skills["夕照雷峰"].post_hit_effect.append(self.post_hit_effect_consume)
        status.skills["云飞玉皇"].post_hit_effect.append(self.post_hit_effect_consume)
        status.buffs["山居剑意"].gain_effect.append(self.gain_effect)
        status.buffs["山居剑意"].revoke_effect.append(self.revoke_effect)


class 造化:
    @staticmethod
    def increase_effect(self: Buff):
        if self.status.stacks[self.name] > 75:
            if not self.status.stacks["造化"] or self.status.buffs["造化"].level != 2:
                self.status.buffs["造化"].clear()
                self.status.buffs["造化"].trigger(2)
        elif self.status.stacks[self.name] > 50:
            if not self.status.stacks["造化"] or self.status.buffs["造化"].level != 1:
                self.status.buffs["造化"].clear()
                self.status.buffs["造化"].trigger(1)
        else:
            self.status.buffs["造化"].clear()

    @staticmethod
    def decrease_effect(self: Buff):
        if self.status.stacks[self.name] > 75:
            self.status.buffs["造化"].clear()
            self.status.buffs["造化"].trigger(2)
        elif self.status.stacks[self.name] > 50:
            self.status.buffs["造化"].clear()
            self.status.buffs["造化"].trigger(1)
        else:
            self.status.buffs["造化"].clear()

    def __call__(self, status: Status):
        status.buffs["剑气"].increase_effect.append(self.increase_effect)
        status.buffs["剑气"].decrease_effect.append(self.decrease_effect)


class 怜光:
    @staticmethod
    def gain_effect(self: Buff, level, stack):
        self.status.attribute.damage_addition += 102 / 1024

    @staticmethod
    def revoke_effect(self: Buff, level, stack):
        self.status.attribute.damage_addition -= 102 / 1024

    def __call__(self, status: Status):
        status.buffs["山居剑意"].gain_effect.append(self.gain_effect)
        status.buffs["山居剑意"].revoke_effect.append(self.revoke_effect)


class 层云:
    def __call__(self, status: Status):
        status.skills["风来吴山"].sub_skill = "风来吴山-持续"


class 撼岳:
    @staticmethod
    def add_effect(self: Buff):
        self.status.skills["听雷"].skill_critical_strike += 0.1

    @staticmethod
    def remove_effect(self: Buff):
        self.status.skills["听雷"].skill_critical_strike -= 0.1

    @staticmethod
    def gain_effect(self: Buff, level, stack):
        self.status.skills["听雷"].skill_critical_strike += 0.1
        self.status.skills["听雷"].skill_critical_power += 102 / 1024

    @staticmethod
    def revoke_effect(self: Buff, level, stack):
        self.status.skills["听雷"].skill_critical_strike -= 0.1
        self.status.skills["听雷"].skill_critical_power -= 102 / 1024

    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["惊雷"].trigger()

    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["惊雷"]:
            self.status.skills["惊雷"].cast()

    def __call__(self, status: Status):
        status.buffs["山居剑意"].add_effect.append(self.add_effect)
        status.buffs["山居剑意"].remove_effect.append(self.remove_effect)
        status.buffs["山居剑意"].gain_effect.append(self.gain_effect)
        status.buffs["山居剑意"].revoke_effect.append(self.revoke_effect)
        status.skills["听雷"].post_cast_effect.append(self.post_cast_effect)
        status.skills["风来吴山-持续"].post_hit_effect.append(self.post_hit_effect)
        status.skills["风来吴山-引导"].post_hit_effect.append(self.post_hit_effect)


class 雾锁:
    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.buffs["雾锁"].trigger()

    def __call__(self, status: Status):
        status.skills["夕照雷峰"].post_hit_effect.append(self.post_hit_effect)


class 碧归:
    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.buffs["碧归-计数"].trigger()
        self.status.buffs["剑气"].increase(5)

    def __call__(self, status: Status):
        status.skills["风来吴山"].cost = 0
        status.skills["风来吴山-持续"].post_hit_effect.append(self.post_hit_effect)
        status.skills["风来吴山-引导"].post_hit_effect.append(self.post_hit_effect)


class 如风:
    @staticmethod
    def add_effect(self: Buff):
        self.status.buffs["如风"].trigger()

    @staticmethod
    def remove_effect(self: Buff):
        self.status.buffs["如风"].clear()

    @staticmethod
    def critical_hit_effect(self: Skill):
        self.status.buffs["如风"].extend()

    def __call__(self, status: Status):
        status.buffs["山居剑意"].add_effect.append(self.add_effect)
        status.buffs["山居剑意"].remove_effect.append(self.remove_effect)
        for skill in status.skills.values():
            if skill.is_hit:
                skill.critical_hit_effect.append(self.critical_hit_effect)


class 飞来闻踪:
    def __call__(self, status: Status):
        status.skills["飞来闻踪"].activate = True


TALENTS = [
    ["淘尽"],
    ["清风"],
    ["岱宗", "夜雨"],
    ["景行"],
    ["造化", "映波锁澜"],
    ["怜光"],
    ["层云"],
    ["撼岳"],
    ["雾锁"],
    ["碧归"],
    ["如风"],
    ["飞来闻踪"]
]
TALENT_GAINS = {
    "淘尽": 淘尽(),
    "清风": 清风(),
    "岱宗": 岱宗(),
    "夜雨": 夜雨(),
    "景行": 景行(),
    "映波锁澜": 映波锁澜(),
    "造化": 造化(),
    "怜光": 怜光(),
    "层云": 层云(),
    "撼岳": 撼岳(),
    "雾锁": 雾锁(),
    "碧归": 碧归(),
    "如风": 如风(),
    "飞来闻踪": 飞来闻踪(),
}
