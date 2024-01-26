from base.buff import Buff
from base.skill import Skill, MagicalDamage
from base.status import Status


class 腾焰飞芒:
    def __call__(self, status: Status):
        for skill in ["烈日斩", "银月斩"]:
            status.skills[skill].skill_critical_strike += 0.1
            status.skills[skill].skill_critical_power += 102 / 1024


class 无幽不烛:
    def __call__(self, status: Status):
        for skill in ["赤日轮", "幽月轮"]:
            status.skills[skill].skill_damage_addition += 102 / 1024


class 血泪成悦:
    def __call__(self, status: Status):
        pass


class 无往不复:
    @staticmethod
    def critical_hit_effect_sun(self: Skill):
        self.status.buffs["日灵"].increase(20)

    @staticmethod
    def critical_hit_effect_moon(self: Skill):
        self.status.buffs["月灵"].increase(20)

    def __call__(self, status: Status):
        status.skills["烈日斩"].critical_hit_effect.append(self.critical_hit_effect_sun)
        status.skills["银月斩"].critical_hit_effect.append(self.critical_hit_effect_moon)


class 净身明礼:
    def __call__(self, status: Status):
        status.skills["烈日斩"].skill_damage_addition += 256 / 1024
        status.skills["银月斩"].skill_damage_addition += 256 / 1024


class 诛邪镇魔:
    @staticmethod
    def post_cast_effect_trigger_sun(self: Skill):
        if self.status.stacks["诛邪镇魔"]:
            pass
        elif self.status.stacks["魂·日"]:
            self.status.buffs["诛邪镇魔"].trigger(1)
        elif self.status.stacks["魂·月"]:
            self.status.buffs["诛邪镇魔"].trigger(2)
        else:
            self.status.buffs["魂·日"].trigger()

    @staticmethod
    def post_cast_effect_trigger_moon(self: Skill):
        if self.status.stacks["诛邪镇魔"]:
            pass
        elif self.status.stacks["魂·月"]:
            self.status.buffs["诛邪镇魔"].trigger(3)
        elif self.status.stacks["魂·日"]:
            self.status.buffs["诛邪镇魔"].trigger(4)
        else:
            self.status.buffs["魂·月"].trigger()

    @staticmethod
    def post_cast_effect_add_sun(self: Skill):
        if self.status.stacks["魂·日"]:
            self.status.buffs["诛邪镇魔"].trigger(1)
        elif self.status.stacks["魂·月"]:
            self.status.buffs["诛邪镇魔"].trigger(2)

    @staticmethod
    def post_cast_effect_add_moon(self: Skill):
        if self.status.stacks["魂·月"]:
            self.status.buffs["诛邪镇魔"].trigger(3)
        elif self.status.stacks["魂·日"]:
            self.status.buffs["诛邪镇魔"].trigger(4)

    def __call__(self, status: Status):
        for skill in ["净世破魔击·日", "净世破魔击·日·悬象"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_trigger_sun)
        for skill in ["净世破魔击·月", "净世破魔击·月·悬象"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_trigger_moon)
        for skill in ["生死劫·日", "生死劫·日·悬象"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_add_sun)
        for skill in ["生死劫·月", "生死劫·月·悬象"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_add_moon)


class 洞若观火:
    @staticmethod
    def post_cast_effect_sun(self: Skill):
        self.status.skills["洞若观火-日"].cast()

    @staticmethod
    def post_cast_effect_moon(self: Skill):
        self.status.skills["洞若观火-月"].cast()

    def __call__(self, status: Status):
        for skill in ["烈日斩", "烈日斩·悬象", "净世破魔击·日", "净世破魔击·日·悬象", "生死劫·日", "生死劫·日·悬象",
                      "悬象著明·日"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_sun)
        for skill in ["银月斩", "银月斩·悬象", "净世破魔击·月", "净世破魔击·月·悬象", "生死劫·月", "生死劫·月·悬象",
                      "悬象著明·月"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_moon)


class 无明业火:
    def __call__(self, status: Status):
        status.attribute.magical_critical_strike_gain += 0.1
        status.attribute.magical_critical_power_gain += 52 / 1024


