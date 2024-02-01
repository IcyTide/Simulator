from base.buff import Buff
from base.skill import Skill
from base.status import Status


class 中峙:
    def __call__(self, status: Status):
        for skill in ["行云式·一", "行云式·二", "行云式·三"]:
            status.skills[skill].skill_damage_addition += 102 / 1024


class 渊冲:
    def __call__(self, status: Status):
        for skill in ["行云式·一", "行云式·二", "行云式·三"]:
            status.skills[skill].skill_critical_strike += 0.1
            status.skills[skill].skill_critical_power += 102 / 1024


class 戗风:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["戗风"].trigger()

    def __call__(self, status: Status):
        status.skills["识破"].post_cast_effect.append(self.post_cast_effect)


class 雨积:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.buffs["雨积"].trigger()

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        self.status.buffs["雨积"].clear()

    def __call__(self, status: Status):
        status.skills["留客雨"].post_cast_effect.append(self.post_cast_effect_trigger)
        for skill in ["行云式·一", "行云式·二", "行云式·三", "停云式"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_consume)


class 溃延:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.cds["决云式"] = max(0, self.status.cds["决云式"] - 13 * 16)

    def __call__(self, status: Status):
        status.buffs["身形"].duration += 5 * 16
        status.skills["识破"].post_cast_effect.append(self.post_cast_effect)


class 放皓:
    def __call__(self, status: Status):
        status.skills["沧浪三叠·一"].skill_critical_strike += 0.1
        status.skills["沧浪三叠·一"].skill_critical_power += 102 / 1024
        status.skills["沧浪三叠·二"].skill_critical_strike += 0.2
        status.skills["沧浪三叠·二"].skill_critical_power += 205 / 1024
        status.skills["沧浪三叠·三"].skill_critical_strike += 0.3
        status.skills["沧浪三叠·三"].skill_critical_power += 307 / 1024


class 电逝:
    @staticmethod
    def pre_cast_effect(self: Skill):
        if self.status.stacks["灭影追风"]:
            for _ in range(2):
                self.status.buffs["行云式"].trigger()

    def __call__(self, status: Status):
        status.buffs["灭影追风"].duration += 5 * 16
        status.skills["行云式"].pre_cast_effect.append(self.pre_cast_effect)


class 威声:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["双手持刀"].trigger()

    def __call__(self, status: Status):
        status.skills["灭影追风"].post_cast_effect.append(self.post_cast_effect)


class 观衅:
    def __call__(self, status: Status):
        status.buffs["破绽"].duration = 60 * 15


class 承磊:
    def __call__(self, status: Status):
        status.buffs["破绽"].stack_max = 6
        status.buffs["流血"].stack_max = 6


class 镇机:

    def __call__(self, status: Status):
        status.buffs["破绽"].sub_buffs.append("镇机")


class 界破:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.skills["界破"].cast()

    def __call__(self, status: Status):
        status.skills["孤锋破浪"].post_cast_effect.append(self.post_cast_effect)


class 长溯:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.buffs["长溯"].trigger()

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        self.status.buffs["长溯"].clear()

    def __call__(self, status: Status):
        status.skills["沧浪三叠"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["孤锋破浪"].post_cast_effect.append(self.post_cast_effect_consume)


class 涣衍:
    def __call__(self, status: Status):
        status.skills["流血"].tick_base += 6


class 周流:
    @staticmethod
    def post_cast_effect(self: Skill):
        if self.status.stacks["识破"]:
            self.status.buffs["锐意"].increase(15)

    def __call__(self, status: Status):
        status.skills["决云式"].post_cast_effect.append(self.post_cast_effect)


class 涤瑕:
    def __call__(self, status: Status):
        status.buffs["流血"].sub_buffs.append("涤瑕")


class 强膂:
    def __call__(self, status: Status):
        status.attribute.strength_gain += 102 / 1024


class 流岚:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        for _ in range(3):
            self.status.buffs["身形"].trigger()

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        self.status.buffs["流岚"].trigger()

    def __call__(self, status: Status):
        status.skills["游风飘踪"].cd_base += 12 * 16
        status.skills["游风飘踪"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["识破"].post_cast_effect.append(self.post_cast_effect_consume)


class 聚疏:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.cds["决云式"] = max(0, self.status.cds["决云式"] - 3 * 16)

    def __call__(self, status: Status):
        status.skills["留客雨"].post_cast_effect.append(self.post_cast_effect)


class 斩颓:
    @staticmethod
    def pre_cast_effect(self: Skill):
        self.level = self.status.stacks["破绽"]

    def __call__(self, status: Status):
        status.skills["避实击虚"].pre_cast_effect.append(self.pre_cast_effect)


class 潋风:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.buffs["潋风"].trigger()

    @staticmethod
    def post_cast_effect_1(self: Skill):
        if self.status.stacks["潋风"]:
            self.status.skills["潋风·携刃"].cast()

    @staticmethod
    def post_cast_effect_2(self: Skill):
        if self.status.stacks["潋风"]:
            self.status.skills["潋风·拓锋"].cast()

    def __call__(self, status: Status):
        status.skills["决云式"].post_cast_effect.append(self.post_cast_effect_trigger)
        for skill in ["行云式·一", "行云式·二", "行云式·三", "停云式", "决云式"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_1)
        status.skills["断云式"].post_cast_effect.append(self.post_cast_effect_2)


class 截辕:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.skills["截辕"].cast()

    def __call__(self, status: Status):
        status.skills["截辕"].post_cast_effect.append(self.post_cast_effect)


TALENTS = [
    ["渊冲", "中峙"],
    ["戗风"],
    ["溃延", "雨积"],
    ["放皓"],
    ["电逝", "威声"],
    ["承磊", "观衅"],
    ["镇机", "界破"],
    ["长溯"],
    ["涣衍", "周流"],
    ["涤瑕", "强膂"],
    ["流岚", "聚疏", "斩颓"],
    ["潋风", "截辕"]
]
TALENT_GAINS = {
    "中峙": 中峙(),
    "渊冲": 渊冲(),
    "戗风": 戗风(),
    "溃延": 溃延(),
    "雨积": 雨积(),
    "放皓": 放皓(),
    "电逝": 电逝(),
    "威声": 威声(),
    "承磊": 承磊(),
    "观衅": 观衅(),
    "镇机": 镇机(),
    "界破": 界破(),
    "长溯": 长溯(),
    "涣衍": 涣衍(),
    "周流": 周流(),
    "涤瑕": 涤瑕(),
    "强膂": 强膂(),
    "流岚": 流岚(),
    "聚疏": 聚疏(),
    "斩颓": 斩颓(),
    "潋风": 潋风(),
    "截辕": 截辕()
}
