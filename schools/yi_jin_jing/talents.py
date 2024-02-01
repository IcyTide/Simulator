from base.buff import Buff
from base.skill import Skill, MagicalDamage
from base.status import Status


class 涅果:
    def __call__(self, status: Status):
        status.skills["普渡四方"].skill_damage_addition += 102 / 1024
        status.skills["普渡四方-外功"].skill_damage_addition += 102 / 1024


class 明法:
    def __call__(self, status: Status):
        status.buffs["普渡"].stack_max = 3


class 秉心:
    @staticmethod
    def post_cast_effect(self: Skill):
        buff = self.status.buffs["秉心"]
        if self.name not in buff.count_list:
            buff.count_list.append(self.name)
            buff.trigger()

    def __call__(self, status: Status):
        for skill in ("捕风式", "捉影式", "守缺式"):
            status.skills[skill].post_cast_effect.append(self.post_cast_effect)


class 幻身:
    def __call__(self, status: Status):
        status.skills["横扫六合"].attack_power_cof_gain += 1.65 * 1.05
        status.skills["横扫六合-持续"].attack_power_cof_gain += 1.65 * 1.05


class 善心:
    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.skills["横扫六合-持续"].consume(3)

    def __call__(self, status: Status):
        status.skills["韦陀献杵"].post_hit_effect.append(self.post_hit_effect)
        status.skills["拿云式"].post_hit_effect.append(self.post_hit_effect)


class 身意:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["身意"].trigger()

    def __call__(self, status: Status):
        status.skills["守缺式"].post_cast_effect.append(self.post_cast_effect)


class 纷纭:
    @staticmethod
    def post_cast_effect_1(self: Skill):
        self.status.buffs["千斤坠·无取"].trigger()

    @staticmethod
    def post_cast_effect_2(self: Skill):
        self.status.buffs["千斤坠·无取"].clear()
        self.status.buffs["千斤坠·无舍"].trigger()

    @staticmethod
    def post_cast_effect_3(self: Skill):
        self.status.buffs["千斤坠·无舍"].clear()

    def __call__(self, status: Status):
        status.skills["千斤坠"].post_cast_effect.append(self.post_cast_effect_1)
        status.skills["千斤坠·无取"].post_cast_effect.append(self.post_cast_effect_2)
        status.skills["千斤坠·无舍"].post_cast_effect.append(self.post_cast_effect_3)


class 缩地:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["缩地"].trigger()

    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["缩地"]:
            self.status.skills["缩地"].cast()

    def __call__(self, status: Status):
        for skill in ("韦陀献杵", "拿云式", "罗汉金身"):
            status.skills[skill].post_cast_effect.append(self.post_cast_effect)
        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.post_hit_effect)


class 降魔渡厄:
    @staticmethod
    def post_cast_effect_1(self: Skill):
        self.status.skills["降魔"].cast(1)

    @staticmethod
    def post_cast_effect_2(self: Skill):
        self.status.skills["降魔"].cast(2)

    def __call__(self, status: Status):
        status.skills["韦陀献杵"].post_cast_effect.append(self.post_cast_effect_1)
        status.skills["拿云式"].post_cast_effect.append(self.post_cast_effect_2)


class 系珠:
    def __call__(self, status: Status):
        Skill.to_charging(status.skills["擒龙诀"])
        status.skills["擒龙诀"].cd_base = 25 * 16
        status.skills["擒龙"].interval_list = [24] * 6


class 金刚怒目:
    @staticmethod
    def add_effect(self: Buff):
        self.status.buffs["金刚怒目"].trigger()

    @staticmethod
    def remove_effect(self: Buff):
        self.status.buffs["金刚怒目"].clear()

    def __call__(self, status: Status):
        status.buffs["罗汉金身"].add_effect.append(self.add_effect)
        status.buffs["罗汉金身"].remove_effect.append(self.remove_effect)