class 明光恒照:
    @staticmethod
    def post_cast_effect_sun(self: Skill):
        self.status.buffs["明光·月"].trigger()
        self.status.buffs["明光·日"].clear()

    @staticmethod
    def post_cast_effect_moon(self: Skill):
        self.status.buffs["明光·月"].clear()
        self.status.buffs["明光·日"].trigger()

    def __call__(self, status: Status):
        for skill in ["净世破魔击·日", "生死劫·日", "悬象著明·日"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_sun)
        for skill in ["净世破魔击·月", "生死劫·月", "悬象著明·月"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_moon)


class 辉耀红尘:
    @staticmethod
    def post_cast_effect_sun(self: Skill):
        self.status.skills["灼烧"].cast()

    @staticmethod
    def post_cast_effect_moon(self: Skill):
        self.status.buffs["日灵"].increase(20)

    def __call__(self, status: Status):
        status.skills["净世破魔击·日"].post_cast_effect.append(self.post_cast_effect_sun)
        status.skills["净世破魔击·月"].post_cast_effect.append(self.post_cast_effect_moon)


class 日月同辉:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.buffs["日月同辉"].trigger()

    @staticmethod
    def post_cast_effect_count(self: Skill):
        self.status.buffs["日月灵魂"].trigger()

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        self.status.buffs["日月同辉"].consume()

    def __call__(self, status: Status):
        status.skills["暗尘弥散"].post_cast_effect.append(self.post_cast_effect_trigger)
        for skill in ["净世破魔击", "生死劫", "悬象著明"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_count)
        status.skills["驱夜断愁"].post_cast_effect.append(self.post_cast_effect_consume)


class 靡业报劫:
    @staticmethod
    def post_cast_effect_sun(self: Skill):
        self.status.skills["靡业报劫"].cast()
        self.status.skills["靡业报劫·日"].cast()

    @staticmethod
    def post_cast_effect_moon(self: Skill):
        self.status.skills["靡业报劫"].cast()
        self.status.skills["靡业报劫·月"].cast()

    @staticmethod
    def post_cast_effect_sun_shadow(self: Skill):
        self.status.skills["靡业报劫·日"].cast(2)

    @staticmethod
    def post_cast_effect_moon_shadow(self: Skill):
        self.status.skills["靡业报劫·月"].cast(2)

    def __call__(self, status: Status):
        status.skills["生死劫"].cd_base += 14 * 16
        status.skills["生死劫·日"].post_cast_effect.append(self.post_cast_effect_sun)
        status.skills["生死劫·月"].post_cast_effect.append(self.post_cast_effect_moon)
        status.skills["生死劫·日·悬象"].post_cast_effect.append(self.post_cast_effect_sun_shadow)
        status.skills["生死劫·月·悬象"].post_cast_effect.append(self.post_cast_effect_moon_shadow)


class 超凡入圣:
    @staticmethod
    def post_cast_effect_trigger(self: Skill):
        self.status.buffs["超凡入圣"].trigger()

    @staticmethod
    def post_cast_effect_consume(self: Skill):
        self.status.buffs["超凡入圣"].clear()

    def __call__(self, status: Status):
        status.skills["驱夜断愁"].post_cast_effect.append(self.post_cast_effect_trigger)
        status.skills["净世破魔击·日"].post_cast_effect.append(self.post_cast_effect_consume)
        status.skills["净世破魔击·月"].post_cast_effect.append(self.post_cast_effect_consume)


class 用晦而明:
    @staticmethod
    def add_effect(self: Buff):
        self.status.buffs["用晦而明"].trigger()

    @staticmethod
    def remove_effect(self: Buff):
        self.status.buffs["用晦而明"].clear()

    def __call__(self, status: Status):
        status.buffs["烈日"].add_effect.append(self.add_effect)
        status.buffs["烈日"].remove_effect.append(self.remove_effect)


class 天地诛戮:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["诛戮"].trigger()

    def __call__(self, status: Status):
        status.skills["驱夜断愁"].post_cast_effect.append(self.post_cast_effect)


