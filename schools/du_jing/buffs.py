from base.buff import Buff, GainBuff, DotBuff, CountBuff, CDBuff, TriggerBuff, PlacementBuff, Energy, Pet
from general.buffs import 内功双会套装


class 蛊殇(内功双会套装):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛊殇"


class 蛊毒(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛊毒"

        self.duration = 120 * 16

        self.stack_max = 3


class 凤凰蛊(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "凤凰蛊"

        self.duration = 30 * 60 * 16


class 蛇影_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛇影-持续"


class 百足_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "百足-持续"


class 蟾啸_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蟾啸-持续"


class 灵蛇引(Pet):
    def __init__(self, status):
        super().__init__(status)
        self.name = "灵蛇引"


class 灵蛇献祭(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "灵蛇献祭"

        self.duration = 192

        self.value = 512 / 1024

        self.gain_attribute = "attack_power"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value


class 蝎心_持续(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蝎心-持续"


class 虫兽(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "虫兽"

        self.value = 154 / 1024

        self.gain_attribute = "attack_power"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value


class 重蛊(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "重蛊"

        self.duration = 6 * 16

        self.value = 205 / 1024

        self.gain_skills = []
        self.gain_attribute = "damage_addition"

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_damage_addition -= self.value


class 不鸣(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "不鸣"

        self.stack_max = 3

        self.sub_buffs = ["不鸣-增伤", "不鸣-攻击"]


class 不鸣_增伤(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "不鸣-增伤"

        self.stack_max = 3

        self.values = [307 / 1024, 614 / 1024, 921 / 1024]

        self.gain_skills = ["蝎心-伤害"]
        self.gain_attribute = "damage_addition"

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_damage_addition += self.values[stack - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_damage_addition -= self.values[stack - 1]


class 不鸣_攻击(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "不鸣-攻击"

        self.stack_max = 3

        self.values = [0.3, 0.6, 0.9]

        self.gain_skills = ["蝎心-持续"]
        self.gain_attribute = "attack_power"

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].attack_power_cof_gain += self.values[stack - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].attack_power_cof_gain -= self.values[stack - 1]


class 嗜蛊(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "嗜蛊"

        self.duration = 15 * 16

        self.value = 820 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.all_shield_ignore += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.all_shield_ignore -= self.value


class 曲致(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "曲致"

        self.value = 0.3

        self.gain_skills = ["灵蛇引"]
        self.gain_attribute = "critical_strike"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_critical_strike_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_critical_strike_gain -= self.value


class 轻鸣(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "轻鸣"

        self.duration = 35 * 16


class 荒息_计数(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "荒息"

        self.stack_max = 2

    def add(self):
        super().add()
        if self.status.stacks[self.name] == self.stack_max and self.status.stacks["灵蛇"]:
            self.status.skills["荒息"].cast()
            self.clear()


class 篾片蛊(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "篾片蛊"

        self.stack_max = 5


class 蛊虫狂暴(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛊虫狂暴"

        self.duration = 20 * 16

        self.sub_buffs = ["蛊虫狂暴-增伤", "蛊虫狂暴-攻击"]


class 蛊虫狂暴_增伤(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛊虫狂暴-增伤"

        self.value = 102 / 1024

        self.gain_attribute = "damage_addition"

    def add(self):
        super().add()
        self.status.attribute.extra_haste += self.value

    def remove(self):
        super().remove()
        self.status.attribute.extra_haste -= self.value

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.all_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.all_damage_addition -= self.value


class 蛊虫狂暴_攻击(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "蛊虫狂暴-攻击"

        self.value = 512 / 124

        self.gain_skills = ["灵蛇引"]
        self.gain_attribute = "attack_power"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value


class 引魂(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "引魂"

        self.duration = 10 * 16

        self.sub_buffs = ["引魂-增伤", "引魂-攻击"]


class 引魂_增伤(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "引魂-增伤"

        self.value = 102 / 1024

        self.gain_attribute = "damage_addition"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.all_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.all_damage_addition -= self.value


class 引魂_攻击(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "引魂-攻击"

        self.value = 410 / 124

        self.gain_skills = ["灵蛇引"]
        self.gain_attribute = "attack_power"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value
        

class 连缘蛊_无视(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "连缘蛊-无视"

        self.value = 819 / 1024

        self.gain_skills = ["破", "连缘蛊", "连缘蛊-额外"]

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_shield_gain -= self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_shield_gain += self.value


class 连缘蛊_增伤(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "连缘蛊-增伤"

        self.stack_max = 4

        self.values = [819 / 1024, 1638 / 1024, 2458 / 1024, 3277 / 1024]

        self.gain_skills = ["连缘蛊", "连缘蛊-额外"]
        self.gain_attribute = "damage_addition"

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_damage_addition += self.values[stack - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_damage_addition -= self.values[stack - 1]


BUFFS = [蛊殇, 蛊毒, 凤凰蛊, 蛇影_持续, 百足_持续, 蟾啸_持续, 灵蛇引, 灵蛇献祭, 蝎心_持续, 虫兽,
         重蛊, 不鸣, 不鸣_增伤, 不鸣_攻击, 嗜蛊, 曲致, 轻鸣, 荒息_计数, 篾片蛊, 蛊虫狂暴, 蛊虫狂暴_增伤, 蛊虫狂暴_攻击,
         引魂, 引魂_增伤, 引魂_攻击, 连缘蛊_无视, 连缘蛊_增伤]