class 净果:
    @staticmethod
    def post_hit_effect(self: Skill):
        self.status.buffs["拿云"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_hit and isinstance(skill, MagicalDamage):
                skill.post_hit_effect.append(self.post_hit_effect)


class 三生:
    @staticmethod
    def increase_effect(self: Buff):
        self.status.buffs["三生"].trigger(stack=self.status.stacks[self.name] - self.status.stacks["禅那"])

    @staticmethod
    def decrease_effect(self: Buff):
        self.status.buffs["三生"].consume(self.status.stacks["三生"] - self.status.stacks[self.name])

    def __call__(self, status: Status):
        status.buffs["禅那"].increase_effect.append(self.increase_effect)
        status.buffs["禅那"].decrease_effect.append(self.decrease_effect)


class 我闻:
    def __call__(self, status: Status):
        status.skills["横扫六合"].cd_base -= 3 * 16

        for skill in ("横扫六合", "横扫六合-外功", "横扫六合-持续"):
            status.skills[skill].skill_critical_strike += 0.1
            status.skills[skill].skill_critical_power += 205 / 1024

        status.buffs["横扫六合-持续"].stack_max = 3


class 众嗔:
    @staticmethod
    def add_effect(self: Skill):
        self.status.buffs["众嗔"].trigger()

    @staticmethod
    def remove_effect(self: Skill):
        self.status.buffs["众嗔"].clear()

    def __call__(self, status: Status):
        status.buffs["横扫六合-持续"].add_effect.append(self.add_effect)
        status.buffs["横扫六合-持续"].remove_effect.append(self.remove_effect)


class 华香:
    def __call__(self, status: Status):
        status.skills["韦陀献杵"].skill_shield_gain = -614 / 1024
        status.skills["拿云式"].skill_shield_gain = -614 / 1024
        status.skills["守缺式"].skill_shield_gain = -614 / 1024


class 无执:
    @staticmethod
    def add_effect(self: Skill):
        for skill in ("捕风式", "捉影式", "拿云式", "守缺式"):
            self.status.skills[skill].gcd_index = 1
            self.status.skills[skill].gcd_base = 16

    @staticmethod
    def remove_effect(self: Skill):
        for skill in ("捕风式", "捉影式", "拿云式", "守缺式"):
            self.status.skills[skill].gcd_index = 0
            self.status.skills[skill].gcd_base = 24

    def __call__(self, status: Status):
        status.buffs["缴械"].add_effect.append(self.add_effect)
        status.buffs["缴械"].remove_effect.append(self.remove_effect)


class 佛果:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.skills["佛果"].cast()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)


class 金刚日轮:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.buffs["金刚日轮"].trigger()
        self.status.buffs["金刚日轮-计数"].clear()

    @staticmethod
    def post_cast_effect(self: Skill):
        if self.status.stacks["金刚日轮"]:
            self.status.skills["金刚龙爪功"].cast()

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        buff = self.status.buffs["金刚日轮-计数"]
        if self.name not in buff.count_list:
            buff.count_list.append(self.name)
            buff.trigger()

    def __call__(self, status: Status):
        status.skills["千斤坠"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["千斤坠·无取"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["千斤坠·无舍"].post_cast_effect.append(self.post_cast_effect_trigger)
        for skill in ("捕风式", "捉影式", "拿云式", "守缺式"):
            status.skills[skill].post_cast_effect.append(self.post_cast_effect)
        status.skills["横扫六合"].post_cast_effect.append(self.post_cast_effect_consume)
        status.skills["普渡四方"].post_cast_effect.append(self.post_cast_effect_consume)


class 无诤:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.skills["守缺式"].reset()
        self.status.skills["六合棍意"].cast()

    @staticmethod
    def post_cast_effect(self: Skill):
        if self.status.stacks["六合棍意"]:
            self.status.buffs["拿云"].increase(1)

    def __call__(self, status: Status):
        status.skills["横扫六合"].cd_base = 20 * 16
        status.skills["横扫六合"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["守缺式"].post_cast_effect.append(self.post_cast_effect)


TALENTS = [
    ["明法", "涅果", "秉心"],
    ["幻身", "善心"],
    ["纷纭", "身意"],
    ["缩地"],
    ["降魔渡厄"],
    ["金刚怒目", "系珠"],
    ["净果"],
    ["三生", "我闻"],
    ["众嗔"],
    ["无执", "华香"],
    ["金刚日轮", "佛果"],
    ["无诤"]
]
TALENT_GAINS = {
    "明法": 明法(),
    "涅果": 涅果(),
    "秉心": 秉心(),
    "幻身": 幻身(),
    "善心": 善心(),
    "纷纭": 纷纭(),
    "身意": 身意(),
    "缩地": 缩地(),
    "降魔渡厄": 降魔渡厄(),
    "金刚怒目": 金刚怒目(),
    "系珠": 系珠(),
    "净果": 净果(),
    "三生": 三生(),
    "我闻": 我闻(),
    "众嗔": 众嗔(),
    "无执": 无执(),
    "华香": 华香(),
    "金刚日轮": 金刚日轮(),
    "佛果": 佛果(),
    "无诤": 无诤()
}