class 净体不畏:
    @staticmethod
    def post_cast_effect_sun_1(self: Skill):
        self.status.cds["烈日斩"] = max(0, self.status.cds["烈日斩"] - 16)
        self.status.cds["银月斩"] = max(0, self.status.cds["银月斩"] - 16)
        if self.status.stacks["银月斩-持续"]:
            self.status.skills["烈日斩-外功"].cast()
            self.status.skills["净体不畏·日"].cast(1)

    @staticmethod
    def post_cast_effect_sun_shadow_1(self: Skill):
        self.status.cds["烈日斩"] = max(0, self.status.cds["烈日斩"] - 16)
        self.status.cds["银月斩"] = max(0, self.status.cds["银月斩"] - 16)
        if self.status.stacks["银月斩-持续"]:
            self.status.skills["净体不畏·日"].cast(1)

    @staticmethod
    def post_cast_effect_sun_2(self: Skill):
        if self.status.stacks["银月斩-持续"]:
            self.status.skills["净体不畏·日"].cast(2)

    @staticmethod
    def post_cast_effect_sun_3(self: Skill):
        if self.status.stacks["银月斩-持续"]:
            self.status.skills["净体不畏·日"].cast(3)

    @staticmethod
    def post_cast_effect_sun_4(self: Skill):
        if self.status.stacks["银月斩-持续"]:
            self.status.skills["净体不畏·日"].cast(4)

    @staticmethod
    def post_cast_effect_moon_1(self: Skill):
        self.status.cds["烈日斩"] = max(0, self.status.cds["烈日斩"] - 16)
        self.status.cds["银月斩"] = max(0, self.status.cds["银月斩"] - 16)
        if self.status.stacks["烈日"]:
            self.status.skills["银月斩-外功"].cast()
            self.status.skills["净体不畏·月"].cast(1)

    @staticmethod
    def post_cast_effect_moon_shadow_1(self: Skill):
        self.status.cds["烈日斩"] = max(0, self.status.cds["烈日斩"] - 16)
        self.status.cds["银月斩"] = max(0, self.status.cds["银月斩"] - 16)
        if self.status.stacks["烈日"]:
            self.status.skills["净体不畏·月"].cast(1)

    @staticmethod
    def post_cast_effect_moon_2(self: Skill):
        if self.status.stacks["烈日"]:
            self.status.skills["净体不畏·月"].cast(2)

    @staticmethod
    def post_cast_effect_moon_3(self: Skill):
        if self.status.stacks["烈日"]:
            self.status.skills["净体不畏·月"].cast(3)

    @staticmethod
    def post_cast_effect_moon_4(self: Skill):
        if self.status.stacks["烈日"]:
            self.status.skills["净体不畏·月"].cast(4)

    def __call__(self, status: Status):
        status.skills["烈日斩"].post_cast_effect.append(self.post_cast_effect_sun_1)
        status.skills["烈日斩·悬象"].post_cast_effect.append(self.post_cast_effect_sun_shadow_1)
        for skill in ["赤日轮", "赤日轮·悬象"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_sun_2)
        for skill in ["净世破魔击·日", "净世破魔击·日·悬象", "悬象著明·日"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_sun_3)
        for skill in ["生死劫·日", "生死劫·日·悬象", "诛邪镇魔-日"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_sun_4)

        status.skills["银月斩"].post_cast_effect.append(self.post_cast_effect_moon_1)
        status.skills["银月斩·悬象"].post_cast_effect.append(self.post_cast_effect_moon_shadow_1)
        for skill in ["幽月轮", "幽月轮·悬象"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_moon_2)
        for skill in ["净世破魔击·月", "净世破魔击·月·悬象", "悬象著明·月"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_moon_3)
        for skill in ["生死劫·月", "生死劫·月·悬象", "诛邪镇魔-月"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_moon_4)


