from base.buff import Buff
from base.skill import Skill
from base.status import Status


class 封侯:
    def __call__(self, status: Status):
        status.skills["穿云"].skill_damage_addition += 102 / 1024


class 扬戈:
    def __call__(self, status: Status):
        status.skills["穿云"].skill_critical_strike += 0.1
        status.skills["穿云"].skill_critical_power += 102 / 1024


class 神勇:
    def __call__(self, status: Status):
        status.skills["龙牙"].skill_critical_strike += 0.1
        status.skills["龙牙"].skill_critical_power += 102 / 1024
        status.skills["龙牙-龙血"].skill_critical_strike += 0.1
        status.skills["龙牙-龙血"].skill_critical_power += 102 / 1024


class 挫锐:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.buffs["挫锐"].trigger()

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        self.status.buffs["挫锐"].clear()

    def __call__(self, status: Status):
        status.skills["龙吟"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["穿云"].post_cast_effect.append(self.post_cast_effect_consume)


class 骁勇:
    def __call__(self, status: Status):
        status.skills["流血"].attack_power_cof_gain += 0.12


class 大漠:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.buffs["大漠"].trigger()

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        self.status.buffs["大漠"].clear()

    def __call__(self, status: Status):
        status.skills["龙吟"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["龙牙"].post_cast_effect.append(self.post_cast_effect_consume)


class 击水:
    @staticmethod
    def pre_cast_effect(self: Skill):
        if self.status.stacks[self.name] == 3:
            self.status.skills["击水"].trigger()

    def __call__(self, status: Status):
        status.skills["流血"].tick_base += 3
        status.buffs["流血"].stack_max = 3
        status.skills["流血"].pre_cast_effect.append(self.pre_cast_effect)


class 龙驭:
    @staticmethod
    def post_cast_effect(self: Skill):
        if self.status.stacks["骑御"]:
            self.status.buffs["龙驭"].trigger()

    @staticmethod
    def remove_effect(self: Buff):
        self.status.buffs["龙驭"].clear()

    def __call__(self, status: Status):
        status.skills["任驰骋"].cd_base -= 6 * 16
        for skill in ['穿云', '龙吟', '龙牙']:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect)
        status.buffs["骑御"].remove_effect.append(self.remove_effect)


class 驰骋:
    def __call__(self, status: Status):
        status.buffs["驰骋"].value = 307 / 1024
        status.skills["灭"].not_horse = True


class 牧云:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.buffs["牧云"].clear()
        self.status.buffs["牧云"].trigger()

    @staticmethod
    def post_cast_effect_add(self: Skill):
        if self.status.stacks["牧云"]:
            self.status.buffs["牧云"].add(1)

    def __call__(self, status: Status):
        status.skills["突"].cd_base += 37 * 16
        status.skills["突"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["龙牙"].post_cast_effect.append(self.post_cast_effect_add)


class 风虎:
    @staticmethod
    def increase_effect(self: Buff):
        self.status.buffs["风虎"].trigger(self.status.stacks[self.name])

    @staticmethod
    def decrease_effect(self: Buff):
        self.status.buffs["风虎"].trigger(self.status.stacks[self.name])

    def __call__(self, status: Status):
        status.buffs["战意"].increase_effect.append(self.increase_effect)
        status.buffs["战意"].decrease_effect.append(self.decrease_effect)


class 战心:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["战意"].increase(3)
        self.status.skills["流血"].cast()
        self.status.buffs["战心"].trigger()

    @staticmethod
    def pre_cast_effect(self: Skill):
        self.status.buffs["战心"].clear()

    def __call__(self, status: Status):
        status.skills["灭"].post_cast_effect.append(self.post_cast_effect)
        status.skills["流血"].pre_cast_effect.append(self.pre_cast_effect)


class 渊:
    def __call__(self, status: Status):
        status.skills["渊"].activate = True


class 夜征:
    @staticmethod
    def add_effect(self: Buff):
        self.status.buffs["夜征"].trigger()

    @staticmethod
    def remove_effect(self: Buff):
        self.status.buffs["夜征"].clear()

    def __call__(self, status: Status):
        status.buffs["激雷"].duration *= 2.5
        status.buffs["激雷"].add_effect.append(self.add_effect)
        status.buffs["激雷"].remove_effect.append(self.remove_effect)


class 龙血:
    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["流血"]:
            self.status.skills["龙牙-龙血"].cast()

    def __call__(self, status: Status):
        status.skills["龙牙"].post_hit_effect.append(self.post_hit_effect)


class 虎贲:
    @staticmethod
    def post_cast_effect(self: Skill):
        if self.roll < 0.3:
            self.status.buffs["战意"].increase(3)

    def __call__(self, status: Status):
        status.skills["龙牙"].post_cast_effect.append(self.post_cast_effect)


TALENTS = [
    ["扬戈", "封侯"],
    ["神勇", "挫锐"],
    ["大漠", "骁勇"],
    ["龙驭", "击水"],
    ["驰骋"],
    ["牧云"],
    ["风虎"],
    ["战心"],
    ["渊"],
    ["夜征"],
    ["龙血"],
    ["虎贲"]
]
TALENT_GAINS = {
    "扬戈": 扬戈(),
    "封侯": 封侯(),
    "神勇": 神勇(),
    "挫锐": 挫锐(),
    "大漠": 大漠(),
    "骁勇": 骁勇(),
    "龙驭": 龙驭(),
    "击水": 击水(),
    "驰骋": 驰骋(),
    "牧云": 牧云(),
    "风虎": 风虎(),
    "战心": 战心(),
    "渊": 渊(),
    "夜征": 夜征(),
    "龙血": 龙血(),
    "虎贲": 虎贲()
}