class 降灵尊:
    @staticmethod
    def post_cast_effect_trigger(self: Buff):
        self.status.buffs["降灵尊"].trigger()

    @staticmethod
    def post_cast_effect_sun(self: Buff):
        if self.status.stacks["降灵尊"]:
            self.status.skills["破"].cast()
            self.status.skills["降灵尊"].cast()
            self.status.buffs["月灵"].increase(20)

    @staticmethod
    def post_cast_effect_moon(self: Buff):
        if self.status.stacks["降灵尊"]:
            self.status.skills["破"].cast()
            self.status.skills["降灵尊"].cast()
            self.status.buffs["日灵"].increase(20)

    @staticmethod
    def post_cast_effect(self: Buff):
        if self.status.stacks["降灵尊"]:
            self.status.skills["破"].cast()
            self.status.skills["降灵尊"].cast()

    def __call__(self, status: Status):
        status.skills["暗尘弥散"].post_cast_effect.append(self.post_cast_effect_trigger)
        for skill in ["生死劫·日", "生死劫·日·悬象", "净世破魔击·日", "净世破魔击·日·悬象", "悬象著明·日"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_sun)
        for skill in ["生死劫·月", "生死劫·月·悬象", "净世破魔击·月", "净世破魔击·月·悬象", "悬象著明·月"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_moon)
        status.skills["诛邪镇魔"].post_cast_effect.append(self.post_cast_effect)


class 万念俱寂:
    def __call__(self, status: Status):
        status.skills["驱夜断愁"].condition = True
        status.skills["驱夜断愁"].cd_base = 6 * 16
        status.skills["驱夜断愁"].gain = 20


class 悬象著明:
    @staticmethod
    def post_cast_effect_1(self: Skill):
        if self.status.stacks["悬象著明·日"]:
            self.status.skills["赤日轮·悬象"].cast()
        elif self.status.stacks["悬象著明·月"]:
            self.status.skills["幽月轮·悬象"].cast()

    @staticmethod
    def post_cast_effect_2(self: Skill):
        if self.status.stacks["悬象著明·日"]:
            self.status.skills["烈日斩·悬象"].cast()
        elif self.status.stacks["悬象著明·月"]:
            self.status.skills["银月斩·悬象"].cast()

    @staticmethod
    def post_cast_effect_3(self: Skill):
        if self.status.stacks["悬象著明·日"]:
            self.status.skills["净世破魔击·日·悬象"].cast()
        elif self.status.stacks["悬象著明·月"]:
            self.status.skills["净世破魔击·月·悬象"].cast()

    @staticmethod
    def post_cast_effect_4(self: Skill):
        if self.status.stacks["悬象著明·日"]:
            self.status.skills["生死劫·日·悬象"].cast()
        elif self.status.stacks["悬象著明·月"]:
            self.status.skills["生死劫·月·悬象"].cast()

    def __call__(self, status: Status):
        status.skills["悬象著明"].activate = True
        for skill in ["赤日轮", "幽月轮"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_1)
        for skill in ["烈日斩", "银月斩"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_2)
        for skill in ["净世破魔击·日", "净世破魔击·月"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_3)
        for skill in ["生死劫·日", "生死劫·月"]:
            status.skills[skill].post_cast_effect.append(self.post_cast_effect_4)


class 日月齐光:
    @staticmethod
    def post_cast_effect_sun_1(self: Skill):
        if self.status.stacks["日月齐光"]:
            if not self.status.stacks["日月齐光·净世破魔击"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·净世破魔击"].trigger()
        else:
            if self.status.stacks["日月齐光·日"]:
                pass
            elif self.status.stacks["日月齐光·月"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·净世破魔击"].trigger()
            else:
                self.status.buffs["日月齐光·日"].trigger()

    @staticmethod
    def post_cast_effect_sun_2(self: Skill):
        if self.status.stacks["日月齐光"]:
            if not self.status.stacks["日月齐光·生死劫"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·生死劫"].trigger()
        else:
            if self.status.stacks["日月齐光·日"]:
                pass
            elif self.status.stacks["日月齐光·月"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·生死劫"].trigger()
            else:
                self.status.buffs["日月齐光·日"].trigger()

    @staticmethod
    def post_cast_effect_sun_3(self: Skill):
        if self.status.stacks["日月齐光"]:
            if not self.status.stacks["日月齐光·悬象著明"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·悬象著明"].trigger()
        else:
            if self.status.stacks["日月齐光·日"]:
                pass
            elif self.status.stacks["日月齐光·月"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·悬象著明"].trigger()
            else:
                self.status.buffs["日月齐光·日"].trigger()

    @staticmethod
    def post_cast_effect_moon_1(self: Skill):
        if self.status.stacks["日月齐光"]:
            if not self.status.stacks["日月齐光·净世破魔击"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·净世破魔击"].trigger()
        else:
            if self.status.stacks["日月齐光·月"]:
                pass
            elif self.status.stacks["日月齐光·日"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·净世破魔击"].trigger()
            else:
                self.status.buffs["日月齐光·月"].trigger()

    @staticmethod
    def post_cast_effect_moon_2(self: Skill):
        if self.status.stacks["日月齐光"]:
            if not self.status.stacks["日月齐光·生死劫"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·生死劫"].trigger()
        else:
            if self.status.stacks["日月齐光·月"]:
                pass
            elif self.status.stacks["日月齐光·日"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·生死劫"].trigger()
            else:
                self.status.buffs["日月齐光·月"].trigger()

    @staticmethod
    def post_cast_effect_moon_3(self: Skill):
        if self.status.stacks["日月齐光"]:
            if not self.status.stacks["日月齐光·悬象著明"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·悬象著明"].trigger()
        else:
            if self.status.stacks["日月齐光·月"]:
                pass
            elif self.status.stacks["日月齐光·日"]:
                self.status.buffs["日月齐光"].trigger()
                self.status.buffs["日月齐光·悬象著明"].trigger()
            else:
                self.status.buffs["日月齐光·月"].trigger()

    def __call__(self, status: Status):
        status.skills["净世破魔击·日"].post_cast_effect.append(self.post_cast_effect_sun_1)
        status.skills["生死劫·日"].post_cast_effect.append(self.post_cast_effect_sun_2)
        status.skills["悬象著明·日"].post_cast_effect.append(self.post_cast_effect_sun_3)
        status.skills["净世破魔击·月"].post_cast_effect.append(self.post_cast_effect_moon_1)
        status.skills["生死劫·月"].post_cast_effect.append(self.post_cast_effect_moon_2)
        status.skills["悬象著明·月"].post_cast_effect.append(self.post_cast_effect_moon_3)


class 驱夷逐法:
    @staticmethod
    def pre_cast_effect(self: Skill):
        if self.status.stacks["日灵"] >= 60 and self.status.stacks["月灵"] >= 60:
            self.status.buffs["驱夷逐法"].trigger()

    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["驱夷逐法"].clear()

    def __call__(self, status: Status):
        for skill in ["净世破魔击·日", "净世破魔击·日", "净世破魔击·月"]:
            status.skills[skill].pre_cast_effect.append(self.pre_cast_effect)
            status.skills[skill].post_cast_effect.append(self.post_cast_effect)


TALENTS = [
    ["腾焰飞芒", "无幽不烛", "血泪成悦"],
    ["净身明礼", "无往不复"],
    ["诛邪镇魔", "洞若观火"],
    ["无明业火"],
    ["明光恒照"],
    ["日月同辉", "辉耀红尘"],
    ["靡业报劫", "超凡入圣"],
    ["用晦而明"],
    ["净体不畏", "天地诛戮"],
    ["降灵尊", "万念俱寂"],
    ["悬象著明"],
    ["日月齐光", "驱夷逐法"]
]
TALENT_GAINS = {
    "腾焰飞芒": 腾焰飞芒(),
    "无幽不烛": 无幽不烛(),
    "血泪成悦": 血泪成悦(),
    "净身明礼": 净身明礼(),
    "无往不复": 无往不复(),
    "诛邪镇魔": 诛邪镇魔(),
    "洞若观火": 洞若观火(),
    "无明业火": 无明业火(),
    "明光恒照": 明光恒照(),
    "辉耀红尘": 辉耀红尘(),
    "日月同辉": 日月同辉(),
    "靡业报劫": 靡业报劫(),
    "超凡入圣": 超凡入圣(),
    "用晦而明": 用晦而明(),
    "天地诛戮": 天地诛戮(),
    "净体不畏": 净体不畏(),
    "降灵尊": 降灵尊(),
    "万念俱寂": 万念俱寂(),
    "悬象著明": 悬象著明(),
    "日月齐光": 日月齐光(),
    "驱夷逐法": 驱夷逐法()
}
